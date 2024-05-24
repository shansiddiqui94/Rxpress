 import logo from './assets/Rxpress.png'; // Update path as needed
import './StickyNav.css';
import '../RedShift.jsx'
import Redshift from '../RedShift.jsx';
import '/Users/DanielSkies/Development/code/phase-5/Rxpress/client/Rxpress/src/index.css'
import { NavLink } from 'react-router-dom';
const StickyNav = () =>{


  return (
    <div className='navbar'>
      <a href="/" className="logo">
        <img src={logo} alt="Home" className="logo" /> 
      </a>
     
        <ul className="nav-links">
    <li><NavLink to="/">Home</NavLink></li> 
     <li><NavLink to="PatientUI">Patient Dashboard</NavLink></li> 
      <li><NavLink to="PharmUI">Pharmacist Dashboard</NavLink></li>
        <li><Redshift/></li>
      </ul>
        <div className='nav-login'>
          <button>Login</button>
          </div>
          <div className='nav-register'>
          <button>Register</button>  
          </div>
    </div>
  );
};

export default StickyNav;
