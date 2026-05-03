import React from 'react';

const MarketIndexView = ({ data }) => {
  if (!data) return <div className="empty-state">正在初始化数据...</div>;

  const { review_queue, dashboard_summary } = data;
  const indices = review_queue.items.filter(item => item.asset_type === 'index');
  const summary = dashboard_summary.signal_overview.index;

  return (
    <div className="view-container active">
      <section className="animate-in">
        <div className="report-card" style={{ marginBottom: '24px' }}>
          <div className="report-icon">📈</div>
          <div className="report-info">
            <h3>市场指数详情</h3>
            <p style={{ color: 'var(--mac-text-secondary)', fontSize: '14px', margin: 0 }}>
              监控 A 股核心指数趋势，评估全市场风险偏好与运行基调。
            </p>
            <div className="report-meta-grid">
              <div className="health-list">
                <div className="health-row">
                  <span className="health-label">看多指数</span>
                  <span className="health-value" style={{ color: 'var(--mac-success)' }}>{summary.bullish}</span>
                </div>
                <div className="health-row">
                  <span className="health-label">看空指数</span>
                  <span className="health-value" style={{ color: 'var(--mac-danger)' }}>{summary.bearish}</span>
                </div>
              </div>
              <div className="health-list">
                <div className="health-row">
                  <span className="health-label">中性指数</span>
                  <span className="health-value">{summary.neutral}</span>
                </div>
                <div className="health-row">
                  <span className="health-label">资产总数</span>
                  <span className="health-value">{dashboard_summary.latest_run.index_count}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="panel-section animate-in" style={{ animationDelay: '0.1s' }}>
        <div className="panel-title">📡 实时信号明细</div>
        <div className="tab-content">
          <table className="data-table">
            <thead>
              <tr>
                <th>指数名称</th>
                <th>最新信号</th>
                <th>数据状态</th>
                <th>观察原因</th>
                <th>建议操作</th>
              </tr>
            </thead>
            <tbody>
              {indices.length > 0 ? indices.map((item, idx) => (
                <tr key={idx}>
                  <td style={{ fontWeight: 600 }}>{item.name}</td>
                  <td>
                    <span className={`sig-badge sig-${item.latest_signal === 'trend_up' ? 'bullish' : (item.latest_signal === 'trend_down' ? 'bearish' : 'neutral')}`}>
                      {item.latest_signal}
                    </span>
                  </td>
                  <td>{item.latest_data_status}</td>
                  <td style={{ fontSize: '12px', color: 'var(--mac-text-secondary)' }}>{item.reason}</td>
                  <td style={{ fontSize: '12px' }}>{item.suggested_action}</td>
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

export default MarketIndexView;
