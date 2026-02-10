# Resume RAG Backend

FastAPI-based backend for the Resume RAG system.

## Structure

```
backend/
├── __init__.py          # Package initialization
├── main.py              # FastAPI application entry point
├── config.py            # Configuration settings
├── loader.py            # PDF loading and chunking
├── vector_store.py      # FAISS vector store management
├── rag.py               # RAG retrieval and generation
├── prompts.py           # System and user prompts
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (create this)
├── data/                # Data directory
│   └── Shayan-umair-Resume.pdf
├── faiss_index          # FAISS vector index (generated)
├── faiss_index_chunks.pkl  # Chunks pickle file (generated)
└── README.md           # This file
```

## Installation

```bash
# From project root
pip install -r backend/requirements.txt

# Or from backend directory
cd backend
pip install -r requirements.txt
```

## Running the Server

### Development Mode
```bash
# From project root
python -m backend.main

# Or using uvicorn
uvicorn backend.main:app --reload
```

### Production Mode
```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000
```

## API Endpoints

- `GET /` - API information
- `GET /health` - Health check endpoint
- `POST /ask` - Ask questions about the resume

## Configuration

Edit `config.py` to modify:
- Resume file path
- FAISS index location
- OpenAI models
- Chunking parameters
- API settings

## Environment Variables

Create a `.env` file in the `backend/` directory:

```env
OPENAI_API_KEY=your_api_key_here
```
