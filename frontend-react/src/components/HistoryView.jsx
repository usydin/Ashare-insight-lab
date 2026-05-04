import React, { useState } from 'react';

const HistoryView = ({ data }) => {
  const [copyStatus, setCopyStatus] = useState({});

  if (!data) return <div className="empty-state">正在加载运行记录...</div>;

  const { latest_run, paths, generated_at } = data;

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

  const timelineItems = [
    {
      title: '最新运行 (Latest Run)',
      time: latest_run?.finished_at ? latest_run.finished_at.replace('T', ' ') : '暂无数据',
      desc: `执行状态: ${latest_run?.status || '未知'}，处理资产共计 ${(latest_run?.index_count || 0) + (latest_run?.sector_count || 0) + (latest_run?.stock_count || 0)} 个。`,
      icon: '🚀'
    },
    {
      title: '快照生成 (Snapshot Generation)',
      time: generated_at || '未知',
      desc: '后端 UI 结构化快照已生成，包含 Dashboard、关注队列与信号变更。',
      icon: '📸'
    },
    {
      title: '报告产物生成 (Report Assets)',
      time: latest_run?.finished_at ? latest_run.finished_at.replace('T', ' ') : '暂无数据',
      desc: `分析日报已输出至: ${latest_run?.report_path || '暂无路径'}`,
      path: latest_run?.report_path,
      icon: '📄'
    },
    {
      title: '前端快照同步 (Frontend Sync)',
      time: generated_at || '未知',
      desc: '数据已同步至前端静态目录，当前桌面应用正在展示此快照内容。',
      icon: '🔄'
    }
  ];

  return (
    <div className="view-container active">
      {/* 说明卡片 */}
      <section className="animate-in">
        <div className="soft-info" style={{ marginBottom: '24px' }}>
          <div>
            <p style={{ margin: '0 0 8px', fontWeight: 700 }}>💡 快照级历史说明</p>
            <ul className="info-list" style={{ margin: 0, paddingLeft: '20px', fontSize: '12px' }}>
              <li>当前展示的是打包快照中的 <code>latest_run</code> 记录。</li>
              <li>完整 SQLite 历史查询功能（支持翻页与搜索）将在后续版本接入。</li>
            </ul>
          </div>
        </div>
      </section>

      {/* 运行摘要卡片 */}
      <section className="animate-in" style={{ animationDelay: '0.1s' }}>
        <div className="state-card" style={{ marginBottom: '32px', borderLeft: '4px solid var(--mac-accent)' }}>
          <div style={{ display: 'flex', gap: '20px' }}>
            <div className="report-icon" style={{ width: '60px', height: '60px', fontSize: '32px' }}>🕒</div>
            <div style={{ flex: 1 }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                <h3 style={{ margin: 0, fontSize: '18px' }}>最新运行摘要</h3>
                <button 
                  className={`copy-inline-button ${copyStatus.summary ? 'success' : ''}`}
                  onClick={copySummary}
                >
                  {copyStatus.summary ? '✅ 已复制摘要' : '📋 复制运行摘要'}
                </button>
              </div>
              <p style={{ color: 'var(--mac-text-secondary)', fontSize: '12px', margin: '4px 0 12px' }}>
                ID: {latest_run?.id || 'N/A'} | 状态: 
                <span className={`status-pill ${latest_run?.status || 'unknown'}`} style={{ marginLeft: '8px' }}>
                  {latest_run?.status || '未知'}
                </span>
              </p>
              <div className="report-meta-grid" style={{ marginTop: '0' }}>
                <div className="health-list">
                  <div className="meta-row">
                    <span className="meta-label">运行日期</span>
                    <span className="meta-value">{latest_run?.run_date || '暂无数据'}</span>
                  </div>
                  <div className="meta-row">
                    <span className="meta-label">快照生成</span>
                    <span className="meta-value">{generated_at ? generated_at.replace('T', ' ') : '暂无数据'}</span>
                  </div>
                </div>
                <div className="health-list">
                  <div className="meta-row">
                    <span className="meta-label">资产总计</span>
                    <span className="meta-value">
                      {(latest_run?.index_count || 0) + (latest_run?.sector_count || 0) + (latest_run?.stock_count || 0)}
                    </span>
                  </div>
                  <div className="meta-row">
                    <span className="meta-label">核心版本</span>
                    <span className="meta-value">{latest_run?.app_version || 'v0.0.0'}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* 时间线视图 */}
      <section className="panel-section animate-in" style={{ animationDelay: '0.2s' }}>
        <div className="section-heading">🗓️ 运行时间线 (Timeline)</div>
        <div className="timeline-card">
          <div className="timeline-list">
            {timelineItems.map((item, idx) => (
              <div key={idx} className="timeline-item">
                <div className="timeline-dot"></div>
                <div className="timeline-content">
                  <div className="timeline-header">
                    <div className="timeline-title">{item.icon} {item.title}</div>
                    <div className="timeline-time">{item.time || '暂无数据'}</div>
                  </div>
                  <div className="timeline-desc">
                    {item.desc}
                    {item.path && (
                      <div style={{ marginTop: '8px' }}>
                        <button 
                          className={`copy-inline-button ${copyStatus[idx] ? 'success' : ''}`}
                          onClick={() => handleCopy(item.path, idx)}
                        >
                          {copyStatus[idx] ? '✅ 已复制' : '📋 复制路径'}
                        </button>
                      </div>
                    )}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* 底部提示 */}
      <div style={{ marginTop: '40px', textAlign: 'center' }}>
        <p style={{ fontSize: '11px', color: 'var(--mac-text-secondary)' }}>
          提示：若需查看更早的运行历史，请在终端执行 <code>python3 app.py history</code>。
        </p>
      </div>
    </div>
  );
};

export default HistoryView;
