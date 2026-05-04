import React, { useState } from 'react';

const RefreshDataPanel = ({ snapshotAt, latestRun }) => {
  const [copyStatus, setCopyStatus] = useState({ a: '复制', b: '复制' });

  const isExpired = () => {
    if (!snapshotAt || snapshotAt === '未知') return 'unknown';
    try {
      const generatedDate = new Date(snapshotAt);
      const now = new Date();
      const diffInHours = (now - generatedDate) / (1000 * 60 * 60);
      return diffInHours > 24 ? 'expired' : 'valid';
    } catch (e) {
      return 'unknown';
    }
  };

  const status = isExpired();

  const handleCopy = (text, key) => {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(() => {
        setCopyStatus({ ...copyStatus, [key]: '已复制' });
        setTimeout(() => setCopyStatus({ ...copyStatus, [key]: '复制' }), 2000);
      });
    } else {
      alert('您的浏览器不支持自动复制，请手动选择文字进行复制。');
    }
  };

  const refreshCommands = `source .venv/bin/activate
python3 app.py run-daily
python3 app.py ui-snapshot
python3 app.py validate-snapshot
python3 app.py sync-frontend-snapshot`;

  const packageCommands = `source ~/.zshrc
nvm use 22
source "$HOME/.cargo/env"
bash packaging/macos/build_macos.sh`;

  return (
    <div className="refresh-data-panel">
      <section className="state-card">
        <div className="state-card-header">
          <div className="state-card-title">当前快照状态</div>
          <div className={`status-pill ${status}`}>
            {status === 'valid' ? '快照处于当前可用状态' : 
             status === 'expired' ? '快照可能已过期' : '快照时间未知'}
          </div>
        </div>
        
        <div className="snapshot-details">
          <div className="meta-row">
            <span className="meta-label">生成时间:</span>
            <span className="meta-value">{snapshotAt || '待同步'}</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">最近运行:</span>
            <span className="meta-value">{latestRun?.run_date || '未运行'} ({latestRun?.status || 'Unknown'})</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">数据源路径:</span>
            <code className="meta-value code">frontend-react/src/data/snapshot.json</code>
          </div>
        </div>
      </section>

      <section className="soft-info">
        <p className="refresh-hint" style={{ color: 'inherit' }}>
          当前版本为离线桌面快照模式。刷新数据需在项目根目录运行后端命令，再重新同步前端快照。
        </p>
      </section>

      <section className="state-card">
        <div className="state-card-header">
          <div className="state-card-title" style={{ fontSize: '14px' }}>A. 刷新快照命令</div>
          <button className={`copy-inline-button ${copyStatus.a === '已复制' ? 'success' : ''}`} onClick={() => handleCopy(refreshCommands, 'a')}>
            {copyStatus.a === '已复制' ? '✅ 已复制' : '📋 复制命令'}
          </button>
        </div>
        <pre className="command-block">
          <code>{refreshCommands}</code>
        </pre>
      </section>

      <section className="state-card">
        <div className="state-card-header">
          <div className="state-card-title" style={{ fontSize: '14px' }}>B. 打包命令</div>
          <button className={`copy-inline-button ${copyStatus.b === '已复制' ? 'success' : ''}`} onClick={() => handleCopy(packageCommands, 'b')}>
            {copyStatus.b === '已复制' ? '✅ 已复制' : '📋 复制命令'}
          </button>
        </div>
        <pre className="command-block">
          <code>{packageCommands}</code>
        </pre>
      </section>
    </div>
  );
};

export default RefreshDataPanel;
