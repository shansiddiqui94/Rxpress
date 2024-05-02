import  { useState, useEffect } from "react";

function PatientDash() {
  const [patients, setPatients] = useState([]); // Initialize as an empty array
  const [loading, setLoading] = useState(true); // Track loading status

  useEffect(() => {
    fetchPatient(); 
  }, []); 

  const fetchPatient = () => {
    fetch("http://127.0.0.1:5555/patients") 
      .then((res) => res.json())
      .then((data) => {
        setPatients(data); // Set the fetched data
        setLoading(false); // Indicate loading is complete
      })
      .catch((err) => console.error("Error fetching patients:", err)); // Error handling
  };

  return (
    <div>
      {loading ? (
        <p>Loading patients...</p> // Display loading message while fetching
      ) : (
        patients.map((patient) => ( // Map over the patients array to display data
          <div key={patient.id}>
            <h3>{patient.name}</h3>
            <p>Address: {patient.address}</p>
            <p>Insurance: {patient.insurance}</p>
          </div>
        ))
      )}
    </div>
  );
}

export default PatientDash;
