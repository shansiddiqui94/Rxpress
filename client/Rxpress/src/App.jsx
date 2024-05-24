import './App.css'
import Footer from './components/Footer';
import StickyNav from './components/StickyNav'
import { Outlet } from 'react-router-dom';

function App() {

  
  return (
    <>
   
      <div className='container'> 
      <StickyNav/>
      <Outlet/>
      <Footer/>
      </div>
    </>
  );
}

export default App;
