# 长桥 OpenAPI OAuth 授权失败排查材料

## 一、问题摘要

A股智研台计划接入 Longbridge OpenAPI 作为只读行情源，仅使用 `QuoteContext`，不使用 `TradeContext`。

历史上卡在 `OAuthBuilder` 授权阶段：本地 CLI 可启动授权流程并生成授权 URL，但浏览器打开授权页后返回：

```text
Authorization Failed
Error: internal_server_error
```

进展更新：目前授权已成功（浏览器显示 Authorization Successful），系统可继续进入 `Config.from_oauth(oauth)` / `QuoteContext` 只读行情验证。

## 二、环境信息

- macOS arm64
- Python 3.12.13
- longbridge SDK 4.0.5
- SDK 可导入模块：
  - Config: yes
  - QuoteContext: yes
  - OAuthBuilder: yes
  - TradeContext: ignored / 未导入

## 三、当前凭证状态

以下内容仅为脱敏状态说明，不包含真实凭证值（当前沿用 SDK 托管 token cache，不复制完整 token）：

- App Key: present
- App Secret: present
- Legacy Access Token: missing / 后台显示 `--`
- Region: cn
- OAuth Client ID: present/missing（通过 /oauth2/register 单独注册）
- OAuth token file: missing
- `.secrets/longbridge_oauth_token.json`: not generated
- 已确认：App Key ≠ OAuth client_id（需使用独立的 OAuth Client ID）
- redirect_uri 使用: `http://localhost:60355/callback`
- 禁止纳入：注册接口返回的 access token（不写入代码、文档、日志、测试、snapshot 或 Git）

严禁写入以下内容（包括但不限于）：

- App Secret
- 完整 App Key
- 完整授权 URL
- state
- code
- token

## 四、复现步骤

按以下顺序执行：

```bash
python3 app.py longbridge-sdk-status
python3 app.py longbridge-status
python3 app.py longbridge-oauth-start
```

说明（历史问题已解决）：

- 过去因误用 App Key 作为 OAuth client_id 导致 `internal_server_error`，现已通过独立 OAuth Client ID 修正。
- SDK 可能托管 token cache，本项目仅记录脱敏 metadata，`longbridge-oauth-status` 会显示 `sdk_managed_configured`。

## 五、实际结果

浏览器页面（历史）：

```text
Authorization Failed
Error: internal_server_error
```

终端脱敏结果：

```text
oauth: oauth_failed
error_type: internal_server_error
likely_stage: authorization_server
client_id_present: true
redirect_uri_host: localhost
redirect_uri_scheme: http
quote_only: true
trade_enabled: false
```

## 六、期望结果

希望继续用 OAuth 授权对象调用 `QuoteContext` 做只读行情查询，并优先验证 US/HK 市场标的。

## 七、需要 Longbridge 支持确认的问题

1. 已确认 App Key 不能作为 `OAuthBuilder` 的 `client_id` 使用（本地已采用独立 OAuth Client ID）
2. OAuth Client 需通过 `/oauth2/register` 单独创建（已完成本地注册）
3. 是否需要登记 `redirect_uri`？
4. `OAuthBuilder` 默认 `localhost` callback 是否被支持？
5. 当前账号 / 地区 / 权限是否支持 `OAuthBuilder`？
6. Legacy Access Token 显示为 `--` 是否是正常策略？
7. 只读行情权限是否需要单独开通？
8. A股 CN quote 是否需要额外行情权限？
9. `internal_server_error` 是否为已知问题？
10. 是否建议先用 HK / US 标的验证，比如 `700.HK` / `AAPL.US`？

## 八、项目安全边界

- 只读行情
- 只使用 `QuoteContext`
- 不导入 `TradeContext`
- 不读资产
- 不读持仓
- 不读订单
- 不下单
- 不撤单
- 不修改账户
- token 不进入 Git
- token 不进入 logs / reports / snapshot / frontend json

## 九、后续接入计划

等 Longbridge 授权问题解决后，再进入：

`V1.0-alpha-03-longbridge-oauth-quote-market-support`

计划如下：

1. 使用 Longbridge OAuth 成功后的凭证调用 `QuoteContext`
2. 增加 `longbridge-oauth-quote` US/HK 只读行情验证（AAPL.US / 700.HK）
3. 增加 `LongbridgeProvider` 的真实 quote 读取（仅 QuoteContext）
4. 前端 RealtimeMarketView 增加真实 Longbridge 行情卡片
5. 数据源切换从视觉原型升级为真实只读切换
6. AkShare 作为 fallback，Longbridge 作为候选 / 可选高质量源
7. 全程保持不接交易
