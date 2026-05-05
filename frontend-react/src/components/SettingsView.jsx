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
  const sourceStatus = data?.source_status || {
    default_quote_source: 'akshare',
    sources: [],
  };
  const sourceMap = Object.fromEntries((sourceStatus.sources || []).map((item) => [item.source_id, item]));
  const longbridgeSource = sourceMap.longbridge || {};
  const marketauxSource = sourceMap.marketaux || {};
  const tushareSource = sourceMap.tushare || {};
  const akshareSource = sourceMap.akshare || {};

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

      <section className="panel-section animate-in" style={{ animationDelay: '0.25s' }}>
        <div className="section-heading">🔐 API Token 状态</div>
        <div className="state-card">
          <div style={{ fontSize: '12px', color: 'var(--mac-text-secondary)', marginBottom: '12px', lineHeight: 1.6 }}>
            本页面只显示凭证状态和 CLI 指引，不展示完整 token、不展示完整授权 URL，也不提供前端录入入口。真实凭证仅保存在本机 `.env` 或 `.secrets`。
          </div>
          <div className="meta-row">
            <span className="meta-label">Marketaux Token</span>
            <span className="meta-value">状态查看：python3 app.py token-status</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">更新 Marketaux Token</span>
            <span className="meta-value code">python3 app.py token-set --key MARKETAUX_API_TOKEN</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">Longbridge App Key / Secret</span>
            <span className="meta-value">状态查看：python3 app.py longbridge-status</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">Longbridge OAuth Token</span>
            <span className="meta-value">状态查看：python3 app.py longbridge-oauth-status</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">Longbridge OAuth 指引</span>
            <span className="meta-value code">python3 app.py longbridge-oauth-help</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">OpenAI</span>
            <span className="meta-value">状态查看：python3 app.py token-status</span>
          </div>
          <div className="meta-row" style={{ border: 'none' }}>
            <span className="meta-label">Tushare</span>
            <span className="meta-value">状态查看：python3 app.py token-status</span>
          </div>
        </div>
      </section>

      <section className="panel-section animate-in" style={{ animationDelay: '0.28s' }}>
        <div className="section-heading">🛰️ 数据源状态</div>
        <div className="state-card">
          <div style={{ fontSize: '12px', color: 'var(--mac-text-secondary)', marginBottom: '12px', lineHeight: 1.6 }}>
            数据源状态与凭证状态分开展示。当前默认行情源为 AkShare，Longbridge 仅作为候选只读行情源，待 OAuth 阻塞解除后再启用真实切换。
          </div>
          <div className="meta-row">
            <span className="meta-label">AkShare</span>
            <span className="meta-value">{akshareSource.status_label || '可用'} / 默认行情源</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">Longbridge</span>
            <span className="meta-value">{longbridgeSource.status_label || '待授权'} / {longbridgeSource.auth_mode || 'oauthbuilder_required'}</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">Longbridge 安全边界</span>
            <span className="meta-value">quote_only=true / trade_enabled=false</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">Marketaux</span>
            <span className="meta-value">{marketauxSource.status_label || '已配置'} / 国际新闻源</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">Tushare</span>
            <span className="meta-value">{tushareSource.status_label || '预留'} / 历史与财务数据预留</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">统一状态摘要</span>
            <span className="meta-value code">python3 app.py source-status</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">Longbridge CLI 检测</span>
            <span className="meta-value code">python3 app.py longbridge-status</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">Longbridge 只读行情研究</span>
            <span className="meta-value code">python3 app.py longbridge-oauth-quote --symbol 600519 --market CN</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">安全边界</span>
            <span className="meta-value">只读行情，不接交易，不读资产/持仓，不下单/撤单</span>
          </div>
          <div className="meta-row" style={{ border: 'none' }}>
            <span className="meta-label">前端交互</span>
            <span className="meta-value">数据源切换当前仅为视觉原型，不影响后端真实取数</span>
          </div>
        </div>
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
