import React from 'react';

const base = { fontSize: '0.8rem', color: '#8a7a6a' };
const ok = { ...base, color: '#2d6a2d' };
const bad = { ...base, color: '#a63d3d' };
const wait = { ...base, color: '#8a7a6a' };

function ApiStatus({ status }) {
  const msg = status === 'online' ? 'API connected' : status === 'offline' ? 'API disconnected' : 'Checking…';
  const style = status === 'online' ? ok : status === 'offline' ? bad : wait;
  return <p style={style}>{msg}</p>;
}

export default ApiStatus;
