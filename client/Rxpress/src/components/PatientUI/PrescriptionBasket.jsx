// src/components/PatientUI/PrescriptionBasket.jsx 
import React, { useState, useEffect } from 'react';
import './PrescriptionBasket.css'; 

const PrescriptionBasket = () => {
    const [pendingPrescriptions, setPendingPrescriptions] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);

    // Function to fetch pending prescriptions
    const fetchPendingPrescriptions = async () => { 
        setIsLoading(true);
        setError(null);

        try {
            const response = await fetch('/api/prescriptions/pending'); 
            if (!response.ok) {
                throw new Error('Could not fetch pending prescriptions');
            }
            const data = await response.json();
            setPendingPrescriptions(data);
        } catch (error) {
            setError(error.message); 
        } finally {
            setIsLoading(false);
        }
    };

    useEffect(() => {
        fetchPendingPrescriptions();
    }, []); 

    return (
        <div className="prescription-basket-container">
            <h2>Prescriptions Awaiting Pharmacist Approval</h2> 

            {isLoading && <p>Loading...</p>}
            {error && <p>Error: {error}</p>}

            {pendingPrescriptions.length > 0 ? (
                <ul className="pending-prescriptions-list"> 
                    {pendingPrescriptions.map((prescription) => (
                        <li key={prescription.id}>
                             {/* Display prescription details */}
                        </li>
                    ))}
                </ul>
            ) : (
                <p>No prescriptions pending.</p>
            )}
        </div>
    );
};

export default PrescriptionBasket;
