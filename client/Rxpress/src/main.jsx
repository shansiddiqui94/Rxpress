import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css' 
import {createBrowserRouter, RouterProvider} from "react-router-dom" // step 1
import LandingPage from './LandingPage.jsx'
import PharmacistDash from './components/PharamacistUI/PharmacistDash.jsx'
import PatientDashboard from './components/PatientUI/PatientDashboard.jsx'

// Created association here 
// SharedLayout(root) to add nav and footer to every route

const router = createBrowserRouter([{
path: "/", element: <App/>, //App now holds outlet which is a template of shared information that will exist in each component 
children: [{path:"/", element: <LandingPage/>}, {path:"/PatientUI", element: <PatientDashboard/>}, {path:"/PharmUI", element:<PharmacistDash/>}] // children determine the possibility of a route this can be Patient Dashboard, that we are now calling the componenet directly
// route config prop called router 

}])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router}/>
  </React.StrictMode>,
)


// Step 1 install react router, and setup the CreateBrowerRouter function 
//Step 2 Created an Array of object is its own route(path) and component(element) pairing. 
//step3: If multiple routes have some shared layout then make those routes be children of a route, outlet is whatever component you want 
// Shared Layout is a template of whatever you want to reuse in other components(nav, footer) + the outlet, which would be replaced with children(home, ptDash, pharmDash)
// Navlinks is react routers version of an A tag. 

// Outlet: a component defined by react router that gets replaced, by componenets as such as PatientUI, and PharamUI. Ex: we removed the components out of App.jsx and replaced it with Outlet

// RouterProvider: Create a const router, pass as a prop to RouterProvider is a custom component whose job it is to render a router configuartion which is pretty much CreateBrowserRouter