# Receipt Parser

This project extracts text from an image of a store receipt and converts it into a structured JSON object using OCR and AI.

## Requirements

- Python 3.x
- OpenCV
- Pytesseract
- Groq Python client (free API)

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install Tesseract OCR (Windows):**
    - Download from: https://github.com/UB-Mannheim/tesseract/wiki
    - Run the installer (e.g., tesseract-ocr-w64-setup-5.3.x.exe)
    - During installation, note the path (usually `C:\Program Files\Tesseract-OCR`)
    - Update the path in [main.py](main.py) if installed in a different location

3. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Get a free Groq API key and set it via `.env`:
    - Sign up for free at: https://console.groq.com/
    - Copy `env.example` to `.env` and edit:
        ```
        GROQ_API_KEY=your-groq-api-key-here
        ```
    - Do not commit secrets to git. Regenerate the key if it was exposed
    )
    ```

## Usage

1. Add an image of a receipt named `receipt.jpg` to the project directory.

2. Run the script:
    ```sh
    python main.py
    ```

3. The extracted JSON data will be saved in `receipt.json`.

## Project Structure

- main.py: The main script that processes the image, extracts text, and converts it to JSON.
- requirements.txt: The list of required Python packages.
- readme.md: Project documentation.

## License

This project is licensed under the MIT License.


