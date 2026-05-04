import { useState } from 'react';

const MarketauxConfigPanel = () => {
  const [copyStatus, setCopyStatus] = useState('复制 CLI 命令');
  const [statusCopy, setStatusCopy] = useState('复制状态检测命令');

  const cliCommand = `source .venv/bin/activate
export MARKETAUX_API_TOKEN="你的 token"
python3 app.py international-news --ticker AAPL --market US --hours 72 --limit 3`;

  const statusCommand = `python3 app.py marketaux-status`;

  const handleCopy = (text, kind) => {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(() => {
        if (kind === 'cli') {
          setCopyStatus('已复制');
          setTimeout(() => setCopyStatus('复制 CLI 命令'), 2000);
          return;
        }
        setStatusCopy('已复制');
        setTimeout(() => setStatusCopy('复制状态检测命令'), 2000);
      });
      return;
    }
    alert('当前环境不支持自动复制，请手动选择命令。');
  };

  return (
    <div className="marketaux-panel">
      <div className="state-card-header">
        <div className="state-card-title">国际新闻数据源 / Marketaux</div>
      </div>

      <div className="api-status-grid">
        <div className="api-status-card">
          <div className="meta-label">模块状态</div>
          <div className="meta-value">已接入 CLI</div>
        </div>
        <div className="api-status-card">
          <div className="meta-label">Token 来源</div>
          <div className="meta-value code">MARKETAUX_API_TOKEN</div>
        </div>
        <div className="api-status-card">
          <div className="meta-label">当前 UI</div>
          <div className="meta-value">不读取、不保存、不显示 token</div>
        </div>
        <div className="api-status-card">
          <div className="meta-label">免费额度</div>
          <div className="meta-value">100 requests/day，默认每次最多 3 条</div>
        </div>
        <div className="api-status-card">
          <div className="meta-label">已验证样例</div>
          <div className="meta-value">AAPL 可返回新闻</div>
        </div>
        <div className="api-status-card">
          <div className="meta-label">港股覆盖</div>
          <div className="meta-value">00700.HK 暂无结果，后续需继续研究</div>
        </div>
      </div>

      <div className="cli-command-card">
        <div className="state-card-header">
          <div className="state-card-title" style={{ fontSize: '14px' }}>配置状态检测命令</div>
          <button className={`copy-button ${statusCopy === '已复制' ? 'success' : ''}`} onClick={() => handleCopy(statusCommand, 'status')}>
            {statusCopy === '已复制' ? '已复制' : '复制状态检测命令'}
          </button>
        </div>
        <pre className="command-block">
          <code>{statusCommand}</code>
        </pre>
        <div className="meta-value" style={{ fontSize: '12px', color: 'var(--mac-text-secondary)' }}>
          该命令只检查环境变量是否存在，不会访问 Marketaux API，不会消耗免费额度。
        </div>
      </div>

      <div className="cli-command-card">
        <div className="state-card-header">
          <div className="state-card-title" style={{ fontSize: '14px' }}>CLI 测试命令</div>
          <button className={`copy-button ${copyStatus === '已复制' ? 'success' : ''}`} onClick={() => handleCopy(cliCommand, 'cli')}>
            {copyStatus === '已复制' ? '已复制' : '复制 CLI 命令'}
          </button>
        </div>
        <pre className="command-block">
          <code>{cliCommand}</code>
        </pre>
      </div>

      <div className="security-note">
        <div className="meta-label">安全提示</div>
        <ul>
          <li>不要把 token 写入源码。</li>
          <li>不要把 token 提交到 GitHub。</li>
          <li>当前阶段不接 run-daily，避免消耗免费额度。</li>
        </ul>
      </div>

      <div className="security-note">
        <div className="meta-label">后续路线</div>
        <ul>
          <li>V0.8.4 可考虑配置状态检测。</li>
          <li>V0.8.5 可考虑 Watchlist 新闻观察。</li>
          <li>V1.x 再考虑 AI 摘要。</li>
        </ul>
      </div>
    </div>
  );
};

export default MarketauxConfigPanel;
