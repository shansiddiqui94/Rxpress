import React from 'react'
import  { useState } from 'react'
import './PatientCard.css';

const PatientCard = ({ patient, onOpenModal }) => {
  const [openModal, setOpenModal] = useState(false); 
  const [patientId, setPatientId] = useState(null); 

  const handleClick = () => {
    console.log("I HAVE BEEN CLICKED")
    onOpenModal(patient.id); 
    setOpenModal(true);
  };

   

  return (
    <div onClick={handleClick}> 
      <div className="info-container">
        <h3 className="card-title">{patient.name}</h3>
        <p className="card-des">Address: {patient.address}</p> 
      </div>
    </div>
  );
};

export default PatientCard;
