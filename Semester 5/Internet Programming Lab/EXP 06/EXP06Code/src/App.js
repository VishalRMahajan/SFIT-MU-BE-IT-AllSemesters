import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faInstagram, faFacebook, faYoutube } from '@fortawesome/free-brands-svg-icons';
import Home from './Home';
import Sessions from './Sessions';
import Contacts from './Contacts';
import './App.css';

function App() {
  return (
    <Router>
      <div className='App'>
        <header>
          <h1 className='header'>Single Page Application</h1>
          <nav className='navbar'>
            <span>Internet Programming</span>
            <div>
              <Link to="/">Home</Link>
              <Link to="/Sessions">Sessions</Link>
              <Link to="/Contacts">Contacts</Link>
            </div>
            <div className='Social-icons'>
              <FontAwesomeIcon icon={faFacebook} />
              <FontAwesomeIcon icon={faInstagram} />
              <FontAwesomeIcon icon={faYoutube} />
            </div>
          </nav>
        </header>
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/Sessions" element={<Sessions />} />
            <Route path="/Contacts" element={<Contacts />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
