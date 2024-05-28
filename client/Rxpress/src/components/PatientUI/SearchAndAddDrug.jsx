
// V1
// import React, { useState, useEffect } from 'react';
// import './SearchAndAddDrug.css'; // Your CSS file

// function SearchAndAddDrug({ onDrugSelect, patientId, onPrescriptionAdded }) {
//   const [searchTerm, setSearchTerm] = useState('');
//   const [searchResults, setSearchResults] = useState([]);
//   const [isLoading, setIsLoading] = useState(false);
//   const [error, setError] = useState(null);

//   // Function to handle search input changes
//   const handleSearchTermChange = (event) => {
//     setSearchTerm(event.target.value); // Update state with search term from input
//   };

//   // Function to fetch drug search results (called on mount and search term change)
//   const handleSearch = async () => {
//     if (searchTerm) {
//       setIsLoading(true);
//       setError(null);

//       try {
//         console.log(`Searching for drugs with term: ${searchTerm}`);
//         const response = await fetch(`http://127.0.0.1:5555/drugs?name=${searchTerm}`);
        
//         console.log(`Response status: ${response.status}`);
        
//         if (!response.ok) {
//           const errorMessage = await response.text();
//           throw new Error(`Error fetching drugs: ${errorMessage}`);
//         }
        
//         const data = await response.json();
//         console.log(`Fetched drugs: ${JSON.stringify(data)}`);
//         setSearchResults(data);
//       } catch (error) {
//         console.error('Error fetching drugs:', error);
//         setError(error.message); // Update error state for display
//       } finally {
//         setIsLoading(false);
//       }
//     } else {
//       setSearchResults([]); // Clear search results if search term is empty
//       setError(null); // Clear any previous error if search term is empty
//     }
//   };

//   // Function to handle adding a drug to the prescription list
//   const handleAddDrug = (drug) => {
//     onDrugSelect(drug.id); // Notify parent of selected drug
//     onPrescriptionAdded({ drugId: drug.id, patientId }); // Add the drug to the prescription list
//   };

//   // Call handleSearch on component mount (optional, remove if search is triggered by a button)
//   useEffect(() => {
//     handleSearch();
//   }, [searchTerm]); // Fetch drugs when search term changes

//   return (
//     <div className="search-and-add-container">
//       <h2>Search for Drugs</h2>
//       <input
//         type="text"
//         value={searchTerm}
//         onChange={handleSearchTermChange}
//         placeholder="Enter drug name"
//       />

//       <button onClick={handleSearch}>Search</button>

//       {isLoading && <p>Loading...</p>}
//       {error && <p>Error: {error}</p>}

//       {searchResults.length > 0 && (
//         <ul className="search-results">
//           {searchResults.map((drug) => (
//             <li key={drug.id}>
//               {drug.name}
//               <button onClick={() => handleAddDrug(drug)}>Add</button>
//             </li>
//           ))}
//         </ul>
//       )}
//     </div>
//   );
// }

// export default SearchAndAddDrug;

// V2:
// import React, { useState, useEffect } from 'react';
// import './SearchAndAddDrug.css'; // Your CSS file

// function SearchAndAddDrug({ onDrugSelect, patientId, onPrescriptionAdded }) {
//   const [searchTerm, setSearchTerm] = useState('');
//   const [searchResults, setSearchResults] = useState([]);
//   const [isLoading, setIsLoading] = useState(false);
//   const [error, setError] = useState(null);

//   const handleSearchTermChange = (event) => {
//     setSearchTerm(event.target.value);
//   };

//   const handleSearch = async () => {
//     if (searchTerm) {
//       setIsLoading(true);
//       setError(null);

//       try {
//         const response = await fetch(`http://127.0.0.1:5555/drugs?name=${searchTerm}`);
//         if (!response.ok) {
//           throw new Error('Error fetching drugs');
//         }
//         const data = await response.json();
//         setSearchResults(data);
//       } catch (error) {
//         setError(error.message);
//       } finally {
//         setIsLoading(false);
//       }
//     } else {
//       setSearchResults([]);
//       setError(null);
//     }
//   };

//   const handleAddDrug = async (drug) => {
//     const pharmacistId = 1; // Set this to an appropriate value or fetch dynamically
//     const instructions = 'Default instructions'; // You can customize this

//     try {
//       const response = await fetch('http://127.0.0.1:5555/prescriptions', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json',
//         },
//         body: JSON.stringify({
//           drug_id: drug.id,
//           patient_id: patientId,
//           pharmacist_id: pharmacistId,
//           instructions: instructions,
//           status: 'Pending'
//         }),
//       });

//       if (!response.ok) {
//         throw new Error('Error adding prescription');
//       }

//       const newPrescription = await response.json();
//       onPrescriptionAdded(newPrescription);
//     } catch (error) {
//       setError(error.message);
//     }
//   };

//   useEffect(() => {
//     handleSearch();
//   }, [searchTerm]);

//   return (
//     <div className="search-and-add-container">
//       <h2>Search for Drugs</h2>
//       <input
//         type="text"
//         value={searchTerm}
//         onChange={handleSearchTermChange}
//         placeholder="Enter drug name"
//       />
//       <button onClick={handleSearch}>Search</button>
//       {isLoading && <p>Loading...</p>}
//       {error && <p>Error: {error}</p>}
//       {searchResults.length > 0 && (
//         <ul className="search-results">
//           {searchResults.map((drug) => (
//             <li key={drug.id}>
//               {drug.name}
//               <button onClick={() => handleAddDrug(drug)}>Add</button>
//             </li>
//           ))}
//         </ul>
//       )}
//     </div>
//   );
// }

