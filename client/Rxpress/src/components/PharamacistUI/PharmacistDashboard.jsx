
import { useEffect, useState } from 'react';
import SearchBar from './SearchBar';
import PatientCard from './PatientCard';
import fetchPatientPrescriptions from './PharmModal/fetchPatientPrescriptions';
import './dashboard.css';
import PatientPrescriptions from './PatientPrescriptions'; // Import the new component

function PharmacistDashboard({ onOpenModal }) {
  const [patients, setPatients] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null); // To hold any fetch error
  const [selectedPatientId, setSelectedPatientId] = useState(null); // Track selected patient
  const [prescriptions, setPrescriptions] = useState([])

  // Function to fetch patients based on a search term
  const fetchPatients = (query = '') => {
    setIsLoading(true);
    setError(null);


    const handleSearch = (query) => {
      if (query) {
        fetchPatients(query); // Fetch patients based on the search term
      }
    };
  
    const handlePatientSelection = (patientId) => {
      setSelectedPatientId(patientId);
      setPrescriptions(null) // Update selected patient ID
    };

    // Construct the endpoint with optional query
    const endpoint = query
      ? `http://127.0.0.1:5555/patients/search?name=${encodeURIComponent(query)}`
      : 'http://127.0.0.1:5555/patients/search';

    fetch(endpoint)
      .then((res) => {
        // if (!res.ok) {
        //   throw new Error(`HTTP error! status: ${res.status}`); // Handle non-200 status
        // }
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
  
// This is the handleCardClick function that will fetch our Patients Prescription
const handleCardClick = (patientId) => {
  fetchPatientPrescriptions(patientId)
      .then(prescriptions => {
          openModal(patientId, prescriptions); // Pass both patientId and prescriptions
      })
      .catch(error => {
          // Handle fetch errors
      });
};

const handlePatientSelection = (patientId) => {
  setSelectedPatientId(patientId); // Update selected patient ID state
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
      ) : error ? (
        <p>{`Error: ${error}`}</p>
      ) : patients.length > 0 ? (
        patients.map((patient) => (
          
          <PatientCard
  key={patient.id}
  patient={patient}
  onPatientSelection={handlePatientSelection}
  selected={patient.id === selectedPatientId}
  fetchPrescriptions={(patientId) => {
    // Function to trigger the fetch
    setIsLoading(true);
    fetchPatientPrescriptions(patientId)
      .then((prescriptions) => setPrescriptions(prescriptions))
      .catch((error) => setError(error.message)) // Update error state if needed
      .finally(() => setIsLoading(false));
  }}
/>

        ))
      ) : (
        <p>No patients found!!!!</p>
      )}
    </div>
    {/* Conditionally render PatientPrescriptions component */}
    {selectedPatientId && (
      <PatientPrescriptions
        patientId={selectedPatientId}
        prescriptions={prescriptions} // Pass prescriptions fetched from PatientCard
      />
    )}
  </div>
  );
}

export default PharmacistDashboard;

// _________________REVISED PHARMACY DASHBOARD________________________________

// import { useEffect, useState } from 'react';
// import SearchBar from './SearchBar';
// import PatientCard from './PatientCard';
// import './dashboard.css';

// function PharmacistDashboard({ onOpenModal }) { // Rename to onOpenModal if unused
//   const [patients, setPatients] = useState([]);
//   const [searchTerm, setSearchTerm] = useState('');
//   const [isLoading, setIsLoading] = useState(false);
//   const [error, setError] = useState(null); // To hold any fetch error

//   // Function to fetch patients based on a search term
//   const fetchPatients = (query = '') => {
//     setIsLoading(true);
//     setError(null);

//     // Construct the endpoint with optional query
//     const endpoint = query
//       ? `http://127.0.0.1:5555/patients/search?name=${encodeURIComponent(query)}`
//       : 'http://127.0.0.1:5555/patients/search';

//     fetch(endpoint)
//       .then((res) => {
//         return res.json();
//       })
//       .then((data) => {
//         setPatients(data);
//       })
//       .catch((err) => {
//         console.error('Error fetching:', err);
//         setError(err.message); // Update the error state
//       })
//       .finally(() => {
//         setIsLoading(false);
//       });
//   };

//   // Initial fetch on component mount
//   useEffect(() => {
//     fetchPatients(); // Fetch all patients initially
//   }, []);

//   const handleSearch = (query) => {
//     if (query) {
//       fetchPatients(query); // Fetch patients based on the search term
//     }
//   };

//   // Fetch patient prescriptions function
//   const fetchPatientPrescriptions = (patientId) => {
//     const baseURL = 'http://127.0.0.1:5555'; 
//     const url = `${baseURL}/patients/${patientId}/prescriptions`; 

//     return fetch(url) 
//       .then((response) => {
//         if (!response.ok) {
//           throw new Error(`Failed to fetch prescriptions (status: ${response.status})`);
//         }
//         return response.json(); 
//       })
//       .catch((error) => {
//         console.error("Error fetching prescriptions:", error);
//         throw error; // Rethrow to allow catching within PatientCard
//       });
//   };

//   return (
//     <div className="dashboard-container">
//       <SearchBar
//         onSearch={handleSearch}
//         searchTerm={searchTerm}
//         onSearchTermChange={setSearchTerm}
//       />
//       <div className="patient-results">

//         {isLoading ? (
//           <p>Loading...</p>
//         ) : error ? ( // Display an error message if there's an error
//           <p>{`Error: ${error}`}</p>
//         ) : patients.length > 0 ? (
//           patients.map((patient) => (
//             <PatientCard  
//                 key={patient.id} 
//                 patient={patient} 
//                 fetchPrescriptions={fetchPatientPrescriptions} 
//             /> 
//           ))
//         ) : (
//           <p>No patients found!!!!</p>
//         )}
//       </div>
//     </div>
//   );
// }

// export default PharmacistDashboard;
