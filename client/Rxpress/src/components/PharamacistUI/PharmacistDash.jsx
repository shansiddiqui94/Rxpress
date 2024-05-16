// import React, { useState, useEffect } from 'react';
// import PatientCard from './PatientCard';

// function PharmacistDash() {
//   const [searchTerm, setSearchTerm] = useState('');
//   const [prescriptionData, setPrescriptionData] = useState([]);
//   const [selectedPatientId, setSelectedPatientId] = useState(null);


//   // Define handleSearch function to fetch prescription data
//   const handleSearch = (searchTerm) => {
//     if (searchTerm) {
//       fetch(`http://127.0.0.1:5555/patients/search?name=${searchTerm}`)
//         .then(res => res.json())
//         .then(data => {
//           // Perform chained fetch to fetch prescriptions based on patient data
//           const prescriptionPromises = data.map(patient => {
//             return fetch(`http://127.0.0.1:5555/patients/${patient.id}/prescriptions`)
//               .then(res => res.json());
//           });

//           Promise.all(prescriptionPromises)
//             .then(prescriptionData => {
//               // Set fetched prescription data
//               setPrescriptionData(prescriptionData);
//             })
//             .catch(error => console.error('Error fetching prescription data:', error));
//         })
//         .catch(error => console.error('Error fetching patient data:', error));
//     }
//   };

//   useEffect(() => {
//     // Call handleSearch when searchTerm changes
//     handleSearch(searchTerm);
//   }, [searchTerm]);

//   return (
//     <div className='PharmacistUI'>
//       <PatientCard
//         setPrescriptionData={setPrescriptionData}
//         handleSearch={handleSearch}
//       />
//       {/* Render other necessary components */}
//     </div>
//   );
// }

// export default PharmacistDash;
//  Pharm dash * modal 
import React, { useState, useEffect } from 'react';
import PatientCard from './PatientCard';
import '/Users/DanielSkies/Development/code/phase-5/Rxpress/client/Rxpress/src/components/PharamacistUI/PharmacistDash.css'

function PharmacistDash() {
  const [searchTerm, setSearchTerm] = useState('');
  const [prescriptionData, setPrescriptionData] = useState([]);
  const [selectedPatientId, setSelectedPatientId] = useState('');

  // Define handleSearch function to fetch prescription data
  const handleSearch = (searchTerm) => {
    if (searchTerm) {
      fetch(`http://127.0.0.1:5555/patients/search?name=${searchTerm}`)
        .then(res => res.json())
        .then(data => {
          // Perform chained fetch to fetch prescriptions based on patient data
          const prescriptionPromises = data.map(patient => {
            return fetch(`http://127.0.0.1:5555/patients/${patient.id}/prescriptions`)
              .then(res => res.json());
          });

          Promise.all(prescriptionPromises)
            .then(prescriptionData => {
              // Set fetched prescription data
              setPrescriptionData(prescriptionData);
            })
            .catch(error => console.error('Error fetching prescription data:', error));
        })
        .catch(error => console.error('Error fetching patient data:', error));
    }
  };

  useEffect(() => {
    // Call handleSearch when searchTerm changes
    handleSearch(searchTerm);
  }, [searchTerm]);

  // Define function to handle patient selection
  const handleSelectPatient = (patientId) => {
    console.log('Selected patient:', patientId);
    setSelectedPatientId(patientId);
  };

  useEffect(() => {
    // Fetch prescriptions when selectedPatientId changes
    if (selectedPatientId) {
      console.log('Fetching prescription data for patient:', selectedPatientId);
      fetch(`http://127.0.0.1:5555/patients/${selectedPatientId}/prescriptions`)
        .then(res => res.json())
        .then(prescriptionData => {
          console.log('Fetched prescription data:', prescriptionData);
          setPrescriptionData(prescriptionData);
        })
        .catch(error => console.error('Error fetching prescription data:', error));
    }
  }, [selectedPatientId]);
  

  return (
    <div className='PharmacistUI'>
      <PatientCard onSelect={handleSelectPatient} />
      <div className='prescription-container'>
      {/* Render the prescription data */}
      {prescriptionData.map((prescription, index) => (
       <div className="prescription-card" key={index}>
       <h3>Prescription {index + 1}</h3>
       <p>Medication: {prescription.drug.name}</p>
       <p>Dosage: {prescription.drug.dosage_form}</p>
       <p></p>
       <p></p>
       <p></p>
       <p>Status: {prescription.status}</p>
     </div>  
      ))}
    </div>
    </div>
  );
}

export default PharmacistDash;
