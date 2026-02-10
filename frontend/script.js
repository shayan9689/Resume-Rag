/**
 * Frontend JavaScript for Resume RAG System
 */

// API Base URL - loaded from config.js or default
const API_BASE_URL = (typeof CONFIG !== 'undefined' && CONFIG.API_BASE_URL) 
    ? CONFIG.API_BASE_URL 
    : 'http://localhost:8000';

// Check API status on load
window.addEventListener('DOMContentLoaded', () => {
    checkApiStatus();
});

async function checkApiStatus() {
    const statusElement = document.getElementById('api-status');
    try {
        const response = await fetch(`${API_BASE_URL}/health`);
        const data = await response.json();
        
        if (data.status === 'healthy') {
            statusElement.textContent = '✓ API Online - System Ready';
            statusElement.className = 'status online';
        } else {
            statusElement.textContent = '⚠ API Degraded';
            statusElement.className = 'status offline';
        }
    } catch (error) {
        statusElement.textContent = '✗ API Offline';
        statusElement.className = 'status offline';
    }
}

function setQuestion(question) {
    document.getElementById('question-input').value = question;
    document.getElementById('question-input').focus();
}

async function askQuestion() {
    const questionInput = document.getElementById('question-input');
    const question = questionInput.value.trim();
    
    // Hide previous results
    document.getElementById('answer-section').classList.add('hidden');
    document.getElementById('error-section').classList.add('hidden');
    
    // Validate input
    if (!question) {
        showError('Please enter a question.');
        return;
    }
    
    // Show loading state
    const askButton = document.getElementById('ask-button');
    const buttonText = document.getElementById('button-text');
    const loadingSpinner = document.getElementById('loading-spinner');
    
    askButton.disabled = true;
    buttonText.textContent = 'Processing...';
    loadingSpinner.classList.remove('hidden');
    
    try {
        const response = await fetch(`${API_BASE_URL}/ask`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question: question })
        });
        
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || 'Failed to get answer');
        }
        
        const data = await response.json();
        showAnswer(data.answer);
        
    } catch (error) {
        console.error('Error:', error);
        showError(error.message || 'Failed to connect to API. Make sure the server is running.');
    } finally {
        // Reset button state
        askButton.disabled = false;
        buttonText.textContent = 'Ask Question';
        loadingSpinner.classList.add('hidden');
    }
}

function showAnswer(answer) {
    const answerSection = document.getElementById('answer-section');
    const answerContent = document.getElementById('answer-content');
    
    // Format the answer (convert markdown-style formatting if needed)
    const formattedAnswer = formatAnswer(answer);
    answerContent.innerHTML = formattedAnswer;
    
    answerSection.classList.remove('hidden');
    answerSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function formatAnswer(answer) {
    // Convert markdown-style formatting to HTML
    let formatted = answer
        // Bold text (**text**)
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        // Numbered lists
        .replace(/(\d+\.\s+.*)/g, '<div style="margin: 0.5rem 0;">$1</div>')
        // Bullet points (- or •)
        .replace(/^[-•]\s+(.*)$/gm, '<div style="margin: 0.25rem 0; padding-left: 1rem;">• $1</div>')
        // Line breaks
        .replace(/\n\n/g, '</p><p>')
        .replace(/\n/g, '<br>');
    
    return `<p>${formatted}</p>`;
}

function showError(message) {
    const errorSection = document.getElementById('error-section');
    const errorMessage = document.getElementById('error-message');
    
    errorMessage.textContent = message;
    errorSection.classList.remove('hidden');
    errorSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

// Allow Enter key to submit (Ctrl+Enter or Shift+Enter)
document.getElementById('question-input').addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.shiftKey) && e.key === 'Enter') {
        askQuestion();
    }
});
