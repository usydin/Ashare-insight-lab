import RefreshDataPanel from './RefreshDataPanel';
import MarketauxConfigPanel from './MarketauxConfigPanel';

const SettingsView = ({ data }) => {
  if (!data) return (
    <div className="empty-state">
      <span className="empty-state-icon">⚙️</span>
      正在载入设置...
    </div>
  );
  
  const { app } = data;

  return (
    <div id="settingsView" className="view-container active">
      <section className="panel-section animate-in">
        <div className="section-heading">⚙️ 系统与品牌信息</div>
        <div className="state-card app-identity-card">
          <div className="meta-row">
            <span className="meta-label">产品名称</span>
            <span className="meta-value">A股智研台</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">English Name</span>
            <span className="meta-value">AShare Insight Lab</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">核心版本</span>
            <span className="meta-value">{app?.version || 'v0.6.7'}</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">开发者</span>
            <span className="meta-value">pL</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">版权所有</span>
            <span className="meta-value" style={{ fontSize: '11px' }}>Copyright © 2026 @B‘lock10STUdio. All rights reserved.</span>
          </div>
        </div>
      </section>

      <section className="panel-section animate-in" style={{ animationDelay: '0.1s' }}>
        <div className="section-heading">🔄 数据刷新与快照同步</div>
        <RefreshDataPanel snapshotAt={data?.generated_at} latestRun={data?.latest_run} />
      </section>

      <section className="panel-section animate-in" style={{ animationDelay: '0.2s' }}>
        <div className="section-heading">🌍 国际新闻数据源</div>
        <MarketauxConfigPanel />
      </section>

      <section className="panel-section animate-in" style={{ animationDelay: '0.3s' }}>
        <div className="section-heading">🖼️ 品牌资产预览 (Local Brand Assets)</div>
        <div className="state-card">
          <div className="meta-row">
            <span className="meta-label">侧边栏 Logo</span>
            <span className="meta-value code">/brand/logo.png</span>
          </div>
          <div className="meta-row" style={{ border: 'none' }}>
            <span className="meta-label">Hero Banner 预览</span>
            <span className="meta-value code">/brand/banner2.png</span>
          </div>
          <img 
            src="/brand/banner2.png" 
            alt="Banner Preview" 
            className="brand-banner-preview"
            onError={(e) => { e.target.style.display = 'none'; }}
          />
          <div className="meta-row" style={{ marginTop: '16px' }}>
            <span className="meta-label">应用图标 (.icns)</span>
            <span className="meta-value code">src-tauri/icons/icon.icns</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">Favicon</span>
            <span className="meta-value code">/brand/favicon_32.png</span>
          </div>
        </div>
      </section>

      <div className="brand-watermark">A股智研台 | AShare Insight Lab</div>

      <div style={{ marginTop: '40px', textAlign: 'center' }}>
        <p style={{ fontSize: '11px', color: 'var(--mac-text-secondary)' }}>更多个性化设置（UI 风格、数据同步频率等）开发中。</p>
      </div>
    </div>
  );
};

export default SettingsView;
