import React, { useState, useEffect } from 'react';
import DrugSearch from './SearchAndAddDrug';
import PrescriptionBasket from './PrescriptionBasket';
import RotatingImages from './RotatingImages';

function PatientDashboard() {
  const [selectedPatientId, setSelectedPatientId] = useState(null);
  const [patients, setPatients] = useState([]);
  const [prescriptions, setPrescriptions] = useState([]);
  const [error, setError] = useState(null);

  // Fetch list of patients on component mount
  useEffect(() => {
    fetchPatients();
  }, []);

  // Fetch prescriptions whenever selectedPatientId changes
  useEffect(() => {
    if (selectedPatientId !== null) {
      fetchPatientPrescriptions(selectedPatientId);
    }
  }, [selectedPatientId]);

  // Function to fetch list of patients
  const fetchPatients = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5555/patients');
      if (!response.ok) {
        throw new Error('Error fetching patients');
      }
      const data = await response.json();
      setPatients(data);
      // Optionally, set the first patient as selected by default
      if (data.length > 0) {
        setSelectedPatientId(data[0].id);
      }
    } catch (error) {
      console.error('Error fetching patients:', error);
      setError(error.message);
    }
  };

  // Function to fetch patient's prescriptions
  const fetchPatientPrescriptions = async (patientId) => {
    try {
      const response = await fetch(`http://127.0.0.1:5555/prescriptions?patientId=${patientId}`);
      if (!response.ok) {
        throw new Error('Error fetching prescriptions');
      }
      const data = await response.json();
      setPrescriptions(data);
    } catch (error) {
      console.error('Error fetching prescriptions:', error);
      setError(error.message);
    }
  };

  // Function to handle drug selection from DrugSearch component
  const handleDrugSelection = (drugId) => {
    setSelectedDrugId(drugId);
  };

  // Function to handle adding a prescription
  const handlePrescriptionAdded = (newPrescription) => {
    setPrescriptions((prevPrescriptions) => [...prevPrescriptions, newPrescription]);
  };

  // Function to handle submitting basket contents (simulates submitting for a new prescription)
  const handleSubmitBasket = async () => {
    if (prescriptions.length === 0) {
      console.warn('Basket is empty. No prescriptions to submit.');
      return;
    }

    try {
      // Replace with your actual logic to submit prescriptions to the backend
      // This might involve sending the prescriptions array to a different endpoint or performing additional actions,
      // potentially interacting with a healthcare record system or following specific workflows
      console.log('Submitting basket:', prescriptions);

      // Assuming successful submission, clear the basket
      setPrescriptions([]);
    } catch (error) {
      console.error('Error submitting prescriptions:', error);
      setError(error.message);
    }
  };

  return (
    <div className="dashboard-container">
      <h2>Patient Dashboard</h2>
      <div className="top-section">
        <label htmlFor="patient-select">Select Patient:</label>
        <select
          id="patient-select"
          value={selectedPatientId}
          onChange={(e) => setSelectedPatientId(e.target.value)}
        >
          {patients.map((patient) => (
            <option key={patient.id} value={patient.id}>
              {patient.name}
            </option>
          ))}
        </select>
      </div>
      <div className="left-section">
        <RotatingImages />
      </div>
      <div className="center-section">
        <DrugSearch
          onDrugSelect={handleDrugSelection}
          patientId={selectedPatientId}
          onPrescriptionAdded={handlePrescriptionAdded}
        />
      </div>
      <div className="right-section">
        <PrescriptionBasket prescriptions={prescriptions} />
        {error && <p className="error-message">Error: {error}</p>}
        <button onClick={handleSubmitBasket} disabled={prescriptions.length === 0}>
          Submit Basket
        </button>
      </div>
    </div>
  );
}

export default PatientDashboard;
