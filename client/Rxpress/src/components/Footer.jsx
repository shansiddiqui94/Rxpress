import React from 'react';
import './Footer.css'; // Import your CSS file
import '@fortawesome/fontawesome-free/css/all.min.css'; // Import Font Awesome CSS

function Footer() {
  return (
    <footer className="footer">
      <p>
        Privacy Notice | Site Terms | Cookie Settings | Do Not Share My Personal Information
      </p>
      <p>
        &copy; {new Date().getFullYear()} Rxpress. All rights reserved.
      </p>
      
    </footer>
  );
}

export default Footer;
