// PrescriptionItem.jsx
import React from 'react';

function PrescriptionItem({ prescription }) {
  return (
    <div className="prescription-item">
      {/* Access and render prescription properties here */}
      <p>Prescription ID: {prescription.id}</p> 
      <p>Drug: {prescription.drug.name}</p>
      <p>Instructions: {prescription.instructions}</p>
      {/* Add more prescription details as needed */}
    </div>
  );
}

export default PrescriptionItem;
