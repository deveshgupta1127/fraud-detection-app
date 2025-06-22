import React from 'react';
import TransactionForm from './TransactionForm';
import './styles.css';

function App() {
  return (
    <div className="app-wrapper">
      <header className="app-header"><h1>Credit Card Fraud Detector</h1></header>
      <TransactionForm />
    </div>
  );
}

export default App;