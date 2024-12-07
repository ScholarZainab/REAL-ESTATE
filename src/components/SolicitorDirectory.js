// src/components/SolicitorDirectory.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const SolicitorDirectory = () => {
  const [solicitors, setSolicitors] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    axios.get('/api/solicitors/').then((response) => {
      setSolicitors(response.data);
    });
  }, []);

  const filteredSolicitors = solicitors.filter((solicitor) =>
    solicitor.name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="solicitor-directory">
      <h2>Verified Solicitor Directory</h2>
      <input
        type="text"
        placeholder="Search by name or state"
        onChange={(e) => setSearch(e.target.value)}
      />
      <ul>
        {filteredSolicitors.map((solicitor) => (
          <li key={solicitor.id}>
            {solicitor.name} - {solicitor.state} - {solicitor.yearsOfExperience} years
          </li>
        ))}
      </ul>
    </div>
  );
};

export default SolicitorDirectory;
