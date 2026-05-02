# AGPL-3.0 项目使用边界补充

## 文档定位

本文档用于补充说明 MiroFish 与 FinceptTerminal 这类强约束许可证项目在 A股智研台中的研究边界。

## MiroFish 的许可证属性

根据扫描报告可见，MiroFish 使用 `AGPL-3.0`。

这意味着：

- 若复制、修改并分发其代码，需要遵守 AGPL-3.0
- 若将修改版作为网络服务公开提供，也会触发对应源码开放义务

因此，对这类项目不能用“只是参考一下实现”来弱化许可证边界。

## FinceptTerminal 的许可证属性

FinceptTerminal 同样属于强约束许可证项目。

其特点是：

- 具有 AGPL-3.0 约束
- 还叠加商业许可与商标、trade dress 等额外边界

因此，MiroFish 与 FinceptTerminal 都不适合在当前阶段直接并入 A股智研台代码体系。

## 当前阶段的硬边界

当前阶段明确只学习架构，不复制源码：

- 不复制 MiroFish 源码
- 不复制 FinceptTerminal 源码
- 不引入 MiroFish 依赖
- 不引入 FinceptTerminal 依赖
- 不照搬其前后端结构
- 不复刻其界面、品牌、交互词汇或视觉表达

## 对 MiroFish 的具体限制

当前明确不引入以下内容：

- MiroFish 源码
- MiroFish Logo
- MiroFish 名称
- MiroFish UI
- MiroFish 前后端结构

即使某些流程设计有启发，也只能做抽象研究与自有规划，不能做复制式落地。

## 本项目版权体系保持独立

A股智研台当前继续保持自有版权体系：

- 开发者：`pL`
- 版权品牌：`@B‘lock10STUdio`
- 自有版权：`Copyright © 2026 @B‘lock10STUdio. All rights reserved.`

第三方项目的研究文档，不会改变本项目自有代码、文档与设计的版权归属。

## 研究与实现的区分原则

未来若确实要参考 AGPL-3.0 项目的某个具体思路，必须遵守以下原则：

1. 先做许可证重新评估
2. 优先自研，不复制源码
3. 不使用第三方品牌、名称与界面表达
4. 明确记录参考来源与研究边界

## 当前结论

MiroFish 与 FinceptTerminal 当前都只作为“强约束许可证下的架构研究对象”存在。

本项目当前只吸收：

- 产品思路
- 流程组织方法
- 架构分层启发

本项目当前不吸收：

- 源码实现
- UI 表达
- 品牌资产
- 前后端工程结构
