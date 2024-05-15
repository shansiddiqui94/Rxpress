import React, { useState, useEffect } from 'react';
import axios from 'axios';

function DrugSearch() {
  const [searchTerm, setSearchTerm] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [searchError, setSearchError] = useState(null);

  const handleSearchInputChange = (event) => {
    setSearchTerm(event.target.value);
  };

  useEffect(() => {
    // Implement debouncing or throttling for search requests if desired 

    const performSearch = async () => {
      if (!searchTerm) { 
        setSearchResults([]);
        return; 
      }

      setIsLoading(true);
      setSearchError(null);

      try {
        const response = await axios.get(`http://127.0.0.1:5555/drugs?name=${searchTerm}`);
        setSearchResults(response.data);
      } catch (error) {
        setSearchError('Error fetching drugs. Please try again.');
      } finally {
        setIsLoading(false);
      }
    };

    performSearch();
  }, [searchTerm]);

  function handleDrugSelection(selectedDrug) {
    setSelectedDrug(selectedDrug);

}


  return (
    <div>
      <input
        type="text"
        placeholder="Search Drugs"
        value={searchTerm}
        onChange={handleSearchInputChange}
      />

      {isLoading && <p>Loading...</p>}

      {searchError && <p className="error-message">{searchError}</p>}

      <ul>
        {searchResults.map((drug) => (
          <li key={drug.id}>
            {drug.name} 
            {/* Potentially display more details like strength, dosage form */}
            <button onClick={() => handleDrugSelection(drug)}>Select</button> 
          </li>
        ))}
      </ul>
    </div>
  );
}


export default DrugSearch;
