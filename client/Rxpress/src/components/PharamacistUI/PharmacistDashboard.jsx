
// Search feature will be here 
// Logic for Patient card will also be here
//Logic for fetching and opening the Review Modal

import { useState, useEffect } from 'react';
import SearchBar from './SearchBar.jsx';
import PatientCard from './PatientCard';
import './dashboard.css'; 

function PharmacistDashboard() {
  const [patients, setPatients] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [isLoading, setIsLoading] = useState(false); 

  useEffect(() => {
    const initialFetch = () => {
      setIsLoading(true);

      fetch('http://127.0.0.1:5555/patients/search') // Initial fetch without query
        .then((res) => res.json())
        .then((data) => {
          setPatients(data);
        })
        .catch((error) => {
          console.error("Error fetching:", error);
          // Handle the error appropriately 
        })
        .finally(() => {
          setIsLoading(false);
        });
    };

    initialFetch(); 
  }, []);

  const handleSearch = (searchQuery) => {
    if (!searchQuery) return; // No fetch if search is empty

    setIsLoading(true);

    const encodedSearchTerm = encodeURIComponent(searchQuery);
    fetch(`http://127.0.0.1:5555/patients/search?name=${encodedSearchTerm}`)
      .then((res) => res.json())
      .then((data) => {
        setPatients(data);
      })
      .catch((error) => {
        console.error("Error fetching:", error);
        // Handle the error appropriately 
      })
      .finally(() => {
        setIsLoading(false);
      });
  };


  return (
    <div className="dashboard-container"> 
     <SearchBar
         onSearch={handleSearch}
         searchTerm={searchTerm} // Pass the current searchTerm state
         onSearchTermChange={handleSearchTermChange}
/>
      <div className="patient-results"> 
        {isLoading ? (
          <p>Loading...</p>   
        ) : patients.length > 0 ? (
          patients.map((patient) => (
            <PatientCard key={patient.id} patient={patient} /> 
          ))
        ) : (
          <p>No patients found.</p> 
        )}
      </div>    
    </div>
  );
}

export default PharmacistDashboard;




// // Using fetch
// const searchPatient = async (name) => {
//   const response = await fetch(`http://127.0.0.1:5555/patients/search?name=${encodeURIComponent(name)}`);
  
//   if (response.ok) { // Check if the request was successful
//     const data = await response.json(); // Parse the JSON response
//     console.log('Patients found:', data); // Handle the response data
//   } else {
//     console.error('Error fetching patients:', response.statusText); // Handle error case
//   }
// };

// // Fetch data for Charlie Brown
// searchPatient('Charlie Brown');

// Using axios Note we will be use fetch and .then
// import axios from 'axios';

// const searchPatient = async (name) => {
//   try {
//     const response = await axios.get(`http://127.0.0.1:5555/patients/search`, {
//       params: { name }, // Pass query parameter as object
//     });
//     console.log('Patients found:', response.data); // Handle the response data
//   } catch (error) {
//     console.error('Error fetching patients:', error.message); // Handle error case
//   }
// };

// // Fetch data for Charlie Brown
// searchPatient('Charlie Brown');

