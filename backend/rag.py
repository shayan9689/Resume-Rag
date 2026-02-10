"""
Retrieval-Augmented Generation (RAG) module.
Enhanced to handle greetings, conversational queries, and comprehensive resume questions.
"""

import re
from typing import List
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

from backend.prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE, GREETING_PROMPT
from backend.vector_store import VectorStore


class ResumeRAG:
    """RAG system for answering questions about resume with enhanced prompt engineering."""
    
    # Patterns to detect greetings and conversational queries
    GREETING_PATTERNS = [
        r'\b(hi|hello|hey|greetings|good morning|good afternoon|good evening|hi there|hey there)\b',
        r'\b(how are you|how\'?s it going|what\'?s up|sup)\b',
        r'^\s*(hi|hello|hey|greetings)\s*[!?.]*\s*$',
    ]
    
    # Patterns for general "tell me about" queries
    GENERAL_QUERY_PATTERNS = [
        r'\b(tell me about|tell me|what can you tell me|what do you know|overview|summary)\b',
        r'\b(describe|explain|inform me about)\b',
    ]
    
    def __init__(self, vector_store: VectorStore, openai_api_key: str, model_name: str = "gpt-4o-mini", temperature: float = 0.2):
        """
        Initialize the ResumeRAG system.
        
        Args:
            vector_store: Initialized VectorStore instance
            openai_api_key: OpenAI API key for generation
            model_name: OpenAI model for generation
            temperature: Temperature for generation (lower = more factual)
        """
        self.vector_store = vector_store
        self.llm = ChatOpenAI(
            model=model_name,
            temperature=temperature,
            openai_api_key=openai_api_key
        )
    
    def _is_greeting(self, query: str) -> bool:
        """Check if the query is a greeting or conversational opener."""
        query_lower = query.lower().strip()
        
        # Check for pure greetings (just greeting words)
        if len(query_lower.split()) <= 3:
            for pattern in self.GREETING_PATTERNS:
                if re.search(pattern, query_lower, re.IGNORECASE):
                    return True
        
        # Check if it starts with a greeting
        for pattern in self.GREETING_PATTERNS[:1]:  # Just check basic greetings
            if re.match(pattern, query_lower, re.IGNORECASE):
                return True
        
        return False
    
    def _is_general_query(self, query: str) -> bool:
        """Check if the query is asking for general information."""
        query_lower = query.lower()
        for pattern in self.GENERAL_QUERY_PATTERNS:
            if re.search(pattern, query_lower, re.IGNORECASE):
                return True
        return False
    
    def _handle_greeting(self, message: str) -> str:
        """Handle greeting messages with a warm, helpful response."""
        prompt = GREETING_PROMPT.format(message=message)
        
        messages = [
            SystemMessage(content="You are a friendly, professional resume assistant."),
            HumanMessage(content=prompt)
        ]
        
        response = self.llm.invoke(messages)
        return response.content
    
    def _handle_general_query(self, query: str, k: int = 6) -> str:
        """Handle general queries by retrieving more context for comprehensive overview."""
        # Retrieve more chunks for general queries
        relevant_chunks = self.vector_store.search(query, k=k)
        context = "\n\n".join(relevant_chunks)
        
        # Enhance the query for better context
        enhanced_query = f"Provide a comprehensive overview of this resume. Include: name, current role/status, key skills, education, work experience, notable achievements, and any other relevant information. {query}"
        
        user_prompt = USER_PROMPT_TEMPLATE.format(
            context=context,
            question=enhanced_query
        )
        
        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=user_prompt)
        ]
        
        response = self.llm.invoke(messages)
        return response.content
    
    def ask(self, question: str, k: int = 4) -> str:
        """
        Answer a question about the resume using enhanced RAG with prompt engineering.
        
        Handles:
        - Greetings and conversational queries
        - General "tell me about" queries
        - Specific information queries
        - Multiple topic queries
        
        Args:
            question: User's question about the resume
            k: Number of chunks to retrieve (default, may increase for general queries)
            
        Returns:
            Answer string based on resume content or greeting response
        """
        # Normalize the question
        question = question.strip()
        
        # Handle greetings
        if self._is_greeting(question):
            return self._handle_greeting(question)
        
        # Handle general queries with more context
        if self._is_general_query(question):
            return self._handle_general_query(question, k=6)
        
        # Handle specific queries with standard RAG
        # Retrieve relevant chunks
        relevant_chunks = self.vector_store.search(question, k=k)
        
        # If no relevant chunks found, try with more chunks
        if not relevant_chunks or len(relevant_chunks) == 0:
            relevant_chunks = self.vector_store.search(question, k=k*2)
        
        # Combine chunks into context
        context = "\n\n".join(relevant_chunks) if relevant_chunks else ""
        
        # If still no context, provide helpful message
        if not context:
            return "I couldn't find relevant information in the resume for your question. Could you please rephrase your question or ask about something else? I can help with skills, education, experience, projects, certifications, or contact information."
        
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
        
        return response.content
