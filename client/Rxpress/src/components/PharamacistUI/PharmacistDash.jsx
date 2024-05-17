// import React, { useState, useEffect } from 'react';
// import PatientCard from './PatientCard';
// import '/Users/DanielSkies/Development/code/phase-5/Rxpress/client/Rxpress/src/components/PharamacistUI/PharmacistDash.css';
// // Remove the import statement for PrescriptionModal

// function PharmacistDash() {
//   // State variables
//   const [searchTerm, setSearchTerm] = useState('');
//   const [prescriptionData, setPrescriptionData] = useState([]);
//   const [selectedPatientId, setSelectedPatientId] = useState('');
//   const [modalOpen, setModalOpen] = useState(false);
//   const [selectedPrescription, setSelectedPrescription] = useState(null);

//   // Function to handle patient search
//   const handleSearch = (searchTerm) => {
//     if (searchTerm) {
//       // Fetch patients matching the search term
//       fetch(`http://127.0.0.1:5555/patients/search?name=${searchTerm}`)
//         .then(res => res.json())
//         .then(data => {
//           // Fetch prescriptions for each patient
//           const prescriptionPromises = data.map(patient => {
//             return fetch(`http://127.0.0.1:5555/patients/${patient.id}/prescriptions`)
//               .then(res => res.json());
//           });
//           // Set prescription data when all prescriptions are fetched
//           Promise.all(prescriptionPromises)
//             .then(prescriptionData => {
//               setPrescriptionData(prescriptionData.flat());
//             })
//             .catch(error => console.error('Error fetching prescription data:', error));
//         })
//         .catch(error => console.error('Error fetching patient data:', error));
//     }
//   };

//   // Effect hook to trigger search when searchTerm changes
//   useEffect(() => {
//     handleSearch(searchTerm);
//   }, [searchTerm]);

//   // Function to handle selection of a patient
//   const handleSelectPatient = (patientId) => {
//     setSelectedPatientId(patientId);
//     setModalOpen(true);
//   };

//   // Effect hook to fetch prescriptions when selectedPatientId changes
//   useEffect(() => {
//     if (selectedPatientId) {
//       fetch(`http://127.0.0.1:5555/patients/${selectedPatientId}/prescriptions`)
//         .then(res => res.json())
//         .then(prescriptionData => {
//           setPrescriptionData(prescriptionData);
//         })
//         .catch(error => console.error('Error fetching prescription data:', error));
//     }
//   }, [selectedPatientId]);

//   // Function to handle updating a prescription
//   const handleUpdatePrescription = (prescriptionId, newStatus, newInstructions) => {
//     fetch(`http://127.0.0.1:5555/prescriptions/${prescriptionId}`, {
//       method: 'PATCH',
//       headers: {
//         'Content-Type': 'application/json',
//       },
//       body: JSON.stringify({ status: newStatus, instructions: newInstructions }),
//     })
//       .then(res => res.json())
//       .then(updatedPrescription => {
//         setPrescriptionData(prescriptions =>
//           prescriptions.map(pres =>
//             pres.id === updatedPrescription.id ? updatedPrescription : pres
//           )
//         );
//       })
//       .catch(error => console.error('Error updating prescription:', error));
//   };

//   // Function to handle status change of a prescription
//   const handleStatusChange = (prescriptionId, newStatus) => {
//     const prescription = prescriptionData.find(pres => pres.id === prescriptionId);
//     handleUpdatePrescription(prescriptionId, newStatus, prescription.instructions);
//   };

//   // Function to handle instructions change of a prescription
//   const handleInstructionsChange = (prescriptionId, newInstructions) => {
//     const prescription = prescriptionData.find(pres => pres.id === prescriptionId);
//     handleUpdatePrescription(prescriptionId, prescription.status, newInstructions);
//   };

//   // Return JSX
//   return (
//     <div className='PharmacistUI'>
//       {/* Render the PatientCard component */}
//       <PatientCard onOpenModal={handleSelectPatient} />
//       <div className='prescription-container'>
//         {/* Render prescription cards */}
//         {prescriptionData.map((prescription, index) => (
//           <div className="prescription-card" key={prescription.id}>
//             <h3>Prescription {index + 1}</h3>
//             <p>Medication: {prescription.drug.name}</p>
//             <p>Dosage: {prescription.drug.dosage_form}</p>
//             <p>Status: 
//               <select 
//                 value={prescription.status} 
//                 onChange={(e) => handleStatusChange(prescription.id, e.target.value)}
//                 style={{ color: prescription.status === 'approved' ? 'green' : 'black' }}
//               >
//                 <option value="pending">Pending</option>
//                 <option value="approved" style={{ color: 'green' }}>Approved</option>
//                 <option value="rejected" style={{ color: 'red' }}>Rejected</option>
//               </select>
//             </p>
//             <p>Instructions: 
//               <input 
//                 type="text" 
//                 value={prescription.instructions || ''} 
//                 onChange={(e) => handleInstructionsChange(prescription.id, e.target.value)} 
//               />
//             </p>
//           </div>
//         ))}
//       </div>
//       {/* Remove the PrescriptionModal component rendering */}
//     </div>
//   );
// }

