import React from 'react';

const EXAMPLES = [
  { text: 'Hello', label: 'Greeting' },
  { text: 'مرحبا', label: 'مرحبا' },
  { text: 'Tell me about these documents', label: 'Overview' },
  { text: 'ما هي أبرز أهداف الوثيقة؟', label: 'أهداف' },
  { text: 'What are the main strategic goals?', label: 'Goals' },
  { text: 'What indicators are mentioned?', label: 'Indicators' },
  { text: 'ما هي المؤشرات الرئيسية؟', label: 'مؤشرات' },
  { text: 'What is the vision or timeline?', label: 'Vision' },
  { text: 'ما الرؤية والجدول الزمني؟', label: 'رؤية' },
  { text: 'Key initiatives or pillars?', label: 'Initiatives' },
];

const wrap = {
  marginTop: '2.5rem',
  paddingTop: '1.5rem',
  borderTop: '1px solid #c4b8a8',
};

const title = {
  fontSize: '0.75rem',
  fontWeight: '600',
  color: '#8a7a6a',
  marginBottom: '0.75rem',
  textTransform: 'uppercase',
  letterSpacing: '0.08em',
};

const list = {
  display: 'flex',
  flexWrap: 'wrap',
  gap: '0.5rem',
};

const pill = {
  padding: '0.4rem 0.75rem',
  fontSize: '0.8rem',
  color: '#8b4513',
  background: 'transparent',
  border: '1px solid #c4b8a8',
  borderRadius: '999px',
  cursor: 'pointer',
  transition: 'all 0.2s',
};

const pillHover = {
  ...pill,
  background: '#f5f1eb',
  borderColor: '#8b4513',
};

function ExampleQuestions({ onExampleClick }) {
  const [over, setOver] = React.useState(null);
  return (
    <div style={wrap}>
      <div style={title}>Examples</div>
      <div style={list}>
        {EXAMPLES.map((ex, i) => (
          <button
            key={i}
            type="button"
            style={over === i ? pillHover : pill}
            onClick={() => onExampleClick(ex.text)}
            onMouseEnter={() => setOver(i)}
            onMouseLeave={() => setOver(null)}
          >
            {ex.label}
          </button>
        ))}
      </div>
    </div>
  );
}

export default ExampleQuestions;
