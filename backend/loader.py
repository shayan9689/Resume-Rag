"""
Document PDF loading and text chunking module.
Handles multiple PDFs and supports Arabic text for RAG processing.
"""

from pathlib import Path
from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


class DocumentLoader:
    """Handles loading and chunking of multiple PDF documents (supports Arabic)."""

    def __init__(self, document_paths: List[Path], chunk_size: int = 800, chunk_overlap: int = 100):
        """
        Initialize the DocumentLoader.

        Args:
            document_paths: List of paths to PDF files
            chunk_size: Size of each text chunk
            chunk_overlap: Overlap between chunks
        """
        self.document_paths = [Path(p) for p in document_paths]
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        # Separators work for both English and Arabic; keep space for Arabic word boundaries
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", ". ", " ", ""],
        )

    def load_documents(self) -> List[str]:
        """
        Load all PDFs and extract text chunks.

        Returns:
            List of text chunks from all documents

        Raises:
            FileNotFoundError: If any PDF is not found
            Exception: If PDF loading fails
        """
        all_chunks = []

        for doc_path in self.document_paths:
            if not doc_path.exists():
                raise FileNotFoundError(
                    f"Document not found at {doc_path}. "
                    f"Please ensure PDF files are in backend/data/."
                )

            try:
                loader = PyPDFLoader(str(doc_path))
                documents = loader.load()
                full_text = "\n\n".join([doc.page_content for doc in documents])
                # Normalize whitespace but preserve Arabic text as-is
                full_text = " ".join(full_text.split())
                if not full_text.strip():
                    continue
                chunks = self.text_splitter.split_text(full_text)
                all_chunks.extend(chunks)
            except Exception as e:
                raise Exception(f"Failed to load PDF {doc_path.name}: {str(e)}")

        if not all_chunks:
            raise ValueError("No text could be extracted from the provided PDFs.")

        return all_chunks
