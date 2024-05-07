// import React, { useState } from 'react';
// import './SearchBar.css'; // Add your styling

// const SearchBar = ({ onSearch, onSearchTermChange, searchTerm }) => {
//   const [searchTerm, setSearchTerm] = useState(''); // Initialize searchTerm state

//   const handleInputChange = (event) => {
//     setSearchTerm(event.target.value);
//     // Also call onSearchTermChange if you want live search updates
//     if (onSearchTermChange) {
//       onSearchTermChange(event.target.value);
//     }
//   };

//   const handleSubmit = (event) => {
//     event.preventDefault();
//     if (searchTerm) {  // Ensure searchTerm has a value before calling onSearch
//       onSearch(searchTerm);
//     }
//   };

//   return (
//     <form onSubmit={handleSubmit} className="search-form">
//       <input
//         type="text"
//         placeholder="Search patient by name"
//         value={searchTerm}  // Access the state variable here
//         onChange={handleInputChange}
//       />
//       <button type="submit">Search</button>
//     </form>
//   );
// };

// export default SearchBar;

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
