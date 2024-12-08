// src/components/Map.js
import React from "react";

const Map = ({ latitude, longitude }) => {
  const mapUrl = `https://www.google.com/maps/embed/v1/view?key=YOUR_GOOGLE_MAPS_API_KEY&center=${latitude},${longitude}&zoom=15`;

  return (
    <div className="map">
      <iframe
        src={mapUrl}
        width="100%"
        height="400"
        style={{ border: 0 }}
        allowFullScreen
        loading="lazy"
        title="Property Location"
      ></iframe>
    </div>
  );
};

export default Map;
