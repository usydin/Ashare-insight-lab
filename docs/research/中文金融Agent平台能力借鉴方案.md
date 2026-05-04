# 中文金融 Agent 平台能力借鉴方案

基于对 TradingAgents-CN v1.0.1 版本的调研，为 A股智研台 (AShare Insight Lab) 提出以下能力增强建议。

## 1. 数据获取与治理增强

### 多级降级数据链 (Fallback Strategy)
- **借鉴**: TradingAgents-CN 在实时行情获取上实现了 `stock_bid_ask_em -> stock_zh_a_spot -> stock_zh_a_spot_em -> stock_zh_a_hist` 的降级链。
- **落地**: A股智研台应在 `data_sources/akshare_provider.py` 中增加类似的 Fallback 逻辑，当主接口受限时自动切换到备用接口。

### 统一 Provider 规范
- **借鉴**: 使用 canonical key 规范化不同数据源（AkShare/Tushare）的字段。
- **落地**: 在 Python Core 层建立标准的数据模型 (Pydantic)，确保无论底层数据源是谁，输出给 UI 的快照格式始终如一。

## 2. LLM 适配与智能体协同

### 模型能力自适应 (Model Capability)
- **借鉴**: 根据任务类型（如简单的文本提取 vs 复杂的深度财报分析）自动选择不同层级的模型。
- **落地**: 在 `app_core/ai_assistant` 中引入模型分级，默认配置中将 DeepSeek/Qwen 等高性能模型分配给深度分析任务，将轻量级模型分配给简单摘要任务。

### 角色化提示词管理
- **借鉴**: 明确 Analyst, Researcher, Risk Mgmt 等角色。
- **落地**: 将当前的 AI 分析逻辑重构为“角色包”，每个包包含针对特定金融场景优化的 Prompt Template。

## 3. 产品功能模块借鉴

### 报告导出中心 (Report Export)
- **借鉴**: 支持 Markdown、PDF、Word 多格式。
- **落地**: 增强当前的 `ReportCenterView.jsx`，提供一个“导出为 PDF”按钮，利用 Python 后端的 `reportlab` 或 `pandoc` 工具链生成精美文档。

### 风险教育与合规墙 (Compliance)
- **借鉴**: 专门的“学习中心”和启动时的免责声明。
- **落地**: 在 A股智研台设置页面增加“投资风险教育”模块，在 Dashboard 显著位置标注“仅供学习研究，不构成投资建议”。

### 任务队列可视化
- **借鉴**: 使用 SSE/WebSocket 展示详细的 Agent 运行步骤。
- **落地**: 在 `ContextPanel` 中增加一个“详细运行日志”折叠框，展示 Agent 正在调用的工具名、思考状态等。

## 4. 部署与环境优化

### 多架构支持
- **借鉴**: 对 ARM64 (M1/M2 Mac) 的深度支持。
- **落地**: 持续优化 `packaging/macos/build_macos.sh`，确保在不同架构的 Mac 上均能流畅运行。

## 5. 结论
TradingAgents-CN 展示了一个成熟的中文金融 Agent Web 终端应具备的深度。A股智研台应保持目前的“桌面原生终端”定位，但在数据可靠性、模型适配灵活性和研报专业度上积极吸收其先进经验。
