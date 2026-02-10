import React from 'react';

const wrap = {
  marginBottom: '2rem',
  animation: 'fadeUp 0.4s ease-out',
};

const label = {
  display: 'block',
  fontSize: '0.75rem',
  fontWeight: '600',
  color: '#6b5b4f',
  marginBottom: '0.5rem',
  textTransform: 'uppercase',
  letterSpacing: '0.08em',
};

const textarea = {
  width: '100%',
  padding: '1rem 1.25rem',
  fontSize: '1rem',
  fontFamily: 'inherit',
  lineHeight: '1.5',
  border: '1px solid #c4b8a8',
  borderLeft: '4px solid #8b4513',
  borderRadius: '0',
  background: '#fff',
  color: '#2d2520',
  resize: 'vertical',
  outline: 'none',
  transition: 'border-color 0.2s',
};

const textareaFocus = {
  ...textarea,
  borderColor: '#8b4513',
};

const textareaDisabled = {
  ...textarea,
  background: '#f5f1eb',
  cursor: 'not-allowed',
  opacity: 0.8,
};

const btn = {
  marginTop: '1rem',
  padding: '0.75rem 1.5rem',
  fontSize: '0.9rem',
  fontWeight: '600',
  color: '#fff',
  background: '#8b4513',
  border: 'none',
  borderRadius: '0',
  cursor: 'pointer',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center',
  gap: '0.5rem',
};

const btnHover = { ...btn, background: '#6d3410' };
const btnDisabled = { ...btn, background: '#a08060', cursor: 'not-allowed' };

const spinner = {
  width: '14px',
  height: '14px',
  border: '2px solid rgba(255,255,255,0.3)',
  borderTopColor: '#fff',
  borderRadius: '50%',
  animation: 'spin 0.7s linear infinite',
};

const hint = { marginTop: '0.5rem', fontSize: '0.75rem', color: '#8a7a6a' };

function QuestionInput({ question, setQuestion, onAsk, loading, onKeyPress }) {
  const [focus, setFocus] = React.useState(false);
  const [hover, setHover] = React.useState(false);

  const taStyle = loading ? textareaDisabled : focus ? textareaFocus : textarea;
  const btnStyle = loading || !question.trim() ? btnDisabled : hover ? btnHover : btn;

  return (
    <div style={wrap}>
      <label htmlFor="q" style={label}>Your question</label>
      <textarea
        id="q"
        style={taStyle}
        placeholder="e.g. What are the main goals? / ما هي أبرز الأهداف؟"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        onKeyPress={onKeyPress}
        onFocus={() => setFocus(true)}
        onBlur={() => setFocus(false)}
        rows={4}
        disabled={loading}
      />
      <button
        type="button"
        style={btnStyle}
        onClick={onAsk}
        onMouseEnter={() => setHover(true)}
        onMouseLeave={() => setHover(false)}
        disabled={loading || !question.trim()}
      >
        {loading ? (
          <>
            <span style={spinner} />
            <span>Asking…</span>
          </>
        ) : (
          'Ask'
        )}
      </button>
      <p style={hint}>Ctrl+Enter to send</p>
    </div>
  );
}

export default QuestionInput;
