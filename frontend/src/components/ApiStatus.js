import React from 'react';

const statusBaseStyles = {
  marginTop: '0.75rem',
  fontSize: '0.95rem',
  fontWeight: '600',
  padding: '0.5rem 1rem',
  borderRadius: '8px',
  display: 'inline-block',
  transition: 'all 0.3s ease',
};

const statusOnlineStyles = {
  ...statusBaseStyles,
  color: '#10b981',
  background: 'rgba(16, 185, 129, 0.1)',
  border: '1px solid rgba(16, 185, 129, 0.3)',
};

const statusOfflineStyles = {
  ...statusBaseStyles,
  color: '#ef4444',
  background: 'rgba(239, 68, 68, 0.1)',
  border: '1px solid rgba(239, 68, 68, 0.3)',
};

const statusCheckingStyles = {
  ...statusBaseStyles,
  color: '#f59e0b',
  background: 'rgba(245, 158, 11, 0.1)',
  border: '1px solid rgba(245, 158, 11, 0.3)',
};

function ApiStatus({ status }) {
  const getStatusText = () => {
    switch (status) {
      case 'online':
        return '✓ API Online - System Ready';
      case 'offline':
        return '✗ API Offline - Check Backend Server';
      default:
        return '⏳ Checking API status...';
    }
  };

  const getStatusStyle = () => {
    switch (status) {
      case 'online':
        return statusOnlineStyles;
      case 'offline':
        return statusOfflineStyles;
      default:
        return statusCheckingStyles;
    }
  };

  return (
    <p style={getStatusStyle()}>
      {getStatusText()}
    </p>
  );
}

export default ApiStatus;
