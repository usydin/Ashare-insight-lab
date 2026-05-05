<p align="center">
  <img src="asset/logo/banner1.png" alt="A股智研台 | AShare Insight Lab" width="960">
</p>

# A股智研台 / AShare Insight Lab

## 项目定位

A股智研台是一个运行在 macOS 本地环境的 A 股投研辅助平台，当前聚焦以下方向：

- 本地优先
- 只读行情
- 投研辅助
- 数据源状态透明
- 前后端快照驱动展示

当前项目不做自动交易，不接实盘交易，不提供任何交易执行能力。现阶段核心目标是把日常研究、数据采集、状态诊断、前端展示和文档沉淀做扎实，为后续产品化和桌面演示打基础。

## 当前阶段

- 阶段标签：`V1.0-alpha-stage-freeze-docs`
- 最新冻结能力基线：`V0.9.7 realtime source status and switch prototype`
- 最新已知稳定提交：`c4d1dc0 feat: add realtime source status and switch prototype`

当前阶段以“行情源状态控制台 + 本地 Token 管理 + Longbridge 只读接入准备 + React/Tauri 前端展示”为核心，功能上强调透明、安全、可验证，不追求重功能扩张。

## 当前能力概览

### 1. 日报与信号流程

- 支持 `run-daily` 生成本地研究数据、信号结果与日报输出。
- 支持历史查询、变化摘要、Dashboard 摘要、Review Queue 与 UI Snapshot。
- 支持 SQLite 本地数据资产沉淀。

### 2. 本地 SQLite 数据资产

- 已建立本地 SQLite 历史库与结构化快照能力。
- 已支持 `history`、`changes`、`dashboard-summary`、`review-queue`、`ui-snapshot`、`validate-snapshot`。
- 当前前端静态页面通过 `ui_snapshot` 与 `snapshot.json` 驱动展示。

### 3. 静态前端与 React / Tauri 前端

- 前端采用 `React + Vite`。
- 桌面端路线保持 `Tauri` 作为原生壳方向。
- 已完成 Dashboard、实时行情原型、设置页、品牌化界面与 snapshot 同步链路。

### 4. 实时行情与 K 线

- 已支持 AkShare A 股实时行情查询。
- 已支持 AkShare / 本地 Provider K 线能力。
- 已提供 `quote`、`quote-batch`、`kline` CLI。
- 已提供实时行情页的前端原型与数据源状态区。

### 5. 国际新闻

- 已接入 Marketaux 国际新闻源。
- 已支持 Token 状态检测与新闻 CLI。
- 国际新闻能力定位为投研辅助，不作为交易信号。

### 6. Token 本地管理

- 已支持 `.env` 自动加载。
- 已支持本地 Token 状态查看、设置、清空。
- 已支持 `.secrets` metadata 管理与脱敏显示。
- 所有 CLI 均只输出脱敏状态，不回显真实 token。

### 7. Longbridge 只读接入准备

- 已完成 Longbridge readonly adapter 基础层。
- 已支持 legacy API Key 状态识别。
- 已完成本地 OAuth token 准备层与 OAuthBuilder 研究命令。
- 已完成 `internal_server_error` 诊断输出增强。

### 8. 数据源状态控制台

- 已新增 `source-status` 多数据源状态摘要。
- 已将 `source_status` 纳入 `ui_snapshot`。
- RealtimeMarketView 已增加行情源状态与切换视觉原型。
- SettingsView 已区分 API Token 状态与数据源状态。

## 当前默认数据源

- `AkShare`：默认 A 股实时行情源
- `Marketaux`：国际新闻源
- `Longbridge`：候选只读行情源，当前 OAuth 阻塞
- `Tushare`：预留数据源

## CLI 命令总览

### 基础

```bash
python3 app.py doctor
python3 app.py run-daily
python3 app.py history
```

### 实时行情

```bash
python3 app.py quote --symbol 600519 --market CN
python3 app.py quote-batch --symbols 600519,300750,000001 --market CN
python3 app.py kline --symbol 600519 --market CN --period daily --adjust qfq --limit 20
python3 app.py source-status
```

### 新闻

```bash
python3 app.py marketaux-status
python3 app.py international-news --ticker AAPL --market US --hours 72 --limit 3
```

### Token

```bash
python3 app.py token-status
python3 app.py token-set --key MARKETAUX_API_TOKEN
python3 app.py token-clear --key MARKETAUX_API_TOKEN
```

### Longbridge

```bash
python3 app.py longbridge-status
python3 app.py longbridge-sdk-status
python3 app.py longbridge-quote --symbol 600519 --market CN
python3 app.py longbridge-oauth-status
python3 app.py longbridge-oauth-help
python3 app.py longbridge-oauth-start
python3 app.py longbridge-oauth-quote --symbol 600519 --market CN
python3 app.py longbridge-oauth-set
python3 app.py longbridge-oauth-clear
```

### UI

```bash
python3 app.py ui-snapshot
python3 app.py validate-snapshot
python3 app.py sync-frontend-snapshot
```

## 安全边界

项目当前明确遵守以下边界：

- 只读行情
- 不接交易
- 不导入 `TradeContext`
- 不读资产 / 持仓 / 订单
- 不下单 / 撤单 / 改单
- token 只保存在本地 `.env` / `.secrets`
- `.env` / `.secrets` / `data` / `logs` / `reports` / `dist` / `target` 禁止提交

仓库中所有 CLI、快照、前端 JSON 和文档只允许出现脱敏状态，不允许写入真实 token、完整 OAuth URL 或 App Secret。

## Longbridge 当前状态

当前 Longbridge OpenAPI 只作为候选只读行情源，不作为默认行情源：

- SDK `4.0.5` 已安装并可导入
- `Config` / `QuoteContext` / `OAuthBuilder` 可用
- `OAuthBuilder` 可生成授权 URL
- 浏览器授权页当前返回 `Authorization Failed / internal_server_error`
- 当前尚未获得 OAuth token
- 当前问题判断更接近 Longbridge OAuth 服务端、OAuth client 配置、`redirect_uri` 或账号权限侧问题
- 默认行情源仍为 `AkShare`

## 开发与验证命令

常用验证命令如下：

```bash
source .venv/bin/activate
python3 -m pytest
python3 app.py source-status
python3 app.py token-status
python3 app.py validate-snapshot
cd frontend-react && npm run build
```

前端本地开发命令：

```bash
cd frontend-react
npm run dev
```

## 目录结构

```text
ashare-insight-lab/
├── app.py
├── README.md
├── requirements.txt
├── .env.example
├── app_core/
├── config/
├── docs/
├── frontend-react/
├── data/
├── logs/
└── reports/
```

## 文档入口

建议从以下文档继续了解当前冻结状态：

- `docs/当前阶段进展.md`
- `docs/版本记录.md`
- `docs/data/实时行情源状态与切换说明.md`
- `docs/stage_freeze/V1.0-alpha-行情源控制台阶段冻结说明.md`
- `docs/demo/V1.0-alpha-演示操作说明.md`

## 后续路线

下一阶段建议按以下顺序推进：

1. 前端行情源切换交互增强
2. 联系 Longbridge OpenAPI 支持并完成 OAuth 复测
3. 数据源健康评分与状态排序
4. Tushare 接入评估
5. OpenAI Key 后续用于 AI 摘要 / 研报
6. Tauri 桌面演示包打包

## 说明

- 当前分支：`main`
- 开发者：`pL`
- 版权品牌：`@B‘lock10STUdio`
- 项目当前强调研究、验证、展示与安全边界，不提供自动交易能力
