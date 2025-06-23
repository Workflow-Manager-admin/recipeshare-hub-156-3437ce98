import React from 'react';

// PUBLIC_INTERFACE
export default function MainContent() {
  return (
    <main className="main-content">
      <div className="placeholder-content">
        {/* Placeholder for main recipe content */}
        Recipe catalog will appear here.<br />
        <span style={{ color: 'var(--accent)' }}>Coming soon!</span>
      </div>
    </main>
  );
}
