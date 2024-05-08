
// ++++++++++++++++___________________SearchBar Revised__________________+++++++++++++++

import React from 'react';
import './SearchBar.css';

const SearchBar = ({ onSearch, searchTerm, onSearchTermChange }) => {
  const handleInputChange = (event) => {
    const value = event.target.value;
    onSearchTermChange(value); // Update the search term
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if (searchTerm) {
      onSearch(searchTerm); // Trigger search when form is submitted
    }
  };

  return (
    <form onSubmit={handleSubmit} className="search-form">
      <input
        className='searchbox'
        type="text"
        placeholder="Search patient by name"
        value={searchTerm} // Pass the searchTerm from props
        onChange={handleInputChange}
      />
      <button type="submit">Search</button>
    </form>
  );
};

export default SearchBar;
