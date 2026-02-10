# 🚀 Quick Start Guide - Resume RAG System

## Backend + Frontend Setup

### Step 1: Start Backend Server

Open a terminal and run:

```bash
python -m app.main
```

Or with uvicorn:
```bash
uvicorn app.main:app --reload
```

**Backend will run on:** `http://localhost:8000`

### Step 2: Open Frontend

**Option A: Direct Browser (Easiest)**
- Navigate to `frontend/` folder
- Double-click `index.html`
- It will open in your default browser

**Option B: Local Server (Recommended)**
```bash
cd frontend
python start_server.py
# Automatically finds available port and opens browser
```

**Or manually specify port:**
```bash
cd frontend
python -m http.server 8001
# Then open http://localhost:8001
```

### Step 3: Use the Interface

1. Type your question in the text area
2. Click "Ask Question" or press `Ctrl+Enter`
3. View the answer below
4. Try the example questions for quick testing

## ✅ Verify Everything Works

### Test Backend:
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/health" -Method GET
```

### Test Frontend:
- Open `frontend/index.html` in browser
- Check if "✓ API Online" appears at the bottom
- Try asking a question

## 🎯 Example Questions to Try

- "What are your key skills?"
- "What is your educational background?"
- "What programming languages do you know?"
- "What certifications do you have?"
- "What experience do you have in AI?"

## 📁 Project Structure

```
RESUME-RAG/
├── app/              # Backend API (FastAPI)
├── frontend/         # Frontend UI (HTML/CSS/JS)
├── data/            # Resume PDF
└── .env             # API keys
```

## 🔧 Troubleshooting

**Frontend can't connect to API:**
- Make sure backend is running on port 8000
- Check browser console for CORS errors
- Verify API URL in `frontend/script.js`

**Backend not starting:**
- Check if resume PDF exists: `data/Shayan-umair-Resume.pdf`
- Verify API key in `.env` file
- Check Python dependencies: `pip install -r requirements.txt`

## 🎨 Frontend Features

- ✅ Modern, responsive design
- ✅ Real-time API status
- ✅ Loading states
- ✅ Error handling
- ✅ Example questions
- ✅ Keyboard shortcuts (Ctrl+Enter)

## 📚 Documentation

- Backend API: See `README.md`
- Frontend: See `frontend/README.md`
- API Tests: Run `.\test.ps1`

---

**Ready to go!** 🎉
