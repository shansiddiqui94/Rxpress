// import React, { useState, useEffect } from 'react';
// import './SearchAndAddDrug.css'; // Your CSS file

// const SearchAndAddDrug = () => {
//   const [searchTerm, setSearchTerm] = useState('');
//   const [searchResults, setSearchResults] = useState([]);
//   const [isLoading, setIsLoading] = useState(false);
//   const [error, setError] = useState(null);

//   // Function to fetch drug search results 
//   const handleSearch = () => {
//     if (searchTerm) {
//       setIsLoading(true);
//       setError(null);

//       fetch(`http://127.0.0.1:5555/api/drugs?name=${searchTerm}`)
//         .then((response) => {
//           if (!response.ok) {
//             throw new Error('Error fetching drugs');
//           }
//           return response.json();
//         })
//         .then((data) => {
//           setSearchResults(data);
//         })
//         .catch((error) => {
//           setError(error.message); 
//         })
//         .finally(() => {
//           setIsLoading(false);
//         });
//     }
//   };

//   // Function to handle adding a drug to the basket
//   const handleAddPrescription = (drug) => {
//     // API request to create a new prescription with 'pending' status
//     // ... implementation here ...
//   };

//   return (
//     <div className="search-and-add-container">
//       <h2>Search for Drugs</h2>

//       <input 
//         type="text" 
//         value={searchTerm} 
//         onChange={(e) => setSearchTerm(e.target.value)} 
//         placeholder="Enter drug name"
//       />

//       <button onClick={handleSearch}>Search</button>

//       {isLoading && <p>Loading...</p>}
//       {error && <p>Error: {error}</p>}

//       {searchResults.length > 0 && (
//   <ul className="search-results">
//     {searchResults.map((drug) => (
//       <li key={drug.id}>
//         {drug.name} {/* Display only the drug name */}
//         <button onClick={() => handleAddPrescription(drug)}>Add to Basket</button>
//       </li>
//     ))}
//   </ul>
//       )}
//     </div>
//   );
// };

// export default SearchAndAddDrug;

import React, { useState, useEffect } from 'react';
import './SearchAndAddDrug.css'; // Your CSS file

function SearchAndAddDrug({ onDrugSelect, patientId, onPrescriptionAdded }) {
  const [searchTerm, setSearchTerm] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  // Function to handle search input changes
  const handleSearchTermChange = (event) => {
    setSearchTerm(event.target.value); // Update state with search term from input
  };

  // Function to fetch drug search results (called on mount and search term change)
  const handleSearch = async () => {
    if (searchTerm) {
      setIsLoading(true);
      setError(null);

      try {
        console.log(`Searching for drugs with term: ${searchTerm}`);
        const response = await fetch(`http://127.0.0.1:5555/drugs?name=${searchTerm}`);
        
        console.log(`Response status: ${response.status}`);
        
        if (!response.ok) {
          const errorMessage = await response.text();
          throw new Error(`Error fetching drugs: ${errorMessage}`);
        }
        
        const data = await response.json();
        console.log(`Fetched drugs: ${JSON.stringify(data)}`);
        setSearchResults(data);
      } catch (error) {
        console.error('Error fetching drugs:', error);
        setError(error.message); // Update error state for display
      } finally {
        setIsLoading(false);
      }
    } else {
      setSearchResults([]); // Clear search results if search term is empty
      setError(null); // Clear any previous error if search term is empty
    }
  };

  // Function to handle adding a drug to the prescription list
  const handleAddDrug = (drug) => {
    onDrugSelect(drug.id); // Notify parent of selected drug
    onPrescriptionAdded({ drugId: drug.id, patientId }); // Add the drug to the prescription list
  };

  // Call handleSearch on component mount (optional, remove if search is triggered by a button)
  useEffect(() => {
    handleSearch();
  }, [searchTerm]); // Fetch drugs when search term changes

  return (
    <div className="search-and-add-container">
      <h2>Search for Drugs</h2>
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
            <li key={drug.id}>
              {drug.name}
              <button onClick={() => handleAddDrug(drug)}>Add</button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default SearchAndAddDrug;

