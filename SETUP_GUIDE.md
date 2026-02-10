# 🚀 Setup Guide - Resume RAG System

## Professional Project Structure

The project is now organized into two main folders:

```
RESUME-RAG/
├── backend/          # FastAPI backend API
└── frontend/         # HTML/CSS/JavaScript frontend
```

## Step-by-Step Setup

### 1. Prerequisites

- ✅ Python 3.10 or higher
- ✅ OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- ✅ Resume PDF file

### 2. Environment Setup

```bash
# Navigate to project directory
cd Resume-RAG

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration

Create `.env` file in project root:

```env
OPENAI_API_KEY=sk-proj-your-actual-api-key-here
```

### 4. Add Resume

Place your resume PDF in `data/` directory:
```
data/Shayan-umair-Resume.pdf
```

### 5. Start Backend

```bash
# From project root directory
python -m backend.main
```

**Backend runs on:** `http://localhost:8000`

**Verify backend:**
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/health" -Method GET
```

### 6. Start Frontend

**Option A: Direct Browser (Easiest)**
```bash
# Simply open in browser:
frontend/index.html
```

**Option B: Local Server (Recommended)**
```bash
cd frontend
python -m http.server 8080
# Then open: http://localhost:8080
```

## 🎯 Quick Test

1. **Backend Health Check:**
   ```powershell
   Invoke-RestMethod -Uri "http://localhost:8000/health"
   ```

2. **Test API:**
   ```powershell
   $body = @{question="What are your key skills?"} | ConvertTo-Json
   Invoke-RestMethod -Uri "http://localhost:8000/ask" -Method POST -ContentType "application/json" -Body $body
   ```

3. **Use Frontend:**
   - Open `frontend/index.html`
   - Type a question
   - Click "Ask Question"

## 📁 Project Structure Explained

### Backend (`backend/`)
- **main.py** - FastAPI application & API endpoints
- **config.py** - All configuration settings
- **loader.py** - PDF loading & text chunking
- **vector_store.py** - FAISS vector store operations
- **rag.py** - RAG pipeline (retrieval + generation)
- **prompts.py** - Prompt templates
- **run.py** - Production server entry point

### Frontend (`frontend/`)
- **index.html** - Main HTML structure
- **styles.css** - Modern, responsive styling
- **script.js** - JavaScript logic & API calls
- **config.js** - Frontend configuration

## 🔧 Configuration Files

### Backend Configuration
Edit `backend/config.py` to modify:
- Resume file path
- FAISS index location
- OpenAI models
- Chunking parameters
- API host/port

### Frontend Configuration
Edit `frontend/config.js` to modify:
- API base URL
- UI settings
- Example questions

## 🚀 Running in Production

### Backend Production
```bash
python -m backend.run
```

Or with uvicorn:
```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000
```

### Frontend Production
- Serve `frontend/` directory with any static file server
- Update `frontend/config.js` with production API URL
- Consider using Nginx, Apache, or CDN

## 📚 Documentation

- **Main README**: `README.md`
- **Backend Docs**: `backend/README.md`
- **Frontend Docs**: `frontend/README.md`
- **Project Structure**: `PROJECT_STRUCTURE.md`
- **Quick Start**: `QUICK_START.md`

## ✅ Verification Checklist

- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] `.env` file created with OpenAI API key
- [ ] Resume PDF placed in `data/` directory
- [ ] Backend starts successfully (`python -m backend.main`)
- [ ] Health check returns "healthy" status
- [ ] Frontend opens in browser
- [ ] Frontend shows "API Online" status
- [ ] Can ask questions and receive answers

## 🐛 Troubleshooting

### Backend Issues

**Import Errors:**
- Make sure you're running from project root
- Use: `python -m backend.main` (not `python backend/main.py`)

**Resume Not Found:**
- Check file exists: `data/Shayan-umair-Resume.pdf`
- Verify path in `backend/config.py`

**API Key Error:**
- Check `.env` file exists in project root
- Verify API key is correct
- Restart backend after changing `.env`

### Frontend Issues

**Can't Connect to API:**
- Verify backend is running on port 8000
- Check `frontend/config.js` API_BASE_URL
- Check browser console for CORS errors

**CORS Errors:**
- Backend CORS is configured in `backend/main.py`
- Verify CORS_ORIGINS in `backend/config.py`

## 🎉 You're All Set!

Your Resume RAG system is now professionally organized and ready to use!
