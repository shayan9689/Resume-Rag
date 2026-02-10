import React, { useEffect, useRef } from 'react';

const box = {
  background: '#fff',
  border: '1px solid #c4b8a8',
  borderLeft: '4px solid #8b4513',
  padding: '1.75rem 1.5rem',
  marginBottom: '2rem',
  animation: 'fadeUp 0.4s ease-out',
};

const heading = {
  fontFamily: 'Georgia, serif',
  fontSize: '0.85rem',
  fontWeight: '400',
  color: '#8b4513',
  marginBottom: '1rem',
  textTransform: 'uppercase',
  letterSpacing: '0.1em',
};

const content = {
  fontFamily: 'Georgia, serif',
  color: '#2d2520',
  lineHeight: '1.8',
  fontSize: '1rem',
};

const pStyle = {
  marginBottom: '1rem',
  whiteSpace: 'pre-wrap',
  wordBreak: 'break-word',
};

const ulStyle = {
  margin: '1rem 0',
  paddingLeft: '1.5rem',
  color: '#2d2520',
};

const liStyle = { marginBottom: '0.5rem', lineHeight: '1.7' };

function AnswerDisplay({ answer }) {
  const ref = useRef(null);
  useEffect(() => {
    ref.current?.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }, [answer]);

  const format = (text) => {
    const blocks = text.split(/\n\n+/);
    return blocks.map((block, i) => {
      if (/^[-*•]\s/.test(block.trim()) || /^\d+\.\s/.test(block.trim())) {
        const items = block.split(/\n/).filter((s) => s.trim());
        return (
          <ul key={i} style={ulStyle}>
            {items.map((item, j) => (
              <li key={j} style={liStyle}>
                {item.replace(/^[-*•]\s/, '').replace(/^\d+\.\s/, '')}
              </li>
            ))}
          </ul>
        );
      }
      return (
        <p key={i} style={pStyle}>
          {block.trim()}
        </p>
      );
    });
  };

  return (
    <article style={box} ref={ref}>
      <div style={heading}>Answer</div>
      <div style={content}>{format(answer)}</div>
    </article>
  );
}

export default AnswerDisplay;
