import React, { useState, useEffect } from 'react';
import './RotatingImages.css';
import image1 from '../assets/Happyolder.png';
import image2 from '../assets/Happypeeps.jpeg';
import image3 from '../assets/subway.jpeg';
import image4 from '../assets/redbeard.png';

const images = [image1, image2, image3, image4];

function RotatingImages() {
  const [currentIndex, setCurrentIndex] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentIndex((prevIndex) => (prevIndex + 1) % images.length);
    }, 15000); // Change image every 15 seconds
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="rotating-images">
      <img src={images[currentIndex]} alt="Happy customer" />
    </div>
  );
}

export default RotatingImages;
