# macOS 打包说明 (Packaging for macOS)

本目录包含用于在 macOS 环境下构建 **A股智研台** 桌面客户端的自动化脚本。

## 1. 当前适用环境

- **操作系统**: macOS (Intel/Apple Silicon)
- **Node.js**: v22 LTS (推荐 22.11.0+)
- **npm**: 10.9.7+
- **Rust**: 1.82.0+ (Cargo)
- **Tauri**: v2.x
- **品牌资产**: 已集成 V0.6.7 标准化 logo/banner

## 2. 首次准备命令

在执行打包脚本前，请确保终端环境已正确加载 Node 和 Rust 路径：

```bash
# 加载 zsh 配置 (如果使用的是 zsh)
source ~/.zshrc

# 切换到 Node 22
nvm use 22

# 加载 Rust 环境
source "$HOME/.cargo/env"
```

## 3. 一键打包命令

在项目根目录下执行以下命令即可开始完整构建流程：

```bash
bash packaging/macos/build_macos.sh
```

该脚本将自动完成：
1. 环境检查 (Node, npm, Rust, Tauri CLI)
2. 前端构建 (`frontend-react` npm run build)
3. 后端构建与打包 (Tauri build)
4. **DMG Fallback**: 如果 Tauri 自带的 DMG 封装脚本 (`bundle_dmg.sh`) 失败，只要 `.app` 已成功生成，脚本会自动调用 `hdiutil` 生成一个朴素的 DMG 安装包，确保打包流程不中断。

## 4. 输出产物路径

成功构建后，产物将位于：

- **.app 程序**: `src-tauri/target/release/bundle/macos/A股智研台.app`
- **.dmg 安装包**: `src-tauri/target/release/bundle/dmg/A股智研台_{版本}_{架构}.dmg`

> **注意**: 使用 `hdiutil fallback` 生成的 DMG 为朴素版，暂不包含自定义背景图和 /Applications 快捷方式软链接。当前阶段以“稳定可交付”为优先。

## 5. 常见问题 (FAQ)

- **nvm command not found**: 请确保已安装 nvm，并在 `.zshrc` 或 `.bash_profile` 中配置了加载脚本。
- **node 版本不对**: 脚本会检查 Node 版本，若非 v22 请执行 `nvm use 22`。
- **cargo/rustc command not found**: 请确保已安装 Rustup，并执行 `source "$HOME/.cargo/env"`。
- **Tauri CLI 未找到**: 本项目优先复用 `tauri-lab` 中的 Tauri CLI。如果两者均无，请在主项目执行 `npm install -D @tauri-apps/cli` (注意：本说明暂不建议在主项目执行 npm install)。
- **图标 PNG must be RGBA**: 如果更换了图标，请确保 `src-tauri/icons` 下的 PNG 为 RGBA 格式。
- **macOS 提示无法验证开发者**: 这是因为当前流程尚未进行 Apple Developer 签名。
  - **解决方法**: 在 Finder 中右键点击 `.app` -> “打开”，或在“系统设置 -> 隐私与安全性”中点击“仍要打开”。

## 6. 重要说明

- **签名与公证**: 当前为本地开发打包流程，**尚未**集成 Apple Developer ID 签名与公证 (Notarization)。生成的 DMG 仅供本地测试或内部分发。
- **依赖管理**: 请遵循项目规则，不要随意升级 `package.json` 中的依赖版本。
