# 🆓 Receipt Vision - FREE Deployment Options

## 100% Free Deployment Methods

All options below are **completely free** with no credit card required!

---

## Option 1: Render.com (⭐ BEST FREE OPTION)

### Features
- ✅ Completely FREE (no credit card required)
- ✅ Automatic HTTPS
- ✅ Auto-deploy from Git
- ✅ 750 hours/month free (enough for always-on)
- ⚠️ Sleeps after 15 min inactivity (wakes up in ~1 minute)

### Setup Steps

#### 1. Create Render Account
- Go to https://render.com
- Sign up with GitHub (free, no credit card)

#### 2. Create `render.yaml` Configuration
Already created in your project!

#### 3. Deploy
1. Push code to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Deploy to Render"
   git remote add origin your-github-repo-url
   git push -u origin main
   ```

2. On Render.com:
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select "receipt-vision" repo
   - Render auto-detects settings from `render.yaml`
   - Add environment variable: `GROQ_API_KEY=your-key`
   - Click "Create Web Service"

3. Done! Your app will be live at: `https://your-app-name.onrender.com`

**Time to deploy:** 10 minutes
**Cost:** $0 forever
**Limitations:** Sleeps after 15 min inactivity

---

## Option 2: Railway.app (Great Alternative)

### Features
- ✅ FREE with $5 monthly credit
- ✅ Automatic HTTPS
- ✅ No sleep time
- ✅ Very fast deployment
- ⚠️ Credit card required (but not charged)

### Setup Steps

1. Go to https://railway.app
2. Sign up with GitHub (free)
3. Click "New Project"
4. Choose "Deploy from GitHub repo"
5. Select your repository
6. Add environment variable: `GROQ_API_KEY=your-key`
7. Railway auto-detects Python and deploys

**Time to deploy:** 5 minutes
**Cost:** $0 (using free credits)
**Limitations:** $5 credit/month (enough for small use)

---

## Option 3: PythonAnywhere (Always Free)

