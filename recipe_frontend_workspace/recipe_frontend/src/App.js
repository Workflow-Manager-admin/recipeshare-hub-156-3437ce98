import React from 'react';
import './App.css';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import MainContent from './components/MainContent';

// PUBLIC_INTERFACE
function App() {
  return (
    <div className="recipe-layout">
      <Header />
      <Sidebar />
      <MainContent />
    </div>
  );
}

export default App;