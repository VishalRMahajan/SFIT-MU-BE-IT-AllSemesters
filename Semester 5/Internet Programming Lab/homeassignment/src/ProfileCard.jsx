import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import './ProfileCard.css';
import profileImage from './assets/images/Profile.jpg';

export default class ProfileCard extends Component {
  render() {
    const profile = {
      name: 'Vishal Rajesh Mahajan',
      rollNo: 'TE IT A4 Roll no 62',
      tagline: 'From Code to Career, find me everywhere as "vishalrmahajan"',
      imageUrl: profileImage,
      bannerUrl: 'https://www.vishalrmahajan.in/assets/images/banner.png',
      skills : ['Python', 'HTML', 'CSS', 'JavaScript', 'React', 'AWS', 'FastApi', 'SQL','Machine Learning'],
    };

    return (
      <div class="card-container">
        <img class="round" src={profile.imageUrl} alt="user" />
        <h3>{profile.name}</h3>
        <h6>{profile.tagline}</h6>
        <p></p>
        <div class="buttons">
        <Link to="/detailed-profile" state={{ profile }}>
          <button class="primary">
            View Details
          </button>
        </Link>
        </div>
      </div>


    );
  }
}