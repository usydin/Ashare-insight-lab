# AGPL-3.0 与商业许可边界说明

## 1. FinceptTerminal 的许可证模式
根据 `docs/research/FinceptTerminal_source_scan_20260502_223321.md`，FinceptTerminal 采用 **AGPL-3.0 + Commercial License** 的双许可证模式：
- **AGPL-3.0**：开源版本，要求修改后必须开源，且即使是通过网络提供服务（SaaS）也必须开源。
- **Commercial License**：商业许可，适用于企业内部使用、闭源商业化或特定商业场景。

## 2. 学习与研究边界
A股智研台（AShare Insight Lab）当前对 FinceptTerminal 的研究处于**纯学术/架构调研**阶段，必须遵守以下边界：
- **不复制源码**：严禁将 FinceptTerminal 的任何 C++ 或 Python 源码（包括但不限于算法、UI 逻辑、数据处理代码）复制到本项目中。
- **不引入重依赖**：不引入 FinceptTerminal 专有的或其核心依赖（如特定的 C++ 库、Qt 专有扩展等）。
- **不复刻 Trade Dress**：不模仿其 UI 布局、配色、图标体系、终端命令（Syntax）、快捷键、dashboard widget vocabulary 等整体视觉风格。
- **不使用品牌资产**：严禁使用 Fincept 名称、Logo、商标或任何具有识别性的品牌元素。
- **不包含第三方代码**：不把 FinceptTerminal 的任何部分放入本项目的 `third_party` 或 `vendor` 目录。

## 3. 许可证差异对比
| 项目 | 许可证 | 核心限制 |
| :--- | :--- | :--- |
| **TradingAgents** | Apache-2.0 | 宽松，允许商业化，要求保留版权声明。 |
| **FinceptTerminal** | AGPL-3.0 + 商业 | 严格，强制传染开源（网络服务），商业使用需付费。 |
| **A股智研台** | 待定 (自有版权) | Copyright © 2026 @B‘lock10STUdio. |

## 4. 未来引用说明
如果在项目后续开发中，确实需要参考 FinceptTerminal 的某个具体功能实现：
1. **重新评估**：必须针对该具体实现重新进行许可证兼容性评估。
2. **优先自行实现**：基于业务逻辑，从零开始编写代码，不参考其具体源码实现。
3. **独立性**：确保本项目的代码逻辑与第三方项目具有明显的实质性差异。

## 5. 版权声明
本项目（A股智研台）的所有自有代码、文档及设计版权均为：
**Copyright © 2026 @B‘lock10STUdio. All rights reserved.**

任何对第三方项目的研究、学习记录，不改变本项目自有版权的独立性。
