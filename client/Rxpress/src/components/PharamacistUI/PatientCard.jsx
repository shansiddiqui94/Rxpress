import React, { useState, useEffect } from 'react';
import './PatientCard.css';
import fetchPatientPrescriptions from './PharmModal/fetchPatientPrescriptions';

const PatientCard = ({ patient, onPatientSelection, selected, fetchedPrescriptions }) => {
  const [prescriptions, setPrescriptions] = useState(fetchedPrescriptions || null); 
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  // Fetch prescriptions for selected patient on mount or selection change
  useEffect(() => {
    const fetchPrescriptionsIfNeeded = async () => {
      if (selected) { // Only fetch when selected
        setIsLoading(true);
        setError(null);

        try {
          const data = await fetchPatientPrescriptions(patient.id);
          setPrescriptions(data);
        } catch (error) {
          console.error("Error fetching prescriptions:", error);
          setError(error.message);
        } finally {
          setIsLoading(false);
        }
      }
    };

    fetchPrescriptionsIfNeeded();
  }, [selected, patient.id]); // Dependencies for triggering the fetch

  
  return (
    <div className={`patient-card ${selected ? 'selected' : ''}`}> 
      <input
        type="checkbox"
        checked={selected}
        onChange={() => onPatientSelection(patient.id)} 
      />
      <h3 className="card-title">{patient.name}</h3> 
      {/* Other patient info elements */} 

      {isLoading && <p>Loading prescriptions...</p>} 
      {error && <p>Error: {error}</p>} 

      {prescriptions && ( 
        <ul>
        {prescriptions.map((prescription) => (
          <li key={prescription.id}>
            <div className="prescription-details"> 
              <h2>Medication: {prescription.drug}</h2>
              <p>Dosage: {prescription.instructions}</p>
              <p>Status: {prescription.status}</p>
              <p>Patient: {prescription.patient.name}</p>
              <p>Pharmacist: {prescription.pharmacist.name}</p> 
            </div>
          </li>
        ))}
      </ul>
      )}
    </div>
  );
};

export default PatientCard;

// ___________________________________PT CARD REVISED_____________________

// import React, { useState, useEffect } from 'react';

// const PatientCard = ({ patient, fetchPrescriptions }) => { 
//   const [prescriptions, setPrescriptions] = useState(null); 
//   const [isLoading, setIsLoading] = useState(false); 
//   const [error, setError] = useState(null); 

//   useEffect(() => {
//     const fetchPatientData = async () => {
//       setIsLoading(true);

//       try {
//         const data = await fetchPrescriptions(patient.id); 
//         setPrescriptions(data);
//       } catch (error) {
//         setError(error.message); 
//       } finally {
//         setIsLoading(false);
//       }
//     };

//     fetchPatientData(); 
//   }, [patient.id]); // Dependency for patientId

//   return (
//     <div className="patient-card">
//       <div className="patient-info"> {/* Container for main patient info */}  
//         {patient.name && <h3 className="card-title">{patient.name}</h3>}
//         {patient.address && <p className="card-des">Address: {patient.address}</p>}
//         {patient.phone && <p className="card-des">Phone: {patient.phone}</p>} 
//       </div>

//       <div className="prescription-container"> {/* Container for prescriptions */}
//         {isLoading && <p>Loading prescriptions...</p>}
//         {error && <p>Error fetching prescriptions</p>}
//         {prescriptions && (
//           <ul> 
//             {/* Render prescription list here */}
//           </ul>
//         )}
//       </div>
//     </div>
//   );
// };

// export default PatientCard;
