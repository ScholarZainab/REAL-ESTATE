// Frontend: React - src/components/Listings.js
import React, { useEffect, useState } from "react";
import axios from "axios";

const Listings = () => {
  const [listings, setListings] = useState([]);

  useEffect(() => {
    axios.get("/api/listings/").then((response) => {
      setListings(response.data);
    });
  }, []);

  return (
    <div className="listings">
      {listings.map((listing) => (
        <div key={listing.id} className="listing">
          <h2>{listing.title}</h2>
          <p>{listing.description}</p>
          <p>${listing.price}</p>
          <img src={listing.image} alt={listing.title} />
        </div>
      ))}
    </div>
  );
};

export default Listings;
