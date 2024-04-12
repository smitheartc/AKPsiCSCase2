import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [getMessage, setGetMessage] = useState({})

  useEffect(()=>{
    axios.post('http://localhost:5000/lyrics/',{
      "artist" : "Taylor Swift",
       "song": "Anti-Hero" })
       .then(response => {
      console.log("SUCCESS", response)
      setGetMessage(response)
    }).catch(error => {
      console.log(error)
    })

  }, [])
  return (
    <div className="App" >
      <header className="App-header">
      <h1>"ACOUSTIQ</h1>
        {/* <img src={logo} className="App-logo" alt="logo" />
        <div>{getMessage.status === 200 ? 
          <p>{getMessage.data.lyrics}</p>
          :
          <p>LOADING</p>}</div> */}
      </header>
    </div>
  );
}
export default App;
