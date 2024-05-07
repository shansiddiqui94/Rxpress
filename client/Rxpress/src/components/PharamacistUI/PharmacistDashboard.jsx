
// Search feature will be here 
// Logic for Patient card will also be here
//Logic for fetching and opening the Review Modal

// import { useState, useEffect } from 'react';
// import SearchBar from './SearchBar.jsx';
// import PatientCard from './PatientCard';
// import './dashboard.css'; 

// function PharmacistDashboard() {
//   const [patients, setPatients] = useState([]);
//   const [searchTerm, setSearchTerm] = useState('');
//   const [isLoading, setIsLoading] = useState(false); 

//   useEffect(() => {
//     const initialFetch = () => {
//       setIsLoading(true);

//       fetch('http://127.0.0.1:5555/patients/search') // Initial fetch without query
//         .then((res) => res.json())
//         .then((data) => {
//           setPatients(data);
//         })
//         .catch((error) => {
//           console.error("Error fetching:", error);
//           // Handle the error appropriately 
//         })
//         .finally(() => {
//           setIsLoading(false);
//         });
//     };

//     initialFetch(); 
//   }, []);

//   const handleSearch = (searchQuery) => {
//     if (!searchQuery) return; // No fetch if search is empty

//     setIsLoading(true);

//     const encodedSearchTerm = encodeURIComponent(searchQuery);
//     fetch(`http://127.0.0.1:5555/patients/search?name=${encodedSearchTerm}`)
//       .then((res) => res.json())
//       .then((data) => {
//         setPatients(data);
//       })
//       .catch((error) => {
//         console.error("Error fetching:", error);
//         // Handle the error appropriately 
//       })
//       .finally(() => {
//         setIsLoading(false);
//       });
//   };


//   return (
//     <div className="dashboard-container"> 
//      <SearchBar
//          onSearch={handleSearch}
//          searchTerm={searchTerm} // Pass the current searchTerm state
//          onSearchTermChange={handleSearchTermChange}
// />
//       <div className="patient-results"> 
//         {isLoading ? (
//           <p>Loading...</p>   
//         ) : patients.length > 0 ? (
//           patients.map((patient) => (
//             <PatientCard key={patient.id} patient={patient} /> 
//           ))
//         ) : (
//           <p>No patients found.</p> 
//         )}
//       </div>    
//     </div>
//   );
// }

// export default PharmacistDashboard;




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

// _________________REVISED PHARMACY DASHBOARD________________________________

import { useEffect, useState } from 'react';
import SearchBar from './SearchBar';
import PatientCard from './PatientCard';
import './dashboard.css';

function PharmacistDashboard({ onOpenModal }) {
  const [patients, setPatients] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null); // To hold any fetch error

  // Function to fetch patients based on a search term
  const fetchPatients = (query = '') => {
    setIsLoading(true);
    setError(null);

    // Construct the endpoint with optional query
    const endpoint = query
      ? `http://127.0.0.1:5555/patients/search?name=${encodeURIComponent(query)}`
      : 'http://127.0.0.1:5555/patients/search';

    fetch(endpoint)
      .then((res) => {
        if (!res.ok) {
          throw new Error(`HTTP error! status: ${res.status}`); // Handle non-200 status
        }
        return res.json();
      })
      .then((data) => {
        setPatients(data);
      })
      .catch((err) => {
        console.error('Error fetching:', err);
        setError(err.message); // Update the error state
      })
      .finally(() => {
        setIsLoading(false);
      });
  };

  // Initial fetch on component mount
  useEffect(() => {
    fetchPatients(); // Fetch all patients initially
  }, []);

  const handleSearch = (query) => {
    if (query) {
      fetchPatients(query); // Fetch patients based on the search term
    }
  };

  return (
    <div className="dashboard-container">
      <SearchBar
        onSearch={handleSearch}
        searchTerm={searchTerm}
        onSearchTermChange={setSearchTerm}
      />
      <div className="patient-results">
        {isLoading ? (
          <p>Loading...</p>
        ) : error ? ( // Display an error message if there's an error
          <p>{`Error: ${error}`}</p>
        ) : patients.length > 0 ? (
          patients.map((patient) => (
            <PatientCard  key={patient.id} 
            patient={patient} 
            onOpenModal={onOpenModal} />
          ))
        ) : (
          <p>No patients found.</p>
        )}
      </div>
    </div>
  );
}

export default PharmacistDashboard;
