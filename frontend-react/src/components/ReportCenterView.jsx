import React, { useState } from 'react';

const ReportCenterView = ({ data }) => {
  const [copyStatus, setCopyStatus] = useState({});

  if (!data) return (
    <div className="empty-state">
      <span className="empty-state-icon">📊</span>
      正在载入报告信息...
    </div>
  );

  const { latest_run, snapshot, dashboard_summary, signal_changes, paths } = data;

  const handleCopy = (text, key) => {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(() => {
        setCopyStatus({ ...copyStatus, [key]: '已复制' });
        setTimeout(() => setCopyStatus({ ...copyStatus, [key]: null }), 2000);
      });
    } else {
      alert('您的浏览器不支持自动复制，请手动选择文字进行复制。');
    }
  };

  const productMatrix = [
    { key: 'daily_report', name: '分析日报 (Markdown)', path: latest_run?.report_path, desc: '包含当日行情摘要、板块分析及自选股信号变化的完整报告。' },
    { key: 'ui_snapshot_json', name: 'UI 快照 (JSON)', path: paths?.ui_snapshot_json, desc: '前端 UI 渲染的核心数据源，包含 Dashboard 和关注队列。' },
    { key: 'dashboard_summary_json', name: 'Dashboard 摘要 (JSON)', path: paths?.dashboard_summary_json, desc: '用于快速统计和展示当日运行结果的摘要数据。' },
    { key: 'review_queue_json', name: '关注队列 (JSON)', path: paths?.review_queue_json, desc: '经过策略筛选出的每日重点关注项及其建议动作。' },
    { key: 'review_queue_csv', name: '关注队列 (CSV)', path: paths?.review_queue_csv, desc: '关注队列的 CSV格式，便于导入 Excel 或第三方工具。' },
    { key: 'signal_changes_csv', name: '信号变化 (CSV)', path: paths?.signal_changes_csv, desc: '与上一轮运行相比，所有资产的信号变化详细记录。' },
    { key: 'daily_signals_csv', name: '自选股信号 (CSV)', path: paths?.daily_signals_csv, desc: '当日所有监控自选股的 MA 策略计算结果。' },
    { key: 'index_signals_csv', name: '指数信号 (CSV)', path: paths?.index_signals_csv, desc: '当日市场核心指数的策略计算与趋势判断结果。' },
    { key: 'sector_signals_csv', name: '板块信号 (CSV)', path: paths?.sector_signals_csv, desc: '当日各行业板块的强弱信号与趋势判断结果。' },
  ];

  const riskCount = dashboard_summary?.data_health?.risk_item_count || 0;
  const healthStatus = riskCount > 0 ? 'Risk' : 'Healthy';

  return (
    <div id="reportsView" className="view-container active">
      <div className="section-heading">报告中心摘要</div>
      {/* 摘要区 */}
      <section className="report-summary-grid animate-in">
        <div className="summary-stat-card">
          <div className="stat-label">今日关注项</div>
          <div className="stat-value">{data?.review_queue?.count || 0}</div>
        </div>
        <div className="summary-stat-card">
          <div className="stat-label">资产信号变化</div>
          <div className="stat-value">
            {signal_changes?.summary?.index_change_count || 0} / {signal_changes?.summary?.sector_change_count || 0} / {signal_changes?.summary?.stock_change_count || 0}
          </div>
        </div>
        <div className="summary-stat-card">
          <div className="stat-label">数据健康状态</div>
          <div className={`stat-value ${healthStatus === 'Risk' ? 'text-danger' : 'text-success'}`}>
            {healthStatus} {riskCount > 0 ? `(${riskCount})` : ''}
          </div>
        </div>
      </section>

      {/* 最新分析日报主卡片 */}
      <section className="animate-in" style={{ animationDelay: '0.1s' }}>
        <div className="report-hero-card">
          <div className="report-icon">📊</div>
          <div className="report-hero-content">
            <div className="hero-header">
              <h3>最新分析日报</h3>
              <div className={`status-pill ${latest_run?.status || 'unknown'}`}>
                {latest_run?.status || '未知'}
              </div>
            </div>
            <div className="hero-meta-grid">
              <div className="meta-row">
                <span className="meta-label">运行日期:</span>
                <span className="meta-value">{latest_run?.run_date || '未运行'}</span>
              </div>
              <div className="meta-row">
                <span className="meta-label">快照生成:</span>
                <span className="meta-value">{data?.generated_at ? data.generated_at.replace('T', ' ') : '待同步'}</span>
              </div>
              <div className="meta-row">
                <span className="meta-label">报告路径:</span>
                <code className="hero-path">{latest_run?.report_path || '暂无路径'}</code>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* 报告产物矩阵 */}
      <section className="panel-section animate-in" style={{ animationDelay: '0.2s' }}>
        <div className="section-heading">📦 报告产物矩阵</div>
        <div className="report-product-grid">
          {productMatrix.map((product) => (
            <div className="report-product-card" key={product.key}>
              <div className="product-header">
                <div className="product-name">{product.name}</div>
                <div className="product-type">{product.path ? product.path.split('.').pop().toUpperCase() : '--'}</div>
              </div>
              <div className="product-desc">{product.desc}</div>
              <div className="product-path-area">
                <code className="product-path">{product.path || '暂无路径'}</code>
                {product.path && (
                  <button 
                    className={`copy-inline-button ${copyStatus[product.key] ? 'success' : ''}`}
                    onClick={() => handleCopy(product.path, product.key)}
                  >
                    {copyStatus[product.key] || '📋 复制路径'}
                  </button>
                )}
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* 报告状态说明 */}
      <section className="panel-section animate-in" style={{ animationDelay: '0.3s' }}>
        <div className="soft-info">
          <div>
            <p style={{ margin: '0 0 8px', fontWeight: 700 }}>💡 报告中心说明</p>
            <ul className="info-list" style={{ margin: 0, paddingLeft: '20px', fontSize: '12px' }}>
              <li>当前为离线快照报告中心，报告内容来自最近一次 <code>run-daily</code> / <code>ui-snapshot</code>。</li>
              <li>若数据已过期或需要更新，请前往“偏好设置”执行“数据刷新与快照同步”命令。</li>
              <li>本系统不输出任何投资建议，所有报告产物仅作为投研辅助与数据复核入口。</li>
            </ul>
          </div>
        </div>
      </section>
    </div>
  );
};

export default ReportCenterView;
