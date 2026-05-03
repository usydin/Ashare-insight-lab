import React, { useState, useEffect } from 'react';
import Sidebar from './components/Sidebar';
import TopBar from './components/TopBar';
import DashboardView from './components/DashboardView';
import ReportCenterView from './components/ReportCenterView';
import SettingsView from './components/SettingsView';
import PlaceholderView from './components/PlaceholderView';
import ReviewQueuePanel from './components/ReviewQueuePanel';
import DataHealthPanel from './components/DataHealthPanel';
import snapshotData from './data/snapshot.json';
import './styles.css';

function App() {
  const [activeView, setActiveView] = useState('dashboard');
  const [data, setData] = useState(null);

  useEffect(() => {
    // In this sandbox, we import the JSON directly
    setData(snapshotData);
  }, []);

  const renderView = () => {
    if (!data) return <div className="empty-state">Loading...</div>;

    switch (activeView) {
      case 'dashboard':
        return <DashboardView data={data} />;
      case 'reports':
        return <ReportCenterView data={data} />;
      case 'settings':
        return <SettingsView data={data} />;
      case 'market_indices':
        return (
          <PlaceholderView 
            id="market_indices" 
            title="市场指数视图开发中" 
            icon="📈" 
            description="正在为您准备实时指数监控面板。" 
          />
        );
      case 'sector_boards':
        return (
          <PlaceholderView 
            id="sector_boards" 
            title="行业板块视图开发中" 
            icon="❖" 
            description="正在构建行业热点与板块轮动分析工具。" 
          />
        );
      case 'watchlist':
        return (
          <PlaceholderView 
            id="watchlist" 
            title="自选股工作台开发中" 
            icon="🎯" 
            description="个性化监控与信号预警中心即将上线。" 
          />
        );
      case 'search':
        return (
          <PlaceholderView 
            id="search" 
            title="全量搜索开发中" 
            icon="🔍" 
            description="支持代码、名称、拼音的全局快速定位。" 
          />
        );
      case 'history':
        return (
          <PlaceholderView 
            id="history" 
            title="运行历史开发中" 
            icon="🕒" 
            description="正在为您同步云端与本地的运行记录。" 
          />
        );
      case 'ai':
        return (
          <PlaceholderView 
            id="ai" 
            title="AI 投研室" 
            icon="🤖" 
            description="AI 智能分析模块后续接入。" 
            disclaimer="当前阶段 AI 仅用于辅助分析结构化快照，系统不生成任何投资建议或交易指令。所有分析结果仅供参考。"
          />
        );
      case 'scenario':
        return (
          <PlaceholderView 
            id="scenario" 
            title="情景推演室后续接入" 
            icon="🎭" 
            description="基于历史数据的策略复盘与推演工具。" 
            disclaimer="本功能仅用于研究和复盘，不具备实盘交易对接功能，不发送任何交易指令。"
            disclaimerColor="#004085"
            disclaimerBg="#eef4ff"
            disclaimerBorder="#d2e3ff"
          />
        );
      default:
        return <DashboardView data={data} />;
    }
  };

  const getTitle = () => {
    const titles = {
      dashboard: '总览面板',
      market_indices: '市场指数',
      sector_boards: '行业板块',
      watchlist: '监控自选',
      search: '全量搜索',
      history: '运行历史',
      reports: '日报中心',
      ai: 'AI 投研室',
      scenario: '情景推演',
      settings: '偏好设置'
    };
    return titles[activeView] || '总览面板';
  };

  return (
    <div className="app-container">
      <Sidebar 
        activeView={activeView} 
        onViewChange={setActiveView} 
        version={data?.app?.version} 
      />
      
      <main className="content">
        <TopBar 
          title={getTitle()} 
          snapshotAt={data?.generated_at} 
          runDate={data?.latest_run?.run_date} 
          healthStatus={data?.dashboard_summary?.data_health?.risk_item_count > 0 ? 'Risk' : 'OK'}
        />
        {renderView()}
      </main>

      <aside className="details-panel">
        <ReviewQueuePanel items={data?.review_queue?.items} />
        <DataHealthPanel health={data?.dashboard_summary?.data_health} />
        
        <section className="panel-section">
          <div className="panel-title">🤖 AI 投研摘要</div>
          <div className="empty-state" style={{ padding: '20px', fontSize: '11px' }}>
            AI 摘要模块正在开发中。当前显示结构化分析快照。
          </div>
        </section>
      </aside>
    </div>
  );
}

export default App;
