// This Modal will contain the following code
//Displaying original prescription details (left container)
//Providing an update form (right container)
//Handling the submission of prescription updates
import React, { useState } from 'react';
import ReviewModalContent from './ReviewModalContent';
import './ReviewModal.css';

const ReviewModal = ({ patientData, onOpen, onClose }) => {
  const [isOpen, setIsOpen] = useState(false);

  const handleOpen = () => {
    if (onOpen) onOpen(); // Call the function provided for opening logic (optional)
    setIsOpen(true);
  };

  const handleClose = () => {
    setIsOpen(false);
    if (onClose) onClose(); // Call the function provided for closing logic (optional)
  };

  return (
    <div className="review-modal-overlay" style={{ display: isOpen ? 'block' : 'none' }}>
      <div className="review-modal-container">
        <button className="close-btn" onClick={handleClose}>X</button>
        <ReviewModalContent patient={patientData} /> {/* Pass patient data */}
      </div>
    </div>
  );
};

export default ReviewModal;