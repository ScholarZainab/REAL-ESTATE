// src/components/FeaturedListings.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const FeaturedListings = () => {
  const [listings, setListings] = useState([]);

  useEffect(() => {
    axios.get('/api/listings/featured/').then((response) => {
      setListings(response.data);
    });
  }, []);

  return (
    <div className="featured-listings">
      <h2>Featured Listings</h2>
      <div className="listings-grid">
        {listings.map((listing) => (
          <div key={listing.id} className="listing-card">
            <img src={listing.image} alt={listing.title} />
            <h3>{listing.title}</h3>
            <p>{listing.location}</p>
            <p>${listing.price}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default FeaturedListings;
