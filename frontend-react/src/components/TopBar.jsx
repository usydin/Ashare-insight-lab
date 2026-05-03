import React from 'react';

const TopBar = ({ title, snapshotAt, runDate, healthStatus }) => {
  return (
    <header className="top-header">
      <div className="page-title-area">
        <h1>{title}</h1>
        <div style={{ fontSize: '10px', color: 'var(--mac-text-secondary)', marginTop: '4px' }}>
          当前读取: <code style={{ background: '#eee', padding: '2px 4px', borderRadius: '3px' }}>src/data/snapshot.json</code>
        </div>
      </div>
      <div className="status-capsules">
        <div className="capsule info">
          <span>🕒</span> 生成: {snapshotAt || '--'}
        </div>
        <div className="capsule">
          <span>📅</span> 运行日期: {runDate || '--'}
        </div>
        <div className="capsule">
          <span>🛡️</span> 数据健康: {healthStatus || '--'}
        </div>
      </div>
    </header>
  );
};

export default TopBar;
