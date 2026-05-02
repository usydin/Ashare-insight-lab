# FinceptTerminal 源码学习笔记

## 说明
- 本文档基于对 `FinceptTerminal` 扫描报告（`docs/research/FinceptTerminal_source_scan_20260502_223321.md`）的学习整理。
- FinceptTerminal 是第三方开源项目，不属于 A股智研台。
- 当前阶段只做架构学习，不复制其源码，不引入其依赖。

## 1. FinceptTerminal 项目定位
FinceptTerminal 是一个高性能、原生（C++20/Qt6）的金融智能终端平台。它的定位是“金融投研工作站”，强调：
- **原生性能**：拒绝 Electron/Web 方案，采用 C++ + Qt6 提供极速响应。
- **数据连接器体系**：拥有 100+ 数据连接器，通过 DataHub 统一管理。
- **AI 赋能**：内置 30+ 角色化 AI Agent，覆盖投研全流程。
- **模块化扩展**：屏幕（Screens）与服务（Services）高度解耦。

## 2. 顶层目录结构
从扫描报告看，其核心组织如下：
- `fincept-qt/src/`：主体源码目录。
  - `screens/`：UI 页面层，按功能分区。
  - `services/`：业务逻辑层，为页面提供数据支持。
  - `core/`：核心基础设施（日志、配置、网络等）。
  - `datahub/`：统一数据分发与接入中心。
  - `python/`：嵌入式 Python 运行环境。
- `fincept-qt/scripts/`：包含大量 Python 编写的数据采集、AI Agent 和量化模块。

## 3. fincept-qt/src/screens 的页面组织方式
FinceptTerminal 的 UI 不是一个整体，而是高度模块化的“工作台”集合：
- `dashboard`：运行概览。
- `watchlist`：自选股监控。
- `portfolio`：投资组合。
- `report_builder`：报告生成工具。
- `node_editor`：可视化自动化节点编辑器。
- `akshare`：专门的 A股数据展示页。
- `settings`：系统设置。
- **启发**：一个金融终端应由多个独立但互通的功能分区（Screens）组成，每个分区聚焦特定任务。

## 4. fincept-qt/src/services 的服务组织方式
Service 层作为 UI 和数据/逻辑之间的桥梁：
- `news`：新闻聚合服务。
- `markets`：行情数据服务。
- `agents`：AI 智能体服务。
- `data_normalization`：数据标准化服务。
- **启发**：UI 不直接请求 API，而是调用 Service，Service 负责处理并发、缓存和格式转换。

## 5. 模块启发
- `src/storage`：采用 SQLite 和缓存机制（Cache/Repositories），保证本地数据快速读取。
- `src/trading`：抽象出 Brokers 和 Exchanges 接口，便于扩展不同交易平台。
- `src/ui`：高度抽象的组件库（Charts, Tables, Widgets），保证全局视觉统一。
- `src/python`：将 Python 脚本能力作为“插件”或“计算引擎”嵌入原生应用。

## 6. scripts 模块组织方式
其 Python 脚本层非常庞大，分类清晰：
- `agents/`：按角色（Economic, Geopolitics, TraderInvestors）组织 Agent。
- `ai_quant_lab/`：基于 Qlib 的量化研究环境。
- `alpha_arena/`：Agent 竞技场/策略对比。
- `akshare_xxx.py`：针对 AKShare 不同接口（Stocks, Funds, Economics）的精细化封装。
- **启发**：将数据抓取、策略逻辑、AI 角色等变动频繁的内容放在脚本层，核心架构放在编译层。

## 7. 核心概念
- **DataHub**：数据中枢，解决“数据从哪来、怎么存、怎么给 UI 用”的痛点。
- **Workspace**：工作区概念，允许用户保存当前的布局、自选和分析状态。
- **Report Builder**：将分析结论转化为可分发的 Markdown/PDF 报告。
- **Node Editor**：可视化低代码方式编排投研流程。

## 8. 对 A股智研台的启发
- **模块化分区**：未来 UI 演进应遵循“功能分区”逻辑，如“日报中心”、“数据源中心”。
- **DataHub 思路**：目前 A股智研台已具备 Data Sources 雏形，未来应强化数据标准化和缓存层。
- **角色化 Agent**：借鉴其对 30+ 角色的精细定义，完善本项目的 Agent 路线图。
- **脚本/内核分离**：保持 A股智研台 Python 端的灵活性，未来如有 GUI，GUI 只负责展示。

## 9. 明确边界
- **仅学习架构**：本项目当前仅学习其目录组织、解耦思想和产品定义。
- **不复制源码**：严禁复制其 C++/Python 源码。
- **不复刻 UI**：不模仿其视觉风格、终端命令、快捷键及专有词汇。
