"""
Retrieval-Augmented Generation (RAG) module.
- Greetings: friendly + redirect to document topics
- Query embedding/redirect: map vague queries to main context
- Answers: 100% document match, attention to detail
"""

import re
from typing import List
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

from backend.prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE, GREETING_PROMPT
from backend.vector_store import VectorStore


class ArabicRAG:
    """RAG for Arabic document Q&A with greetings, query redirect, and strict doc matching."""

    # English greeting patterns
    GREETING_PATTERNS_EN = [
        r"^\s*(hi|hello|hey|greetings|good morning|good afternoon|good evening|howdy)\s*[!?.]*\s*$",
        r"^\s*(hi|hello|hey)\s+(there|you)\s*[!?.]*\s*$",
        r"^\s*how\s+are\s+you\s*[!?.]*\s*$",
        r"^\s*what'?s\s+up\s*[!?.]*\s*$",
    ]
    # Arabic greeting patterns
    GREETING_PATTERNS_AR = [
        r"^\s*مرحبا\s*[!?.]*\s*$",
        r"^\s*أهلا\s*[!?.]*\s*$",
        r"^\s*السلام\s+عليكم\s*[!?.]*\s*$",
        r"^\s*اهلين\s*[!?.]*\s*$",
        r"^\s*هلا\s*[!?.]*\s*$",
        r"^\s*كيف\s+حالك\s*[!?.]*\s*$",
    ]

    def __init__(
        self,
        vector_store: VectorStore,
        openai_api_key: str,
        model_name: str = "gpt-4o-mini",
        temperature: float = 0.1,
    ):
        self.vector_store = vector_store
        self.llm = ChatOpenAI(
            model=model_name,
            temperature=temperature,
            openai_api_key=openai_api_key,
        )

    def _is_greeting(self, query: str) -> bool:
        """Detect greetings in English or Arabic."""
        q = query.strip()
        if not q or len(q) > 120:
            return False
        # English
        for p in self.GREETING_PATTERNS_EN:
            if re.search(p, q, re.IGNORECASE):
                return True
        # Arabic
        for p in self.GREETING_PATTERNS_AR:
            if re.search(p, q):
                return True
        # Short generic (e.g. "hey" only)
        if len(q.split()) <= 3 and re.search(r"^(hi|hello|hey|مرحبا|أهلا|هلا|اهلين)\s*[!?.]*$", q, re.IGNORECASE):
            return True
        return False

    def _handle_greeting(self, message: str) -> str:
        """Friendly greeting + redirect to document topics."""
        prompt = GREETING_PROMPT.format(message=message)
        messages = [
            SystemMessage(content="You are a friendly document assistant. Respond warmly then redirect to document topics in the user's language."),
            HumanMessage(content=prompt),
        ]
        response = self.llm.invoke(messages)
        return response.content.strip()

    def ask(self, question: str, k: int = 4) -> str:
        """
        Answer with greetings handled, query redirect when helpful, 100% doc match.
        """
        question = question.strip()
        if not question:
            return "Please ask a question about the documents."

        # 1. Greetings: friendly response + redirect to main topic
        if self._is_greeting(question):
            return self._handle_greeting(question)

        # 2. Retrieve context
        relevant_chunks = self.vector_store.search(question, k=k)
        if not relevant_chunks:
            relevant_chunks = self.vector_store.search(question, k=k * 2)

        context = "\n\n".join(relevant_chunks) if relevant_chunks else ""

        if not context:
            return (
                "This information is not in the provided documents."
                if not re.search(r"[\u0600-\u06FF]", question)
                else "هذه المعلومة غير واردة في المستندات المعطاة."
            )

        # 3. Generate answer: prompt handles redirect to main topic + 100% doc match
        user_prompt = USER_PROMPT_TEMPLATE.format(context=context, question=question)
        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=user_prompt),
        ]
        response = self.llm.invoke(messages)
        answer = response.content.strip()

        # Remove filler prefixes if present
        filler_en = [
            "Based on the documents,",
            "According to the documents,",
            "From the documents,",
            "The documents state that",
            "The documents show that",
        ]
        filler_ar = ["وفقاً للمستندات،", "بناءً على الوثائق،", "من الوثائق،"]
        for phrase in filler_en + filler_ar:
            if answer.startswith(phrase):
                answer = answer[len(phrase) :].strip()
                if answer:
                    answer = answer[0].upper() + answer[1:] if answer[0].isalpha() else answer
                break

        return answer
