import React, { Component } from 'react';
import { useLocation } from 'react-router-dom';
import './DetailedProfile.css';
import { Link } from 'react-router-dom';
import { FaInstagramSquare } from 'react-icons/fa';
import { FaLinkedin } from 'react-icons/fa';
import { FaGithub } from 'react-icons/fa';

class DetailedProfile extends Component {
  render() {
    const { profile } = this.props.location.state;

    return (
      <div class="card-container">
        <img class="round" src={profile.imageUrl} alt="user" />
        <h3>{profile.name}</h3>
        <h6>{profile.tagline}</h6>

        <div class="skills">
          <h6>Skills</h6>
          <ul>
            {profile.skills.map((skill, index) => (
              <li key={index}>{skill}</li>
            ))}
          </ul>
        </div>
        
        <div class="social">
          <h4>Connect with me</h4>
          <div class="social-icons">
            <a href="https://www.instagram.com/vishalrmahajan" target="_blank" rel="noreferrer">
              <FaInstagramSquare size={32} color='white' />
            </a>
            <a href="https://www.linkedin.com/in/vishalrmahajan" target="_blank" rel="noreferrer">
              <FaLinkedin size={32} color='white' />
            </a>
            <a href="https://www.github.com/vishalrmahajan" target="_blank" rel="noreferrer">
              <FaGithub size={32} color='white' />
            </a>
          </div>
        </div>
        <Link to="/" state={{ profile }}>
          <button class="primary">
            Hide Details
          </button>
        </Link>
      </div>
    );
  }
}

export default function DetailedProfileWrapper() {
  const location = useLocation();
  return <DetailedProfile location={location} />;
}