// export default PharmacistDash;


import React, { useState, useEffect } from 'react';
import PatientCard from './PatientCard';
import '/Users/DanielSkies/Development/code/phase-5/Rxpress/client/Rxpress/src/components/PharamacistUI/PharmacistDash.css';

function PharmacistDash() {
  const [searchTerm, setSearchTerm] = useState('');
  const [prescriptionData, setPrescriptionData] = useState([]);
  const [selectedPatientId, setSelectedPatientId] = useState('');
 

  const handleSearch = (searchTerm) => {
    if (searchTerm) {
      fetch(`http://127.0.0.1:5555/patients/search?name=${searchTerm}`)
        .then(res => res.json())
        .then(data => {
          const prescriptionPromises = data.map(patient => {
            return fetch(`http://127.0.0.1:5555/patients/${patient.id}/prescriptions`)
              .then(res => res.json());
          });
          Promise.all(prescriptionPromises)
            .then(prescriptionData => {
              setPrescriptionData(prescriptionData.flat());
            })
            .catch(error => console.error('Error fetching prescription data:', error));
        })
        .catch(error => console.error('Error fetching patient data:', error));
    }
  };

  useEffect(() => {
    handleSearch(searchTerm);
  }, [searchTerm]);

  const handleSelectPatient = (patientId) => {
    setSelectedPatientId(patientId);
    setModalOpen(true);
  };

  useEffect(() => {
    if (selectedPatientId) {
      fetch(`http://127.0.0.1:5555/patients/${selectedPatientId}/prescriptions`)
        .then(res => res.json())
        .then(prescriptionData => {
          setPrescriptionData(prescriptionData);
        })
        .catch(error => console.error('Error fetching prescription data:', error));
    }
  }, [selectedPatientId]);

  const handleUpdatePrescription = (prescriptionId, newStatus, newInstructions) => {
    fetch(`http://127.0.0.1:5555/prescriptions/${prescriptionId}`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ status: newStatus, instructions: newInstructions }),
    })
      .then(res => res.json())
      .then(updatedPrescription => {
        setPrescriptionData(prescriptions =>
          prescriptions.map(pres =>
            pres.id === updatedPrescription.id ? updatedPrescription : pres
          )
        );
      })
      .catch(error => console.error('Error updating prescription:', error));
  };

  const handleStatusChange = (prescriptionId, newStatus) => {
    const prescription = prescriptionData.find(pres => pres.id === prescriptionId);
    handleUpdatePrescription(prescriptionId, newStatus, prescription.instructions);
  };

  const handleInstructionsChange = (prescriptionId, newInstructions) => {
    const prescription = prescriptionData.find(pres => pres.id === prescriptionId);
    handleUpdatePrescription(prescriptionId, prescription.status, newInstructions);
  };

  return (
    <div className='PharmacistUI'>
      <PatientCard onOpenModal={handleSelectPatient} />
      <div className='prescription-container'>
        {prescriptionData.map((prescription, index) => (
          <div className="prescription-card" key={prescription.id}>
            <h3>Prescription {index + 1}</h3>
            <p>Medication: {prescription.drug.name}</p>
            <p>Dosage: {prescription.drug.dosage_form}</p>
            <p>Status: {prescription.status}
              <select 
                value={prescription.status} 
                onChange={(e) => handleStatusChange(prescription.id, e.target.value)}
                style={{ color: prescription.status === 'approved' ? 'green' : 'black' }}
              >
                <option value="pending">Pending</option>
                <option value="approved" style={{ color: 'green' }}>Approved</option>
                <option value="rejected" style={{ color: 'red' }}>Rejected</option>
              </select>
            </p>
            <p>Instructions: 
                 <textarea 
                  value={prescription.instructions || ''} 
                  onChange={(e) => handleInstructionsChange(prescription.id, e.target.value)}
                  rows={4} 
                  style={{ width: '100%' }} 
                  />
             </p>
          </div>
        ))}
      </div>
      
    </div>
  );
}

export default PharmacistDash;
