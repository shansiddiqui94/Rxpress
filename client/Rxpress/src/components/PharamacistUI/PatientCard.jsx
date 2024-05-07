 import React from 'react';
 import './PatientCard.css';

 const PatientCard = ({ patient }) => {
   return (
     <div className="patient-card">
       <div className="info-container">
        <h3 className="card-title">{patient.name}</h3>
         <p className="card-des">Address: {patient.address}</p> 
         {/* Add more fields as needed */}
       </div>
    </div>
  );
 };

 export default PatientCard;

// import React from 'react';
// import './TShirts.css'; // Importing the updated CSS stylesheet

// const PatientCard = ({ patient }) => {
//   if (!patient) {
//     return <p>No patient information available.</p>; // Handle cases where patient data is missing
//   }

//   const { name = 'Unknown', address = 'Not Provided' } = patient;

//   return (
//     <div className="card"> {/* Applying the 'card' class for consistent styling */}
//       <div className="info-container"> {/* Using the 'info-container' class for the main content */}
//         <h3 className="card-title">{name}</h3> {/* Applying 'card-title' styling */}
//         <p className="card-des">Address: {address}</p> {/* Applying 'card-des' for descriptions */}
//         <p className="card-des">Contact: {contact}</p> {/* Additional patient information */}
//       </div>
//     </div>
//   );
// };

// export default PatientCard;
