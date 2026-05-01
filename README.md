# A股智研台 / AShare Insight Lab

## 项目定位

A股智研台是一个运行在 Mac 本地环境的 A 股智能投研与模拟盘平台，当前阶段聚焦研究、数据整理、策略信号、模拟盘记录与报告生成，不涉及任何实盘自动交易能力。

本项目当前作为开发骨架使用，目标是先建立清晰、可维护、可验证的目录结构、配置方式与文档体系，为后续 `run-daily` 和策略模块开发打基础。

当前 `run-daily` 已具备基础数据采集、均线信号、日报输出和失败不中断能力。
当前项目已加入统一项目元信息管理，开发者为 pL，版权品牌为 @B‘lock10STUdio。

## 当前阶段

- 阶段名称：`V0.1.2 项目元信息统一管理`
- 当前目标：统一管理项目名称、版本、开发者、版权信息与展示输出
- 当前边界：不实现模拟盘、不接入实盘交易、不引入自动下单能力

## 开发机与部署机分离方案

项目采用开发机与部署机分离思路：

- 开发机：当前 Mac mini，仅用于 Trae 开发、代码调试、GitHub 提交、文档维护、结构设计
- 部署机：未来独立 Mac mini，用于 24 小时运行、正式数据存储、Token 管理、模拟盘记录、报告输出

这样做的目的：

- 降低开发环境与运行环境相互影响
- 避免在开发机长期保存正式数据和敏感信息
- 方便后续将定时任务、日志和报告稳定迁移到部署机

## 安全边界

第一阶段明确遵守以下边界：

- 只做本地数据采集、策略信号、本地模拟盘、日报生成、复盘报告
- 不做实盘自动交易
- 不做自动下单
- 不模拟点击东方财富、同花顺、券商客户端
- 不绕过验证码、登录风控或平台限制
- 不抓包复刻交易接口

仓库安全约束：

- 不提交 `.env`
- 不提交 token、API key
- 不提交数据库文件
- 不提交日志文件
- 不提交真实原始数据、处理后数据和正式模拟盘记录

## 技术路线

当前技术路线保持轻量，优先保证可维护性：

- 语言：Python 3.12
- 底层核心：由 Python 平台实现数据采集、数据存储、策略信号、模拟盘、风控和报告
- 依赖管理：`requirements.txt`
- 配置管理：`config/settings.json`、`config/watchlist.json`
- 元信息管理：`app_core/project_info.py`
- 数据目录：`data/raw`、`data/processed`、`data/sim`
- 报告目录：`reports/daily`、`reports/weekly`
- 核心代码组织：`app_core/`
- AI 与自动化扩展：后续接入 OpenClaw，作为本地 AI Agent 与自动化调度层
- 启动方式：`python app.py`

本阶段不引入复杂框架，不做过度封装，以清晰目录和明确职责为主。

## OpenClaw 接入定位

OpenClaw 不是本项目的底层交易核心，也不负责替代 Python 平台内部的数据、策略或模拟盘能力。

本项目的底层核心由 Python 平台实现，负责以下基础能力：

- 数据采集
- 数据存储
- 策略信号
- 模拟盘
- 风控
- 报告

OpenClaw 的长期定位是后续接入的本地 AI Agent 与自动化调度层，建立在 Python 平台之上，主要承担以下职责：

- 定时触发数据采集任务
- 汇总 A 股、美股、港股和全球宏观信息
- 读取本地策略信号和模拟盘结果
- 生成盘前、盘后、周报和复盘摘要
- 对交易建议进行风险解释和反方审查
- 监控数据源异常、任务失败和模拟盘异常回撤
- 作为本地 AI 交互入口

因此，OpenClaw 更适合作为“调度、解释、汇总、监控、交互”层，而不是交易执行核心。

## 目录结构

```text
ashare-insight-lab/
├── app.py
├── README.md
├── requirements.txt
├── .env.example
├── config/
│   ├── settings.json
│   └── watchlist.json
├── app_core/
│   ├── __init__.py
│   ├── config_loader.py
│   ├── path_utils.py
│   ├── ai_assistant/
│   ├── data_sources/
│   ├── reports/
│   ├── scheduler/
│   ├── simulator/
│   ├── storage/
│   └── strategies/
├── docs/
│   ├── 项目说明.md
│   ├── 当前阶段进展.md
│   ├── 安全边界.md
│   ├── 开发计划.md
│   ├── 模拟盘规则.md
│   ├── 数据安全与账号隔离.md
│   ├── 开发机与部署机分离方案.md
│   ├── 部署说明.md
│   └── AI协作规则.md
├── data/
│   ├── raw/
│   ├── processed/
│   └── sim/
├── logs/
└── reports/
    ├── daily/
    └── weekly/
```

## 第一阶段目标

第一阶段聚焦以下五项：

1. 本地数据采集
2. 策略信号生成
3. 本地模拟盘记录
4. 日报生成
5. 复盘报告整理

阶段目标强调“研究与验证”，不强调“自动执行交易”。

## 运行方式

### 1. 准备环境

确保已经完成：

- Python 3.12 虚拟环境创建
- `requirements.txt` 安装完成
- VS Code 或 Trae 已指向 `.venv/bin/python`

如在普通终端中运行，建议先激活虚拟环境：

```bash
source .venv/bin/activate
```

### 2. 启动项目

在项目根目录执行：

```bash
python app.py
```

启动后将输出：

- 项目名称
- 英文名称
- 版本号
- 当前环境
- 项目根目录
- 当前时间
- 开发者
- 版权
- 仓库地址
- 安全提醒
- `V0.1.2 project metadata management is ready.`

### 3. 查看版本与项目信息

```bash
python app.py --version
python app.py about
```
### 4. 校验 JSON 配置

```bash
python -m json.tool config/settings.json
python -m json.tool config/watchlist.json
```

## 后续计划

后续按以下顺序推进：

1. 完善 `run-daily` 所需的日常执行链路设计
2. 接入本地数据采集与缓存机制
3. 建立基础策略信号模块
4. 完成模拟盘记账与风控约束
5. 生成日报与复盘报告
6. 规划 OpenClaw 接入方式，使其承担本地 AI 调度、摘要生成、风险解释和异常监控
7. 逐步为部署机准备独立运行方案

## 说明

- 当前分支：`main`
- 项目元信息、开发者信息和版权信息已统一管理
- 版权与项目信息见 `COPYRIGHT.md`、`NOTICE.md` 与 `docs/开发者与项目信息.md`
