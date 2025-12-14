import cv2
import pytesseract
from groq import Groq
import os
import sys
from dotenv import load_dotenv

# Configure Tesseract path for Windows
# Update this path via env `TESSERACT_PATH` or fallback default
# Load environment variables from .env if present
load_dotenv()

default_tesseract = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
tesseract_path = os.getenv('TESSERACT_PATH') or default_tesseract
pytesseract.pytesseract.tesseract_cmd = tesseract_path

# Get API key from environment variable (supports .env)
api_key = os.getenv('GROQ_API_KEY')
if not api_key:
    print("Error: GROQ_API_KEY environment variable not set.")
    print("Set it in a .env file like: GROQ_API_KEY=your-api-key-here")
    print("Get your free API key at: https://console.groq.com/")
    sys.exit(1)

ai_client = Groq(api_key=api_key)

def preprocess_image(image):
    image = cv2.imread(image)
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image

    cv2.imwrite('gray_image.jpg', gray)

    # Apply thresholding
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Save the thresholded image

    cv2.imwrite('thresholded_image.jpg', threshold)

    return threshold

def extract_text(image):
    return pytesseract.image_to_string(image)

def ai_extract(text_content):
    prompt = """You are a receipt parser AI. I am going to provide you with text extracted from an image of a store receipt.
    I need you to return a JSON object with this structure:
    {“total”, “business”, “items”: [{“title”, “quantity”, “price”}], “transaction_timestamp”}.
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

    return response.choices[0].message.content[response.choices[0].message.content.find('{'):response.choices[0].message.content.rfind('}')+1]

if __name__ == '__main__':

    image_path = "receipt.jpg"
    
    if not os.path.exists(image_path):
        print(f"Error: {image_path} not found!")
        sys.exit(1)

    preprocessed_image = preprocess_image(image_path)

    text_content = extract_text(preprocessed_image)
    
    print("Extracted text from receipt:")
    print(text_content)
    print("\n" + "="*50 + "\n")

    try:
        json_data = ai_extract(text_content)
        
        with open('receipt.json', 'w') as f:
            f.write(json_data)
        
        print("Success! Receipt data saved to receipt.json")
        print(json_data)
    except Exception as e:
        print(f"Error calling Groq API: {e}")
        print("\nPlease check:")
        print("1. Your API key is valid")
        print("2. Your account is active at https://console.groq.com/")
        sys.exit(1)