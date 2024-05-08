// fetchFunctions.js
function fetchPatientPrescriptions(patientId) {
    const baseURL = 'http://127.0.0.1:5555'; 
    const url = `${baseURL}/patients/${patientId}/prescriptions`;
  
    fetch(url)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Failed to fetch prescriptions (status: ${response.status})`);
        }
        return response.json(); // Parse the response as JSON
      })
      .then((data) => {
        // Handle the fetched data here
        console.log("Fetched prescriptions:", data); 
        return data; // You can optionally return data 
      })
      .catch((error) => {
        console.error("Error fetching prescriptions:", error);
        // Handle the error here, e.g., display an error message to the user
      });
  }
  
  export default fetchPatientPrescriptions;
  