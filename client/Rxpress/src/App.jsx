import './App.css'
import Footer from './components/Footer';
import StickyNav from './components/StickyNav'
import { useState } from 'react'
import PharmacistDash from './components/PharamacistUI/PharmacistDash';
// import PatientCard from './components/PharamacistUI/PatientCard';
function App() {

  
  return (
    <>
      <div className='container'>
      <StickyNav/>
      <PharmacistDash/>
      <Footer/>
      </div>
    </>
  );
}

export default App;
