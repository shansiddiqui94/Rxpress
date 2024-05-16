import React, { useState, useEffect } from 'react';
import '/Users/DanielSkies/Development/code/phase-5/Rxpress/client/Rxpress/src/components/PharamacistUI/PatientCard.css';

function PatientCard({ onSelect }) {
  const [fetchPt, setFetchPt] = useState([]); // Initialize as an empty array
  const [searchTerm, setSearchTerm] = useState(''); // State for search input

  // Fetch with search term (assuming your API supports it)
  const handleSearch = () => {
    if (searchTerm) {
      fetch(`http://127.0.0.1:5555/patients/search?name=${searchTerm}`)
        .then(res => res.json())
        .then(data => setFetchPt(data))
        .catch(error => console.error('Error fetching data:', error)); // Add error handling
    }
  };

  // Define function to handle patient selection
  const handleSelect = (patientId) => {
    // Call onSelect function passed from parent component
    onSelect(patientId);
  };

  return (
    <div>
      <div className='searchForm'>
        <input
          type="text"
          value={searchTerm}
          placeholder="Type Patient Name" 
          onChange={(event) => setSearchTerm(event.target.value)} 
        />
      </div>
      <button onClick={handleSearch}>
        {/* Add the search emoji using Unicode */}
        <span role="img" aria-label="Search">🔍</span> 
      </button>

      <div className='patientCardList'>
        {fetchPt.map(patient => (
          <div className="card" key={patient.id} onClick={() => handleSelect(patient.id)}> 
            {/* ^^^ Added onClick event to trigger handleSelect */}
            <h3>{patient.name}</h3>
            <p>{patient.address}</p>
            <p>{patient.insurance}</p>
            {/* Add onClick event to trigger handleSelect */}
            <button onClick={() => handleSelect(patient.id)}>Select</button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default PatientCard;
