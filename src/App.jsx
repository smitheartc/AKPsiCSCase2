import land from './music_landscape.jpeg';
import note from './music_note.jpeg';
import logo from './ACOUSTIQ.png';

import { Parallax, ParallaxLayer } from '@react-spring/parallax';

function App() {
    
    return (
        <div>
            <Parllax pages={4}>
                <ParallaxLayer>
                    <h2>Welcome to my website</h2>
                </ParallaxLayer>

                <ParallaxLayer offset={1}>
                    <h2>Web Dev</h2>
                </ParallaxLayer>
            </Parllax>

        </div>
    )
}

export default App;