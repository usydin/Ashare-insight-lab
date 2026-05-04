import React, { useState } from 'react';

const RealtimeMarketView = () => {
  const [selectedTicker, setSelectedTicker] = useState('600519.SH');
  const [period, setPeriod] = useState('daily');

  const mockData = [
    {
      ticker: '600519.SH',
      name: '贵州茅台',
      market: 'SH',
      price: '1650.00',
      change: '+15.50',
      pct: '+0.95%',
      volume: '35.2亿',
      time: '15:00:00',
      status: 'Mock',
      history: [1620, 1635, 1630, 1640, 1638, 1645, 1642, 1650, 1648, 1655, 1652, 1660, 1658, 1665, 1662, 1670, 1668, 1675, 1672, 1680]
    },
    {
      ticker: '300750.SZ',
      name: '宁德时代',
      market: 'SZ',
      price: '198.50',
      change: '-2.30',
      pct: '-1.15%',
      volume: '42.8亿',
      time: '15:00:00',
      status: 'Mock',
      history: [205, 203, 204, 202, 201, 199, 200, 198, 197, 199, 198, 196, 195, 197, 196, 194, 193, 195, 194, 192]
    },
    {
      ticker: '000001.SH',
      name: '上证指数',
      market: 'Index',
      price: '3050.25',
      change: '+12.45',
      pct: '+0.41%',
      volume: '3200亿',
      time: '15:00:00',
      status: 'Mock',
      history: [3020, 3025, 3022, 3030, 3028, 3035, 3032, 3040, 3038, 3045, 3042, 3050, 3048, 3055, 3052, 3060, 3058, 3065, 3062, 3070]
    },
    {
      ticker: 'AAPL.US',
      name: 'Apple',
      market: 'US',
      price: '185.92',
      change: '+1.24',
      pct: '+0.67%',
      volume: '5800万',
      time: '04:00:00',
      status: 'Mock',
      history: [180, 182, 181, 183, 182, 184, 183, 185, 184, 186, 185, 187, 186, 188, 187, 189, 188, 190, 189, 191]
    }
  ];

  const selectedData = mockData.find(d => d.ticker === selectedTicker) || mockData[0];

  const renderKLine = (history) => {
    const min = Math.min(...history);
    const max = Math.max(...history);
    const range = max - min;
    const padding = range * 0.1;
    
    const points = history.map((val, idx) => {
      const x = (idx / (history.length - 1)) * 100;
      const y = 100 - ((val - (min - padding)) / (range + 2 * padding)) * 100;
      return `${x},${y}`;
    }).join(' ');

    return (
      <svg className="mini-kline-svg" viewBox="0 0 100 100" preserveAspectRatio="none">
        <polyline
          fill="none"
          stroke={selectedData.pct.startsWith('+') ? '#ff3b30' : '#34c759'}
          strokeWidth="2"
          points={points}
        />
        {/* Simple grid lines */}
        <line x1="0" y1="25" x2="100" y2="25" stroke="rgba(255,255,255,0.1)" strokeWidth="0.5" />
        <line x1="0" y1="50" x2="100" y2="50" stroke="rgba(255,255,255,0.1)" strokeWidth="0.5" />
        <line x1="0" y1="75" x2="100" y2="75" stroke="rgba(255,255,255,0.1)" strokeWidth="0.5" />
      </svg>
    );
  };

  return (
    <div id="realtimeMarketView" className="view-container active">
      <div className="realtime-page animate-in">
        {/* 顶部标题与状态 */}
        <header className="page-header">
          <div>
            <div className="section-heading">实时行情</div>
            <div style={{ fontSize: '12px', color: 'var(--mac-text-secondary)', marginTop: '4px' }}>
              Realtime Market Watch / Quote & K-Line Preview
            </div>
          </div>
          <div className="realtime-status-grid">
            <div className="market-mode-pill">模式：前端原型 / Mock</div>
            <div className="market-mode-pill" style={{ background: 'rgba(0,0,0,0.05)', color: '#666' }}>后续：AkShare / Longbridge</div>
          </div>
        </header>

        {/* 顶部状态栏卡片 */}
        <section className="api-status-grid">
          <div className="api-status-card">
            <div className="meta-label">数据源方案</div>
            <div className="meta-value">AkShare (CN) / Longbridge (Global)</div>
          </div>
          <div className="api-status-card">
            <div className="meta-label">交易能力</div>
            <div className="meta-value">未接入 (仅观察模式)</div>
          </div>
          <div className="api-status-card">
            <div className="meta-label">更新频率</div>
            <div className="meta-value">Mock 每 3s (接入后为准)</div>
          </div>
          <div className="api-status-card">
            <div className="meta-label">安全提示</div>
            <div className="meta-value">仅用于数据展示，不构成投资建议</div>
          </div>
        </section>

        {/* 行情列表 */}
        <section className="quote-table-card">
          <table className="quote-table">
            <thead>
              <tr>
                <th>代码</th>
                <th>名称</th>
                <th>市场</th>
                <th>最新价</th>
                <th>涨跌额</th>
                <th>涨跌幅</th>
                <th>成交额</th>
                <th>更新时间</th>
                <th>状态</th>
              </tr>
            </thead>
            <tbody>
              {mockData.map((item) => (
                <tr 
                  key={item.ticker} 
                  className={`quote-row ${selectedTicker === item.ticker ? 'active' : ''}`}
                  onClick={() => setSelectedTicker(item.ticker)}
                >
                  <td className="code">{item.ticker}</td>
                  <td style={{ fontWeight: '600' }}>{item.name}</td>
                  <td>{item.market}</td>
                  <td style={{ fontFamily: 'monospace', fontWeight: '600' }}>{item.price}</td>
                  <td className={item.change.startsWith('+') ? 'quote-change-positive' : 'quote-change-negative'}>
                    {item.change}
                  </td>
                  <td className={item.pct.startsWith('+') ? 'quote-change-positive' : 'quote-change-negative'}>
                    {item.pct}
                  </td>
                  <td>{item.volume}</td>
                  <td style={{ color: 'var(--mac-text-secondary)', fontSize: '11px' }}>{item.time}</td>
                  <td>
                    <span className="status-pill synced" style={{ fontSize: '10px', padding: '2px 6px' }}>{item.status}</span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>

        {/* K线详情区 */}
        <section className="kline-layout">
          <div className="kline-preview-card">
            <div className="kline-header">
              <div className="kline-main-info">
                <div style={{ fontSize: '20px', fontWeight: '600' }}>{selectedData.name} ({selectedData.ticker})</div>
                <div className="kline-price">{selectedData.price}</div>
                <div className={selectedData.pct.startsWith('+') ? 'quote-change-positive' : 'quote-change-negative'} style={{ fontSize: '18px', fontWeight: '600' }}>
                  {selectedData.pct}
                </div>
              </div>
              <div className="period-switcher">
                {['日K', '60分', '30分', '15分'].map(p => (
                  <button 
                    key={p} 
                    className={`period-btn ${period === p ? 'active' : ''}`}
                    onClick={() => setPeriod(p)}
                  >
                    {p}
                  </button>
                ))}
              </div>
            </div>

            <div style={{ height: '240px', position: 'relative' }}>
              {renderKLine(selectedData.history)}
              <div style={{ position: 'absolute', top: 0, right: 0, fontSize: '10px', color: 'rgba(255,255,255,0.3)' }}>
                {selectedTicker} 20-Point Trend (Mock)
              </div>
            </div>

            <div className="api-status-grid" style={{ marginTop: '20px', background: 'transparent' }}>
              <div className="api-status-card" style={{ background: 'rgba(255,255,255,0.05)', border: '1px solid rgba(255,255,255,0.1)' }}>
                <div className="meta-label" style={{ color: '#aaa' }}>今日最高</div>
                <div className="meta-value" style={{ color: '#fff' }}>{selectedData.history[selectedData.history.length-1] * 1.02}</div>
              </div>
              <div className="api-status-card" style={{ background: 'rgba(255,255,255,0.05)', border: '1px solid rgba(255,255,255,0.1)' }}>
                <div className="meta-label" style={{ color: '#aaa' }}>今日最低</div>
                <div className="meta-value" style={{ color: '#fff' }}>{selectedData.history[selectedData.history.length-1] * 0.98}</div>
              </div>
              <div className="api-status-card" style={{ background: 'rgba(255,255,255,0.05)', border: '1px solid rgba(255,255,255,0.1)' }}>
                <div className="meta-label" style={{ color: '#aaa' }}>数据状态</div>
                <div className="meta-value" style={{ color: 'var(--mac-warning)' }}>Mock / 待接入</div>
              </div>
            </div>

            <div className="quote-disclaimer">
              ⚠️ 当前为前端展示原型，仅展示 UI 布局与 K线预览能力，数据为随机生成的 Mock 内容，不构成实时行情或投资建议。
            </div>
          </div>
        </section>

        <div className="brand-watermark">A股智研台 | Realtime Market Prototype</div>
      </div>
    </div>
  );
};

export default RealtimeMarketView;
