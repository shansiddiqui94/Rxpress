import React from 'react';
import './ModalContent.css'; // Renamed CSS file

const ModalContent = ({ isOpen, onClose, title, leftContent, rightContent, prescriptionData }) => {
  if (!isOpen) return null;

  return (
    <div className="modal-backdrop" onClick={onClose}>
      <div className="modal-split" onClick={(e) => e.stopPropagation()}>
      <div className="modal-content-left">
          <h3 className="text-xl font-bold mb-4">{title}</h3>
          {prescriptionData ? ( 
            <div>
              <p>Prescription:</p>
              <ul>
                <li>Medication: {prescriptionData.medication}</li>
                <li>Dosage: {prescriptionData.dosage}</li>
              </ul>
            </div>
          ) : (
            <p>Loading prescription...</p>
          )}
        </div>
          <h3 className="text-xl font-bold mb-4">{title}</h3>
          {leftContent}         
        </div>

        <div className="divider" /> 

        <div className="modal-content-right">
          {rightContent} 
          <button className="modal-close-btn" onClick={onClose}>
            Close
          </button>
        </div>
      </div>
  );
};

export default ModalContent;
