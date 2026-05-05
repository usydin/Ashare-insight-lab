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

## 真实授权失败记录：internal_server_error

- 日期：2026-05-05
- 环境：macOS arm64
- Python：3.12.13
- SDK：longbridge 4.0.5
- SDK 状态：Config / QuoteContext / OAuthBuilder 均可用
- TradeContext：未导入、未调用
- 现象：OAuthBuilder 能生成授权 URL，浏览器授权页返回 `Authorization Failed / internal_server_error`
- 本地 OAuth token 文件：未生成
- `.secrets/longbridge_oauth_token.json`：不存在
- Git 状态：clean
- 安全扫描：无输出
- 结论：失败发生在授权服务端 / OAuth client 配置 / redirect_uri / 账号权限侧，尚未进入 QuoteContext 行情请求阶段
- 后续建议：联系 Longbridge OpenAPI 支持，或检查开发者后台 OAuth 配置、redirect_uri 和账号权限

## 禁止事项

- 禁止接入 TradeContext
- 禁止读取资产 / 持仓 / 订单
- 禁止下单 / 撤单