// export default SearchAndAddDrug;

// V3
// import React, { useState, useEffect } from 'react';
// import './SearchAndAddDrug.css';

// function SearchAndAddDrug({ onDrugSelect, patientId, onPrescriptionAdded }) {
//   const [searchTerm, setSearchTerm] = useState('');
//   const [searchResults, setSearchResults] = useState([]);
//   const [isLoading, setIsLoading] = useState(false);
//   const [error, setError] = useState(null);

//   const handleSearchTermChange = (event) => {
//     setSearchTerm(event.target.value);
//   };

//   const handleSearch = async () => {
//     if (searchTerm) {
//       setIsLoading(true);
//       setError(null);

//       try {
//         const response = await fetch(`http://127.0.0.1:5555/drugs?name=${searchTerm}`);
//         if (!response.ok) {
//           throw new Error('Error fetching drugs');
//         }
//         const data = await response.json();
//         setSearchResults(data);
//       } catch (error) {
//         setError(error.message);
//       } finally {
//         setIsLoading(false);
//       }
//     } else {
//       setSearchResults([]);
//       setError(null);
//     }
//   };

//   const handleAddDrug = async (drug) => {
//     const pharmacistId = 1; // Set this to an appropriate value or fetch dynamically
//     const instructions = 'Default instructions'; // You can customize this

//     try {
//       const response = await fetch('http://127.0.0.1:5555/prescriptions', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json',
//         },
//         body: JSON.stringify({
//           drug_id: drug.id,
//           patient_id: patientId,
//           pharmacist_id: pharmacistId,
//           instructions: instructions,
//           status: 'Pending'
//         }),
//       });

//       if (!response.ok) {
//         throw new Error('Error adding prescription');
//       }

//       const newPrescription = await response.json();
//       onPrescriptionAdded(newPrescription);
//     } catch (error) {
//       setError(error.message);
//     }
//   };

//   useEffect(() => {
//     handleSearch();
//   }, [searchTerm]);

//   return (
//     <div className="search-and-add-container">
//       <input
//         type="text"
//         value={searchTerm}
//         onChange={handleSearchTermChange}
//         placeholder="Enter drug name"
//       />
//       <button onClick={handleSearch}>Search</button>
//       {isLoading && <p>Loading...</p>}
//       {error && <p>Error: {error}</p>}
//       {searchResults.length > 0 && (
//         <ul className="search-results">
//           {searchResults.map((drug) => (
//             <li key={drug.id}>
//               {drug.name} <button onClick={() => handleAddDrug(drug)}>Add to Basket</button>
//             </li>
//           ))}
//         </ul>
//       )}
//     </div>
//   );
// }

// export default SearchAndAddDrug;

// V4
import React, { useState, useEffect } from 'react';
import './SearchAndAddDrug.css';

function SearchAndAddDrug({ onDrugSelect, patientId, onPrescriptionAdded }) {
  const [searchTerm, setSearchTerm] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSearchTermChange = (event) => {
    setSearchTerm(event.target.value);
  };

  const handleSearch = async () => {
    if (searchTerm) {
      setIsLoading(true);
      setError(null);

      try {
        const response = await fetch(`http://127.0.0.1:5555/drugs?name=${searchTerm}`);
        if (!response.ok) {
          throw new Error('Error fetching drugs');
        }
        const data = await response.json();
        setSearchResults(data);
      } catch (error) {
        setError(error.message);
      } finally {
        setIsLoading(false);
      }
    } else {
      setSearchResults([]);
      setError(null);
    }
  };

  const handleAddDrug = async (drug) => {
    const pharmacistId = 1; // Set this to an appropriate value or fetch dynamically
    const instructions = 'Default instructions'; // You can customize this

    try {
      const response = await fetch('http://127.0.0.1:5555/prescriptions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          drug_id: drug.id,
          patient_id: patientId,
          pharmacist_id: pharmacistId,
          instructions: instructions,
          status: 'Pending'
        }),
      });

      if (!response.ok) {
        throw new Error('Error adding prescription');
      }

      const newPrescription = await response.json();
      onPrescriptionAdded(newPrescription);
    } catch (error) {
      setError(error.message);
    }
  };

  useEffect(() => {
    handleSearch();
  }, [searchTerm]);

  return (
    <div className="search-and-add-container">
      <input
        type="text"
        value={searchTerm}
        onChange={handleSearchTermChange}
        placeholder="Enter drug name"
      />
      <button onClick={handleSearch}>Search</button>
      {isLoading && <p>Loading...</p>}
      {error && <p>Error: {error}</p>}
      {searchResults.length > 0 && (
        <ul className="search-results">
          {searchResults.map((drug) => (
            <li key={drug.id} className="drug-item">
              <div className="drug-info">
                <strong>{drug.name}</strong>
                <p>{drug.description}</p> 
              </div>
              <button onClick={() => handleAddDrug(drug)}>Add to Basket</button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default SearchAndAddDrug;

