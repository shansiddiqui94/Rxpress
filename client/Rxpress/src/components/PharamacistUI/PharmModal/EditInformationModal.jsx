import React, { useState, useEffect } from 'react';
import Modal from './ModalContent'; 

const EditInformationModal = ({ onClose, patientId, prescriptions }) => {
  const [isModalOpen, setModalOpen] = useState(false);
  const [prescriptionData, setPrescriptionData] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  
  useEffect(() => {
    const fetchPrescription = () => { 
      if (!patientId) return; // Stop if there's no patientId

      setIsLoading(true);

      fetch(`http://127.0.0.1:5555/prescriptions/${patientId}`) 
        .then(response => {
          if (!response.ok) {
            throw new Error('Failed to fetch prescription');
          }
          return response.json();
        })
        .then(data => {
          setPrescriptionData({ 
            medication: data.drug,  
            dosage: data.instructions, 
          });
        })
        .catch(error => {
          console.error('Error fetching prescription:', error); 
        })
        .finally(() => {
          setIsLoading(false);
        });
    };

    // Call the fetch function when the modal opens & patientId exists
    fetchPrescription(); 

  }, [patientId]);

  const openModal = (id) => {
    setPatientId(id);
    setModalOpen(true);
    console.log("helllo")
  };

  const closeModal = () => {
    setModalOpen(false); 
    setPatientId(null); 
    setPrescriptionData(null);
  };


  // const originalContent = (
  //   <div>
  //     <p>Information to be updated:</p>
  //     <ul>
  //       <li>Update patient name</li>
  //       <li>Update age</li>
  //       <li>Update condition</li>
  //     </ul>
  //   </div>
  // );

  const updatedContent = (
    <div>
      <p>Updated information:</p>
      <ul>
        <li>Name: John Doe</li>
        <li>Age: 30</li>
        <li>Condition: Hypertension</li>
      </ul>
    </div>
  );

  return ( // The return statement!
  <div className="flex min-h-screen flex-col items-center justify-center py-12">
  <button 
    className="bg-blue-500 text-white px-8 py-4 rounded"
    onClick={() => openModal(patientId)} 
  >
    Open Edit Modal
  </button> 

  {/* Conditional Rendering of Modal */}
  {isModalOpen && ( 
    <Modal
      // ... existing props 
      leftContent={isLoading ? <p>Loading prescription...</p> : 
                   prescriptions ? ( 
                     <div>
                       <p>Prescription:</p>
                       <ul>
                         {prescriptions.map(prescription => (
                           <li key={prescription.id}>
                             Medication: {prescription.drug.name} 
                             Dosage: {prescription.instructions} 
                           </li>
                         ))}
                       </ul> 
                     </div> 
                   ) : (
                     <p>No prescriptions found.</p> 
                   )
                 }
    />
  )} 
</div>
  );
};

export default EditInformationModal;
