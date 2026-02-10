"""
Production-ready server entry point.
Run with: python -m backend.run
"""

import uvicorn
from backend.config import API_HOST, API_PORT

if __name__ == "__main__":
    uvicorn.run(
        "backend.main:app",
        host=API_HOST,
        port=API_PORT,
        reload=False,  # Set to True for development
        log_level="info"
    )
