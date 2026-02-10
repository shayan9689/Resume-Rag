"""
Python script to test the Resume RAG API
Run with: python test_api.py
"""

import requests
import json
from typing import Dict, Any

BASE_URL = "http://localhost:8000"

def test_endpoint(method: str, endpoint: str, data: Dict[str, Any] = None) -> Dict[str, Any]:
    """Test an API endpoint and return the response."""
    url = f"{BASE_URL}{endpoint}"
    
    try:
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url, json=data)
        else:
            return {"error": f"Unsupported method: {method}"}
        
        response.raise_for_status()
        return {
            "status_code": response.status_code,
            "response": response.json()
        }
    except requests.exceptions.RequestException as e:
        return {
            "status_code": getattr(e.response, 'status_code', None),
            "error": str(e)
        }

def print_test_result(test_name: str, result: Dict[str, Any]):
    """Print test result in a formatted way."""
    print(f"\n{'='*60}")
    print(f"Test: {test_name}")
    print(f"{'='*60}")
    print(json.dumps(result, indent=2))

def main():
    """Run all API tests."""
    print("Starting Resume RAG API Tests...")
    print(f"Base URL: {BASE_URL}\n")
    
    # Test 1: Health Check
    print_test_result(
        "Health Check",
        test_endpoint("GET", "/health")
    )
    
    # Test 2: Root Endpoint
    print_test_result(
        "Root Endpoint",
        test_endpoint("GET", "/")
    )
    
    # Test Questions
    test_questions = [
        "What is your educational background?",
        "What work experience do you have?",
        "What programming languages and technologies do you know?",
        "Tell me about your projects",
        "What certifications do you have?",
        "What experience do you have in AI or machine learning?",
        "What is your contact information?",
        "What are your key skills?",
        "What is your favorite color?"  # Should return "not available"
    ]
    
    for i, question in enumerate(test_questions, 1):
        print_test_result(
            f"Question {i}: {question[:50]}...",
            test_endpoint("POST", "/ask", {"question": question})
        )
    
    print(f"\n{'='*60}")
    print("All tests completed!")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
