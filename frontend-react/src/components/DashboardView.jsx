import React, { useState } from 'react';

const DashboardView = ({ data }) => {
  const [activeTab, setActiveTab] = useState('market_indices');
  const [copyStatus, setCopyStatus] = useState({});

  if (!data) return <div className="empty-state">正在初始化数据...</div>;

  const { dashboard_summary, signal_changes, paths, generated_at, review_queue } = data;
  const { signal_overview, latest_run } = dashboard_summary;

  const handleCopy = (text, key) => {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(() => {
        setCopyStatus({ ...copyStatus, [key]: true });
        setTimeout(() => setCopyStatus({ ...copyStatus, [key]: false }), 2000);
      });
    }
  };

  const copySummary = () => {
    const summary = `运行日期: ${latest_run?.run_date || '暂无数据'}
状态: ${latest_run?.status || '未知'}
生成时间: ${generated_at || '未知'}
报告路径: ${latest_run?.report_path || '暂无数据'}`;
    handleCopy(summary, 'summary');
  };

  const stats = [
    { 
      header: '📈 市场指数', 
      value: `${signal_overview?.index?.bullish || 0}/${latest_run?.index_count || 0}`, 
      desc: `看多: ${signal_overview?.index?.bullish || 0} | 看空: ${signal_overview?.index?.bearish || 0}`,
      delay: '0s'
    },
    { 
      header: '🧱 行业板块', 
      value: `${signal_overview?.sector?.bullish || 0}/${latest_run?.sector_count || 0}`, 
      desc: `看多: ${signal_overview?.sector?.bullish || 0} | 中性: ${signal_overview?.sector?.neutral || 0}`,
      delay: '0.05s'
    },
    { 
      header: '🎯 核心个股', 
      value: `${signal_overview?.stock?.bullish || 0}/${latest_run?.stock_count || 0}`, 
      desc: `看多: ${signal_overview?.stock?.bullish || 0} | 看空: ${signal_overview?.stock?.bearish || 0}`,
      delay: '0.1s'
    },
    { 
      header: '🚨 信号变更', 
      value: (signal_changes?.summary?.sector_change_count || 0) + (signal_changes?.summary?.index_change_count || 0), 
      desc: '今日新增变更',
      delay: '0.15s'
    },
  ];

  const systemStatusCards = [
    {
      title: '数据源健康',
      status: dashboard_summary?.data_health?.risk_item_count > 0 ? 'Risk' : 'Healthy',
      desc: `正常: ${dashboard_summary?.data_health?.ok_count || 0} | 异常: ${dashboard_summary?.data_health?.risk_item_count || 0}`,
      icon: '🛡️'
    },
    {
      title: '快照同步',
      status: generated_at ? 'Synced' : 'Unknown',
      desc: `同步: ${generated_at ? generated_at.split('T')[1] : '未知'}`,
      icon: '🔄'
    },
    {
      title: '报告产物',
      status: latest_run?.report_path ? 'Ready' : 'Missing',
      desc: latest_run?.report_path ? '日报已生成' : '未找到日报',
      icon: '📄'
    },
    {
      title: '本地路径',
      status: paths?.daily_signals_csv ? 'Linked' : 'Missing',
      desc: paths?.daily_signals_csv ? '数据链路正常' : '链路异常',
      icon: '📁'
    }
  ];

  const renderTable = () => {
    const items = signal_changes?.top_changes || [];
    
    return (
      <table className="data-table">
        <thead>
          <tr>
            <th>类型</th>
            <th>名称</th>
            <th>最新信号</th>
            <th>数据状态</th>
            <th>变更说明</th>
          </tr>
        </thead>
        <tbody>
          {items.length > 0 ? items.map((item, idx) => (
            <tr key={idx}>
              <td>{item.asset_type === 'sector' ? '行业' : '指数'}</td>
              <td>{item.name}</td>
              <td>
                <span className={`sig-badge sig-${item.latest_signal === 'trend_up' ? 'bullish' : (item.latest_signal === 'trend_down' ? 'bearish' : 'neutral')}`}>
                  {item.latest_signal}
                </span>
              </td>
              <td>{item.latest_data_status}</td>
              <td>{item.change_type}</td>
            </tr>
          )) : (
            <tr>
              <td colSpan="5" className="empty-state">暂无变更数据</td>
            </tr>
          )}
        </tbody>
      </table>
    );
  };

  return (
    <div id="dashboardView" className="view-container active">
      {/* 今日运行状态区域 (Clean Hero) */}
      <section className="dashboard-hero-clean animate-in">
        <div className="hero-main-stat">
          <div className="hero-stat-item">
            <span className="hero-label">运行日期</span>
            <span className="hero-value">{latest_run?.run_date || '未运行'}</span>
          </div>
          <div className="hero-stat-item">
            <span className="hero-label">运行状态</span>
            <span className={`status-pill ${latest_run?.status || 'unknown'}`}>{latest_run?.status || 'Unknown'}</span>
          </div>
          <div className="hero-stat-item">
            <span className="hero-label">快照生成</span>
            <span className="hero-value">{generated_at ? generated_at.replace('T', ' ') : '待同步'}</span>
          </div>
          <div className="hero-stat-item">
            <span className="hero-label">关注队列</span>
            <span className="hero-value">{review_queue?.count || 0} 项</span>
          </div>
        </div>
        <div className="hero-actions">
          <button 
            className={`copy-inline-button ${copyStatus.summary ? 'success' : ''}`}
            onClick={copySummary}
          >
            {copyStatus.summary ? '✅ 已复制摘要' : '📋 复制运行摘要'}
          </button>
        </div>
      </section>

      {/* 指标卡片网格 */}
      <section className="dashboard-grid">
        {stats.map((stat, idx) => (
          <div className="stat-card animate-in" key={idx} style={{ animationDelay: stat.delay }}>
            <div className="stat-header">{stat.header}</div>
            <div className="stat-value">{stat.value}</div>
            <div className="stat-desc">{stat.desc}</div>
          </div>
        ))}
      </section>

      {/* 系统状态迷你卡片 */}
      <section className="section-heading" style={{ marginTop: '32px' }}>
        系统集成状态
      </section>
      <section className="system-status-grid animate-in" style={{ animationDelay: '0.2s', marginTop: '0' }}>
        {systemStatusCards.map((card, idx) => (
          <div className="status-mini-card" key={idx}>
            <div className="status-card-icon">{card.icon}</div>
            <div className="status-card-content">
              <div className="status-card-title">{card.title}</div>
              <div className="status-card-meta">
                <span className={`status-pill ${card.status.toLowerCase()}`}>{card.status}</span>
                <span className="status-card-desc">{card.desc}</span>
              </div>
            </div>
          </div>
        ))}
      </section>

      <section className="tabs-section animate-in" style={{ animationDelay: '0.3s' }}>
        <div className="tabs-header">
          <div 
            className={`tab-item ${activeTab === 'market_indices' ? 'active' : ''}`} 
            onClick={() => setActiveTab('market_indices')}
          >
            市场指数
          </div>
          <div 
            className={`tab-item ${activeTab === 'sector_boards' ? 'active' : ''}`} 
            onClick={() => setActiveTab('sector_boards')}
          >
            行业板块
          </div>
          <div 
            className={`tab-item ${activeTab === 'watchlist' ? 'active' : ''}`} 
            onClick={() => setActiveTab('watchlist')}
          >
            监控自选
          </div>
        </div>
        <div className="tab-content">
          {renderTable()}
        </div>
      </section>

      <section className="panel-section animate-in" style={{ marginTop: '40px', animationDelay: '0.4s' }}>
        <div className="section-heading">
          <span>🔗 快照路径索引</span>
          <div style={{ display: 'flex', gap: '8px' }}>
             <button 
                className={`copy-inline-button ${copyStatus.report_path ? 'success' : ''}`}
                onClick={() => handleCopy(latest_run?.report_path, 'report_path')}
              >
                {copyStatus.report_path ? '✅ 已复制日报路径' : '📋 复制日报路径'}
              </button>
              <button 
                className={`copy-inline-button ${copyStatus.snapshot_path ? 'success' : ''}`}
                onClick={() => handleCopy('frontend-react/src/data/snapshot.json', 'snapshot_path')}
              >
                {copyStatus.snapshot_path ? '✅ 已复制快照路径' : '📋 复制快照路径'}
              </button>
          </div>
        </div>
        <div className="health-list" style={{ fontFamily: 'monospace', fontSize: '11px' }}>
          {paths && Object.entries(paths).length > 0 ? Object.entries(paths).map(([key, value]) => (
            <div className="health-row" key={key}>
              <span className="health-label">{key}</span>
              <span className="health-value">{value || '待生成'}</span>
            </div>
          )) : (
            <div className="empty-state" style={{ padding: '20px' }}>
              <span className="empty-state-icon">📁</span>
              暂无可用路径索引
            </div>
          )}
        </div>
      </section>

      <section className="panel-section animate-in" style={{ marginTop: '32px', animationDelay: '0.5s' }}>
        <div className="section-heading">💬 系统运行提示</div>
        <div className="msg-list" style={{ background: 'white', border: '1px solid var(--mac-border)', color: 'var(--mac-text-secondary)' }}>
          {data.messages && data.messages.length > 0 ? data.messages.map((msg, idx) => (
            <div className="msg-item" key={idx}>
              <span>•</span> {msg}
            </div>
          )) : (
            <div className="msg-item">
              <span>ℹ️</span> 系统当前运行状态良好，未发现需要人工干预的异常。
            </div>
          )}
        </div>
      </section>

      {/* 品牌横幅 (Brand Footer) */}
      <section className="brand-footer-card animate-in" style={{ animationDelay: '0.6s' }}>
        <img 
          src="/brand/banner2.png" 
          alt="Brand Banner" 
          className="brand-banner-footer"
          onError={(e) => { e.target.style.display = 'none'; }}
        />
        <div className="brand-footer-info">
          <span className="brand-footer-title">A股智研台 / AShare Insight Lab</span>
          <span>•</span>
          <span>AI 驱动的本地 A股智能投研终端</span>
        </div>
      </section>
    </div>
  );
};

export default DashboardView;
