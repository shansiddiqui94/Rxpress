import React, { useState, useEffect } from 'react';
import axios from 'axios';


function PatientList() {
  const [patients, setPatients] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [search, setSearch] = useState('');

  useEffect(() => {
    const fetchPatients = async () => { 
      setIsLoading(true); 
      setError(null); 

      try {
        const response = await axios.get('http://127.0.0.1:5555/patients'); 
        setPatients(response.data);
      } catch (error) {
        setError('Error fetching patients. Please try again.'); 
      } finally {
        setIsLoading(false);
      }
    };

    fetchPatients(); 
  }, []);

  const filteredPatients = search
    ? patients.filter((p) => p.name.toLowerCase().includes(search.toLowerCase()))
    : patients;

  return (
    <div>
      <h2>Patient List</h2>
      {/* Add a search input here */}
      <input
        type="text"
        placeholder="Search Patients"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

      {isLoading && <p>Loading patients...</p>} 

      {error && <p className="error-message">{error}</p>} 

      <ul>
        {filteredPatients.map((patient) => (
          <li key={patient.id}>
              {patient.name} 
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PatientList;
