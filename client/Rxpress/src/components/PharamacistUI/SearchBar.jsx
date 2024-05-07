import React, { useState } from 'react';
import './SearchBar.css'; // Add your styling

const SearchBar = ({ onSearch, onSearchTermChange, searchTerm }) => {
  const [searchTerm, setSearchTerm] = useState(''); // Initialize searchTerm state

  const handleInputChange = (event) => {
    setSearchTerm(event.target.value);
    // Also call onSearchTermChange if you want live search updates
    if (onSearchTermChange) {
      onSearchTermChange(event.target.value);
    }
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if (searchTerm) {  // Ensure searchTerm has a value before calling onSearch
      onSearch(searchTerm);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="search-form">
      <input
        type="text"
        placeholder="Search patient by name"
        value={searchTerm}  // Access the state variable here
        onChange={handleInputChange}
      />
      <button type="submit">Search</button>
    </form>
  );
};

export default SearchBar;
