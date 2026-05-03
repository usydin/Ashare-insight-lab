import React from 'react';

const ReviewQueuePanel = ({ items }) => {
  return (
    <section className="panel-section">
      <div className="panel-title">🚩 今日关注 Top 5</div>
      <div id="reviewQueueList">
        {items && items.length > 0 ? (
          items.slice(0, 5).map((item, index) => (
            <div className="review-item animate-in" key={index} style={{ animationDelay: `${index * 0.05}s` }}>
              <div className="review-item-header">
                <div className="item-name-group">
                  <span className="item-name">{item.name}</span>
                  <span className="item-symbol">{item.symbol}</span>
                </div>
                <div className="item-tags">
                  <span className={`item-badge badge-${item.severity || 'medium'}`}>
                    {item.category || 'focus'}
                  </span>
                </div>
              </div>
              <div className="item-reason">{item.reason}</div>
            </div>
          ))
        ) : (
          <div className="empty-state">暂无队列数据</div>
        )}
      </div>
    </section>
  );
};

export default ReviewQueuePanel;
