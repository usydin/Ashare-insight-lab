import React from 'react';

const TopBar = ({ title, snapshotAt, runDate, healthStatus, status }) => {
  const isExpired = () => {
    if (!snapshotAt || snapshotAt === '未知') return true;
    try {
      const generatedDate = new Date(snapshotAt);
      const now = new Date();
      const diffInHours = (now - generatedDate) / (1000 * 60 * 60);
      return diffInHours > 24;
    } catch (e) {
      return true;
    }
  };

  const getStatusLabel = () => {
    if (status === 'success') return 'Success';
    if (status === 'running') return 'Running';
    if (status === 'failed') return 'Failed';
    return status || '--';
  };

  const expired = isExpired();

  const getRefreshHint = () => {
    if (!snapshotAt || snapshotAt === '未知') return '需同步快照';
    return expired ? '建议刷新快照' : '快照可用';
  };

  const getHealthClass = () => {
    return healthStatus === 'Risk' ? 'danger' : 'success';
  };

  return (
    <header className="top-header">
      <div className="page-title-area">
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <img src="/brand/logo_128.png" alt="" className="brand-mark" />
          <h1>{title}</h1>
        </div>
        <div style={{ fontSize: '10px', color: 'var(--mac-text-secondary)', marginTop: '4px' }}>
          数据源: <code style={{ background: 'rgba(0,0,0,0.05)', padding: '2px 4px', borderRadius: '3px' }}>frontend-react/src/data/snapshot.json</code>
          <span style={{ 
            marginLeft: '12px', 
            color: expired ? '#d93025' : 'var(--mac-success)', 
            fontWeight: 'bold' 
          }}>
            • {getRefreshHint()}
          </span>
          {expired && snapshotAt !== '未知' && (
            <span style={{ marginLeft: '12px', color: '#d93025' }}>
              (生成已超过 24h)
            </span>
          )}
        </div>
      </div>
      <div className="status-capsules">
        <div className="capsule info">
          <span>🕒</span> {snapshotAt ? `生成: ${snapshotAt.replace('T', ' ')}` : '待同步'}
        </div>
        <div className="capsule">
          <span>📅</span> 运行: {runDate || '未运行'} ({getStatusLabel()})
        </div>
        <div className={`capsule ${getHealthClass()}`}>
          <span>🛡️</span> 健康: {healthStatus || '待检'}
        </div>
      </div>
    </header>
  );
};

export default TopBar;
