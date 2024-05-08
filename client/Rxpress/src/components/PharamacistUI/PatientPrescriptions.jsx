import React from 'react';

const PatientPrescriptions = ({ patientId, prescriptions }) => {
  // ... Logic to fetch prescriptions if not provided as props (optional)

  return (
    <div className="patient-prescriptions">
      <h2>Prescriptions for Patient ID: {patientId}</h2>
      {prescriptions && prescriptions.length > 0 ? (
        <ul>
          {prescriptions.map((prescription) => (
            <li key={prescription.id}>
              {/* Render prescription details */}
              Medication: {prescriptions.drug}
              Dosage: {prescriptions.instructions}
              
            </li>
          ))}
        </ul>
      ) : (
        <p>No prescriptions found for this patient.</p>
      )}
    </div>
  );
};

export default PatientPrescriptions;
