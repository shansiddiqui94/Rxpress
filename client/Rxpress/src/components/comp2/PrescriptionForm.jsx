import React, { useState, useEffect } from 'react';
import axios from 'axios';

function PrescriptionForm() {
  const [selectedDrug, setSelectedDrug] = useState(null);
  const [allDrugs, setAllDrugs] = useState([]); // For drug selection
  const [patientId, setPatientId] = useState('');
  const [instructions, setInstructions] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false); 
  const [submitError, setSubmitError] = useState(null);

  // Fetch available drugs for the dropdown 
  useEffect(() => {
    const fetchDrugs = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5555/drugs');
        setAllDrugs(response.data);
      } catch (error) {
        console.error("Error fetching drugs:", error); 
      }
    };
    fetchDrugs(); 
  }, []);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setIsSubmitting(true);
    setSubmitError(null); 

    try {
      const response = await axios.post('http://127.0.0.1:5555/prescriptions', {
        drug_id: selectedDrug.id,
        patient_id: patientId,
        instructions: instructions, 
      });

      console.log('Prescription created:', response.data);
      // Handle success: Clear form, display success message, etc.      
    } catch (error) {
      setSubmitError(error.message || 'An error occurred');  
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="drug-select">Drug:</label>
        <select id="drug-select" value={selectedDrug?.id || ''} onChange={(e) => setSelectedDrug(allDrugs.find(d => d.id === parseInt(e.target.value)))}>
          <option value="">Select a drug</option>
          {allDrugs.map((drug) => (
            <option key={drug.id} value={drug.id}>
              {drug.name}
            </option>
          ))}
        </select>
      </div>

      {/* Similar input field for Patient ID (consider a dropdown if needed) */}

      <div>
        <label htmlFor="instructions">Instructions:</label>
        <textarea id="instructions" value={instructions} onChange={(e) => setInstructions(e.target.value)} />
      </div>

      <button type="submit" disabled={isSubmitting}>
        {isSubmitting ? 'Submitting...' : 'Create Prescription'}
      </button>

      {submitError && <div className="error-message">{submitError}</div>}
    </form>
  );
}

export default PrescriptionForm;
