# 长桥 OpenAPI OAuth 授权失败排查材料

## 一、问题摘要

A股智研台计划接入 Longbridge OpenAPI 作为只读行情源，仅使用 `QuoteContext`，不使用 `TradeContext`。

当前卡在 `OAuthBuilder` 授权阶段：本地 CLI 可启动授权流程并生成授权 URL，但浏览器打开授权页后返回：

```text
Authorization Failed
Error: internal_server_error
```

当前问题尚未进入真实只读行情查询阶段，系统也尚未获得可用于 `Config.from_oauth(oauth)` 的授权对象或本地 OAuth token。

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

以下内容仅为脱敏状态说明，不包含真实凭证值：

- App Key: present
- App Secret: present
- Legacy Access Token: missing / 后台显示 `--`
- Region: cn
- OAuth token file: missing
- `.secrets/longbridge_oauth_token.json`: not generated

严禁写入以下内容：

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

说明：

- 执行 `longbridge-oauth-start` 后，SDK 可以生成授权 URL。
- 浏览器打开授权 URL 后，授权页返回 `internal_server_error`。
- 本地未生成 `.secrets/longbridge_oauth_token.json`。

## 五、实际结果

浏览器页面：

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

希望完成 OAuth 授权，获得可用于 `Config.from_oauth(oauth)` 的授权对象或 token，使系统可以继续调用 `QuoteContext` 做只读行情查询。

## 七、需要 Longbridge 支持确认的问题

1. 开发者后台的 App Key 是否可以直接作为 `OAuthBuilder` 的 `client_id` 使用？
2. 是否需要单独创建 OAuth Client？
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

`V1.0-alpha-03-longbridge-real-quote-integration`

计划如下：

1. 使用 Longbridge OAuth 成功后的凭证调用 `QuoteContext`
2. 增加 `longbridge-oauth-quote` 真实行情验证
3. 增加 `LongbridgeProvider` 的真实 quote 读取
4. 前端 RealtimeMarketView 增加真实 Longbridge 行情卡片
5. 数据源切换从视觉原型升级为真实只读切换
6. AkShare 作为 fallback，Longbridge 作为候选 / 可选高质量源
7. 全程保持不接交易
