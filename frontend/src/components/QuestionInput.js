import React from 'react';

const containerStyles = {
  marginBottom: '2.5rem',
  animation: 'fadeIn 0.6s ease-out',
};

const labelStyles = {
  display: 'block',
  fontSize: '1.15rem',
  fontWeight: '700',
  color: '#ffffff',
  marginBottom: '1rem',
  textShadow: '0 2px 4px rgba(0, 0, 0, 0.2)',
};

const textareaStyles = {
  width: '100%',
  padding: '1.25rem',
  fontSize: '1rem',
  fontFamily: 'inherit',
  border: '2px solid rgba(255, 255, 255, 0.2)',
  borderRadius: '16px',
  background: 'rgba(255, 255, 255, 0.95)',
  backdropFilter: 'blur(10px)',
  color: '#1a202c',
  resize: 'vertical',
  transition: 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)',
  boxShadow: '0 4px 20px rgba(0, 0, 0, 0.1)',
  outline: 'none',
};

const textareaFocusStyles = {
  ...textareaStyles,
  border: '2px solid #667eea',
  boxShadow: '0 8px 30px rgba(102, 126, 234, 0.4)',
  transform: 'translateY(-2px)',
};

const textareaDisabledStyles = {
  ...textareaStyles,
  background: 'rgba(255, 255, 255, 0.7)',
  cursor: 'not-allowed',
  opacity: 0.7,
};

const buttonStyles = {
  width: '100%',
  marginTop: '1.25rem',
  padding: '1rem 2rem',
  fontSize: '1.05rem',
  fontWeight: '700',
  color: '#ffffff',
  background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
  border: 'none',
  borderRadius: '12px',
  cursor: 'pointer',
  transition: 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center',
  gap: '0.75rem',
  boxShadow: '0 6px 20px rgba(102, 126, 234, 0.4)',
  textTransform: 'uppercase',
  letterSpacing: '0.5px',
};

const buttonHoverStyles = {
  ...buttonStyles,
  transform: 'translateY(-3px)',
  boxShadow: '0 10px 30px rgba(102, 126, 234, 0.5)',
};

const buttonDisabledStyles = {
  ...buttonStyles,
  background: 'rgba(156, 163, 175, 0.8)',
  cursor: 'not-allowed',
  transform: 'none',
  boxShadow: 'none',
};

const spinnerStyles = {
  width: '18px',
  height: '18px',
  border: '3px solid rgba(255, 255, 255, 0.3)',
  borderTopColor: '#ffffff',
  borderRadius: '50%',
  animation: 'spin 0.8s linear infinite',
};

const hintStyles = {
  marginTop: '0.75rem',
  fontSize: '0.875rem',
  color: 'rgba(255, 255, 255, 0.8)',
  textAlign: 'center',
  fontStyle: 'italic',
};

function QuestionInput({ question, setQuestion, onAsk, loading, onKeyPress }) {
  const [isFocused, setIsFocused] = React.useState(false);
  const [isHovered, setIsHovered] = React.useState(false);

  const getTextareaStyle = () => {
    if (loading) return textareaDisabledStyles;
    if (isFocused) return textareaFocusStyles;
    return textareaStyles;
  };

  const getButtonStyle = () => {
    if (loading || !question.trim()) return buttonDisabledStyles;
    if (isHovered) return buttonHoverStyles;
    return buttonStyles;
  };

  return (
    <div style={containerStyles}>
      <label htmlFor="question-input" style={labelStyles}>
        Ask a Question:
      </label>
      <textarea
        id="question-input"
        style={getTextareaStyle()}
        placeholder="e.g., What are your key skills? What is your educational background?"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        onKeyPress={onKeyPress}
        onFocus={() => setIsFocused(true)}
        onBlur={() => setIsFocused(false)}
        rows="4"
        disabled={loading}
      />
      <button
        style={getButtonStyle()}
        onClick={onAsk}
        onMouseEnter={() => setIsHovered(true)}
        onMouseLeave={() => setIsHovered(false)}
        disabled={loading || !question.trim()}
      >
        {loading ? (
          <>
            <span style={spinnerStyles}></span>
            <span>Processing...</span>
          </>
        ) : (
          'Ask Question'
        )}
      </button>
      <p style={hintStyles}>💡 Press Ctrl+Enter to submit</p>
    </div>
  );
}

export default QuestionInput;
