import React, { useState } from 'react';

const DashboardView = ({ data }) => {
  const [activeTab, setActiveTab] = useState('market_indices');

  if (!data) return <div className="empty-state">正在初始化数据...</div>;

  const { dashboard_summary, signal_changes, paths } = data;
  const { signal_overview, latest_run } = dashboard_summary;

  const stats = [
    { 
      header: '📈 市场指数', 
      value: `${signal_overview.index.bullish}/${latest_run.index_count}`, 
      desc: `看多: ${signal_overview.index.bullish} | 看空: ${signal_overview.index.bearish}`,
      delay: '0s'
    },
    { 
      header: '🧱 行业板块', 
      value: `${signal_overview.sector.bullish}/${latest_run.sector_count}`, 
      desc: `看多: ${signal_overview.sector.bullish} | 中性: ${signal_overview.sector.neutral}`,
      delay: '0.05s'
    },
    { 
      header: '🎯 核心个股', 
      value: `${signal_overview.stock.bullish}/${latest_run.stock_count}`, 
      desc: `看多: ${signal_overview.stock.bullish} | 看空: ${signal_overview.stock.bearish}`,
      delay: '0.1s'
    },
    { 
      header: '🚨 信号变更', 
      value: signal_changes.summary.sector_change_count + signal_changes.summary.index_change_count, 
      desc: '今日新增变更',
      delay: '0.15s'
    },
  ];

  const renderTable = () => {
    // In parity with static-ui-reference.html, showing top changes
    const items = signal_changes.top_changes || [];
    
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
      <section className="dashboard-grid">
        {stats.map((stat, idx) => (
          <div className="stat-card animate-in" key={idx} style={{ animationDelay: stat.delay }}>
            <div className="stat-header">{stat.header}</div>
            <div className="stat-value">{stat.value}</div>
            <div className="stat-desc">{stat.desc}</div>
          </div>
        ))}
      </section>

      <section className="tabs-section animate-in" style={{ animationDelay: '0.2s' }}>
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

      <section className="panel-section animate-in" style={{ marginTop: '40px', animationDelay: '0.3s' }}>
        <div className="panel-title">🔗 快照路径索引</div>
        <div className="health-list" style={{ fontFamily: 'monospace', fontSize: '11px' }}>
          {Object.entries(paths).map(([key, value]) => (
            <div className="health-row" key={key}>
              <span className="health-label">{key}</span>
              <span className="health-value">{value}</span>
            </div>
          ))}
        </div>
      </section>

      <section className="panel-section animate-in" style={{ marginTop: '32px', animationDelay: '0.4s' }}>
        <div className="panel-title">💬 系统运行提示</div>
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
    </div>
  );
};

export default DashboardView;
