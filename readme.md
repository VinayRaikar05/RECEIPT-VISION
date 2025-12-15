# Receipt Vision 📄

Transform receipt images into structured JSON data using OCR and AI.

## ✨ Features

- 📤 **Upload receipts** via drag-and-drop web interface
- 🔍 **OCR extraction** using Tesseract
- 🤖 **AI parsing** with Groq API (free)
- 📥 **Download JSON** with one click
- 🎨 **Beautiful UI** - responsive and modern

## 🚀 Quick Start (Local)

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install Tesseract OCR**
   - Windows: https://github.com/UB-Mannheim/tesseract/wiki
   - macOS: `brew install tesseract`
   - Linux: `apt-get install tesseract-ocr`

3. **Configure API key**
   ```bash
   # Copy template
   cp env.example .env
   
   # Edit .env and add your GROQ_API_KEY
   # Get free key at: https://console.groq.com/
   ```

4. **Run the app**
   ```bash
   python app.py
   ```

5. **Open browser**
   ```
   http://localhost:5000
   ```

## 🆓 Free Deployment (No Credit Card)

### Option 1: ngrok (2 minutes - Instant Share)

```bash
# Terminal 1: Start app
python app.py

# Terminal 2: Expose to internet
ngrok http 5000
```
Copy the ngrok URL and share!

### Option 2: Render.com (10 minutes - Professional)

1. Push to GitHub
2. Go to https://render.com (sign up free)
3. "New" → "Web Service" → Connect GitHub
4. Select repository
5. Add environment variable: `GROQ_API_KEY=your-key`
6. Deploy!

**📖 See [DEPLOYMENT_FREE.md](DEPLOYMENT_FREE.md) for complete free deployment guide**

## 📊 Output Format

```json
{
  "total": 1500,
  "business": "Store Name",
  "items": [
    {
      "title": "Item Name",
      "quantity": 1,
      "price": 500
    }
  ],
  "transaction_timestamp": "2024-12-15T10:30:00"
}
```
*Note: Prices are in pennies (£1 = 100)*

## 📁 Project Structure

```
.
├── app.py                    # Flask web application
├── templates/
│   └── index.html           # Web interface
├── main.py                  # CLI version (legacy)
├── requirements.txt         # Dependencies
├── env.example             # Configuration template
├── render.yaml             # Render.com config
├── Dockerfile              # Docker config
└── README.md               # This file
```

## 🛠️ Tech Stack

- **Backend:** Flask, Python
- **OCR:** Tesseract
- **AI:** Groq API (free)
- **Frontend:** HTML, CSS, JavaScript

## 📝 Environment Variables

```bash
GROQ_API_KEY=your-groq-api-key-here
TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe  # Windows only
```

## 🎯 Use Cases

- Expense tracking
- Receipt digitization
- Bookkeeping automation
- Budget analysis
- Tax preparation

## 🆓 Free Deployment Options

| Platform | Time | Cost | Always On | Card Needed |
|----------|------|------|-----------|-------------|
| **ngrok** | 2 min | $0 | Yes* | ❌ |
| **Render** | 10 min | $0 | No** | ❌ |
| **Replit** | 5 min | $0 | No** | ❌ |
| **Railway** | 5 min | $0*** | Yes | ⚠️ |

*Computer must stay on  
**Sleeps after 15 min inactivity  
***Using $5 free credits/month

**Full guide:** [FREE_DEPLOYMENT_QUICK_START.txt](FREE_DEPLOYMENT_QUICK_START.txt)

## 🐛 Troubleshooting

**Tesseract not found:**
- Verify installation: `tesseract --version`
- Set path in `.env`: `TESSERACT_PATH=/path/to/tesseract`

**Module not found:**
- Install dependencies: `pip install -r requirements.txt`

**API key errors:**
- Verify key in `.env` file
- Get new key at https://console.groq.com/

## 📄 License

MIT License - Free to use and modify

## 🙏 Credits

- Tesseract OCR
- Groq API
- Flask Framework

---

**Ready to deploy?** Check [DEPLOYMENT_FREE.md](DEPLOYMENT_FREE.md) for complete free deployment instructions! 🚀




