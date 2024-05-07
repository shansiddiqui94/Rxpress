import './App.css'
import { useState } from 'react'
// import StickyNav from './components/StickyNav'
import PharmacistDashboard from './components/PharamacistUI/PharmacistDashboard'
import EditInformationModal from './components/PharamacistUI/PharmModal/EditInformationModal'
function App() {
  const [openModal, setOpenModal] = useState(false); 
  const [patientId, setPatientId] = useState(null)

  const handleOpenModal = (patientId) => {
    setPatientId(patientId);
    setOpenModal(true);
 }

  return (
    <>
      <div>
        {/* <StickyNav/> */}
        <PharmacistDashboard onOpenModal={handleOpenModal} />
        {openModal && (
       <EditInformationModal 
          onClose={() => setOpenModal(false)} 
          openModal={handleOpenModal} // Pass openModal here
       /> 
    )}

      </div>
    </>
  )
}

export default App
