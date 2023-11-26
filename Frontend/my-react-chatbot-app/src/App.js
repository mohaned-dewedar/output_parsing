import React from 'react';
import './assets/styles/App.css';
import Chatbot from './components/Chatbot';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>My React Chatbot App</h1>
      </header>
      <Chatbot />
    </div>
  );
}

export default App;