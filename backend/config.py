"""
Configuration settings for the Document RAG backend.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables: try backend/.env first, then project root .env
_backend_dir = Path(__file__).parent
_project_root = _backend_dir.parent
load_dotenv(dotenv_path=_backend_dir / ".env")
load_dotenv(dotenv_path=_project_root / ".env")  # fallback

# Project root directory (parent of backend/)
PROJECT_ROOT = Path(__file__).parent.parent

# Data directory (stored in backend directory)
DATA_DIR = Path(__file__).parent / "data"

# Document PDFs (Arabic documents)
DOCUMENT_PATHS = [
    DATA_DIR / "NDS_AR_0.pdf",
    DATA_DIR / "QNDS3_AR.pdf",
    DATA_DIR / "NDS2Final.pdf",
    DATA_DIR / "QNV2030_Arabic_v2.pdf",
]

# FAISS index paths (stored in backend directory)
FAISS_INDEX_DIR = Path(__file__).parent
FAISS_INDEX_PATH = FAISS_INDEX_DIR / "faiss_index"
FAISS_CHUNKS_PATH = FAISS_INDEX_DIR / "faiss_index_chunks.pkl"

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
EMBEDDING_MODEL = "text-embedding-3-large"
GENERATION_MODEL = "gpt-4o-mini"
TEMPERATURE = 0.2

# RAG Configuration (chunk size suitable for Arabic text)
CHUNK_SIZE = 800
CHUNK_OVERLAP = 100
TOP_K_CHUNKS = 4

# API Configuration
API_HOST = "0.0.0.0"
API_PORT = 8000
API_TITLE = "Arabic Docs RAG API"
API_VERSION = "1.0.0"

# CORS Configuration
CORS_ORIGINS = ["*"]  # In production, replace with specific frontend URL
