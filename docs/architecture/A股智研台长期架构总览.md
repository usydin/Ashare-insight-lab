# A股智研台长期架构总览

## 文档定位

本文档用于把 TradingAgents、FinceptTerminal、MiroFish 三个研究对象的结论，正式收敛为 A股智研台自己的长期架构总览。

当前阶段只做架构规划，不落地新增功能代码。

## A股智研台长期定位

A股智研台的长期目标，不是一个零散脚本集合，而是一个本地化、可持续演进的 A 股智能投研终端。

其长期定位包括：

- 本地 A股智能投研终端
- 中文投研报告
- 本地模拟盘
- 多 Agent 研究
- 数据源健康检查
- 情景推演
- 未来轻量 GUI 工作台
- OpenClaw 调度层

## 总体架构分层

从长期看，A股智研台可分为以下层级：

### 1. DataHub 数据底座

- 负责统一数据入口、缓存、标准化和数据路由
- 向上为策略、报告、Agent、Scenario Lab 提供统一数据供应

### 2. Data Source Health 数据源健康检查

- 负责 `doctor` / `check-data-source`
- 检查网络、依赖、代理、目标站点可用性与采集状态

### 3. Strategy Signals 策略信号层

- 负责结构化技术信号与基础观察结果
- 当前 `run-daily` 已具备这一层的基础形态

### 4. Report Center 报告中心

- 负责日报、周报、复盘报告的生成、归档与阅读
- 是 CLI 阶段和未来 GUI 阶段的共同输出中心

### 5. Paper Trading 模拟盘账本

- 负责本地模拟盘记录、收益跟踪、回撤分析与复盘
- 只做本地模拟，不接真实券商

### 6. Risk Center 风控中心

- 负责风险提示、异常暴露、组合集中度与研究建议审查
- 长期作为策略层、模拟盘层和 Agent 层的共同约束

### 7. Agent Research AI 投研层

- 负责多角色研究、结构化解释、多空辩论和建议汇总
- 吸收 TradingAgents 的角色分层与研究流程思想

### 8. Scenario Lab 情景推演室

- 负责事件冲击、叙事传播、政策影响与情景推演
- 吸收 MiroFish 的多阶段推演与多角色社会模拟思想

### 9. Decision Memory 决策记忆与复盘

- 负责保存研究建议、模拟盘结果、复盘总结和经验迁移
- 长期连接报告、Agent、模拟盘与风险审查

### 10. OpenClaw Scheduler 调度层

- 负责调度、汇总、提醒、监控与交互
- 不负责交易执行，不替代 Python 核心

### 11. GUI Terminal 未来终端工作台

- 负责未来的本地终端化展示
- 把 DataHub、报告、风控、Agent、Scenario Lab 组织成统一工作台

## 三个开源项目的借鉴位置

### TradingAgents 启发 Agent Research

借鉴重点：

- 多角色研究分工
- 多空辩论
- 风控审查
- 结构化输出
- 决策记忆思路

### FinceptTerminal 启发 GUI Terminal / DataHub / 产品形态

借鉴重点：

- 终端化产品形态
- 工作台式模块组织
- DataHub 思路
- 页面层与服务层解耦
- 报告中心 / 风控中心 / 工作区等模块化设计

### MiroFish 启发 Scenario Lab

借鉴重点：

- 五阶段情景推演流程
- 事件种子输入
- 多角色社会模拟
- 三情景输出
- 传播路径与风险触发条件

## 当前 V0.1.x 已完成内容

当前 V0.1.x 已经完成的内容包括：

- `run-daily`
- `doctor` / `check-data-source`
- 项目元信息与版权统一管理
- TradingAgents / FinceptTerminal / MiroFish 开源金融项目研究

这些内容说明：

- A股智研台已经有了基础数据采集与报告骨架
- 已完成数据源健康检查能力
- 已完成长期架构灵感来源的研究收敛

## 未来 UI 与金融终端化技术路线

A股智研台最终的 UI 目标，是本地 A股智能投研终端，而不是普通脚本工具。

这一方向可以综合借鉴：

- TradingAgents 的多 Agent 流程展示思路
- FinceptTerminal 的金融终端产品形态
- MiroFish 的关系图谱和情景推演表现方式

但必须明确：

- 只借鉴产品思想和交互形态
- 不复制第三方源码
- 不复刻 FinceptTerminal 的 UI
- 不复刻其 trade dress
- 不复刻其 terminal command
- 不复刻其快捷键体系

推荐长期技术路线如下：

- Python Core
- PySide6 桌面壳
- Markdown / HTML 报告
- ECharts 金融图表
- Cytoscape.js 或类似图谱组件用于 Scenario Lab
- SQLite / DuckDB 作为本地数据底座
- OpenClaw 作为未来调度层

推荐 UI 阶段路线如下：

- V0.2-V0.3：继续 CLI + Markdown
- V0.4：增强 HTML 报告
- V0.5：轻量 GUI 原型
- V0.6：Agent 工作台
- V0.7：Scenario Lab 图谱推演
- V1.0：本地智能投研终端

当前阶段只写入架构文档，不实现 GUI 代码，不引入新依赖。

## 当前不落地内容

当前明确不落地：

- 不做实盘自动交易
- 不接券商
- 不复制第三方源码
- 不引入重依赖

并且当前仍不做：

- 不实现 GUI
- 不实现 OpenClaw
- 不实现 Scenario Lab 代码
- 不实现多 Agent 运行框架

## 当前结论

V0.1.7 的意义，是把三条研究线正式收敛为 A股智研台自己的长期架构。

后续进入 V0.2 时，项目将继续以数据源、日报、结构化输出和最小闭环迭代为主，而不是直接跳进终端、Agent 或情景推演实现。
