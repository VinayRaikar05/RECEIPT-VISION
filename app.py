import cv2
import pytesseract
from groq import Groq
import os
import sys
from dotenv import load_dotenv
from flask import Flask, render_template, request, send_file, jsonify
from werkzeug.utils import secure_filename
import json
from io import BytesIO
import tempfile

# Load environment variables from .env if present
load_dotenv()

# Configure Tesseract path
import platform
if platform.system() == 'Windows':
    default_tesseract = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
else:
    # Linux/Unix path
    default_tesseract = '/usr/bin/tesseract'

tesseract_path = os.getenv('TESSERACT_PATH') or default_tesseract
pytesseract.pytesseract.tesseract_cmd = tesseract_path

# Get API key from environment variable
api_key = os.getenv('GROQ_API_KEY')
if not api_key:
    print("Warning: GROQ_API_KEY environment variable not set.")
    print("Set it in a .env file like: GROQ_API_KEY=your-api-key-here")
    print("Get your free API key at: https://console.groq.com/")

ai_client = Groq(api_key=api_key) if api_key else None

# Initialize Flask app
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(image_path):
    """Preprocess image for OCR"""
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Could not read image file")
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    return threshold

def extract_text(image):
    """Extract text from image using Tesseract"""
    return pytesseract.image_to_string(image)

def ai_extract(text_content):
    """Extract structured JSON from OCR text using Groq AI"""
    if not ai_client:
        raise ValueError("GROQ_API_KEY not configured")
    
    prompt = """You are a receipt parser AI. I am going to provide you with text extracted from an image of a store receipt.
    I need you to return a JSON object with this structure:
    {"total", "business", "items": [{"title", "quantity", "price"}], "transaction_timestamp"}.
    Return the prices as integers that represent the number of pennies (£1 = 100) Only return the JSON object.
    Do not return anything else. Here is the text extracted from the receipt: """ + text_content

    response = ai_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response.choices[0].message.content
    # Extract JSON from response
    json_start = content.find('{')
    json_end = content.rfind('}') + 1
    
    if json_start == -1 or json_end == 0:
        raise ValueError("No JSON found in AI response")
    
    return content[json_start:json_end]

@app.route('/')
def index():
    """Render the main upload page"""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_receipt():
    """Handle receipt upload and processing"""
    try:
        # Check if file is in request
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type. Allowed: png, jpg, jpeg, gif, bmp'}), 400
        
        # Save file temporarily
        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp:
            file.save(tmp.name)
            temp_path = tmp.name
        
        try:
            # Process the receipt
            print(f"Processing receipt: {file.filename}")
            
            preprocessed_image = preprocess_image(temp_path)
            text_content = extract_text(preprocessed_image)
            
            print(f"Extracted text length: {len(text_content)}")
            
            json_data = ai_extract(text_content)
            
            # Parse to validate JSON
            parsed_data = json.loads(json_data)
            
            return jsonify({
                'success': True,
                'data': parsed_data,
                'extracted_text': text_content
            }), 200
        
        finally:
            # Clean up temporary file
            if os.path.exists(temp_path):
                os.remove(temp_path)
    
    except ValueError as e:
        return jsonify({'error': f'API not configured: {str(e)}'}), 500
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': f'Error processing receipt: {str(e)}'}), 500

@app.route('/download', methods=['POST'])
def download_json():
    """Download the processed receipt as JSON"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Create JSON file in memory
        json_data = json.dumps(data, indent=2)
        
        return send_file(
            BytesIO(json_data.encode('utf-8')),
            mimetype='application/json',
            as_attachment=True,
            download_name='receipt.json'
        )
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Get configuration from environment variables
    import os
    debug = os.getenv('FLASK_ENV') == 'development'
    
    # Support different hosting platforms
    host = os.getenv('FLASK_HOST', '0.0.0.0')  # Changed default to 0.0.0.0 for hosting
    port = int(os.getenv('PORT', os.getenv('FLASK_PORT', 5000)))  # Support PORT env var
    
    # In production, use a WSGI server like Gunicorn instead
    if debug:
        app.run(debug=True, host=host, port=port, use_reloader=False)
    else:
        print(f"Running in production mode on {host}:{port}")
        app.run(debug=False, host=host, port=port)
