import React, { useEffect, useRef } from 'react';

const containerStyles = {
  background: 'linear-gradient(135deg, rgba(255, 255, 255, 0.98) 0%, rgba(255, 255, 255, 0.95) 100%)',
  border: '2px solid rgba(102, 126, 234, 0.3)',
  borderRadius: '20px',
  padding: '2rem',
  margin: '2rem 0',
  boxShadow: '0 10px 40px rgba(0, 0, 0, 0.15)',
  backdropFilter: 'blur(10px)',
  animation: 'fadeIn 0.5s ease-out',
  position: 'relative',
  overflow: 'hidden',
};

const containerOverlay = {
  position: 'absolute',
  top: 0,
  left: 0,
  right: 0,
  height: '4px',
  background: 'linear-gradient(90deg, #667eea 0%, #764ba2 100%)',
};

const titleStyles = {
  fontSize: '1.5rem',
  fontWeight: '800',
  color: '#667eea',
  marginBottom: '1.5rem',
  paddingBottom: '1rem',
  borderBottom: '3px solid #e2e8f0',
  display: 'flex',
  alignItems: 'center',
  gap: '0.75rem',
};

const contentStyles = {
  color: '#2d3748',
  lineHeight: '1.9',
  fontSize: '1.05rem',
  fontWeight: '400',
};

const paragraphStyles = {
  marginBottom: '1.25rem',
  whiteSpace: 'pre-wrap',
  wordWrap: 'break-word',
  color: '#4a5568',
};

const listStyles = {
  margin: '1.25rem 0',
  paddingLeft: '2rem',
  listStyleType: 'disc',
  color: '#4a5568',
};

const listItemStyles = {
  marginBottom: '0.75rem',
  lineHeight: '1.8',
  paddingLeft: '0.5rem',
};

function AnswerDisplay({ answer }) {
  const answerRef = useRef(null);

  useEffect(() => {
    if (answerRef.current) {
      answerRef.current.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
  }, [answer]);

  const formatAnswer = (text) => {
    const paragraphs = text.split(/\n\n+/);
    
    return paragraphs.map((paragraph, index) => {
      if (/^[-*•]\s/.test(paragraph.trim()) || /^\d+\.\s/.test(paragraph.trim())) {
        const items = paragraph.split(/\n/).filter(item => item.trim());
        return (
          <ul key={index} style={listStyles}>
            {items.map((item, itemIndex) => (
              <li key={itemIndex} style={listItemStyles}>
                {item.replace(/^[-*•]\s/, '').replace(/^\d+\.\s/, '')}
              </li>
            ))}
          </ul>
        );
      }
      
      return (
        <p key={index} style={paragraphStyles}>
          {paragraph.trim()}
        </p>
      );
    });
  };

  return (
    <div style={containerStyles} ref={answerRef}>
      <div style={containerOverlay}></div>
      <h2 style={titleStyles}>
        <span>✨</span>
        <span>Answer:</span>
      </h2>
      <div style={contentStyles}>
        {formatAnswer(answer)}
      </div>
    </div>
  );
}

export default AnswerDisplay;
