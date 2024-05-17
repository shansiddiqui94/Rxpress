import React, { useState, useRef, useEffect } from 'react'; 

function Redshift() {
  const [isRedshiftActive, setIsRedshiftActive] = useState(false);
  const buttonRef = useRef(null);

  const toggleRedshift = () => {
    setIsRedshiftActive(!isRedshiftActive);
  };

  useEffect(() => {
    if (buttonRef.current) {
      buttonRef.current.classList.toggle('redshift-active', isRedshiftActive);
    }
    document.body.classList.toggle('redshift-active', isRedshiftActive);
  }, [isRedshiftActive]);

    return (
        <label className="toggle-switch">
        <input type="checkbox" checked={isRedshiftActive} onChange={toggleRedshift} />
        <span className="slider round"></span> 
      </label>
      );
      
}

export default Redshift;
