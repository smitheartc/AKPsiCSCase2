import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [artist, setArtist] = useState('');
  const [song, setSong] = useState('');
  const [lyrics, setLyrics] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [engLyrics, setEngLyrics] = useState('');
  const [theme, setTheme] = useState('');
  

  //lyric api post request, called with the "find lyrics" button
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

      if (response.status === 200) {
        setLyrics(response.data.lyrics);
        setEngLyrics(response.data.lyrics);
      } 

      else {
        console.log("I'm a little bitch!")
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


  //lyric api post request, called with the "translate" buttons im actually really proud of this
  const handleTranslateSubmit = (lang) => {
    // e.preventDefault(); //Prevent page refresh
    setLoading(true); //So the user can see it's loading
    setError(''); //Clear previous error messages

    //Actual call here
    axios.post('http://localhost:5000/translate/', {
      language: lang,
      text: engLyrics
    })
    
    .then(response => {
      if (response.status === 200) {
        setLyrics(response.data.text);
        handleThemeSubmit();
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
  } //translate function




    //theme api post request, called with find lyrics and refreshed with the find theme button - bug not feature(?)
    const handleThemeSubmit = () => { 


      axios.post('http://localhost:5000/theme/', {
        lyrics: engLyrics
      })
      
      .then(response => {
        if (response.status === 200) {
          setTheme(response.data.theme);
        } 
  
        else {
          setError('Error: Failed to fetch lyrics');
        }
      })
      //error catching
      .catch(error => {
        console.log(error);
        setError('Error: Failed to fetch lyrics');
      });
  }; //theme function




  //Kaustubh's html begins here
  return (
    <>
      <meta charSet="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <h1>Lyric Finder</h1>
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
        <button id="translate-to-english" onClick={() => handleTranslateSubmit('en')}>Translate to English</button>
        <button id="translate-to-french" onClick={() => handleTranslateSubmit('fr')}>Translate to French</button>
        <button id="translate-to-italian" onClick={() => handleTranslateSubmit('it')}>Translate to Italian</button>
        <button id="translate-to-spanish" onClick={() => handleTranslateSubmit('es')}>Translate to Spanish</button>
      </div>
      {error ? <p>{error}</p> : <textarea id="lyrics-output" readOnly="" defaultValue={loading ? 'LOADING' : lyrics} />}
      
      <button id="Theme-Submit" onClick={() => handleThemeSubmit()}>Theme Submit</button>
      <h2 id="theme-heading">Theme:</h2>
      <textarea id="theme-output" readOnly="" defaultValue={theme} />
    </>
  );
}
export default App;