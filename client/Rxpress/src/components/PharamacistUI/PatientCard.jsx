import React, { useState, useEffect } from 'react';
import '/Users/DanielSkies/Development/code/phase-5/Rxpress/client/Rxpress/src/components/PharamacistUI/PatientCard.css';
import PatientImage from '../assets/patient.png';
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

    <div className="wrap">
    <div className="search">
      <input
        type="text"
        value={searchTerm}
        placeholder="Type Patients Name...."
        onChange={(event) => setSearchTerm(event.target.value)}
        className="searchTerm"
        id="input_text"
      />
      <button type="submit" className="searchButton" onClick={handleSearch}>
      <img src={PatientImage} alt="Search" aria-label="Search" />
      </button>




     </div>
      <div className='patientCardList'>
        {fetchPt.map(patient => (
          <div className="card" key={patient.id} onClick={() => handleSelect(patient.id)}> 
            <h3>{patient.name}</h3>
            <p>{patient.address}</p>
            <p>{patient.insurance}</p>
            <button onClick={() => handleSelect(patient.id)}>Select</button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default PatientCard;
