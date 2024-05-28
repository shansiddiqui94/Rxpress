// import React from 'react';
// import logo from './assets/RxpressLogo.png'; // Update path as needed
// import './StickyNav.css';
// import Redshift from '../RedShift.jsx';
// import { NavLink } from 'react-router-dom';

// const StickyNav = () => {
//   return (
//     <header className="navbar">
//       <div className="navbar-container">
//         <a href="/" className="navbar-logo">
//           <img src={logo} alt="Home" className="logo" />
//         </a>
//         <nav className="navbar-menu">
//           <ul className="navbar-links">
//             <li><NavLink to="/">Home</NavLink></li>
//             <li><NavLink to="/PatientUI">Patient Dashboard</NavLink></li>
//             <li><NavLink to="/PharmUI">Pharmacist Dashboard</NavLink></li>
//             <li><Redshift /></li>
//           </ul>
//           <div className="navbar-actions">
//             <button className="navbar-button">Login</button>
//             <button className="navbar-button">Register</button>
//           </div>
//         </nav>
//       </div>
//     </header>
//   );
// };

// export default StickyNav;

//v2
import React from 'react';
import logo from './assets/RxpressLogo.png';
import './StickyNav.css';
import { NavLink } from 'react-router-dom';
import Redshift from '../RedShift.jsx';
const StickyNav = () => {
  return (
    <header className="navbar">
      <div className="navbar-container">
        <a href="/" className="navbar-logo">
          <img src={logo} alt="Home" className="logo" />
        </a>
        <nav className="navbar-menu">
          <ul className="navbar-links">
          <li><NavLink to="/">Home</NavLink></li>
          <li><NavLink to="/PatientUI">Patient Dashboard</NavLink></li>
          <li><NavLink to="/PharmUI">Pharmacist Dashboard</NavLink></li>
          <li><Redshift /></li>
          </ul>
        </nav>
        <div className="navbar-actions">
          <button className="navbar-button login">Login</button>
          <button className="navbar-button register">Register</button>
        </div>
      </div>
    </header>
  );
};

export default StickyNav;
