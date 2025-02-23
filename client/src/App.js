import React, { useState, useEffect } from 'react'
import './styles.css';
import axios from "axios";

function App() {
  const [data, setData] = useState([{}])  // Initialize with an empty array for members
  const [userInput, setUserInput] = useState('');
  const [response, setResponse] = useState('');

  useEffect(() => {
    fetch("http://127.0.0.1:8000/")
      .then(res => res.json())
      .then(data => {
        setData(data)  // Set the received data
        console.log(data)  // Log the fetched data (just to verify it's correct)
      })
  }, [])
  return (
    <div class="Outside">
      <div class="title">
        <h1>ScribbleScore</h1>
      </div>
      <div class="upload">
        <div class="absolute-container">
          <div class="right-abs">
            <h1>Some slogan about improving handwriting</h1>
          </div>
          <div class="left-abs">
            
          </div>
        </div>
      </div>
      <div class="faq">
        <h1>Frequently Asked questions</h1>
        <h2>How can I improve my handwriting?</h2>
      </div>
      <div class="footer">
        <div class="footer-left">
          Copyright © 2024 Scribblescore. All rights reserved.
        </div>
        <div class="footer-right">
          icons here
          <a href="https://www.vecteezy.com/free-vector/blue-yellow-gradient">Blue Yellow Gradient Vectors by Vecteezy</a>
        </div>
      </div>
      {//(//data != 'undefined') ? (
        //<p>Loading...</p>
        //data["Members"].map((member, i) => (
          //<p key={i}>{member}</p>))
        
      //)://(
        //<p>Loading...</p>
        //data["Members"].map((member, i) => (
          //<p key={i}>{member}</p>
        //))
      //)
      //<p>{data["Members"]}</p>
      } 
    </div>
  )
}

export default App
