"""
Configuration settings for the Resume RAG backend.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Project root directory (parent of backend/)
PROJECT_ROOT = Path(__file__).parent.parent

# Data directory
DATA_DIR = PROJECT_ROOT / "data"
RESUME_PATH = DATA_DIR / "Shayan-umair-Resume.pdf"

# FAISS index paths
FAISS_INDEX_DIR = PROJECT_ROOT
FAISS_INDEX_PATH = FAISS_INDEX_DIR / "faiss_index"
FAISS_CHUNKS_PATH = FAISS_INDEX_DIR / "faiss_index_chunks.pkl"

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
EMBEDDING_MODEL = "text-embedding-3-large"
GENERATION_MODEL = "gpt-4o-mini"
TEMPERATURE = 0.2

# RAG Configuration
CHUNK_SIZE = 800
CHUNK_OVERLAP = 100
TOP_K_CHUNKS = 4

# API Configuration
API_HOST = "0.0.0.0"
API_PORT = 8000
API_TITLE = "Resume RAG API"
API_VERSION = "1.0.0"

# CORS Configuration
CORS_ORIGINS = ["*"]  # In production, replace with specific frontend URL
