import './App.css'
import { useState } from 'react'
import PharmacistDashboard from './components/PharamacistUI/PharmacistDashboard'
import EditInformationModal from './components/PharamacistUI/PharmModal/EditInformationModal'

function App() {
  const [openModal, setOpenModal] = useState(false);
  const [patientId, setPatientId] = useState(null);
  const [prescriptions, setPrescriptions] = useState(null); // State to store prescriptions

  const handleOpenModal = (patientId) => {
    setPatientId(patientId);
    setOpenModal(true);
  };

  const handleFetchPrescriptions = (prescriptions) => {
    setPrescriptions(prescriptions); // Store fetched prescriptions
  };

  return (
    <>
      <div>
        <PharmacistDashboard onOpenModal={handleOpenModal} onFetchPrescriptions={handleFetchPrescriptions} /> 
        {openModal && (
          <EditInformationModal
            patientId={patientId}
            prescriptions={prescriptions}  // Pass prescriptions here!
            onClose={() => { 
              setOpenModal(false);
              setPrescriptions(null); // Reset prescriptions when closing
            }}
          />
        )}
      </div>
    </>
  );
}

export default App;
