import React from 'react';
import './SearchBar.css';

const PatientCard = ({ patient }) => {
  return (
    <div className="patient-card">
      <h3>{patient.name}</h3>
      <p>Address: {patient.address}</p> 
      {/* Add more fields as needed */}
    </div>
  );
};

export default PatientCard;