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

启动 OAuthBuilder 授权研究流程：

```bash
python3 app.py longbridge-oauth-start
```

执行只读行情验证：

```bash
python3 app.py longbridge-oauth-quote --symbol 600519 --market CN
```

## 授权流程

1. 终端运行 `longbridge-oauth-start`
2. 终端打印授权 URL
3. 在浏览器打开该 URL
4. 登录并完成授权
5. 返回终端查看授权结果
6. 如 SDK 支持缓存，将记录为 `sdk_token_cache: maybe_configured`

## Token 安全

- 不提交 `.env`
- 不提交 `.secrets`
- 不截图或粘贴 token 到聊天窗口
- 如果 SDK 自身有缓存目录，也只作为本机缓存，不纳入 Git
- 本项目仅保存脱敏状态或非敏感 metadata，不主动复制完整 OAuth token

## 已知风险

- SDK 行为可能在后续版本变化
- OAuthBuilder 可能需要回调端口或额外交互
- A 股行情权限可能受账户自身行情权限影响
- 实测时 `00700.HK` / `AAPL.US` 可能比 A 股更容易先验证

## 禁止事项

- 禁止接入 TradeContext
- 禁止读取资产 / 持仓 / 订单
- 禁止下单 / 撤单
