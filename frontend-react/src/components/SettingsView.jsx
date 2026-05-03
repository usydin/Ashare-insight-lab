import React from 'react';

const SettingsView = ({ data }) => {
  if (!data) return <div className="empty-state">载入设置中...</div>;
  const { app } = data;

  return (
    <div id="settingsView" className="view-container active">
      <section className="panel-section animate-in">
        <div className="panel-title">⚙️ 系统设置</div>
        <div className="health-list">
          <div className="health-row">
            <span className="health-label">产品名称</span>
            <span className="health-value" id="settingsAppName">{app.name_cn}</span>
          </div>
          <div className="health-row">
            <span className="health-label">English Name</span>
            <span className="health-value">{app.name_en}</span>
          </div>
          <div className="health-row">
            <span className="health-label">核心版本</span>
            <span className="health-value" id="settingsVersion">{app.version}</span>
          </div>
          <div className="health-row">
            <span className="health-label">开发者</span>
            <span className="health-value" id="settingsDev">{app.developer}</span>
          </div>
          <div className="health-row">
            <span className="health-label">所属品牌</span>
            <span className="health-value">b‘lock10STUdio</span>
          </div>
        </div>
      </section>

      <section className="panel-section animate-in" style={{ animationDelay: '0.1s' }}>
        <div className="panel-title">🖼️ 品牌资源索引</div>
        <div className="health-list">
          <div className="health-row">
            <span className="health-label">Logo 路径</span>
            <span className="health-value" style={{ fontFamily: 'monospace', fontSize: '11px' }}>src/assets/logo.png</span>
          </div>
          <div className="health-row">
            <span className="health-label">macOS 图标 (.icns)</span>
            <span className="health-value" style={{ fontFamily: 'monospace', fontSize: '11px' }}>asset/logo/logo.icns</span>
          </div>
          <div className="health-row">
            <span className="health-label">Windows 图标 (.ico)</span>
            <span className="health-value" style={{ fontFamily: 'monospace', fontSize: '11px' }}>asset/logo/logo.ico</span>
          </div>
          <div className="health-row">
            <span className="health-label">启动动画预留</span>
            <span className="health-value" style={{ fontSize: '11px', color: 'var(--mac-accent)' }}>后续 macOS App 打包阶段可接入品牌启动动画。</span>
          </div>
        </div>
      </section>

      <section className="panel-section animate-in" style={{ animationDelay: '0.2s' }}>
        <div className="panel-title">🔗 数据快照源</div>
        <div className="health-list">
          <div className="health-row">
            <span className="health-label">当前快照路径</span>
            <span className="health-value" style={{ fontFamily: 'monospace', fontSize: '11px' }}>src/data/snapshot.json</span>
          </div>
        </div>
      </section>

      <div className="empty-state" style={{ paddingTop: '20px' }}>
        <p style={{ fontSize: '12px', color: 'var(--mac-text-secondary)' }}>更多个性化设置（UI 风格、数据同步频率等）开发中。</p>
      </div>
    </div>
  );
};

export default SettingsView;
