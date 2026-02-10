import React, { useState, useEffect } from 'react';
import QuestionInput from './components/QuestionInput';
import AnswerDisplay from './components/AnswerDisplay';
import ExampleQuestions from './components/ExampleQuestions';
import ApiStatus from './components/ApiStatus';

const API_BASE_URL = 'http://localhost:8000';

const appStyles = {
  minHeight: '100vh',
  padding: '2rem 1rem 4rem',
  maxWidth: '720px',
  margin: '0 auto',
};

const headerStyles = {
  marginBottom: '2.5rem',
  paddingBottom: '1.5rem',
  borderBottom: '1px solid #c4b8a8',
};

const titleStyles = {
  fontFamily: 'Georgia, serif',
  fontSize: '2rem',
  fontWeight: '400',
  color: '#2d2520',
  letterSpacing: '0.02em',
};

const subtitleStyles = {
  marginTop: '0.35rem',
  fontSize: '0.9rem',
  color: '#6b5b4f',
  fontWeight: '400',
};

const errorStyles = {
  background: '#fdf2f2',
  color: '#9b2c2c',
  padding: '1rem 1.25rem',
  marginBottom: '1.5rem',
  borderRadius: '4px',
  border: '1px solid #fecaca',
  fontSize: '0.9rem',
};

const footerStyles = {
  marginTop: '3rem',
  paddingTop: '1.5rem',
  borderTop: '1px solid #c4b8a8',
  fontSize: '0.8rem',
  color: '#6b5b4f',
  textAlign: 'center',
};

function App() {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [apiStatus, setApiStatus] = useState('checking');

  useEffect(() => {
    const check = async () => {
      try {
        const r = await fetch(`${API_BASE_URL}/health`);
        setApiStatus(r.ok ? 'online' : 'offline');
      } catch {
        setApiStatus('offline');
      }
    };
    check();
    const id = setInterval(check, 30000);
    return () => clearInterval(id);
  }, []);

  const askQuestion = async () => {
    if (!question.trim()) {
      setError('Please enter a question.');
      return;
    }
    setLoading(true);
    setError(null);
    setAnswer('');
    try {
      const r = await fetch(`${API_BASE_URL}/ask`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: question.trim() }),
      });
      if (!r.ok) throw new Error(r.status === 503 ? 'Service starting. Try again in a moment.' : `Error ${r.status}`);
      const data = await r.json();
      setAnswer(data.answer);
      setQuestion('');
    } catch (err) {
      setError(err.message || 'Request failed. Is the backend running?');
    } finally {
      setLoading(false);
    }
  };

  const handleExample = (q) => {
    setQuestion(q);
    setError(null);
    setAnswer('');
  };

  return (
    <div style={appStyles}>
      <header style={headerStyles}>
        <h1 style={titleStyles}>Document Q&A</h1>
        <p style={subtitleStyles}>Ask in Arabic or English. Answers are from your documents only.</p>
      </header>

      <QuestionInput
        question={question}
        setQuestion={setQuestion}
        onAsk={askQuestion}
        loading={loading}
        onKeyPress={(e) => e.key === 'Enter' && e.ctrlKey && askQuestion()}
      />

      {error && <div style={errorStyles}>{error}</div>}
      {answer && <AnswerDisplay answer={answer} />}
      <ExampleQuestions onExampleClick={handleExample} />

      <footer style={footerStyles}>
        <ApiStatus status={apiStatus} />
      </footer>
    </div>
  );
}

export default App;
