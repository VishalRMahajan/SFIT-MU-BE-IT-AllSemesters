import React, { Component } from 'react';
import { useLocation } from 'react-router-dom';
import './DetailedProfile.css';

class DetailedProfile extends Component {
  render() {
    const { profile } = this.props.location.state;

    return (
      <div className='DetailedBackground'>
        <div className='DetailedProfile-card'>
          <div className='Banner'>
            <img src={profile.bannerUrl} alt="Banner" />
          </div>
          <div className='Profile-image'>
            <img src={profile.imageUrl} alt="Profile" />
          </div>
          <div className='Profile-details'>
            <h2>{profile.name}</h2>
            <h4>{profile.rollNo}</h4>
            <p>{profile.description}</p>
            <p>{profile.experience}</p>
            <p>Connect with me on LinkedIn for more details.</p>
          </div>
        </div>
      </div>
    );
  }
}

export default function DetailedProfileWrapper() {
  const location = useLocation();
  return <DetailedProfile location={location} />;
}