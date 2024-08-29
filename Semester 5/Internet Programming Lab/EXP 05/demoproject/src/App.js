import logo from './logo.svg';
import './App.css';
import { useState } from "react";

function App() {
  const [inputText, setInputText] = useState("");
  const handleChange = (e) => {
    setInputText(e.target.value);
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Add Your Name in Text Box and see the magic..
        </p>
        <input 
          type="text" 
          onChange={handleChange} 
          value={inputText} 
          style={{ 
            padding: '10px', 
            fontSize: '16px', 
            borderRadius: '5px', 
            border: '1px solid #ccc', 
          }} 
        />
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          <p>Hello , {inputText}</p>
        </a>
      </header>
    </div>
  );
}

export default App;