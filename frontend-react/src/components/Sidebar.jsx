import React from 'react';

const Sidebar = ({ activeView, onViewChange, version }) => {
  const navGroups = [
    {
      label: '总览 (Overview)',
      items: [
        { id: 'dashboard', icon: '📊', label: '总览面板', meta: '核心指标与状态' },
      ]
    },
    {
      label: '数据与报告 (Data)',
      items: [
        { id: 'reports', icon: '📄', label: '报告中心', meta: '日报与产物矩阵' },
        { id: 'history', icon: '🕒', label: '运行历史', meta: '快照时间线' },
      ]
    },
    {
      label: '研究与检索 (Research)',
      items: [
        { id: 'search', icon: '🔍', label: '全量搜索', meta: '资产与路径检索' },
        { id: 'market_indices', icon: '📈', label: '市场指数', meta: '核心宽基指数' },
        { id: 'sector_boards', icon: '🧱', label: '行业板块', meta: '行业强弱监控' },
        { id: 'watchlist', icon: '🎯', label: '监控自选', meta: '核心关注个股' },
      ]
    },
    {
      label: '系统 (System)',
      items: [
        { id: 'settings', icon: '⚙️', label: '偏好设置', meta: '环境与同步控制' },
      ]
    }
  ];

  return (
    <aside className="sidebar">
      <div className="brand-section sidebar-brand">
        <img 
          src="/brand/logo.png" 
          alt="AShare Lab" 
          className="brand-logo" 
          onError={(e) => { e.target.src = 'src/assets/logo.png'; e.target.onerror = null; }}
        />
        <div className="brand-text-group">
          <div className="brand-title">A股智研台</div>
          <div className="brand-subtitle">AShare Insight Lab</div>
        </div>
      </div>

      <div className="sidebar-scroll-area">
        {navGroups.map((group, gIdx) => (
          <div className="sidebar-section" key={gIdx}>
            <div className="nav-label">{group.label}</div>
            <div className="nav-group">
              {group.items.map((item) => (
                <button
                  key={item.id}
                  className={`nav-item ${activeView === item.id ? 'active' : ''}`}
                  onClick={() => onViewChange(item.id)}
                >
                  <span className="nav-icon">{item.icon}</span>
                  <div style={{ display: 'flex', flexDirection: 'column' }}>
                    <span className="nav-label-text">{item.label}</span>
                    <span className="sidebar-item-meta">{item.meta}</span>
                  </div>
                </button>
              ))}
            </div>
          </div>
        ))}
      </div>
    </aside>
  );
};

export default Sidebar;
