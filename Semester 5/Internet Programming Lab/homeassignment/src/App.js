import './App.css';
import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ProfileCard from './ProfileCard';
import DetailedProfile from './DetailedProfile';

export default class App extends Component {
  render() {
    return (
      <Router>
        <Routes>
          <Route exact path="/" element={<ProfileCard />} />
          <Route path="/detailed-profile" element={<DetailedProfile />} />
        </Routes>
      </Router>
    );
  }
}