import React from 'react';
import './Footer.css'; // Import your CSS file

function Footer() {
  return (
    <footer className="footer">
      <p>
        &copy; {new Date().getFullYear()} Rxpress. All rights reserved.
      </p>
      <div className="social-icons">
        {/* Add social media links here (optional) */}
        <a href="https://twitter.com/yourcompany" target="_blank" rel="noopener noreferrer">
          <i className="fab fa-twitter"></i>
        </a>
        {/* ... other social icons ... */}
      </div>
    </footer>
  );
}

export default Footer;
