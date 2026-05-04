import React, { useState, useMemo } from 'react';

const SearchView = ({ data }) => {
  const [query, setQuery] = useState('');
  const [activeType, setActiveType] = useState('全部');
  const [copyStatus, setCopyStatus] = useState({});

  const filterTypes = ['全部', '关注项', '信号变化', '路径', '系统消息'];

  const handleCopy = (text, key) => {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(() => {
        setCopyStatus({ ...copyStatus, [key]: true });
        setTimeout(() => setCopyStatus({ ...copyStatus, [key]: false }), 2000);
      });
    }
  };

  const highlightText = (text, highlight) => {
    if (!highlight.trim()) return text;
    const parts = text.split(new RegExp(`(${highlight})`, 'gi'));
    return (
      <span>
        {parts.map((part, i) => 
          part.toLowerCase() === highlight.toLowerCase() ? (
            <mark key={i} className="highlight-mark">{part}</mark>
          ) : part
        )}
      </span>
    );
  };

  const allResults = useMemo(() => {
    if (!data || !query.trim()) return [];

    const lowerQuery = query.toLowerCase();
    const results = [];

    // 1. Search in review_queue.items
    if (data.review_queue?.items) {
      data.review_queue.items.forEach(item => {
        if (
          item.name?.toLowerCase().includes(lowerQuery) ||
          item.symbol?.toLowerCase().includes(lowerQuery) ||
          item.reason?.toLowerCase().includes(lowerQuery)
        ) {
          results.push({
            type: '关注项',
            title: item.name,
            symbol: item.symbol,
            status: item.latest_signal,
            desc: item.reason,
            category: item.asset_type,
            original: item.name
          });
        }
      });
    }

    // 2. Search in signal_changes.top_changes
    if (data.signal_changes?.top_changes) {
      data.signal_changes.top_changes.forEach(item => {
        if (
          item.name?.toLowerCase().includes(lowerQuery) ||
          item.symbol?.toLowerCase().includes(lowerQuery) ||
          item.change_type?.toLowerCase().includes(lowerQuery)
        ) {
          results.push({
            type: '信号变化',
            title: item.name,
            symbol: item.symbol,
            status: `${item.previous_signal} → ${item.latest_signal}`,
            desc: item.change_type,
            category: item.asset_type,
            original: item.name
          });
        }
      });
    }

    // 3. Search in paths
    if (data.paths) {
      Object.entries(data.paths).forEach(([key, path]) => {
        if (key.toLowerCase().includes(lowerQuery) || path.toLowerCase().includes(lowerQuery)) {
          results.push({
            type: '路径',
            title: key,
            symbol: '',
            status: 'Path',
            desc: path,
            category: 'system',
            original: key,
            path: path
          });
        }
      });
    }

    // 4. Search in messages
    if (data.messages) {
      data.messages.forEach((msg, idx) => {
        if (msg.toLowerCase().includes(lowerQuery)) {
          results.push({
            type: '系统消息',
            title: `System Message #${idx + 1}`,
            symbol: '',
            status: 'Info',
            desc: msg,
            category: 'message',
            original: msg
          });
        }
      });
    }

    return results;
  }, [data, query]);

  const filteredResults = useMemo(() => {
    if (activeType === '全部') return allResults;
    return allResults.filter(r => r.type === activeType);
  }, [allResults, activeType]);

  const typeCounts = useMemo(() => {
    const counts = { '全部': allResults.length };
    filterTypes.slice(1).forEach(type => {
      counts[type] = allResults.filter(r => r.type === type).length;
    });
    return counts;
  }, [allResults]);

  return (
    <div className="view-container active">
      <section className="animate-in">
        <div className="section-heading">全量搜索检索</div>
        <div className="section-subtitle">检索当前快照中的关注项、信号变化、产物路径与系统消息</div>
        
        <div style={{ marginBottom: '24px' }}>
          <div style={{ position: 'relative', marginBottom: '20px' }}>
            <span style={{ position: 'absolute', left: '12px', top: '50%', transform: 'translateY(-50%)', color: 'var(--mac-text-secondary)', fontSize: '18px' }}>🔍</span>
            <input
              type="text"
              placeholder="输入代码、行业、路径或关键词..."
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              style={{
                width: '100%',
                padding: '12px 12px 12px 40px',
                borderRadius: 'var(--mac-radius-md)',
                border: '1px solid var(--mac-border)',
                fontSize: '14px',
                outline: 'none',
                background: 'white',
                boxShadow: '0 2px 8px rgba(0,0,0,0.02)'
              }}
            />
          </div>

          {query.trim() && (
            <>
              <div className="filter-group">
                {filterTypes.map(type => (
                  <div
                    key={type}
                    className={`filter-chip ${activeType === type ? 'active' : ''}`}
                    onClick={() => setActiveType(type)}
                  >
                    {type} ({typeCounts[type]})
                  </div>
                ))}
              </div>

              <div className="search-summary-grid">
                <div className="search-summary-item">
                  <span>关键词:</span>
                  <span className="count">"{query}"</span>
                </div>
                <div className="search-summary-item">
                  <span>总命中:</span>
                  <span className="count">{allResults.length}</span>
                </div>
                {activeType !== '全部' && (
                  <div className="search-summary-item">
                    <span>当前类型:</span>
                    <span className="count">{filteredResults.length}</span>
                  </div>
                )}
              </div>
            </>
          )}
        </div>

        {!query.trim() ? (
          <div className="empty-state">
            <span className="empty-state-icon">🔦</span>
            <p>输入关键词以检索当前快照数据</p>
            <div style={{ fontSize: '11px', color: 'var(--mac-text-secondary)', maxWidth: '300px' }}>
              支持搜索资产名称、股票代码、行业板块、文件路径或系统运行消息。
            </div>
          </div>
        ) : filteredResults.length > 0 ? (
          <div className="search-results">
            {filteredResults.map((result, idx) => (
              <div key={idx} className="review-item" style={{ padding: '16px' }}>
                <div className="review-item-header">
                  <div className="item-name-group">
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <span className="item-name">{highlightText(result.title, query)}</span>
                      <span className="status-pill info" style={{ fontSize: '9px' }}>
                        {result.type}
                      </span>
                    </div>
                    {result.symbol && <span className="item-symbol">{highlightText(result.symbol, query)}</span>}
                  </div>
                  <div className="item-tags">
                    <span className={`sig-badge ${result.status.includes('trend_up') || result.status.includes('→ bullish') ? 'sig-bullish' : result.status.includes('trend_down') ? 'sig-bearish' : 'sig-neutral'}`}>
                      {result.status}
                    </span>
                  </div>
                </div>
                <div className="item-reason" style={{ marginTop: '8px' }}>
                  {highlightText(result.desc, query)}
                </div>
                {result.type === '路径' && result.path && (
                  <div style={{ marginTop: '12px', display: 'flex', justifyContent: 'flex-end' }}>
                    <button 
                      className={`copy-inline-button ${copyStatus[idx] ? 'success' : ''}`}
                      onClick={() => handleCopy(result.path, idx)}
                    >
                      {copyStatus[idx] ? '✅ 已复制' : '📋 复制路径'}
                    </button>
                  </div>
                )}
              </div>
            ))}
          </div>
        ) : (
          <div className="empty-state">
            <span className="empty-state-icon">📭</span>
            <p>当前快照未匹配到相关内容</p>
            <div style={{ fontSize: '11px', color: 'var(--mac-text-secondary)', maxWidth: '300px' }}>
              可尝试搜索：股票代码、行业名称、报告路径或信号关键词（如 trend_up）。
            </div>
          </div>
        )}
      </section>
    </div>
  );
};

export default SearchView;
