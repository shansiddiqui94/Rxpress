import {useState, useEffect} from 'react';
import logo from '/Users/DanielSkies/Development/code/phase-5/Rxpress/client/Rxpress/src/components/assets/Rxpress.png';
import './StickyNav.css';

const StickyNav = () => {
 
  const [navBarColor, setNavBarColor] = useState('transparent'); // Initial color is transparent

  const handleScroll = () => {
    if (window.scrollY > 50) {
      setNavBarColor('navy'); // Change to navy blue when scrolled more than 50px
    } else {
      setNavBarColor('transparent'); // Revert to transparent when scrolled back
    }
  };

  useEffect(() => {
    window.addEventListener('scroll', handleScroll); // Add scroll event listener
    return () => {
      window.removeEventListener('scroll', handleScroll); // Clean up listener on unmount
    };
  }, []); // Run only on component mount and unmount

  return (
    <nav className="navbar" style={{ backgroundColor: navBarColor }}>
      <a href="/" className="home-link">
        <img src={logo} alt="Home" className="logo" />
      </a>
      <ul className="nav-links">
        <li><a href="#about">About</a></li>
        <li><a href="#services">Services</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </nav>
  ); 
      
}

export default StickyNav;