### Features
- ✅ Completely FREE forever
- ✅ No credit card required
- ✅ No sleep time
- ✅ Beginner-friendly
- ⚠️ Limited to 1 web app on free tier
- ⚠️ No Tesseract on free tier (OCR won't work)

### Setup Steps

1. Sign up at https://www.pythonanywhere.com (free account)
2. Open Bash console
3. Clone your repo:
   ```bash
   git clone your-repo-url
   cd receipt-vision
   ```
4. Create virtual environment:
   ```bash
   mkvirtualenv --python=python3.10 receipt-vision
   pip install -r requirements.txt
   ```
5. Configure web app:
   - Go to "Web" tab
   - Add new web app (Flask)
   - Point to your app.py
   - Add environment variables in .env
6. Reload web app

**Time to deploy:** 15 minutes
**Cost:** $0 forever
**Limitations:** ⚠️ Tesseract not available (OCR won't work on free tier)

---

## Option 4: ngrok + Local (Completely Free)

### Features
- ✅ 100% FREE
- ✅ No limits
- ✅ Full control
- ✅ All features work (including Tesseract)
- ⚠️ Your computer must stay on
- ⚠️ URL changes each time

### Setup Steps

1. Install ngrok:
   ```bash
   # Windows (using Chocolatey)
   choco install ngrok
   
   # Or download from https://ngrok.com/download
   ```

2. Run your app:
   ```bash
   python app.py
   ```

3. In another terminal, expose to internet:
   ```bash
   ngrok http 5000
   ```

4. ngrok will give you a public URL like:
   ```
   https://abc123.ngrok.io
   ```

5. Share that URL with anyone!

**Time to deploy:** 2 minutes
**Cost:** $0 forever
**Limitations:** Computer must stay on, URL changes

---

## Option 5: Glitch (Simple & Free)

### Features
- ✅ Completely FREE
- ✅ No credit card required
- ✅ Code in browser
- ✅ Auto-deploy
- ⚠️ Sleeps after 5 min inactivity
- ⚠️ Limited resources

### Setup Steps

1. Go to https://glitch.com
2. Sign up (free)
3. Click "New Project" → "Import from GitHub"
4. Enter your repository URL
5. Add `.env` file with `GROQ_API_KEY`
6. Glitch auto-deploys

**Time to deploy:** 5 minutes
**Cost:** $0 forever
**Limitations:** Sleeps after inactivity, limited CPU

---

## Option 6: Replit (Code & Host Free)

### Features
- ✅ Completely FREE
- ✅ Code in browser
- ✅ No credit card
- ✅ Easy sharing
- ⚠️ Public code (free tier)
- ⚠️ Sleeps after inactivity

### Setup Steps

1. Go to https://replit.com
2. Sign up (free)
3. Click "Create Repl"
4. Choose "Import from GitHub"
5. Add your repository URL
6. Add `GROQ_API_KEY` to Secrets (lock icon)
7. Click "Run"

**Time to deploy:** 5 minutes
**Cost:** $0 forever
**Limitations:** Code is public, sleeps after inactivity

---

## Option 7: Vercel (Serverless Free)

### Features
- ✅ FREE forever
- ✅ Unlimited bandwidth
- ✅ Automatic HTTPS
- ✅ Fast deployments
- ⚠️ Requires serverless adaptation

### Setup Steps

1. Go to https://vercel.com
2. Sign up with GitHub (free)
3. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```
4. Deploy:
   ```bash
   vercel
   ```
5. Add environment variables on Vercel dashboard

**Time to deploy:** 10 minutes
**Cost:** $0 forever
**Limitations:** Need to adapt for serverless

---

## Comparison Table

| Platform | Cost | Setup Time | Always On? | Tesseract Works? | Credit Card? |
|----------|------|-----------|------------|------------------|--------------|
| **Render** ⭐ | $0 | 10 min | No (sleeps) | ✅ Yes | ❌ No |
| **Railway** | $0 | 5 min | Yes ($5 credit) | ✅ Yes | ✅ Yes* |
| **PythonAnywhere** | $0 | 15 min | Yes | ❌ No | ❌ No |
| **ngrok + Local** | $0 | 2 min | Yes | ✅ Yes | ❌ No |
| **Glitch** | $0 | 5 min | No (sleeps) | ⚠️ Maybe | ❌ No |
| **Replit** | $0 | 5 min | No (sleeps) | ⚠️ Maybe | ❌ No |
| **Vercel** | $0 | 10 min | Yes | ⚠️ Complex | ❌ No |

*Railway requires card but doesn't charge

---

## 🏆 RECOMMENDED: Render.com

**Why Render?**
- ✅ Truly free (no card needed)
- ✅ Tesseract OCR works
- ✅ Easy setup
- ✅ Professional features
- ⚠️ Only downside: Sleeps after 15 min (wakes in 1 min)

### Quick Render Deployment

1. Push to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Deploy"
   # Create repo on GitHub first, then:
   git remote add origin your-github-url
   git push -u origin main
   ```

2. On Render.com:
   - Sign up (free)
   - "New" → "Web Service"
   - Connect GitHub
   - Select repository
   - Set environment: `GROQ_API_KEY=your-key`
   - Deploy!

3. Access at: `https://your-app.onrender.com`

---

## Alternative: Local + ngrok (Best for Testing)

If you just want to share your app quickly:

```bash
# Terminal 1: Run app
python app.py

# Terminal 2: Expose to internet
ngrok http 5000
```

Copy the ngrok URL and share! Completely free, works perfectly.

---

## Cost Comparison After 1 Year

| Platform | Year 1 | Year 2+ | Always On? |
|----------|--------|---------|------------|
| Render | $0 | $0 | No (sleeps) |
| Railway | $0 | $0 | Yes ($5 credit) |
| ngrok + Local | $0 | $0 | Yes |
| Heroku | $60 | $60 | Yes |
| AWS | $0 | $120 | Yes |

---

## Files Needed for Free Deployment

All files are already created! You have:
- ✅ `render.yaml` (for Render)
- ✅ `Dockerfile` (for Railway)
- ✅ `requirements.txt` (for all platforms)
- ✅ `.env.example` (configuration template)

---

## Step-by-Step: Deploy to Render (FREE)

### Prerequisites
- GitHub account (free)
- Render account (free, no card)
- Your code in a GitHub repository

### Steps

1. **Create GitHub Repository**
   ```bash
   # If not already done
   git init
   git add .
   git commit -m "Initial commit"
   
   # Create repo on GitHub.com, then:
   git remote add origin https://github.com/yourusername/receipt-vision.git
   git push -u origin main
   ```

2. **Sign Up on Render**
   - Go to https://render.com
   - Click "Get Started for Free"
   - Sign in with GitHub
   - Authorize Render to access your repos

3. **Create Web Service**
   - Click "New +" button
   - Select "Web Service"
   - Connect your `receipt-vision` repository
   - Render will detect it's a Python app

4. **Configure Service**
   - Name: `receipt-vision` (or your choice)
   - Region: Choose closest to you
   - Branch: `main`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
   - Instance Type: **Free**

5. **Add Environment Variables**
   - Click "Environment" tab
   - Add: `GROQ_API_KEY` = `your-groq-api-key`
   - Add: `TESSERACT_PATH` = `/usr/bin/tesseract`

6. **Deploy**
   - Click "Create Web Service"
   - Wait 3-5 minutes for build
   - Your app will be live!

7. **Access Your App**
   - URL: `https://receipt-vision-xxxx.onrender.com`
   - Share this URL with anyone!

### Auto-Updates
Every time you push to GitHub:
```bash
git add .
git commit -m "Update app"
git push
```
Render automatically rebuilds and deploys! 🚀

---

## Troubleshooting Free Deployments

### "App is sleeping" on Render
- **Normal behavior** on free tier
- App wakes up in 30-60 seconds on first request
- Solution: Keep it awake with uptime monitor (also free)

### Tesseract not found
- Render: Already configured in `render.yaml`
- Railway: Install via Nixpacks
- Others: May need premium tier

### Out of memory
- Reduce image size before processing
- Lower max upload size in app.py
- Use smaller OCR models

---

## Keep Free App Awake

Use a free uptime monitor to ping your app every 10 minutes:

1. **UptimeRobot** (free): https://uptimerobot.com
   - Create free account
   - Add monitor with your app URL
   - Ping every 5 minutes
   - Keeps app awake!

2. **Cron-job.org** (free): https://cron-job.org
   - Create free account
   - Add cron job to ping your URL
   - Run every 10 minutes

---

## Summary

**Best FREE options ranked:**

1. **Render.com** ⭐ - Most recommended
   - Easy setup, professional, truly free
   - Downside: Sleeps after inactivity

2. **ngrok + Local** - For quick sharing
   - Instant setup, completely free
   - Downside: Computer must stay on

3. **Railway.app** - Best free features
   - No sleep, great performance
   - Downside: Requires credit card (not charged)

4. **Replit/Glitch** - Easiest for beginners
   - Code in browser, simple
   - Downside: Limited resources

---

## Ready to Deploy for Free?

Choose one:
- **Want easy & professional?** → Render.com
- **Want instant share?** → ngrok + Local
- **Want no sleep + features?** → Railway.app
- **Want super simple?** → Replit or Glitch

All instructions above. Deploy now! 🚀

**Total Cost: $0 forever** ✅
