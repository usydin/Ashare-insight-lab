import React from 'react';

const DataHealthPanel = ({ health }) => {
  if (!health) return <div className="empty-state">数据健康信息不可用</div>;

  return (
    <section className="panel-section">
      <div className="panel-title">💾 数据资产概况</div>
      <div className="health-list">
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
