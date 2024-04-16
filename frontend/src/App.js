import React, { useReducer, useState } from 'react';
import axios from 'axios';
import './App.css';
import land from './music_landscape.jpeg';
import note from './music_note.png';
import logo from './ACOUSTIQ.png';
import { Parallax, ParallaxLayer } from '@react-spring/parallax';


function App() {
  const [artist, setArtist] = useState('');
  const [song, setSong] = useState('');
  const [lyrics, setLyrics] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [engLyrics, setEngLyrics] = useState('');
  const [theme, setTheme] = useState('');
  
  const handleLyricSubmit = (e) => {
    
    e.preventDefault(); //Prevent page refresh
    setLoading(true); //So the user can see it's loading
    setError(''); //Clear previous error messages

    //Actual call here
    axios.post('http://127.0.0.1:5000/lyrics/', {
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

    const handleThemeSubmit = () => {
      // e.preventDefault(); //Prevent page refresh
      setLoading(true); //So the user can see it's loading
      setError(''); //Clear previous error messages
  
      //Actual call here
      axios.post('http://localhost:5000/theme/', {
        lyrics: engLyrics
      })
      
      .then(response => {
        if (response.status === 200) {
          setTheme(response.data.text);
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
}
  return (
    <>
      <meta charSet="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      
      {/* <div>
            <Parallax pages={4}>
                <ParallaxLayer>
                    <h2>Welcome to my website</h2>
                </ParallaxLayer>

                <ParallaxLayer offset={1}>
                    <h2>Web Dev</h2>
                </ParallaxLayer>
            </Parallax>

        </div> */}
      
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
        <button id="translate-to-english" onClick={() => handleTranslateSubmit('en')}>Translate to English</button>
        <button id="translate-to-french" onClick={() => handleTranslateSubmit('fr')}>Translate to French</button>
        <button id="translate-to-italian" onClick={() => handleTranslateSubmit('it')}>Translate to Italian</button>
        <button id="translate-to-spanish" onClick={() => handleTranslateSubmit('es')}>Translate to Spanish</button>
      </div>
      {error ? <p>{error}</p> : <textarea id="lyrics-output" readOnly="" defaultValue={loading ? 'LOADING' : lyrics} />}
      <h2 id="theme-heading">Theme:</h2>
      <textarea id="theme-output" readOnly="" defaultValue={loading ? 'LOADING' : theme} />
    </>
  );
}
export default App;