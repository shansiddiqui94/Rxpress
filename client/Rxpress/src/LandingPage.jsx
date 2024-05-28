import React from 'react';
import './LandingPage.css';
import heroImage from './components/assets/pharmlanding.jpeg';
import featureImage1 from './components/assets/LeftRxpressmachine.jpeg';
import featureImage2 from './components/assets/pharamcistHappy.jpeg';
import featureImage3 from './components/assets/elderlyhappy.jpeg';

const LandingPage = () => {
  return (
    <div className="landing-page">
      <section className="hero" style={{ backgroundImage: `url(${heroImage})` }}>
        <div className="hero-content">
          <h1>Welcome to Rxpress</h1>
          <p>For quick and easy refills</p>
          <button className="cta-button">Learn More</button>
        </div>
        <div className="hero-slogan">
          <h2>Rxpress - Easy, Quick Pickup</h2>
        </div>
      </section>
      
      <section className="features">
        <div className="feature">
          <img src={featureImage1} alt="Feature One" />
          <h2>Prescription Management</h2>
          <p>Experience the convenience of quickly picking up your prescriptions at one of our many locations, including traditional pharmacies, drugstores, and other public centers. Rxpress ensures that you get your medications efficiently, without the wait.</p>
        </div>
        <div className="feature">
          <img src={featureImage2} alt="Feature Two" />
          <h2>Real-Time Status Updates</h2>
          <p>  All prescriptions are filled by certified pharmacists who are available on demand for when a customer requests it or needs more assistance. At Rxpress, we put the customer's time and care first.</p>
        </div>
        <div className="feature">
          <img src={featureImage3} alt="Feature Three" />
          <h2>Efficient Pharmacist Dashboard</h2>
          <p>Efficiently review and process incoming prescription requests.</p>
        </div>
      </section>

      {/* Need to edit CSS or make seperate About page */}
      {/* <section className="about">
        <h2>About Rxpress</h2>
        <p>
          Rxpress is an intuitive pharmacy management application aimed at simplifying the prescription process for both patients and pharmacists. Our platform provides a seamless experience for managing prescriptions, allowing patients to conveniently order and track their medications, while enabling pharmacists to efficiently review and process prescription requests.
        </p>
        <p>
          At Rxpress, we believe in making pharmacy services faster and simpler. With our innovative Rxpress Vending Machines located at your local pharmacy, you can quickly pick up your prescriptions at your convenience. Our mission is to enhance your pharmacy experience, ensuring that you receive your medications without the hassle.
        </p>
        <h3>Key Features</h3>
        <h4>For Patients:</h4>
        <ul>
          <li><strong>Prescription Management:</strong> Easily add prescriptions to a digital basket for approval.</li>
          <li><strong>Real-Time Status Updates:</strong> Receive instant updates on prescription status changes.</li>
          <li><strong>Basket Functionality:</strong> Manage prescriptions in the digital basket, including adding, removing, or updating quantities.</li>
        </ul>
        <h4>For Pharmacists:</h4>
        <ul>
          <li><strong>Pharmacist Dashboard:</strong> Efficiently review and process incoming prescription requests.</li>
          <li><strong>Prescription Review:</strong> Quickly review patient prescriptions and update their status.</li>
          <li><strong>Red-Shift Toggle:</strong> Adjust screen colors to reduce eye strain during extended work sessions.</li>
        </ul>
        <p>
          Join us at Rxpress and experience the future of pharmacy services. With our customer-focused approach, we ensure that your pharmacy needs are met with efficiency and convenience.
        </p>
      </section> */}

    </div>
  );
};

export default LandingPage;
