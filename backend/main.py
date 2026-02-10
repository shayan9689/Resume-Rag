"""
FastAPI entry point for Arabic Docs RAG.
REST API for Q&A over Arabic/English documents.
"""

import sys
from pathlib import Path

# Add parent directory to path to allow imports when running directly
backend_dir = Path(__file__).parent
project_root = backend_dir.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from contextlib import asynccontextmanager
from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.config import (
    DOCUMENT_PATHS,
    FAISS_INDEX_PATH,
    OPENAI_API_KEY,
    EMBEDDING_MODEL,
    GENERATION_MODEL,
    TEMPERATURE,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    TOP_K_CHUNKS,
    API_TITLE,
    API_VERSION,
    CORS_ORIGINS,
    API_HOST,
    API_PORT,
)
from backend.loader import DocumentLoader
from backend.vector_store import VectorStore
from backend.rag import ArabicRAG

# Global variables for RAG system
vector_store: Optional[VectorStore] = None
rag_system: Optional[ArabicRAG] = None
_init_error: Optional[str] = None  # Reason RAG failed to start (for /health and 503)


def validate_openai_key() -> str:
    if not OPENAI_API_KEY or OPENAI_API_KEY == "your_openai_api_key_here":
        raise ValueError(
            "OPENAI_API_KEY not found in environment variables. "
            "Please create a .env file in the backend directory with your OpenAI API key."
        )
    return OPENAI_API_KEY


def documents_exist() -> bool:
    """Check if at least one configured document exists."""
    return any(p.exists() for p in DOCUMENT_PATHS)


def initialize_rag_system():
    """Initialize the RAG system on startup."""
    global vector_store, rag_system, _init_error
    _init_error = None

    try:
        api_key = validate_openai_key()

        vector_store = VectorStore(
            openai_api_key=api_key,
            index_path=str(FAISS_INDEX_PATH),
            embedding_model=EMBEDDING_MODEL,
        )

        index_loaded = vector_store.load_index()

        if not index_loaded:
            print("Index not found. Creating new index from documents...")

            if not documents_exist():
                _init_error = "No document PDFs found in backend/data/. Add NDS_AR_0.pdf, QNDS3_AR.pdf, NDS2Final.pdf, QNV2030_Arabic_v2.pdf"
                print("WARNING: No document PDFs found in backend/data/.")
                print("Expected: NDS_AR_0.pdf, QNDS3_AR.pdf, NDS2Final.pdf, QNV2030_Arabic_v2.pdf")
                print("Server will start but /ask will return 503 until documents are added.")
                return

            loader = DocumentLoader(
                document_paths=DOCUMENT_PATHS,
                chunk_size=CHUNK_SIZE,
                chunk_overlap=CHUNK_OVERLAP,
            )
            chunks = loader.load_documents()
            print(f"Loaded {len(chunks)} chunks from {len(DOCUMENT_PATHS)} documents.")

            vector_store.create_index(chunks)
            vector_store.save_index()
            print("Index created and saved successfully.")
        else:
            print("Loaded existing index from disk.")

        rag_system = ArabicRAG(
            vector_store=vector_store,
            openai_api_key=api_key,
            model_name=GENERATION_MODEL,
            temperature=TEMPERATURE,
        )
        print("RAG system initialized successfully.")

    except ValueError as e:
        _init_error = str(e)
        print(f"ERROR: {_init_error}")
        print("Server will start but /ask will return 503 until API key is set in backend/.env")
    except Exception as e:
        import traceback
        _init_error = str(e)
        print(f"WARNING: Failed to initialize RAG system: {_init_error}")
        traceback.print_exc()
        print("Server will start but /ask will return 503. Fix the error above and restart.")


@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_rag_system()
    yield


app = FastAPI(
    title=API_TITLE,
    description="Arabic Docs RAG — Q&A over Arabic/English documents",
    version=API_VERSION,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QuestionRequest(BaseModel):
    question: str


class AnswerResponse(BaseModel):
    answer: str


@app.get("/")
async def root():
    return {
        "message": API_TITLE,
        "version": API_VERSION,
        "endpoints": {
            "/ask": "POST - Ask questions about the documents",
            "/health": "GET - Health check",
            "/docs": "GET - Interactive API documentation (Swagger UI)",
        },
    }


@app.get("/health")
async def health_check():
    docs_exist = documents_exist()
    api_key_set = OPENAI_API_KEY and OPENAI_API_KEY != "your_openai_api_key_here"

    if rag_system is None or vector_store is None:
        return {
            "status": "degraded",
            "message": "RAG system not initialized",
            "init_error": _init_error,
            "documents_available": docs_exist,
            "api_key_configured": api_key_set,
            "index_loaded": False,
            "chunks_count": 0,
        }

    return {
        "status": "healthy",
        "index_loaded": vector_store.index is not None,
        "chunks_count": len(vector_store.chunks) if vector_store.chunks else 0,
    }


@app.post("/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    if rag_system is None:
        detail = "RAG system not initialized. Check server logs and ensure backend/.env has OPENAI_API_KEY and documents exist in backend/data/."
        if _init_error:
            detail += f" Error: {_init_error}"
        raise HTTPException(status_code=503, detail=detail)

    if not request.question or not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    try:
        answer = rag_system.ask(request.question, k=TOP_K_CHUNKS)
        return AnswerResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing question: {str(e)}")


if __name__ == "__main__":
    import uvicorn

    print("=" * 60)
    print(f"Starting {API_TITLE} v{API_VERSION}")
    print(f"Server: http://{API_HOST}:{API_PORT}")
    print(f"Docs: http://{API_HOST}:{API_PORT}/docs")
    print("=" * 60)

    uvicorn.run(app, host=API_HOST, port=API_PORT, reload=False, log_level="info")
