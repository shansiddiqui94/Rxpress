// //This where the content for the Modal will live:
// import React, { useState, useEffect } from 'react';

// const ReviewModalContent = ({ patient }) => {
//   const [prescription, setPrescription] = useState(null); 

//   useEffect(() => {
//     const fetchPrescription = async () => {
//       // Replace with the correct prescription ID
//       const prescriptionId = patient.prescriptionId; // Assuming patient has this info

//       try {
//         const response = await fetch(`http://127.0.0.1:5555/prescriptions/${prescriptionId}`);
//         if (!response.ok) {
//           throw new Error(`Request failed with status ${response.status}`);
//         }
//         const data = await response.json();
//         setPrescription(data);
//       } catch (error) {
//         console.error("Error fetching prescription:", error);
//         // Handle errors 
//       }
//     };

//     if (patient) { // Fetch if patient data is available
//       fetchPrescription();
//     }
//   }, [patient]);

//   // ... rest of your modal content (display, update form)
// };

// export default ReviewModalContent;


import React from 'react';

const ReviewModalContent = ({ patient }) => {
  // Implement your UI structure here, using patient data to display prescriptions etc.
  // Consider using a CSS grid or flexbox for layout

  return (
    <div className="review-modal-content">
      <h2>Patient Review</h2>
      {/* Display patient information, prescriptions, updated Rx information here */}
    </div>
  );
};

export default ReviewModalContent;
