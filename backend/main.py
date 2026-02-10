"""
FastAPI entry point for Resume RAG system.
Provides REST API endpoint for querying resume information.
"""

import os
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
    RESUME_PATH,
    FAISS_INDEX_PATH,
    FAISS_CHUNKS_PATH,
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
    API_PORT
)
from backend.loader import ResumeLoader
from backend.vector_store import VectorStore
from backend.rag import ResumeRAG

# Global variables for RAG system
vector_store: Optional[VectorStore] = None
rag_system: Optional[ResumeRAG] = None


def validate_openai_key() -> str:
    """
    Validate and retrieve OpenAI API key from configuration.
    
    Returns:
        OpenAI API key string
        
    Raises:
        ValueError: If API key is not found
    """
    if not OPENAI_API_KEY or OPENAI_API_KEY == "your_openai_api_key_here":
        raise ValueError(
            "OPENAI_API_KEY not found in environment variables. "
            "Please create a .env file in the backend directory with your OpenAI API key."
        )
    return OPENAI_API_KEY


def initialize_rag_system():
    """Initialize the RAG system on startup."""
    global vector_store, rag_system
    
    try:
        # Validate API key
        api_key = validate_openai_key()
        
        # Initialize vector store
        vector_store = VectorStore(
            openai_api_key=api_key,
            index_path=str(FAISS_INDEX_PATH),
            embedding_model=EMBEDDING_MODEL
        )
        
        # Try to load existing index
        index_loaded = vector_store.load_index()
        
        if not index_loaded:
            # Create new index from resume
            print("Index not found. Creating new index from resume...")
            
            if not RESUME_PATH.exists():
                print(f"WARNING: Resume file not found at {RESUME_PATH}")
                print("Please place your resume PDF file in the backend/data/ directory.")
                print("The server will start but /ask endpoint will not work until resume is added.")
                return
            
            loader = ResumeLoader(
                resume_path=str(RESUME_PATH),
                chunk_size=CHUNK_SIZE,
                chunk_overlap=CHUNK_OVERLAP
            )
            chunks = loader.load_resume()
            
            vector_store.create_index(chunks)
            vector_store.save_index()
            print("Index created and saved successfully.")
        else:
            print("Loaded existing index from disk.")
        
        # Initialize RAG system
        rag_system = ResumeRAG(
            vector_store=vector_store,
            openai_api_key=api_key,
            model_name=GENERATION_MODEL,
            temperature=TEMPERATURE
        )
        print("RAG system initialized successfully.")
        
    except ValueError as e:
        # API key validation error
        print(f"ERROR: {str(e)}")
        print("Server will start but /ask endpoint will not work until API key is configured.")
    except Exception as e:
        print(f"WARNING: Failed to initialize RAG system: {str(e)}")
        print("Server will start but /ask endpoint will not work until the issue is resolved.")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for FastAPI startup/shutdown events."""
    # Startup
    initialize_rag_system()
    yield
    # Shutdown (if needed in future)
    pass


# Initialize FastAPI app with lifespan
app = FastAPI(
    title=API_TITLE,
    description="Retrieval-Augmented Generation system for querying resume information",
    version=API_VERSION,
    lifespan=lifespan
)

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request/Response models
class QuestionRequest(BaseModel):
    """Request model for /ask endpoint."""
    question: str


class AnswerResponse(BaseModel):
    """Response model for /ask endpoint."""
    answer: str


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": API_TITLE,
        "version": API_VERSION,
        "endpoints": {
            "/ask": "POST - Ask questions about the resume",
            "/health": "GET - Health check",
            "/docs": "GET - Interactive API documentation (Swagger UI)"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    resume_exists = RESUME_PATH.exists()
    api_key_set = OPENAI_API_KEY and OPENAI_API_KEY != "your_openai_api_key_here"
    
    if rag_system is None or vector_store is None:
        return {
            "status": "degraded",
            "message": "RAG system not initialized",
            "resume_exists": resume_exists,
            "api_key_configured": api_key_set,
            "index_loaded": False,
            "chunks_count": 0
        }
    
    return {
        "status": "healthy",
        "index_loaded": vector_store.index is not None,
        "chunks_count": len(vector_store.chunks) if vector_store.chunks else 0
    }


@app.post("/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    """
    Answer a question about the resume.
    
    Args:
        request: QuestionRequest containing the question
        
    Returns:
        AnswerResponse with the answer
        
    Raises:
        HTTPException: If RAG system is not initialized or question is empty
    """
    if rag_system is None:
        raise HTTPException(status_code=503, detail="RAG system not initialized")
    
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
    print(f"Server will run on: http://{API_HOST}:{API_PORT}")
    print(f"API Documentation: http://{API_HOST}:{API_PORT}/docs")
    print(f"Frontend should connect to: http://localhost:{API_PORT}")
    print("=" * 60)
    print()
    
    uvicorn.run(
        app,
        host=API_HOST,
        port=API_PORT,
        reload=False,
        log_level="info"
    )
