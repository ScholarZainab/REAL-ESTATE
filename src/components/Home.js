// src/components/Home.js
import React from 'react';
import FeaturedListings from './FeaturedListings';

const Home = () => {
  return (
    <div className="home">
      <header>
        <h1>Welcome to Elitehaven</h1>
        <p>Explore Transparent Luxury Real Estate Listings</p>
        <input
          type="text"
          placeholder="Search properties by location or category"
          className="search-bar"
        />
      </header>
      <FeaturedListings />
    </div>
  );
};

export default Home;
