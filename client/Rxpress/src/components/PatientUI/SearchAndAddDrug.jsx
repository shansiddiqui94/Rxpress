import React, { useState, useEffect } from 'react';
import './SearchAndAddDrug.css'; // Your CSS file

const SearchAndAddDrug = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  // Function to fetch drug search results 
  const handleSearch = () => {
    if (searchTerm) {
      setIsLoading(true);
      setError(null);

      fetch(`http://127.0.0.1:5555/api/drugs?name=${searchTerm}`)
        .then((response) => {
          if (!response.ok) {
            throw new Error('Error fetching drugs');
          }
          return response.json();
        })
        .then((data) => {
          setSearchResults(data);
        })
        .catch((error) => {
          setError(error.message); 
        })
        .finally(() => {
          setIsLoading(false);
        });
    }
  };

  // Function to handle adding a drug to the basket
  const handleAddPrescription = (drug) => {
    // API request to create a new prescription with 'pending' status
    // ... implementation here ...
  };

  return (
    <div className="search-and-add-container">
      <h2>Search for Drugs</h2>

      <input 
        type="text" 
        value={searchTerm} 
        onChange={(e) => setSearchTerm(e.target.value)} 
        placeholder="Enter drug name"
      />

      <button onClick={handleSearch}>Search</button>

      {isLoading && <p>Loading...</p>}
      {error && <p>Error: {error}</p>}

      {searchResults.length > 0 && (
  <ul className="search-results">
    {searchResults.map((drug) => (
      <li key={drug.id}>
        {drug.name} {/* Display only the drug name */}
        <button onClick={() => handleAddPrescription(drug)}>Add to Basket</button>
      </li>
    ))}
  </ul>
      )}
    </div>
  );
};

export default SearchAndAddDrug;
