import React, { useState, useEffect } from 'react';
import Sidebar from './components/Sidebar';
import TopBar from './components/TopBar';
import DashboardView from './components/DashboardView';
import ReportCenterView from './components/ReportCenterView';
import SettingsView from './components/SettingsView';
import PlaceholderView from './components/PlaceholderView';
import MarketIndexView from './components/MarketIndexView';
import SectorBoardView from './components/SectorBoardView';
import WatchlistView from './components/WatchlistView';
import HistoryView from './components/HistoryView';
import SearchView from './components/SearchView';
import ReviewQueuePanel from './components/ReviewQueuePanel';
import DataHealthPanel from './components/DataHealthPanel';
import SplashScreen from './components/SplashScreen';
import snapshotData from './data/snapshot.json';
import './styles.css';

function App() {
  const [activeView, setActiveView] = useState('dashboard');
  const [data, setData] = useState(null);
  const [showSplash, setShowSplash] = useState(true);
  const [isFadingOut, setIsFadingOut] = useState(false);

  useEffect(() => {
    // In this sandbox, we import the JSON directly
    setData(snapshotData);

    // Splash screen timing logic
    const fadeTimer = setTimeout(() => {
      setIsFadingOut(true);
    }, 1600); // 1.6s before start fading

    const hideTimer = setTimeout(() => {
      setShowSplash(false);
    }, 2100); // 1.6s + 0.5s transition

    return () => {
      clearTimeout(fadeTimer);
      clearTimeout(hideTimer);
    };
  }, []);

  const renderView = () => {
    if (!data) return (
      <div className="empty-state">
        <span className="empty-state-icon">🔄</span>
        正在载入快照数据...
      </div>
    );

    switch (activeView) {
      case 'dashboard':
        return <DashboardView data={data} />;
      case 'market_indices':
        return <MarketIndexView data={data} />;
      case 'sector_boards':
        return <SectorBoardView data={data} />;
      case 'watchlist':
        return <WatchlistView data={data} />;
      case 'history':
        return <HistoryView data={data} />;
      case 'search':
        return <SearchView data={data} />;
      case 'reports':
        return <ReportCenterView data={data} />;
      case 'settings':
        return <SettingsView data={data} />;
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

  const getContextDesc = () => {
    const descs = {
      dashboard: '核心市场指标与系统运行状态概览。',
      market_indices: '监控 A 股核心宽基指数的趋势与信号。',
      sector_boards: '行业板块强弱监控与异动发现。',
      watchlist: '核心自选个股的 MA 策略信号跟踪。',
      search: '快照内资产、路径与消息的全局检索。',
      history: '系统运行与快照生成的关键时间轴记录。',
      reports: '自动化分析报告与数据产物矩阵索引。',
      settings: '控制数据同步频率、环境配置与路径。'
    };
    return descs[activeView] || '';
  };

  return (
    <>
      {showSplash && <SplashScreen isFadingOut={isFadingOut} />}
      <div className={`app-shell ${!showSplash ? 'ready' : ''}`}>
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
            status={data?.latest_run?.status}
            healthStatus={data?.dashboard_summary?.data_health?.risk_item_count > 0 ? 'Risk' : 'OK'}
          />
          {renderView()}
        </main>

        <aside className="context-panel">
          <section className="context-card animate-in">
            <div className="section-heading">📍 页面上下文</div>
            <div className="sidebar-item-meta" style={{ fontSize: '12px', opacity: 1, color: 'var(--mac-text-primary)', marginBottom: '8px' }}>
              {getTitle()}
            </div>
            <p style={{ fontSize: '11px', color: 'var(--mac-text-secondary)', margin: 0, lineHeight: 1.5 }}>
              {getContextDesc()}
            </p>
          </section>

          <section className="context-card animate-in" style={{ animationDelay: '0.1s' }}>
            <div className="section-heading">🕒 快照状态</div>
            <div className="meta-row">
              <span className="meta-label">生成时间</span>
              <span className="meta-value" style={{ fontSize: '11px' }}>{data?.generated_at?.split('T')[1] || '待同步'}</span>
            </div>
            <div className="meta-row">
              <span className="meta-label">运行日期</span>
              <span className="meta-value">{data?.latest_run?.run_date || '未运行'}</span>
            </div>
            <div className="meta-row">
              <span className="meta-label">运行结论</span>
              <span className={`status-pill ${data?.latest_run?.status || 'unknown'}`}>{data?.latest_run?.status || 'Unknown'}</span>
            </div>
          </section>

          <ReviewQueuePanel items={data?.review_queue?.items} />
          
          <section className="context-card animate-in" style={{ animationDelay: '0.2s' }}>
            <div className="section-heading">🤖 AI 辅助</div>
            <div className="empty-state" style={{ padding: '20px', fontSize: '11px', borderStyle: 'solid', background: 'transparent' }}>
              AI 摘要模块正在开发中。当前仅显示结构化快照。
            </div>
          </section>
        </aside>
      </div>
    </>
  );
}

export default App;
