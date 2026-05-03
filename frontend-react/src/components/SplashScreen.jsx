import React from 'react';
import logo from '../assets/logo.png';

const SplashScreen = ({ isFadingOut }) => {
  return (
    <div className={`splash-screen ${isFadingOut ? 'fade-out' : ''}`}>
      <div className="splash-content">
        <div className="splash-logo-container">
          <img src={logo} alt="AShare Insight Lab Logo" className="splash-logo" />
          <div className="splash-glow"></div>
        </div>
        <div className="splash-text-group">
          <h1 className="splash-title">A股智研台</h1>
          <p className="splash-subtitle">AShare Insight Lab</p>
          <div className="splash-loading-container">
            <span className="splash-loading-text">Loading Market Intelligence...</span>
            <div className="splash-progress-bar">
              <div className="splash-progress-inner"></div>
            </div>
          </div>
        </div>
        <div className="splash-footer">
          <span className="brand-text">b‘lock10STUdio</span>
        </div>
      </div>
    </div>
  );
};

export default SplashScreen;
