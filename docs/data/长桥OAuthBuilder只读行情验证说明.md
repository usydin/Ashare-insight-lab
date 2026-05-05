# 长桥 OAuthBuilder 只读行情验证说明

## 官方 SDK 示例摘要

Longbridge Python SDK 官方只读行情授权示例核心链路如下：

```python
from longbridge.openapi import Config, QuoteContext, OAuthBuilder

oauth = OAuthBuilder("your-client-id").build(
    lambda url: print(f"Open this URL to authorize: {url}")
)
config = Config.from_oauth(oauth)
ctx = QuoteContext(config)
resp = ctx.quote(["700.HK", "AAPL.US"])
```

本项目仅研究并接入 `OAuthBuilder`、`Config.from_oauth`、`QuoteContext`。

## 只读边界

- 仅验证只读行情。
- 不接交易能力。
- 不读取资产、持仓、订单。
- 不下单、不撤单、不改单。

## 安装要求

需要本机安装 Longbridge Python SDK：

```bash
pip install longbridge
```

本轮不自动安装依赖，若本机未安装，CLI 会友好返回 `sdk_missing`。

## 命令说明

查看 SDK 探测状态：

```bash
python3 app.py longbridge-sdk-status
```

查看 OAuthBuilder 帮助：

```bash
python3 app.py longbridge-oauth-help
```

启动 OAuthBuilder 授权研究流程（自动打开浏览器，不打印完整 URL）：

```bash
python3 app.py longbridge-oauth-start
```

执行只读行情验证（建议先验证 US / HK）：

```bash
python3 app.py longbridge-oauth-quote --symbol AAPL --market US
python3 app.py longbridge-oauth-quote --symbol 700  --market HK
# 如需 A 股，再评估账号行情权限后执行：
# python3 app.py longbridge-oauth-quote --symbol 600519 --market CN
```

## 授权流程

1. 终端运行 `longbridge-oauth-start`
2. 系统自动打开默认浏览器到授权页
3. 登录并完成授权
4. 返回终端查看授权结果（不展示完整 URL 或敏感参数）
5. 如 SDK 支持缓存，将记录为 `sdk_token_cache: maybe_configured`

## Token 安全

- 不提交 `.env`
- 不提交 `.secrets`
- 不截图或粘贴 token 到聊天窗口
- 如果 SDK 自身有缓存目录，也只作为本机缓存，不纳入 Git
- 本项目仅保存脱敏状态或非敏感 metadata，不主动复制完整 OAuth token
- 不要保存或提交注册接口返回的 access token

## 已知风险

- SDK 行为可能在后续版本变化
- OAuthBuilder 可能需要回调端口或额外交互
- A 股行情权限可能受账户自身行情权限影响
- 实测时 `00700.HK` / `AAPL.US` 可能比 A 股更容易先验证

## 授权进展与历史问题

- 日期：2026-05-05
- 环境：macOS arm64
- Python：3.12.13
- SDK：longbridge 4.0.5
- SDK 状态：Config / QuoteContext / OAuthBuilder 均可用
- TradeContext：未导入、未调用
进展更新：

- 当前授权已成功，浏览器显示 “Authorization Successful! You can close this window and return to the terminal.”
- 根因：过去误用 App Key 作为 OAuth client_id，已改为使用独立 `LONGBRIDGE_OAUTH_CLIENT_ID`。
- SDK token cache 由 Longbridge SDK 托管，本项目仅记录脱敏 metadata 与状态，不读取或复制完整 token。

## 当前阶段补充说明

- 已确认：App Key 不能作为 OAuth client_id 使用；需通过 `/oauth2/register` 单独注册 OAuth Client 并登记 redirect_uri。
- 本项目 redirect_uri: `http://localhost:60355/callback`
- `.env` 仅在本机保存 `LONGBRIDGE_OAUTH_CLIENT_ID`；不提交 Git。
- 下一步：优先验证 US/HK 只读行情（AAPL.US / 700.HK），A 股根据账号行情权限再评估。

## 禁止事项

- 禁止接入 TradeContext
- 禁止读取资产 / 持仓 / 订单
- 禁止下单 / 撤单
