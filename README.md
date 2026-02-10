# Resume RAG System

A production-ready Retrieval-Augmented Generation (RAG) system for querying resume information. This system uses LangChain, OpenAI embeddings, and FAISS vector store to provide accurate, resume-based answers to questions.

## 🎯 Features

- **Strict Content Adherence**: Answers are generated strictly from resume content only
- **No Hallucinations**: System clearly states when information is not available
- **Professional Output**: Recruiter-friendly, accurate responses
- **Fast Retrieval**: FAISS vector store for efficient similarity search
- **RESTful API**: FastAPI-based endpoint for easy integration
- **Modern Frontend**: Beautiful, responsive web interface

## 🏗️ Project Structure

```
RESUME-RAG/
├── backend/                 # Backend API (FastAPI)
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── config.py            # Configuration settings
│   ├── loader.py            # PDF loading & chunking
│   ├── vector_store.py      # FAISS index management
│   ├── rag.py               # RAG retrieval & generation
│   ├── prompts.py           # System & user prompts
│   ├── run.py               # Production server entry point
│   ├── requirements.txt     # Python dependencies
│   ├── .env                 # Environment variables (create this)
│   ├── data/                # Data directory
│   │   └── Shayan-umair-Resume.pdf
│   ├── faiss_index          # FAISS vector index (generated)
│   ├── faiss_index_chunks.pkl  # Chunks pickle file (generated)
│   └── README.md            # Backend documentation
├── frontend/                # Frontend UI (HTML/CSS/JS)
│   ├── index.html           # Main HTML
│   ├── styles.css           # Styling
│   ├── script.js            # JavaScript logic
│   ├── config.js            # Frontend configuration
│   └── README.md            # Frontend documentation
├── README.md                # This file
└── venv/                    # Virtual environment
```

## 🚀 Quick Start

### 1. Prerequisites

- Python 3.10+
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### 2. Setup

```bash
# Clone or navigate to project directory
cd Resume-RAG

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r backend/requirements.txt
```

### 3. Configuration

Create a `.env` file in the `backend/` directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Place Resume

Place your resume PDF in the `backend/data/` directory:
```
backend/data/Shayan-umair-Resume.pdf
```

### 5. Run Backend

**Open Terminal 1:**
```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/Mac

# Start backend
python -m backend.main
```

✅ Backend runs on: `http://localhost:8000`

### 6. Run Frontend

**Open Terminal 2 (NEW terminal):**

**Option A: Automatic (Recommended)**
```bash
cd frontend
python start_server.py
# Automatically finds port and opens browser
```

**Option B: Direct Browser (Easiest)**
```bash
# Windows:
start frontend\index.html

# Mac/Linux:
open frontend/index.html
```

**Option C: Manual Port**
```bash
cd frontend
python -m http.server 8001
# Then open http://localhost:8001
```

### Quick Start Scripts

**Windows:**
```bash
# Double-click or run:
START.bat
```

**Linux/Mac:**
```bash
chmod +x START.sh
./START.sh
```

See `RUN_LOCALHOST.md` for detailed commands.

## 📚 Documentation

- **Backend API**: See `backend/README.md`
- **Frontend**: See `frontend/README.md`
- **Quick Start**: See `QUICK_START.md`

## 🔧 Configuration

### Backend Configuration

Edit `backend/config.py` to modify:
- Resume file path
- FAISS index location
- OpenAI models
- Chunking parameters
- API settings

### Frontend Configuration

Edit `frontend/config.js` to modify:
- API base URL
- UI settings
- Example questions

## 🧪 Testing

### Test Backend API

```powershell
# Health check
Invoke-RestMethod -Uri "http://localhost:8000/health" -Method GET

# Ask a question
$body = @{question="What are your key skills?"} | ConvertTo-Json
Invoke-RestMethod -Uri "http://localhost:8000/ask" -Method POST -ContentType "application/json" -Body $body
```

### Run Test Script

```powershell
.\test.ps1
```

## 📡 API Endpoints

- `GET /` - API information
- `GET /health` - Health check
- `POST /ask` - Ask questions about resume
- `GET /docs` - Interactive API documentation (Swagger UI)

## 🛠️ Tech Stack

### Backend
- Python 3.10+
- FastAPI
- LangChain
- OpenAI API (text-embedding-3-large, gpt-4o-mini)
- FAISS (vector store)
- python-dotenv
- PyPDF

### Frontend
- HTML5
- CSS3 (Modern, responsive design)
- Vanilla JavaScript (ES6+)
- Fetch API for HTTP requests

## 📝 System Behavior

- **Chunking**: Text split into 800-character chunks with 100-character overlap
- **Embeddings**: OpenAI `text-embedding-3-large` model
- **Generation**: GPT-4o-mini with temperature 0.2 for factual accuracy
- **Retrieval**: Top 4 most relevant chunks per query
- **Strict Prompting**: Prevents hallucinations, resume-only answers

## 🔒 Security Notes

- Never commit `.env` file (already in `.gitignore`)
- In production, update CORS origins in `backend/config.py`
- Use environment variables for sensitive data
- Consider rate limiting for production deployment

## 📄 License

This project is for personal/portfolio use.

## 🤝 Support

For issues or questions:
1. Check OpenAI API key is valid and has credits
2. Verify resume PDF is properly formatted
3. Ensure all dependencies are installed
4. Check virtual environment is activated

---

**Built with ❤️ using FastAPI, LangChain, and OpenAI**
