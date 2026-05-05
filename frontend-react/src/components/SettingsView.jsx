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

      <section className="panel-section animate-in" style={{ animationDelay: '0.25s' }}>
        <div className="section-heading">🔌 长桥 OpenAPI 只读行情（候选源）</div>
        <div className="state-card">
          <div className="meta-row">
            <span className="meta-label">当前接入</span>
            <span className="meta-value">只读行情原型，CLI 可用</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">默认数据源</span>
            <span className="meta-value">AkShare</span>
          </div>
          <div className="meta-row" style={{ border: 'none' }}>
            <span className="meta-label">候选数据源</span>
            <span className="meta-value">Longbridge（后续评估实时推送与批量刷新）</span>
          </div>
          <div className="meta-row" style={{ marginTop: '8px' }}>
            <span className="meta-label">CLI 检测</span>
            <span className="meta-value code">python3 app.py longbridge-status</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">示例查询</span>
            <span className="meta-value code">python3 app.py longbridge-quote --symbol 600519 --market CN</span>
          </div>
          <div className="meta-row" style={{ border: 'none' }}>
            <span className="meta-label">安全提示</span>
            <span className="meta-value" style={{ fontSize: '11px' }}>不读取/不保存/不显示 token；环境变量仅用于命令行检测。</span>
          </div>
        </div>
      </section>

      <section className="panel-section animate-in" style={{ animationDelay: '0.28s' }}>
        <div className="section-heading">🔐 本地 API Token 状态</div>
        <div className="state-card">
          <div style={{ fontSize: '12px', color: 'var(--mac-text-secondary)', marginBottom: '12px', lineHeight: 1.6 }}>
            本页面仅显示本机 API 凭证的脱敏状态，不展示完整 Token。真实 Token 保存在本机 `.env` 或 `.secrets` 中，不会进入 Git。
          </div>
          <div className="meta-row">
            <span className="meta-label">Marketaux 新闻 API</span>
            <span className="meta-value">状态查看：python3 app.py token-status</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">替换 Marketaux Token</span>
            <span className="meta-value code">python3 app.py token-set --key MARKETAUX_API_TOKEN</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">Longbridge 行情 API</span>
            <span className="meta-value">App Key / Secret 已配置，Legacy Access Token 未配置</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">Longbridge OAuth Token</span>
            <span className="meta-value">未配置 / 已配置 / 已过期，仅显示脱敏状态</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">推荐下一步</span>
            <span className="meta-value code">python3 app.py longbridge-oauth-help</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">OAuthBuilder 验证</span>
            <span className="meta-value">待执行 / 已支持 CLI</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">只读行情验证命令</span>
            <span className="meta-value code">python3 app.py longbridge-oauth-quote --symbol 600519 --market CN</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">安全边界</span>
            <span className="meta-value">只读行情，不接交易</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">前端输入</span>
            <span className="meta-value">不在前端输入 token</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">SDK 探测</span>
            <span className="meta-value code">python3 app.py longbridge-sdk-status</span>
          </div>
          <div className="meta-row">
            <span className="meta-label">OpenAI API</span>
            <span className="meta-value">用于后续 AI 摘要、研报与投研助手</span>
          </div>
          <div className="meta-row" style={{ border: 'none' }}>
            <span className="meta-label">Tushare Pro</span>
            <span className="meta-value">预留：A股历史数据、财务数据、基础数据</span>
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
