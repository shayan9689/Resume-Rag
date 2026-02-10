"""
FAISS vector store management module.
Handles embedding generation, FAISS index creation, and persistence.
"""

import os
import pickle
from pathlib import Path
from typing import List, Optional
import faiss
import numpy as np
from langchain_openai import OpenAIEmbeddings


class VectorStore:
    """Manages FAISS vector store for resume embeddings."""
    
    def __init__(self, openai_api_key: str, index_path: str = "faiss_index", embedding_model: str = "text-embedding-3-large"):
        """
        Initialize the VectorStore.
        
        Args:
            openai_api_key: OpenAI API key for embeddings
            index_path: Path to save/load FAISS index
            embedding_model: OpenAI embedding model name
        """
        self.index_path = Path(index_path)
        self.embeddings = OpenAIEmbeddings(
            model=embedding_model,
            openai_api_key=openai_api_key
        )
        self.index: Optional[faiss.Index] = None
        self.chunks: List[str] = []
        self.embedding_dimension = None
    
    def create_index(self, chunks: List[str]) -> None:
        """
        Create FAISS index from text chunks.
        
        Args:
            chunks: List of text chunks to embed and index
        """
        if not chunks:
            raise ValueError("Cannot create index from empty chunks list")
        
        self.chunks = chunks
        
        # Generate embeddings
        print(f"Generating embeddings for {len(chunks)} chunks...")
        embeddings_list = self.embeddings.embed_documents(chunks)
        embeddings_array = np.array(embeddings_list, dtype=np.float32)
        
        # Get embedding dimension
        self.embedding_dimension = embeddings_array.shape[1]
        
        # Create FAISS index
        self.index = faiss.IndexFlatL2(self.embedding_dimension)
        self.index.add(embeddings_array)
        
        print(f"Created FAISS index with {self.index.ntotal} vectors of dimension {self.embedding_dimension}")
    
    def save_index(self) -> None:
        """Save FAISS index and chunks to disk."""
        if self.index is None:
            raise ValueError("No index to save. Create index first.")
        
        # Save FAISS index
        faiss.write_index(self.index, str(self.index_path))
        
        # Save chunks
        chunks_path = self.index_path.parent / f"{self.index_path.name}_chunks.pkl"
        with open(chunks_path, 'wb') as f:
            pickle.dump(self.chunks, f)
        
        print(f"Saved index to {self.index_path} and chunks to {chunks_path}")
    
    def load_index(self) -> bool:
        """
        Load FAISS index and chunks from disk.
        
        Returns:
            True if index was loaded successfully, False otherwise
        """
        chunks_path = self.index_path.parent / f"{self.index_path.name}_chunks.pkl"
        
        if not self.index_path.exists() or not chunks_path.exists():
            return False
        
        try:
            # Load FAISS index
            self.index = faiss.read_index(str(self.index_path))
            
            # Load chunks
            with open(chunks_path, 'rb') as f:
                self.chunks = pickle.load(f)
            
            # Get embedding dimension from loaded index
            self.embedding_dimension = self.index.d
            
            print(f"Loaded index with {self.index.ntotal} vectors and {len(self.chunks)} chunks")
            return True
        
        except Exception as e:
            print(f"Failed to load index: {str(e)}")
            return False
    
    def search(self, query: str, k: int = 4) -> List[str]:
        """
        Search for most relevant chunks.
        
        Args:
            query: Search query string
            k: Number of top results to return
            
        Returns:
            List of top k most relevant chunks
        """
        if self.index is None:
            raise ValueError("Index not initialized. Create or load index first.")
        
        # Generate query embedding
        query_embedding = self.embeddings.embed_query(query)
        query_vector = np.array([query_embedding], dtype=np.float32)
        
        # Search FAISS index
        distances, indices = self.index.search(query_vector, min(k, self.index.ntotal))
        
        # Retrieve chunks
        results = [self.chunks[idx] for idx in indices[0]]
        
        return results
