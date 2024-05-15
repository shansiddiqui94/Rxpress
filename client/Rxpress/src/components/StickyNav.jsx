 import logo from './assets/Rxpress.png'; // Update path as needed
import './StickyNav.css';

const StickyNav = () =>{


  return (
    <div className='navbar'>
      <a href="/" className="logo">
        <img src={logo} alt="Home" className="logo" /> 
      </a>

        <ul className="nav-links">
        <li><a href="#">Home</a></li>
        <li><a href="#">Patient Dashboard</a></li>
        <li><a href="#">Pharmacist Dashboard</a></li>
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
