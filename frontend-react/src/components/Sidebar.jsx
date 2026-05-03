import React from 'react';
import logo from '../assets/logo.png';

const Sidebar = ({ activeView, onViewChange, version }) => {
  const navGroups = [
    {
      label: '主要功能',
      items: [
        { id: 'dashboard', label: '总览面板', icon: '⊞' },
        { id: 'market_indices', label: '市场指数', icon: '↗' },
        { id: 'sector_boards', label: '行业板块', icon: '❖' },
        { id: 'watchlist', label: '监控自选', icon: '⊙' },
        { id: 'search', label: '全量搜索', icon: '⌕' },
        { id: 'history', label: '运行历史', icon: '◷' },
      ]
    },
    {
      label: '投研分析',
      items: [
        { id: 'reports', label: '日报中心', icon: '▤' },
        { id: 'ai', label: 'AI 投研室', icon: '◈' },
        { id: 'scenario', label: '情景推演', icon: '♺' },
      ]
    }
  ];

  return (
    <aside className="sidebar">
      <div className="brand-section">
        <img src={logo} alt="Logo" className="brand-logo" />
        <div className="brand-text-group">
          <div className="brand-title">A股智研台</div>
          <div className="brand-subtitle">AShare Insight Lab</div>
        </div>
      </div>

      {navGroups.map((group) => (
        <div className="nav-group" key={group.label}>
          <div className="nav-label">{group.label}</div>
          {group.items.map((item) => (
            <div
              key={item.id}
              className={`nav-item ${activeView === item.id ? 'active' : ''}`}
              onClick={() => onViewChange(item.id)}
            >
              <span className="nav-icon">{item.icon}</span>
              <span className="nav-text">{item.label}</span>
            </div>
          ))}
        </div>
      ))}

      <div style={{ flex: 1 }}></div>

      <div className="nav-group" style={{ marginBottom: 0 }}>
        <div
          className={`nav-item ${activeView === 'settings' ? 'active' : ''}`}
          onClick={() => onViewChange('settings')}
        >
          <span className="nav-icon">⚙</span>
          <span className="nav-text">偏好设置</span>
        </div>
        <div id="appVersion" style={{ fontSize: '10px', color: 'var(--mac-text-secondary)', padding: '8px 12px' }}>
          v{version || '0.4.3'} · Ready
        </div>
      </div>
    </aside>
  );
};

export default Sidebar;
