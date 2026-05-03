#!/bin/bash

# 设置严格模式
set -euo pipefail

# 1. 自动定位项目根目录
# 脚本所在目录是 project_root/packaging/macos/
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../" && pwd)"

cd "$PROJECT_ROOT"

echo "=== A股智研台 macOS 打包流程开始 ==="
echo "项目根目录: $PROJECT_ROOT"

# 2. 检查 Node.js 版本是否为 v22
NODE_VERSION=$(node -v 2>/dev/null || echo "none")
if [[ ! "$NODE_VERSION" =~ ^v22 ]]; then
    echo "错误: 当前 Node.js 版本为 $NODE_VERSION，要求 v22 LTS。"
    echo "提示: 请执行 'nvm use 22' 切换版本。"
    exit 1
fi
echo "✓ Node.js 版本: $NODE_VERSION"

# 3. 检查 npm 是否存在
if ! command -v npm &> /dev/null; then
    echo "错误: 未找到 npm，请确保已安装 Node.js。"
    exit 1
fi
echo "✓ npm 已就绪: $(npm -v)"

# 4. 检查 rustc / cargo 是否存在
if ! command -v rustc &> /dev/null || ! command -v cargo &> /dev/null; then
    echo "错误: 未找到 Rust 或 Cargo。"
    echo "提示: 请确保已执行 'source \"\$HOME/.cargo/env\"'。"
    exit 1
fi
echo "✓ Rust/Cargo 已就绪: $(rustc --version)"

# 5. 检查 frontend-react/package.json
if [ ! -f "frontend-react/package.json" ]; then
    echo "错误: 未找到 frontend-react/package.json。"
    exit 1
fi

# 6. 检查 src-tauri/tauri.conf.json
if [ ! -f "src-tauri/tauri.conf.json" ]; then
    echo "错误: 未找到 src-tauri/tauri.conf.json。"
    exit 1
fi

# 7. 构建前端
echo ">>> 正在构建前端 (frontend-react)..."
cd "frontend-react"
npm run build
cd "$PROJECT_ROOT"

# 8. 执行 Tauri build
# 定义 Tauri CLI 路径
TAURI_CLI_LOCAL="./node_modules/.bin/tauri"
TAURI_CLI_EXTERNAL="/Users/balwyn/Documents/trae_projects/tauri-lab/node_modules/.bin/tauri"

if [ -f "$TAURI_CLI_LOCAL" ]; then
    TAURI_CLI="$TAURI_CLI_LOCAL"
elif [ -f "$TAURI_CLI_EXTERNAL" ]; then
    TAURI_CLI="$TAURI_CLI_EXTERNAL"
elif command -v tauri &> /dev/null; then
    TAURI_CLI="tauri"
else
    echo "错误: 未找到 Tauri CLI。"
    echo "提示: 未找到 Tauri CLI，请先在 tauri-lab 或主项目中准备 Tauri CLI。"
    exit 1
fi

echo "✓ 使用 Tauri CLI: $TAURI_CLI"

# 清理旧的 DMG 目录，防止 bundle_dmg.sh 失败
if [ -d "src-tauri/target/release/bundle/dmg" ]; then
    echo ">>> 清理旧的 DMG 构建目录..."
    rm -rf src-tauri/target/release/bundle/dmg
fi

echo ">>> 正在执行 Tauri Build..."
# 临时关闭 set -e 以捕获退出码
set +e
$TAURI_CLI build
TAURI_EXIT_CODE=$?
set -e

APP_PATH="src-tauri/target/release/bundle/macos/A股智研台.app"

if [ $TAURI_EXIT_CODE -eq 0 ]; then
    echo "✓ Tauri Build 成功完成。"
else
    echo "⚠️  Tauri Build 过程中出现错误 (退出码: $TAURI_EXIT_CODE)。"
    
    if [ -d "$APP_PATH" ]; then
        echo "💡 Tauri 自带 DMG 封装失败，但 .app 已生成，开始使用 hdiutil fallback 生成朴素 DMG。"
        
        STAGING_DIR="packaging/macos/dmg-staging"
        DMG_OUT_DIR="src-tauri/target/release/bundle/dmg"
        FINAL_DMG="$DMG_OUT_DIR/A股智研台_0.5.0_aarch64.dmg"
        
        # 清理并准备环境
        rm -rf "$STAGING_DIR"
        mkdir -p "$STAGING_DIR"
        mkdir -p "$DMG_OUT_DIR"
        rm -f "$FINAL_DMG"
        
        # 复制 .app 到暂存区
        cp -R "$APP_PATH" "$STAGING_DIR/"
        
        # 使用 hdiutil 生成 DMG
        echo ">>> 正在使用 hdiutil 生成 DMG..."
        hdiutil create \
          -volname "A股智研台" \
          -srcfolder "$STAGING_DIR" \
          -ov \
          -format UDZO \
          "$FINAL_DMG"
        
        echo "✅ 已使用 hdiutil fallback 生成 DMG"
        # 清理暂存区
        rm -rf "$STAGING_DIR"
    else
        echo "❌ 错误: Tauri build 未生成 .app，请检查 Rust/Tauri 编译错误。"
        exit 1
    fi
fi

# 10. 输出产物路径
echo "=== 打包完成 ==="
DMG_PATH=$(find src-tauri/target/release/bundle/dmg -name "A股智研台_*.dmg" | head -n 1)

if [ -d "$APP_PATH" ]; then
    echo "✅ .app 产物: $PROJECT_ROOT/$APP_PATH"
else
    echo "❌ 未找到 .app 产物"
fi

if [ -n "$DMG_PATH" ] && [ -f "$DMG_PATH" ]; then
    echo "✅ .dmg 产物: $PROJECT_ROOT/$DMG_PATH"
else
    echo "❌ 未找到 .dmg 产物"
fi
