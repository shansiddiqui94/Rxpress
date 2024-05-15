import './App.css'
import Footer from './components/Footer';
import StickyNav from './components/StickyNav'
import { useState } from 'react'
// import PharmacistDashboard from './components/PharamacistUI/PharmacistDashboard';
// import PatientCard from './components/PharamacistUI/PatientCard';
function App() {

  
  return (
    <>
      <div className='container'>
      <StickyNav/>
      <Footer/>
      </div>
    </>
  );
}

export default App;
