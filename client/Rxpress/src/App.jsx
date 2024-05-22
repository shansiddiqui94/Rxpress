import './App.css'
import Footer from './components/Footer';
import StickyNav from './components/StickyNav'
import PharmacistDash from './components/PharamacistUI/PharmacistDash';
import PatientDashboard from './components/PatientUI/PatientDashboard';

function App() {

  
  return (
    <>
      <div className='container'>
      <StickyNav/>
      {/* <PharmacistDash/> */}
      <PatientDashboard/>
      <Footer/>
      </div>
    </>
  );
}

export default App;
