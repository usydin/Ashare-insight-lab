import React from 'react';

const DataHealthPanel = ({ health }) => {
  if (!health) return <div className="empty-state">数据健康信息不可用</div>;

  const { ok_count, risk_item_count, fetch_failed_count, stale_data_count, stale_cache_count, cache_fallback_count, unavailable_count } = health;

  return (
    <section className="panel-section animate-in" style={{ animationDelay: '0.3s' }}>
      <div className="panel-title">🛡️ 数据健康与诊断</div>
      <div className="health-grid">
        <div className="health-card">
          <div className="health-header">
            <span className="health-icon" style={{ color: 'var(--mac-success)' }}>●</span>
            <span className="health-label">在线正常项</span>
          </div>
          <div className="health-value">{ok_count || 0}</div>
        </div>
        <div className="health-card">
          <div className="health-header">
            <span className="health-icon" style={{ color: 'var(--mac-cyan)' }}>●</span>
            <span className="health-label">缓存兜底项</span>
          </div>
          <div className="health-value">{cache_fallback_count || 0}</div>
        </div>
        <div className="health-card">
          <div className="health-header">
            <span className="health-icon" style={{ color: 'var(--mac-warning)' }}>●</span>
            <span className="health-label">过期缓存项</span>
          </div>
          <div className="health-value">{stale_cache_count || 0}</div>
        </div>
        <div className="health-card">
          <div className="health-header">
            <span className="health-icon" style={{ color: 'var(--mac-danger)' }}>●</span>
            <span className="health-label">采集失败项</span>
          </div>
          <div className="health-value">{fetch_failed_count || 0}</div>
        </div>
      </div>

      <div style={{ marginTop: '16px', display: 'flex', flexDirection: 'column', gap: '8px' }}>
        {cache_fallback_count > 0 && (
          <div className="source-status-note cache">
            💡 在线源失败，已使用本地缓存兜底。
          </div>
        )}
        {stale_cache_count > 0 && (
          <div className="source-status-note stale">
            ⚠️ 当前使用的是过期缓存，仅供复核观察。
          </div>
        )}
        {fetch_failed_count > 0 && (
          <div className="source-status-note failed">
            ❌ 存在采集失败项：在线源与缓存均不可用。
          </div>
        )}
      </div>

      <div className="health-list" style={{ marginTop: '16px' }}>
        <div className="health-row">
          <span className="health-label">OK 资产</span>
          <span className="health-value" style={{ color: 'var(--mac-success)' }}>{health.ok_count || 0}</span>
        </div>
        <div className="health-row">
          <span className="health-label">风险项</span>
          <span className="health-value" style={{ color: 'var(--mac-danger)' }}>{health.risk_item_count || 0}</span>
        </div>
        <div className="health-row">
          <span className="health-label">采集失败</span>
          <span className="health-value">{health.fetch_failed_count || 0}</span>
        </div>
        <div className="health-row">
          <span className="health-label">陈旧数据</span>
          <span className="health-value">{health.stale_data_count || 0}</span>
        </div>
        <div className="health-row">
          <span className="health-label">数据缺失</span>
          <span className="health-value">{health.unavailable_count || 0}</span>
        </div>
      </div>
      <div id="healthSummary" style={{ marginTop: '12px', padding: '10px', background: 'rgba(0,0,0,0.02)', borderRadius: 'var(--mac-radius-sm)', fontSize: '11px', lineHeight: '1.4', color: 'var(--mac-text-secondary)' }}>
        {health.risk_item_count > 0 
          ? `检测到 ${health.risk_item_count} 个风险项，请在控制台查看详细错误日志。`
          : '系统当前数据资产完整度较高，未发现重大同步风险。'}
      </div>
    </section>
  );
};

export default DataHealthPanel;
