# TradingAgents-CN 技术栈学习笔记

## 1. 项目整体定位
TradingAgents-CN 是一个面向中文用户的**多智能体与大模型股票分析学习平台**。它专注于合规的股票研究与策略实验，提供中文化学习中心与工具，支持 A股/港股/美股 的分析与教学。其核心价值在于将复杂的 AI 多智能体框架（基于原版 TradingAgents）转化为易于中文用户部署和使用的 Web 终端。

## 2. 核心技术栈清点

### 后端架构 (FastAPI)
- **框架**: FastAPI + Uvicorn，提供高性能异步 RESTful API。
- **任务处理**: 采用异步任务模型（基于 Python `asyncio`），支持 SSE (Server-Sent Events) 和 WebSocket 双通道推送进度。
- **配置管理**: 实现了统一配置桥接（Config Bridge），支持 `.env`、YAML 和数据库配置的多级覆盖与热加载。

### 前端架构 (Vue 3)
- **框架**: Vue 3 + Vite + Element Plus。
- **状态管理**: Pinia (根据目录结构 `frontend/src/stores` 推断)。
- **交互模式**: 现代化的单页应用 (SPA)，提供可视化的大模型配置、数据源管理和系统设置界面。

### 数据持久化与缓存
- **数据库**: MongoDB (主存储，存储股票基础信息、分析结果、用户信息等)。
- **缓存**: Redis (用于任务队列、进度跟踪和高性能数据缓存)。
- **多级缓存**: 支持 MongoDB/Redis/本地文件三级缓存策略，提升数据获取速度。

### 数据源适配 (Multi-Source)
- **数据提供商**: 深度集成 AkShare, Tushare, BaoStock。
- **海外市场**: 支持 yfinance, Finnhub。
- **适配器模式**: 实现了统一的数据供应商管理（Manager/Adapter 模式），支持数据降级（Fallback）逻辑。

### AI 智能体 (Agentic Core)
- **框架**: 基于 LangGraph 和 LangChain 构建多智能体图结构。
- **LLM 适配**: 支持多供应商 (OpenAI, Google AI, DeepSeek, DashScope, AiHubMix 等)。
- **角色划分**: 包含 Analyst (分析师), Researcher (研究员), Risk Manager (风控), Trader (交易员) 等角色，每个角色拥有独立的提示词模板和工具集。

## 3. 核心设计思路借鉴

### 多 LLM Provider 配置
- 实现了 `llm_clients` 抽象层，屏蔽了不同模型供应商的 API 差异。
- 支持动态添加供应商，并根据任务复杂度自动匹配最佳模型（Model Capability Management）。

### 报告导出体系
- 支持多种格式导出：Markdown, Word (docx), PDF。
- 采用模板驱动，将分析图表和 Agent 输出结果整合为专业研报。

### 学习中心与风险教育
- 内置专门的 Learning 页面，涵盖 AI 基础、提示词工程、风险与局限等教育内容。
- 体现了金融终端产品的合规性导向。

### Docker 部署与多架构支持
- 提供完善的 Docker Compose 配置，支持 amd64 和 arm64 (Apple Silicon) 架构。
- 采用多阶段构建（Multi-stage build）优化镜像体积。

## 4. 对 A股智研台的启发

A股智研台当前采用 **React + Tauri + Python Core** 路线，与 TradingAgents-CN 的 B/S 架构有所不同，但以下点具有高度借鉴价值：
- **数据供应商降级链**: 在 AkShare 接口失效时，自动尝试 Tushare 或本地缓存，提升系统鲁棒性。
- **Agent 角色化工具集**: 为 Python 核心逻辑层引入更明确的“角色”概念，不同任务调用不同的提示词包。
- **SSE/WebSocket 进度反馈**: 在 Tauri 界面中实现更细粒度的分析进度条。
- **报告模板化**: 借鉴其研报导出的排版与结构设计。

## 5. 边界与限制
- **不可复制**: 明确 `app/` (FastAPI 后端) 和 `frontend/` (Vue 前端) 为专有许可证代码，严禁源码复制。
- **可学习**: 学习其目录结构规范、多源数据对齐逻辑和 Agent 协同流程。
