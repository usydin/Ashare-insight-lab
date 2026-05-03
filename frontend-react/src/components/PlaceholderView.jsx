import React from 'react';

const PlaceholderView = ({ id, title, icon, description, disclaimer, disclaimerColor = '#856404', disclaimerBg = '#fffbe6', disclaimerBorder = '#ffe58f' }) => {
  return (
    <div className="view-container active">
      <div className="empty-state">
        <div style={{ fontSize: '48px', marginBottom: '20px' }}>{icon}</div>
        <h2>{title}</h2>
        <p>{description}</p>
        {disclaimer && (
          <div style={{ 
            marginTop: '24px', 
            padding: '16px', 
            background: disclaimerBg, 
            border: `1px solid ${disclaimerBorder}`, 
            borderRadius: 'var(--mac-radius-md)', 
            maxWidth: '500px', 
            display: 'inline-block', 
            textAlign: 'left' 
          }}>
            <p style={{ margin: 0, color: disclaimerColor, fontSize: '13px' }}>
              <strong>说明：</strong>{disclaimer}
            </p>
          </div>
        )}
      </div>
    </div>
  );
};

export default PlaceholderView;
