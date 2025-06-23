import React from 'react';

// PUBLIC_INTERFACE
export default function Header() {
  return (
    <header className="header">
      <div className="logo">
        <span
          style={{
            display: 'inline-block',
            width: 22,
            height: 22,
            fontSize: '1.55rem',
            color: 'var(--primary)',
          }}
        >
          🍽️
        </span>
        RecipeShare
      </div>
      <nav className="header-nav">
        <a href="#" className="active" tabIndex={0}>
          Browse
        </a>
        <a href="#">Create</a>
        <a href="#">My Recipes</a>
        <a href="#">Login</a>
      </nav>
      <div className="spacer" />
    </header>
  );
}
