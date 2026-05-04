import React from 'react';

const renderDataStatus = (status) => {
  const map = {
    'ok': { label: '在线正常', className: 'source-status-ok' },
    'cache_fallback': { label: '缓存兜底', className: 'source-status-cache' },
    'stale_cache': { label: '过期缓存', className: 'source-status-stale' },
    'fetch_failed': { label: '采集失败', className: 'source-status-failed' },
    'unavailable': { label: '不可用', className: 'source-status-failed' }
  };
  const config = map[status] || { label: '状态未知', className: 'source-status-unknown' };
  return <span className={`source-status-badge ${config.className}`}>{config.label}</span>;
};

const SectorBoardView = ({ data }) => {
  if (!data) return <div className="empty-state">正在初始化数据...</div>;

  const { review_queue, dashboard_summary, signal_changes } = data;
  
  // Combine sector data from different sources
  const sectorItems = review_queue.items.filter(item => item.asset_type === 'sector');
  const changedSectors = signal_changes.top_changes.filter(item => item.asset_type === 'sector');
  
  const summary = dashboard_summary.signal_overview.sector;

  return (
    <div className="view-container active">
      <section className="animate-in">
        <div className="report-card" style={{ marginBottom: '24px' }}>
          <div className="report-icon">❖</div>
          <div className="report-info">
            <h3>行业板块详情</h3>
            <p style={{ color: 'var(--mac-text-secondary)', fontSize: '14px', margin: 0 }}>
              多维跟踪申万二级或核心概念板块，挖掘行业轮动机会与结构性风险。
            </p>
            <div className="report-meta-grid">
              <div className="health-list">
                <div className="health-row">
                  <span className="health-label">看多板块</span>
                  <span className="health-value" style={{ color: 'var(--mac-success)' }}>{summary.bullish}</span>
                </div>
                <div className="health-row">
                  <span className="health-label">风险板块</span>
                  <span className="health-value" style={{ color: 'var(--mac-danger)' }}>{dashboard_summary.data_health.risk_item_count}</span>
                </div>
              </div>
              <div className="health-list">
                <div className="health-row">
                  <span className="health-label">中性板块</span>
                  <span className="health-value">{summary.neutral}</span>
                </div>
                <div className="health-row">
                  <span className="health-label">资产总数</span>
                  <span className="health-value">{dashboard_summary.latest_run.sector_count}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="panel-section animate-in" style={{ animationDelay: '0.1s' }}>
        <div className="panel-title">🚨 重点板块信号</div>
        <div className="tab-content">
          <table className="data-table">
            <thead>
              <tr>
                <th>板块名称</th>
                <th>最新信号</th>
                <th>数据状态</th>
                <th>变更/风险原因</th>
                <th>研究提示</th>
              </tr>
            </thead>
            <tbody>
              {sectorItems.length > 0 || changedSectors.length > 0 ? (
                // Use a Set to avoid duplicates if same sector is in both
                [...new Map([...sectorItems, ...changedSectors].map(item => [item.name, item])).values()].map((item, idx) => (
                  <tr key={idx}>
                    <td style={{ fontWeight: 600 }}>{item.name}</td>
                    <td>
                      <span className={`sig-badge sig-${item.latest_signal === 'trend_up' ? 'bullish' : (item.latest_signal === 'trend_down' ? 'bearish' : 'neutral')}`}>
                        {item.latest_signal}
                      </span>
                    </td>
                    <td>{renderDataStatus(item.latest_data_status)}</td>
                    <td style={{ fontSize: '12px', color: 'var(--mac-text-secondary)' }}>{item.reason || item.change_type}</td>
                    <td style={{ fontSize: '12px' }}>{item.suggested_action || '例行观察'}</td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan="5" className="empty-state">
                    当前快照未提供该分类明细，可在 run-daily 后同步前端快照刷新。
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </section>
    </div>
  );
};

export default SectorBoardView;
