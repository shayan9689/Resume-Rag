"""
Test script for enhanced prompt engineering.
Tests various query types including greetings, general queries, and specific questions.
"""

import requests
import json
from typing import Dict, Any

API_BASE_URL = "http://localhost:8000"

def test_query(question: str, description: str) -> Dict[str, Any]:
    """Test a query and return the result."""
    try:
        response = requests.post(
            f"{API_BASE_URL}/ask",
            json={"question": question},
            timeout=30
        )
        response.raise_for_status()
        result = response.json()
        return {
            "status": "success",
            "question": question,
            "description": description,
            "answer": result.get("answer", "")
        }
    except Exception as e:
        return {
            "status": "error",
            "question": question,
            "description": description,
            "error": str(e)
        }

def print_result(result: Dict[str, Any]):
    """Print test result."""
    print(f"\n{'='*80}")
    print(f"Test: {result['description']}")
    print(f"Question: {result['question']}")
    print(f"{'='*80}")
    if result['status'] == 'success':
        print(f"Answer:\n{result['answer']}")
    else:
        print(f"Error: {result['error']}")
    print()

def main():
    """Run comprehensive tests."""
    print("="*80)
    print("PROMPT ENGINEERING TEST SUITE")
    print("Testing Enhanced Resume RAG System")
    print("="*80)
    
    test_cases = [
        # Greetings
        ("Hello", "Greeting - Basic"),
        ("Hi there!", "Greeting - With punctuation"),
        ("Good morning", "Greeting - Time-based"),
        ("Hey, how are you?", "Greeting - Conversational"),
        
        # General Queries
        ("Tell me about this resume", "General - Overview request"),
        ("What can you tell me about the candidate?", "General - Candidate overview"),
        ("Give me a summary", "General - Summary request"),
        ("Tell me everything", "General - Comprehensive request"),
        
        # Skills & Technologies
        ("What are your key skills?", "Skills - General"),
        ("What programming languages do you know?", "Skills - Programming languages"),
        ("What technologies are you familiar with?", "Skills - Technologies"),
        ("Do you know Python?", "Skills - Specific technology"),
        ("What AI/ML skills do you have?", "Skills - Domain-specific"),
        
        # Education
        ("What is your educational background?", "Education - General"),
        ("What degrees do you have?", "Education - Degrees"),
        ("Where did you study?", "Education - Institution"),
        ("What is your major?", "Education - Field of study"),
        
        # Experience
        ("What work experience do you have?", "Experience - General"),
        ("Tell me about your previous jobs", "Experience - Jobs"),
        ("What companies have you worked for?", "Experience - Companies"),
        ("How many years of experience do you have?", "Experience - Duration"),
        
        # Projects
        ("What projects have you worked on?", "Projects - General"),
        ("Tell me about your portfolio", "Projects - Portfolio"),
        ("What are your notable projects?", "Projects - Notable"),
        
        # Certifications
        ("What certifications do you have?", "Certifications - General"),
        ("What credentials do you hold?", "Certifications - Credentials"),
        ("Do you have any certifications?", "Certifications - Yes/No"),
        
        # Contact Information
        ("What is your contact information?", "Contact - General"),
        ("What is your email?", "Contact - Email"),
        ("What is your phone number?", "Contact - Phone"),
        ("Where are you located?", "Contact - Location"),
        
        # Achievements & Accomplishments
        ("What are your achievements?", "Achievements - General"),
        ("Tell me about your accomplishments", "Achievements - Accomplishments"),
        ("What awards have you received?", "Achievements - Awards"),
        
        # Specific Details
        ("What is your current role?", "Details - Current role"),
        ("What is your name?", "Details - Name"),
        ("What is your LinkedIn?", "Details - LinkedIn"),
        ("What is your GitHub?", "Details - GitHub"),
        
        # Comparisons & Analysis
        ("What is your strongest skill?", "Analysis - Strongest skill"),
        ("What makes you unique?", "Analysis - Unique qualities"),
        ("Why should we hire you?", "Analysis - Value proposition"),
        
        # Multiple Topics
        ("What are your skills and education?", "Multiple - Skills + Education"),
        ("Tell me about your experience and projects", "Multiple - Experience + Projects"),
        
        # Edge Cases
        ("", "Edge Case - Empty query"),
        ("What is your favorite color?", "Edge Case - Not in resume"),
        ("Tell me a joke", "Edge Case - Off-topic"),
    ]
    
    results = []
    for question, description in test_cases:
        if question:  # Skip empty queries
            result = test_query(question, description)
            results.append(result)
            print_result(result)
    
    # Summary
    print("\n" + "="*80)
    print("TEST SUMMARY")
    print("="*80)
    successful = sum(1 for r in results if r['status'] == 'success')
    failed = sum(1 for r in results if r['status'] == 'error')
    print(f"Total Tests: {len(results)}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print("="*80)

if __name__ == "__main__":
    main()
