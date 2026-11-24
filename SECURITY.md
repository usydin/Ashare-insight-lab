# 安全政策 | Security Policy

## 范围 / Scope

本项目为本地投研辅助与模拟研究工具，非交易执行系统。当前不承诺生产服务、安全响应 SLA 或经认证的安全等级。This is a local research and simulation project, not a live trading execution system. No production support SLA or security certification is claimed.

## 数据与凭据 / Data and credentials

- 不提交 API Token、OAuth 凭据、账户资料、真实持仓、个人数据或未获许可的行情数据；样例使用脱敏或合成数据。
- 只读行情访问与真实交易执行是不同权限，不能因读取成功推定具备交易授权。
- 发现凭据泄露时不要复制公开值；通过相应服务商及授权维护渠道评估撤销、轮换和影响。
- Do not commit API tokens, OAuth credentials, account records, actual holdings, personal data or market data without redistribution rights. Use sanitized or synthetic examples.
- Read-only market access does not authorize trading. Report suspected credential exposure privately and evaluate revocation and rotation.

## 报告 / Reporting

通过已建立的授权维护人员私密联系渠道报告，提供受影响版本、最小脱敏复现、影响与修复建议。不要在公开 Issue 中披露秘密或个人信息。正式公开漏洞报告入口与响应期限尚待核实。
Use an established private channel with authorized maintainers. Include affected version, sanitized reproduction, impact and remediation. Do not post secrets or personal information publicly. A dedicated reporting channel and response timeline remain to be verified.

现有 [版权声明](COPYRIGHT.md) 与 [NOTICE](NOTICE.md) 保持有效。本政策不授予新增许可，也不代表完成历史密钥扫描或安全测试。
Existing copyright and notice terms remain unchanged. This policy is not a security audit or new license.
