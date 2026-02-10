# 🚀 Running Resume RAG on Localhost

## Quick Start Commands

### Step 1: Start Backend Server

Open a terminal and run:

```bash
# Navigate to project root
cd Resume-RAG

# Activate virtual environment (if not already activated)
# Windows:
venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate

# Start backend server
python -m backend.main
```

**Backend will run on:** `http://localhost:8000`

---

### Step 2: Start Frontend (Choose One Method)

#### Method 1: Direct Browser (Easiest)
```bash
# Just open the HTML file directly in your browser
# Windows:
start frontend\index.html

# Mac:
open frontend/index.html

# Linux:
xdg-open frontend/index.html
```

#### Method 2: Python HTTP Server (Recommended)
```bash
# Open a NEW terminal window
cd frontend

# Start server (automatically finds available port)
python start_server.py

# Or manually specify port:
python -m http.server 8001
```

**Frontend will run on:** `http://localhost:8001` (or port shown)

---

## Complete Setup Commands

### Windows PowerShell

**Terminal 1 - Backend:**
```powershell
cd D:\AI\AI-Learning\Resume-RAG
venv\Scripts\activate
python -m backend.main
```

**Terminal 2 - Frontend:**
```powershell
cd D:\AI\AI-Learning\Resume-RAG\frontend
python start_server.py
```

### Linux/Mac Terminal

**Terminal 1 - Backend:**
```bash
cd Resume-RAG
source venv/bin/activate
python -m backend.main
```

**Terminal 2 - Frontend:**
```bash
cd Resume-RAG/frontend
python start_server.py
```

---

## Alternative Commands

### Backend Alternatives

```bash
# Using uvicorn directly
uvicorn backend.main:app --reload

# Production mode
python -m backend.run

# Custom host/port
uvicorn backend.main:app --host 0.0.0.0 --port 8000
```

### Frontend Alternatives

```bash
# Manual port selection
cd frontend
python -m http.server 3000

# Using Node.js http-server (if installed)
cd frontend
npx http-server -p 8080
```

---

## Verify Everything is Running

### Check Backend
```powershell
# PowerShell
Invoke-RestMethod -Uri "http://localhost:8000/health" -Method GET

# Or open in browser:
# http://localhost:8000/health
# http://localhost:8000/docs (API documentation)
```

### Check Frontend
- Open browser to the URL shown by `start_server.py`
- Or open `frontend/index.html` directly
- Should see "✓ API Online" at the bottom

---

## Troubleshooting

### Port Already in Use

**Backend (port 8000):**
```powershell
# Find what's using port 8000
netstat -ano | findstr :8000

# Stop the process (replace PID with actual process ID)
Stop-Process -Id <PID> -Force
```

**Frontend (port 8080 or other):**
- Use `start_server.py` - it automatically finds available port
- Or use a different port: `python -m http.server 3000`

### Backend Not Starting

```bash
# Check if virtual environment is activated
# You should see (venv) in your terminal prompt

# Verify dependencies
pip install -r requirements.txt

# Check .env file exists with API key
# Verify resume PDF exists: data/Shayan-umair-Resume.pdf
```

### Frontend Can't Connect to Backend

1. Make sure backend is running on port 8000
2. Check `frontend/config.js` - API_BASE_URL should be `http://localhost:8000`
3. Check browser console for errors (F12)
4. Verify CORS is enabled in backend (already configured)

---

## Quick Reference

| Component | Command | URL |
|-----------|---------|-----|
| **Backend** | `python -m backend.main` | http://localhost:8000 |
| **Frontend** | `python start_server.py` | http://localhost:8001+ |
| **API Docs** | (Auto) | http://localhost:8000/docs |
| **Health Check** | (Auto) | http://localhost:8000/health |

---

## One-Line Commands

### Windows PowerShell (Two Terminals)

**Terminal 1:**
```powershell
cd Resume-RAG; venv\Scripts\activate; python -m backend.main
```

**Terminal 2:**
```powershell
cd Resume-RAG\frontend; python start_server.py
```

### Linux/Mac (Two Terminals)

**Terminal 1:**
```bash
cd Resume-RAG && source venv/bin/activate && python -m backend.main
```

**Terminal 2:**
```bash
cd Resume-RAG/frontend && python start_server.py
```

---

## Testing Commands

### Test Backend API
```powershell
# Health check
Invoke-RestMethod -Uri "http://localhost:8000/health"

# Ask a question
$body = @{question="Hello"} | ConvertTo-Json
Invoke-RestMethod -Uri "http://localhost:8000/ask" -Method POST -ContentType "application/json" -Body $body
```

### Test Frontend
- Open `frontend/index.html` in browser
- Type a question and click "Ask Question"
- Check if answer appears

---

**That's it! Your Resume RAG system is now running on localhost!** 🎉
