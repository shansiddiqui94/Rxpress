import React, { useState, useEffect } from 'react';
import axios from 'axios';

function PatientDetails() {
  const [patient, setPatient] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchPatientDetails = async () => {
      setIsLoading(true);
      setError(null);

      try {
        const response = await axios.get(`http://127.0.0.1:5555/patients/${props.patientId}`);
        setPatient(response.data);
      } catch (error) {
        setError('Error fetching patient details. Please try again.'); 
      } finally {
        setIsLoading(false);
      }
    };

    fetchPatientDetails();
  }, [props.patientId]);

  if (isLoading) {
    return <p>Loading patient details...</p>;
  }

  if (error) {
    return <p className="error-message">{error}</p>;
  }

  if (!patient) {
    return <p>Patient not found.</p>;
  }

  return (
    <div>
      <h2>Patient Details</h2>
      <p><strong>Name:</strong> {patient.name}</p>
      <p><strong>Address:</strong> {patient.address}</p>
      <p><strong>Insurance:</strong> {patient.insurance}</p>

      <h3>Prescriptions</h3>
      {patient.prescriptions.length > 0 ? (
        <ul>
          {patient.prescriptions.map((prescription) => (
            <li key={prescription.id}>
              Drug: {prescription.drug.name} (Status: {prescription.status})
            </li>
          ))}
        </ul>
      ) : (
        <p>No prescriptions found for this patient.</p>
      )}
    </div>
  );
}

export default PatientDetails;
