import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';


function App() {
  const [artist, setArtist] = useState('');
  const [song, setSong] = useState('');
  const [lyrics, setLyrics] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [engLyrics, setEngLyrics] = useState('');
  const [language, setLanguage] = useState('');
  
  const handleLyricSubmit = (e) => {
    
    e.preventDefault(); //Prevent page refresh
    setLoading(true); //So the user can see it's loading
    setError(''); //Clear previous error messages

    //Actual call here
    axios.post('http://localhost:5000/lyrics/', {
      artist: artist,
      song: song
    })
    .then(response => {
      //console.log("SUCCESS", response);


      if (response.status === 200) {
        setLyrics(response.data.lyrics);
        setEngLyrics(response.data.lyrics);
      } 

      else {
        setError('Error: Failed to fetch lyrics');
      }

      setLoading(false);
    })

    //error catching
    .catch(error => {
      console.log(error);
      setError('Error: Failed to fetch lyrics');
      setLoading(false);
    });
  };

  const handleTranslateSubmit = (e) => {
    e.preventDefault(); //Prevent page refresh
    setLoading(true); //So the user can see it's loading
    setError(''); //Clear previous error messages

    //Actual call here
    axios.post('http://localhost:5000/translate/', {
      language: language,
      text: engLyrics
    })
    
    .then(response => {
      if (response.status === 200) {
        setLyrics(response.data.text);
      } 

      else {
        setError('Error: Failed to fetch lyrics');
      }
      setLoading(false);
    })
    //error catching
    .catch(error => {
      console.log(error);
      setError('Error: Failed to fetch lyrics');
      setLoading(false);
    });
  };

  const setLanguageEn = (e) => {
    e.preventDefault();
    setLyrics(engLyrics);
  };

  const setLanguageFr = (e) => {
    e.preventDefault();
    setLanguage("fr");
    handleTranslateSubmit(e);
  };

  const setLanguageIt = (e) => {
    e.preventDefault();
    e.setLanguage("it");
    handleTranslateSubmit(e);
  };

  const setLanguageEs = (e) => {
    e.preventDefault();
    e.setLanguage("es");
    handleTranslateSubmit(e);
  };

  return (
    <>
      <meta charSet="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <h1>Lyric Finder</h1>
      <img
        src="ACOUSTIQ.png"
        alt="ACOUSTIQ logo"
        width={300}
        height={300}
        style={{ marginTop: "2rem" }}
      />
      <form onSubmit={handleLyricSubmit}> {/* Woah there lil bro */}
        <label htmlFor="artist-name">Enter artist name:</label>
        <input 
          type="text" 
          id="artist-name" 
          name="artist-name" 
          value={artist}
          onChange={(e) => setArtist(e.target.value)}
        />
        <label htmlFor="song-name">Enter song name:</label>
        <input 
          type="text" 
          id="song-name" 
          name="song-name" 
          value={song}
          onChange={(e) => setSong(e.target.value)}
        />
        <button type="submit" id="find-lyrics">Find Lyrics</button>
      </form>
      <div className="translation-buttons">
        <button id="translate-to-english" onClick={setLanguageEn}>Translate to English</button>
        <button id="translate-to-french" onClick={setLanguageFr}>Translate to French</button>
        <button id="translate-to-italian" onClick={setLanguageIt}>Translate to Italian</button>
        <button id="translate-to-spanish" onClick={setLanguageEs}>Translate to Spanish</button>
      </div>
      {error ? <p>{error}</p> : <textarea id="lyrics-output" readOnly="" defaultValue={loading ? 'LOADING' : lyrics} />}
      <h2 id="theme-heading">Theme:</h2>
      <textarea id="theme-output" readOnly="" defaultValue={""} />
    </>
  );
}
export default App;