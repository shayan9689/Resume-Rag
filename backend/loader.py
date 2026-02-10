"""
Resume PDF loading and text chunking module.
Handles PDF extraction and text splitting for RAG processing.
"""

import os
from pathlib import Path
from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


class ResumeLoader:
    """Handles loading and chunking of resume PDF."""
    
    def __init__(self, resume_path: str, chunk_size: int = 800, chunk_overlap: int = 100):
        """
        Initialize the ResumeLoader.
        
        Args:
            resume_path: Path to the resume PDF file
            chunk_size: Size of each text chunk
            chunk_overlap: Overlap between chunks
        """
        self.resume_path = Path(resume_path)
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", ". ", " ", ""]
        )
    
    def load_resume(self) -> List[str]:
        """
        Load resume PDF and extract text chunks.
        
        Returns:
            List of text chunks from the resume
            
        Raises:
            FileNotFoundError: If resume PDF is not found
            Exception: If PDF loading fails
        """
        if not self.resume_path.exists():
            raise FileNotFoundError(
                f"Resume file not found at {self.resume_path}. "
                f"Please ensure the resume PDF file is placed in the data/ directory."
            )
        
        try:
            # Load PDF using PyPDFLoader
            loader = PyPDFLoader(str(self.resume_path))
            documents = loader.load()
            
            # Extract text from all pages
            full_text = "\n\n".join([doc.page_content for doc in documents])
            
            # Clean up extra whitespace
            full_text = " ".join(full_text.split())
            
            # Split into chunks
            chunks = self.text_splitter.split_text(full_text)
            
            return chunks
        
        except Exception as e:
            raise Exception(f"Failed to load resume PDF: {str(e)}")
