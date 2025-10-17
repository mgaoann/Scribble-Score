import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './styles.css'; // make sure this path matches your CSS file

// Render the App component into the #root div in index.html
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);