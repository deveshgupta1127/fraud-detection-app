import React, { useState } from 'react';
import axios from 'axios';
import './styles.css';

const featureNames = [
  'Time','V1','V2','V3','V4','V5','V6','V7','V8','V9','V10','V11','V12','V13','V14','V15',
  'V16','V17','V18','V19','V20','V21','V22','V23','V24','V25','V26','V27','V28','Amount']

export default function TransactionForm() {
  const [values, setValues] = useState(featureNames.reduce((acc, key) => ({ ...acc, [key]: '' }), {}));
  const [result, setResult] = useState(null);

  const handleChange = e => {
    setValues({ ...values, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    const features = featureNames.map(k => parseFloat(values[k]) || 0);
    const res = await axios.post('http://localhost:5000/predict', { features });
    setResult(res.data);
  };

  return (
    <div className="form-container">
      <h2>Enter Transaction Data</h2>
      <form className="transaction-form" onSubmit={handleSubmit}>
        {featureNames.map(name => (
          <input
            key={name}
            name={name}
            value={values[name]}
            onChange={handleChange}
            placeholder={name}
            className="feature-input"
          />
        ))}
        <button type="submit" className="submit-button">Check</button>
      </form>
      {result && (
        <div className="result-box">
          <p><strong>Fraud Score:</strong> {result.fraud_score.toFixed(4)}</p>
          <p className={result.is_fraud ? "fraud-text" : "legit-text"}>
            {result.is_fraud ? '🚩 Fraud Detected' : '✅ Legitimate'}
          </p>
        </div>
      )}
    </div>
  );
}