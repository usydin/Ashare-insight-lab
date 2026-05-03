import React from 'react';

const WatchlistView = ({ data }) => {
  if (!data) return <div className="empty-state">正在初始化数据...</div>;

  const { dashboard_summary, review_queue } = data;
  const { watchlist_focus } = dashboard_summary;
  
  const stocks = [
    ...(watchlist_focus.high_priority || []),
    ...(watchlist_focus.watching || [])
  ];

  // De-duplicate by code
  const uniqueStocks = [...new Map(stocks.map(item => [item.code, item])).values()];
  
  const summary = dashboard_summary.signal_overview.stock;

  return (
    <div className="view-container active">
      <section className="animate-in">
        <div className="report-card" style={{ marginBottom: '24px' }}>
          <div className="report-icon">🎯</div>
          <div className="report-info">
            <h3>监控自选详情</h3>
            <p style={{ color: 'var(--mac-text-secondary)', fontSize: '14px', margin: 0 }}>
              深度监控核心个股趋势与异动，支持多维标签分类与观察原因复核。
            </p>
            <div className="report-meta-grid">
              <div className="health-list">
                <div className="health-row">
                  <span className="health-label">看多个股</span>
                  <span className="health-value" style={{ color: 'var(--mac-success)' }}>{summary.bullish}</span>
                </div>
                <div className="health-row">
                  <span className="health-label">看空个股</span>
                  <span className="health-value" style={{ color: 'var(--mac-danger)' }}>{summary.bearish}</span>
                </div>
              </div>
              <div className="health-list">
                <div className="health-row">
                  <span className="health-label">中性个股</span>
                  <span className="health-value">{summary.neutral}</span>
                </div>
                <div className="health-row">
                  <span className="health-label">总监控数</span>
                  <span className="health-value">{dashboard_summary.latest_run.stock_count}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="panel-section animate-in" style={{ animationDelay: '0.1s' }}>
        <div className="panel-title">📋 自选监控列表</div>
        <div className="tab-content">
          <table className="data-table">
            <thead>
              <tr>
                <th>名称/代码</th>
                <th>行业/板块</th>
                <th>最新信号</th>
                <th>收盘/MA20</th>
                <th>观察/风险原因</th>
              </tr>
            </thead>
            <tbody>
              {uniqueStocks.length > 0 ? uniqueStocks.map((item, idx) => (
                <tr key={idx}>
                  <td>
                    <div style={{ display: 'flex', flexDirection: 'column' }}>
                      <span style={{ fontWeight: 600 }}>{item.name}</span>
                      <span style={{ fontSize: '10px', color: 'var(--mac-text-secondary)', fontFamily: 'monospace' }}>{item.code}</span>
                    </div>
                  </td>
                  <td>
                    <div style={{ display: 'flex', flexDirection: 'column' }}>
                      <span style={{ fontSize: '12px' }}>{item.industry}</span>
                      <span style={{ fontSize: '10px', color: 'var(--mac-text-secondary)' }}>{item.board}</span>
                    </div>
                  </td>
                  <td>
                    <span className={`sig-badge sig-${item.signal === 'trend_up' ? 'bullish' : (item.signal === 'trend_down' ? 'bearish' : 'neutral')}`}>
                      {item.signal}
                    </span>
                  </td>
                  <td>
                    <div style={{ display: 'flex', flexDirection: 'column' }}>
                      <span style={{ fontSize: '12px' }}>{item.close}</span>
                      <span style={{ fontSize: '10px', color: 'var(--mac-text-secondary)' }}>{item.ma20?.toFixed(2)}</span>
                    </div>
                  </td>
                  <td style={{ maxWidth: '240px' }}>
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                      <span style={{ fontSize: '11px', color: 'var(--mac-text-primary)' }}>{item.observe_reason}</span>
                      {item.risk_note && (
                        <span style={{ fontSize: '10px', color: 'var(--mac-danger)', background: 'rgba(255, 59, 48, 0.05)', padding: '2px 4px', borderRadius: '2px' }}>
                          ⚠️ {item.risk_note}
                        </span>
                      )}
                    </div>
                  </td>
                </tr>
              )) : (
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

export default WatchlistView;
