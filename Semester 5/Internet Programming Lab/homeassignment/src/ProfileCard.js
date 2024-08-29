import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import './ProfileCard.css';
import profileImage from './assets/images/Profile.jpg';

export default class ProfileCard extends Component {
  render() {
    const profile = {
      name: 'Vishal Rajesh Mahajan',
      rollNo: 'TE IT A4 Roll no 62',
      description: 'Software Engineer passionate about building scalable web applications and working with modern web technologies.',
      experience: 'Experience in React, Node.js, and other web technologies.',
      imageUrl: profileImage,
      bannerUrl: 'https://www.vishalrmahajan.in/assets/images/banner.png'
    };

    return (
      <div className='Background'>
        <div className='Profile-card'>
          <div className='Profile-image'>
            <img src={profile.imageUrl} alt="Profile" />
          </div>
          <div className='Profile-details'>
            <h2>{profile.name}</h2>
            <h4>{profile.rollNo}</h4>
            <p>Click on button below to know more !!!</p>
            <Link to="/detailed-profile" state={{ profile }}>
              <button className='Profile-button'>Know More</button>
            </Link>
          </div>
        </div>
      </div>
    );
  }
}