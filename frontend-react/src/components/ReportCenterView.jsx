import React from 'react';

const ReportCenterView = ({ data }) => {
  if (!data) return <div className="empty-state">正在载入报告信息...</div>;

  const { latest_run, paths } = data;

  return (
    <div id="reportsView" className="view-container active">
      <section className="animate-in">
        <div className="report-card">
          <div className="report-icon">📄</div>
          <div className="report-info">
            <h3 id="reportTitle">最新分析日报</h3>
            <p id="reportSub" style={{ color: 'var(--mac-text-secondary)', fontSize: '14px', margin: 0 }}>
              {latest_run.report_path || '未生成报告'}
            </p>
            
            <div className="report-meta-grid">
              <div className="health-list">
                <div className="health-row">
                  <span className="health-label">报告日期</span>
                  <span className="health-value" id="reportDate">{latest_run.run_date}</span>
                </div>
                <div className="health-row">
                  <span className="health-label">运行状态</span>
                  <span className="health-value" id="reportStatus">{latest_run.status}</span>
                </div>
              </div>
              <div className="health-list">
                <div className="health-row">
                  <span className="health-label">生成时间</span>
                  <span className="health-value" id="reportGenTime">{latest_run.finished_at.split('T')[1] || '--'}</span>
                </div>
                <div className="health-row">
                  <span className="health-label">资产总数</span>
                  <span className="health-value" id="reportAssetCount">
                    {latest_run.index_count + latest_run.sector_count + latest_run.stock_count}
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="panel-section animate-in" style={{ animationDelay: '0.1s' }}>
        <div className="panel-title">📦 可用数据产物列表</div>
        <div className="product-list" id="productList">
          {Object.entries(paths).map(([key, path]) => (
            <div className="product-item" key={key}>
              <span className="product-label">{key}</span>
              <span className="product-path">{path}</span>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
};

export default ReportCenterView;
