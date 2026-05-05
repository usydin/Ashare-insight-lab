const fallbackSourceStatus = {
  default_quote_source: 'akshare',
  sources: [
    {
      source_id: 'akshare',
      display_name: 'AkShare A股实时行情',
      status: 'available',
      status_label: '可用',
      category: 'quote',
      note: '当前默认 A股快照/免费数据源',
      token_status: 'not_required',
      quote_only: true,
      trade_enabled: false,
    },
    {
      source_id: 'longbridge',
      display_name: 'Longbridge OpenAPI 只读行情',
      status: 'available',
      status_label: '候选可用',
      category: 'quote',
      note: 'OAuth 授权只读实时行情源',
      token_status: 'configured',
      auth_mode: '已授权 / 可读取只读行情',
      quote_only: true,
      trade_enabled: false,
    },
  ],
};

const fallbackRealtimeQuotes = {
  provider: 'longbridge',
  generated_at: '',
  status: 'missing',
  message: '请先运行 python3 app.py longbridge-quote-snapshot 生成实时行情快照。',
  quote_only: true,
  trade_enabled: false,
  items: [],
};

const getStatusPillClass = (status) => {
  if (status === 'available') return 'success';
  if (status === 'blocked') return 'missing';
  return 'unknown';
};

const getQuoteStatusLabel = (status) => {
  if (status === 'ok') return '可用';
  if (status === 'permission_required') return '需权限';
  if (status === 'missing') return '未就绪';
  if (status === 'oauth_required' || status === 'oauthbuilder_required') return '待授权';
  return status || '-';
};

const getQuoteStatusClass = (status) => {
  if (status === 'ok') return 'success';
  if (status === 'permission_required') return 'missing';
  return 'unknown';
};

const formatSourceLabel = (sourceId) => {
  if (sourceId === 'akshare') return 'AkShare';
  if (sourceId === 'longbridge') return 'Longbridge';
  if (sourceId === 'marketaux') return 'Marketaux';
  if (sourceId === 'tushare') return 'Tushare';
  return sourceId;
};

const formatValue = (value, suffix = '') => {
  if (value === null || value === undefined || value === '') return '-';
  return `${value}${suffix}`;
};

const formatSignedValue = (value, suffix = '') => {
  if (value === null || value === undefined || value === '') return '-';
  const numeric = Number(value);
  if (Number.isNaN(numeric)) return `${value}${suffix}`;
  const sign = numeric > 0 ? '+' : '';
  return `${sign}${numeric}${suffix}`;
};

