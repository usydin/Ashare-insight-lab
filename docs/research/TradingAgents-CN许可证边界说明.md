# TradingAgents-CN 许可证边界说明

## 1. 许可证类型清点
根据 TradingAgents-CN 官方声明（v1.0.1 版本），该项目采用**混合许可证 (Mixed License)** 模式。

| 组成部分 | 许可证类型 | 权限说明 |
| :--- | :--- | :--- |
| **开源部分** | Apache 2.0 | 包含根目录下除 `app/` 和 `frontend/` 外的所有文件（如 `tradingagents/` 核心逻辑、`docs/`、`scripts/` 等）。 |
| **专有部分** | **专有许可证 (Proprietary)** | 包含 `app/` (FastAPI 后端) 和 `frontend/` (Vue 前端) 目录。 |

## 2. A股智研台 (AShare Insight Lab) 的合规原则

### 源码引用禁令
- **绝对禁止**: 严禁将 TradingAgents-CN 的 `app/` 或 `frontend/` 目录下的任何代码片段、组件或逻辑实现直接复制到 A股智研台。
- **原因**: 这部分代码受专有许可证保护，商业使用（或包含在 A股智研台项目中）必须获得原作者商业授权。

### 架构与设计学习
- **允许范围**: 学习其公开的架构图、技术选型方案（如 FastAPI + Vue 3）、数据流向设计。
- **允许范围**: 阅读其公开的 `docs/` 文档，理解多智能体协同原理、LLM 适配层抽象思路。

### Apache 2.0 部分引用规则
若未来 A股智研台需要引用其 `tradingagents/` 核心层代码（属于 Apache 2.0 授权范围）：
1. **保留声明**: 必须保留原始代码中的版权声明、LICENSE 文件。
2. **NOTICE 文件**: 若原项目有 NOTICE 文件，必须包含在引用方的项目中。
3. **显著变更说明**: 必须在修改过的文件中附带显著的变更说明。

## 3. 商业授权边界
- **个人研究**: 在本地运行 TradingAgents-CN 源码进行研究是允许的。
- **商业授权**: 任何基于 TradingAgents-CN 的商业产品化行为，必须联系原作者（[hsliup@163.com](mailto:hsliup@163.com)）获取授权。

## 4. 总结
A股智研台目前的开发路线（React + Tauri + Python）是完全独立的实现。我们对 TradingAgents-CN 的研究应仅限于“架构思路借鉴”和“能力范围对标”，确保代码实现层面完全自研或基于纯开源许可代码。
