import React from 'react';

const EXAMPLE_QUESTIONS = [
  { text: 'Hello', label: '👋 Greeting' },
  { text: 'Tell me about this resume', label: '📄 Overview' },
  { text: 'What are your key skills?', label: '💼 Key Skills' },
  { text: 'What is your educational background?', label: '🎓 Education' },
  { text: 'What programming languages do you know?', label: '💻 Programming' },
  { text: 'What work experience do you have?', label: '🏢 Experience' },
  { text: 'What projects have you worked on?', label: '🚀 Projects' },
  { text: 'What certifications do you have?', label: '🏅 Certifications' },
  { text: 'What is your contact information?', label: '📧 Contact' },
  { text: 'What are your achievements?', label: '⭐ Achievements' },
  { text: 'What makes you unique?', label: '✨ Unique Qualities' },
  { text: 'What are your skills and education?', label: '🔗 Multiple Topics' },
];

const containerStyles = {
  marginTop: '3rem',
  paddingTop: '2.5rem',
  borderTop: '2px solid rgba(255, 255, 255, 0.2)',
  animation: 'fadeIn 0.8s ease-out',
};

const titleStyles = {
  fontSize: '1.2rem',
  fontWeight: '700',
  color: '#ffffff',
  marginBottom: '1.5rem',
  textShadow: '0 2px 4px rgba(0, 0, 0, 0.2)',
};

const gridStyles = {
  display: 'grid',
  gridTemplateColumns: 'repeat(auto-fill, minmax(160px, 1fr))',
  gap: '1rem',
};

const buttonBaseStyles = {
  padding: '1rem 1.25rem',
  fontSize: '0.95rem',
  fontWeight: '600',
  color: '#667eea',
  background: 'rgba(255, 255, 255, 0.95)',
  backdropFilter: 'blur(10px)',
  border: '2px solid rgba(102, 126, 234, 0.3)',
  borderRadius: '12px',
  cursor: 'pointer',
  transition: 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)',
  textAlign: 'center',
  boxShadow: '0 4px 15px rgba(0, 0, 0, 0.1)',
};

const buttonHoverStyles = {
  ...buttonBaseStyles,
  background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
  color: '#ffffff',
  transform: 'translateY(-4px) scale(1.02)',
  boxShadow: '0 8px 25px rgba(102, 126, 234, 0.4)',
  border: '2px solid transparent',
};

const buttonActiveStyles = {
  ...buttonHoverStyles,
  transform: 'translateY(-2px) scale(1)',
};

function ExampleQuestions({ onExampleClick }) {
  const [hoveredIndex, setHoveredIndex] = React.useState(null);
  const [activeIndex, setActiveIndex] = React.useState(null);

  const getButtonStyle = (index) => {
    if (activeIndex === index) return buttonActiveStyles;
    if (hoveredIndex === index) return buttonHoverStyles;
    return buttonBaseStyles;
  };

  return (
    <div style={containerStyles}>
      <h3 style={titleStyles}>Example Questions:</h3>
      <div style={gridStyles}>
        {EXAMPLE_QUESTIONS.map((example, index) => (
          <button
            key={index}
            style={getButtonStyle(index)}
            onClick={() => {
              onExampleClick(example.text);
              setActiveIndex(index);
              setTimeout(() => setActiveIndex(null), 200);
            }}
            onMouseEnter={() => setHoveredIndex(index)}
            onMouseLeave={() => setHoveredIndex(null)}
          >
            {example.label}
          </button>
        ))}
      </div>
    </div>
  );
}

export default ExampleQuestions;