const RealtimeMarketView = ({ data }) => {
  const sourceStatus = data?.source_status || fallbackSourceStatus;
  const realtimeQuotes = data?.realtime_quotes || fallbackRealtimeQuotes;
  const quoteSources = sourceStatus.sources.filter((item) => item.category === 'quote' || item.source_id === 'tushare');
  const defaultSource = quoteSources.find((item) => item.source_id === sourceStatus.default_quote_source) || quoteSources[0];
  const longbridgeSource = sourceStatus.sources.find((item) => item.source_id === 'longbridge');
  const marketauxSource = sourceStatus.sources.find((item) => item.source_id === 'marketaux');
  const tushareSource = sourceStatus.sources.find((item) => item.source_id === 'tushare');
  const quoteItems = Array.isArray(realtimeQuotes.items) ? realtimeQuotes.items : [];

  return (
    <div id="realtimeMarketView" className="view-container active">
      <div className="realtime-page animate-in">
        <header className="page-header">
          <div>
            <div className="section-heading">实时行情</div>
            <div style={{ fontSize: '12px', color: 'var(--mac-text-secondary)', marginTop: '4px' }}>
              Longbridge Quote Snapshot / Manual Refresh
            </div>
          </div>
          <div className="realtime-status-grid">
            <div className="market-mode-pill">模式：手动刷新式实时快照</div>
            <div className="market-mode-pill" style={{ background: 'rgba(0,0,0,0.05)', color: '#666' }}>
              刷新方式：CLI 重新生成 snapshot
            </div>
          </div>
        </header>

        <section className="api-status-grid">
          <div className="api-status-card">
            <div className="meta-label">数据源方案</div>
            <div className="meta-value">AkShare：A股快照 / Longbridge：OAuth 只读行情</div>
          </div>
          <div className="api-status-card">
            <div className="meta-label">Longbridge 快照状态</div>
            <div className="meta-value">{realtimeQuotes.status || '-'}</div>
          </div>
          <div className="api-status-card">
            <div className="meta-label">快照生成时间</div>
            <div className="meta-value">{realtimeQuotes.generated_at || '-'}</div>
          </div>
          <div className="api-status-card">
            <div className="meta-label">安全提示</div>
            <div className="meta-value">前端只读快照，不显示 token，不接交易</div>
          </div>
        </section>

        <section className="quote-table-card" style={{ marginBottom: '20px' }}>
          <div className="section-heading" style={{ marginBottom: '12px' }}>行情源状态</div>
          <div className="api-status-grid" style={{ marginBottom: '16px' }}>
            <div className="api-status-card">
              <div className="meta-label">当前默认行情源</div>
              <div className="meta-value">{formatSourceLabel(sourceStatus.default_quote_source)}</div>
            </div>
            <div className="api-status-card">
              <div className="meta-label">Longbridge OpenAPI</div>
              <div className="meta-value">
                {longbridgeSource ? `${longbridgeSource.status_label} / ${longbridgeSource.auth_mode}` : '待授权 / OAuth 阻塞'}
              </div>
            </div>
            <div className="api-status-card">
              <div className="meta-label">Marketaux 新闻</div>
              <div className="meta-value">{marketauxSource?.status_label || '已配置'}</div>
            </div>
            <div className="api-status-card">
              <div className="meta-label">Tushare</div>
              <div className="meta-value">{tushareSource?.status_label || '预留'}</div>
            </div>
          </div>

          <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', marginBottom: '14px' }}>
            {quoteSources.map((source) => {
              const helperText = source.source_id === 'akshare'
                ? '默认 A股快照/免费数据源'
                : source.source_id === 'longbridge'
                  ? 'OAuth 授权只读实时行情源'
                  : '预留';
              return (
                <div
                  key={source.source_id}
                  style={{
                    borderRadius: '10px',
                    border: source.source_id === sourceStatus.default_quote_source
                      ? '1px solid rgba(10,132,255,0.35)'
                      : '1px solid rgba(255,255,255,0.08)',
                    background: source.source_id === sourceStatus.default_quote_source
                      ? 'rgba(10,132,255,0.12)'
                      : 'rgba(255,255,255,0.04)',
                    color: 'var(--mac-text-primary)',
                    padding: '10px 12px',
                    minWidth: '150px',
                    textAlign: 'left',
                  }}
                >
                  <div style={{ fontSize: '12px', fontWeight: 600 }}>{source.display_name}</div>
                  <div style={{ fontSize: '11px', marginTop: '4px' }}>{source.status_label}</div>
                  <div style={{ fontSize: '10px', marginTop: '4px', color: 'var(--mac-text-secondary)' }}>{helperText}</div>
                </div>
              );
            })}
          </div>

          <div className="api-status-grid" style={{ marginBottom: 0 }}>
            {sourceStatus.sources.map((source) => (
              <div
                key={source.source_id}
                className="api-status-card"
                style={{ background: 'rgba(255,255,255,0.04)', border: '1px solid rgba(255,255,255,0.08)' }}
              >
                <div className="meta-row" style={{ paddingTop: 0 }}>
                  <span className="meta-label">{source.display_name}</span>
                  <span className={`status-pill ${getStatusPillClass(source.status)}`}>{source.status_label}</span>
                </div>
                <div className="meta-row">
                  <span className="meta-label">Token</span>
                  <span className="meta-value">{source.token_status || 'not_required'}</span>
                </div>
                {source.source_id === 'longbridge' && (
                  <div className="meta-row">
                    <span className="meta-label">安全</span>
                    <span className="meta-value">quote_only={String(source.quote_only)}, trade_enabled={String(source.trade_enabled)}</span>
                  </div>
                )}
                <div style={{ fontSize: '11px', color: 'var(--mac-text-secondary)', lineHeight: 1.6 }}>
                  {source.note}
                </div>
              </div>
            ))}
          </div>

          <div className="quote-disclaimer" style={{ marginTop: '14px' }}>
            数据源切换当前仅为视觉原型。默认仍使用 {defaultSource?.display_name || 'AkShare'}，Longbridge 行情通过后端手动刷新式快照接入。
          </div>
        </section>

        <section className="quote-table-card" style={{ marginBottom: '20px' }}>
          <div className="section-heading" style={{ marginBottom: '12px' }}>数据源安全边界</div>
          <div className="api-status-grid">
            <div className="api-status-card">
              <div className="meta-label">quote_only</div>
              <div className="meta-value">{String(realtimeQuotes.quote_only)}</div>
            </div>
            <div className="api-status-card">
              <div className="meta-label">trade_enabled</div>
              <div className="meta-value">{String(realtimeQuotes.trade_enabled)}</div>
            </div>
            <div className="api-status-card">
              <div className="meta-label">交易边界</div>
              <div className="meta-value">不接交易 / 不读资产持仓订单</div>
            </div>
            <div className="api-status-card">
              <div className="meta-label">Token 管理</div>
              <div className="meta-value">SDK 托管 token，前端不显示 token</div>
            </div>
          </div>
        </section>

        <section className="quote-table-card" style={{ marginBottom: '20px' }}>
          <div className="section-heading" style={{ marginBottom: '12px' }}>Longbridge 实时行情卡片</div>
          {realtimeQuotes.message ? (
            <div className="quote-disclaimer" style={{ marginBottom: '14px' }}>
              {realtimeQuotes.message}
            </div>
          ) : null}
          <div className="api-status-grid">
            {quoteItems.length === 0 ? (
              <div className="api-status-card">
                <div className="meta-label">状态</div>
                <div className="meta-value">暂无快照数据</div>
              </div>
            ) : quoteItems.map((item) => (
              <div key={`${item.market}-${item.symbol}`} className="api-status-card">
                <div className="meta-row" style={{ paddingTop: 0 }}>
                  <span className="meta-label">{item.name || item.symbol}</span>
                  <span className={`status-pill ${getQuoteStatusClass(item.data_status)}`}>
                    {getQuoteStatusLabel(item.data_status)}
                  </span>
                </div>
                <div className="meta-row">
                  <span className="meta-label">股票代码</span>
                  <span className="meta-value">{item.symbol || '-'}</span>
                </div>
                <div className="meta-row">
                  <span className="meta-label">Longbridge代码</span>
                  <span className="meta-value">{item.longbridge_symbol || '-'}</span>
                </div>
                <div className="meta-row">
                  <span className="meta-label">市场</span>
                  <span className="meta-value">{item.market || '-'}</span>
                </div>
                <div className="meta-row">
                  <span className="meta-label">当前价</span>
                  <span className="meta-value">{formatValue(item.price)}</span>
                </div>
                <div className="meta-row">
                  <span className="meta-label">涨跌额</span>
                  <span className="meta-value">{formatSignedValue(item.change)}</span>
                </div>
                <div className="meta-row">
                  <span className="meta-label">涨跌幅</span>
                  <span className="meta-value">{formatSignedValue(item.change_percent, '%')}</span>
                </div>
                <div className="meta-row">
                  <span className="meta-label">更新时间</span>
                  <span className="meta-value">{item.quote_time || '-'}</span>
                </div>
                <div className="meta-row">
                  <span className="meta-label">Provider</span>
                  <span className="meta-value">{item.provider || '-'}</span>
                </div>
                <div className="meta-row">
                  <span className="meta-label">安全</span>
                  <span className="meta-value">
                    quote_only={String(item.quote_only)}, trade_enabled={String(item.trade_enabled)}
                  </span>
                </div>
                <div style={{ fontSize: '11px', color: 'var(--mac-text-secondary)', lineHeight: 1.6 }}>
                  {item.message || '手动刷新式实时快照展示'}
                </div>
              </div>
            ))}
          </div>
        </section>

        <section className="quote-table-card">
          <div className="section-heading" style={{ marginBottom: '12px' }}>Longbridge 行情明细</div>
          <table className="quote-table">
            <thead>
              <tr>
                <th>代码</th>
                <th>Longbridge代码</th>
                <th>名称</th>
                <th>市场</th>
                <th>最新价</th>
                <th>涨跌额</th>
                <th>涨跌幅</th>
                <th>成交量</th>
                <th>成交额</th>
                <th>更新时间</th>
                <th>状态</th>
              </tr>
            </thead>
            <tbody>
              {quoteItems.length === 0 ? (
                <tr>
                  <td colSpan="10" style={{ textAlign: 'center', color: 'var(--mac-text-secondary)' }}>
                    暂无 Longbridge 实时行情快照，请先运行 `python3 app.py longbridge-quote-snapshot`
                  </td>
                </tr>
              ) : quoteItems.map((item) => (
                <tr key={`${item.market}-${item.symbol}`} className="quote-row">
                  <td className="code">{item.symbol || '-'}</td>
                  <td className="code">{item.longbridge_symbol || '-'}</td>
                  <td style={{ fontWeight: '600' }}>{item.name || '-'}</td>
                  <td>{item.market || '-'}</td>
                  <td style={{ fontFamily: 'monospace', fontWeight: '600' }}>{formatValue(item.price)}</td>
                  <td>{formatSignedValue(item.change)}</td>
                  <td>{formatSignedValue(item.change_percent, '%')}</td>
                  <td>{formatValue(item.volume)}</td>
                  <td>{formatValue(item.turnover)}</td>
                  <td style={{ color: 'var(--mac-text-secondary)', fontSize: '11px' }}>{item.quote_time || '-'}</td>
                  <td>
                    <span className={`status-pill ${getQuoteStatusClass(item.data_status)}`} style={{ fontSize: '10px', padding: '2px 6px' }}>
                      {getQuoteStatusLabel(item.data_status)}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>

        <div className="brand-watermark">A股智研台 | Longbridge Quote Snapshot</div>
      </div>
    </div>
  );
};

export default RealtimeMarketView;
