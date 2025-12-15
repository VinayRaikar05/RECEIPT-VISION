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

# Configure Groq client with timeout to prevent hanging
import httpx
ai_client = Groq(
    api_key=api_key,
    timeout=httpx.Timeout(30.0, connect=5.0),  # 30s total, 5s connect
    max_retries=2
) if api_key else None

# Initialize Flask app
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB max file size (reduced for faster upload)
app.config['JSON_SORT_KEYS'] = False  # Faster JSON serialization
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}

# Enable response compression
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(image_path):
    """Preprocess image for OCR"""
    # Read image directly in grayscale to save memory and processing time
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError("Could not read image file")
    
    # Apply adaptive thresholding for better results on varied receipts
    threshold = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    
    return threshold

def extract_text(image):
    """Extract text from image using Tesseract"""
    # Use PSM 6 (uniform block of text) which is faster for receipts
    custom_config = r'--oem 3 --psm 6'
    return pytesseract.image_to_string(image, config=custom_config)

def ai_extract(text_content):
    """Extract structured JSON from OCR text using Groq AI"""
    if not ai_client:
        raise ValueError("GROQ_API_KEY not configured")
    
    # Truncate text if too long to speed up processing
    max_text_length = 2000
    if len(text_content) > max_text_length:
        text_content = text_content[:max_text_length]
    
    # Shortened, more efficient prompt
    prompt = f"""Extract receipt data as JSON: {{"total": int (pennies), "business": str, "items": [{{"title": str, "quantity": int, "price": int (pennies)}}], "transaction_timestamp": str}}. Return ONLY valid JSON, no explanation.\n\nReceipt text:\n{text_content}"""

    response = ai_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,  # Lower temperature for more consistent output
        max_tokens=1000   # Limit tokens to speed up response
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
    temp_path = None
    try:
        # Check if file is in request
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type. Allowed: png, jpg, jpeg, gif, bmp'}), 400
        
        # Save file temporarily with proper extension
        file_ext = file.filename.rsplit('.', 1)[1].lower()
        with tempfile.NamedTemporaryFile(suffix=f'.{file_ext}', delete=False) as tmp:
            file.save(tmp.name)
            temp_path = tmp.name
        
        # Process the receipt
        print(f"Processing receipt: {file.filename}")
        
        preprocessed_image = preprocess_image(temp_path)
        text_content = extract_text(preprocessed_image)
        
        print(f"Extracted text length: {len(text_content)}")
        
        # Only send to AI if we have meaningful text
        if len(text_content.strip()) < 10:
            return jsonify({'error': 'Could not extract enough text from image'}), 400
        
        json_data = ai_extract(text_content)
        
        # Parse to validate JSON
        parsed_data = json.loads(json_data)
        
        return jsonify({
            'success': True,
            'data': parsed_data,
            'extracted_text': text_content[:500]  # Limit text in response
        }), 200
    
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {str(e)}")
        return jsonify({'error': 'Invalid JSON from AI'}), 500
    except Exception as e:
        print(f"Error processing: {str(e)}")
        return jsonify({'error': f'Error processing receipt: {str(e)}'}), 500
    finally:
        # Clean up temporary file
        if temp_path and os.path.exists(temp_path):
            try:
                os.remove(temp_path)
            except:
                pass
    
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
