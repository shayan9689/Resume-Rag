import React, { useState, useEffect } from 'react';
import QuestionInput from './components/QuestionInput';
import AnswerDisplay from './components/AnswerDisplay';
import ExampleQuestions from './components/ExampleQuestions';
import ApiStatus from './components/ApiStatus';

const API_BASE_URL = 'http://localhost:8000';

const appStyles = {
  minHeight: '100vh',
  display: 'flex',
  flexDirection: 'column',
  background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
};

const headerStyles = {
  background: 'linear-gradient(135deg, #1a202c 0%, #2d3748 100%)',
  color: '#ffffff',
  padding: '3rem 1.5rem',
  textAlign: 'center',
  boxShadow: '0 10px 30px rgba(0, 0, 0, 0.3)',
  position: 'relative',
  overflow: 'hidden',
};

const headerOverlay = {
  position: 'absolute',
  top: 0,
  left: 0,
  right: 0,
  bottom: 0,
  background: 'linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%)',
  pointerEvents: 'none',
};

const titleStyles = {
  fontSize: 'clamp(1.75rem, 4vw, 2.5rem)',
  fontWeight: '800',
  marginBottom: '0.75rem',
  color: '#ffffff',
  textShadow: '0 2px 10px rgba(0, 0, 0, 0.3)',
  letterSpacing: '-0.02em',
  position: 'relative',
  zIndex: 1,
};

const subtitleStyles = {
  fontSize: 'clamp(0.9rem, 2vw, 1.1rem)',
  opacity: 0.9,
  color: '#e2e8f0',
  fontWeight: '400',
  position: 'relative',
  zIndex: 1,
};

const mainStyles = {
  flex: 1,
  maxWidth: '1000px',
  width: '100%',
  margin: '0 auto',
  padding: '2.5rem 1.5rem',
  animation: 'fadeIn 0.6s ease-out',
};

const errorSectionStyles = {
  background: 'linear-gradient(135deg, #fee2e2 0%, #fecaca 100%)',
  border: '2px solid #ef4444',
  borderRadius: '12px',
  padding: '1.25rem 1.5rem',
  margin: '1.5rem 0',
  color: '#991b1b',
  boxShadow: '0 4px 12px rgba(239, 68, 68, 0.2)',
  animation: 'slideIn 0.3s ease-out',
};

const errorTitleStyles = {
  fontSize: '1.1rem',
  fontWeight: '700',
  marginBottom: '0.5rem',
  color: '#991b1b',
};

const footerStyles = {
  background: 'linear-gradient(135deg, #1a202c 0%, #2d3748 100%)',
  color: '#ffffff',
  padding: '2rem 1.5rem',
  textAlign: 'center',
  marginTop: 'auto',
  boxShadow: '0 -5px 20px rgba(0, 0, 0, 0.2)',
};

const footerTextStyles = {
  margin: '0.5rem 0',
  fontSize: '0.95rem',
  opacity: 0.9,
};

function App() {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [apiStatus, setApiStatus] = useState('checking');

  useEffect(() => {
    checkApiStatus();
    const interval = setInterval(checkApiStatus, 30000);
    return () => clearInterval(interval);
  }, []);

  const checkApiStatus = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/health`);
      if (response.ok) {
        setApiStatus('online');
      } else {
        setApiStatus('offline');
      }
    } catch (err) {
      setApiStatus('offline');
    }
  };

  const askQuestion = async () => {
    if (!question.trim()) {
      setError('Please enter a question');
      return;
    }

    setLoading(true);
    setError(null);
    setAnswer('');

    try {
      const response = await fetch(`${API_BASE_URL}/ask`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question: question.trim() }),
      });

      if (!response.ok) {
        throw new Error(`API error: ${response.status}`);
      }

      const data = await response.json();
      setAnswer(data.answer);
      setQuestion('');
    } catch (err) {
      setError(err.message || 'Failed to get answer. Please check if the backend server is running.');
    } finally {
      setLoading(false);
    }
  };

  const handleExampleClick = (exampleQuestion) => {
    setQuestion(exampleQuestion);
    setError(null);
    setAnswer('');
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && e.ctrlKey) {
      askQuestion();
    }
  };

  return (
    <div style={appStyles}>
      <header style={headerStyles}>
        <div style={headerOverlay}></div>
        <h1 style={titleStyles}>📄 Resume RAG System</h1>
        <p style={subtitleStyles}>Ask questions about the resume using AI-powered retrieval</p>
      </header>

      <main style={mainStyles}>
        <QuestionInput
          question={question}
          setQuestion={setQuestion}
          onAsk={askQuestion}
          loading={loading}
          onKeyPress={handleKeyPress}
        />

        {error && (
          <div style={errorSectionStyles}>
            <h3 style={errorTitleStyles}>Error:</h3>
            <p>{error}</p>
          </div>
        )}

        {answer && <AnswerDisplay answer={answer} />}

        <ExampleQuestions onExampleClick={handleExampleClick} />
      </main>

      <footer style={footerStyles}>
        <p style={footerTextStyles}>Powered by FastAPI + LangChain + OpenAI</p>
        <ApiStatus status={apiStatus} />
      </footer>
    </div>
  );
}

export default App;
