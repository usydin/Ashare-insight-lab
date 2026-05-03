import React from 'react';

const HistoryView = ({ data }) => {
  if (!data) return <div className="empty-state">正在加载运行记录...</div>;

  const { latest_run, paths, signal_changes, messages } = data;

  return (
    <div className="view-container active">
      <section className="animate-in">
        <div className="report-card" style={{ marginBottom: '24px', borderLeft: '4px solid var(--mac-accent)' }}>
          <div className="report-icon">🕒</div>
          <div className="report-info">
            <h3>最新运行摘要</h3>
            <p style={{ color: 'var(--mac-text-secondary)', fontSize: '13px', margin: '4px 0 0' }}>
              ID: {latest_run.id || 'N/A'} | 状态: 
              <span style={{ color: latest_run.status === 'success' ? 'var(--mac-success)' : 'var(--mac-danger)', marginLeft: '4px', fontWeight: 600 }}>
                {latest_run.status || '未知'}
              </span>
            </p>
            <div className="report-meta-grid">
              <div className="health-list">
                <div className="health-row">
                  <span className="health-label">运行日期</span>
                  <span className="health-value">{latest_run.run_date || '暂无数据'}</span>
                </div>
                <div className="health-row">
                  <span className="health-label">生成时间</span>
                  <span className="health-value">{latest_run.finished_at ? latest_run.finished_at.replace('T', ' ') : '暂无数据'}</span>
                </div>
              </div>
              <div className="health-list">
                <div className="health-row">
                  <span className="health-label">资产总计</span>
                  <span className="health-value">
                    {(latest_run.index_count || 0) + (latest_run.sector_count || 0) + (latest_run.stock_count || 0)}
                  </span>
                </div>
                <div className="health-row">
                  <span className="health-label">核心版本</span>
                  <span className="health-value">{latest_run.app_version || 'v0.0.0'}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="panel-section animate-in" style={{ animationDelay: '0.1s' }}>
        <div className="panel-title">📦 数据产物时间线</div>
        <div className="health-list" style={{ background: 'transparent', border: 'none' }}>
          {paths && Object.entries(paths).length > 0 ? Object.entries(paths).map(([key, path], idx) => (
            <div className="review-item" key={key} style={{ display: 'flex', alignItems: 'center', gap: '16px', marginBottom: '12px', padding: '12px 16px' }}>
              <div style={{ width: '8px', height: '8px', borderRadius: '50%', background: 'var(--mac-accent)', flexShrink: 0 }}></div>
              <div style={{ flex: 1 }}>
                <div style={{ fontSize: '12px', fontWeight: 700, textTransform: 'uppercase', color: 'var(--mac-text-secondary)', marginBottom: '4px' }}>{key}</div>
                <div style={{ fontSize: '11px', fontFamily: 'monospace', color: 'var(--mac-text-primary)', wordBreak: 'break-all', background: '#f5f5f7', padding: '4px 8px', borderRadius: '4px' }}>{path}</div>
              </div>
            </div>
          )) : (
            <div className="empty-state">暂无产物路径数据</div>
          )}
        </div>
      </section>

      <section className="panel-section animate-in" style={{ animationDelay: '0.2s' }}>
        <div className="panel-title">🚨 信号变更摘要</div>
        <div className="dashboard-grid" style={{ gridTemplateColumns: 'repeat(4, 1fr)', gap: '12px' }}>
          <div className="stat-card" style={{ padding: '12px' }}>
            <div className="stat-header" style={{ fontSize: '10px' }}>指数变更</div>
            <div className="stat-value" style={{ fontSize: '18px' }}>{signal_changes?.summary?.index_change_count ?? 0}</div>
          </div>
          <div className="stat-card" style={{ padding: '12px' }}>
            <div className="stat-header" style={{ fontSize: '10px' }}>板块变更</div>
            <div className="stat-value" style={{ fontSize: '18px' }}>{signal_changes?.summary?.sector_change_count ?? 0}</div>
          </div>
          <div className="stat-card" style={{ padding: '12px' }}>
            <div className="stat-header" style={{ fontSize: '10px' }}>个股变更</div>
            <div className="stat-value" style={{ fontSize: '18px' }}>{signal_changes?.summary?.stock_change_count ?? 0}</div>
          </div>
          <div className="stat-card" style={{ padding: '12px' }}>
            <div className="stat-header" style={{ fontSize: '10px' }}>风险项</div>
            <div className="stat-value" style={{ fontSize: '18px', color: (signal_changes?.summary?.risk_item_count ?? 0) > 0 ? 'var(--mac-danger)' : 'inherit' }}>
              {signal_changes?.summary?.risk_item_count ?? 0}
            </div>
          </div>
        </div>
      </section>

      <section className="panel-section animate-in" style={{ animationDelay: '0.3s' }}>
        <div className="panel-title">💬 系统消息</div>
        <div className="msg-list" style={{ background: 'white', border: '1px solid var(--mac-border)', color: 'var(--mac-text-secondary)' }}>
          {messages && messages.length > 0 ? messages.map((msg, idx) => (
            <div className="msg-item" key={idx}>
              <span>•</span> {msg}
            </div>
          )) : (
            <div className="msg-item">
              <span>ℹ️</span> 当前快照未包含系统运行消息。
            </div>
          )}
        </div>
      </section>

      <div style={{ marginTop: '32px', padding: '16px', background: '#eef4ff', border: '1px solid #d2e3ff', borderRadius: 'var(--mac-radius-md)', textAlign: 'center' }}>
        <p style={{ margin: 0, color: '#004085', fontSize: '12px' }}>
          <strong>说明：</strong>当前为快照级运行历史，完整 SQLite 历史查询将在后续版本接入。
        </p>
      </div>
    </div>
  );
};

export default HistoryView;
