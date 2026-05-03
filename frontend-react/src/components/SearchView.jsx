import React, { useState, useMemo } from 'react';

const SearchView = ({ data }) => {
  const [query, setQuery] = useState('');

  const searchResults = useMemo(() => {
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
            category: item.asset_type
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
            category: item.asset_type
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
            category: 'system'
          });
        }
      });
    }

    // 4. Search in messages
    if (data.messages) {
      data.messages.forEach(msg => {
        if (msg.toLowerCase().includes(lowerQuery)) {
          results.push({
            type: '系统消息',
            title: 'System Message',
            symbol: '',
            status: 'Info',
            desc: msg,
            category: 'message'
          });
        }
      });
    }

    return results;
  }, [data, query]);

  return (
    <div className="view-container active">
      <section className="animate-in">
        <div style={{ marginBottom: '24px' }}>
          <div style={{ position: 'relative' }}>
            <span style={{ position: 'absolute', left: '12px', top: '50%', transform: 'translateY(-50%)', color: 'var(--mac-text-secondary)', fontSize: '18px' }}>🔍</span>
            <input
              type="text"
              placeholder="搜索资产、代码、路径或系统消息..."
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              style={{
                width: '100%',
                padding: '12px 12px 12px 40px',
                fontSize: '15px',
                borderRadius: 'var(--mac-radius-md)',
                border: '1px solid var(--mac-border)',
                outline: 'none',
                background: 'rgba(255, 255, 255, 0.8)',
                backdropFilter: 'blur(10px)',
                boxShadow: '0 2px 8px rgba(0,0,0,0.05)'
              }}
            />
          </div>
        </div>
      </section>

      <section className="panel-section animate-in" style={{ animationDelay: '0.1s' }}>
        <div className="panel-title">检索结果 ({searchResults.length})</div>
        <div className="tab-content" style={{ background: 'transparent', border: 'none' }}>
          {!query.trim() ? (
            <div className="empty-state" style={{ padding: '80px 20px' }}>
              <div style={{ fontSize: '48px', marginBottom: '16px' }}>🔎</div>
              <p>输入关键词以搜索当前快照数据</p>
            </div>
          ) : searchResults.length > 0 ? (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
              {searchResults.map((result, idx) => (
                <div className="review-item animate-in" key={idx} style={{ animationDelay: `${idx * 0.05}s`, margin: 0 }}>
                  <div className="review-item-header">
                    <div className="item-name-group">
                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                        <span style={{ fontSize: '10px', fontWeight: 700, padding: '2px 6px', borderRadius: '4px', background: 'rgba(0,0,0,0.05)', color: 'var(--mac-text-secondary)' }}>
                          {result.type}
                        </span>
                        <span className="item-name">{result.title}</span>
                        {result.symbol && <span className="item-symbol">{result.symbol}</span>}
                      </div>
                    </div>
                    <div className="item-tags">
                      <span className={`sig-badge sig-${result.status?.includes('trend_up') ? 'bullish' : (result.status?.includes('trend_down') ? 'bearish' : 'neutral')}`}>
                        {result.status}
                      </span>
                    </div>
                  </div>
                  <div className="item-reason" style={{ marginTop: '8px', wordBreak: 'break-all' }}>
                    {result.desc}
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <div className="empty-state" style={{ padding: '80px 20px' }}>
              <div style={{ fontSize: '48px', marginBottom: '16px' }}>📭</div>
              <p>当前快照未匹配到相关内容</p>
            </div>
          )}
        </div>
      </section>
    </div>
  );
};

export default SearchView;
