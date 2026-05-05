# 长桥 OAuth 只读行情接入准备说明

## 背景

在当前长桥后台配置中，`Access Token` 显示为 `--`，这意味着传统的 legacy 三件套模式无法完整成立。A股智研台需要为后续的 OAuth 2.0 只读行情接入预留本地安全存储、状态识别和 CLI 操作能力。

## Legacy API Key 与 OAuth 2.0

- `Legacy API Key` 模式依赖 `LONGBRIDGE_APP_KEY`、`LONGBRIDGE_APP_SECRET`、`LONGBRIDGE_ACCESS_TOKEN` 三项同时存在。
- `OAuth 2.0` 模式通常通过授权页、回调 `code exchange`、`refresh token` 等流程获取本地 token。
- 本项目当前阶段只实现 OAuth 准备层，不强行硬编码未知 SDK 细节。

## 本项目的安全边界

- 只读行情。
- 不接 `TradeContext`。
- 不读资产、不读持仓。
- 不下单、不撤单、不改单。
- 不将完整 token 写入 Git、日志、报告、快照或前端 JSON。

## 本地 Token 文件

OAuth token 本地文件路径：

```text
.secrets/longbridge_oauth_token.json
```

文件仅保存在本机，默认权限应为 `600`。CLI 与状态命令只能输出脱敏摘要。

## Git Ignore 规则

- `.env` 已加入 `.gitignore`
- `.secrets/` 已加入 `.gitignore`

因此本地凭证文件不应进入版本控制。

## CLI 使用说明

查看本地 OAuth 状态：

```bash
python3 app.py longbridge-oauth-status
```

查看 OAuth 接入帮助：

```bash
python3 app.py longbridge-oauth-help
```

手动保存本地 OAuth Token（开发临时工具）：

```bash
python3 app.py longbridge-oauth-set
```

清除本地 OAuth Token：

```bash
python3 app.py longbridge-oauth-clear
```

## 后续真实授权流程待办

- 研究 Longbridge 官方 `OAuthBuilder`
- 明确授权 URL 生成方式
- 设计 callback / code exchange 流程
- 增加 refresh token 刷新逻辑
- 在只读边界内接入 `QuoteContext`

## 禁止事项

- 不接 `TradeContext`
- 不读资产/持仓
- 不下单/撤单
- 不把完整 token 发到聊天窗口
- 不把 `.env`、`.secrets/` 或 token 文件提交到 Git
