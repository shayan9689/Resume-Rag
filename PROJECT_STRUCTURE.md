# 📁 Project Structure

## Overview

This project follows a clean, professional structure with clear separation between backend and frontend.

```
RESUME-RAG/
│
├── backend/                    # Backend API (FastAPI)
│   ├── __init__.py            # Package initialization
│   ├── main.py                # FastAPI application entry point
│   ├── config.py              # Centralized configuration
│   ├── loader.py              # PDF loading & text chunking
│   ├── vector_store.py        # FAISS vector store management
│   ├── rag.py                 # RAG retrieval & generation logic
│   ├── prompts.py             # System & user prompt templates
│   ├── run.py                 # Production server entry point
│   └── README.md              # Backend-specific documentation
│
├── frontend/                   # Frontend UI (HTML/CSS/JS)
│   ├── index.html             # Main HTML structure
│   ├── styles.css             # Styling & responsive design
│   ├── script.js              # JavaScript logic & API calls
│   ├── config.js              # Frontend configuration
│   └── README.md              # Frontend-specific documentation
│
├── data/                       # Data directory
│   └── Shayan-umair-Resume.pdf # Resume PDF file
│
├── .env                        # Environment variables (not in git)
├── .gitignore                  # Git ignore rules
├── requirements.txt            # Python dependencies
├── README.md                   # Main project documentation
├── QUICK_START.md              # Quick start guide
├── PROJECT_STRUCTURE.md        # This file
│
└── venv/                       # Virtual environment (not in git)
```

## Backend Structure

### `backend/main.py`
- FastAPI application setup
- API endpoints (`/`, `/health`, `/ask`)
- CORS middleware configuration
- Request/Response models
- Application lifecycle management

### `backend/config.py`
- Centralized configuration
- Path definitions
- Model settings
- API configuration
- Environment variable loading

### `backend/loader.py`
- PDF document loading
- Text extraction
- Recursive text splitting
- Chunk management

### `backend/vector_store.py`
- FAISS index creation
- Embedding generation
- Vector search operations
- Index persistence

### `backend/rag.py`
- RAG pipeline orchestration
- Context retrieval
- Answer generation
- LLM integration

### `backend/prompts.py`
- System prompts
- User prompt templates
- Prompt formatting

### `backend/run.py`
- Production server entry point
- Uvicorn configuration
- Server settings

## Frontend Structure

### `frontend/index.html`
- HTML structure
- UI components
- Semantic markup

### `frontend/styles.css`
- Modern CSS styling
- Responsive design
- Animations & transitions
- Color scheme & typography

### `frontend/script.js`
- API communication
- UI interactions
- Error handling
- Loading states

### `frontend/config.js`
- API endpoint configuration
- UI settings
- Example questions

## Configuration Files

### `.env`
Environment variables (not committed):
```env
OPENAI_API_KEY=your_key_here
```

### `requirements.txt`
Python package dependencies

### `.gitignore`
Files and directories to exclude from version control

## Data Files

### `data/Shayan-umair-Resume.pdf`
- Resume PDF file
- Processed by loader.py
- Indexed in FAISS

### Generated Files (not in git)
- `faiss_index` - FAISS vector index
- `faiss_index_chunks.pkl` - Chunk metadata

## Best Practices

1. **Separation of Concerns**
   - Backend and frontend are completely separate
   - Clear API contract between them
   - Independent deployment possible

2. **Configuration Management**
   - Centralized config in `backend/config.py`
   - Environment variables for secrets
   - Frontend config in `frontend/config.js`

3. **Code Organization**
   - Each module has a single responsibility
   - Clear naming conventions
   - Comprehensive docstrings

4. **Documentation**
   - README files in each directory
   - Inline code documentation
   - API documentation via FastAPI

5. **Version Control**
   - `.gitignore` excludes sensitive files
   - Clean project structure
   - No compiled files committed

## Running the Project

### Backend
```bash
# From project root
python -m backend.main
```

### Frontend
```bash
# Option 1: Direct browser
open frontend/index.html

# Option 2: Local server
cd frontend
python -m http.server 8080
```

## Deployment Considerations

### Backend
- Use `backend/run.py` for production
- Configure CORS origins properly
- Set up environment variables
- Use process manager (PM2, systemd)

### Frontend
- Can be served from any static file server
- Update `config.js` with production API URL
- Consider CDN for static assets
- Enable compression
