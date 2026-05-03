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

  return (
    <header className="top-header">
      <div className="page-title-area">
        <h1>{title}</h1>
        <div style={{ fontSize: '10px', color: 'var(--mac-text-secondary)', marginTop: '4px' }}>
          数据源: <code style={{ background: '#eee', padding: '2px 4px', borderRadius: '3px' }}>frontend-react/src/data/snapshot.json</code>
          {expired && (
            <span style={{ marginLeft: '12px', color: '#d93025', fontWeight: 'bold' }}>
              ⚠️ 快照可能已过期，请执行 run-daily 并同步
            </span>
          )}
        </div>
      </div>
      <div className="status-capsules">
        <div className="capsule info">
          <span>🕒</span> {snapshotAt ? `生成: ${snapshotAt}` : '快照时间未知'}
        </div>
        <div className="capsule">
          <span>📅</span> 运行: {runDate || '--'} ({getStatusLabel()})
        </div>
        <div className="capsule">
          <span>🛡️</span> 健康: {healthStatus || '--'}
        </div>
      </div>
    </header>
  );
};

export default TopBar;
