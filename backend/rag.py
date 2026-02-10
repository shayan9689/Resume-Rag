"""
Retrieval-Augmented Generation (RAG) module.
Focused on providing direct, precise answers.
"""

import re
from typing import List
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

from backend.prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE, GREETING_PROMPT
from backend.vector_store import VectorStore


class ResumeRAG:
    """RAG system for answering questions about resume with focused prompt engineering."""
    
    # Patterns to detect greetings
    GREETING_PATTERNS = [
        r'^\s*(hi|hello|hey|greetings|good morning|good afternoon|good evening)\s*[!?.]*\s*$',
        r'\b(hi|hello|hey)\s+(there|you)\b',
    ]
    
    def __init__(self, vector_store: VectorStore, openai_api_key: str, model_name: str = "gpt-4o-mini", temperature: float = 0.1):
        """
        Initialize the ResumeRAG system.
        
        Args:
            vector_store: Initialized VectorStore instance
            openai_api_key: OpenAI API key for generation
            model_name: OpenAI model for generation
            temperature: Temperature for generation (lower = more focused)
        """
        self.vector_store = vector_store
        self.llm = ChatOpenAI(
            model=model_name,
            temperature=temperature,  # Lower temperature for more focused answers
            openai_api_key=openai_api_key
        )
    
    def _is_greeting(self, query: str) -> bool:
        """Check if the query is a greeting."""
        query_lower = query.lower().strip()
        
        # Check for pure greetings (short messages)
        if len(query_lower.split()) <= 4:
            for pattern in self.GREETING_PATTERNS:
                if re.search(pattern, query_lower, re.IGNORECASE):
                    return True
        
        return False
    
    def _handle_greeting(self, message: str) -> str:
        """Handle greeting messages with a brief response."""
        prompt = GREETING_PROMPT.format(message=message)
        
        messages = [
            SystemMessage(content="You are a concise resume assistant."),
            HumanMessage(content=prompt)
        ]
        
        response = self.llm.invoke(messages)
        return response.content.strip()
    
    def ask(self, question: str, k: int = 4) -> str:
        """
        Answer a question about the resume using focused RAG.
        
        Args:
            question: User's question about the resume
            k: Number of chunks to retrieve
            
        Returns:
            Direct answer string based on resume content
        """
        # Normalize the question
        question = question.strip()
        
        # Handle greetings
        if self._is_greeting(question):
            return self._handle_greeting(question)
        
        # Retrieve relevant chunks
        relevant_chunks = self.vector_store.search(question, k=k)
        
        # If no relevant chunks found, try with more chunks
        if not relevant_chunks or len(relevant_chunks) == 0:
            relevant_chunks = self.vector_store.search(question, k=k*2)
        
        # Combine chunks into context
        context = "\n\n".join(relevant_chunks) if relevant_chunks else ""
        
        # If still no context, provide direct message
        if not context:
            return "This information is not available in the resume."
        
        # Format user prompt
        user_prompt = USER_PROMPT_TEMPLATE.format(
            context=context,
            question=question
        )
        
        # Generate response
        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=user_prompt)
        ]
        
        response = self.llm.invoke(messages)
        
        # Return cleaned, focused answer
        answer = response.content.strip()
        
        # Remove common filler phrases if they appear
        filler_phrases = [
            "Based on the resume,",
            "According to the resume,",
            "From the resume,",
            "The resume shows that",
            "The candidate has",
        ]
        
        for phrase in filler_phrases:
            if answer.startswith(phrase):
                answer = answer[len(phrase):].strip()
                # Capitalize first letter
                if answer:
                    answer = answer[0].upper() + answer[1:]
        
        return answer
