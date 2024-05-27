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
          <p>Your convenient pharmacy solution with vending machine pickup.</p>
          <button className="cta-button">Book an Appointment</button>
        </div>
        <div className="hero-slogan">
          <h2>Rxpress - Easy, Quick Pickup</h2>
        </div>
      </section>
      
      <section className="features">
        <div className="feature">
          <img src={featureImage1} alt="Feature One" />
          <h2>Newest Technologies</h2>
          <p>Experience the latest in pharmaceutical technology with our advanced vending machines.</p>
        </div>
        <div className="feature">
          <img src={featureImage2} alt="Feature Two" />
          <h2>Experienced Pharmacists</h2>
          <p>Our pharmacists are highly qualified and ready to assist you with your needs.</p>
        </div>
        <div className="feature">
          <img src={featureImage3} alt="Feature Three" />
          <h2>High Customer Satisfaction</h2>
          <p>We pride ourselves on excellent customer service and satisfaction.</p>
        </div>
      </section>

      <section className="additional-info">
        <h2>Why Choose Rxpress?</h2>
        <p>At Rxpress, we provide the best pharmacy services with the convenience of vending machine pickup. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam.</p>
      </section>
    </div>
  );
};

export default LandingPage;
