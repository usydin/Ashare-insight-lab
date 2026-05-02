# MiroFish 源码初步扫描报告

生成时间：2026-05-02 23:29:43
源码路径：/Users/balwyn/Downloads/MiroFish-main

## 1. Git 信息

未检测到 .git 目录，可能是 GitHub 下载的 zip 解压包。

## 2. 顶层目录

```text
total 184
drwxrwxr-x@ 17 balwyn  staff    544  2 Apr 16:52 .
drwx------@ 57 balwyn  staff   1824  2 May 23:29 ..
-rw-rw-r--@  1 balwyn  staff    223  2 Apr 16:52 .dockerignore
-rw-rw-r--@  1 balwyn  staff    714  2 Apr 16:52 .env.example
drwxrwxr-x@  3 balwyn  staff     96  2 Apr 16:52 .github
-rw-rw-r--@  1 balwyn  staff    554  2 Apr 16:52 .gitignore
drwxrwxr-x@  8 balwyn  staff    256  2 Apr 16:52 backend
-rw-rw-r--@  1 balwyn  staff    371  2 Apr 16:52 docker-compose.yml
-rw-rw-r--@  1 balwyn  staff    723  2 Apr 16:52 Dockerfile
drwxrwxr-x@  9 balwyn  staff    288  2 Apr 16:52 frontend
-rw-rw-r--@  1 balwyn  staff  34523  2 Apr 16:52 LICENSE
drwxrwxr-x@  5 balwyn  staff    160  2 Apr 16:52 locales
-rw-rw-r--@  1 balwyn  staff  11188  2 Apr 16:52 package-lock.json
-rw-rw-r--@  1 balwyn  staff    702  2 Apr 16:52 package.json
-rw-rw-r--@  1 balwyn  staff   8151  2 Apr 16:52 README-ZH.md
-rw-rw-r--@  1 balwyn  staff   9124  2 Apr 16:52 README.md
drwxrwxr-x@  3 balwyn  staff     96  2 Apr 16:52 static
```

## 3. 目录结构，最多 4 层

```text
.
./.github
./.github/workflows
./backend
./backend/app
./backend/app/api
./backend/app/models
./backend/app/services
./backend/app/utils
./backend/scripts
./frontend
./frontend/public
./frontend/src
./frontend/src/api
./frontend/src/assets
./frontend/src/assets/logo
./frontend/src/components
./frontend/src/i18n
./frontend/src/router
./frontend/src/store
./frontend/src/views
./locales
./static
./static/image
./static/image/Screenshot
```

## 4. 主要文件清单，最多 350 个

```text
./.dockerignore
./.env.example
./.github/workflows/docker-image.yml
./.gitignore
./backend/app/__init__.py
./backend/app/api/__init__.py
./backend/app/api/graph.py
./backend/app/api/report.py
./backend/app/api/simulation.py
./backend/app/config.py
./backend/app/models/__init__.py
./backend/app/models/project.py
./backend/app/models/task.py
./backend/app/services/__init__.py
./backend/app/services/graph_builder.py
./backend/app/services/oasis_profile_generator.py
./backend/app/services/ontology_generator.py
./backend/app/services/report_agent.py
./backend/app/services/simulation_config_generator.py
./backend/app/services/simulation_ipc.py
./backend/app/services/simulation_manager.py
./backend/app/services/simulation_runner.py
./backend/app/services/text_processor.py
./backend/app/services/zep_entity_reader.py
./backend/app/services/zep_graph_memory_updater.py
./backend/app/services/zep_tools.py
./backend/app/utils/__init__.py
./backend/app/utils/file_parser.py
./backend/app/utils/llm_client.py
./backend/app/utils/locale.py
./backend/app/utils/logger.py
./backend/app/utils/retry.py
./backend/app/utils/zep_paging.py
./backend/pyproject.toml
./backend/requirements.txt
./backend/run.py
./backend/scripts/action_logger.py
./backend/scripts/run_parallel_simulation.py
./backend/scripts/run_reddit_simulation.py
./backend/scripts/run_twitter_simulation.py
./backend/scripts/test_profile_format.py
./backend/uv.lock
./docker-compose.yml
./Dockerfile
./frontend/.gitignore
./frontend/index.html
./frontend/package-lock.json
./frontend/package.json
./frontend/public/icon.png
./frontend/src/api/graph.js
./frontend/src/api/index.js
./frontend/src/api/report.js
./frontend/src/api/simulation.js
./frontend/src/App.vue
./frontend/src/assets/logo/MiroFish_logo_compressed.jpeg
./frontend/src/assets/logo/MiroFish_logo_left.jpeg
./frontend/src/components/GraphPanel.vue
./frontend/src/components/HistoryDatabase.vue
./frontend/src/components/LanguageSwitcher.vue
./frontend/src/components/Step1GraphBuild.vue
./frontend/src/components/Step2EnvSetup.vue
./frontend/src/components/Step3Simulation.vue
./frontend/src/components/Step4Report.vue
./frontend/src/components/Step5Interaction.vue
./frontend/src/i18n/index.js
./frontend/src/main.js
./frontend/src/router/index.js
./frontend/src/store/pendingUpload.js
./frontend/src/views/Home.vue
./frontend/src/views/InteractionView.vue
./frontend/src/views/MainView.vue
./frontend/src/views/Process.vue
./frontend/src/views/ReportView.vue
./frontend/src/views/SimulationRunView.vue
./frontend/src/views/SimulationView.vue
./frontend/vite.config.js
./LICENSE
./locales/en.json
./locales/languages.json
./locales/zh.json
./package-lock.json
./package.json
./README-ZH.md
./README.md
./static/image/红楼梦模拟推演封面.jpg
./static/image/武大模拟演示封面.png
./static/image/MiroFish_logo_compressed.jpeg
./static/image/MiroFish_logo.jpeg
./static/image/QQ群.png
./static/image/Screenshot/运行截图1.png
./static/image/Screenshot/运行截图2.png
./static/image/Screenshot/运行截图3.png
./static/image/Screenshot/运行截图4.png
./static/image/Screenshot/运行截图5.png
./static/image/Screenshot/运行截图6.png
./static/image/shanda_logo.png
```

## 5. 文件类型统计

```text
.py: 35
.vue: 16
.png: 10
.js: 9
.json: 7
[no_ext]: 5
.jpeg: 4
.md: 2
.yml: 2
.example: 1
.html: 1
.txt: 1
.lock: 1
.toml: 1
.jpg: 1
```

## 6. 关键项目文件预览

### README.md

```text
<div align="center">

<img src="./static/image/MiroFish_logo_compressed.jpeg" alt="MiroFish Logo" width="75%"/>

<a href="https://trendshift.io/repositories/16144" target="_blank"><img src="https://trendshift.io/api/badge/repositories/16144" alt="666ghj%2FMiroFish | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

简洁通用的群体智能引擎，预测万物
</br>
<em>A Simple and Universal Swarm Intelligence Engine, Predicting Anything</em>

<a href="https://www.shanda.com/" target="_blank"><img src="./static/image/shanda_logo.png" alt="666ghj%2MiroFish | Shanda" height="40"/></a>

[![GitHub Stars](https://img.shields.io/github/stars/666ghj/MiroFish?style=flat-square&color=DAA520)](https://github.com/666ghj/MiroFish/stargazers)
[![GitHub Watchers](https://img.shields.io/github/watchers/666ghj/MiroFish?style=flat-square)](https://github.com/666ghj/MiroFish/watchers)
[![GitHub Forks](https://img.shields.io/github/forks/666ghj/MiroFish?style=flat-square)](https://github.com/666ghj/MiroFish/network)
[![Docker](https://img.shields.io/badge/Docker-Build-2496ED?style=flat-square&logo=docker&logoColor=white)](https://hub.docker.com/)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/666ghj/MiroFish)

[![Discord](https://img.shields.io/badge/Discord-Join-5865F2?style=flat-square&logo=discord&logoColor=white)](http://discord.gg/ePf5aPaHnA)
[![X](https://img.shields.io/badge/X-Follow-000000?style=flat-square&logo=x&logoColor=white)](https://x.com/mirofish_ai)
[![Instagram](https://img.shields.io/badge/Instagram-Follow-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/mirofish_ai/)

[English](./README.md) | [中文文档](./README-ZH.md)

</div>

## ⚡ Overview

**MiroFish** is a next-generation AI prediction engine powered by multi-agent technology. By extracting seed information from the real world (such as breaking news, policy drafts, or financial signals), it automatically constructs a high-fidelity parallel digital world. Within this space, thousands of intelligent agents with independent personalities, long-term memory, and behavioral logic freely interact and undergo social evolution. You can inject variables dynamically from a "God's-eye view" to precisely deduce future trajectories — **rehearse the future in a digital sandbox, and win decisions after countless simulations**.

> You only need to: Upload seed materials (data analysis reports or interesting novel stories) and describe your prediction requirements in natural language</br>
> MiroFish will return: A detailed prediction report and a deeply interactive high-fidelity digital world

### Our Vision

MiroFish is dedicated to creating a swarm intelligence mirror that maps reality. By capturing the collective emergence triggered by individual interactions, we break through the limitations of traditional prediction:

- **At the Macro Level**: We are a rehearsal laboratory for decision-makers, allowing policies and public relations to be tested at zero risk
- **At the Micro Level**: We are a creative sandbox for individual users — whether deducing novel endings or exploring imaginative scenarios, everything can be fun, playful, and accessible

From serious predictions to playful simulations, we let every "what if" see its outcome, making it possible to predict anything.

## 🌐 Live Demo

Welcome to visit our online demo environment and experience a prediction simulation on trending public opinion events we've prepared for you: [mirofish-live-demo](https://666ghj.github.io/mirofish-demo/)

## 📸 Screenshots

<div align="center">
<table>
<tr>
<td><img src="./static/image/Screenshot/运行截图1.png" alt="Screenshot 1" width="100%"/></td>
<td><img src="./static/image/Screenshot/运行截图2.png" alt="Screenshot 2" width="100%"/></td>
</tr>
<tr>
<td><img src="./static/image/Screenshot/运行截图3.png" alt="Screenshot 3" width="100%"/></td>
<td><img src="./static/image/Screenshot/运行截图4.png" alt="Screenshot 4" width="100%"/></td>
</tr>
<tr>
<td><img src="./static/image/Screenshot/运行截图5.png" alt="Screenshot 5" width="100%"/></td>
<td><img src="./static/image/Screenshot/运行截图6.png" alt="Screenshot 6" width="100%"/></td>
</tr>
</table>
</div>

## 🎬 Demo Videos

### 1. Wuhan University Public Opinion Simulation + MiroFish Project Introduction

<div align="center">
<a href="https://www.bilibili.com/video/BV1VYBsBHEMY/" target="_blank"><img src="./static/image/武大模拟演示封面.png" alt="MiroFish Demo Video" width="75%"/></a>

Click the image to watch the complete demo video for prediction using BettaFish-generated "Wuhan University Public Opinion Report"
</div>

### 2. Dream of the Red Chamber Lost Ending Simulation

<div align="center">
<a href="https://www.bilibili.com/video/BV1cPk3BBExq" target="_blank"><img src="./static/image/红楼梦模拟推演封面.jpg" alt="MiroFish Demo Video" width="75%"/></a>

Click the image to watch MiroFish's deep prediction of the lost ending based on hundreds of thousands of words from the first 80 chapters of "Dream of the Red Chamber"
</div>

> **Financial Prediction**, **Political News Prediction** and more examples coming soon...

## 🔄 Workflow

1. **Graph Building**: Seed extraction & Individual/collective memory injection & GraphRAG construction
2. **Environment Setup**: Entity relationship extraction & Persona generation & Agent configuration injection
3. **Simulation**: Dual-platform parallel simulation & Auto-parse prediction requirements & Dynamic temporal memory updates
4. **Report Generation**: ReportAgent with rich toolset for deep interaction with post-simulation environment
5. **Deep Interaction**: Chat with any agent in the simulated world & Interact with ReportAgent

## 🚀 Quick Start

### Option 1: Source Code Deployment (Recommended)

#### Prerequisites

| Tool | Version | Description | Check Installation |
|------|---------|-------------|-------------------|
| **Node.js** | 18+ | Frontend runtime, includes npm | `node -v` |
| **Python** | ≥3.11, ≤3.12 | Backend runtime | `python --version` |
| **uv** | Latest | Python package manager | `uv --version` |

#### 1. Configure Environment Variables

```bash
# Copy the example configuration file
cp .env.example .env

# Edit the .env file and fill in the required API keys
```

**Required Environment Variables:**

```env
# LLM API Configuration (supports any LLM API with OpenAI SDK format)
# Recommended: Alibaba Qwen-plus model via Bailian Platform: https://bailian.console.aliyun.com/
# High consumption, try simulations with fewer than 40 rounds first
LLM_API_KEY=your_api_key
LLM_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
LLM_MODEL_NAME=qwen-plus

# Zep Cloud Configuration
# Free monthly quota is sufficient for simple usage: https://app.getzep.com/
ZEP_API_KEY=your_zep_api_key
```

#### 2. Install Dependencies

```bash
# One-click installation of all dependencies (root + frontend + backend)
npm run setup:all
```

Or install step by step:

```bash
# Install Node dependencies (root + frontend)
npm run setup

# Install Python dependencies (backend, auto-creates virtual environment)
npm run setup:backend
```

#### 3. Start Services

```bash
# Start both frontend and backend (run from project root)
npm run dev
```

**Service URLs:**
- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:5001`

**Start Individually:**

```bash
npm run backend   # Start backend only
npm run frontend  # Start frontend only
```

### Option 2: Docker Deployment

```bash
# 1. Configure environment variables (same as source deployment)
cp .env.example .env

# 2. Pull image and start
docker compose up -d
```

Reads `.env` from root directory by default, maps ports `3000 (frontend) / 5001 (backend)`

> Mirror address for faster pulling is provided as comments in `docker-compose.yml`, replace if needed.

## 📬 Join the Conversation

<div align="center">
<img src="./static/image/QQ群.png" alt="QQ Group" width="60%"/>
</div>

&nbsp;

The MiroFish team is recruiting full-time/internship positions. If you're interested in multi-agent simulation and LLM applications, feel free to send your resume to: **mirofish@shanda.com**

## 📄 Acknowledgments

**MiroFish has received strategic support and incubation from Shanda Group!**

MiroFish's simulation engine is powered by **[OASIS (Open Agent Social Interaction Simulations)](https://github.com/camel-ai/oasis)**, We sincerely thank the CAMEL-AI team for their open-source contributions!

## 📈 Project Statistics

<a href="https://www.star-history.com/#666ghj/MiroFish&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=666ghj/MiroFish&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=666ghj/MiroFish&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=666ghj/MiroFish&type=date&legend=top-left" />
 </picture>
</a>```

### package.json

```text
{
  "name": "mirofish",
  "version": "0.1.0",
  "description": "MiroFish - 简洁通用的群体智能引擎，预测万物",
  "scripts": {
    "setup": "npm install && cd frontend && npm install",
    "setup:backend": "cd backend && uv sync",
    "setup:all": "npm run setup && npm run setup:backend",
    "dev": "concurrently --kill-others -n \"backend,frontend\" -c \"green,cyan\" \"npm run backend\" \"npm run frontend\"",
    "backend": "cd backend && uv run python run.py",
    "frontend": "cd frontend && npm run dev",
    "build": "cd frontend && npm run build"
  },
  "devDependencies": {
    "concurrently": "^9.1.2"
  },
  "engines": {
    "node": ">=18.0.0"
  },
  "license": "AGPL-3.0"
}
```

### package-lock.json

```text
{
  "name": "mirofish",
  "version": "0.1.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "mirofish",
      "version": "0.1.0",
      "license": "AGPL-3.0",
      "devDependencies": {
        "concurrently": "^9.1.2"
      },
      "engines": {
        "node": ">=18.0.0"
      }
    },
    "node_modules/ansi-regex": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz",
      "integrity": "sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/ansi-styles": {
      "version": "4.3.0",
      "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-4.3.0.tgz",
      "integrity": "sha512-zbB9rCJAT1rbjiVDb2hqKFHNYLxgtk8NURxZ3IZwD3F6NtxbXZQCnnSi1Lkx+IDohdPlFp222wVALIheZJQSEg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "color-convert": "^2.0.1"
      },
      "engines": {
        "node": ">=8"
      },
      "funding": {
        "url": "https://github.com/chalk/ansi-styles?sponsor=1"
      }
    },
    "node_modules/chalk": {
      "version": "4.1.2",
      "resolved": "https://registry.npmjs.org/chalk/-/chalk-4.1.2.tgz",
      "integrity": "sha512-oKnbhFyRIXpUuez8iBMmyEa4nbj4IOQyuhc/wy9kY7/WVPcwIO9VA668Pu8RkO7+0G76SLROeyw9CpQ061i4mA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "ansi-styles": "^4.1.0",
        "supports-color": "^7.1.0"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/chalk/chalk?sponsor=1"
      }
    },
    "node_modules/chalk/node_modules/supports-color": {
      "version": "7.2.0",
      "resolved": "https://registry.npmjs.org/supports-color/-/supports-color-7.2.0.tgz",
      "integrity": "sha512-qpCAvRl9stuOHveKsn7HncJRvv501qIacKzQlO/+Lwxc9+0q2wLyv4Dfvt80/DPn2pqOBsJdDiogXGR9+OvwRw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "has-flag": "^4.0.0"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/cliui": {
      "version": "8.0.1",
      "resolved": "https://registry.npmjs.org/cliui/-/cliui-8.0.1.tgz",
      "integrity": "sha512-BSeNnyus75C4//NQ9gQt1/csTXyo/8Sb+afLAkzAptFuMsod9HFokGNudZpi/oQV73hnVK+sR+5PVRMd+Dr7YQ==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "string-width": "^4.2.0",
        "strip-ansi": "^6.0.1",
        "wrap-ansi": "^7.0.0"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/color-convert": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/color-convert/-/color-convert-2.0.1.tgz",
      "integrity": "sha512-RRECPsj7iu/xb5oKYcsFHSppFNnsj/52OVTRKb4zP5onXwVF3zVmmToNcOfGC+CRDpfK/U584fMg38ZHCaElKQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "color-name": "~1.1.4"
      },
      "engines": {
        "node": ">=7.0.0"
      }
    },
    "node_modules/color-name": {
      "version": "1.1.4",
      "resolved": "https://registry.npmjs.org/color-name/-/color-name-1.1.4.tgz",
      "integrity": "sha512-dOy+3AuW3a2wNbZHIuMZpTcgjGuLU/uBL/ubcZF9OXbDo8ff4O8yVp5Bf0efS8uEoYo5q4Fx7dY9OgQGXgAsQA==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/concurrently": {
      "version": "9.2.1",
      "resolved": "https://registry.npmjs.org/concurrently/-/concurrently-9.2.1.tgz",
      "integrity": "sha512-fsfrO0MxV64Znoy8/l1vVIjjHa29SZyyqPgQBwhiDcaW8wJc2W3XWVOGx4M3oJBnv/zdUZIIp1gDeS98GzP8Ng==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "chalk": "4.1.2",
        "rxjs": "7.8.2",
        "shell-quote": "1.8.3",
        "supports-color": "8.1.1",
        "tree-kill": "1.2.2",
        "yargs": "17.7.2"
      },
      "bin": {
        "conc": "dist/bin/concurrently.js",
        "concurrently": "dist/bin/concurrently.js"
      },
      "engines": {
        "node": ">=18"
      },
      "funding": {
        "url": "https://github.com/open-cli-tools/concurrently?sponsor=1"
      }
    },
    "node_modules/emoji-regex": {
      "version": "8.0.0",
      "resolved": "https://registry.npmjs.org/emoji-regex/-/emoji-regex-8.0.0.tgz",
      "integrity": "sha512-MSjYzcWNOA0ewAHpz0MxpYFvwg6yjy1NG3xteoqz644VCo/RPgnr1/GGt+ic3iJTzQ8Eu3TdM14SawnVUmGE6A==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/escalade": {
      "version": "3.2.0",
      "resolved": "https://registry.npmjs.org/escalade/-/escalade-3.2.0.tgz",
      "integrity": "sha512-WUj2qlxaQtO4g6Pq5c29GTcWGDyd8itL8zTlipgECz3JesAiiOKotd8JU6otB3PACgG6xkJUyVhboMS+bje/jA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/get-caller-file": {
      "version": "2.0.5",
      "resolved": "https://registry.npmjs.org/get-caller-file/-/get-caller-file-2.0.5.tgz",
      "integrity": "sha512-DyFP3BM/3YHTQOCUL/w0OZHR0lpKeGrxotcHWcqNEdnltqFwXVfhEBQ94eIo34AfQpo0rGki4cyIiftY06h2Fg==",
      "dev": true,
      "license": "ISC",
      "engines": {
        "node": "6.* || 8.* || >= 10.*"
      }
    },
    "node_modules/has-flag": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/has-flag/-/has-flag-4.0.0.tgz",
      "integrity": "sha512-EykJT/Q1KjTWctppgIAgfSO0tKVuZUjhgMr17kqTumMl6Afv3EISleU7qZUzoXDFTAHTDC4NOoG/ZxU3EvlMPQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/is-fullwidth-code-point": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-3.0.0.tgz",
      "integrity": "sha512-zymm5+u+sCsSWyD9qNaejV3DFvhCKclKdizYaJUuHA83RLjb7nSuGnddCHGv0hk+KY7BMAlsWeK4Ueg6EV6XQg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/require-directory": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/require-directory/-/require-directory-2.1.1.tgz",
      "integrity": "sha512-fGxEI7+wsG9xrvdjsrlmL22OMTTiHRwAMroiEeMgq8gzoLC/PQr7RsRDSTLUg/bZAZtF+TVIkHc6/4RIKrui+Q==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/rxjs": {
      "version": "7.8.2",
      "resolved": "https://registry.npmjs.org/rxjs/-/rxjs-7.8.2.tgz",
      "integrity": "sha512-dhKf903U/PQZY6boNNtAGdWbG85WAbjT/1xYoZIC7FAY0yWapOBQVsVrDl58W86//e1VpMNBtRV4MaXfdMySFA==",
      "dev": true,
      "license": "Apache-2.0",
      "dependencies": {
        "tslib": "^2.1.0"
      }
    },
    "node_modules/shell-quote": {
      "version": "1.8.3",
      "resolved": "https://registry.npmjs.org/shell-quote/-/shell-quote-1.8.3.tgz",
      "integrity": "sha512-ObmnIF4hXNg1BqhnHmgbDETF8dLPCggZWBjkQfhZpbszZnYur5DUljTcCHii5LC3J5E0yeO/1LIMyH+UvHQgyw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/string-width": {
      "version": "4.2.3",
      "resolved": "https://registry.npmjs.org/string-width/-/string-width-4.2.3.tgz",
      "integrity": "sha512-wKyQRQpjJ0sIp62ErSZdGsjMJWsap5oRNihHhu6G7JVO/9jIB6UyevL+tXuOqrng8j/cxKTWyWUwvSTriiZz/g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "emoji-regex": "^8.0.0",
        "is-fullwidth-code-point": "^3.0.0",
        "strip-ansi": "^6.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/strip-ansi": {
      "version": "6.0.1",
      "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz",
      "integrity": "sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "ansi-regex": "^5.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/supports-color": {
      "version": "8.1.1",
      "resolved": "https://registry.npmjs.org/supports-color/-/supports-color-8.1.1.tgz",
      "integrity": "sha512-MpUEN2OodtUzxvKQl72cUF7RQ5EiHsGvSsVG0ia9c5RbWGL2CI4C7EpPS8UTBIplnlzZiNuV56w+FuNxy3ty2Q==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "has-flag": "^4.0.0"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/chalk/supports-color?sponsor=1"
      }
    },
    "node_modules/tree-kill": {
      "version": "1.2.2",
      "resolved": "https://registry.npmjs.org/tree-kill/-/tree-kill-1.2.2.tgz",
```

### Dockerfile

```text
FROM python:3.11

# 安装 Node.js （满足 >=18）及必要工具
RUN apt-get update \
  && apt-get install -y --no-install-recommends nodejs npm \
  && rm -rf /var/lib/apt/lists/*

# 从 uv 官方镜像复制 uv
COPY --from=ghcr.io/astral-sh/uv:0.9.26 /uv /uvx /bin/

WORKDIR /app

# 先复制依赖描述文件以利用缓存
COPY package.json package-lock.json ./
COPY frontend/package.json frontend/package-lock.json ./frontend/
COPY backend/pyproject.toml backend/uv.lock ./backend/

# 安装依赖（Node + Python）
RUN npm ci \
  && npm ci --prefix frontend \
  && cd backend && uv sync --frozen

# 复制项目源码
COPY . .

EXPOSE 3000 5001

# 同时启动前后端（开发模式）
CMD ["npm", "run", "dev"]```

### docker-compose.yml

```text
services:
  mirofish:
    image: ghcr.io/666ghj/mirofish:latest
    # 加速镜像（如拉取缓慢可替换上方地址）
    # image: ghcr.nju.edu.cn/666ghj/mirofish:latest
    container_name: mirofish
    env_file:
      - .env
    ports:
      - "3000:3000"
      - "5001:5001"
    restart: unless-stopped
    volumes:
      - ./backend/uploads:/app/backend/uploads```

### LICENSE

```text
                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU Affero General Public License is a free, copyleft license for
software and other kinds of works, specifically designed to ensure
cooperation with the community in the case of network server software.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
our General Public Licenses are intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  Developers that use our General Public Licenses protect your rights
with two steps: (1) assert copyright on the software, and (2) offer
you this License which gives you legal permission to copy, distribute
and/or modify the software.

  A secondary benefit of defending all users' freedom is that
improvements made in alternate versions of the program, if they
receive widespread use, become available for other developers to
incorporate.  Many developers of free software are heartened and
encouraged by the resulting cooperation.  However, in the case of
software used on network servers, this result may fail to come about.
The GNU General Public License permits making a modified version and
letting the public access it on a server without ever releasing its
source code to the public.

  The GNU Affero General Public License is designed specifically to
ensure that, in such cases, the modified source code becomes available
to the community.  It requires the operator of a network server to
provide the source code of the modified version running there to the
users of that server.  Therefore, public use of a modified version, on
a publicly accessible server, gives the public access to the source
code of the modified version.

  An older license, called the Affero General Public License and
published by Affero, was designed to accomplish similar goals.  This is
a different license, not a version of the Affero GPL, but Affero has
released a new version of the Affero GPL which permits relicensing under
this license.

  The precise terms and conditions for copying, distribution and
modification follow.

                       TERMS AND CONDITIONS

  0. Definitions.

  "This License" refers to version 3 of the GNU Affero General Public License.

  "Copyright" also means copyright-like laws that apply to other kinds of
works, such as semiconductor masks.

  "The Program" refers to any copyrightable work licensed under this
License.  Each licensee is addressed as "you".  "Licensees" and
"recipients" may be individuals or organizations.

  To "modify" a work means to copy from or adapt all or part of the work
in a fashion requiring copyright permission, other than the making of an
exact copy.  The resulting work is called a "modified version" of the
earlier work or a work "based on" the earlier work.

  A "covered work" means either the unmodified Program or a work based
on the Program.

  To "propagate" a work means to do anything with it that, without
permission, would make you directly or secondarily liable for
infringement under applicable copyright law, except executing it on a
computer or modifying a private copy.  Propagation includes copying,
distribution (with or without modification), making available to the
public, and in some countries other activities as well.

  To "convey" a work means any kind of propagation that enables other
parties to make or receive copies.  Mere interaction with a user through
a computer network, with no transfer of a copy, is not conveying.

  An interactive user interface displays "Appropriate Legal Notices"
to the extent that it includes a convenient and prominently visible
feature that (1) displays an appropriate copyright notice, and (2)
tells the user that there is no warranty for the work (except to the
extent that warranties are provided), that licensees may convey the
work under this License, and how to view a copy of this License.  If
the interface presents a list of user commands or options, such as a
menu, a prominent item in the list meets this criterion.

  1. Source Code.

  The "source code" for a work means the preferred form of the work
for making modifications to it.  "Object code" means any non-source
form of a work.

  A "Standard Interface" means an interface that either is an official
standard defined by a recognized standards body, or, in the case of
interfaces specified for a particular programming language, one that
is widely used among developers working in that language.

  The "System Libraries" of an executable work include anything, other
than the work as a whole, that (a) is included in the normal form of
packaging a Major Component, but which is not part of that Major
Component, and (b) serves only to enable use of the work with that
Major Component, or to implement a Standard Interface for which an
implementation is available to the public in source code form.  A
"Major Component", in this context, means a major essential component
(kernel, window system, and so on) of the specific operating system
(if any) on which the executable work runs, or a compiler used to
produce the work, or an object code interpreter used to run it.

  The "Corresponding Source" for a work in object code form means all
the source code needed to generate, install, and (for an executable
work) run the object code and to modify the work, including scripts to
control those activities.  However, it does not include the work's
System Libraries, or general-purpose tools or generally available free
programs which are used unmodified in performing those activities but
which are not part of the work.  For example, Corresponding Source
includes interface definition files associated with source files for
the work, and the source code for shared libraries and dynamically
linked subprograms that the work is specifically designed to require,
such as by intimate data communication or control flow between those
subprograms and other parts of the work.

  The Corresponding Source need not include anything that users
can regenerate automatically from other parts of the Corresponding
Source.

  The Corresponding Source for a work in source code form is that
same work.

  2. Basic Permissions.

  All rights granted under this License are granted for the term of
copyright on the Program, and are irrevocable provided the stated
conditions are met.  This License explicitly affirms your unlimited
permission to run the unmodified Program.  The output from running a
covered work is covered by this License only if the output, given its
content, constitutes a covered work.  This License acknowledges your
rights of fair use or other equivalent, as provided by copyright law.

  You may make, run and propagate covered works that you do not
convey, without conditions so long as your license otherwise remains
in force.  You may convey covered works to others for the sole purpose
of having them make modifications exclusively for you, or provide you
with facilities for running those works, provided that you comply with
the terms of this License in conveying all material for which you do
not control copyright.  Those thus making or running the covered works
for you must do so exclusively on your behalf, under your direction
and control, on terms that prohibit them from making any copies of
your copyrighted material outside their relationship with you.

  Conveying under any other circumstances is permitted solely under
the conditions stated below.  Sublicensing is not allowed; section 10
makes it unnecessary.

  3. Protecting Users' Legal Rights From Anti-Circumvention Law.

  No covered work shall be deemed part of an effective technological
measure under any applicable law fulfilling obligations under article
11 of the WIPO copyright treaty adopted on 20 December 1996, or
similar laws prohibiting or restricting circumvention of such
measures.

  When you convey a covered work, you waive any legal power to forbid
circumvention of technological measures to the extent such circumvention
is effected by exercising rights under this License with respect to
the covered work, and you disclaim any intention to limit operation or
modification of the work as a means of enforcing, against the work's
users, your or third parties' legal rights to forbid circumvention of
technological measures.

  4. Conveying Verbatim Copies.

  You may convey verbatim copies of the Program's source code as you
receive it, in any medium, provided that you conspicuously and
appropriately publish on each copy an appropriate copyright notice;
keep intact all notices stating that this License and any
non-permissive terms added in accord with section 7 apply to the code;
keep intact all notices of the absence of any warranty; and give all
recipients a copy of this License along with the Program.

  You may charge any price or no price for each copy that you convey,
and you may offer support or warranty protection for a fee.

  5. Conveying Modified Source Versions.

  You may convey a work based on the Program, or the modifications to
produce it from the Program, in the form of source code under the
terms of section 4, provided that you also meet all of these conditions:

    a) The work must carry prominent notices stating that you modified
    it, and giving a relevant date.

    b) The work must carry prominent notices stating that it is
    released under this License and any conditions added under section
    7.  This requirement modifies the requirement in section 4 to
    "keep intact all notices".

    c) You must license the entire work, as a whole, under this
    License to anyone who comes into possession of a copy.  This
    License will therefore apply, along with any applicable section 7
    additional terms, to the whole of the work, and all its parts,
    regardless of how they are packaged.  This License gives no
    permission to license the work in any other way, but it does not
    invalidate such permission if you have separately received it.

    d) If the work has interactive user interfaces, each must display
    Appropriate Legal Notices; however, if the Program has interactive
    interfaces that do not display Appropriate Legal Notices, your
    work need not make them do so.

  A compilation of a covered work with other separate and independent
works, which are not by their nature extensions of the covered work,
and which are not combined with it such as to form a larger program,
in or on a volume of a storage or distribution medium, is called an
"aggregate" if the compilation and its resulting copyright are not
used to limit the access or legal rights of the compilation's users
beyond what the individual works permit.  Inclusion of a covered work
in an aggregate does not cause this License to apply to the other
parts of the aggregate.

  6. Conveying Non-Source Forms.

  You may convey a covered work in object code form under the terms
of sections 4 and 5, provided that you also convey the
machine-readable Corresponding Source under the terms of this License,
in one of these ways:

    a) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by the
    Corresponding Source fixed on a durable physical medium
    customarily used for software interchange.

    b) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by a
    written offer, valid for at least three years and valid for as
    long as you offer spare parts or customer support for that product
    model, to give anyone who possesses the object code either (1) a
    copy of the Corresponding Source for all the software in the
    product that is covered by this License, on a durable physical
    medium customarily used for software interchange, for a price no
    more than your reasonable cost of physically performing this
    conveying of source, or (2) access to copy the
    Corresponding Source from a network server at no charge.

    c) Convey individual copies of the object code with a copy of the
    written offer to provide the Corresponding Source.  This
    alternative is allowed only occasionally and noncommercially, and
    only if you received the object code with such an offer, in accord
```

### .env.example

```text
# LLM API配置（支持 OpenAI SDK 格式的任意 LLM API）
# 推荐使用阿里百炼平台qwen-plus模型：https://bailian.console.aliyun.com/
# 注意消耗较大，可先进行小于40轮的模拟尝试
LLM_API_KEY=your_api_key_here
LLM_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
LLM_MODEL_NAME=qwen-plus

# ===== ZEP记忆图谱配置 =====
# 每月免费额度即可支撑简单使用：https://app.getzep.com/
ZEP_API_KEY=your_zep_api_key_here

# ===== 加速 LLM 配置（可选）=====
# 注意如果不使用加速配置，env文件中就不要出现下面的配置项
LLM_BOOST_API_KEY=your_api_key_here
LLM_BOOST_BASE_URL=your_base_url_here
LLM_BOOST_MODEL_NAME=your_model_name_here```

## 7. 许可证与边界关键词扫描

```text
./frontend/package-lock.json:26:      "license": "MIT",
./frontend/package-lock.json:35:      "license": "MIT",
./frontend/package-lock.json:44:      "license": "MIT",
./frontend/package-lock.json:59:      "license": "MIT",
./frontend/package-lock.json:76:      "license": "MIT",
./frontend/package-lock.json:93:      "license": "MIT",
./frontend/package-lock.json:110:      "license": "MIT",
./frontend/package-lock.json:127:      "license": "MIT",
./frontend/package-lock.json:144:      "license": "MIT",
./frontend/package-lock.json:161:      "license": "MIT",
./frontend/package-lock.json:178:      "license": "MIT",
./frontend/package-lock.json:195:      "license": "MIT",
./frontend/package-lock.json:212:      "license": "MIT",
./frontend/package-lock.json:229:      "license": "MIT",
./frontend/package-lock.json:246:      "license": "MIT",
./frontend/package-lock.json:263:      "license": "MIT",
./frontend/package-lock.json:280:      "license": "MIT",
./frontend/package-lock.json:297:      "license": "MIT",
./frontend/package-lock.json:314:      "license": "MIT",
./frontend/package-lock.json:331:      "license": "MIT",
./frontend/package-lock.json:348:      "license": "MIT",
./frontend/package-lock.json:365:      "license": "MIT",
./frontend/package-lock.json:382:      "license": "MIT",
./frontend/package-lock.json:399:      "license": "MIT",
./frontend/package-lock.json:416:      "license": "MIT",
./frontend/package-lock.json:433:      "license": "MIT",
./frontend/package-lock.json:450:      "license": "MIT",
./frontend/package-lock.json:467:      "license": "MIT",
./frontend/package-lock.json:484:      "license": "MIT",
./frontend/package-lock.json:501:      "license": "MIT",
./frontend/package-lock.json:514:      "license": "MIT",
./frontend/package-lock.json:531:      "license": "MIT",
./frontend/package-lock.json:547:      "license": "MIT",
./frontend/package-lock.json:563:      "license": "MIT",
./frontend/package-lock.json:575:      "license": "MIT"
./frontend/package-lock.json:582:      "license": "MIT"
./frontend/package-lock.json:592:      "license": "MIT",
./frontend/package-lock.json:606:      "license": "MIT",
./frontend/package-lock.json:620:      "license": "MIT",
./frontend/package-lock.json:634:      "license": "MIT",
./frontend/package-lock.json:648:      "license": "MIT",
./frontend/package-lock.json:662:      "license": "MIT",
./frontend/package-lock.json:676:      "license": "MIT",
./frontend/package-lock.json:690:      "license": "MIT",
./frontend/package-lock.json:704:      "license": "MIT",
./frontend/package-lock.json:718:      "license": "MIT",
./frontend/package-lock.json:732:      "license": "MIT",
./frontend/package-lock.json:746:      "license": "MIT",
./frontend/package-lock.json:760:      "license": "MIT",
./frontend/package-lock.json:774:      "license": "MIT",
./frontend/package-lock.json:788:      "license": "MIT",
./frontend/package-lock.json:802:      "license": "MIT",
./frontend/package-lock.json:816:      "license": "MIT",
./frontend/package-lock.json:830:      "license": "MIT",
./frontend/package-lock.json:844:      "license": "MIT",
./frontend/package-lock.json:858:      "license": "MIT",
./frontend/package-lock.json:872:      "license": "MIT",
./frontend/package-lock.json:886:      "license": "MIT",
./frontend/package-lock.json:900:      "license": "MIT",
./frontend/package-lock.json:914:      "license": "MIT",
./frontend/package-lock.json:928:      "license": "MIT",
./frontend/package-lock.json:939:      "license": "MIT"
./frontend/package-lock.json:946:      "license": "MIT",
./frontend/package-lock.json:962:      "license": "MIT",
./frontend/package-lock.json:975:      "license": "MIT",
./frontend/package-lock.json:985:      "license": "MIT",
./frontend/package-lock.json:1002:      "license": "MIT",
./frontend/package-lock.json:1012:      "license": "MIT"
./frontend/package-lock.json:1018:      "license": "MIT",
./frontend/package-lock.json:1027:      "license": "MIT",
./frontend/package-lock.json:1037:      "license": "MIT",
./frontend/package-lock.json:1049:      "license": "MIT",
./frontend/package-lock.json:1062:      "license": "MIT"
./frontend/package-lock.json:1068:      "license": "MIT"
./frontend/package-lock.json:1074:      "license": "MIT",
./frontend/package-lock.json:1085:      "license": "MIT",
./frontend/package-lock.json:1098:      "license": "MIT",
./frontend/package-lock.json:1110:      "license": "MIT",
./frontend/package-lock.json:1119:      "license": "MIT"
./frontend/package-lock.json:1125:      "license": "ISC",
./frontend/package-lock.json:1166:      "license": "ISC",
./frontend/package-lock.json:1178:      "license": "ISC",
./frontend/package-lock.json:1187:      "license": "ISC",
./frontend/package-lock.json:1203:      "license": "ISC",
./frontend/package-lock.json:1215:      "license": "ISC",
./frontend/package-lock.json:1224:      "license": "ISC",
./frontend/package-lock.json:1236:      "license": "ISC",
./frontend/package-lock.json:1248:      "license": "ISC",
./frontend/package-lock.json:1257:      "license": "ISC",
./frontend/package-lock.json:1270:      "license": "ISC",
./frontend/package-lock.json:1295:      "license": "BSD-3-Clause",
./frontend/package-lock.json:1304:      "license": "ISC",
./frontend/package-lock.json:1316:      "license": "ISC",
./frontend/package-lock.json:1330:      "license": "ISC",
./frontend/package-lock.json:1339:      "license": "ISC",
./frontend/package-lock.json:1351:      "license": "ISC",
./frontend/package-lock.json:1360:      "license": "ISC",
./frontend/package-lock.json:1372:      "license": "ISC",
./frontend/package-lock.json:1381:      "license": "ISC",
./frontend/package-lock.json:1390:      "license": "ISC",
./frontend/package-lock.json:1399:      "license": "ISC",
./frontend/package-lock.json:1408:      "license": "ISC",
./frontend/package-lock.json:1424:      "license": "ISC",
./frontend/package-lock.json:1437:      "license": "ISC",
./frontend/package-lock.json:1447:      "license": "ISC",
./frontend/package-lock.json:1459:      "license": "ISC",
./frontend/package-lock.json:1471:      "license": "ISC",
./frontend/package-lock.json:1483:      "license": "ISC",
./frontend/package-lock.json:1492:      "license": "ISC",
./frontend/package-lock.json:1511:      "license": "ISC",
./frontend/package-lock.json:1527:      "license": "ISC",
./frontend/package-lock.json:1536:      "license": "MIT",
./frontend/package-lock.json:1545:      "license": "MIT",
./frontend/package-lock.json:1559:      "license": "BSD-2-Clause",
./frontend/package-lock.json:1571:      "license": "MIT",
./frontend/package-lock.json:1580:      "license": "MIT",
./frontend/package-lock.json:1589:      "license": "MIT",
./frontend/package-lock.json:1601:      "license": "MIT",
./frontend/package-lock.json:1618:      "license": "MIT",
./frontend/package-lock.json:1658:      "license": "MIT"
./frontend/package-lock.json:1665:      "license": "MIT",
./frontend/package-lock.json:1688:      "license": "MIT",
./frontend/package-lock.json:1702:      "license": "MIT",
./frontend/package-lock.json:1720:      "license": "MIT",
./frontend/package-lock.json:1733:      "license": "MIT",
./frontend/package-lock.json:1742:      "license": "MIT",
./frontend/package-lock.json:1766:      "license": "MIT",
./frontend/package-lock.json:1779:      "license": "MIT",
./frontend/package-lock.json:1791:      "license": "MIT",
./frontend/package-lock.json:1803:      "license": "MIT",
./frontend/package-lock.json:1818:      "license": "MIT",
./frontend/package-lock.json:1830:      "license": "MIT",
./frontend/package-lock.json:1842:      "license": "ISC",
./frontend/package-lock.json:1851:      "license": "MIT",
./frontend/package-lock.json:1860:      "license": "MIT",
./frontend/package-lock.json:1869:      "license": "MIT",
./frontend/package-lock.json:1878:      "license": "MIT",
./frontend/package-lock.json:1896:      "license": "MIT",
./frontend/package-lock.json:1908:      "license": "ISC"
./frontend/package-lock.json:1915:      "license": "MIT",
./frontend/package-lock.json:1942:      "license": "MIT",
./frontend/package-lock.json:1956:      "license": "MIT",
./frontend/package-lock.json:1965:      "license": "Unlicense"
./frontend/package-lock.json:1972:      "license": "MIT",
./frontend/package-lock.json:2016:      "license": "BSD-3-Clause"
./frontend/package-lock.json:2022:      "license": "MIT"
./frontend/package-lock.json:2028:      "license": "BSD-3-Clause",
./frontend/package-lock.json:2038:      "license": "MIT",
./frontend/package-lock.json:2055:      "license": "MIT",
./frontend/package-lock.json:2130:      "license": "MIT",
./frontend/package-lock.json:2152:      "license": "MIT",
./frontend/package-lock.json:2173:      "license": "MIT",
./LICENSE:6: of this license document, but changing it is not allowed.
./LICENSE:10:  The GNU Affero General Public License is a free, copyleft license for
./LICENSE:14:  The licenses for most software and other practical works are designed
./LICENSE:23:them if you wish), that you receive source code or can get it if you
./LICENSE:28:with two steps: (1) assert copyright on the software, and (2) offer
./LICENSE:29:you this License which gives you legal permission to copy, distribute
./LICENSE:40:source code to the public.
./LICENSE:43:ensure that, in such cases, the modified source code becomes available
./LICENSE:45:provide the source code of the modified version running there to the
./LICENSE:50:  An older license, called the Affero General Public License and
./LICENSE:52:a different license, not a version of the Affero GPL, but Affero has
./LICENSE:53:released a new version of the Affero GPL which permits relicensing under
./LICENSE:54:this license.
./LICENSE:65:  "Copyright" also means copyright-like laws that apply to other kinds of
./LICENSE:68:  "The Program" refers to any copyrightable work licensed under this
./LICENSE:69:License.  Each licensee is addressed as "you".  "Licensees" and
./LICENSE:73:in a fashion requiring copyright permission, other than the making of an
./LICENSE:81:permission, would make you directly or secondarily liable for
./LICENSE:82:infringement under applicable copyright law, except executing it on a
./LICENSE:93:feature that (1) displays an appropriate copyright notice, and (2)
./LICENSE:94:tells the user that there is no warranty for the work (except to the
./LICENSE:95:extent that warranties are provided), that licensees may convey the
./LICENSE:102:  The "source code" for a work means the preferred form of the work
./LICENSE:116:implementation is available to the public in source code form.  A
./LICENSE:123:the source code needed to generate, install, and (for an executable
./LICENSE:130:the work, and the source code for shared libraries and dynamically
./LICENSE:139:  The Corresponding Source for a work in source code form is that
./LICENSE:145:copyright on the Program, and are irrevocable provided the stated
./LICENSE:147:permission to run the unmodified Program.  The output from running a
./LICENSE:150:rights of fair use or other equivalent, as provided by copyright law.
./LICENSE:153:convey, without conditions so long as your license otherwise remains
./LICENSE:158:not control copyright.  Those thus making or running the covered works
./LICENSE:161:your copyrighted material outside their relationship with you.
./LICENSE:171:11 of the WIPO copyright treaty adopted on 20 December 1996, or
./LICENSE:185:  You may convey verbatim copies of the Program's source code as you
./LICENSE:187:appropriately publish on each copy an appropriate copyright notice;
./LICENSE:190:keep intact all notices of the absence of any warranty; and give all
./LICENSE:194:and you may offer support or warranty protection for a fee.
./LICENSE:199:produce it from the Program, in the form of source code under the
./LICENSE:210:    c) You must license the entire work, as a whole, under this
./LICENSE:215:    permission to license the work in any other way, but it does not
./LICENSE:216:    invalidate such permission if you have separately received it.
./LICENSE:227:"aggregate" if the compilation and its resulting copyright are not
./LICENSE:259:    alternative is allowed only occasionally and noncommercially, and
./LICENSE:281:  A separable portion of the object code, whose source code is excluded
./LICENSE:295:commercial, industrial or non-consumer uses, unless such uses represent
./LICENSE:318:requirement to continue to provide support service, warranty, or updates
./LICENSE:328:source code form), and must require no special password or key for
./LICENSE:333:  "Additional permissions" are terms that supplement the terms of this
./LICENSE:335:Additional permissions that are applicable to the entire Program shall
./LICENSE:337:that they are valid under applicable law.  If additional permissions
./LICENSE:339:under those permissions, but the entire Program remains governed by
./LICENSE:340:this License without regard to the additional permissions.
./LICENSE:343:remove any additional permissions from that copy, or from any part of
./LICENSE:344:it.  (Additional permissions may be written to require their own
./LICENSE:346:additional permissions on material, added by you to a covered work,
./LICENSE:347:for which you have or can give appropriate copyright permission.
./LICENSE:350:add to a covered work, you may (if authorized by the copyright holders of
./LICENSE:353:    a) Disclaiming warranty or limiting liability differently from the
./LICENSE:367:    e) Declining to grant rights under trademark law for use of some
./LICENSE:368:    trade names, trademarks, or service marks; or
./LICENSE:372:    it) with contractual assumptions of liability to the recipient, for
./LICENSE:373:    any liability that these contractual assumptions directly impose on
./LICENSE:380:restriction, you may remove that term.  If a license document contains
./LICENSE:383:of that license document, provided that the further restriction does
./LICENSE:392:form of a separately written license, or stated as exceptions;
./LICENSE:400:this License (including any patent licenses granted under the third
./LICENSE:404:license from a particular copyright holder is reinstated (a)
./LICENSE:405:provisionally, unless and until the copyright holder explicitly and
./LICENSE:406:finally terminates your license, and (b) permanently, if the copyright
./LICENSE:410:  Moreover, your license from a particular copyright holder is
./LICENSE:411:reinstated permanently if the copyright holder notifies you of the
./LICENSE:414:copyright holder, and you cure the violation prior to 30 days after
./LICENSE:418:licenses of parties who have received copies or rights from you under
./LICENSE:420:reinstated, you do not qualify to receive new licenses for the same
./LICENSE:429:nothing other than this License grants you permission to propagate or
./LICENSE:430:modify any covered work.  These actions infringe copyright if you do
./LICENSE:437:receives a license from the original licensors, to run, modify and
./LICENSE:446:licenses to the work the party's predecessor in interest had or could
./LICENSE:453:not impose a license fee, royalty, or other charge for exercise of
./LICENSE:461:  A "contributor" is a copyright holder who authorizes use under this
./LICENSE:463:work thus licensed is called the contributor's "contributor version".
./LICENSE:472:patent sublicenses in a manner consistent with the requirements of
./LICENSE:476:patent license under the contributor's essential patent claims, to
./LICENSE:480:  In the following three paragraphs, a "patent license" is any express
./LICENSE:482:(such as an express permission to practice a patent or covenant not to
./LICENSE:483:sue for patent infringement).  To "grant" such a patent license to a
./LICENSE:487:  If you convey a covered work, knowingly relying on a patent license,
./LICENSE:493:patent license for this particular work, or (3) arrange, in a manner
./LICENSE:495:license to downstream recipients.  "Knowingly relying" means you have
./LICENSE:496:actual knowledge that, but for the patent license, your conveying the
./LICENSE:503:covered work, and grant a patent license to some of the parties
./LICENSE:505:or convey a specific copy of the covered work, then the patent license
./LICENSE:509:  A patent license is "discriminatory" if it does not include within
./LICENSE:518:patent license (a) in connection with copies of the covered work
./LICENSE:522:or that patent license was granted, prior to 28 March 2007.
./LICENSE:525:any implied license or other defenses to infringement that may
./LICENSE:554:permission to link or combine any covered work with a work licensed
./LICENSE:582:  Later license versions may give you additional or different
./LICENSE:583:permissions.  However, no additional obligations are imposed on any
./LICENSE:584:author or copyright holder as a result of your choosing to follow a
./LICENSE:589:  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
./LICENSE:592:OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
./LICENSE:602:THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
./LICENSE:604:USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
./LICENSE:612:  If the disclaimer of warranty and limitation of liability provided
./LICENSE:615:an absolute waiver of all civil liability in connection with the
./LICENSE:616:Program, unless a warranty or assumption of liability accompanies a
./LICENSE:625:free software which everyone can redistribute and change under these terms.
./LICENSE:629:state the exclusion of warranty; and each file should have at least
./LICENSE:630:the "copyright" line and a pointer to where the full notice is found.
./LICENSE:635:    This program is free software: you can redistribute it and/or modify
./LICENSE:641:    but WITHOUT ANY WARRANTY; without even the implied warranty of
./LICENSE:646:    along with this program.  If not, see <https://www.gnu.org/licenses/>.
./LICENSE:659:if any, to sign a "copyright disclaimer" for the program, if necessary.
./LICENSE:660:For more information on this, and how to apply and follow the GNU AGPL, see
./LICENSE:661:<https://www.gnu.org/licenses/>.
./backend/app/api/simulation.py:2032:                LIMIT ? OFFSET ?
./backend/app/api/simulation.py:2107:                    LIMIT ? OFFSET ?
./backend/app/api/simulation.py:2113:                    LIMIT ? OFFSET ?
./backend/app/services/report_agent.py:818:REACT_TOOL_LIMIT_MSG = (
./backend/app/services/report_agent.py:1411:                        "content": REACT_TOOL_LIMIT_MSG.format(
./backend/app/services/simulation_runner.py:1684:                    LIMIT ?
./backend/app/services/simulation_runner.py:1692:                    LIMIT ?
./backend/pyproject.toml:6:license = { text = "AGPL-3.0" }
./backend/scripts/run_reddit_simulation.py:323:                LIMIT 1
./backend/scripts/run_parallel_simulation.py:540:                LIMIT 1
./backend/scripts/run_twitter_simulation.py:323:                LIMIT 1
./package-lock.json:10:      "license": "AGPL-3.0",
./package-lock.json:23:      "license": "MIT",
./package-lock.json:33:      "license": "MIT",
./package-lock.json:49:      "license": "MIT",
./package-lock.json:66:      "license": "MIT",
./package-lock.json:79:      "license": "ISC",
./package-lock.json:94:      "license": "MIT",
./package-lock.json:107:      "license": "MIT"
./package-lock.json:114:      "license": "MIT",
./package-lock.json:139:      "license": "MIT"
./package-lock.json:146:      "license": "MIT",
./package-lock.json:156:      "license": "ISC",
./package-lock.json:166:      "license": "MIT",
./package-lock.json:176:      "license": "MIT",
./package-lock.json:186:      "license": "MIT",
./package-lock.json:196:      "license": "Apache-2.0",
./package-lock.json:206:      "license": "MIT",
./package-lock.json:219:      "license": "MIT",
./package-lock.json:234:      "license": "MIT",
./package-lock.json:247:      "license": "MIT",
./package-lock.json:263:      "license": "MIT",
./package-lock.json:273:      "license": "0BSD"
./package-lock.json:280:      "license": "MIT",
./package-lock.json:298:      "license": "ISC",
./package-lock.json:308:      "license": "MIT",
./package-lock.json:327:      "license": "ISC",
./package.json:20:  "license": "AGPL-3.0"
./.github/workflows/docker-image.yml:8:permissions:
```

## 8. Agent / Swarm / Simulation / Graph 关键词扫描

```text
./locales/zh.json:40:    "heroDesc": "即使只有一段文字，{brand} 也能基于其中的现实种子，全自动生成与之对应的至多{agentScale}构成的平行世界。通过上帝视角注入变量，在复杂的群体交互中寻找动态环境下的{optimalSolution}",
./locales/zh.json:42:    "heroDescAgentScale": "百万级Agent",
./locales/zh.json:44:    "slogan": "让未来在 Agent 群中预演，让决策在百战后胜出",
./locales/zh.json:51:    "metricHighAvailDesc": "最多百万级Agent模拟",
./locales/zh.json:54:    "step01Desc": "现实种子提取 & 个体与群体记忆注入 & GraphRAG构建",
./locales/zh.json:56:    "step02Desc": "实体关系抽取 & 人设生成 & 环境配置Agent注入仿真参数",
./locales/zh.json:60:    "step04Desc": "ReportAgent拥有丰富的工具集与模拟后环境进行深度交互",
./locales/zh.json:62:    "step05Desc": "与模拟世界中的任意一位进行对话 & 与ReportAgent进行对话",
./locales/zh.json:68:    "simulationPrompt": ">_ 02 / 模拟提示词",
./locales/zh.json:75:    "layoutGraph": "图谱",
./locales/zh.json:87:    "graphRagBuild": "GraphRAG构建",
./locales/zh.json:88:    "graphRagDesc": "基于生成的本体，将文档自动分块后调用 Zep 构建知识图谱，提取实体和关系，并形成时序记忆与社区摘要",
./locales/zh.json:97:    "createSimulationFailed": "创建模拟失败: {error}",
./locales/zh.json:98:    "createSimulationException": "创建模拟异常: {error}"
./locales/zh.json:102:    "simInstanceDesc": "新建simulation实例，拉取模拟世界参数模版",
./locales/zh.json:104:    "generateAgentPersona": "生成 Agent 人设",
./locales/zh.json:105:    "generateAgentPersonaDesc": "结合上下文，自动调用工具从知识图谱梳理实体与关系，初始化模拟个体，并基于现实种子赋予他们独特的行为与记忆",
./locales/zh.json:106:    "currentAgentCount": "当前Agent数",
./locales/zh.json:107:    "expectedAgentTotal": "预期Agent总数",
./locales/zh.json:109:    "generatedAgentPersonas": "已生成的 Agent 人设",
./locales/zh.json:114:    "simulationDuration": "模拟时长",
./locales/zh.json:122:    "agentConfig": "Agent 配置",
./locales/zh.json:151:    "estimatedDuration": "若Agent规模为100：预计耗时约 {minutes} 分钟",
./locales/zh.json:152:    "estimatedDurationFull": "若Agent规模为100：预计耗时 {minutes} 分钟",
./locales/zh.json:155:    "backToGraphBuild": "返回图谱构建",
./locales/zh.json:164:    "personaDimExperience": "事件全景经历",
./locales/zh.json:165:    "personaDimExperienceDesc": "在此事件中的完整行为轨迹",
./locales/zh.json:166:    "personaDimBehavior": "行为模式侧写",
./locales/zh.json:167:    "personaDimBehaviorDesc": "经验总结与行事风格偏好",
./locales/zh.json:168:    "personaDimMemory": "独特记忆印记",
./locales/zh.json:169:    "personaDimMemoryDesc": "基于现实种子形成的记忆",
./locales/zh.json:170:    "personaDimSocial": "社会关系网络",
./locales/zh.json:171:    "personaDimSocialDesc": "个体链接与交互图谱",
./locales/zh.json:182:    "waitingForActions": "Waiting for agent actions...",
./locales/zh.json:183:    "errorMissingSimId": "错误：缺少 simulationId",
./locales/zh.json:185:    "graphMemoryUpdateEnabled": "已开启动态图谱更新模式",
./locales/zh.json:197:    "graphRealtimeRefresh": "开启图谱实时刷新 (30s)",
./locales/zh.json:198:    "graphRefreshStopped": "停止图谱实时刷新",
./locales/zh.json:213:    "waitingForReportAgent": "Waiting for Report Agent...",
./locales/zh.json:217:    "scenarioLabel": "预测场景: ",
./locales/zh.json:249:    "world1": "世界1",
./locales/zh.json:250:    "world2": "世界2"
./locales/zh.json:254:    "agentsAvailable": "{count} agents available",
./locales/zh.json:255:    "chatWithReportAgent": "与Report Agent对话",
./locales/zh.json:256:    "chatWithAgent": "与世界中任意个体对话",
./locales/zh.json:259:    "reportAgentChat": "Report Agent - Chat",
./locales/zh.json:260:    "reportAgentDesc": "报告生成智能体的快速对话版本，可调用 4 种专业工具，拥有MiroFish的完整记忆",
./locales/zh.json:266:    "toolQuickSearchDesc": "基于 GraphRAG 的即时查询接口，优化索引效率，用于快速提取具体的节点属性与离散事实",
./locales/zh.json:267:    "toolInterviewSubAgent": "InterviewSubAgent 虚拟访谈",
./locales/zh.json:268:    "toolInterviewSubAgentDesc": "自主式访谈，能够并行与模拟世界中个体进行多轮对话，采集非结构化的观点数据与心理状态",
./locales/zh.json:270:    "chatEmptyReportAgent": "与 Report Agent 对话，深入了解报告内容",
./locales/zh.json:271:    "chatEmptyAgent": "与模拟个体对话，了解他们的观点",
./locales/zh.json:285:    "selectAgentFirst": "请先选择一个模拟个体"
./locales/zh.json:287:  "graph": {
./locales/zh.json:288:    "panelTitle": "Graph Relationship Visualization",
./locales/zh.json:289:    "refreshGraph": "刷新图谱",
./locales/zh.json:290:    "graphMemoryRealtime": "GraphRAG长短期记忆实时更新中",
./locales/zh.json:293:    "nodeDetails": "Node Details",
./locales/zh.json:294:    "relationship": "Relationship",
./locales/zh.json:295:    "graphDataLoading": "图谱数据加载中...",
./locales/zh.json:302:    "graphBuild": "图谱构建",
./locales/zh.json:318:    "untitledSimulation": "未命名模拟",
./locales/zh.json:326:    "requireSimulationRequirement": "请提供模拟需求描述 (simulation_requirement)",
./locales/zh.json:331:    "zepApiKeyMissing": "ZEP_API_KEY未配置",
./locales/zh.json:333:    "graphBuilding": "图谱正在构建中，请勿重复提交。如需强制重建，请添加 force: true",
./locales/zh.json:336:    "graphBuildStarted": "图谱构建任务已启动，请通过 /task/{taskId} 查询进度",
./locales/zh.json:337:    "graphBuildComplete": "图谱构建完成",
./locales/zh.json:340:    "graphDeleted": "图谱已删除: {id}",
./locales/zh.json:342:    "graphNotBuilt": "项目尚未构建图谱，请先调用 /api/graph/build",
./locales/zh.json:343:    "requireSimulationId": "请提供 simulation_id",
./locales/zh.json:344:    "simulationNotFound": "模拟不存在: {id}",
./locales/zh.json:345:    "projectMissingRequirement": "项目缺少模拟需求描述 (simulation_requirement)",
./locales/zh.json:346:    "prepareStarted": "准备任务已启动，请通过 /api/simulation/prepare/status 查询进度",
./locales/zh.json:348:    "notStartedPrepare": "尚未开始准备，请调用 /api/simulation/prepare 开始",
./locales/zh.json:350:    "requireTaskOrSimId": "请提供 task_id 或 simulation_id",
./locales/zh.json:355:    "requireGraphId": "请提供 graph_id",
./locales/zh.json:362:    "graphIdRequiredForMemory": "启用图谱记忆更新需要有效的 graph_id，请确保项目已构建图谱",
./locales/zh.json:365:    "missingGraphId": "缺少图谱ID",
./locales/zh.json:366:    "missingGraphIdEnsure": "缺少图谱ID，请确保已构建图谱",
./locales/zh.json:368:    "reportAlreadyExists": "报告已存在",
./locales/zh.json:369:    "reportGenerateStarted": "报告生成任务已启动，请通过 /api/report/generate/status 查询进度",
./locales/zh.json:370:    "reportGenerated": "报告已生成",
./locales/zh.json:371:    "reportNotFound": "报告不存在: {id}",
./locales/zh.json:373:    "reportDeleted": "报告已删除: {id}",
./locales/zh.json:374:    "reportGenerateFailed": "报告生成失败",
./locales/zh.json:376:    "reportProgressNotAvail": "报告不存在或进度信息不可用: {id}",
./locales/zh.json:377:    "requireAgentId": "请提供 agent_id",
./locales/zh.json:383:    "interviewListMissingAgentId": "采访列表第{index}项缺少 agent_id",
./locales/zh.json:390:    "requireGraphIdAndQuery": "请提供 graph_id 和 query",
./locales/zh.json:391:    "initReportAgent": "初始化Report Agent..."
./locales/zh.json:394:    "initGraphService": "初始化图谱构建服务...",
./locales/zh.json:396:    "creatingZepGraph": "创建Zep图谱...",
./locales/zh.json:400:    "fetchingGraphData": "获取图谱数据...",
./locales/zh.json:401:    "graphBuildComplete": "图谱构建完成",
./locales/zh.json:403:    "startBuildingGraph": "开始构建图谱...",
./locales/zh.json:404:    "graphCreated": "图谱已创建: {graphId}",
./locales/zh.json:407:    "fetchingGraphInfo": "获取图谱信息...",
./locales/zh.json:413:    "zepProcessing": "Zep处理中... {completed}/{total} 完成, {pending} 待处理 ({elapsed}秒)",
./locales/zh.json:418:    "connectingZepGraph": "正在连接Zep图谱...",
./locales/zh.json:433:    "reportComplete": "报告生成完成",
./locales/zh.json:434:    "reportFailed": "报告生成失败: {error}",
./locales/zh.json:442:    "generatingAgentConfig": "生成Agent配置 ({start}-{end}/{total})...",
./locales/zh.json:444:    "zepSearchQuery": "关于{name}的所有信息、活动、事件、关系和背景",
./locales/zh.json:447:    "agentConfigResult": "Agent配置: 成功生成 {count} 个",
./locales/zh.json:450:    "readingGraphEntities": "读取图谱实体",
./locales/zh.json:451:    "generatingProfiles": "生成Agent人设",
./locales/zh.json:473:    "graphDataLoadSuccess": "图谱数据加载成功",
./locales/zh.json:474:    "graphLoadFailed": "图谱加载失败: {error}",
./locales/zh.json:475:    "graphRealtimeRefreshStart": "开启图谱实时刷新 (30s)",
./locales/zh.json:476:    "graphRealtimeRefreshStop": "停止图谱实时刷新",
./locales/zh.json:477:    "simRunViewInit": "SimulationRunView 初始化",
./locales/zh.json:488:    "simViewInit": "SimulationView 初始化",
./locales/zh.json:489:    "errorMissingSimId": "错误：缺少 simulationId",
./locales/zh.json:495:    "zepEntitiesFound": "从Zep图谱读取到 {count} 个实体",
./locales/zh.json:503:    "generatingAgentProfileConfig": "正在生成Agent人设配置...",
./locales/zh.json:506:    "configSummaryAgents": "  ├─ Agent数量: {count}个",
./locales/zh.json:516:    "startGeneratingAgentProfiles": "开始生成Agent人设...",
./locales/zh.json:517:    "agentProfile": "→ Agent人设 {current}/{total}: {name} ({profession})",
./locales/zh.json:518:    "allProfilesComplete": "✓ 全部 {count} 个Agent人设生成完成",
./locales/zh.json:520:    "loadedAgentProfiles": "已加载 {count} 个Agent人设",
./locales/zh.json:529:    "graphMemoryUpdateEnabled": "已开启动态图谱更新模式",
./locales/zh.json:540:    "reportRequestSent": "报告生成请求已发送，请稍候...",
./locales/zh.json:542:    "reportGenTaskStarted": "✓ 报告生成任务已启动: {reportId}",
./locales/zh.json:543:    "reportGenFailed": "✗ 启动报告生成失败: {error}",
./locales/zh.json:544:    "reportGenException": "✗ 启动报告生成异常: {error}",
./locales/zh.json:548:    "sendToReportAgent": "向 Report Agent 发送: {message}...",
./locales/zh.json:549:    "reportAgentReplied": "Report Agent 已回复",
./locales/zh.json:550:    "sendToAgent": "向 {name} 发送: {message}...",
./locales/zh.json:551:    "agentReplied": "{name} 已回复",
./locales/zh.json:557:    "reportDataLoaded": "报告数据加载完成",
./locales/zh.json:562:    "reportViewInit": "ReportView 初始化",
./locales/zh.json:568:  "report": {
./locales/zh.json:580:    "reportComplete": "报告生成完成",
./locales/zh.json:582:    "agentInitDone": "ReportAgent 初始化完成: graph_id={graphId}, simulation_id={simulationId}",
./locales/zh.json:598:    "outlineSavedToFile": "大纲已保存到文件: {reportId}/outline.json",
./locales/zh.json:599:    "sectionSaved": "章节已保存: {reportId}/section_{sectionNum}.md",
./locales/zh.json:600:    "reportGenDone": "报告生成完成: {reportId}",
./locales/zh.json:601:    "reportGenFailed": "报告生成失败: {error}",
./locales/zh.json:602:    "agentChat": "Report Agent对话: {message}...",
./locales/zh.json:604:    "outlineSaved": "大纲已保存: {reportId}",
./locales/zh.json:605:    "sectionFileSaved": "章节已保存: {reportId}/{fileSuffix}",
./locales/zh.json:606:    "fullReportAssembled": "完整报告已组装: {reportId}",
./locales/zh.json:607:    "reportSaved": "报告已保存: {reportId}",
./locales/zh.json:608:    "reportFolderDeleted": "报告文件夹已删除: {reportId}",
./locales/zh.json:609:    "redirectToQuickSearch": "search_graph 已重定向到 quick_search",
./locales/zh.json:610:    "redirectToInsightForge": "get_simulation_context 已重定向到 insight_forge"
./locales/zh.json:613:    "zepToolsInitialized": "ZepToolsService 初始化完成",
./locales/zh.json:614:    "zepRetryAttempt": "Zep {operation} 第 {attempt} 次尝试失败: {error}, {delay}秒后重试...",
./locales/zh.json:615:    "zepAllRetriesFailed": "Zep {operation} 在 {retries} 次尝试后仍失败: {error}",
./locales/zh.json:616:    "graphSearch": "图谱搜索: graph_id={graphId}, query={query}...",
./locales/zh.json:617:    "graphSearchOp": "图谱搜索(graph={graphId})",
./locales/zh.json:619:    "zepSearchApiFallback": "Zep Search API失败，降级为本地搜索: {error}",
./locales/zh.json:623:    "fetchingAllNodes": "获取图谱 {graphId} 的所有节点...",
./locales/zh.json:625:    "fetchingAllEdges": "获取图谱 {graphId} 的所有边...",
./locales/zh.json:636:    "fetchingGraphStats": "获取图谱 {graphId} 的统计信息...",
./locales/zh.json:640:    "insightForgeComplete": "InsightForge完成: {facts}条事实, {entities}个实体, {relationships}条关系",
./locales/zh.json:646:    "interviewAgentsStart": "InterviewAgents 深度采访（真实API）: {requirement}...",
./locales/zh.json:648:    "loadedProfiles": "加载到 {count} 个Agent人设",
./locales/zh.json:649:    "selectedAgentsForInterview": "选择了 {count} 个Agent进行采访: {indices}",
./locales/zh.json:651:    "callingBatchInterviewApi": "调用批量采访API（双平台）: {count} 个Agent",
./locales/zh.json:656:    "interviewAgentsComplete": "InterviewAgents完成: 采访了 {count} 个Agent（双平台）",
./locales/zh.json:661:    "llmSelectAgentFailed": "LLM选择Agent失败，使用默认选择: {error}",
./locales/en.json:30:    "description": "MiroFish - Social Media Opinion Simulation System"
./locales/en.json:36:    "tagline": "Concise & Universal Swarm Intelligence Engine",
./locales/en.json:40:    "heroDesc": "From a single document, {brand} extracts reality seeds to auto-generate a parallel world with up to {agentScale}. Inject variables from a god's-eye view to find the {optimalSolution} in complex group dynamics.",
./locales/en.json:42:    "heroDescAgentScale": "million-scale Agents",
./locales/en.json:44:    "slogan": "Let Agents rehearse the future, let decisions prevail",
./locales/en.json:47:    "systemReadyDesc": "Prediction engine on standby. Upload unstructured data to initialize a simulation sequence.",
./locales/en.json:51:    "metricHighAvailDesc": "Millions of Agents",
./locales/en.json:53:    "step01Title": "Graph Build",
./locales/en.json:54:    "step01Desc": "Seed extraction & memory injection & GraphRAG construction",
./locales/en.json:56:    "step02Desc": "Entity extraction & persona generation & Agent config injection",
./locales/en.json:57:    "step03Title": "Simulation",
./locales/en.json:58:    "step03Desc": "Dual-platform parallel sim & auto-parse requirements & temporal memory",
./locales/en.json:60:    "step04Desc": "ReportAgent interacts with the post-simulation environment via rich tools",
./locales/en.json:62:    "step05Desc": "Chat with any simulated individual & converse with ReportAgent",
./locales/en.json:68:    "simulationPrompt": ">_ 02 / Simulation Prompt",
./locales/en.json:69:    "promptPlaceholder": "// Describe your simulation or prediction requirement in natural language",
./locales/en.json:75:    "layoutGraph": "Graph",
./locales/en.json:78:    "stepNames": ["Graph Build", "Env Setup", "Run Simulation", "Report Generation", "Deep Interaction"]
./locales/en.json:85:    "ontologyDesc": "LLM analyzes document content and simulation requirements, extracts reality seeds, and auto-generates a suitable ontology structure",
./locales/en.json:87:    "graphRagBuild": "GraphRAG Build",
./locales/en.json:88:    "graphRagDesc": "Based on the generated ontology, documents are auto-chunked and sent to Zep to build a knowledge graph, extracting entities and relations, forming temporal memory and community summaries",
./locales/en.json:93:    "buildCompleteDesc": "Graph build is complete. Proceed to the next step for simulation environment setup.",
./locales/en.json:97:    "createSimulationFailed": "Failed to create simulation: {error}",
./locales/en.json:98:    "createSimulationException": "Simulation creation error: {error}"
./locales/en.json:101:    "simInstanceInit": "Simulation Instance Initialization",
./locales/en.json:102:    "simInstanceDesc": "Create a new simulation instance and pull world parameter templates",
./locales/en.json:104:    "generateAgentPersona": "Generate Agent Personas",
./locales/en.json:105:    "generateAgentPersonaDesc": "Combine context to auto-extract entities and relations from the knowledge graph, initialize simulated individuals, and assign unique behaviors and memories based on reality seeds",
./locales/en.json:106:    "currentAgentCount": "Current Agents",
./locales/en.json:107:    "expectedAgentTotal": "Expected Total Agents",
./locales/en.json:109:    "generatedAgentPersonas": "Generated Agent Personas",
./locales/en.json:113:    "dualPlatformConfigDesc": "LLM intelligently sets world time flow, recommendation algorithms, each individual's active hours, posting frequency, event triggers, and more based on requirements and reality seeds",
./locales/en.json:114:    "simulationDuration": "Simulation Duration",
./locales/en.json:122:    "agentConfig": "Agent Config",
./locales/en.json:140:    "initialActivationDesc": "Auto-generate initial activation events and hot topics based on narrative direction to guide the simulation world's initial state",
./locales/en.json:146:    "setupCompleteDesc": "Simulation environment is ready. You can now start the simulation.",
./locales/en.json:147:    "roundsConfig": "Simulation Rounds Configuration",
./locales/en.json:148:    "roundsConfigDesc": "MiroFish auto-plans to simulate {hours} real-world hours, each round representing {minutesPerRound} minutes of elapsed time",
./locales/en.json:151:    "estimatedDuration": "For 100 Agents: est. ~{minutes} minutes",
./locales/en.json:152:    "estimatedDurationFull": "For 100 Agents: est. {minutes} minutes",
./locales/en.json:155:    "backToGraphBuild": "Back to Graph Build",
./locales/en.json:156:    "startDualWorldSim": "Start Dual-World Parallel Simulation",
./locales/en.json:164:    "personaDimExperience": "Full Event Experience",
./locales/en.json:165:    "personaDimExperienceDesc": "Complete behavioral trajectory in this event",
./locales/en.json:166:    "personaDimBehavior": "Behavioral Profile",
./locales/en.json:167:    "personaDimBehaviorDesc": "Experience summary and behavioral preferences",
./locales/en.json:168:    "personaDimMemory": "Unique Memory Imprint",
./locales/en.json:169:    "personaDimMemoryDesc": "Memories formed from reality seeds",
./locales/en.json:170:    "personaDimSocial": "Social Network",
./locales/en.json:171:    "personaDimSocialDesc": "Individual connections and interaction graph",
./locales/en.json:182:    "waitingForActions": "Waiting for agent actions...",
./locales/en.json:183:    "errorMissingSimId": "Error: missing simulationId",
./locales/en.json:184:    "startingDualSim": "Starting dual-platform parallel simulation...",
./locales/en.json:185:    "graphMemoryUpdateEnabled": "Dynamic graph memory update enabled",
./locales/en.json:186:    "setMaxRounds": "Max simulation rounds set to: {rounds}",
./locales/en.json:187:    "oldSimCleared": "Old simulation logs cleared, restarting simulation",
./locales/en.json:188:    "engineStarted": "Simulation engine started successfully",
./locales/en.json:191:    "stoppingSim": "Stopping simulation...",
./locales/en.json:192:    "simStopped": "Simulation stopped",
./locales/en.json:195:    "allPlatformsCompleted": "All platform simulations have ended",
./locales/en.json:196:    "simCompleted": "Simulation completed",
./locales/en.json:197:    "graphRealtimeRefresh": "Graph real-time refresh enabled (30s)",
./locales/en.json:198:    "graphRefreshStopped": "Graph real-time refresh stopped",
./locales/en.json:199:    "preparingGoBack": "Preparing to return to Step 2, closing simulation...",
./locales/en.json:200:    "closingSimEnv": "Closing simulation environment...",
./locales/en.json:201:    "simEnvClosed": "Simulation environment closed",
./locales/en.json:202:    "closeFailed": "Failed to close simulation environment, attempting force stop...",
./locales/en.json:203:    "stoppingProcess": "Stopping simulation process...",
./locales/en.json:204:    "checkStatusFailed": "Failed to check simulation status: {error}",
./locales/en.json:205:    "forceStopSuccess": "Simulation force stopped",
./locales/en.json:213:    "waitingForReportAgent": "Waiting for Report Agent...",
./locales/en.json:217:    "scenarioLabel": "Scenario: ",
./locales/en.json:222:    "panelKeyFacts": "Latest key facts from temporal memory",
./locales/en.json:249:    "world1": "World 1",
./locales/en.json:250:    "world2": "World 2"
./locales/en.json:254:    "agentsAvailable": "{count} agents available",
./locales/en.json:255:    "chatWithReportAgent": "Chat with Report Agent",
./locales/en.json:256:    "chatWithAgent": "Chat with any individual in the world",
./locales/en.json:258:    "sendSurvey": "Send survey to the world",
./locales/en.json:259:    "reportAgentChat": "Report Agent - Chat",
./locales/en.json:260:    "reportAgentDesc": "A conversational version of the report generation agent with access to 4 professional tools and MiroFish's complete memory",
./locales/en.json:262:    "toolInsightForgeDesc": "Aligns real-world seed data with simulation state, combining Global/Local Memory for cross-temporal deep attribution analysis",
./locales/en.json:264:    "toolPanoramaSearchDesc": "Graph-based BFS algorithm that reconstructs event propagation paths, capturing the full topology of information flow",
./locales/en.json:266:    "toolQuickSearchDesc": "GraphRAG-based instant query interface with optimized indexing for fast extraction of node attributes and discrete facts",
./locales/en.json:267:    "toolInterviewSubAgent": "InterviewSubAgent Virtual Interview",
./locales/en.json:268:    "toolInterviewSubAgentDesc": "Autonomous interviews that conduct parallel multi-round dialogues with simulated individuals, collecting unstructured opinion data and psychological states",
./locales/en.json:270:    "chatEmptyReportAgent": "Chat with Report Agent to explore report content in depth",
./locales/en.json:271:    "chatEmptyAgent": "Chat with simulated individuals to understand their perspectives",
./locales/en.json:285:    "selectAgentFirst": "Please select a simulated individual first"
./locales/en.json:287:  "graph": {
./locales/en.json:288:    "panelTitle": "Graph Relationship Visualization",
./locales/en.json:289:    "refreshGraph": "Refresh Graph",
./locales/en.json:290:    "graphMemoryRealtime": "GraphRAG short/long-term memory updating in real-time",
./locales/en.json:292:    "pendingContentHint": "Some content is still processing. Consider refreshing the graph manually later.",
./locales/en.json:293:    "nodeDetails": "Node Details",
./locales/en.json:294:    "relationship": "Relationship",
./locales/en.json:295:    "graphDataLoading": "Loading graph data...",
./locales/en.json:301:    "title": "Simulation History",
./locales/en.json:302:    "graphBuild": "Graph Build",
./locales/en.json:308:    "simRequirement": "Simulation Requirement",
./locales/en.json:311:    "replayTitle": "Simulation Replay",
./locales/en.json:312:    "step1Button": "Graph Build",
./locales/en.json:315:    "replayHint": "Step 3 'Run Simulation' and Step 5 'Deep Interaction' must be started during runtime and do not support history replay",
./locales/en.json:318:    "untitledSimulation": "Untitled simulation",
./locales/en.json:326:    "requireSimulationRequirement": "Please provide a simulation requirement (simulation_requirement)",
./locales/en.json:331:    "zepApiKeyMissing": "ZEP_API_KEY not configured",
./locales/en.json:333:    "graphBuilding": "Graph build in progress. Do not resubmit. To force rebuild, add force: true.",
./locales/en.json:336:    "graphBuildStarted": "Graph build task started. Query progress via /task/{taskId}.",
./locales/en.json:337:    "graphBuildComplete": "Graph build complete",
./locales/en.json:340:    "graphDeleted": "Graph deleted: {id}",
./locales/en.json:342:    "graphNotBuilt": "Graph not yet built. Please call /api/graph/build first.",
./locales/en.json:343:    "requireSimulationId": "Please provide simulation_id",
./locales/en.json:344:    "simulationNotFound": "Simulation not found: {id}",
./locales/en.json:345:    "projectMissingRequirement": "Project missing simulation requirement (simulation_requirement)",
./locales/en.json:346:    "prepareStarted": "Preparation task started. Query progress via /api/simulation/prepare/status.",
./locales/en.json:348:    "notStartedPrepare": "Preparation not started. Please call /api/simulation/prepare.",
./locales/en.json:350:    "requireTaskOrSimId": "Please provide task_id or simulation_id",
./locales/en.json:351:    "configNotFound": "Simulation config not found. Please call /prepare first.",
./locales/en.json:355:    "requireGraphId": "Please provide graph_id",
./locales/en.json:360:    "simRunningForceHint": "Simulation is running. Stop it first via /stop, or use force=true to restart.",
./locales/en.json:361:    "simNotReady": "Simulation not ready. Current status: {status}. Please call /prepare first.",
./locales/en.json:362:    "graphIdRequiredForMemory": "Graph memory update requires a valid graph_id. Ensure the graph is built.",
./locales/en.json:363:    "dbNotExist": "Database does not exist. The simulation may not have run yet.",
./locales/en.json:365:    "missingGraphId": "Missing graph ID",
./locales/en.json:366:    "missingGraphIdEnsure": "Missing graph ID. Please ensure the graph has been built.",
./locales/en.json:367:    "missingSimRequirement": "Missing simulation requirement description",
./locales/en.json:368:    "reportAlreadyExists": "Report already exists",
./locales/en.json:369:    "reportGenerateStarted": "Report generation task started. Query progress via /api/report/generate/status.",
./locales/en.json:370:    "reportGenerated": "Report generated",
./locales/en.json:371:    "reportNotFound": "Report not found: {id}",
./locales/en.json:372:    "noReportForSim": "No report found for this simulation: {id}",
./locales/en.json:373:    "reportDeleted": "Report deleted: {id}",
./locales/en.json:374:    "reportGenerateFailed": "Report generation failed",
./locales/en.json:376:    "reportProgressNotAvail": "Report not found or progress unavailable: {id}",
./locales/en.json:377:    "requireAgentId": "Please provide agent_id",
./locales/en.json:380:    "envNotRunning": "Simulation environment not running or closed. Ensure simulation is complete and in command-wait mode.",
./locales/en.json:383:    "interviewListMissingAgentId": "Interview list item {index} missing agent_id",
./locales/en.json:390:    "requireGraphIdAndQuery": "Please provide graph_id and query",
./locales/en.json:391:    "initReportAgent": "Initializing Report Agent..."
./locales/en.json:394:    "initGraphService": "Initializing graph build service...",
./locales/en.json:396:    "creatingZepGraph": "Creating Zep graph...",
./locales/en.json:400:    "fetchingGraphData": "Fetching graph data...",
./locales/en.json:401:    "graphBuildComplete": "Graph build complete",
./locales/en.json:403:    "startBuildingGraph": "Starting graph build...",
./locales/en.json:404:    "graphCreated": "Graph created: {graphId}",
./locales/en.json:407:    "fetchingGraphInfo": "Fetching graph info...",
./locales/en.json:413:    "zepProcessing": "Zep processing... {completed}/{total} done, {pending} pending ({elapsed}s)",
./locales/en.json:417:    "startPreparingEnv": "Preparing simulation environment...",
./locales/en.json:418:    "connectingZepGraph": "Connecting to Zep graph...",
./locales/en.json:419:    "readingNodeData": "Reading node data...",
./locales/en.json:422:    "analyzingRequirements": "Analyzing simulation requirements...",
./locales/en.json:423:    "generatingOutline": "Generating report outline...",
./locales/en.json:427:    "initReport": "Initializing report...",
./locales/en.json:428:    "startPlanningOutline": "Planning report outline...",
./locales/en.json:432:    "assemblingReport": "Assembling full report...",
./locales/en.json:433:    "reportComplete": "Report generation complete",
./locales/en.json:434:    "reportFailed": "Report generation failed: {error}",
./locales/en.json:442:    "generatingAgentConfig": "Generating agent config ({start}-{end}/{total})...",
./locales/en.json:444:    "zepSearchQuery": "All information, activities, events, relationships and background about {name}",
./locales/en.json:447:    "agentConfigResult": "Agent Config: {count} generated",
./locales/en.json:450:    "readingGraphEntities": "Reading Graph Entities",
./locales/en.json:451:    "generatingProfiles": "Generating Agent Profiles",
./locales/en.json:452:    "generatingSimConfig": "Generating Simulation Config",
./locales/en.json:456:    "preparingGoBack": "Preparing to return to Step 2, closing simulation...",
./locales/en.json:457:    "closingSimEnv": "Closing simulation environment...",
./locales/en.json:458:    "simEnvClosed": "✓ Simulation environment closed",
./locales/en.json:459:    "closeSimEnvFailed": "Failed to close simulation environment, attempting force stop...",
./locales/en.json:460:    "simForceStopSuccess": "✓ Simulation force stopped",
./locales/en.json:462:    "stoppingSimProcess": "Stopping simulation process...",
./locales/en.json:463:    "simStopped": "✓ Simulation stopped",
./locales/en.json:464:    "stopSimFailed": "Failed to stop simulation: {error}",
./locales/en.json:465:    "checkStatusFailed": "Failed to check simulation status: {error}",
./locales/en.json:467:    "loadingSimData": "Loading simulation data: {id}",
./locales/en.json:471:    "loadSimDataFailed": "Failed to load simulation data: {error}",
./locales/en.json:473:    "graphDataLoadSuccess": "Graph data loaded successfully",
./locales/en.json:474:    "graphLoadFailed": "Graph load failed: {error}",
./locales/en.json:475:    "graphRealtimeRefreshStart": "Graph real-time refresh enabled (30s)",
./locales/en.json:476:    "graphRealtimeRefreshStop": "Graph real-time refresh stopped",
./locales/en.json:477:    "simRunViewInit": "SimulationRunView initialized",
./locales/en.json:478:    "customRounds": "Custom simulation rounds: {rounds}",
./locales/en.json:479:    "enterStep3": "Entering Step 3: Run Simulation",
./locales/en.json:480:    "customRoundsConfig": "Custom simulation rounds: {rounds} rounds",
./locales/en.json:481:    "useAutoRounds": "Using auto-configured simulation rounds",
./locales/en.json:482:    "detectedSimEnvRunning": "Detected running simulation environment, closing...",
./locales/en.json:483:    "closeSimEnvFailedWithError": "Failed to close simulation environment: {error}",
./locales/en.json:484:    "closeSimEnvException": "Simulation environment close error: {error}",
./locales/en.json:485:    "detectedSimRunning": "Detected simulation is running, stopping...",
./locales/en.json:486:    "forceStopSimFailed": "Force stop simulation failed: {error}",
./locales/en.json:487:    "forceStopSimException": "Force stop simulation error: {error}",
./locales/en.json:488:    "simViewInit": "SimulationView initialized",
./locales/en.json:489:    "errorMissingSimId": "Error: missing simulationId",
./locales/en.json:490:    "simInstanceCreated": "Simulation instance created: {id}",
./locales/en.json:491:    "preparingSimEnv": "Preparing simulation environment...",
./locales/en.json:495:    "zepEntitiesFound": "Found {count} entities from Zep graph",
./locales/en.json:502:    "startGeneratingConfig": "Generating dual-platform simulation config...",
./locales/en.json:503:    "generatingAgentProfileConfig": "Generating agent persona config...",
./locales/en.json:504:    "generatingLLMConfig": "Calling LLM to generate simulation config parameters...",
./locales/en.json:505:    "configComplete": "✓ Simulation config generated",
./locales/en.json:506:    "configSummaryAgents": "  ├─ Agents: {count}",
./locales/en.json:513:    "envSetupComplete": "✓ Environment setup complete, ready to simulate",
./locales/en.json:514:    "startSimCustomRounds": "Starting simulation, custom rounds: {rounds}",
./locales/en.json:515:    "startSimAutoRounds": "Starting simulation, auto-configured rounds: {rounds}",
./locales/en.json:516:    "startGeneratingAgentProfiles": "Generating agent personas...",
./locales/en.json:517:    "agentProfile": "→ Agent persona {current}/{total}: {name} ({profession})",
./locales/en.json:518:    "allProfilesComplete": "✓ All {count} agent personas generated",
./locales/en.json:520:    "loadedAgentProfiles": "Loaded {count} agent personas",
./locales/en.json:521:    "configLoadSuccess": "✓ Simulation config loaded",
./locales/en.json:525:    "step2Init": "Step 2 environment setup initialized",
./locales/en.json:526:    "step3Init": "Step 3 simulation run initialized",
./locales/en.json:527:    "startingDualSim": "Starting dual-platform parallel simulation...",
./locales/en.json:528:    "setMaxRounds": "Max simulation rounds set to: {rounds}",
./locales/en.json:529:    "graphMemoryUpdateEnabled": "Dynamic graph memory update enabled",
./locales/en.json:530:    "oldSimCleared": "✓ Old simulation logs cleared, restarting simulation",
./locales/en.json:531:    "engineStarted": "✓ Simulation engine started successfully",
./locales/en.json:534:    "stoppingSim": "Stopping simulation...",
./locales/en.json:535:    "simStoppedSuccess": "✓ Simulation stopped",
./locales/en.json:538:    "allPlatformsCompleted": "✓ All platform simulations have ended",
./locales/en.json:539:    "simCompleted": "✓ Simulation completed",
./locales/en.json:540:    "reportRequestSent": "Report generation request sent, please wait...",
./locales/en.json:541:    "startingReportGen": "Starting report generation...",
./locales/en.json:542:    "reportGenTaskStarted": "✓ Report generation task started: {reportId}",
./locales/en.json:543:    "reportGenFailed": "✗ Failed to start report generation: {error}",
./locales/en.json:544:    "reportGenException": "✗ Report generation error: {error}",
./locales/en.json:548:    "sendToReportAgent": "Sent to Report Agent: {message}...",
./locales/en.json:549:    "reportAgentReplied": "Report Agent replied",
./locales/en.json:550:    "sendToAgent": "Sent to {name}: {message}...",
./locales/en.json:551:    "agentReplied": "{name} replied",
./locales/en.json:555:    "loadReportData": "Loading report data: {id}",
./locales/en.json:556:    "loadReportFailed": "Failed to load report: {error}",
./locales/en.json:557:    "reportDataLoaded": "Report data loaded",
./locales/en.json:558:    "loadReportLogFailed": "Failed to load report logs: {error}",
./locales/en.json:559:    "loadedProfiles": "Loaded {count} simulated individuals",
./locales/en.json:560:    "loadProfilesFailed": "Failed to load simulated individuals: {error}",
./locales/en.json:562:    "reportViewInit": "ReportView initialized",
./locales/en.json:563:    "getReportInfoFailed": "Failed to get report info: {error}",
./locales/en.json:566:    "customSimRounds": "Custom simulation rounds: {rounds} rounds"
./locales/en.json:568:  "report": {
./locales/en.json:570:    "planningStart": "Starting report outline planning",
./locales/en.json:571:    "fetchSimContext": "Fetching simulation context",
./locales/en.json:580:    "reportComplete": "Report generation complete",
./locales/en.json:582:    "agentInitDone": "ReportAgent initialized: graph_id={graphId}, simulation_id={simulationId}",
./locales/en.json:585:    "startPlanningOutline": "Starting report outline planning...",
./locales/en.json:598:    "outlineSavedToFile": "Outline saved to file: {reportId}/outline.json",
./locales/en.json:599:    "sectionSaved": "Section saved: {reportId}/section_{sectionNum}.md",
./locales/en.json:600:    "reportGenDone": "Report generation complete: {reportId}",
./locales/en.json:601:    "reportGenFailed": "Report generation failed: {error}",
./locales/en.json:602:    "agentChat": "Report Agent chat: {message}...",
./locales/en.json:603:    "fetchReportFailed": "Failed to fetch report content: {error}",
./locales/en.json:604:    "outlineSaved": "Outline saved: {reportId}",
./locales/en.json:605:    "sectionFileSaved": "Section saved: {reportId}/{fileSuffix}",
./locales/en.json:606:    "fullReportAssembled": "Full report assembled: {reportId}",
./locales/en.json:607:    "reportSaved": "Report saved: {reportId}",
./locales/en.json:608:    "reportFolderDeleted": "Report folder deleted: {reportId}",
./locales/en.json:609:    "redirectToQuickSearch": "search_graph redirected to quick_search",
./locales/en.json:610:    "redirectToInsightForge": "get_simulation_context redirected to insight_forge"
./locales/en.json:613:    "zepToolsInitialized": "ZepToolsService initialized",
./locales/en.json:614:    "zepRetryAttempt": "Zep {operation} attempt {attempt} failed: {error}, retrying in {delay}s...",
./locales/en.json:615:    "zepAllRetriesFailed": "Zep {operation} failed after {retries} attempts: {error}",
./locales/en.json:616:    "graphSearch": "Graph search: graph_id={graphId}, query={query}...",
./locales/en.json:617:    "graphSearchOp": "Graph search (graph={graphId})",
./locales/en.json:619:    "zepSearchApiFallback": "Zep Search API failed, falling back to local search: {error}",
./locales/en.json:623:    "fetchingAllNodes": "Fetching all nodes for graph {graphId}...",
./locales/en.json:624:    "fetchedNodes": "Fetched {count} nodes",
./locales/en.json:625:    "fetchingAllEdges": "Fetching all edges for graph {graphId}...",
./locales/en.json:626:    "fetchedEdges": "Fetched {count} edges",
./locales/en.json:627:    "fetchingNodeDetail": "Fetching node detail: {uuid}...",
./locales/en.json:628:    "fetchNodeDetailOp": "Fetch node detail (uuid={uuid}...)",
./locales/en.json:629:    "fetchNodeDetailFailed": "Failed to fetch node detail: {error}",
./locales/en.json:630:    "fetchingNodeEdges": "Fetching edges for node {uuid}...",
./locales/en.json:631:    "foundNodeEdges": "Found {count} edges related to node",
./locales/en.json:632:    "fetchNodeEdgesFailed": "Failed to fetch node edges: {error}",
./locales/en.json:635:    "fetchingEntitySummary": "Fetching relationship summary for entity {name}...",
./locales/en.json:636:    "fetchingGraphStats": "Fetching statistics for graph {graphId}...",
./locales/en.json:637:    "fetchingSimContext": "Fetching simulation context: {requirement}...",
./locales/en.json:640:    "insightForgeComplete": "InsightForge complete: {facts} facts, {entities} entities, {relationships} relationships",
./locales/en.json:646:    "interviewAgentsStart": "InterviewAgents deep interview (real API): {requirement}...",
./locales/en.json:647:    "profilesNotFound": "Profiles not found for simulation {simId}",
./locales/en.json:648:    "loadedProfiles": "Loaded {count} agent profiles",
./locales/en.json:649:    "selectedAgentsForInterview": "Selected {count} agents for interview: {indices}",
./locales/en.json:651:    "callingBatchInterviewApi": "Calling batch interview API (dual platform): {count} agents",
./locales/en.json:656:    "interviewAgentsComplete": "InterviewAgents complete: interviewed {count} agents (dual platform)",
./locales/en.json:661:    "llmSelectAgentFailed": "LLM agent selection failed, using default selection: {error}",
./frontend/package-lock.json:22:    "node_modules/@babel/helper-string-parser": {
./frontend/package-lock.json:28:        "node": ">=6.9.0"
./frontend/package-lock.json:31:    "node_modules/@babel/helper-validator-identifier": {
./frontend/package-lock.json:37:        "node": ">=6.9.0"
./frontend/package-lock.json:40:    "node_modules/@babel/parser": {
./frontend/package-lock.json:52:        "node": ">=6.0.0"
./frontend/package-lock.json:55:    "node_modules/@babel/types": {
./frontend/package-lock.json:65:        "node": ">=6.9.0"
./frontend/package-lock.json:68:    "node_modules/@esbuild/aix-ppc64": {
./frontend/package-lock.json:82:        "node": ">=18"
./frontend/package-lock.json:85:    "node_modules/@esbuild/android-arm": {
./frontend/package-lock.json:99:        "node": ">=18"
./frontend/package-lock.json:102:    "node_modules/@esbuild/android-arm64": {
./frontend/package-lock.json:116:        "node": ">=18"
./frontend/package-lock.json:119:    "node_modules/@esbuild/android-x64": {
./frontend/package-lock.json:133:        "node": ">=18"
./frontend/package-lock.json:136:    "node_modules/@esbuild/darwin-arm64": {
./frontend/package-lock.json:150:        "node": ">=18"
./frontend/package-lock.json:153:    "node_modules/@esbuild/darwin-x64": {
./frontend/package-lock.json:167:        "node": ">=18"
./frontend/package-lock.json:170:    "node_modules/@esbuild/freebsd-arm64": {
./frontend/package-lock.json:184:        "node": ">=18"
./frontend/package-lock.json:187:    "node_modules/@esbuild/freebsd-x64": {
./frontend/package-lock.json:201:        "node": ">=18"
./frontend/package-lock.json:204:    "node_modules/@esbuild/linux-arm": {
./frontend/package-lock.json:218:        "node": ">=18"
./frontend/package-lock.json:221:    "node_modules/@esbuild/linux-arm64": {
./frontend/package-lock.json:235:        "node": ">=18"
./frontend/package-lock.json:238:    "node_modules/@esbuild/linux-ia32": {
./frontend/package-lock.json:252:        "node": ">=18"
./frontend/package-lock.json:255:    "node_modules/@esbuild/linux-loong64": {
./frontend/package-lock.json:269:        "node": ">=18"
./frontend/package-lock.json:272:    "node_modules/@esbuild/linux-mips64el": {
./frontend/package-lock.json:286:        "node": ">=18"
./frontend/package-lock.json:289:    "node_modules/@esbuild/linux-ppc64": {
./frontend/package-lock.json:303:        "node": ">=18"
./frontend/package-lock.json:306:    "node_modules/@esbuild/linux-riscv64": {
./frontend/package-lock.json:320:        "node": ">=18"
./frontend/package-lock.json:323:    "node_modules/@esbuild/linux-s390x": {
./frontend/package-lock.json:337:        "node": ">=18"
./frontend/package-lock.json:340:    "node_modules/@esbuild/linux-x64": {
./frontend/package-lock.json:354:        "node": ">=18"
./frontend/package-lock.json:357:    "node_modules/@esbuild/netbsd-arm64": {
./frontend/package-lock.json:371:        "node": ">=18"
./frontend/package-lock.json:374:    "node_modules/@esbuild/netbsd-x64": {
./frontend/package-lock.json:388:        "node": ">=18"
./frontend/package-lock.json:391:    "node_modules/@esbuild/openbsd-arm64": {
./frontend/package-lock.json:405:        "node": ">=18"
./frontend/package-lock.json:408:    "node_modules/@esbuild/openbsd-x64": {
./frontend/package-lock.json:422:        "node": ">=18"
./frontend/package-lock.json:425:    "node_modules/@esbuild/openharmony-arm64": {
./frontend/package-lock.json:439:        "node": ">=18"
./frontend/package-lock.json:442:    "node_modules/@esbuild/sunos-x64": {
./frontend/package-lock.json:456:        "node": ">=18"
./frontend/package-lock.json:459:    "node_modules/@esbuild/win32-arm64": {
./frontend/package-lock.json:473:        "node": ">=18"
./frontend/package-lock.json:476:    "node_modules/@esbuild/win32-ia32": {
./frontend/package-lock.json:490:        "node": ">=18"
./frontend/package-lock.json:493:    "node_modules/@esbuild/win32-x64": {
./frontend/package-lock.json:507:        "node": ">=18"
./frontend/package-lock.json:510:    "node_modules/@intlify/core-base": {
./frontend/package-lock.json:521:        "node": ">= 16"
./frontend/package-lock.json:527:    "node_modules/@intlify/devtools-types": {
./frontend/package-lock.json:537:        "node": ">= 16"
./frontend/package-lock.json:543:    "node_modules/@intlify/message-compiler": {
./frontend/package-lock.json:553:        "node": ">= 16"
./frontend/package-lock.json:559:    "node_modules/@intlify/shared": {
./frontend/package-lock.json:565:        "node": ">= 16"
./frontend/package-lock.json:571:    "node_modules/@jridgewell/sourcemap-codec": {
./frontend/package-lock.json:577:    "node_modules/@rolldown/pluginutils": {
./frontend/package-lock.json:584:    "node_modules/@rollup/rollup-android-arm-eabi": {
./frontend/package-lock.json:598:    "node_modules/@rollup/rollup-android-arm64": {
./frontend/package-lock.json:612:    "node_modules/@rollup/rollup-darwin-arm64": {
./frontend/package-lock.json:626:    "node_modules/@rollup/rollup-darwin-x64": {
./frontend/package-lock.json:640:    "node_modules/@rollup/rollup-freebsd-arm64": {
./frontend/package-lock.json:654:    "node_modules/@rollup/rollup-freebsd-x64": {
./frontend/package-lock.json:668:    "node_modules/@rollup/rollup-linux-arm-gnueabihf": {
./frontend/package-lock.json:682:    "node_modules/@rollup/rollup-linux-arm-musleabihf": {
./frontend/package-lock.json:696:    "node_modules/@rollup/rollup-linux-arm64-gnu": {
./frontend/package-lock.json:710:    "node_modules/@rollup/rollup-linux-arm64-musl": {
./frontend/package-lock.json:724:    "node_modules/@rollup/rollup-linux-loong64-gnu": {
./frontend/package-lock.json:738:    "node_modules/@rollup/rollup-linux-loong64-musl": {
./frontend/package-lock.json:752:    "node_modules/@rollup/rollup-linux-ppc64-gnu": {
./frontend/package-lock.json:766:    "node_modules/@rollup/rollup-linux-ppc64-musl": {
./frontend/package-lock.json:780:    "node_modules/@rollup/rollup-linux-riscv64-gnu": {
./frontend/package-lock.json:794:    "node_modules/@rollup/rollup-linux-riscv64-musl": {
./frontend/package-lock.json:808:    "node_modules/@rollup/rollup-linux-s390x-gnu": {
./frontend/package-lock.json:822:    "node_modules/@rollup/rollup-linux-x64-gnu": {
./frontend/package-lock.json:836:    "node_modules/@rollup/rollup-linux-x64-musl": {
./frontend/package-lock.json:850:    "node_modules/@rollup/rollup-openbsd-x64": {
./frontend/package-lock.json:864:    "node_modules/@rollup/rollup-openharmony-arm64": {
./frontend/package-lock.json:878:    "node_modules/@rollup/rollup-win32-arm64-msvc": {
./frontend/package-lock.json:892:    "node_modules/@rollup/rollup-win32-ia32-msvc": {
./frontend/package-lock.json:906:    "node_modules/@rollup/rollup-win32-x64-gnu": {
./frontend/package-lock.json:920:    "node_modules/@rollup/rollup-win32-x64-msvc": {
./frontend/package-lock.json:934:    "node_modules/@types/estree": {
./frontend/package-lock.json:941:    "node_modules/@vitejs/plugin-vue": {
./frontend/package-lock.json:951:        "node": "^20.19.0 || >=22.12.0"
./frontend/package-lock.json:958:    "node_modules/@vue/compiler-core": {
./frontend/package-lock.json:971:    "node_modules/@vue/compiler-dom": {
./frontend/package-lock.json:981:    "node_modules/@vue/compiler-sfc": {
./frontend/package-lock.json:998:    "node_modules/@vue/compiler-ssr": {
./frontend/package-lock.json:1008:    "node_modules/@vue/devtools-api": {
./frontend/package-lock.json:1014:    "node_modules/@vue/reactivity": {
./frontend/package-lock.json:1023:    "node_modules/@vue/runtime-core": {
./frontend/package-lock.json:1033:    "node_modules/@vue/runtime-dom": {
./frontend/package-lock.json:1045:    "node_modules/@vue/server-renderer": {
./frontend/package-lock.json:1058:    "node_modules/@vue/shared": {
./frontend/package-lock.json:1064:    "node_modules/asynckit": {
./frontend/package-lock.json:1070:    "node_modules/axios": {
./frontend/package-lock.json:1081:    "node_modules/call-bind-apply-helpers": {
./frontend/package-lock.json:1091:        "node": ">= 0.4"
./frontend/package-lock.json:1094:    "node_modules/combined-stream": {
./frontend/package-lock.json:1103:        "node": ">= 0.8"
./frontend/package-lock.json:1106:    "node_modules/commander": {
./frontend/package-lock.json:1112:        "node": ">= 10"
./frontend/package-lock.json:1115:    "node_modules/csstype": {
./frontend/package-lock.json:1121:    "node_modules/d3": {
./frontend/package-lock.json:1159:        "node": ">=12"
./frontend/package-lock.json:1162:    "node_modules/d3-array": {
./frontend/package-lock.json:1171:        "node": ">=12"
./frontend/package-lock.json:1174:    "node_modules/d3-axis": {
./frontend/package-lock.json:1180:        "node": ">=12"
./frontend/package-lock.json:1183:    "node_modules/d3-brush": {
./frontend/package-lock.json:1196:        "node": ">=12"
./frontend/package-lock.json:1199:    "node_modules/d3-chord": {
./frontend/package-lock.json:1208:        "node": ">=12"
./frontend/package-lock.json:1211:    "node_modules/d3-color": {
./frontend/package-lock.json:1217:        "node": ">=12"
./frontend/package-lock.json:1220:    "node_modules/d3-contour": {
./frontend/package-lock.json:1229:        "node": ">=12"
./frontend/package-lock.json:1232:    "node_modules/d3-delaunay": {
./frontend/package-lock.json:1241:        "node": ">=12"
./frontend/package-lock.json:1244:    "node_modules/d3-dispatch": {
./frontend/package-lock.json:1250:        "node": ">=12"
./frontend/package-lock.json:1253:    "node_modules/d3-drag": {
./frontend/package-lock.json:1263:        "node": ">=12"
./frontend/package-lock.json:1266:    "node_modules/d3-dsv": {
./frontend/package-lock.json:1288:        "node": ">=12"
./frontend/package-lock.json:1291:    "node_modules/d3-ease": {
./frontend/package-lock.json:1297:        "node": ">=12"
./frontend/package-lock.json:1300:    "node_modules/d3-fetch": {
./frontend/package-lock.json:1309:        "node": ">=12"
./frontend/package-lock.json:1312:    "node_modules/d3-force": {
./frontend/package-lock.json:1323:        "node": ">=12"
./frontend/package-lock.json:1326:    "node_modules/d3-format": {
./frontend/package-lock.json:1332:        "node": ">=12"
./frontend/package-lock.json:1335:    "node_modules/d3-geo": {
./frontend/package-lock.json:1344:        "node": ">=12"
./frontend/package-lock.json:1347:    "node_modules/d3-hierarchy": {
./frontend/package-lock.json:1353:        "node": ">=12"
./frontend/package-lock.json:1356:    "node_modules/d3-interpolate": {
./frontend/package-lock.json:1365:        "node": ">=12"
./frontend/package-lock.json:1368:    "node_modules/d3-path": {
./frontend/package-lock.json:1374:        "node": ">=12"
./frontend/package-lock.json:1377:    "node_modules/d3-polygon": {
./frontend/package-lock.json:1383:        "node": ">=12"
./frontend/package-lock.json:1386:    "node_modules/d3-quadtree": {
./frontend/package-lock.json:1392:        "node": ">=12"
./frontend/package-lock.json:1395:    "node_modules/d3-random": {
./frontend/package-lock.json:1401:        "node": ">=12"
./frontend/package-lock.json:1404:    "node_modules/d3-scale": {
./frontend/package-lock.json:1417:        "node": ">=12"
./frontend/package-lock.json:1420:    "node_modules/d3-scale-chromatic": {
./frontend/package-lock.json:1430:        "node": ">=12"
./frontend/package-lock.json:1433:    "node_modules/d3-selection": {
./frontend/package-lock.json:1440:        "node": ">=12"
./frontend/package-lock.json:1443:    "node_modules/d3-shape": {
./frontend/package-lock.json:1452:        "node": ">=12"
./frontend/package-lock.json:1455:    "node_modules/d3-time": {
./frontend/package-lock.json:1464:        "node": ">=12"
./frontend/package-lock.json:1467:    "node_modules/d3-time-format": {
./frontend/package-lock.json:1476:        "node": ">=12"
./frontend/package-lock.json:1479:    "node_modules/d3-timer": {
./frontend/package-lock.json:1485:        "node": ">=12"
./frontend/package-lock.json:1488:    "node_modules/d3-transition": {
./frontend/package-lock.json:1501:        "node": ">=12"
./frontend/package-lock.json:1507:    "node_modules/d3-zoom": {
./frontend/package-lock.json:1520:        "node": ">=12"
./frontend/package-lock.json:1523:    "node_modules/delaunator": {
./frontend/package-lock.json:1532:    "node_modules/delayed-stream": {
./frontend/package-lock.json:1538:        "node": ">=0.4.0"
./frontend/package-lock.json:1541:    "node_modules/dunder-proto": {
./frontend/package-lock.json:1552:        "node": ">= 0.4"
./frontend/package-lock.json:1555:    "node_modules/entities": {
./frontend/package-lock.json:1561:        "node": ">=0.12"
./frontend/package-lock.json:1567:    "node_modules/es-define-property": {
./frontend/package-lock.json:1573:        "node": ">= 0.4"
./frontend/package-lock.json:1576:    "node_modules/es-errors": {
./frontend/package-lock.json:1582:        "node": ">= 0.4"
./frontend/package-lock.json:1585:    "node_modules/es-object-atoms": {
./frontend/package-lock.json:1594:        "node": ">= 0.4"
./frontend/package-lock.json:1597:    "node_modules/es-set-tostringtag": {
./frontend/package-lock.json:1609:        "node": ">= 0.4"
./frontend/package-lock.json:1612:    "node_modules/esbuild": {
./frontend/package-lock.json:1623:        "node": ">=18"
./frontend/package-lock.json:1654:    "node_modules/estree-walker": {
./frontend/package-lock.json:1660:    "node_modules/fdir": {
./frontend/package-lock.json:1667:        "node": ">=12.0.0"
./frontend/package-lock.json:1678:    "node_modules/follow-redirects": {
./frontend/package-lock.json:1690:        "node": ">=4.0"
./frontend/package-lock.json:1698:    "node_modules/form-data": {
./frontend/package-lock.json:1711:        "node": ">= 6"
./frontend/package-lock.json:1714:    "node_modules/fsevents": {
./frontend/package-lock.json:1726:        "node": "^8.16.0 || ^10.6.0 || >=11.0.0"
./frontend/package-lock.json:1729:    "node_modules/function-bind": {
./frontend/package-lock.json:1738:    "node_modules/get-intrinsic": {
./frontend/package-lock.json:1756:        "node": ">= 0.4"
./frontend/package-lock.json:1762:    "node_modules/get-proto": {
./frontend/package-lock.json:1772:        "node": ">= 0.4"
./frontend/package-lock.json:1775:    "node_modules/gopd": {
./frontend/package-lock.json:1781:        "node": ">= 0.4"
./frontend/package-lock.json:1787:    "node_modules/has-symbols": {
./frontend/package-lock.json:1793:        "node": ">= 0.4"
./frontend/package-lock.json:1799:    "node_modules/has-tostringtag": {
./frontend/package-lock.json:1808:        "node": ">= 0.4"
./frontend/package-lock.json:1814:    "node_modules/hasown": {
./frontend/package-lock.json:1823:        "node": ">= 0.4"
./frontend/package-lock.json:1826:    "node_modules/iconv-lite": {
./frontend/package-lock.json:1835:        "node": ">=0.10.0"
./frontend/package-lock.json:1838:    "node_modules/internmap": {
./frontend/package-lock.json:1844:        "node": ">=12"
./frontend/package-lock.json:1847:    "node_modules/magic-string": {
./frontend/package-lock.json:1856:    "node_modules/math-intrinsics": {
./frontend/package-lock.json:1862:        "node": ">= 0.4"
./frontend/package-lock.json:1865:    "node_modules/mime-db": {
./frontend/package-lock.json:1871:        "node": ">= 0.6"
./frontend/package-lock.json:1874:    "node_modules/mime-types": {
./frontend/package-lock.json:1883:        "node": ">= 0.6"
./frontend/package-lock.json:1886:    "node_modules/nanoid": {
./frontend/package-lock.json:1901:        "node": "^10 || ^12 || ^13.7 || ^14 || >=15.0.1"
./frontend/package-lock.json:1904:    "node_modules/picocolors": {
./frontend/package-lock.json:1910:    "node_modules/picomatch": {
./frontend/package-lock.json:1918:        "node": ">=12"
./frontend/package-lock.json:1924:    "node_modules/postcss": {
./frontend/package-lock.json:1949:        "node": "^10 || ^12 || >=14"
./frontend/package-lock.json:1952:    "node_modules/proxy-from-env": {
./frontend/package-lock.json:1958:        "node": ">=10"
./frontend/package-lock.json:1961:    "node_modules/robust-predicates": {
./frontend/package-lock.json:1967:    "node_modules/rollup": {
./frontend/package-lock.json:1980:        "node": ">=18.0.0",
./frontend/package-lock.json:2012:    "node_modules/rw": {
./frontend/package-lock.json:2018:    "node_modules/safer-buffer": {
./frontend/package-lock.json:2024:    "node_modules/source-map-js": {
./frontend/package-lock.json:2030:        "node": ">=0.10.0"
./frontend/package-lock.json:2033:    "node_modules/tinyglobby": {
./frontend/package-lock.json:2044:        "node": ">=12.0.0"
./frontend/package-lock.json:2050:    "node_modules/vite": {
./frontend/package-lock.json:2069:        "node": "^20.19.0 || >=22.12.0"
./frontend/package-lock.json:2078:        "@types/node": "^20.19.0 || >=22.12.0",
./frontend/package-lock.json:2091:        "@types/node": {
./frontend/package-lock.json:2126:    "node_modules/vue": {
./frontend/package-lock.json:2148:    "node_modules/vue-i18n": {
./frontend/package-lock.json:2160:        "node": ">= 16"
./frontend/package-lock.json:2169:    "node_modules/vue-router": {
./frontend/src/api/graph.js:5: * @param {Object} data - 包含files, simulation_requirement, project_name等
```

## 9. LLM / API / 环境变量 / 依赖关键词扫描

```text
./locales/zh.json:85:    "ontologyDesc": "LLM分析文档内容与模拟需求，提取出现实种子，自动生成合适的本体结构",
./locales/zh.json:113:    "dualPlatformConfigDesc": "LLM 根据模拟需求与现实种子，智能设置世界时间流速、推荐算法、每个个体的活跃时间段、发言频率、事件触发等参数",
./locales/zh.json:138:    "llmConfigReasoning": "LLM 配置推理",
./locales/zh.json:330:    "configError": "配置错误: {details}",
./locales/zh.json:331:    "zepApiKeyMissing": "ZEP_API_KEY未配置",
./locales/zh.json:351:    "configNotFound": "模拟配置不存在，请先调用 /prepare 接口",
./locales/zh.json:352:    "configFileNotFound": "配置文件不存在，请先调用 /prepare 接口",
./locales/zh.json:437:    "callingLLMConfig": "正在调用LLM生成配置...",
./locales/zh.json:439:    "configComplete": "配置生成完成",
./locales/zh.json:504:    "generatingLLMConfig": "正在调用LLM生成模拟配置参数...",
./locales/zh.json:505:    "configComplete": "✓ 模拟配置生成完成",
./locales/zh.json:506:    "configSummaryAgents": "  ├─ Agent数量: {count}个",
./locales/zh.json:507:    "configSummaryHours": "  ├─ 模拟时长: {hours}小时",
./locales/zh.json:508:    "configSummaryPosts": "  ├─ 初始帖子: {count}条",
./locales/zh.json:509:    "configSummaryTopics": "  ├─ 热点话题: {count}个",
./locales/zh.json:510:    "configSummaryPlatforms": "  └─ 平台配置: Twitter {twitter}, Reddit {reddit}",
./locales/zh.json:521:    "configLoadSuccess": "✓ 模拟配置加载成功",
./locales/zh.json:522:    "configSummaryPostsAlt": "  └─ 初始帖子: {count}条",
./locales/zh.json:523:    "configGenerating": "配置生成中，开始轮询等待...",
./locales/zh.json:577:    "llmResponse": "LLM 响应 (工具调用: {hasToolCalls}, 最终答案: {hasFinalAnswer})",
./locales/zh.json:589:    "sectionIterNone": "章节 {title} 第 {iteration} 次迭代: LLM 返回 None",
./locales/zh.json:590:    "sectionConflict": "章节 {title} 第 {iteration} 轮: LLM 同时输出工具调用和 Final Answer（第 {conflictCount} 次冲突）",
./locales/zh.json:593:    "multiToolOnlyFirst": "LLM 尝试调用 {total} 个工具，只执行第一个: {toolName}",
./locales/zh.json:594:    "sectionNoPrefix": "章节 {title} 未检测到 'Final Answer:' 前缀，直接采纳LLM输出作为最终内容（工具调用: {count}次）",
./locales/zh.json:596:    "sectionForceFailed": "章节 {title} 强制收尾时 LLM 返回 None，使用默认错误提示",
./locales/zh.json:597:    "sectionGenFailedContent": "（本章节生成失败：LLM 返回空响应，请稍后重试）",
./locales/zh.json:661:    "llmSelectAgentFailed": "LLM选择Agent失败，使用默认选择: {error}",
./locales/en.json:56:    "step02Desc": "Entity extraction & persona generation & Agent config injection",
./locales/en.json:85:    "ontologyDesc": "LLM analyzes document content and simulation requirements, extracts reality seeds, and auto-generates a suitable ontology structure",
./locales/en.json:113:    "dualPlatformConfigDesc": "LLM intelligently sets world time flow, recommendation algorithms, each individual's active hours, posting frequency, event triggers, and more based on requirements and reality seeds",
./locales/en.json:138:    "llmConfigReasoning": "LLM Config Reasoning",
./locales/en.json:330:    "configError": "Configuration error: {details}",
./locales/en.json:331:    "zepApiKeyMissing": "ZEP_API_KEY not configured",
./locales/en.json:351:    "configNotFound": "Simulation config not found. Please call /prepare first.",
./locales/en.json:352:    "configFileNotFound": "Config file not found. Please call /prepare first.",
./locales/en.json:437:    "callingLLMConfig": "Calling LLM to generate config...",
./locales/en.json:438:    "savingConfigFiles": "Saving config files...",
./locales/en.json:439:    "configComplete": "Config generation complete",
./locales/en.json:440:    "generatingTimeConfig": "Generating time config...",
./locales/en.json:441:    "generatingEventConfig": "Generating event config and hot topics...",
./locales/en.json:442:    "generatingAgentConfig": "Generating agent config ({start}-{end}/{total})...",
./locales/en.json:443:    "generatingPlatformConfig": "Generating platform config...",
./locales/en.json:468:    "timeConfig": "Time config: {minutes} minutes per round",
./locales/en.json:469:    "timeConfigFetchFailed": "Failed to fetch time config, using default: {minutes} min/round",
./locales/en.json:481:    "useAutoRounds": "Using auto-configured simulation rounds",
./locales/en.json:502:    "startGeneratingConfig": "Generating dual-platform simulation config...",
./locales/en.json:503:    "generatingAgentProfileConfig": "Generating agent persona config...",
./locales/en.json:504:    "generatingLLMConfig": "Calling LLM to generate simulation config parameters...",
./locales/en.json:505:    "configComplete": "✓ Simulation config generated",
./locales/en.json:506:    "configSummaryAgents": "  ├─ Agents: {count}",
./locales/en.json:507:    "configSummaryHours": "  ├─ Duration: {hours} hours",
./locales/en.json:508:    "configSummaryPosts": "  ├─ Initial posts: {count}",
./locales/en.json:509:    "configSummaryTopics": "  ├─ Hot topics: {count}",
./locales/en.json:510:    "configSummaryPlatforms": "  └─ Platforms: Twitter {twitter}, Reddit {reddit}",
./locales/en.json:511:    "timeConfigDetail": "Time config: {minutes} min/round, {rounds} rounds total",
./locales/en.json:515:    "startSimAutoRounds": "Starting simulation, auto-configured rounds: {rounds}",
./locales/en.json:519:    "loadingExistingConfig": "Loading existing config data...",
./locales/en.json:521:    "configLoadSuccess": "✓ Simulation config loaded",
./locales/en.json:522:    "configSummaryPostsAlt": "  └─ Initial posts: {count}",
./locales/en.json:523:    "configGenerating": "Config generating, polling...",
./locales/en.json:524:    "loadConfigFailed": "Failed to load config: {error}",
./locales/en.json:577:    "llmResponse": "LLM response (tool calls: {hasToolCalls}, final answer: {hasFinalAnswer})",
./locales/en.json:589:    "sectionIterNone": "Section {title} iteration {iteration}: LLM returned None",
./locales/en.json:590:    "sectionConflict": "Section {title} round {iteration}: LLM output both tool call and Final Answer (conflict #{conflictCount})",
./locales/en.json:593:    "multiToolOnlyFirst": "LLM attempted {total} tool calls, executing only the first: {toolName}",
./locales/en.json:594:    "sectionNoPrefix": "Section {title} missing 'Final Answer:' prefix, adopting LLM output as final content (tool calls: {count})",
./locales/en.json:596:    "sectionForceFailed": "Section {title} force-finish LLM returned None, using default error message",
./locales/en.json:597:    "sectionGenFailedContent": "(This section failed to generate: LLM returned empty response, please retry later)",
./locales/en.json:661:    "llmSelectAgentFailed": "LLM agent selection failed, using default selection: {error}",
./frontend/vite.config.js:5:// https://vite.dev/config/
./frontend/src/api/simulation.js:58:  return service.get(`/api/simulation/${simulationId}/config`)
./frontend/src/api/simulation.js:67:  return service.get(`/api/simulation/${simulationId}/config/realtime`)
./frontend/src/api/index.js:6:  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:5001',
./frontend/src/api/index.js:15:  config => {
./frontend/src/api/index.js:16:    config.headers['Accept-Language'] = i18n.global.locale.value
./frontend/src/api/index.js:17:    return config
./backend/run.py:11:    os.environ.setdefault('PYTHONIOENCODING', 'utf-8')
./backend/run.py:13:    if hasattr(sys.stdout, 'reconfigure'):
./backend/run.py:14:        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
./backend/run.py:15:    if hasattr(sys.stderr, 'reconfigure'):
./backend/run.py:16:        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
./backend/run.py:22:from app.config import Config
./backend/run.py:40:    host = os.environ.get('FLASK_HOST', '0.0.0.0')
./backend/run.py:41:    port = int(os.environ.get('FLASK_PORT', 5001))
./backend/app/config.py:7:from dotenv import load_dotenv
./backend/app/config.py:10:# 路径: MiroFish/.env (相对于 backend/app/config.py)
./backend/app/config.py:14:    load_dotenv(project_root_env, override=True)
./backend/app/config.py:17:    load_dotenv(override=True)
./backend/app/config.py:24:    SECRET_KEY = os.environ.get('SECRET_KEY', 'mirofish-secret-key')
./backend/app/config.py:25:    DEBUG = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
./backend/app/config.py:30:    # LLM配置（统一使用OpenAI格式）
./backend/app/config.py:31:    LLM_API_KEY = os.environ.get('LLM_API_KEY')
./backend/app/config.py:32:    LLM_BASE_URL = os.environ.get('LLM_BASE_URL', 'https://api.openai.com/v1')
./backend/app/config.py:33:    LLM_MODEL_NAME = os.environ.get('LLM_MODEL_NAME', 'gpt-4o-mini')
./backend/app/config.py:36:    ZEP_API_KEY = os.environ.get('ZEP_API_KEY')
./backend/app/config.py:48:    OASIS_DEFAULT_MAX_ROUNDS = int(os.environ.get('OASIS_DEFAULT_MAX_ROUNDS', '10'))
./backend/app/config.py:62:    REPORT_AGENT_MAX_TOOL_CALLS = int(os.environ.get('REPORT_AGENT_MAX_TOOL_CALLS', '5'))
./backend/app/config.py:63:    REPORT_AGENT_MAX_REFLECTION_ROUNDS = int(os.environ.get('REPORT_AGENT_MAX_REFLECTION_ROUNDS', '2'))
./backend/app/config.py:64:    REPORT_AGENT_TEMPERATURE = float(os.environ.get('REPORT_AGENT_TEMPERATURE', '0.5'))
./backend/app/config.py:70:        if not cls.LLM_API_KEY:
./backend/app/config.py:71:            errors.append("LLM_API_KEY 未配置")
./backend/app/config.py:72:        if not cls.ZEP_API_KEY:
./backend/app/config.py:73:            errors.append("ZEP_API_KEY 未配置")
./backend/app/__init__.py:15:from .config import Config
./backend/app/__init__.py:19:def create_app(config_class=Config):
./backend/app/__init__.py:22:    app.config.from_object(config_class)
./backend/app/__init__.py:33:    is_reloader_process = os.environ.get('WERKZEUG_RUN_MAIN') == 'true'
./backend/app/__init__.py:34:    debug_mode = app.config.get('DEBUG', False)
./backend/app/utils/__init__.py:6:from .llm_client import LLMClient
./backend/app/utils/__init__.py:9:__all__ = ['FileParser', 'LLMClient', 't', 'get_locale', 'set_locale', 'get_language_instruction']
./backend/app/utils/logger.py:20:        if hasattr(sys.stdout, 'reconfigure'):
./backend/app/utils/logger.py:21:            sys.stdout.reconfigure(encoding='utf-8', errors='replace')
./backend/app/utils/logger.py:22:        if hasattr(sys.stderr, 'reconfigure'):
./backend/app/utils/logger.py:23:            sys.stderr.reconfigure(encoding='utf-8', errors='replace')
./backend/app/utils/retry.py:3:用于处理LLM等外部API调用的重试逻辑
./backend/app/utils/llm_client.py:2:LLM客户端封装
./backend/app/utils/llm_client.py:11:from ..config import Config
./backend/app/utils/llm_client.py:14:class LLMClient:
./backend/app/utils/llm_client.py:15:    """LLM客户端"""
./backend/app/utils/llm_client.py:19:        api_key: Optional[str] = None,
./backend/app/utils/llm_client.py:23:        self.api_key = api_key or Config.LLM_API_KEY
./backend/app/utils/llm_client.py:24:        self.base_url = base_url or Config.LLM_BASE_URL
./backend/app/utils/llm_client.py:25:        self.model = model or Config.LLM_MODEL_NAME
./backend/app/utils/llm_client.py:27:        if not self.api_key:
./backend/app/utils/llm_client.py:28:            raise ValueError("LLM_API_KEY 未配置")
./backend/app/utils/llm_client.py:31:            api_key=self.api_key,
./backend/app/utils/llm_client.py:102:            raise ValueError(f"LLM返回的JSON格式无效: {cleaned_response}")
./backend/app/utils/locale.py:68:    lang_config = _languages.get(locale, _languages.get('zh', {}))
./backend/app/utils/locale.py:69:    return lang_config.get('llmInstruction', '请使用中文回答。')
./backend/app/models/project.py:14:from ..config import Config
./backend/app/api/simulation.py:11:from ..config import Config
./backend/app/api/simulation.py:60:        if not Config.ZEP_API_KEY:
./backend/app/api/simulation.py:97:        if not Config.ZEP_API_KEY:
./backend/app/api/simulation.py:130:        if not Config.ZEP_API_KEY:
./backend/app/api/simulation.py:170:    注意：max_rounds等参数由LLM智能生成，无需手动设置
./backend/app/api/simulation.py:246:    2. 必要文件存在：reddit_profiles.json, twitter_profiles.csv, simulation_config.json
./backend/app/api/simulation.py:257:    from ..config import Config
./backend/app/api/simulation.py:268:        "simulation_config.json",
./backend/app/api/simulation.py:298:        config_generated = state_data.get("config_generated", False)
./backend/app/api/simulation.py:301:        logger.debug(f"检测模拟准备状态: {simulation_id}, status={status}, config_generated={config_generated}")
./backend/app/api/simulation.py:303:        # 如果 config_generated=True 且文件存在，认为准备完成
./backend/app/api/simulation.py:306:        # - preparing: 如果 config_generated=True 说明已完成
./backend/app/api/simulation.py:312:        if status in prepared_statuses and config_generated:
./backend/app/api/simulation.py:315:            config_file = os.path.join(simulation_dir, "simulation_config.json")
./backend/app/api/simulation.py:336:            logger.info(f"模拟 {simulation_id} 检测结果: 已准备完成 (status={status}, config_generated={config_generated})")
./backend/app/api/simulation.py:342:                "config_generated": config_generated,
./backend/app/api/simulation.py:348:            logger.warning(f"模拟 {simulation_id} 检测结果: 未准备完成 (status={status}, config_generated={config_generated})")
./backend/app/api/simulation.py:350:                "reason": f"状态不在已准备列表中或config_generated为false: status={status}, config_generated={config_generated}",
./backend/app/api/simulation.py:352:                "config_generated": config_generated
./backend/app/api/simulation.py:362:    准备模拟环境（异步任务，LLM智能生成所有参数）
./backend/app/api/simulation.py:376:    4. LLM智能生成模拟配置（带重试机制）
./backend/app/api/simulation.py:383:            "use_llm_for_profiles": true,                 // 可选，是否用LLM生成人设
./backend/app/api/simulation.py:403:    from ..config import Config
./backend/app/api/simulation.py:527:                        "generating_config": (70, 90),    # 70-90%
./backend/app/api/simulation.py:538:                        "generating_config": t('progress.generatingSimConfig'),
./backend/app/api/simulation.py:922:            # 获取模拟配置信息（从 simulation_config.json 读取 simulation_requirement）
./backend/app/api/simulation.py:923:            config = manager.get_simulation_config(sim.simulation_id)
./backend/app/api/simulation.py:924:            if config:
./backend/app/api/simulation.py:925:                sim_dict["simulation_requirement"] = config.get("simulation_requirement", "")
./backend/app/api/simulation.py:926:                time_config = config.get("time_config", {})
./backend/app/api/simulation.py:927:                sim_dict["total_simulation_hours"] = time_config.get("total_simulation_hours", 0)
./backend/app/api/simulation.py:930:                    time_config.get("total_simulation_hours", 0) * 60 / 
./backend/app/api/simulation.py:931:                    max(time_config.get("minutes_per_round", 60), 1)
./backend/app/api/simulation.py:1138:@simulation_bp.route('/<simulation_id>/config/realtime', methods=['GET'])
./backend/app/api/simulation.py:1139:def get_simulation_config_realtime(simulation_id: str):
./backend/app/api/simulation.py:1143:    与 /config 接口的区别：
./backend/app/api/simulation.py:1157:                "generation_stage": "generating_config",  // 当前生成阶段
./backend/app/api/simulation.py:1158:                "config": {...}  // 配置内容（如果存在）
./backend/app/api/simulation.py:1176:        config_file = os.path.join(sim_dir, "simulation_config.json")
./backend/app/api/simulation.py:1179:        file_exists = os.path.exists(config_file)
./backend/app/api/simulation.py:1180:        config = None
./backend/app/api/simulation.py:1185:            file_stat = os.stat(config_file)
./backend/app/api/simulation.py:1189:                with open(config_file, 'r', encoding='utf-8') as f:
./backend/app/api/simulation.py:1190:                    config = json.load(f)
./backend/app/api/simulation.py:1192:                logger.warning(f"读取 config 文件失败（可能正在写入中）: {e}")
./backend/app/api/simulation.py:1193:                config = None
./backend/app/api/simulation.py:1198:        config_generated = False
./backend/app/api/simulation.py:1207:                    config_generated = state_data.get("config_generated", False)
./backend/app/api/simulation.py:1212:                            generation_stage = "generating_config"
./backend/app/api/simulation.py:1227:            "config_generated": config_generated,
./backend/app/api/simulation.py:1228:            "config": config
./backend/app/api/simulation.py:1232:        if config:
./backend/app/api/simulation.py:1234:                "total_agents": len(config.get("agent_configs", [])),
./backend/app/api/simulation.py:1235:                "simulation_hours": config.get("time_config", {}).get("total_simulation_hours"),
./backend/app/api/simulation.py:1236:                "initial_posts_count": len(config.get("event_config", {}).get("initial_posts", [])),
./backend/app/api/simulation.py:1237:                "hot_topics_count": len(config.get("event_config", {}).get("hot_topics", [])),
./backend/app/api/simulation.py:1238:                "has_twitter_config": "twitter_config" in config,
./backend/app/api/simulation.py:1239:                "has_reddit_config": "reddit_config" in config,
./backend/app/api/simulation.py:1240:                "generated_at": config.get("generated_at"),
./backend/app/api/simulation.py:1241:                "llm_model": config.get("llm_model")
./backend/app/api/simulation.py:1258:@simulation_bp.route('/<simulation_id>/config', methods=['GET'])
./backend/app/api/simulation.py:1259:def get_simulation_config(simulation_id: str):
./backend/app/api/simulation.py:1261:    获取模拟配置（LLM智能生成的完整配置）
./backend/app/api/simulation.py:1264:        - time_config: 时间配置（模拟时长、轮次、高峰/低谷时段）
./backend/app/api/simulation.py:1265:        - agent_configs: 每个Agent的活动配置（活跃度、发言频率、立场等）
./backend/app/api/simulation.py:1266:        - event_config: 事件配置（初始帖子、热点话题）
./backend/app/api/simulation.py:1267:        - platform_configs: 平台配置
./backend/app/api/simulation.py:1268:        - generation_reasoning: LLM的配置推理说明
./backend/app/api/simulation.py:1272:        config = manager.get_simulation_config(simulation_id)
./backend/app/api/simulation.py:1274:        if not config:
./backend/app/api/simulation.py:1277:                "error": t('api.configNotFound')
./backend/app/api/simulation.py:1282:            "data": config
./backend/app/api/simulation.py:1294:@simulation_bp.route('/<simulation_id>/config/download', methods=['GET'])
./backend/app/api/simulation.py:1295:def download_simulation_config(simulation_id: str):
./backend/app/api/simulation.py:1300:        config_path = os.path.join(sim_dir, "simulation_config.json")
./backend/app/api/simulation.py:1302:        if not os.path.exists(config_path):
./backend/app/api/simulation.py:1305:                "error": t('api.configFileNotFound')
./backend/app/api/simulation.py:1309:            config_path,
./backend/app/api/simulation.py:1311:            download_name="simulation_config.json"
./backend/app/api/simulation.py:1468:        - 不会清理配置文件（simulation_config.json）和 profile 文件
./backend/app/api/graph.py:12:from ..config import Config
./backend/app/api/graph.py:216:        logger.info("调用 LLM 生成本体定义...")
./backend/app/api/graph.py:288:        if not Config.ZEP_API_KEY:
./backend/app/api/graph.py:294:                "error": t('api.configError', details="; ".join(errors))
./backend/app/api/graph.py:390:                builder = GraphBuilderService(api_key=Config.ZEP_API_KEY)
./backend/app/api/graph.py:575:        if not Config.ZEP_API_KEY:
./backend/app/api/graph.py:581:        builder = GraphBuilderService(api_key=Config.ZEP_API_KEY)
./backend/app/api/graph.py:603:        if not Config.ZEP_API_KEY:
./backend/app/api/graph.py:609:        builder = GraphBuilderService(api_key=Config.ZEP_API_KEY)
./backend/app/api/report.py:12:from ..config import Config
./backend/app/api/report.py:765:    - 每个章节的开始、工具调用、LLM响应、完成
./backend/app/services/report_agent.py:21:from ..config import Config
./backend/app/services/report_agent.py:22:from ..utils.llm_client import LLMClient
./backend/app/services/report_agent.py:221:        """记录 LLM 响应（完整内容，不截断）"""
./backend/app/services/report_agent.py:526:这不是LLM模拟，而是调用真实的采访接口获取模拟Agent的原始回答。
./backend/app/services/report_agent.py:889:        llm_client: Optional[LLMClient] = None,
./backend/app/services/report_agent.py:899:            llm_client: LLM客户端（可选）
./backend/app/services/report_agent.py:906:        self.llm = llm_client or LLMClient()
./backend/app/services/report_agent.py:1069:        从LLM响应中解析工具调用
./backend/app/services/report_agent.py:1089:        # 格式2: 兜底 - LLM 直接输出裸 JSON（没包 <tool_call> 标签）
./backend/app/services/report_agent.py:1144:        使用LLM分析模拟需求，规划报告的目录结构
./backend/app/services/report_agent.py:1304:            # 调用LLM
./backend/app/services/report_agent.py:1311:            # 检查 LLM 返回是否为 None（API 异常或内容为空）
./backend/app/services/report_agent.py:1322:            logger.debug(f"LLM响应: {response[:200]}...")
./backend/app/services/report_agent.py:1329:            # ── 冲突处理：LLM 同时输出了工具调用和 Final Answer ──
./backend/app/services/report_agent.py:1337:                    # 前两次：丢弃本次响应，要求 LLM 重新回复
./backend/app/services/report_agent.py:1363:            # 记录 LLM 响应日志
./backend/app/services/report_agent.py:1374:            # ── 情况1：LLM 输出了 Final Answer ──
./backend/app/services/report_agent.py:1404:            # ── 情况2：LLM 尝试调用工具 ──
./backend/app/services/report_agent.py:1488:            # 工具调用已足够，LLM 输出了内容但没带 "Final Answer:" 前缀
./backend/app/services/report_agent.py:1512:        # 检查强制收尾时 LLM 返回是否为 None
./backend/app/services/simulation_runner.py:21:from ..config import Config
./backend/app/services/simulation_runner.py:341:        config_path = os.path.join(sim_dir, "simulation_config.json")
./backend/app/services/simulation_runner.py:343:        if not os.path.exists(config_path):
./backend/app/services/simulation_runner.py:346:        with open(config_path, 'r', encoding='utf-8') as f:
./backend/app/services/simulation_runner.py:347:            config = json.load(f)
./backend/app/services/simulation_runner.py:350:        time_config = config.get("time_config", {})
./backend/app/services/simulation_runner.py:351:        total_hours = time_config.get("total_simulation_hours", 72)
./backend/app/services/simulation_runner.py:352:        minutes_per_round = time_config.get("minutes_per_round", 30)
./backend/app/services/simulation_runner.py:419:                "--config", config_path,  # 使用完整配置文件路径
./backend/app/services/simulation_runner.py:432:            env = os.environ.copy()
./backend/app/services/simulation_runner.py:1117:        注意：不会删除配置文件（simulation_config.json）和 profile 文件
./backend/app/services/simulation_runner.py:1302:        is_reloader_process = os.environ.get('WERKZEUG_RUN_MAIN') == 'true'
./backend/app/services/simulation_runner.py:1303:        is_debug_mode = os.environ.get('FLASK_DEBUG') == '1' or os.environ.get('WERKZEUG_RUN_MAIN') is not None
./backend/app/services/simulation_runner.py:1580:        config_path = os.path.join(sim_dir, "simulation_config.json")
./backend/app/services/simulation_runner.py:1581:        if not os.path.exists(config_path):
./backend/app/services/simulation_runner.py:1584:        with open(config_path, 'r', encoding='utf-8') as f:
./backend/app/services/simulation_runner.py:1585:            config = json.load(f)
./backend/app/services/simulation_runner.py:1587:        agent_configs = config.get("agent_configs", [])
./backend/app/services/simulation_runner.py:1588:        if not agent_configs:
./backend/app/services/simulation_runner.py:1593:        for agent_config in agent_configs:
./backend/app/services/simulation_runner.py:1594:            agent_id = agent_config.get("agent_id")
./backend/app/services/zep_tools.py:18:from ..config import Config
./backend/app/services/zep_tools.py:20:from ..utils.llm_client import LLMClient
./backend/app/services/zep_tools.py:46:        """转换为文本格式，供LLM理解"""
./backend/app/services/zep_tools.py:172:        """转换为详细的文本格式，供LLM理解"""
./backend/app/services/zep_tools.py:376:        """转换为详细的文本格式，供LLM理解和报告引用"""
./backend/app/services/zep_tools.py:425:    def __init__(self, api_key: Optional[str] = None, llm_client: Optional[LLMClient] = None):
./backend/app/services/zep_tools.py:426:        self.api_key = api_key or Config.ZEP_API_KEY
./backend/app/services/zep_tools.py:427:        if not self.api_key:
./backend/app/services/zep_tools.py:428:            raise ValueError("ZEP_API_KEY 未配置")
./backend/app/services/zep_tools.py:430:        self.client = Zep(api_key=self.api_key)
./backend/app/services/zep_tools.py:431:        # LLM客户端用于InsightForge生成子问题
./backend/app/services/zep_tools.py:436:    def llm(self) -> LLMClient:
./backend/app/services/zep_tools.py:437:        """延迟初始化LLM客户端"""
./backend/app/services/zep_tools.py:439:            self._llm_client = LLMClient()
./backend/app/services/zep_tools.py:957:        1. 使用LLM将问题分解为多个子问题
./backend/app/services/zep_tools.py:981:        # Step 1: 使用LLM生成子问题
./backend/app/services/zep_tools.py:1100:        使用LLM生成子问题
./backend/app/services/zep_tools.py:1285:        2. 使用LLM分析采访需求，智能选择最相关的Agent
./backend/app/services/zep_tools.py:1286:        3. 使用LLM生成采访问题
./backend/app/services/zep_tools.py:1295:        - 需要获取模拟Agent的真实回答（非LLM模拟）
./backend/app/services/zep_tools.py:1327:        # Step 2: 使用LLM选择要采访的Agent（返回agent_id列表）
./backend/app/services/zep_tools.py:1559:        使用LLM选择要采访的Agent
./backend/app/services/zep_tools.py:1640:        """使用LLM生成采访问题"""
./backend/app/services/__init__.py:11:from .simulation_config_generator import (
./backend/app/services/oasis_profile_generator.py:21:from ..config import Config
./backend/app/services/oasis_profile_generator.py:183:        api_key: Optional[str] = None,
./backend/app/services/oasis_profile_generator.py:186:        zep_api_key: Optional[str] = None,
./backend/app/services/oasis_profile_generator.py:189:        self.api_key = api_key or Config.LLM_API_KEY
./backend/app/services/oasis_profile_generator.py:190:        self.base_url = base_url or Config.LLM_BASE_URL
./backend/app/services/oasis_profile_generator.py:191:        self.model_name = model_name or Config.LLM_MODEL_NAME
./backend/app/services/oasis_profile_generator.py:193:        if not self.api_key:
./backend/app/services/oasis_profile_generator.py:194:            raise ValueError("LLM_API_KEY 未配置")
./backend/app/services/oasis_profile_generator.py:197:            api_key=self.api_key,
./backend/app/services/oasis_profile_generator.py:202:        self.zep_api_key = zep_api_key or Config.ZEP_API_KEY
./backend/app/services/oasis_profile_generator.py:206:        if self.zep_api_key:
./backend/app/services/oasis_profile_generator.py:208:                self.zep_client = Zep(api_key=self.zep_api_key)
./backend/app/services/oasis_profile_generator.py:224:            use_llm: 是否使用LLM生成详细人设
./backend/app/services/oasis_profile_generator.py:239:            # 使用LLM生成详细人设
./backend/app/services/oasis_profile_generator.py:506:        使用LLM生成非常详细的人设
./backend/app/services/oasis_profile_generator.py:538:                    # 不设置max_tokens，让LLM自由发挥
./backend/app/services/oasis_profile_generator.py:546:                    logger.warning(f"LLM输出被截断 (attempt {attempt+1}), 尝试修复...")
./backend/app/services/oasis_profile_generator.py:573:                logger.warning(f"LLM调用失败 (attempt {attempt+1}): {str(e)[:80]}")
./backend/app/services/oasis_profile_generator.py:578:        logger.warning(f"LLM生成人设失败（{max_attempts}次尝试）: {last_error}, 使用规则生成")
./backend/app/services/oasis_profile_generator.py:866:            use_llm: 是否使用LLM生成详细人设
./backend/app/services/oasis_profile_generator.py:1078:        - user_char: 详细人设描述（注入到LLM系统提示中，指导Agent行为）
./backend/app/services/oasis_profile_generator.py:1082:        - user_char: 内部使用，LLM系统提示，决定Agent如何思考和行动
./backend/app/services/oasis_profile_generator.py:1100:                # user_char: 完整人设（bio + persona），用于LLM系统提示
./backend/app/services/oasis_profile_generator.py:1114:                    user_char,              # user_char: 完整人设（内部LLM使用）
./backend/app/services/simulation_manager.py:4:使用预设脚本 + LLM智能生成配置参数
./backend/app/services/simulation_manager.py:15:from ..config import Config
./backend/app/services/simulation_manager.py:19:from .simulation_config_generator import SimulationConfigGenerator, SimulationParameters
./backend/app/services/simulation_manager.py:63:    config_generated: bool = False
./backend/app/services/simulation_manager.py:64:    config_reasoning: str = ""
./backend/app/services/simulation_manager.py:90:            "config_generated": self.config_generated,
./backend/app/services/simulation_manager.py:91:            "config_reasoning": self.config_reasoning,
./backend/app/services/simulation_manager.py:110:            "config_generated": self.config_generated,
./backend/app/services/simulation_manager.py:122:    3. 使用LLM智能生成模拟配置参数
./backend/app/services/simulation_manager.py:181:            config_generated=data.get("config_generated", False),
./backend/app/services/simulation_manager.py:182:            config_reasoning=data.get("config_reasoning", ""),
./backend/app/services/simulation_manager.py:245:        2. 为每个实体生成OASIS Agent Profile（可选LLM增强，支持并行）
./backend/app/services/simulation_manager.py:246:        3. 使用LLM智能生成模拟配置参数（时间、活跃度、发言频率等）
./backend/app/services/simulation_manager.py:252:            simulation_requirement: 模拟需求描述（用于LLM生成配置）
./backend/app/services/simulation_manager.py:253:            document_text: 原始文档内容（用于LLM理解背景）
./backend/app/services/simulation_manager.py:255:            use_llm_for_profiles: 是否使用LLM生成详细人设
./backend/app/services/simulation_manager.py:384:            # ========== 阶段3: LLM智能生成模拟配置 ==========
./backend/app/services/simulation_manager.py:387:                    "generating_config", 0,
./backend/app/services/simulation_manager.py:393:            config_generator = SimulationConfigGenerator()
./backend/app/services/simulation_manager.py:397:                    "generating_config", 30,
./backend/app/services/simulation_manager.py:398:                    t('progress.callingLLMConfig'),
./backend/app/services/simulation_manager.py:403:            sim_params = config_generator.generate_config(
./backend/app/services/simulation_manager.py:416:                    "generating_config", 70,
./backend/app/services/simulation_manager.py:423:            config_path = os.path.join(sim_dir, "simulation_config.json")
./backend/app/services/simulation_manager.py:424:            with open(config_path, 'w', encoding='utf-8') as f:
./backend/app/services/simulation_manager.py:427:            state.config_generated = True
./backend/app/services/simulation_manager.py:428:            state.config_reasoning = sim_params.generation_reasoning
./backend/app/services/simulation_manager.py:432:                    "generating_config", 100,
./backend/app/services/simulation_manager.py:433:                    t('progress.configComplete'),
./backend/app/services/simulation_manager.py:496:    def get_simulation_config(self, simulation_id: str) -> Optional[Dict[str, Any]]:
./backend/app/services/simulation_manager.py:499:        config_path = os.path.join(sim_dir, "simulation_config.json")
./backend/app/services/simulation_manager.py:501:        if not os.path.exists(config_path):
./backend/app/services/simulation_manager.py:504:        with open(config_path, 'r', encoding='utf-8') as f:
./backend/app/services/simulation_manager.py:510:        config_path = os.path.join(sim_dir, "simulation_config.json")
./backend/app/services/simulation_manager.py:516:            "config_file": config_path,
./backend/app/services/simulation_manager.py:518:                "twitter": f"python {scripts_dir}/run_twitter_simulation.py --config {config_path}",
./backend/app/services/simulation_manager.py:519:                "reddit": f"python {scripts_dir}/run_reddit_simulation.py --config {config_path}",
./backend/app/services/simulation_manager.py:520:                "parallel": f"python {scripts_dir}/run_parallel_simulation.py --config {config_path}",
./backend/app/services/simulation_manager.py:525:                f"   - 单独运行Twitter: python {scripts_dir}/run_twitter_simulation.py --config {config_path}\n"
./backend/app/services/simulation_manager.py:526:                f"   - 单独运行Reddit: python {scripts_dir}/run_reddit_simulation.py --config {config_path}\n"
./backend/app/services/simulation_manager.py:527:                f"   - 并行运行双平台: python {scripts_dir}/run_parallel_simulation.py --config {config_path}"
./backend/app/services/ontology_generator.py:10:from ..utils.llm_client import LLMClient
./backend/app/services/ontology_generator.py:182:    def __init__(self, llm_client: Optional[LLMClient] = None):
./backend/app/services/ontology_generator.py:183:        self.llm_client = llm_client or LLMClient()
./backend/app/services/ontology_generator.py:216:        # 调用LLM
./backend/app/services/ontology_generator.py:228:    # 传给 LLM 的文本最大长度（5万字）
./backend/app/services/ontology_generator.py:229:    MAX_TEXT_LENGTH_FOR_LLM = 50000
./backend/app/services/ontology_generator.py:243:        # 如果文本超过5万字，截断（仅影响传给LLM的内容，不影响图谱构建）
./backend/app/services/ontology_generator.py:244:        if len(combined_text) > self.MAX_TEXT_LENGTH_FOR_LLM:
./backend/app/services/ontology_generator.py:245:            combined_text = combined_text[:self.MAX_TEXT_LENGTH_FOR_LLM]
./backend/app/services/ontology_generator.py:246:            combined_text += f"\n\n...(原文共{original_length}字，已截取前{self.MAX_TEXT_LENGTH_FOR_LLM}字用于本体分析)..."
./backend/app/services/zep_entity_reader.py:12:from ..config import Config
./backend/app/services/zep_entity_reader.py:81:    def __init__(self, api_key: Optional[str] = None):
./backend/app/services/zep_entity_reader.py:82:        self.api_key = api_key or Config.ZEP_API_KEY
./backend/app/services/zep_entity_reader.py:83:        if not self.api_key:
./backend/app/services/zep_entity_reader.py:84:            raise ValueError("ZEP_API_KEY 未配置")
./backend/app/services/zep_entity_reader.py:86:        self.client = Zep(api_key=self.api_key)
./backend/app/services/graph_builder.py:16:from ..config import Config
./backend/app/services/graph_builder.py:46:    def __init__(self, api_key: Optional[str] = None):
./backend/app/services/graph_builder.py:47:        self.api_key = api_key or Config.ZEP_API_KEY
./backend/app/services/graph_builder.py:48:        if not self.api_key:
./backend/app/services/graph_builder.py:49:            raise ValueError("ZEP_API_KEY 未配置")
./backend/app/services/graph_builder.py:51:        self.client = Zep(api_key=self.api_key)
./backend/app/services/zep_graph_memory_updater.py:17:from ..config import Config
./backend/app/services/zep_graph_memory_updater.py:232:    def __init__(self, graph_id: str, api_key: Optional[str] = None):
./backend/app/services/zep_graph_memory_updater.py:238:            api_key: Zep API Key（可选，默认从配置读取）
./backend/app/services/zep_graph_memory_updater.py:241:        self.api_key = api_key or Config.ZEP_API_KEY
./backend/app/services/zep_graph_memory_updater.py:243:        if not self.api_key:
./backend/app/services/zep_graph_memory_updater.py:244:            raise ValueError("ZEP_API_KEY未配置")
./backend/app/services/zep_graph_memory_updater.py:246:        self.client = Zep(api_key=self.api_key)
./backend/app/services/simulation_config_generator.py:3:使用LLM根据模拟需求、文档内容、图谱信息自动生成细致的模拟参数
./backend/app/services/simulation_config_generator.py:21:from ..config import Config
./backend/app/services/simulation_config_generator.py:26:logger = get_logger('mirofish.simulation_config')
./backend/app/services/simulation_config_generator.py:156:    time_config: TimeSimulationConfig = field(default_factory=TimeSimulationConfig)
./backend/app/services/simulation_config_generator.py:159:    agent_configs: List[AgentActivityConfig] = field(default_factory=list)
./backend/app/services/simulation_config_generator.py:162:    event_config: EventConfig = field(default_factory=EventConfig)
./backend/app/services/simulation_config_generator.py:165:    twitter_config: Optional[PlatformConfig] = None
./backend/app/services/simulation_config_generator.py:166:    reddit_config: Optional[PlatformConfig] = None
./backend/app/services/simulation_config_generator.py:168:    # LLM配置
./backend/app/services/simulation_config_generator.py:174:    generation_reasoning: str = ""  # LLM的推理说明
./backend/app/services/simulation_config_generator.py:178:        time_dict = asdict(self.time_config)
./backend/app/services/simulation_config_generator.py:184:            "time_config": time_dict,
./backend/app/services/simulation_config_generator.py:185:            "agent_configs": [asdict(a) for a in self.agent_configs],
./backend/app/services/simulation_config_generator.py:186:            "event_config": asdict(self.event_config),
./backend/app/services/simulation_config_generator.py:187:            "twitter_config": asdict(self.twitter_config) if self.twitter_config else None,
./backend/app/services/simulation_config_generator.py:188:            "reddit_config": asdict(self.reddit_config) if self.reddit_config else None,
./backend/app/services/simulation_config_generator.py:204:    使用LLM分析模拟需求、文档内容、图谱实体信息，
./backend/app/services/simulation_config_generator.py:227:        api_key: Optional[str] = None,
./backend/app/services/simulation_config_generator.py:231:        self.api_key = api_key or Config.LLM_API_KEY
./backend/app/services/simulation_config_generator.py:232:        self.base_url = base_url or Config.LLM_BASE_URL
./backend/app/services/simulation_config_generator.py:233:        self.model_name = model_name or Config.LLM_MODEL_NAME
./backend/app/services/simulation_config_generator.py:235:        if not self.api_key:
./backend/app/services/simulation_config_generator.py:236:            raise ValueError("LLM_API_KEY 未配置")
./backend/app/services/simulation_config_generator.py:239:            api_key=self.api_key,
./backend/app/services/simulation_config_generator.py:243:    def generate_config(
./backend/app/services/simulation_config_generator.py:298:        time_config_result = self._generate_time_config(context, num_entities)
./backend/app/services/simulation_config_generator.py:299:        time_config = self._parse_time_config(time_config_result, num_entities)
./backend/app/services/simulation_config_generator.py:300:        reasoning_parts.append(f"{t('progress.timeConfigLabel')}: {time_config_result.get('reasoning', t('common.success'))}")
./backend/app/services/simulation_config_generator.py:304:        event_config_result = self._generate_event_config(context, simulation_requirement, entities)
./backend/app/services/simulation_config_generator.py:305:        event_config = self._parse_event_config(event_config_result)
./backend/app/services/simulation_config_generator.py:306:        reasoning_parts.append(f"{t('progress.eventConfigLabel')}: {event_config_result.get('reasoning', t('common.success'))}")
./backend/app/services/simulation_config_generator.py:309:        all_agent_configs = []
./backend/app/services/simulation_config_generator.py:320:            batch_configs = self._generate_agent_configs_batch(
./backend/app/services/simulation_config_generator.py:326:            all_agent_configs.extend(batch_configs)
./backend/app/services/simulation_config_generator.py:328:        reasoning_parts.append(t('progress.agentConfigResult', count=len(all_agent_configs)))
./backend/app/services/simulation_config_generator.py:332:        event_config = self._assign_initial_post_agents(event_config, all_agent_configs)
./backend/app/services/simulation_config_generator.py:333:        assigned_count = len([p for p in event_config.initial_posts if p.get("poster_agent_id") is not None])
./backend/app/services/simulation_config_generator.py:338:        twitter_config = None
./backend/app/services/simulation_config_generator.py:339:        reddit_config = None
./backend/app/services/simulation_config_generator.py:342:            twitter_config = PlatformConfig(
./backend/app/services/simulation_config_generator.py:352:            reddit_config = PlatformConfig(
./backend/app/services/simulation_config_generator.py:367:            time_config=time_config,
./backend/app/services/simulation_config_generator.py:368:            agent_configs=all_agent_configs,
./backend/app/services/simulation_config_generator.py:369:            event_config=event_config,
./backend/app/services/simulation_config_generator.py:370:            twitter_config=twitter_config,
./backend/app/services/simulation_config_generator.py:371:            reddit_config=reddit_config,
./backend/app/services/simulation_config_generator.py:377:        logger.info(f"模拟配置生成完成: {len(params.agent_configs)} 个Agent配置")
./backend/app/services/simulation_config_generator.py:387:        """构建LLM上下文，截断到最大长度"""
./backend/app/services/simulation_config_generator.py:435:        """带重试的LLM调用，包含JSON修复逻辑"""
./backend/app/services/simulation_config_generator.py:451:                    # 不设置max_tokens，让LLM自由发挥
./backend/app/services/simulation_config_generator.py:459:                    logger.warning(f"LLM输出被截断 (attempt {attempt+1})")
./backend/app/services/simulation_config_generator.py:469:                    fixed = self._try_fix_config_json(content)
./backend/app/services/simulation_config_generator.py:476:                logger.warning(f"LLM调用失败 (attempt {attempt+1}): {str(e)[:80]}")
./backend/app/services/simulation_config_generator.py:481:        raise last_error or Exception("LLM调用失败")
./backend/app/services/simulation_config_generator.py:501:    def _try_fix_config_json(self, content: str) -> Optional[Dict[str, Any]]:
./backend/app/services/simulation_config_generator.py:535:    def _generate_time_config(self, context: str, num_entities: int) -> Dict[str, Any]:
./backend/app/services/simulation_config_generator.py:594:            logger.warning(f"时间配置LLM生成失败: {e}, 使用默认配置")
./backend/app/services/simulation_config_generator.py:595:            return self._get_default_time_config(num_entities)
./backend/app/services/simulation_config_generator.py:597:    def _get_default_time_config(self, num_entities: int) -> Dict[str, Any]:
./backend/app/services/simulation_config_generator.py:611:    def _parse_time_config(self, result: Dict[str, Any], num_entities: int) -> TimeSimulationConfig:
./backend/app/services/simulation_config_generator.py:646:    def _generate_event_config(
./backend/app/services/simulation_config_generator.py:654:        # 获取可用的实体类型列表，供 LLM 参考
./backend/app/services/simulation_config_generator.py:711:            logger.warning(f"事件配置LLM生成失败: {e}, 使用默认配置")
./backend/app/services/simulation_config_generator.py:719:    def _parse_event_config(self, result: Dict[str, Any]) -> EventConfig:
./backend/app/services/simulation_config_generator.py:730:        event_config: EventConfig,
./backend/app/services/simulation_config_generator.py:731:        agent_configs: List[AgentActivityConfig]
./backend/app/services/simulation_config_generator.py:738:        if not event_config.initial_posts:
./backend/app/services/simulation_config_generator.py:739:            return event_config
./backend/app/services/simulation_config_generator.py:743:        for agent in agent_configs:
./backend/app/services/simulation_config_generator.py:749:        # 类型映射表（处理 LLM 可能输出的不同格式）
./backend/app/services/simulation_config_generator.py:765:        for post in event_config.initial_posts:
./backend/app/services/simulation_config_generator.py:795:                if agent_configs:
./backend/app/services/simulation_config_generator.py:797:                    sorted_agents = sorted(agent_configs, key=lambda a: a.influence_weight, reverse=True)
./backend/app/services/simulation_config_generator.py:810:        event_config.initial_posts = updated_posts
./backend/app/services/simulation_config_generator.py:811:        return event_config
./backend/app/services/simulation_config_generator.py:813:    def _generate_agent_configs_batch(
./backend/app/services/simulation_config_generator.py:852:    "agent_configs": [
./backend/app/services/simulation_config_generator.py:874:            llm_configs = {cfg["agent_id"]: cfg for cfg in result.get("agent_configs", [])}
./backend/app/services/simulation_config_generator.py:876:            logger.warning(f"Agent配置批次LLM生成失败: {e}, 使用规则生成")
./backend/app/services/simulation_config_generator.py:877:            llm_configs = {}
./backend/app/services/simulation_config_generator.py:880:        configs = []
./backend/app/services/simulation_config_generator.py:883:            cfg = llm_configs.get(agent_id, {})
./backend/app/services/simulation_config_generator.py:885:            # 如果LLM没有生成，使用规则生成
./backend/app/services/simulation_config_generator.py:887:                cfg = self._generate_agent_config_by_rule(entity)
./backend/app/services/simulation_config_generator.py:889:            config = AgentActivityConfig(
./backend/app/services/simulation_config_generator.py:904:            configs.append(config)
./backend/app/services/simulation_config_generator.py:906:        return configs
./backend/app/services/simulation_config_generator.py:908:    def _generate_agent_config_by_rule(self, entity: EntityNode) -> Dict[str, Any]:
./backend/scripts/run_reddit_simulation.py:12:    python run_reddit_simulation.py --config /path/to/simulation_config.json
./backend/scripts/run_reddit_simulation.py:13:    python run_reddit_simulation.py --config /path/to/simulation_config.json --no-wait  # 完成后立即关闭
./backend/scripts/run_reddit_simulation.py:39:# 加载项目根目录的 .env 文件（包含 LLM_API_KEY 等配置）
./backend/scripts/run_reddit_simulation.py:40:from dotenv import load_dotenv
./backend/scripts/run_reddit_simulation.py:43:    load_dotenv(_env_file)
./backend/scripts/run_reddit_simulation.py:47:        load_dotenv(_backend_env)
./backend/scripts/run_reddit_simulation.py:99:    loggers_config = {
./backend/scripts/run_reddit_simulation.py:107:    for logger_name, log_file in loggers_config.items():
./backend/scripts/run_reddit_simulation.py:124:        LLMAction,
./backend/scripts/run_reddit_simulation.py:405:    def __init__(self, config_path: str, wait_for_commands: bool = True):
./backend/scripts/run_reddit_simulation.py:410:            config_path: 配置文件路径 (simulation_config.json)
./backend/scripts/run_reddit_simulation.py:413:        self.config_path = config_path
./backend/scripts/run_reddit_simulation.py:414:        self.config = self._load_config()
./backend/scripts/run_reddit_simulation.py:415:        self.simulation_dir = os.path.dirname(config_path)
./backend/scripts/run_reddit_simulation.py:421:    def _load_config(self) -> Dict[str, Any]:
./backend/scripts/run_reddit_simulation.py:423:        with open(self.config_path, 'r', encoding='utf-8') as f:
./backend/scripts/run_reddit_simulation.py:436:        创建LLM模型
./backend/scripts/run_reddit_simulation.py:439:        - LLM_API_KEY: API密钥
./backend/scripts/run_reddit_simulation.py:440:        - LLM_BASE_URL: API基础URL
./backend/scripts/run_reddit_simulation.py:441:        - LLM_MODEL_NAME: 模型名称
./backend/scripts/run_reddit_simulation.py:444:        llm_api_key = os.environ.get("LLM_API_KEY", "")
./backend/scripts/run_reddit_simulation.py:445:        llm_base_url = os.environ.get("LLM_BASE_URL", "")
./backend/scripts/run_reddit_simulation.py:446:        llm_model = os.environ.get("LLM_MODEL_NAME", "")
./backend/scripts/run_reddit_simulation.py:448:        # 如果 .env 中没有，则使用 config 作为备用
./backend/scripts/run_reddit_simulation.py:450:            llm_model = self.config.get("llm_model", "gpt-4o-mini")
./backend/scripts/run_reddit_simulation.py:453:        if llm_api_key:
./backend/scripts/run_reddit_simulation.py:454:            os.environ["OPENAI_API_KEY"] = llm_api_key
./backend/scripts/run_reddit_simulation.py:456:        if not os.environ.get("OPENAI_API_KEY"):
./backend/scripts/run_reddit_simulation.py:457:            raise ValueError("缺少 API Key 配置，请在项目根目录 .env 文件中设置 LLM_API_KEY")
./backend/scripts/run_reddit_simulation.py:460:            os.environ["OPENAI_API_BASE_URL"] = llm_base_url
./backend/scripts/run_reddit_simulation.py:462:        print(f"LLM配置: model={llm_model}, base_url={llm_base_url[:40] if llm_base_url else '默认'}...")
./backend/scripts/run_reddit_simulation.py:465:            model_platform=ModelPlatformType.OPENAI,
./backend/scripts/run_reddit_simulation.py:478:        time_config = self.config.get("time_config", {})
./backend/scripts/run_reddit_simulation.py:479:        agent_configs = self.config.get("agent_configs", [])
./backend/scripts/run_reddit_simulation.py:481:        base_min = time_config.get("agents_per_hour_min", 5)
./backend/scripts/run_reddit_simulation.py:482:        base_max = time_config.get("agents_per_hour_max", 20)
./backend/scripts/run_reddit_simulation.py:484:        peak_hours = time_config.get("peak_hours", [9, 10, 11, 14, 15, 20, 21, 22])
./backend/scripts/run_reddit_simulation.py:485:        off_peak_hours = time_config.get("off_peak_hours", [0, 1, 2, 3, 4, 5])
./backend/scripts/run_reddit_simulation.py:488:            multiplier = time_config.get("peak_activity_multiplier", 1.5)
./backend/scripts/run_reddit_simulation.py:490:            multiplier = time_config.get("off_peak_activity_multiplier", 0.3)
./backend/scripts/run_reddit_simulation.py:497:        for cfg in agent_configs:
./backend/scripts/run_reddit_simulation.py:531:        print(f"配置文件: {self.config_path}")
./backend/scripts/run_reddit_simulation.py:532:        print(f"模拟ID: {self.config.get('simulation_id', 'unknown')}")
./backend/scripts/run_reddit_simulation.py:536:        time_config = self.config.get("time_config", {})
./backend/scripts/run_reddit_simulation.py:537:        total_hours = time_config.get("total_simulation_hours", 72)
./backend/scripts/run_reddit_simulation.py:538:        minutes_per_round = time_config.get("minutes_per_round", 30)
./backend/scripts/run_reddit_simulation.py:554:        print(f"  - Agent数量: {len(self.config.get('agent_configs', []))}")
./backend/scripts/run_reddit_simulation.py:556:        print("\n初始化LLM模型...")
./backend/scripts/run_reddit_simulation.py:581:            semaphore=30,  # 限制最大并发 LLM 请求数，防止 API 过载
./backend/scripts/run_reddit_simulation.py:592:        event_config = self.config.get("event_config", {})
./backend/scripts/run_reddit_simulation.py:593:        initial_posts = event_config.get("initial_posts", [])
./backend/scripts/run_reddit_simulation.py:639:                agent: LLMAction()
./backend/scripts/run_reddit_simulation.py:698:        '--config', 
./backend/scripts/run_reddit_simulation.py:701:        help='配置文件路径 (simulation_config.json)'
./backend/scripts/run_reddit_simulation.py:722:    if not os.path.exists(args.config):
./backend/scripts/run_reddit_simulation.py:723:        print(f"错误: 配置文件不存在: {args.config}")
./backend/scripts/run_reddit_simulation.py:727:    simulation_dir = os.path.dirname(args.config) or "."
./backend/scripts/run_reddit_simulation.py:731:        config_path=args.config,
./backend/scripts/run_parallel_simulation.py:13:    python run_parallel_simulation.py --config simulation_config.json
./backend/scripts/run_parallel_simulation.py:14:    python run_parallel_simulation.py --config simulation_config.json --no-wait  # 完成后立即关闭
./backend/scripts/run_parallel_simulation.py:15:    python run_parallel_simulation.py --config simulation_config.json --twitter-only
./backend/scripts/run_parallel_simulation.py:16:    python run_parallel_simulation.py --config simulation_config.json --reddit-only
./backend/scripts/run_parallel_simulation.py:38:    os.environ.setdefault('PYTHONUTF8', '1')
./backend/scripts/run_parallel_simulation.py:39:    os.environ.setdefault('PYTHONIOENCODING', 'utf-8')
./backend/scripts/run_parallel_simulation.py:42:    if hasattr(sys.stdout, 'reconfigure'):
./backend/scripts/run_parallel_simulation.py:43:        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
./backend/scripts/run_parallel_simulation.py:44:    if hasattr(sys.stderr, 'reconfigure'):
./backend/scripts/run_parallel_simulation.py:45:        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
./backend/scripts/run_parallel_simulation.py:92:# 加载项目根目录的 .env 文件（包含 LLM_API_KEY 等配置）
./backend/scripts/run_parallel_simulation.py:93:from dotenv import load_dotenv
./backend/scripts/run_parallel_simulation.py:96:    load_dotenv(_env_file)
./backend/scripts/run_parallel_simulation.py:102:        load_dotenv(_backend_env)
./backend/scripts/run_parallel_simulation.py:166:        LLMAction,
./backend/scripts/run_parallel_simulation.py:604:def load_config(config_path: str) -> Dict[str, Any]:
./backend/scripts/run_parallel_simulation.py:606:    with open(config_path, 'r', encoding='utf-8') as f:
./backend/scripts/run_parallel_simulation.py:633:def get_agent_names_from_config(config: Dict[str, Any]) -> Dict[int, str]:
./backend/scripts/run_parallel_simulation.py:635:    从 simulation_config 中获取 agent_id -> entity_name 的映射
./backend/scripts/run_parallel_simulation.py:640:        config: simulation_config.json 的内容
./backend/scripts/run_parallel_simulation.py:646:    agent_configs = config.get("agent_configs", [])
./backend/scripts/run_parallel_simulation.py:648:    for agent_config in agent_configs:
./backend/scripts/run_parallel_simulation.py:649:        agent_id = agent_config.get("agent_id")
./backend/scripts/run_parallel_simulation.py:650:        entity_name = agent_config.get("entity_name", f"Agent_{agent_id}")
./backend/scripts/run_parallel_simulation.py:984:def create_model(config: Dict[str, Any], use_boost: bool = False):
./backend/scripts/run_parallel_simulation.py:986:    创建LLM模型
./backend/scripts/run_parallel_simulation.py:988:    支持双 LLM 配置，用于并行模拟时提速：
./backend/scripts/run_parallel_simulation.py:989:    - 通用配置：LLM_API_KEY, LLM_BASE_URL, LLM_MODEL_NAME
./backend/scripts/run_parallel_simulation.py:990:    - 加速配置（可选）：LLM_BOOST_API_KEY, LLM_BOOST_BASE_URL, LLM_BOOST_MODEL_NAME
./backend/scripts/run_parallel_simulation.py:992:    如果配置了加速 LLM，并行模拟时可以让不同平台使用不同的 API 服务商，提高并发能力。
./backend/scripts/run_parallel_simulation.py:995:        config: 模拟配置字典
./backend/scripts/run_parallel_simulation.py:996:        use_boost: 是否使用加速 LLM 配置（如果可用）
./backend/scripts/run_parallel_simulation.py:999:    boost_api_key = os.environ.get("LLM_BOOST_API_KEY", "")
./backend/scripts/run_parallel_simulation.py:1000:    boost_base_url = os.environ.get("LLM_BOOST_BASE_URL", "")
./backend/scripts/run_parallel_simulation.py:1001:    boost_model = os.environ.get("LLM_BOOST_MODEL_NAME", "")
./backend/scripts/run_parallel_simulation.py:1002:    has_boost_config = bool(boost_api_key)
./backend/scripts/run_parallel_simulation.py:1004:    # 根据参数和配置情况选择使用哪个 LLM
./backend/scripts/run_parallel_simulation.py:1005:    if use_boost and has_boost_config:
./backend/scripts/run_parallel_simulation.py:1007:        llm_api_key = boost_api_key
./backend/scripts/run_parallel_simulation.py:1009:        llm_model = boost_model or os.environ.get("LLM_MODEL_NAME", "")
./backend/scripts/run_parallel_simulation.py:1010:        config_label = "[加速LLM]"
./backend/scripts/run_parallel_simulation.py:1013:        llm_api_key = os.environ.get("LLM_API_KEY", "")
./backend/scripts/run_parallel_simulation.py:1014:        llm_base_url = os.environ.get("LLM_BASE_URL", "")
./backend/scripts/run_parallel_simulation.py:1015:        llm_model = os.environ.get("LLM_MODEL_NAME", "")
./backend/scripts/run_parallel_simulation.py:1016:        config_label = "[通用LLM]"
./backend/scripts/run_parallel_simulation.py:1018:    # 如果 .env 中没有模型名，则使用 config 作为备用
./backend/scripts/run_parallel_simulation.py:1020:        llm_model = config.get("llm_model", "gpt-4o-mini")
./backend/scripts/run_parallel_simulation.py:1023:    if llm_api_key:
./backend/scripts/run_parallel_simulation.py:1024:        os.environ["OPENAI_API_KEY"] = llm_api_key
./backend/scripts/run_parallel_simulation.py:1026:    if not os.environ.get("OPENAI_API_KEY"):
./backend/scripts/run_parallel_simulation.py:1027:        raise ValueError("缺少 API Key 配置，请在项目根目录 .env 文件中设置 LLM_API_KEY")
./backend/scripts/run_parallel_simulation.py:1030:        os.environ["OPENAI_API_BASE_URL"] = llm_base_url
./backend/scripts/run_parallel_simulation.py:1032:    print(f"{config_label} model={llm_model}, base_url={llm_base_url[:40] if llm_base_url else '默认'}...")
./backend/scripts/run_parallel_simulation.py:1035:        model_platform=ModelPlatformType.OPENAI,
./backend/scripts/run_parallel_simulation.py:1042:    config: Dict[str, Any],
./backend/scripts/run_parallel_simulation.py:1047:    time_config = config.get("time_config", {})
./backend/scripts/run_parallel_simulation.py:1048:    agent_configs = config.get("agent_configs", [])
./backend/scripts/run_parallel_simulation.py:1050:    base_min = time_config.get("agents_per_hour_min", 5)
./backend/scripts/run_parallel_simulation.py:1051:    base_max = time_config.get("agents_per_hour_max", 20)
./backend/scripts/run_parallel_simulation.py:1053:    peak_hours = time_config.get("peak_hours", [9, 10, 11, 14, 15, 20, 21, 22])
./backend/scripts/run_parallel_simulation.py:1054:    off_peak_hours = time_config.get("off_peak_hours", [0, 1, 2, 3, 4, 5])
./backend/scripts/run_parallel_simulation.py:1057:        multiplier = time_config.get("peak_activity_multiplier", 1.5)
./backend/scripts/run_parallel_simulation.py:1059:        multiplier = time_config.get("off_peak_activity_multiplier", 0.3)
./backend/scripts/run_parallel_simulation.py:1066:    for cfg in agent_configs:
./backend/scripts/run_parallel_simulation.py:1102:    config: Dict[str, Any], 
./backend/scripts/run_parallel_simulation.py:1111:        config: 模拟配置
./backend/scripts/run_parallel_simulation.py:1129:    # Twitter 使用通用 LLM 配置
./backend/scripts/run_parallel_simulation.py:1130:    model = create_model(config, use_boost=False)
./backend/scripts/run_parallel_simulation.py:1145:    agent_names = get_agent_names_from_config(config)
./backend/scripts/run_parallel_simulation.py:1159:        semaphore=30,  # 限制最大并发 LLM 请求数，防止 API 过载
./backend/scripts/run_parallel_simulation.py:1166:        action_logger.log_simulation_start(config)
./backend/scripts/run_parallel_simulation.py:1172:    event_config = config.get("event_config", {})
./backend/scripts/run_parallel_simulation.py:1173:    initial_posts = event_config.get("initial_posts", [])
./backend/scripts/run_parallel_simulation.py:1214:    time_config = config.get("time_config", {})
./backend/scripts/run_parallel_simulation.py:1215:    total_hours = time_config.get("total_simulation_hours", 72)
./backend/scripts/run_parallel_simulation.py:1216:    minutes_per_round = time_config.get("minutes_per_round", 30)
./backend/scripts/run_parallel_simulation.py:1240:            result.env, config, simulated_hour, round_num
./backend/scripts/run_parallel_simulation.py:1253:        actions = {agent: LLMAction() for _, agent in active_agents}
./backend/scripts/run_parallel_simulation.py:1294:    config: Dict[str, Any], 
./backend/scripts/run_parallel_simulation.py:1303:        config: 模拟配置
./backend/scripts/run_parallel_simulation.py:1321:    # Reddit 使用加速 LLM 配置（如果有的话，否则回退到通用配置）
./backend/scripts/run_parallel_simulation.py:1322:    model = create_model(config, use_boost=True)
./backend/scripts/run_parallel_simulation.py:1336:    agent_names = get_agent_names_from_config(config)
./backend/scripts/run_parallel_simulation.py:1350:        semaphore=30,  # 限制最大并发 LLM 请求数，防止 API 过载
./backend/scripts/run_parallel_simulation.py:1357:        action_logger.log_simulation_start(config)
./backend/scripts/run_parallel_simulation.py:1363:    event_config = config.get("event_config", {})
./backend/scripts/run_parallel_simulation.py:1364:    initial_posts = event_config.get("initial_posts", [])
./backend/scripts/run_parallel_simulation.py:1413:    time_config = config.get("time_config", {})
./backend/scripts/run_parallel_simulation.py:1414:    total_hours = time_config.get("total_simulation_hours", 72)
./backend/scripts/run_parallel_simulation.py:1415:    minutes_per_round = time_config.get("minutes_per_round", 30)
./backend/scripts/run_parallel_simulation.py:1439:            result.env, config, simulated_hour, round_num
./backend/scripts/run_parallel_simulation.py:1452:        actions = {agent: LLMAction() for _, agent in active_agents}
./backend/scripts/run_parallel_simulation.py:1495:        '--config', 
./backend/scripts/run_parallel_simulation.py:1498:        help='配置文件路径 (simulation_config.json)'
./backend/scripts/run_parallel_simulation.py:1529:    if not os.path.exists(args.config):
./backend/scripts/run_parallel_simulation.py:1530:        print(f"错误: 配置文件不存在: {args.config}")
./backend/scripts/run_parallel_simulation.py:1533:    config = load_config(args.config)
./backend/scripts/run_parallel_simulation.py:1534:    simulation_dir = os.path.dirname(args.config) or "."
./backend/scripts/run_parallel_simulation.py:1547:    log_manager.info(f"配置文件: {args.config}")
./backend/scripts/run_parallel_simulation.py:1548:    log_manager.info(f"模拟ID: {config.get('simulation_id', 'unknown')}")
./backend/scripts/run_parallel_simulation.py:1552:    time_config = config.get("time_config", {})
./backend/scripts/run_parallel_simulation.py:1553:    total_hours = time_config.get('total_simulation_hours', 72)
./backend/scripts/run_parallel_simulation.py:1554:    minutes_per_round = time_config.get('minutes_per_round', 30)
./backend/scripts/run_parallel_simulation.py:1555:    config_total_rounds = (total_hours * 60) // minutes_per_round
./backend/scripts/run_parallel_simulation.py:1560:    log_manager.info(f"  - 配置总轮数: {config_total_rounds}")
./backend/scripts/run_parallel_simulation.py:1563:        if args.max_rounds < config_total_rounds:
./backend/scripts/run_parallel_simulation.py:1565:    log_manager.info(f"  - Agent数量: {len(config.get('agent_configs', []))}")
./backend/scripts/run_parallel_simulation.py:1580:        twitter_result = await run_twitter_simulation(config, simulation_dir, twitter_logger, log_manager, args.max_rounds)
./backend/scripts/run_parallel_simulation.py:1582:        reddit_result = await run_reddit_simulation(config, simulation_dir, reddit_logger, log_manager, args.max_rounds)
./backend/scripts/run_parallel_simulation.py:1586:            run_twitter_simulation(config, simulation_dir, twitter_logger, log_manager, args.max_rounds),
./backend/scripts/run_parallel_simulation.py:1587:            run_reddit_simulation(config, simulation_dir, reddit_logger, log_manager, args.max_rounds),
./backend/scripts/run_twitter_simulation.py:12:    python run_twitter_simulation.py --config /path/to/simulation_config.json
./backend/scripts/run_twitter_simulation.py:13:    python run_twitter_simulation.py --config /path/to/simulation_config.json --no-wait  # 完成后立即关闭
./backend/scripts/run_twitter_simulation.py:39:# 加载项目根目录的 .env 文件（包含 LLM_API_KEY 等配置）
./backend/scripts/run_twitter_simulation.py:40:from dotenv import load_dotenv
./backend/scripts/run_twitter_simulation.py:43:    load_dotenv(_env_file)
./backend/scripts/run_twitter_simulation.py:47:        load_dotenv(_backend_env)
./backend/scripts/run_twitter_simulation.py:99:    loggers_config = {
./backend/scripts/run_twitter_simulation.py:107:    for logger_name, log_file in loggers_config.items():
./backend/scripts/run_twitter_simulation.py:124:        LLMAction,
./backend/scripts/run_twitter_simulation.py:398:    def __init__(self, config_path: str, wait_for_commands: bool = True):
./backend/scripts/run_twitter_simulation.py:403:            config_path: 配置文件路径 (simulation_config.json)
./backend/scripts/run_twitter_simulation.py:406:        self.config_path = config_path
./backend/scripts/run_twitter_simulation.py:407:        self.config = self._load_config()
./backend/scripts/run_twitter_simulation.py:408:        self.simulation_dir = os.path.dirname(config_path)
./backend/scripts/run_twitter_simulation.py:414:    def _load_config(self) -> Dict[str, Any]:
./backend/scripts/run_twitter_simulation.py:416:        with open(self.config_path, 'r', encoding='utf-8') as f:
./backend/scripts/run_twitter_simulation.py:429:        创建LLM模型
./backend/scripts/run_twitter_simulation.py:432:        - LLM_API_KEY: API密钥
./backend/scripts/run_twitter_simulation.py:433:        - LLM_BASE_URL: API基础URL
./backend/scripts/run_twitter_simulation.py:434:        - LLM_MODEL_NAME: 模型名称
./backend/scripts/run_twitter_simulation.py:437:        llm_api_key = os.environ.get("LLM_API_KEY", "")
./backend/scripts/run_twitter_simulation.py:438:        llm_base_url = os.environ.get("LLM_BASE_URL", "")
./backend/scripts/run_twitter_simulation.py:439:        llm_model = os.environ.get("LLM_MODEL_NAME", "")
./backend/scripts/run_twitter_simulation.py:441:        # 如果 .env 中没有，则使用 config 作为备用
./backend/scripts/run_twitter_simulation.py:443:            llm_model = self.config.get("llm_model", "gpt-4o-mini")
./backend/scripts/run_twitter_simulation.py:446:        if llm_api_key:
./backend/scripts/run_twitter_simulation.py:447:            os.environ["OPENAI_API_KEY"] = llm_api_key
./backend/scripts/run_twitter_simulation.py:449:        if not os.environ.get("OPENAI_API_KEY"):
./backend/scripts/run_twitter_simulation.py:450:            raise ValueError("缺少 API Key 配置，请在项目根目录 .env 文件中设置 LLM_API_KEY")
./backend/scripts/run_twitter_simulation.py:453:            os.environ["OPENAI_API_BASE_URL"] = llm_base_url
./backend/scripts/run_twitter_simulation.py:455:        print(f"LLM配置: model={llm_model}, base_url={llm_base_url[:40] if llm_base_url else '默认'}...")
./backend/scripts/run_twitter_simulation.py:458:            model_platform=ModelPlatformType.OPENAI,
./backend/scripts/run_twitter_simulation.py:479:        time_config = self.config.get("time_config", {})
./backend/scripts/run_twitter_simulation.py:480:        agent_configs = self.config.get("agent_configs", [])
./backend/scripts/run_twitter_simulation.py:483:        base_min = time_config.get("agents_per_hour_min", 5)
./backend/scripts/run_twitter_simulation.py:484:        base_max = time_config.get("agents_per_hour_max", 20)
./backend/scripts/run_twitter_simulation.py:487:        peak_hours = time_config.get("peak_hours", [9, 10, 11, 14, 15, 20, 21, 22])
./backend/scripts/run_twitter_simulation.py:488:        off_peak_hours = time_config.get("off_peak_hours", [0, 1, 2, 3, 4, 5])
./backend/scripts/run_twitter_simulation.py:491:            multiplier = time_config.get("peak_activity_multiplier", 1.5)
./backend/scripts/run_twitter_simulation.py:493:            multiplier = time_config.get("off_peak_activity_multiplier", 0.3)
./backend/scripts/run_twitter_simulation.py:501:        for cfg in agent_configs:
./backend/scripts/run_twitter_simulation.py:539:        print(f"配置文件: {self.config_path}")
./backend/scripts/run_twitter_simulation.py:540:        print(f"模拟ID: {self.config.get('simulation_id', 'unknown')}")
./backend/scripts/run_twitter_simulation.py:545:        time_config = self.config.get("time_config", {})
./backend/scripts/run_twitter_simulation.py:546:        total_hours = time_config.get("total_simulation_hours", 72)
./backend/scripts/run_twitter_simulation.py:547:        minutes_per_round = time_config.get("minutes_per_round", 30)
./backend/scripts/run_twitter_simulation.py:565:        print(f"  - Agent数量: {len(self.config.get('agent_configs', []))}")
./backend/scripts/run_twitter_simulation.py:568:        print("\n初始化LLM模型...")
./backend/scripts/run_twitter_simulation.py:596:            semaphore=30,  # 限制最大并发 LLM 请求数，防止 API 过载
./backend/scripts/run_twitter_simulation.py:607:        event_config = self.config.get("event_config", {})
./backend/scripts/run_twitter_simulation.py:608:        initial_posts = event_config.get("initial_posts", [])
./backend/scripts/run_twitter_simulation.py:649:                agent: LLMAction()
./backend/scripts/run_twitter_simulation.py:710:        '--config', 
./backend/scripts/run_twitter_simulation.py:713:        help='配置文件路径 (simulation_config.json)'
./backend/scripts/run_twitter_simulation.py:734:    if not os.path.exists(args.config):
./backend/scripts/run_twitter_simulation.py:735:        print(f"错误: 配置文件不存在: {args.config}")
./backend/scripts/run_twitter_simulation.py:739:    simulation_dir = os.path.dirname(args.config) or "."
./backend/scripts/run_twitter_simulation.py:743:        config_path=args.config,
./backend/scripts/action_logger.py:92:    def log_simulation_start(self, config: Dict[str, Any]):
./backend/scripts/action_logger.py:98:            "total_rounds": config.get("time_config", {}).get("total_simulation_hours", 72) * 2,
./backend/scripts/action_logger.py:99:            "agents_count": len(config.get("agent_configs", [])),
./backend/scripts/action_logger.py:266:    def log_simulation_start(self, platform: str, config: Dict[str, Any]):
./backend/scripts/action_logger.py:271:            "total_rounds": config.get("time_config", {}).get("total_simulation_hours", 72) * 2,
```

## 10. 前端 / 后端 / 入口文件扫描

```text
./frontend/vite.config.js:6:export default defineConfig({
./frontend/src/main.js:3:import router from './router'
./frontend/src/main.js:8:app.use(router)
./frontend/src/api/index.js:69:export default service
./frontend/src/i18n/index.js:27:export default i18n
./frontend/src/store/pendingUpload.js:33:export default state
./frontend/src/router/index.js:1:import { createRouter, createWebHistory } from 'vue-router'
./frontend/src/router/index.js:9:const routes = [
./frontend/src/router/index.js:47:const router = createRouter({
./frontend/src/router/index.js:49:  routes
./frontend/src/router/index.js:52:export default router
./backend/run.py:25:def main():
./backend/run.py:45:    app.run(host=host, port=port, debug=debug, threaded=True)
./backend/run.py:48:if __name__ == '__main__':
./backend/run.py:49:    main()
./backend/app/config.py:21:    """Flask配置类"""
./backend/app/config.py:23:    # Flask配置
./backend/app/__init__.py:2:MiroFish Backend - Flask应用工厂
./backend/app/__init__.py:12:from flask import Flask, request
./backend/app/__init__.py:20:    """Flask应用工厂函数"""
./backend/app/__init__.py:21:    app = Flask(__name__)
./backend/app/__init__.py:25:    # Flask >= 2.3 使用 app.json.ensure_ascii，旧版本使用 JSON_AS_ASCII 配置
./backend/app/__init__.py:72:    @app.route('/health')
./backend/app/models/project.py:247:            file_storage: Flask的FileStorage对象
./backend/app/api/simulation.py:48:@simulation_bp.route('/entities/<graph_id>', methods=['GET'])
./backend/app/api/simulation.py:93:@simulation_bp.route('/entities/<graph_id>/<entity_uuid>', methods=['GET'])
./backend/app/api/simulation.py:126:@simulation_bp.route('/entities/<graph_id>/by-type/<entity_type>', methods=['GET'])
./backend/app/api/simulation.py:165:@simulation_bp.route('/create', methods=['POST'])
./backend/app/api/simulation.py:359:@simulation_bp.route('/prepare', methods=['POST'])
./backend/app/api/simulation.py:612:        thread.start()
./backend/app/api/simulation.py:642:@simulation_bp.route('/prepare/status', methods=['POST'])
./backend/app/api/simulation.py:755:@simulation_bp.route('/<simulation_id>', methods=['GET'])
./backend/app/api/simulation.py:788:@simulation_bp.route('/list', methods=['GET'])
./backend/app/api/simulation.py:876:@simulation_bp.route('/history', methods=['GET'])
./backend/app/api/simulation.py:990:@simulation_bp.route('/<simulation_id>/profiles', methods=['GET'])
./backend/app/api/simulation.py:1028:@simulation_bp.route('/<simulation_id>/profiles/realtime', methods=['GET'])
./backend/app/api/simulation.py:1138:@simulation_bp.route('/<simulation_id>/config/realtime', methods=['GET'])
./backend/app/api/simulation.py:1258:@simulation_bp.route('/<simulation_id>/config', methods=['GET'])
./backend/app/api/simulation.py:1294:@simulation_bp.route('/<simulation_id>/config/download', methods=['GET'])
./backend/app/api/simulation.py:1323:@simulation_bp.route('/script/<script_name>/download', methods=['GET'])
./backend/app/api/simulation.py:1377:@simulation_bp.route('/generate-profiles', methods=['POST'])
./backend/app/api/simulation.py:1451:@simulation_bp.route('/start', methods=['POST'])
./backend/app/api/simulation.py:1644:@simulation_bp.route('/stop', methods=['POST'])
./backend/app/api/simulation.py:1705:@simulation_bp.route('/<simulation_id>/run-status', methods=['GET'])
./backend/app/api/simulation.py:1763:@simulation_bp.route('/<simulation_id>/run-status/detail', methods=['GET'])
./backend/app/api/simulation.py:1864:@simulation_bp.route('/<simulation_id>/actions', methods=['GET'])
./backend/app/api/simulation.py:1918:@simulation_bp.route('/<simulation_id>/timeline', methods=['GET'])
./backend/app/api/simulation.py:1958:@simulation_bp.route('/<simulation_id>/agent-stats', methods=['GET'])
./backend/app/api/simulation.py:1987:@simulation_bp.route('/<simulation_id>/posts', methods=['GET'])
./backend/app/api/simulation.py:2065:@simulation_bp.route('/<simulation_id>/comments', methods=['GET'])
./backend/app/api/simulation.py:2142:@simulation_bp.route('/interview', methods=['POST'])
./backend/app/api/simulation.py:2271:@simulation_bp.route('/interview/batch', methods=['POST'])
./backend/app/api/simulation.py:2409:@simulation_bp.route('/interview/all', methods=['POST'])
./backend/app/api/simulation.py:2512:@simulation_bp.route('/interview/history', methods=['POST'])
./backend/app/api/simulation.py:2584:@simulation_bp.route('/env-status', methods=['POST'])
./backend/app/api/simulation.py:2649:@simulation_bp.route('/close-env', methods=['POST'])
./backend/app/api/graph.py:36:@graph_bp.route('/project/<project_id>', methods=['GET'])
./backend/app/api/graph.py:55:@graph_bp.route('/project/list', methods=['GET'])
./backend/app/api/graph.py:70:@graph_bp.route('/project/<project_id>', methods=['DELETE'])
./backend/app/api/graph.py:89:@graph_bp.route('/project/<project_id>/reset', methods=['POST'])
./backend/app/api/graph.py:122:@graph_bp.route('/ontology/generate', methods=['POST'])
./backend/app/api/graph.py:260:@graph_bp.route('/build', methods=['POST'])
./backend/app/api/graph.py:513:        thread.start()
./backend/app/api/graph.py:534:@graph_bp.route('/task/<task_id>', methods=['GET'])
./backend/app/api/graph.py:553:@graph_bp.route('/tasks', methods=['GET'])
./backend/app/api/graph.py:569:@graph_bp.route('/data/<graph_id>', methods=['GET'])
./backend/app/api/graph.py:597:@graph_bp.route('/delete/<graph_id>', methods=['DELETE'])
./backend/app/api/report.py:25:@report_bp.route('/generate', methods=['POST'])
./backend/app/api/report.py:180:        thread.start()
./backend/app/api/report.py:203:@report_bp.route('/generate/status', methods=['POST'])
./backend/app/api/report.py:277:@report_bp.route('/<report_id>', methods=['GET'])
./backend/app/api/report.py:319:@report_bp.route('/by-simulation/<simulation_id>', methods=['GET'])
./backend/app/api/report.py:358:@report_bp.route('/list', methods=['GET'])
./backend/app/api/report.py:398:@report_bp.route('/<report_id>/download', methods=['GET'])
./backend/app/api/report.py:444:@report_bp.route('/<report_id>', methods=['DELETE'])
./backend/app/api/report.py:472:@report_bp.route('/chat', methods=['POST'])
./backend/app/api/report.py:569:@report_bp.route('/<report_id>/progress', methods=['GET'])
./backend/app/api/report.py:610:@report_bp.route('/<report_id>/sections', methods=['GET'])
./backend/app/api/report.py:661:@report_bp.route('/<report_id>/section/<int:section_index>', methods=['GET'])
./backend/app/api/report.py:707:@report_bp.route('/check/<simulation_id>', methods=['GET'])
./backend/app/api/report.py:758:@report_bp.route('/<report_id>/agent-log', methods=['GET'])
./backend/app/api/report.py:817:@report_bp.route('/<report_id>/agent-log/stream', methods=['GET'])
./backend/app/api/report.py:853:@report_bp.route('/<report_id>/console-log', methods=['GET'])
./backend/app/api/report.py:899:@report_bp.route('/<report_id>/console-log/stream', methods=['GET'])
./backend/app/api/report.py:935:@report_bp.route('/tools/search', methods=['POST'])
./backend/app/api/report.py:983:@report_bp.route('/tools/statistics', methods=['POST'])
./backend/app/services/report_agent.py:100:    def log_start(self, simulation_id: str, graph_id: str, simulation_requirement: str):
./backend/app/services/report_agent.py:113:    def log_planning_start(self):
./backend/app/services/report_agent.py:143:    def log_section_start(self, section_title: str, section_index: int):
./backend/app/services/report_agent.py:1253:            self.report_logger.log_section_start(section.title, section_index)
./backend/app/services/report_agent.py:1583:            self.report_logger.log_start(
./backend/app/services/report_agent.py:1606:            self.report_logger.log_planning_start()
./backend/app/services/simulation_runner.py:468:            monitor_thread.start()
./backend/app/services/simulation_runner.py:736:                subprocess.run(
./backend/app/services/simulation_runner.py:746:                    subprocess.run(
./backend/app/services/simulation_runner.py:1292:        在 Flask 应用启动时调用，确保服务器关闭时清理所有模拟进程
./backend/app/services/simulation_runner.py:1299:        # Flask debug 模式下，只在 reloader 子进程中注册清理（实际运行应用的进程）
./backend/app/services/simulation_runner.py:1326:            # 调用原有的信号处理器，让 Flask 正常退出
./backend/app/services/simulation_ipc.py:3:用于Flask后端和模拟脚本之间的进程间通信
./backend/app/services/simulation_ipc.py:6:1. Flask写入命令到 commands/ 目录
./backend/app/services/simulation_ipc.py:8:3. Flask轮询响应目录获取结果
./backend/app/services/simulation_ipc.py:97:    模拟IPC客户端（Flask端使用）
./backend/app/services/simulation_ipc.py:313:    def start(self):
./backend/app/services/graph_builder.py:96:        thread.start()
./backend/app/services/zep_graph_memory_updater.py:275:    def start(self):
./backend/app/services/zep_graph_memory_updater.py:290:        self._worker_thread.start()
./backend/app/services/zep_graph_memory_updater.py:507:            updater.start()
./backend/scripts/run_reddit_simulation.py:16:import argparse
./backend/scripts/run_reddit_simulation.py:523:    async def run(self, max_rounds: int = None):
./backend/scripts/run_reddit_simulation.py:695:async def main():
./backend/scripts/run_reddit_simulation.py:696:    parser = argparse.ArgumentParser(description='OASIS Reddit模拟')
./backend/scripts/run_reddit_simulation.py:734:    await runner.run(max_rounds=args.max_rounds)
./backend/scripts/run_reddit_simulation.py:759:if __name__ == "__main__":
./backend/scripts/run_reddit_simulation.py:762:        asyncio.run(main())
./backend/scripts/run_parallel_simulation.py:67:import argparse
./backend/scripts/run_parallel_simulation.py:1166:        action_logger.log_simulation_start(config)
./backend/scripts/run_parallel_simulation.py:1177:        action_logger.log_round_start(0, 0)  # round 0, simulated_hour 0
./backend/scripts/run_parallel_simulation.py:1245:            action_logger.log_round_start(round_num + 1, simulated_hour)
./backend/scripts/run_parallel_simulation.py:1357:        action_logger.log_simulation_start(config)
./backend/scripts/run_parallel_simulation.py:1368:        action_logger.log_round_start(0, 0)  # round 0, simulated_hour 0
./backend/scripts/run_parallel_simulation.py:1444:            action_logger.log_round_start(round_num + 1, simulated_hour)
./backend/scripts/run_parallel_simulation.py:1492:async def main():
./backend/scripts/run_parallel_simulation.py:1493:    parser = argparse.ArgumentParser(description='OASIS双平台并行模拟')
./backend/scripts/run_parallel_simulation.py:1684:if __name__ == "__main__":
./backend/scripts/run_parallel_simulation.py:1687:        asyncio.run(main())
./backend/scripts/run_twitter_simulation.py:16:import argparse
./backend/scripts/run_twitter_simulation.py:531:    async def run(self, max_rounds: int = None):
./backend/scripts/run_twitter_simulation.py:707:async def main():
./backend/scripts/run_twitter_simulation.py:708:    parser = argparse.ArgumentParser(description='OASIS Twitter模拟')
./backend/scripts/run_twitter_simulation.py:746:    await runner.run(max_rounds=args.max_rounds)
./backend/scripts/run_twitter_simulation.py:771:if __name__ == "__main__":
./backend/scripts/run_twitter_simulation.py:774:        asyncio.run(main())
./backend/scripts/test_profile_format.py:162:if __name__ == "__main__":
./backend/scripts/action_logger.py:68:    def log_round_start(self, round_num: int, simulated_hour: int):
./backend/scripts/action_logger.py:92:    def log_simulation_start(self, config: Dict[str, Any]):
./backend/scripts/action_logger.py:242:    def log_round_start(self, round_num: int, simulated_hour: int, platform: str):
./backend/scripts/action_logger.py:266:    def log_simulation_start(self, platform: str, config: Dict[str, Any]):
```

## 11. 数据结构 / Schema / Type / Model 扫描

```text
./locales/zh.json:60:    "step04Desc": "ReportAgent拥有丰富的工具集与模拟后环境进行深度交互",
./locales/zh.json:62:    "step05Desc": "与模拟世界中的任意一位进行对话 & 与ReportAgent进行对话",
./locales/zh.json:89:    "entityNodes": "实体节点",
./locales/zh.json:90:    "relationEdges": "关系边",
./locales/zh.json:91:    "schemaTypes": "SCHEMA类型",
./locales/zh.json:104:    "generateAgentPersona": "生成 Agent 人设",
./locales/zh.json:105:    "generateAgentPersonaDesc": "结合上下文，自动调用工具从知识图谱梳理实体与关系，初始化模拟个体，并基于现实种子赋予他们独特的行为与记忆",
./locales/zh.json:109:    "generatedAgentPersonas": "已生成的 Agent 人设",
./locales/zh.json:163:    "profileModalPersona": "详细人设背景",
./locales/zh.json:168:    "personaDimMemory": "独特记忆印记",
./locales/zh.json:169:    "personaDimMemoryDesc": "基于现实种子形成的记忆",
./locales/zh.json:180:    "startGenerateReport": "开始生成结果报告",
./locales/zh.json:181:    "generatingReport": "启动中...",
./locales/zh.json:185:    "graphMemoryUpdateEnabled": "已开启动态图谱更新模式",
./locales/zh.json:207:    "startGenerateReportBtn": "开始生成结果报告",
./locales/zh.json:208:    "generatingReportBtn": "启动中..."
./locales/zh.json:213:    "waitingForReportAgent": "Waiting for Report Agent...",
./locales/zh.json:243:    "tabEdges": "关系 ({count})",
./locales/zh.json:244:    "tabNodes": "节点 ({count})",
./locales/zh.json:247:    "panelRelatedEdges": "相关关系",
./locales/zh.json:248:    "panelRelatedNodes": "相关节点",
./locales/zh.json:255:    "chatWithReportAgent": "与Report Agent对话",
./locales/zh.json:259:    "reportAgentChat": "Report Agent - Chat",
./locales/zh.json:262:    "toolInsightForgeDesc": "对齐现实世界种子数据与模拟环境状态，结合Global/Local Memory机制，提供跨时空的深度归因分析",
./locales/zh.json:270:    "chatEmptyReportAgent": "与 Report Agent 对话，深入了解报告内容",
./locales/zh.json:290:    "graphMemoryRealtime": "GraphRAG长短期记忆实时更新中",
./locales/zh.json:293:    "nodeDetails": "Node Details",
./locales/zh.json:304:    "analysisReport": "分析报告",
./locales/zh.json:362:    "graphIdRequiredForMemory": "启用图谱记忆更新需要有效的 graph_id，请确保项目已构建图谱",
./locales/zh.json:372:    "noReportForSim": "该模拟暂无报告: {id}",
./locales/zh.json:391:    "initReportAgent": "初始化Report Agent..."
./locales/zh.json:419:    "readingNodeData": "正在读取节点数据...",
./locales/zh.json:427:    "initReport": "初始化报告...",
./locales/zh.json:432:    "assemblingReport": "正在组装完整报告...",
./locales/zh.json:529:    "graphMemoryUpdateEnabled": "已开启动态图谱更新模式",
./locales/zh.json:541:    "startingReportGen": "正在启动报告生成...",
./locales/zh.json:548:    "sendToReportAgent": "向 Report Agent 发送: {message}...",
./locales/zh.json:549:    "reportAgentReplied": "Report Agent 已回复",
./locales/zh.json:555:    "loadReportData": "加载报告数据: {id}",
./locales/zh.json:556:    "loadReportFailed": "加载报告失败: {error}",
./locales/zh.json:558:    "loadReportLogFailed": "加载报告日志失败: {error}",
./locales/zh.json:562:    "reportViewInit": "ReportView 初始化",
./locales/zh.json:563:    "getReportInfoFailed": "获取报告信息失败: {error}",
./locales/zh.json:582:    "agentInitDone": "ReportAgent 初始化完成: graph_id={graphId}, simulation_id={simulationId}",
./locales/zh.json:602:    "agentChat": "Report Agent对话: {message}...",
./locales/zh.json:603:    "fetchReportFailed": "获取报告内容失败: {error}",
./locales/zh.json:606:    "fullReportAssembled": "完整报告已组装: {reportId}",
./locales/zh.json:623:    "fetchingAllNodes": "获取图谱 {graphId} 的所有节点...",
./locales/zh.json:624:    "fetchedNodes": "获取到 {count} 个节点",
./locales/zh.json:625:    "fetchingAllEdges": "获取图谱 {graphId} 的所有边...",
./locales/zh.json:626:    "fetchedEdges": "获取到 {count} 条边",
./locales/zh.json:627:    "fetchingNodeDetail": "获取节点详情: {uuid}...",
./locales/zh.json:628:    "fetchNodeDetailOp": "获取节点详情(uuid={uuid}...)",
./locales/zh.json:629:    "fetchNodeDetailFailed": "获取节点详情失败: {error}",
./locales/zh.json:630:    "fetchingNodeEdges": "获取节点 {uuid}... 的相关边",
./locales/zh.json:631:    "foundNodeEdges": "找到 {count} 条与节点相关的边",
./locales/zh.json:632:    "fetchNodeEdgesFailed": "获取节点边失败: {error}",
./locales/en.json:38:    "heroTitle1": "Upload Reports,",
./locales/en.json:59:    "step04Title": "Report",
./locales/en.json:60:    "step04Desc": "ReportAgent interacts with the post-simulation environment via rich tools",
./locales/en.json:62:    "step05Desc": "Chat with any simulated individual & converse with ReportAgent",
./locales/en.json:78:    "stepNames": ["Graph Build", "Env Setup", "Run Simulation", "Report Generation", "Deep Interaction"]
./locales/en.json:89:    "entityNodes": "Entity Nodes",
./locales/en.json:90:    "relationEdges": "Relation Edges",
./locales/en.json:91:    "schemaTypes": "Schema Types",
./locales/en.json:104:    "generateAgentPersona": "Generate Agent Personas",
./locales/en.json:105:    "generateAgentPersonaDesc": "Combine context to auto-extract entities and relations from the knowledge graph, initialize simulated individuals, and assign unique behaviors and memories based on reality seeds",
./locales/en.json:109:    "generatedAgentPersonas": "Generated Agent Personas",
./locales/en.json:161:    "profileModalBio": "Persona Bio",
./locales/en.json:163:    "profileModalPersona": "Detailed Persona Background",
./locales/en.json:168:    "personaDimMemory": "Unique Memory Imprint",
./locales/en.json:169:    "personaDimMemoryDesc": "Memories formed from reality seeds",
./locales/en.json:180:    "startGenerateReport": "Generate Report",
./locales/en.json:181:    "generatingReport": "Starting...",
./locales/en.json:185:    "graphMemoryUpdateEnabled": "Dynamic graph memory update enabled",
./locales/en.json:207:    "startGenerateReportBtn": "Generate Report",
./locales/en.json:208:    "generatingReportBtn": "Starting..."
./locales/en.json:213:    "waitingForReportAgent": "Waiting for Report Agent...",
./locales/en.json:243:    "tabEdges": "Edges ({count})",
./locales/en.json:244:    "tabNodes": "Nodes ({count})",
./locales/en.json:247:    "panelRelatedEdges": "Related Edges",
./locales/en.json:248:    "panelRelatedNodes": "Related Nodes",
./locales/en.json:255:    "chatWithReportAgent": "Chat with Report Agent",
./locales/en.json:259:    "reportAgentChat": "Report Agent - Chat",
./locales/en.json:262:    "toolInsightForgeDesc": "Aligns real-world seed data with simulation state, combining Global/Local Memory for cross-temporal deep attribution analysis",
./locales/en.json:266:    "toolQuickSearchDesc": "GraphRAG-based instant query interface with optimized indexing for fast extraction of node attributes and discrete facts",
./locales/en.json:270:    "chatEmptyReportAgent": "Chat with Report Agent to explore report content in depth",
./locales/en.json:290:    "graphMemoryRealtime": "GraphRAG short/long-term memory updating in real-time",
./locales/en.json:293:    "nodeDetails": "Node Details",
./locales/en.json:304:    "analysisReport": "Analysis Report",
./locales/en.json:314:    "step4Button": "Analysis Report",
./locales/en.json:362:    "graphIdRequiredForMemory": "Graph memory update requires a valid graph_id. Ensure the graph is built.",
./locales/en.json:368:    "reportAlreadyExists": "Report already exists",
./locales/en.json:369:    "reportGenerateStarted": "Report generation task started. Query progress via /api/report/generate/status.",
./locales/en.json:370:    "reportGenerated": "Report generated",
./locales/en.json:371:    "reportNotFound": "Report not found: {id}",
./locales/en.json:372:    "noReportForSim": "No report found for this simulation: {id}",
./locales/en.json:373:    "reportDeleted": "Report deleted: {id}",
./locales/en.json:374:    "reportGenerateFailed": "Report generation failed",
./locales/en.json:376:    "reportProgressNotAvail": "Report not found or progress unavailable: {id}",
./locales/en.json:391:    "initReportAgent": "Initializing Report Agent..."
./locales/en.json:419:    "readingNodeData": "Reading node data...",
./locales/en.json:427:    "initReport": "Initializing report...",
./locales/en.json:432:    "assemblingReport": "Assembling full report...",
./locales/en.json:433:    "reportComplete": "Report generation complete",
./locales/en.json:434:    "reportFailed": "Report generation failed: {error}",
./locales/en.json:466:    "enterStep4": "Entering Step 4: Report Generation",
./locales/en.json:529:    "graphMemoryUpdateEnabled": "Dynamic graph memory update enabled",
./locales/en.json:540:    "reportRequestSent": "Report generation request sent, please wait...",
./locales/en.json:541:    "startingReportGen": "Starting report generation...",
./locales/en.json:542:    "reportGenTaskStarted": "✓ Report generation task started: {reportId}",
./locales/en.json:544:    "reportGenException": "✗ Report generation error: {error}",
./locales/en.json:548:    "sendToReportAgent": "Sent to Report Agent: {message}...",
./locales/en.json:549:    "reportAgentReplied": "Report Agent replied",
./locales/en.json:555:    "loadReportData": "Loading report data: {id}",
./locales/en.json:556:    "loadReportFailed": "Failed to load report: {error}",
./locales/en.json:557:    "reportDataLoaded": "Report data loaded",
./locales/en.json:558:    "loadReportLogFailed": "Failed to load report logs: {error}",
./locales/en.json:562:    "reportViewInit": "ReportView initialized",
./locales/en.json:563:    "getReportInfoFailed": "Failed to get report info: {error}",
./locales/en.json:569:    "taskStarted": "Report generation task started",
./locales/en.json:580:    "reportComplete": "Report generation complete",
./locales/en.json:582:    "agentInitDone": "ReportAgent initialized: graph_id={graphId}, simulation_id={simulationId}",
./locales/en.json:600:    "reportGenDone": "Report generation complete: {reportId}",
./locales/en.json:601:    "reportGenFailed": "Report generation failed: {error}",
./locales/en.json:602:    "agentChat": "Report Agent chat: {message}...",
./locales/en.json:603:    "fetchReportFailed": "Failed to fetch report content: {error}",
./locales/en.json:606:    "fullReportAssembled": "Full report assembled: {reportId}",
./locales/en.json:607:    "reportSaved": "Report saved: {reportId}",
./locales/en.json:608:    "reportFolderDeleted": "Report folder deleted: {reportId}",
./locales/en.json:623:    "fetchingAllNodes": "Fetching all nodes for graph {graphId}...",
./locales/en.json:624:    "fetchedNodes": "Fetched {count} nodes",
./locales/en.json:625:    "fetchingAllEdges": "Fetching all edges for graph {graphId}...",
./locales/en.json:626:    "fetchedEdges": "Fetched {count} edges",
./locales/en.json:627:    "fetchingNodeDetail": "Fetching node detail: {uuid}...",
./locales/en.json:628:    "fetchNodeDetailOp": "Fetch node detail (uuid={uuid}...)",
./locales/en.json:629:    "fetchNodeDetailFailed": "Failed to fetch node detail: {error}",
./locales/en.json:630:    "fetchingNodeEdges": "Fetching edges for node {uuid}...",
./locales/en.json:631:    "foundNodeEdges": "Found {count} edges related to node",
./locales/en.json:632:    "fetchNodeEdgesFailed": "Failed to fetch node edges: {error}",
./locales/en.json:633:    "fetchingEntitiesByType": "Fetching entities of type {type}...",
./locales/en.json:634:    "foundEntitiesByType": "Found {count} entities of type {type}",
./frontend/src/api/report.js:7:export const generateReport = (data) => {
./frontend/src/api/report.js:15:export const getReportStatus = (reportId) => {
./frontend/src/api/report.js:41:export const getReport = (reportId) => {
./frontend/src/api/report.js:46: * 与 Report Agent 对话
./frontend/src/api/report.js:49:export const chatWithReport = (data) => {
./frontend/src/router/index.js:6:import ReportView from '../views/ReportView.vue'
./frontend/src/router/index.js:35:    name: 'Report',
./frontend/src/router/index.js:36:    component: ReportView,
./backend/app/config.py:61:    # Report Agent配置
./backend/app/__init__.py:56:        if request.content_type and 'json' in request.content_type:
./backend/app/utils/zep_paging.py:92:            logger.warning(f"Node count reached limit ({max_items}), stopping pagination for graph {graph_id}")
./backend/app/utils/zep_paging.py:99:            logger.warning(f"Node missing uuid field, stopping pagination at {len(all_nodes)} nodes")
./backend/app/utils/zep_paging.py:140:            logger.warning(f"Edge missing uuid field, stopping pagination at {len(all_edges)} edges")
./backend/app/models/task.py:9:from enum import Enum
./backend/app/models/task.py:11:from dataclasses import dataclass, field
./backend/app/models/task.py:16:class TaskStatus(str, Enum):
./backend/app/models/task.py:24:@dataclass
./backend/app/models/task.py:171:                tasks = [t for t in tasks if t.task_type == task_type]
./backend/app/models/project.py:12:from enum import Enum
./backend/app/models/project.py:13:from dataclasses import dataclass, field, asdict
./backend/app/models/project.py:17:class ProjectStatus(str, Enum):
./backend/app/models/project.py:26:@dataclass
./backend/app/api/simulation.py:1598:                    "error": t('api.graphIdRequiredForMemory')
./backend/app/api/report.py:2:Report API路由
./backend/app/api/report.py:13:from ..services.report_agent import ReportAgent, ReportManager, ReportStatus
./backend/app/api/report.py:74:            existing_report = ReportManager.get_report_by_simulation(simulation_id)
./backend/app/api/report.py:75:            if existing_report and existing_report.status == ReportStatus.COMPLETED:
./backend/app/api/report.py:135:                    message=t('api.initReportAgent')
./backend/app/api/report.py:138:                # 创建Report Agent
./backend/app/api/report.py:139:                agent = ReportAgent(
./backend/app/api/report.py:160:                ReportManager.save_report(report)
./backend/app/api/report.py:162:                if report.status == ReportStatus.COMPLETED:
./backend/app/api/report.py:233:            existing_report = ReportManager.get_report_by_simulation(simulation_id)
./backend/app/api/report.py:234:            if existing_report and existing_report.status == ReportStatus.COMPLETED:
./backend/app/api/report.py:297:        report = ReportManager.get_report(report_id)
./backend/app/api/report.py:334:        report = ReportManager.get_report_by_simulation(simulation_id)
./backend/app/api/report.py:339:                "error": t('api.noReportForSim', id=simulation_id),
./backend/app/api/report.py:378:        reports = ReportManager.list_reports(
./backend/app/api/report.py:406:        report = ReportManager.get_report(report_id)
./backend/app/api/report.py:414:        md_path = ReportManager._get_report_markdown_path(report_id)
./backend/app/api/report.py:448:        success = ReportManager.delete_report(report_id)
./backend/app/api/report.py:470:# ============== Report Agent对话接口 ==============
./backend/app/api/report.py:475:    与Report Agent对话
./backend/app/api/report.py:477:    Report Agent可以在对话中自主调用检索工具来回答问题
./backend/app/api/report.py:545:        agent = ReportAgent(
./backend/app/api/report.py:588:        progress = ReportManager.get_progress(report_id)
./backend/app/api/report.py:636:        sections = ReportManager.get_generated_sections(report_id)
./backend/app/api/report.py:639:        report = ReportManager.get_report(report_id)
./backend/app/api/report.py:640:        is_complete = report is not None and report.status == ReportStatus.COMPLETED
./backend/app/api/report.py:676:        section_path = ReportManager._get_section_path(report_id, section_index)
./backend/app/api/report.py:727:        report = ReportManager.get_report_by_simulation(simulation_id)
./backend/app/api/report.py:734:        interview_unlocked = has_report and report.status == ReportStatus.COMPLETED
./backend/app/api/report.py:761:    获取 Report Agent 的详细执行日志
./backend/app/api/report.py:801:        log_data = ReportManager.get_agent_log(report_id, from_line=from_line)
./backend/app/api/report.py:832:        logs = ReportManager.get_agent_log_stream(report_id)
./backend/app/api/report.py:856:    获取 Report Agent 的控制台输出日志
./backend/app/api/report.py:883:        log_data = ReportManager.get_console_log(report_id, from_line=from_line)
./backend/app/api/report.py:914:        logs = ReportManager.get_console_log_stream(report_id)
./backend/app/services/report_agent.py:2:Report Agent服务
./backend/app/services/report_agent.py:17:from dataclasses import dataclass, field
./backend/app/services/report_agent.py:19:from enum import Enum
./backend/app/services/report_agent.py:36:class ReportLogger:
./backend/app/services/report_agent.py:38:    Report Agent 详细日志记录器
./backend/app/services/report_agent.py:307:class ReportConsoleLogger:
./backend/app/services/report_agent.py:309:    Report Agent 控制台日志记录器
./backend/app/services/report_agent.py:389:class ReportStatus(str, Enum):
./backend/app/services/report_agent.py:398:@dataclass
./backend/app/services/report_agent.py:399:class ReportSection:
./backend/app/services/report_agent.py:418:@dataclass
./backend/app/services/report_agent.py:419:class ReportOutline:
./backend/app/services/report_agent.py:423:    sections: List[ReportSection]
./backend/app/services/report_agent.py:441:@dataclass
./backend/app/services/report_agent.py:442:class Report:
./backend/app/services/report_agent.py:448:    status: ReportStatus
./backend/app/services/report_agent.py:449:    outline: Optional[ReportOutline] = None
./backend/app/services/report_agent.py:861:# ReportAgent 主类
./backend/app/services/report_agent.py:865:class ReportAgent:
./backend/app/services/report_agent.py:867:    Report Agent - 模拟报告生成Agent
./backend/app/services/report_agent.py:893:        初始化Report Agent
./backend/app/services/report_agent.py:913:        self.report_logger: Optional[ReportLogger] = None
./backend/app/services/report_agent.py:915:        self.console_logger: Optional[ReportConsoleLogger] = None
./backend/app/services/report_agent.py:1049:                entity_type = parameters.get("entity_type", "")
./backend/app/services/report_agent.py:1140:    ) -> ReportOutline:
./backend/app/services/report_agent.py:1150:            ReportOutline: 报告大纲
./backend/app/services/report_agent.py:1191:                sections.append(ReportSection(
./backend/app/services/report_agent.py:1196:            outline = ReportOutline(
./backend/app/services/report_agent.py:1211:            return ReportOutline(
./backend/app/services/report_agent.py:1215:                    ReportSection(title="预测场景与核心发现"),
./backend/app/services/report_agent.py:1216:                    ReportSection(title="人群行为预测分析"),
./backend/app/services/report_agent.py:1217:                    ReportSection(title="趋势展望与风险提示")
./backend/app/services/report_agent.py:1223:        section: ReportSection,
./backend/app/services/report_agent.py:1224:        outline: ReportOutline,
./backend/app/services/report_agent.py:1536:    ) -> Report:
./backend/app/services/report_agent.py:1556:            Report: 完整报告
./backend/app/services/report_agent.py:1565:        report = Report(
./backend/app/services/report_agent.py:1570:            status=ReportStatus.PENDING,
./backend/app/services/report_agent.py:1579:            ReportManager._ensure_report_folder(report_id)
./backend/app/services/report_agent.py:1582:            self.report_logger = ReportLogger(report_id)
./backend/app/services/report_agent.py:1590:            self.console_logger = ReportConsoleLogger(report_id)
./backend/app/services/report_agent.py:1592:            ReportManager.update_progress(
./backend/app/services/report_agent.py:1593:                report_id, "pending", 0, t('progress.initReport'),
./backend/app/services/report_agent.py:1596:            ReportManager.save_report(report)
./backend/app/services/report_agent.py:1599:            report.status = ReportStatus.PLANNING
./backend/app/services/report_agent.py:1600:            ReportManager.update_progress(
./backend/app/services/report_agent.py:1621:            ReportManager.save_outline(report_id, outline)
./backend/app/services/report_agent.py:1622:            ReportManager.update_progress(
./backend/app/services/report_agent.py:1626:            ReportManager.save_report(report)
./backend/app/services/report_agent.py:1631:            report.status = ReportStatus.GENERATING
./backend/app/services/report_agent.py:1641:                ReportManager.update_progress(
./backend/app/services/report_agent.py:1673:                ReportManager.save_section(report_id, section_num, section)
./backend/app/services/report_agent.py:1689:                ReportManager.update_progress(
./backend/app/services/report_agent.py:1699:                progress_callback("generating", 95, t('progress.assemblingReport'))
./backend/app/services/report_agent.py:1701:            ReportManager.update_progress(
./backend/app/services/report_agent.py:1702:                report_id, "generating", 95, t('progress.assemblingReport'),
./backend/app/services/report_agent.py:1706:            # 使用ReportManager组装完整报告
./backend/app/services/report_agent.py:1707:            report.markdown_content = ReportManager.assemble_full_report(report_id, outline)
./backend/app/services/report_agent.py:1708:            report.status = ReportStatus.COMPLETED
./backend/app/services/report_agent.py:1722:            ReportManager.save_report(report)
./backend/app/services/report_agent.py:1723:            ReportManager.update_progress(
./backend/app/services/report_agent.py:1742:            report.status = ReportStatus.FAILED
./backend/app/services/report_agent.py:1751:                ReportManager.save_report(report)
./backend/app/services/report_agent.py:1752:                ReportManager.update_progress(
./backend/app/services/report_agent.py:1772:        与Report Agent对话
./backend/app/services/report_agent.py:1794:            report = ReportManager.get_report_by_simulation(self.simulation_id)
./backend/app/services/report_agent.py:1801:            logger.warning(t('report.fetchReportFailed', error=e))
./backend/app/services/report_agent.py:1884:class ReportManager:
./backend/app/services/report_agent.py:2081:    def save_outline(cls, report_id: str, outline: ReportOutline) -> None:
./backend/app/services/report_agent.py:2099:        section: ReportSection
./backend/app/services/report_agent.py:2271:    def assemble_full_report(cls, report_id: str, outline: ReportOutline) -> str:
./backend/app/services/report_agent.py:2297:        logger.info(t('report.fullReportAssembled', reportId=report_id))
./backend/app/services/report_agent.py:2301:    def _post_process_report(cls, content: str, outline: ReportOutline) -> str:
./backend/app/services/report_agent.py:2427:    def save_report(cls, report: Report) -> None:
./backend/app/services/report_agent.py:2447:    def get_report(cls, report_id: str) -> Optional[Report]:
./backend/app/services/report_agent.py:2462:        # 重建Report对象
./backend/app/services/report_agent.py:2468:                sections.append(ReportSection(
./backend/app/services/report_agent.py:2472:            outline = ReportOutline(
./backend/app/services/report_agent.py:2486:        return Report(
./backend/app/services/report_agent.py:2491:            status=ReportStatus(data['status']),
./backend/app/services/report_agent.py:2500:    def get_report_by_simulation(cls, simulation_id: str) -> Optional[Report]:
./backend/app/services/report_agent.py:2521:    def list_reports(cls, simulation_id: Optional[str] = None, limit: int = 50) -> List[Report]:
./backend/app/services/simulation_runner.py:16:from dataclasses import dataclass, field
./backend/app/services/simulation_runner.py:18:from enum import Enum
./backend/app/services/simulation_runner.py:24:from .zep_graph_memory_updater import ZepGraphMemoryManager
./backend/app/services/simulation_runner.py:36:class RunnerStatus(str, Enum):
./backend/app/services/simulation_runner.py:48:@dataclass
./backend/app/services/simulation_runner.py:75:@dataclass
./backend/app/services/simulation_runner.py:101:@dataclass
./backend/app/services/simulation_runner.py:378:                ZepGraphMemoryManager.create_updater(simulation_id, graph_id)
./backend/app/services/simulation_runner.py:559:                    ZepGraphMemoryManager.stop_updater(simulation_id)
./backend/app/services/simulation_runner.py:607:            graph_updater = ZepGraphMemoryManager.get_updater(state.simulation_id)
./backend/app/services/simulation_runner.py:620:                                event_type = action_data.get("event_type")
./backend/app/services/simulation_runner.py:623:                                if event_type == "simulation_end":
./backend/app/services/simulation_runner.py:643:                                elif event_type == "round_end":
./backend/app/services/simulation_runner.py:815:                ZepGraphMemoryManager.stop_updater(simulation_id)
./backend/app/services/simulation_runner.py:1209:            ZepGraphMemoryManager.stop_all()
./backend/app/services/zep_tools.py:3:封装图谱搜索、节点读取、边查询等工具，供Report Agent使用
./backend/app/services/zep_tools.py:14:from dataclasses import dataclass, field
./backend/app/services/zep_tools.py:27:@dataclass
./backend/app/services/zep_tools.py:57:@dataclass
./backend/app/services/zep_tools.py:58:class NodeInfo:
./backend/app/services/zep_tools.py:77:        entity_type = next((l for l in self.labels if l not in ["Entity", "Node"]), "未知类型")
./backend/app/services/zep_tools.py:81:@dataclass
./backend/app/services/zep_tools.py:82:class EdgeInfo:
./backend/app/services/zep_tools.py:138:@dataclass
./backend/app/services/zep_tools.py:214:@dataclass
./backend/app/services/zep_tools.py:223:    all_nodes: List[NodeInfo] = field(default_factory=list)
./backend/app/services/zep_tools.py:225:    all_edges: List[EdgeInfo] = field(default_factory=list)
./backend/app/services/zep_tools.py:278:                entity_type = next((l for l in node.labels if l not in ["Entity", "Node"]), "实体")
./backend/app/services/zep_tools.py:284:@dataclass
./backend/app/services/zep_tools.py:340:@dataclass
./backend/app/services/zep_tools.py:417:    - get_entities_by_type - 按类型获取实体
./backend/app/services/zep_tools.py:650:    def get_all_nodes(self, graph_id: str) -> List[NodeInfo]:
./backend/app/services/zep_tools.py:660:        logger.info(t("console.fetchingAllNodes", graphId=graph_id))
./backend/app/services/zep_tools.py:667:            result.append(NodeInfo(
./backend/app/services/zep_tools.py:675:        logger.info(t("console.fetchedNodes", count=len(result)))
./backend/app/services/zep_tools.py:678:    def get_all_edges(self, graph_id: str, include_temporal: bool = True) -> List[EdgeInfo]:
./backend/app/services/zep_tools.py:689:        logger.info(t("console.fetchingAllEdges", graphId=graph_id))
./backend/app/services/zep_tools.py:696:            edge_info = EdgeInfo(
./backend/app/services/zep_tools.py:713:        logger.info(t("console.fetchedEdges", count=len(result)))
./backend/app/services/zep_tools.py:716:    def get_node_detail(self, node_uuid: str) -> Optional[NodeInfo]:
./backend/app/services/zep_tools.py:726:        logger.info(t("console.fetchingNodeDetail", uuid=node_uuid[:8]))
./backend/app/services/zep_tools.py:731:                operation_name=t("console.fetchNodeDetailOp", uuid=node_uuid[:8])
./backend/app/services/zep_tools.py:737:            return NodeInfo(
./backend/app/services/zep_tools.py:745:            logger.error(t("console.fetchNodeDetailFailed", error=str(e)))
./backend/app/services/zep_tools.py:748:    def get_node_edges(self, graph_id: str, node_uuid: str) -> List[EdgeInfo]:
./backend/app/services/zep_tools.py:761:        logger.info(t("console.fetchingNodeEdges", uuid=node_uuid[:8]))
./backend/app/services/zep_tools.py:773:            logger.info(t("console.foundNodeEdges", count=len(result)))
./backend/app/services/zep_tools.py:777:            logger.warning(t("console.fetchNodeEdgesFailed", error=str(e)))
./backend/app/services/zep_tools.py:784:    ) -> List[NodeInfo]:
./backend/app/services/zep_tools.py:802:            if entity_type in node.labels:
./backend/app/services/zep_tools.py:874:                if label not in ["Entity", "Node"]:
./backend/app/services/zep_tools.py:927:            custom_labels = [l for l in node.labels if l not in ["Entity", "Node"]]
./backend/app/services/zep_tools.py:1049:                    entity_type = next((l for l in node.labels if l not in ["Entity", "Node"]), "实体")
./backend/app/services/zep_tools.py:1079:                source_name = node_map.get(source_uuid, NodeInfo('', '', [], '', {})).name or source_uuid[:8]
./backend/app/services/zep_tools.py:1080:                target_name = node_map.get(target_uuid, NodeInfo('', '', [], '', {})).name or target_uuid[:8]
./backend/app/services/zep_tools.py:1195:            source_name = node_map.get(edge.source_node_uuid, NodeInfo('', '', [], '', {})).name or edge.source_node_uuid[:8]
./backend/app/services/zep_tools.py:1196:            target_name = node_map.get(edge.target_node_uuid, NodeInfo('', '', [], '', {})).name or edge.target_node_uuid[:8]
./backend/app/services/__init__.py:8:from .zep_entity_reader import ZepEntityReader, EntityNode, FilteredEntities
./backend/app/services/__init__.py:10:from .simulation_manager import SimulationManager, SimulationState, SimulationStatus
./backend/app/services/__init__.py:27:    ZepGraphMemoryUpdater,
./backend/app/services/__init__.py:28:    ZepGraphMemoryManager,
./backend/app/services/__init__.py:45:    'EntityNode',
./backend/app/services/__init__.py:50:    'SimulationState',
./backend/app/services/__init__.py:63:    'ZepGraphMemoryUpdater',
./backend/app/services/__init__.py:64:    'ZepGraphMemoryManager',
./backend/app/services/oasis_profile_generator.py:15:from dataclasses import dataclass, field
./backend/app/services/oasis_profile_generator.py:24:from .zep_entity_reader import EntityNode, ZepEntityReader
./backend/app/services/oasis_profile_generator.py:29:@dataclass
./backend/app/services/oasis_profile_generator.py:214:        entity: EntityNode, 
./backend/app/services/oasis_profile_generator.py:229:        entity_type = entity.get_entity_type() or "Entity"
./backend/app/services/oasis_profile_generator.py:286:    def _search_zep_for_entity(self, entity: EntityNode) -> Dict[str, Any]:
./backend/app/services/oasis_profile_generator.py:414:    def _build_entity_context(self, entity: EntityNode) -> str:
./backend/app/services/oasis_profile_generator.py:464:                custom_labels = [l for l in node_labels if l not in ["Entity", "Node"]]
./backend/app/services/oasis_profile_generator.py:853:        entities: List[EntityNode],
./backend/app/services/oasis_profile_generator.py:922:        def generate_single_profile(idx: int, entity: EntityNode) -> tuple:
./backend/app/services/oasis_profile_generator.py:925:            entity_type = entity.get_entity_type() or "Entity"
./backend/app/services/oasis_profile_generator.py:969:                entity_type = entity.get_entity_type() or "Entity"
./backend/app/services/simulation_manager.py:11:from dataclasses import dataclass, field
./backend/app/services/simulation_manager.py:13:from enum import Enum
./backend/app/services/simulation_manager.py:25:class SimulationStatus(str, Enum):
./backend/app/services/simulation_manager.py:37:class PlatformType(str, Enum):
./backend/app/services/simulation_manager.py:43:@dataclass
./backend/app/services/simulation_manager.py:44:class SimulationState:
./backend/app/services/simulation_manager.py:137:        self._simulations: Dict[str, SimulationState] = {}
./backend/app/services/simulation_manager.py:145:    def _save_simulation_state(self, state: SimulationState):
./backend/app/services/simulation_manager.py:157:    def _load_simulation_state(self, simulation_id: str) -> Optional[SimulationState]:
./backend/app/services/simulation_manager.py:171:        state = SimulationState(
./backend/app/services/simulation_manager.py:200:    ) -> SimulationState:
./backend/app/services/simulation_manager.py:211:            SimulationState
./backend/app/services/simulation_manager.py:216:        state = SimulationState(
./backend/app/services/simulation_manager.py:239:    ) -> SimulationState:
./backend/app/services/simulation_manager.py:260:            SimulationState
./backend/app/services/simulation_manager.py:279:                progress_callback("reading", 30, t('progress.readingNodeData'))
./backend/app/services/simulation_manager.py:459:    def get_simulation(self, simulation_id: str) -> Optional[SimulationState]:
./backend/app/services/simulation_manager.py:463:    def list_simulations(self, project_id: Optional[str] = None) -> List[SimulationState]:
./backend/app/services/ontology_generator.py:210:        system_prompt = f"{ONTOLOGY_SYSTEM_PROMPT}\n\n{lang_instruction}\nIMPORTANT: Entity type names MUST be in English PascalCase (e.g., 'PersonEntity', 'MediaOrganization'). Relationship type names MUST be in English UPPER_SNAKE_CASE (e.g., 'WORKS_FOR'). Attribute names MUST be in English snake_case. Only description fields and analysis_summary should use the specified language above."
./backend/app/services/ontology_generator.py:297:                    logger.warning(f"Entity type name '{original_name}' auto-converted to '{entity['name']}'")
./backend/app/services/ontology_generator.py:314:                    logger.warning(f"Edge type name '{original_name}' auto-converted to '{edge['name']}'")
./backend/app/services/ontology_generator.py:341:                logger.warning(f"Duplicate entity type '{name}' removed during validation")
./backend/app/services/ontology_generator.py:416:            'from pydantic import Field',
./backend/app/services/ontology_generator.py:417:            'from zep_cloud.external_clients.ontology import EntityModel, EntityText, EdgeModel',
./backend/app/services/ontology_generator.py:429:            code_lines.append(f'class {name}(EntityModel):')
./backend/app/services/ontology_generator.py:457:            code_lines.append(f'class {class_name}(EdgeModel):')
./backend/app/services/simulation_ipc.py:16:from dataclasses import dataclass, field
./backend/app/services/simulation_ipc.py:18:from enum import Enum
./backend/app/services/simulation_ipc.py:25:class CommandType(str, Enum):
./backend/app/services/simulation_ipc.py:32:class CommandStatus(str, Enum):
./backend/app/services/simulation_ipc.py:40:@dataclass
./backend/app/services/simulation_ipc.py:66:@dataclass
./backend/app/services/zep_entity_reader.py:8:from dataclasses import dataclass, field
./backend/app/services/zep_entity_reader.py:22:@dataclass
./backend/app/services/zep_entity_reader.py:23:class EntityNode:
./backend/app/services/zep_entity_reader.py:49:            if label not in ["Entity", "Node"]:
./backend/app/services/zep_entity_reader.py:54:@dataclass
./backend/app/services/zep_entity_reader.py:57:    entities: List[EntityNode]
./backend/app/services/zep_entity_reader.py:226:        - 如果节点的Labels包含除"Entity"和"Node"之外的标签，说明符合预定义类型，保留
./backend/app/services/zep_entity_reader.py:255:            # 筛选逻辑：Labels必须包含除"Entity"和"Node"之外的标签
./backend/app/services/zep_entity_reader.py:256:            custom_labels = [l for l in labels if l not in ["Entity", "Node"]]
./backend/app/services/zep_entity_reader.py:267:                entity_type = matching_labels[0]
./backend/app/services/zep_entity_reader.py:269:                entity_type = custom_labels[0]
./backend/app/services/zep_entity_reader.py:274:            entity = EntityNode(
./backend/app/services/zep_entity_reader.py:337:    ) -> Optional[EntityNode]:
./backend/app/services/zep_entity_reader.py:346:            EntityNode或None
./backend/app/services/zep_entity_reader.py:399:            return EntityNode(
./backend/app/services/zep_entity_reader.py:418:    ) -> List[EntityNode]:
./backend/app/services/graph_builder.py:11:from dataclasses import dataclass
./backend/app/services/graph_builder.py:14:from zep_cloud import EpisodeData, EntityEdgeSourceTarget
./backend/app/services/graph_builder.py:23:@dataclass
./backend/app/services/graph_builder.py:209:        from pydantic import Field
./backend/app/services/graph_builder.py:210:        from zep_cloud.external_clients.ontology import EntityModel, EntityText, EdgeModel
./backend/app/services/graph_builder.py:214:        warnings.filterwarnings('ignore', category=UserWarning, module='pydantic')
./backend/app/services/graph_builder.py:245:            entity_class = type(name, (EntityModel,), attrs)
./backend/app/services/graph_builder.py:270:            edge_class = type(class_name, (EdgeModel,), attrs)
./backend/app/services/graph_builder.py:277:                    EntityEdgeSourceTarget(
./backend/app/services/graph_builder.py:416:                    if label not in ["Entity", "Node"]:
./backend/app/services/graph_builder.py:476:            fact_type = getattr(edge, 'fact_type', None) or edge.name or ""
./backend/app/services/zep_graph_memory_updater.py:11:from dataclasses import dataclass
./backend/app/services/zep_graph_memory_updater.py:24:@dataclass
./backend/app/services/zep_graph_memory_updater.py:202:class ZepGraphMemoryUpdater:
./backend/app/services/zep_graph_memory_updater.py:269:        logger.info(f"ZepGraphMemoryUpdater 初始化完成: graph_id={graph_id}, batch_size={self.BATCH_SIZE}")
./backend/app/services/zep_graph_memory_updater.py:288:            name=f"ZepMemoryUpdater-{self.graph_id[:8]}"
./backend/app/services/zep_graph_memory_updater.py:291:        logger.info(f"ZepGraphMemoryUpdater 已启动: graph_id={self.graph_id}")
./backend/app/services/zep_graph_memory_updater.py:303:        logger.info(f"ZepGraphMemoryUpdater 已停止: graph_id={self.graph_id}, "
./backend/app/services/zep_graph_memory_updater.py:332:        if activity.action_type == "DO_NOTHING":
./backend/app/services/zep_graph_memory_updater.py:479:class ZepGraphMemoryManager:
./backend/app/services/zep_graph_memory_updater.py:486:    _updaters: Dict[str, ZepGraphMemoryUpdater] = {}
./backend/app/services/zep_graph_memory_updater.py:490:    def create_updater(cls, simulation_id: str, graph_id: str) -> ZepGraphMemoryUpdater:
./backend/app/services/zep_graph_memory_updater.py:499:            ZepGraphMemoryUpdater实例
./backend/app/services/zep_graph_memory_updater.py:506:            updater = ZepGraphMemoryUpdater(graph_id)
./backend/app/services/zep_graph_memory_updater.py:514:    def get_updater(cls, simulation_id: str) -> Optional[ZepGraphMemoryUpdater]:
./backend/app/services/simulation_config_generator.py:16:from dataclasses import dataclass, field, asdict
./backend/app/services/simulation_config_generator.py:24:from .zep_entity_reader import EntityNode, ZepEntityReader
./backend/app/services/simulation_config_generator.py:51:@dataclass
./backend/app/services/simulation_config_generator.py:83:@dataclass  
./backend/app/services/simulation_config_generator.py:113:@dataclass
./backend/app/services/simulation_config_generator.py:129:@dataclass
./backend/app/services/simulation_config_generator.py:146:@dataclass
./backend/app/services/simulation_config_generator.py:250:        entities: List[EntityNode],
./backend/app/services/simulation_config_generator.py:385:        entities: List[EntityNode]
./backend/app/services/simulation_config_generator.py:409:    def _summarize_entities(self, entities: List[EntityNode]) -> str:
./backend/app/services/simulation_config_generator.py:414:        by_type: Dict[str, List[EntityNode]] = {}
./backend/app/services/simulation_config_generator.py:650:        entities: List[EntityNode]
./backend/app/services/simulation_config_generator.py:662:            etype = e.get_entity_type() or "Unknown"
./backend/app/services/simulation_config_generator.py:663:            if etype not in type_examples:
./backend/app/services/simulation_config_generator.py:691:**重要**: poster_type 必须从上面的"可用实体类型"中选择，这样初始帖子才能分配给合适的 Agent 发布。
./backend/app/services/simulation_config_generator.py:705:        system_prompt = "你是舆论分析专家。返回纯JSON格式。注意 poster_type 必须精确匹配可用实体类型。"
./backend/app/services/simulation_config_generator.py:736:        根据每个帖子的 poster_type 匹配最合适的 agent_id
./backend/app/services/simulation_config_generator.py:744:            etype = agent.entity_type.lower()
./backend/app/services/simulation_config_generator.py:745:            if etype not in agents_by_type:
./backend/app/services/simulation_config_generator.py:766:            poster_type = post.get("poster_type", "").lower()
./backend/app/services/simulation_config_generator.py:773:            if poster_type in agents_by_type:
./backend/app/services/simulation_config_generator.py:781:                    if poster_type in aliases or alias_key == poster_type:
./backend/app/services/simulation_config_generator.py:816:        entities: List[EntityNode],
./backend/app/services/simulation_config_generator.py:908:    def _generate_agent_config_by_rule(self, entity: EntityNode) -> Dict[str, Any]:
./backend/app/services/simulation_config_generator.py:910:        entity_type = (entity.get_entity_type() or "Unknown").lower()
./backend/app/services/simulation_config_generator.py:912:        if entity_type in ["university", "governmentagency", "ngo"]:
./backend/app/services/simulation_config_generator.py:925:        elif entity_type in ["mediaoutlet"]:
./backend/app/services/simulation_config_generator.py:938:        elif entity_type in ["professor", "expert", "official"]:
./backend/app/services/simulation_config_generator.py:951:        elif entity_type in ["student"]:
./backend/app/services/simulation_config_generator.py:964:        elif entity_type in ["alumni"]:
./backend/scripts/run_reddit_simulation.py:355:        command_type = command.get("command_type")
./backend/scripts/run_reddit_simulation.py:360:        if command_type == CommandType.INTERVIEW:
./backend/scripts/run_reddit_simulation.py:368:        elif command_type == CommandType.BATCH_INTERVIEW:
./backend/scripts/run_reddit_simulation.py:375:        elif command_type == CommandType.CLOSE_ENV:
./backend/scripts/run_parallel_simulation.py:572:        command_type = command.get("command_type")
./backend/scripts/run_parallel_simulation.py:577:        if command_type == CommandType.INTERVIEW:
./backend/scripts/run_parallel_simulation.py:586:        elif command_type == CommandType.BATCH_INTERVIEW:
./backend/scripts/run_parallel_simulation.py:594:        elif command_type == CommandType.CLOSE_ENV:
./backend/scripts/run_parallel_simulation.py:730:            action_type = ACTION_TYPE_MAP.get(action, action.upper())
./backend/scripts/run_parallel_simulation.py:766:        if action_type in ('LIKE_POST', 'DISLIKE_POST'):
./backend/scripts/run_parallel_simulation.py:775:        elif action_type == 'REPOST':
./backend/scripts/run_parallel_simulation.py:791:        elif action_type == 'QUOTE_POST':
./backend/scripts/run_parallel_simulation.py:811:        elif action_type == 'FOLLOW':
./backend/scripts/run_parallel_simulation.py:826:        elif action_type == 'MUTE':
./backend/scripts/run_parallel_simulation.py:835:        elif action_type in ('LIKE_COMMENT', 'DISLIKE_COMMENT'):
./backend/scripts/run_parallel_simulation.py:844:        elif action_type == 'CREATE_COMMENT':
./backend/scripts/run_twitter_simulation.py:355:        command_type = command.get("command_type")
./backend/scripts/run_twitter_simulation.py:360:        if command_type == CommandType.INTERVIEW:
./backend/scripts/run_twitter_simulation.py:368:        elif command_type == CommandType.BATCH_INTERVIEW:
./backend/scripts/run_twitter_simulation.py:375:        elif command_type == CommandType.CLOSE_ENV:
```

## 12. 疑似核心源码文件预览

### backend/scripts/run_parallel_simulation.py

```python
"""
OASIS 双平台并行模拟预设脚本
同时运行Twitter和Reddit模拟，读取相同的配置文件

功能特性:
- 双平台（Twitter + Reddit）并行模拟
- 完成模拟后不立即关闭环境，进入等待命令模式
- 支持通过IPC接收Interview命令
- 支持单个Agent采访和批量采访
- 支持远程关闭环境命令

使用方式:
    python run_parallel_simulation.py --config simulation_config.json
    python run_parallel_simulation.py --config simulation_config.json --no-wait  # 完成后立即关闭
    python run_parallel_simulation.py --config simulation_config.json --twitter-only
    python run_parallel_simulation.py --config simulation_config.json --reddit-only

日志结构:
    sim_xxx/
    ├── twitter/
    │   └── actions.jsonl    # Twitter 平台动作日志
    ├── reddit/
    │   └── actions.jsonl    # Reddit 平台动作日志
    ├── simulation.log       # 主模拟进程日志
    └── run_state.json       # 运行状态（API 查询用）
"""

# ============================================================
# 解决 Windows 编码问题：在所有 import 之前设置 UTF-8 编码
# 这是为了修复 OASIS 第三方库读取文件时未指定编码的问题
# ============================================================
import sys
import os

if sys.platform == 'win32':
    # 设置 Python 默认 I/O 编码为 UTF-8
    # 这会影响所有未指定编码的 open() 调用
    os.environ.setdefault('PYTHONUTF8', '1')
    os.environ.setdefault('PYTHONIOENCODING', 'utf-8')
    
    # 重新配置标准输出流为 UTF-8（解决控制台中文乱码）
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    
    # 强制设置默认编码（影响 open() 函数的默认编码）
    # 注意：这需要在 Python 启动时就设置，运行时设置可能不生效
    # 所以我们还需要 monkey-patch 内置的 open 函数
    import builtins
    _original_open = builtins.open
    
    def _utf8_open(file, mode='r', buffering=-1, encoding=None, errors=None, 
                   newline=None, closefd=True, opener=None):
        """
        包装 open() 函数，对于文本模式默认使用 UTF-8 编码
        这可以修复第三方库（如 OASIS）读取文件时未指定编码的问题
        """
        # 只对文本模式（非二进制）且未指定编码的情况设置默认编码
        if encoding is None and 'b' not in mode:
            encoding = 'utf-8'
        return _original_open(file, mode, buffering, encoding, errors, 
                              newline, closefd, opener)
    
    builtins.open = _utf8_open

import argparse
import asyncio
import json
import logging
import multiprocessing
import random
import signal
import sqlite3
import warnings
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple


# 全局变量：用于信号处理
_shutdown_event = None
_cleanup_done = False

# 添加 backend 目录到路径
# 脚本固定位于 backend/scripts/ 目录
_scripts_dir = os.path.dirname(os.path.abspath(__file__))
_backend_dir = os.path.abspath(os.path.join(_scripts_dir, '..'))
_project_root = os.path.abspath(os.path.join(_backend_dir, '..'))
sys.path.insert(0, _scripts_dir)
sys.path.insert(0, _backend_dir)

# 加载项目根目录的 .env 文件（包含 LLM_API_KEY 等配置）
from dotenv import load_dotenv
_env_file = os.path.join(_project_root, '.env')
if os.path.exists(_env_file):
    load_dotenv(_env_file)
    print(f"已加载环境配置: {_env_file}")
else:
    # 尝试加载 backend/.env
    _backend_env = os.path.join(_backend_dir, '.env')
    if os.path.exists(_backend_env):
        load_dotenv(_backend_env)
        print(f"已加载环境配置: {_backend_env}")


class MaxTokensWarningFilter(logging.Filter):
    """过滤掉 camel-ai 关于 max_tokens 的警告（我们故意不设置 max_tokens，让模型自行决定）"""
    
    def filter(self, record):
        # 过滤掉包含 max_tokens 警告的日志
        if "max_tokens" in record.getMessage() and "Invalid or missing" in record.getMessage():
            return False
        return True


# 在模块加载时立即添加过滤器，确保在 camel 代码执行前生效
logging.getLogger().addFilter(MaxTokensWarningFilter())


def disable_oasis_logging():
    """
    禁用 OASIS 库的详细日志输出
    OASIS 的日志太冗余（记录每个 agent 的观察和动作），我们使用自己的 action_logger
    """
    # 禁用 OASIS 的所有日志器
    oasis_loggers = [
        "social.agent",
        "social.twitter", 
        "social.rec",
        "oasis.env",
        "table",
    ]
    
    for logger_name in oasis_loggers:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.CRITICAL)  # 只记录严重错误
        logger.handlers.clear()
        logger.propagate = False


def init_logging_for_simulation(simulation_dir: str):
    """
    初始化模拟的日志配置
    
    Args:
        simulation_dir: 模拟目录路径
    """
    # 禁用 OASIS 的详细日志
    disable_oasis_logging()
    
    # 清理旧的 log 目录（如果存在）
    old_log_dir = os.path.join(simulation_dir, "log")
    if os.path.exists(old_log_dir):
        import shutil
        shutil.rmtree(old_log_dir, ignore_errors=True)


from action_logger import SimulationLogManager, PlatformActionLogger

try:
    from camel.models import ModelFactory
    from camel.types import ModelPlatformType
    import oasis
    from oasis import (
        ActionType,
        LLMAction,
        ManualAction,
        generate_twitter_agent_graph,
        generate_reddit_agent_graph
    )
except ImportError as e:
    print(f"错误: 缺少依赖 {e}")
    print("请先安装: pip install oasis-ai camel-ai")
    sys.exit(1)


# Twitter可用动作（不包含INTERVIEW，INTERVIEW只能通过ManualAction手动触发）
TWITTER_ACTIONS = [
    ActionType.CREATE_POST,
    ActionType.LIKE_POST,

# ... 文件较长，已截断。总行数：1699
```

### backend/scripts/run_reddit_simulation.py

```python
"""
OASIS Reddit模拟预设脚本
此脚本读取配置文件中的参数来执行模拟，实现全程自动化

功能特性:
- 完成模拟后不立即关闭环境，进入等待命令模式
- 支持通过IPC接收Interview命令
- 支持单个Agent采访和批量采访
- 支持远程关闭环境命令

使用方式:
    python run_reddit_simulation.py --config /path/to/simulation_config.json
    python run_reddit_simulation.py --config /path/to/simulation_config.json --no-wait  # 完成后立即关闭
"""

import argparse
import asyncio
import json
import logging
import os
import random
import signal
import sys
import sqlite3
from datetime import datetime
from typing import Dict, Any, List, Optional

# 全局变量：用于信号处理
_shutdown_event = None
_cleanup_done = False

# 添加项目路径
_scripts_dir = os.path.dirname(os.path.abspath(__file__))
_backend_dir = os.path.abspath(os.path.join(_scripts_dir, '..'))
_project_root = os.path.abspath(os.path.join(_backend_dir, '..'))
sys.path.insert(0, _scripts_dir)
sys.path.insert(0, _backend_dir)

# 加载项目根目录的 .env 文件（包含 LLM_API_KEY 等配置）
from dotenv import load_dotenv
_env_file = os.path.join(_project_root, '.env')
if os.path.exists(_env_file):
    load_dotenv(_env_file)
else:
    _backend_env = os.path.join(_backend_dir, '.env')
    if os.path.exists(_backend_env):
        load_dotenv(_backend_env)


import re


class UnicodeFormatter(logging.Formatter):
    """自定义格式化器，将 Unicode 转义序列转换为可读字符"""
    
    UNICODE_ESCAPE_PATTERN = re.compile(r'\\u([0-9a-fA-F]{4})')
    
    def format(self, record):
        result = super().format(record)
        
        def replace_unicode(match):
            try:
                return chr(int(match.group(1), 16))
            except (ValueError, OverflowError):
                return match.group(0)
        
        return self.UNICODE_ESCAPE_PATTERN.sub(replace_unicode, result)


class MaxTokensWarningFilter(logging.Filter):
    """过滤掉 camel-ai 关于 max_tokens 的警告（我们故意不设置 max_tokens，让模型自行决定）"""
    
    def filter(self, record):
        # 过滤掉包含 max_tokens 警告的日志
        if "max_tokens" in record.getMessage() and "Invalid or missing" in record.getMessage():
            return False
        return True


# 在模块加载时立即添加过滤器，确保在 camel 代码执行前生效
logging.getLogger().addFilter(MaxTokensWarningFilter())


def setup_oasis_logging(log_dir: str):
    """配置 OASIS 的日志，使用固定名称的日志文件"""
    os.makedirs(log_dir, exist_ok=True)
    
    # 清理旧的日志文件
    for f in os.listdir(log_dir):
        old_log = os.path.join(log_dir, f)
        if os.path.isfile(old_log) and f.endswith('.log'):
            try:
                os.remove(old_log)
            except OSError:
                pass
    
    formatter = UnicodeFormatter("%(levelname)s - %(asctime)s - %(name)s - %(message)s")
    
    loggers_config = {
        "social.agent": os.path.join(log_dir, "social.agent.log"),
        "social.twitter": os.path.join(log_dir, "social.twitter.log"),
        "social.rec": os.path.join(log_dir, "social.rec.log"),
        "oasis.env": os.path.join(log_dir, "oasis.env.log"),
        "table": os.path.join(log_dir, "table.log"),
    }
    
    for logger_name, log_file in loggers_config.items():
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        logger.handlers.clear()
        file_handler = logging.FileHandler(log_file, encoding='utf-8', mode='w')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.propagate = False


try:
    from camel.models import ModelFactory
    from camel.types import ModelPlatformType
    import oasis
    from oasis import (
        ActionType,
        LLMAction,
        ManualAction,
        generate_reddit_agent_graph
    )
except ImportError as e:
    print(f"错误: 缺少依赖 {e}")
    print("请先安装: pip install oasis-ai camel-ai")
    sys.exit(1)


# IPC相关常量
IPC_COMMANDS_DIR = "ipc_commands"
IPC_RESPONSES_DIR = "ipc_responses"
ENV_STATUS_FILE = "env_status.json"

class CommandType:
    """命令类型常量"""
    INTERVIEW = "interview"
    BATCH_INTERVIEW = "batch_interview"
    CLOSE_ENV = "close_env"


class IPCHandler:
    """IPC命令处理器"""
    
    def __init__(self, simulation_dir: str, env, agent_graph):
        self.simulation_dir = simulation_dir
        self.env = env
        self.agent_graph = agent_graph
        self.commands_dir = os.path.join(simulation_dir, IPC_COMMANDS_DIR)
        self.responses_dir = os.path.join(simulation_dir, IPC_RESPONSES_DIR)
        self.status_file = os.path.join(simulation_dir, ENV_STATUS_FILE)
        self._running = True
        
        # 确保目录存在
        os.makedirs(self.commands_dir, exist_ok=True)
        os.makedirs(self.responses_dir, exist_ok=True)
    
    def update_status(self, status: str):
        """更新环境状态"""
        with open(self.status_file, 'w', encoding='utf-8') as f:
            json.dump({
                "status": status,
                "timestamp": datetime.now().isoformat()
            }, f, ensure_ascii=False, indent=2)
    
    def poll_command(self) -> Optional[Dict[str, Any]]:
        """轮询获取待处理命令"""
        if not os.path.exists(self.commands_dir):
            return None
        
        # 获取命令文件（按时间排序）
        command_files = []
        for filename in os.listdir(self.commands_dir):
            if filename.endswith('.json'):
                filepath = os.path.join(self.commands_dir, filename)
                command_files.append((filepath, os.path.getmtime(filepath)))

# ... 文件较长，已截断。总行数：769
```

### backend/scripts/run_twitter_simulation.py

```python
"""
OASIS Twitter模拟预设脚本
此脚本读取配置文件中的参数来执行模拟，实现全程自动化

功能特性:
- 完成模拟后不立即关闭环境，进入等待命令模式
- 支持通过IPC接收Interview命令
- 支持单个Agent采访和批量采访
- 支持远程关闭环境命令

使用方式:
    python run_twitter_simulation.py --config /path/to/simulation_config.json
    python run_twitter_simulation.py --config /path/to/simulation_config.json --no-wait  # 完成后立即关闭
"""

import argparse
import asyncio
import json
import logging
import os
import random
import signal
import sys
import sqlite3
from datetime import datetime
from typing import Dict, Any, List, Optional

# 全局变量：用于信号处理
_shutdown_event = None
_cleanup_done = False

# 添加项目路径
_scripts_dir = os.path.dirname(os.path.abspath(__file__))
_backend_dir = os.path.abspath(os.path.join(_scripts_dir, '..'))
_project_root = os.path.abspath(os.path.join(_backend_dir, '..'))
sys.path.insert(0, _scripts_dir)
sys.path.insert(0, _backend_dir)

# 加载项目根目录的 .env 文件（包含 LLM_API_KEY 等配置）
from dotenv import load_dotenv
_env_file = os.path.join(_project_root, '.env')
if os.path.exists(_env_file):
    load_dotenv(_env_file)
else:
    _backend_env = os.path.join(_backend_dir, '.env')
    if os.path.exists(_backend_env):
        load_dotenv(_backend_env)


import re


class UnicodeFormatter(logging.Formatter):
    """自定义格式化器，将 Unicode 转义序列转换为可读字符"""
    
    UNICODE_ESCAPE_PATTERN = re.compile(r'\\u([0-9a-fA-F]{4})')
    
    def format(self, record):
        result = super().format(record)
        
        def replace_unicode(match):
            try:
                return chr(int(match.group(1), 16))
            except (ValueError, OverflowError):
                return match.group(0)
        
        return self.UNICODE_ESCAPE_PATTERN.sub(replace_unicode, result)


class MaxTokensWarningFilter(logging.Filter):
    """过滤掉 camel-ai 关于 max_tokens 的警告（我们故意不设置 max_tokens，让模型自行决定）"""
    
    def filter(self, record):
        # 过滤掉包含 max_tokens 警告的日志
        if "max_tokens" in record.getMessage() and "Invalid or missing" in record.getMessage():
            return False
        return True


# 在模块加载时立即添加过滤器，确保在 camel 代码执行前生效
logging.getLogger().addFilter(MaxTokensWarningFilter())


def setup_oasis_logging(log_dir: str):
    """配置 OASIS 的日志，使用固定名称的日志文件"""
    os.makedirs(log_dir, exist_ok=True)
    
    # 清理旧的日志文件
    for f in os.listdir(log_dir):
        old_log = os.path.join(log_dir, f)
        if os.path.isfile(old_log) and f.endswith('.log'):
            try:
                os.remove(old_log)
            except OSError:
                pass
    
    formatter = UnicodeFormatter("%(levelname)s - %(asctime)s - %(name)s - %(message)s")
    
    loggers_config = {
        "social.agent": os.path.join(log_dir, "social.agent.log"),
        "social.twitter": os.path.join(log_dir, "social.twitter.log"),
        "social.rec": os.path.join(log_dir, "social.rec.log"),
        "oasis.env": os.path.join(log_dir, "oasis.env.log"),
        "table": os.path.join(log_dir, "table.log"),
    }
    
    for logger_name, log_file in loggers_config.items():
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        logger.handlers.clear()
        file_handler = logging.FileHandler(log_file, encoding='utf-8', mode='w')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.propagate = False


try:
    from camel.models import ModelFactory
    from camel.types import ModelPlatformType
    import oasis
    from oasis import (
        ActionType,
        LLMAction,
        ManualAction,
        generate_twitter_agent_graph
    )
except ImportError as e:
    print(f"错误: 缺少依赖 {e}")
    print("请先安装: pip install oasis-ai camel-ai")
    sys.exit(1)


# IPC相关常量
IPC_COMMANDS_DIR = "ipc_commands"
IPC_RESPONSES_DIR = "ipc_responses"
ENV_STATUS_FILE = "env_status.json"

class CommandType:
    """命令类型常量"""
    INTERVIEW = "interview"
    BATCH_INTERVIEW = "batch_interview"
    CLOSE_ENV = "close_env"


class IPCHandler:
    """IPC命令处理器"""
    
    def __init__(self, simulation_dir: str, env, agent_graph):
        self.simulation_dir = simulation_dir
        self.env = env
        self.agent_graph = agent_graph
        self.commands_dir = os.path.join(simulation_dir, IPC_COMMANDS_DIR)
        self.responses_dir = os.path.join(simulation_dir, IPC_RESPONSES_DIR)
        self.status_file = os.path.join(simulation_dir, ENV_STATUS_FILE)
        self._running = True
        
        # 确保目录存在
        os.makedirs(self.commands_dir, exist_ok=True)
        os.makedirs(self.responses_dir, exist_ok=True)
    
    def update_status(self, status: str):
        """更新环境状态"""
        with open(self.status_file, 'w', encoding='utf-8') as f:
            json.dump({
                "status": status,
                "timestamp": datetime.now().isoformat()
            }, f, ensure_ascii=False, indent=2)
    
    def poll_command(self) -> Optional[Dict[str, Any]]:
        """轮询获取待处理命令"""
        if not os.path.exists(self.commands_dir):
            return None
        
        # 获取命令文件（按时间排序）
        command_files = []
        for filename in os.listdir(self.commands_dir):
            if filename.endswith('.json'):
                filepath = os.path.join(self.commands_dir, filename)
                command_files.append((filepath, os.path.getmtime(filepath)))

# ... 文件较长，已截断。总行数：780
```

### backend/app/api/graph.py

```python
"""
图谱相关API路由
采用项目上下文机制，服务端持久化状态
"""

import os
import traceback
import threading
from flask import request, jsonify

from . import graph_bp
from ..config import Config
from ..services.ontology_generator import OntologyGenerator
from ..services.graph_builder import GraphBuilderService
from ..services.text_processor import TextProcessor
from ..utils.file_parser import FileParser
from ..utils.logger import get_logger
from ..utils.locale import t, get_locale, set_locale
from ..models.task import TaskManager, TaskStatus
from ..models.project import ProjectManager, ProjectStatus

# 获取日志器
logger = get_logger('mirofish.api')


def allowed_file(filename: str) -> bool:
    """检查文件扩展名是否允许"""
    if not filename or '.' not in filename:
        return False
    ext = os.path.splitext(filename)[1].lower().lstrip('.')
    return ext in Config.ALLOWED_EXTENSIONS


# ============== 项目管理接口 ==============

@graph_bp.route('/project/<project_id>', methods=['GET'])
def get_project(project_id: str):
    """
    获取项目详情
    """
    project = ProjectManager.get_project(project_id)
    
    if not project:
        return jsonify({
            "success": False,
            "error": t('api.projectNotFound', id=project_id)
        }), 404

    return jsonify({
        "success": True,
        "data": project.to_dict()
    })


@graph_bp.route('/project/list', methods=['GET'])
def list_projects():
    """
    列出所有项目
    """
    limit = request.args.get('limit', 50, type=int)
    projects = ProjectManager.list_projects(limit=limit)
    
    return jsonify({
        "success": True,
        "data": [p.to_dict() for p in projects],
        "count": len(projects)
    })


@graph_bp.route('/project/<project_id>', methods=['DELETE'])
def delete_project(project_id: str):
    """
    删除项目
    """
    success = ProjectManager.delete_project(project_id)
    
    if not success:
        return jsonify({
            "success": False,
            "error": t('api.projectDeleteFailed', id=project_id)
        }), 404

    return jsonify({
        "success": True,
        "message": t('api.projectDeleted', id=project_id)
    })


@graph_bp.route('/project/<project_id>/reset', methods=['POST'])
def reset_project(project_id: str):
    """
    重置项目状态（用于重新构建图谱）
    """
    project = ProjectManager.get_project(project_id)
    
    if not project:
        return jsonify({
            "success": False,
            "error": t('api.projectNotFound', id=project_id)
        }), 404

    # 重置到本体已生成状态
    if project.ontology:
        project.status = ProjectStatus.ONTOLOGY_GENERATED
    else:
        project.status = ProjectStatus.CREATED
    
    project.graph_id = None
    project.graph_build_task_id = None
    project.error = None
    ProjectManager.save_project(project)
    
    return jsonify({
        "success": True,
        "message": t('api.projectReset', id=project_id),
        "data": project.to_dict()
    })


# ============== 接口1：上传文件并生成本体 ==============

@graph_bp.route('/ontology/generate', methods=['POST'])
def generate_ontology():
    """
    接口1：上传文件，分析生成本体定义
    
    请求方式：multipart/form-data
    
    参数：
        files: 上传的文件（PDF/MD/TXT），可多个
        simulation_requirement: 模拟需求描述（必填）
        project_name: 项目名称（可选）
        additional_context: 额外说明（可选）
        
    返回：
        {
            "success": true,
            "data": {
                "project_id": "proj_xxxx",
                "ontology": {
                    "entity_types": [...],
                    "edge_types": [...],
                    "analysis_summary": "..."
                },
                "files": [...],
                "total_text_length": 12345
            }
        }
    """
    try:
        logger.info("=== 开始生成本体定义 ===")
        
        # 获取参数
        simulation_requirement = request.form.get('simulation_requirement', '')
        project_name = request.form.get('project_name', 'Unnamed Project')
        additional_context = request.form.get('additional_context', '')
        
        logger.debug(f"项目名称: {project_name}")
        logger.debug(f"模拟需求: {simulation_requirement[:100]}...")
        
        if not simulation_requirement:
            return jsonify({
                "success": False,
                "error": t('api.requireSimulationRequirement')
            }), 400
        
        # 获取上传的文件
        uploaded_files = request.files.getlist('files')
        if not uploaded_files or all(not f.filename for f in uploaded_files):
            return jsonify({
                "success": False,
                "error": t('api.requireFileUpload')
            }), 400
        
        # 创建项目
        project = ProjectManager.create_project(name=project_name)
        project.simulation_requirement = simulation_requirement
        logger.info(f"创建项目: {project.project_id}")
        
        # 保存文件并提取文本

# ... 文件较长，已截断。总行数：622
```

### backend/app/api/report.py

```python
"""
Report API路由
提供模拟报告生成、获取、对话等接口
"""

import os
import traceback
import threading
from flask import request, jsonify, send_file

from . import report_bp
from ..config import Config
from ..services.report_agent import ReportAgent, ReportManager, ReportStatus
from ..services.simulation_manager import SimulationManager
from ..models.project import ProjectManager
from ..models.task import TaskManager, TaskStatus
from ..utils.logger import get_logger
from ..utils.locale import t, get_locale, set_locale

logger = get_logger('mirofish.api.report')


# ============== 报告生成接口 ==============

@report_bp.route('/generate', methods=['POST'])
def generate_report():
    """
    生成模拟分析报告（异步任务）
    
    这是一个耗时操作，接口会立即返回task_id，
    使用 GET /api/report/generate/status 查询进度
    
    请求（JSON）：
        {
            "simulation_id": "sim_xxxx",    // 必填，模拟ID
            "force_regenerate": false        // 可选，强制重新生成
        }
    
    返回：
        {
            "success": true,
            "data": {
                "simulation_id": "sim_xxxx",
                "task_id": "task_xxxx",
                "status": "generating",
                "message": "报告生成任务已启动"
            }
        }
    """
    try:
        data = request.get_json() or {}
        
        simulation_id = data.get('simulation_id')
        if not simulation_id:
            return jsonify({
                "success": False,
                "error": t('api.requireSimulationId')
            }), 400

        force_regenerate = data.get('force_regenerate', False)
        
        # 获取模拟信息
        manager = SimulationManager()
        state = manager.get_simulation(simulation_id)
        
        if not state:
            return jsonify({
                "success": False,
                "error": t('api.simulationNotFound', id=simulation_id)
            }), 404

        # 检查是否已有报告
        if not force_regenerate:
            existing_report = ReportManager.get_report_by_simulation(simulation_id)
            if existing_report and existing_report.status == ReportStatus.COMPLETED:
                return jsonify({
                    "success": True,
                    "data": {
                        "simulation_id": simulation_id,
                        "report_id": existing_report.report_id,
                        "status": "completed",
                        "message": t('api.reportAlreadyExists'),
                        "already_generated": True
                    }
                })
        
        # 获取项目信息
        project = ProjectManager.get_project(state.project_id)
        if not project:
            return jsonify({
                "success": False,
                "error": t('api.projectNotFound', id=state.project_id)
            }), 404
        
        graph_id = state.graph_id or project.graph_id
        if not graph_id:
            return jsonify({
                "success": False,
                "error": t('api.missingGraphIdEnsure')
            }), 400
        
        simulation_requirement = project.simulation_requirement
        if not simulation_requirement:
            return jsonify({
                "success": False,
                "error": t('api.missingSimRequirement')
            }), 400
        
        # 提前生成 report_id，以便立即返回给前端
        import uuid
        report_id = f"report_{uuid.uuid4().hex[:12]}"
        
        # 创建异步任务
        task_manager = TaskManager()
        task_id = task_manager.create_task(
            task_type="report_generate",
            metadata={
                "simulation_id": simulation_id,
                "graph_id": graph_id,
                "report_id": report_id
            }
        )
        
        # Capture locale before spawning background thread
        current_locale = get_locale()

        # 定义后台任务
        def run_generate():
            set_locale(current_locale)
            try:
                task_manager.update_task(
                    task_id,
                    status=TaskStatus.PROCESSING,
                    progress=0,
                    message=t('api.initReportAgent')
                )
                
                # 创建Report Agent
                agent = ReportAgent(
                    graph_id=graph_id,
                    simulation_id=simulation_id,
                    simulation_requirement=simulation_requirement
                )
                
                # 进度回调
                def progress_callback(stage, progress, message):
                    task_manager.update_task(
                        task_id,
                        progress=progress,
                        message=f"[{stage}] {message}"
                    )
                
                # 生成报告（传入预先生成的 report_id）
                report = agent.generate_report(
                    progress_callback=progress_callback,
                    report_id=report_id
                )
                
                # 保存报告
                ReportManager.save_report(report)
                
                if report.status == ReportStatus.COMPLETED:
                    task_manager.complete_task(
                        task_id,
                        result={
                            "report_id": report.report_id,
                            "simulation_id": simulation_id,
                            "status": "completed"
                        }
                    )
                else:
                    task_manager.fail_task(task_id, report.error or t('api.reportGenerateFailed'))
                
            except Exception as e:
                logger.error(f"报告生成失败: {str(e)}")
                task_manager.fail_task(task_id, str(e))
        
        # 启动后台线程
        thread = threading.Thread(target=run_generate, daemon=True)
        thread.start()

# ... 文件较长，已截断。总行数：1020
```

### backend/app/api/simulation.py

```python
"""
模拟相关API路由
Step2: Zep实体读取与过滤、OASIS模拟准备与运行（全程自动化）
"""

import os
import traceback
from flask import request, jsonify, send_file

from . import simulation_bp
from ..config import Config
from ..services.zep_entity_reader import ZepEntityReader
from ..services.oasis_profile_generator import OasisProfileGenerator
from ..services.simulation_manager import SimulationManager, SimulationStatus
from ..services.simulation_runner import SimulationRunner, RunnerStatus
from ..utils.logger import get_logger
from ..utils.locale import t, get_locale, set_locale
from ..models.project import ProjectManager

logger = get_logger('mirofish.api.simulation')


# Interview prompt 优化前缀
# 添加此前缀可以避免Agent调用工具，直接用文本回复
INTERVIEW_PROMPT_PREFIX = "结合你的人设、所有的过往记忆与行动，不调用任何工具直接用文本回复我："


def optimize_interview_prompt(prompt: str) -> str:
    """
    优化Interview提问，添加前缀避免Agent调用工具
    
    Args:
        prompt: 原始提问
        
    Returns:
        优化后的提问
    """
    if not prompt:
        return prompt
    # 避免重复添加前缀
    if prompt.startswith(INTERVIEW_PROMPT_PREFIX):
        return prompt
    return f"{INTERVIEW_PROMPT_PREFIX}{prompt}"


# ============== 实体读取接口 ==============

@simulation_bp.route('/entities/<graph_id>', methods=['GET'])
def get_graph_entities(graph_id: str):
    """
    获取图谱中的所有实体（已过滤）
    
    只返回符合预定义实体类型的节点（Labels不只是Entity的节点）
    
    Query参数：
        entity_types: 逗号分隔的实体类型列表（可选，用于进一步过滤）
        enrich: 是否获取相关边信息（默认true）
    """
    try:
        if not Config.ZEP_API_KEY:
            return jsonify({
                "success": False,
                "error": t('api.zepApiKeyMissing')
            }), 500
        
        entity_types_str = request.args.get('entity_types', '')
        entity_types = [t.strip() for t in entity_types_str.split(',') if t.strip()] if entity_types_str else None
        enrich = request.args.get('enrich', 'true').lower() == 'true'
        
        logger.info(f"获取图谱实体: graph_id={graph_id}, entity_types={entity_types}, enrich={enrich}")
        
        reader = ZepEntityReader()
        result = reader.filter_defined_entities(
            graph_id=graph_id,
            defined_entity_types=entity_types,
            enrich_with_edges=enrich
        )
        
        return jsonify({
            "success": True,
            "data": result.to_dict()
        })
        
    except Exception as e:
        logger.error(f"获取图谱实体失败: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
            "traceback": traceback.format_exc()
        }), 500


@simulation_bp.route('/entities/<graph_id>/<entity_uuid>', methods=['GET'])
def get_entity_detail(graph_id: str, entity_uuid: str):
    """获取单个实体的详细信息"""
    try:
        if not Config.ZEP_API_KEY:
            return jsonify({
                "success": False,
                "error": t('api.zepApiKeyMissing')
            }), 500
        
        reader = ZepEntityReader()
        entity = reader.get_entity_with_context(graph_id, entity_uuid)
        
        if not entity:
            return jsonify({
                "success": False,
                "error": t('api.entityNotFound', id=entity_uuid)
            }), 404
        
        return jsonify({
            "success": True,
            "data": entity.to_dict()
        })
        
    except Exception as e:
        logger.error(f"获取实体详情失败: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
            "traceback": traceback.format_exc()
        }), 500


@simulation_bp.route('/entities/<graph_id>/by-type/<entity_type>', methods=['GET'])
def get_entities_by_type(graph_id: str, entity_type: str):
    """获取指定类型的所有实体"""
    try:
        if not Config.ZEP_API_KEY:
            return jsonify({
                "success": False,
                "error": t('api.zepApiKeyMissing')
            }), 500
        
        enrich = request.args.get('enrich', 'true').lower() == 'true'
        
        reader = ZepEntityReader()
        entities = reader.get_entities_by_type(
            graph_id=graph_id,
            entity_type=entity_type,
            enrich_with_edges=enrich
        )
        
        return jsonify({
            "success": True,
            "data": {
                "entity_type": entity_type,
                "count": len(entities),
                "entities": [e.to_dict() for e in entities]
            }
        })
        
    except Exception as e:
        logger.error(f"获取实体失败: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
            "traceback": traceback.format_exc()
        }), 500


# ============== 模拟管理接口 ==============

@simulation_bp.route('/create', methods=['POST'])
def create_simulation():
    """
    创建新的模拟
    
    注意：max_rounds等参数由LLM智能生成，无需手动设置
    
    请求（JSON）：
        {
            "project_id": "proj_xxxx",      // 必填
            "graph_id": "mirofish_xxxx",    // 可选，如不提供则从project获取
            "enable_twitter": true,          // 可选，默认true
            "enable_reddit": true            // 可选，默认true
        }
    
    返回：

# ... 文件较长，已截断。总行数：2716
```

### backend/app/services/graph_builder.py

```python
"""
图谱构建服务
接口2：使用Zep API构建Standalone Graph
"""

import os
import uuid
import time
import threading
from typing import Dict, Any, List, Optional, Callable
from dataclasses import dataclass

from zep_cloud.client import Zep
from zep_cloud import EpisodeData, EntityEdgeSourceTarget

from ..config import Config
from ..models.task import TaskManager, TaskStatus
from ..utils.zep_paging import fetch_all_nodes, fetch_all_edges
from .text_processor import TextProcessor
from ..utils.locale import t, get_locale, set_locale


@dataclass
class GraphInfo:
    """图谱信息"""
    graph_id: str
    node_count: int
    edge_count: int
    entity_types: List[str]
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "graph_id": self.graph_id,
            "node_count": self.node_count,
            "edge_count": self.edge_count,
            "entity_types": self.entity_types,
        }


class GraphBuilderService:
    """
    图谱构建服务
    负责调用Zep API构建知识图谱
    """
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or Config.ZEP_API_KEY
        if not self.api_key:
            raise ValueError("ZEP_API_KEY 未配置")
        
        self.client = Zep(api_key=self.api_key)
        self.task_manager = TaskManager()
    
    def build_graph_async(
        self,
        text: str,
        ontology: Dict[str, Any],
        graph_name: str = "MiroFish Graph",
        chunk_size: int = 500,
        chunk_overlap: int = 50,
        batch_size: int = 3
    ) -> str:
        """
        异步构建图谱
        
        Args:
            text: 输入文本
            ontology: 本体定义（来自接口1的输出）
            graph_name: 图谱名称
            chunk_size: 文本块大小
            chunk_overlap: 块重叠大小
            batch_size: 每批发送的块数量
            
        Returns:
            任务ID
        """
        # 创建任务
        task_id = self.task_manager.create_task(
            task_type="graph_build",
            metadata={
                "graph_name": graph_name,
                "chunk_size": chunk_size,
                "text_length": len(text),
            }
        )
        
        # Capture locale before spawning background thread
        current_locale = get_locale()

        # 在后台线程中执行构建
        thread = threading.Thread(
            target=self._build_graph_worker,
            args=(task_id, text, ontology, graph_name, chunk_size, chunk_overlap, batch_size, current_locale)
        )
        thread.daemon = True
        thread.start()
        
        return task_id
    
    def _build_graph_worker(
        self,
        task_id: str,
        text: str,
        ontology: Dict[str, Any],
        graph_name: str,
        chunk_size: int,
        chunk_overlap: int,
        batch_size: int,
        locale: str = 'zh'
    ):
        """图谱构建工作线程"""
        set_locale(locale)
        try:
            self.task_manager.update_task(
                task_id,
                status=TaskStatus.PROCESSING,
                progress=5,
                message=t('progress.startBuildingGraph')
            )
            
            # 1. 创建图谱
            graph_id = self.create_graph(graph_name)
            self.task_manager.update_task(
                task_id,
                progress=10,
                message=t('progress.graphCreated', graphId=graph_id)
            )
            
            # 2. 设置本体
            self.set_ontology(graph_id, ontology)
            self.task_manager.update_task(
                task_id,
                progress=15,
                message=t('progress.ontologySet')
            )
            
            # 3. 文本分块
            chunks = TextProcessor.split_text(text, chunk_size, chunk_overlap)
            total_chunks = len(chunks)
            self.task_manager.update_task(
                task_id,
                progress=20,
                message=t('progress.textSplit', count=total_chunks)
            )
            
            # 4. 分批发送数据
            episode_uuids = self.add_text_batches(
                graph_id, chunks, batch_size,
                lambda msg, prog: self.task_manager.update_task(
                    task_id,
                    progress=20 + int(prog * 0.4),  # 20-60%
                    message=msg
                )
            )
            
            # 5. 等待Zep处理完成
            self.task_manager.update_task(
                task_id,
                progress=60,
                message=t('progress.waitingZepProcess')
            )
            
            self._wait_for_episodes(
                episode_uuids,
                lambda msg, prog: self.task_manager.update_task(
                    task_id,
                    progress=60 + int(prog * 0.3),  # 60-90%
                    message=msg
                )
            )
            
            # 6. 获取图谱信息
            self.task_manager.update_task(
                task_id,
                progress=90,
                message=t('progress.fetchingGraphInfo')
            )
            
            graph_info = self._get_graph_info(graph_id)
            

# ... 文件较长，已截断。总行数：506
```

### backend/app/services/oasis_profile_generator.py

```python
"""
OASIS Agent Profile生成器
将Zep图谱中的实体转换为OASIS模拟平台所需的Agent Profile格式

优化改进：
1. 调用Zep检索功能二次丰富节点信息
2. 优化提示词生成非常详细的人设
3. 区分个人实体和抽象群体实体
"""

import json
import random
import time
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
from datetime import datetime

from openai import OpenAI
from zep_cloud.client import Zep

from ..config import Config
from ..utils.logger import get_logger
from ..utils.locale import get_language_instruction, get_locale, set_locale, t
from .zep_entity_reader import EntityNode, ZepEntityReader

logger = get_logger('mirofish.oasis_profile')


@dataclass
class OasisAgentProfile:
    """OASIS Agent Profile数据结构"""
    # 通用字段
    user_id: int
    user_name: str
    name: str
    bio: str
    persona: str
    
    # 可选字段 - Reddit风格
    karma: int = 1000
    
    # 可选字段 - Twitter风格
    friend_count: int = 100
    follower_count: int = 150
    statuses_count: int = 500
    
    # 额外人设信息
    age: Optional[int] = None
    gender: Optional[str] = None
    mbti: Optional[str] = None
    country: Optional[str] = None
    profession: Optional[str] = None
    interested_topics: List[str] = field(default_factory=list)
    
    # 来源实体信息
    source_entity_uuid: Optional[str] = None
    source_entity_type: Optional[str] = None
    
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))
    
    def to_reddit_format(self) -> Dict[str, Any]:
        """转换为Reddit平台格式"""
        profile = {
            "user_id": self.user_id,
            "username": self.user_name,  # OASIS 库要求字段名为 username（无下划线）
            "name": self.name,
            "bio": self.bio,
            "persona": self.persona,
            "karma": self.karma,
            "created_at": self.created_at,
        }
        
        # 添加额外人设信息（如果有）
        if self.age:
            profile["age"] = self.age
        if self.gender:
            profile["gender"] = self.gender
        if self.mbti:
            profile["mbti"] = self.mbti
        if self.country:
            profile["country"] = self.country
        if self.profession:
            profile["profession"] = self.profession
        if self.interested_topics:
            profile["interested_topics"] = self.interested_topics
        
        return profile
    
    def to_twitter_format(self) -> Dict[str, Any]:
        """转换为Twitter平台格式"""
        profile = {
            "user_id": self.user_id,
            "username": self.user_name,  # OASIS 库要求字段名为 username（无下划线）
            "name": self.name,
            "bio": self.bio,
            "persona": self.persona,
            "friend_count": self.friend_count,
            "follower_count": self.follower_count,
            "statuses_count": self.statuses_count,
            "created_at": self.created_at,
        }
        
        # 添加额外人设信息
        if self.age:
            profile["age"] = self.age
        if self.gender:
            profile["gender"] = self.gender
        if self.mbti:
            profile["mbti"] = self.mbti
        if self.country:
            profile["country"] = self.country
        if self.profession:
            profile["profession"] = self.profession
        if self.interested_topics:
            profile["interested_topics"] = self.interested_topics
        
        return profile
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为完整字典格式"""
        return {
            "user_id": self.user_id,
            "user_name": self.user_name,
            "name": self.name,
            "bio": self.bio,
            "persona": self.persona,
            "karma": self.karma,
            "friend_count": self.friend_count,
            "follower_count": self.follower_count,
            "statuses_count": self.statuses_count,
            "age": self.age,
            "gender": self.gender,
            "mbti": self.mbti,
            "country": self.country,
            "profession": self.profession,
            "interested_topics": self.interested_topics,
            "source_entity_uuid": self.source_entity_uuid,
            "source_entity_type": self.source_entity_type,
            "created_at": self.created_at,
        }


class OasisProfileGenerator:
    """
    OASIS Profile生成器
    
    将Zep图谱中的实体转换为OASIS模拟所需的Agent Profile
    
    优化特性：
    1. 调用Zep图谱检索功能获取更丰富的上下文
    2. 生成非常详细的人设（包括基本信息、职业经历、性格特征、社交媒体行为等）
    3. 区分个人实体和抽象群体实体
    """
    
    # MBTI类型列表
    MBTI_TYPES = [
        "INTJ", "INTP", "ENTJ", "ENTP",
        "INFJ", "INFP", "ENFJ", "ENFP",
        "ISTJ", "ISFJ", "ESTJ", "ESFJ",
        "ISTP", "ISFP", "ESTP", "ESFP"
    ]
    
    # 常见国家列表
    COUNTRIES = [
        "China", "US", "UK", "Japan", "Germany", "France", 
        "Canada", "Australia", "Brazil", "India", "South Korea"
    ]
    
    # 个人类型实体（需要生成具体人设）
    INDIVIDUAL_ENTITY_TYPES = [
        "student", "alumni", "professor", "person", "publicfigure", 
        "expert", "faculty", "official", "journalist", "activist"
    ]
    
    # 群体/机构类型实体（需要生成群体代表人设）
    GROUP_ENTITY_TYPES = [
        "university", "governmentagency", "organization", "ngo", 
        "mediaoutlet", "company", "institution", "group", "community"
    ]
    

# ... 文件较长，已截断。总行数：1205
```

### backend/app/services/report_agent.py

```python
"""
Report Agent服务
使用LangChain + Zep实现ReACT模式的模拟报告生成

功能：
1. 根据模拟需求和Zep图谱信息生成报告
2. 先规划目录结构，然后分段生成
3. 每段采用ReACT多轮思考与反思模式
4. 支持与用户对话，在对话中自主调用检索工具
"""

import os
import json
import time
import re
from typing import Dict, Any, List, Optional, Callable
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

from ..config import Config
from ..utils.llm_client import LLMClient
from ..utils.logger import get_logger
from ..utils.locale import get_language_instruction, t
from .zep_tools import (
    ZepToolsService, 
    SearchResult, 
    InsightForgeResult, 
    PanoramaResult,
    InterviewResult
)

logger = get_logger('mirofish.report_agent')


class ReportLogger:
    """
    Report Agent 详细日志记录器
    
    在报告文件夹中生成 agent_log.jsonl 文件，记录每一步详细动作。
    每行是一个完整的 JSON 对象，包含时间戳、动作类型、详细内容等。
    """
    
    def __init__(self, report_id: str):
        """
        初始化日志记录器
        
        Args:
            report_id: 报告ID，用于确定日志文件路径
        """
        self.report_id = report_id
        self.log_file_path = os.path.join(
            Config.UPLOAD_FOLDER, 'reports', report_id, 'agent_log.jsonl'
        )
        self.start_time = datetime.now()
        self._ensure_log_file()
    
    def _ensure_log_file(self):
        """确保日志文件所在目录存在"""
        log_dir = os.path.dirname(self.log_file_path)
        os.makedirs(log_dir, exist_ok=True)
    
    def _get_elapsed_time(self) -> float:
        """获取从开始到现在的耗时（秒）"""
        return (datetime.now() - self.start_time).total_seconds()
    
    def log(
        self, 
        action: str, 
        stage: str,
        details: Dict[str, Any],
        section_title: str = None,
        section_index: int = None
    ):
        """
        记录一条日志
        
        Args:
            action: 动作类型，如 'start', 'tool_call', 'llm_response', 'section_complete' 等
            stage: 当前阶段，如 'planning', 'generating', 'completed'
            details: 详细内容字典，不截断
            section_title: 当前章节标题（可选）
            section_index: 当前章节索引（可选）
        """
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "elapsed_seconds": round(self._get_elapsed_time(), 2),
            "report_id": self.report_id,
            "action": action,
            "stage": stage,
            "section_title": section_title,
            "section_index": section_index,
            "details": details
        }
        
        # 追加写入 JSONL 文件
        with open(self.log_file_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps(log_entry, ensure_ascii=False) + '\n')
    
    def log_start(self, simulation_id: str, graph_id: str, simulation_requirement: str):
        """记录报告生成开始"""
        self.log(
            action="report_start",
            stage="pending",
            details={
                "simulation_id": simulation_id,
                "graph_id": graph_id,
                "simulation_requirement": simulation_requirement,
                "message": t('report.taskStarted')
            }
        )
    
    def log_planning_start(self):
        """记录大纲规划开始"""
        self.log(
            action="planning_start",
            stage="planning",
            details={"message": t('report.planningStart')}
        )
    
    def log_planning_context(self, context: Dict[str, Any]):
        """记录规划时获取的上下文信息"""
        self.log(
            action="planning_context",
            stage="planning",
            details={
                "message": t('report.fetchSimContext'),
                "context": context
            }
        )
    
    def log_planning_complete(self, outline_dict: Dict[str, Any]):
        """记录大纲规划完成"""
        self.log(
            action="planning_complete",
            stage="planning",
            details={
                "message": t('report.planningComplete'),
                "outline": outline_dict
            }
        )
    
    def log_section_start(self, section_title: str, section_index: int):
        """记录章节生成开始"""
        self.log(
            action="section_start",
            stage="generating",
            section_title=section_title,
            section_index=section_index,
            details={"message": t('report.sectionStart', title=section_title)}
        )
    
    def log_react_thought(self, section_title: str, section_index: int, iteration: int, thought: str):
        """记录 ReACT 思考过程"""
        self.log(
            action="react_thought",
            stage="generating",
            section_title=section_title,
            section_index=section_index,
            details={
                "iteration": iteration,
                "thought": thought,
                "message": t('report.reactThought', iteration=iteration)
            }
        )
    
    def log_tool_call(
        self, 
        section_title: str, 
        section_index: int,
        tool_name: str, 
        parameters: Dict[str, Any],
        iteration: int
    ):
        """记录工具调用"""
        self.log(
            action="tool_call",
            stage="generating",
            section_title=section_title,
            section_index=section_index,

# ... 文件较长，已截断。总行数：2572
```

### backend/app/services/simulation_config_generator.py

```python
"""
模拟配置智能生成器
使用LLM根据模拟需求、文档内容、图谱信息自动生成细致的模拟参数
实现全程自动化，无需人工设置参数

采用分步生成策略，避免一次性生成过长内容导致失败：
1. 生成时间配置
2. 生成事件配置
3. 分批生成Agent配置
4. 生成平台配置
"""

import json
import math
from typing import Dict, Any, List, Optional, Callable
from dataclasses import dataclass, field, asdict
from datetime import datetime

from openai import OpenAI

from ..config import Config
from ..utils.logger import get_logger
from ..utils.locale import get_language_instruction, t
from .zep_entity_reader import EntityNode, ZepEntityReader

logger = get_logger('mirofish.simulation_config')

# 中国作息时间配置（北京时间）
CHINA_TIMEZONE_CONFIG = {
    # 深夜时段（几乎无人活动）
    "dead_hours": [0, 1, 2, 3, 4, 5],
    # 早间时段（逐渐醒来）
    "morning_hours": [6, 7, 8],
    # 工作时段
    "work_hours": [9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
    # 晚间高峰（最活跃）
    "peak_hours": [19, 20, 21, 22],
    # 夜间时段（活跃度下降）
    "night_hours": [23],
    # 活跃度系数
    "activity_multipliers": {
        "dead": 0.05,      # 凌晨几乎无人
        "morning": 0.4,    # 早间逐渐活跃
        "work": 0.7,       # 工作时段中等
        "peak": 1.5,       # 晚间高峰
        "night": 0.5       # 深夜下降
    }
}


@dataclass
class AgentActivityConfig:
    """单个Agent的活动配置"""
    agent_id: int
    entity_uuid: str
    entity_name: str
    entity_type: str
    
    # 活跃度配置 (0.0-1.0)
    activity_level: float = 0.5  # 整体活跃度
    
    # 发言频率（每小时预期发言次数）
    posts_per_hour: float = 1.0
    comments_per_hour: float = 2.0
    
    # 活跃时间段（24小时制，0-23）
    active_hours: List[int] = field(default_factory=lambda: list(range(8, 23)))
    
    # 响应速度（对热点事件的反应延迟，单位：模拟分钟）
    response_delay_min: int = 5
    response_delay_max: int = 60
    
    # 情感倾向 (-1.0到1.0，负面到正面)
    sentiment_bias: float = 0.0
    
    # 立场（对特定话题的态度）
    stance: str = "neutral"  # supportive, opposing, neutral, observer
    
    # 影响力权重（决定其发言被其他Agent看到的概率）
    influence_weight: float = 1.0


@dataclass  
class TimeSimulationConfig:
    """时间模拟配置（基于中国人作息习惯）"""
    # 模拟总时长（模拟小时数）
    total_simulation_hours: int = 72  # 默认模拟72小时（3天）
    
    # 每轮代表的时间（模拟分钟）- 默认60分钟（1小时），加快时间流速
    minutes_per_round: int = 60
    
    # 每小时激活的Agent数量范围
    agents_per_hour_min: int = 5
    agents_per_hour_max: int = 20
    
    # 高峰时段（晚间19-22点，中国人最活跃的时间）
    peak_hours: List[int] = field(default_factory=lambda: [19, 20, 21, 22])
    peak_activity_multiplier: float = 1.5
    
    # 低谷时段（凌晨0-5点，几乎无人活动）
    off_peak_hours: List[int] = field(default_factory=lambda: [0, 1, 2, 3, 4, 5])
    off_peak_activity_multiplier: float = 0.05  # 凌晨活跃度极低
    
    # 早间时段
    morning_hours: List[int] = field(default_factory=lambda: [6, 7, 8])
    morning_activity_multiplier: float = 0.4
    
    # 工作时段
    work_hours: List[int] = field(default_factory=lambda: [9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
    work_activity_multiplier: float = 0.7


@dataclass
class EventConfig:
    """事件配置"""
    # 初始事件（模拟开始时的触发事件）
    initial_posts: List[Dict[str, Any]] = field(default_factory=list)
    
    # 定时事件（在特定时间触发的事件）
    scheduled_events: List[Dict[str, Any]] = field(default_factory=list)
    
    # 热点话题关键词
    hot_topics: List[str] = field(default_factory=list)
    
    # 舆论引导方向
    narrative_direction: str = ""


@dataclass
class PlatformConfig:
    """平台特定配置"""
    platform: str  # twitter or reddit
    
    # 推荐算法权重
    recency_weight: float = 0.4  # 时间新鲜度
    popularity_weight: float = 0.3  # 热度
    relevance_weight: float = 0.3  # 相关性
    
    # 病毒传播阈值（达到多少互动后触发扩散）
    viral_threshold: int = 10
    
    # 回声室效应强度（相似观点聚集程度）
    echo_chamber_strength: float = 0.5


@dataclass
class SimulationParameters:
    """完整的模拟参数配置"""
    # 基础信息
    simulation_id: str
    project_id: str
    graph_id: str
    simulation_requirement: str
    
    # 时间配置
    time_config: TimeSimulationConfig = field(default_factory=TimeSimulationConfig)
    
    # Agent配置列表
    agent_configs: List[AgentActivityConfig] = field(default_factory=list)
    
    # 事件配置
    event_config: EventConfig = field(default_factory=EventConfig)
    
    # 平台配置
    twitter_config: Optional[PlatformConfig] = None
    reddit_config: Optional[PlatformConfig] = None
    
    # LLM配置
    llm_model: str = ""
    llm_base_url: str = ""
    
    # 生成元数据
    generated_at: str = field(default_factory=lambda: datetime.now().isoformat())
    generation_reasoning: str = ""  # LLM的推理说明
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        time_dict = asdict(self.time_config)
        return {
            "simulation_id": self.simulation_id,

# ... 文件较长，已截断。总行数：991
```

### backend/app/services/simulation_ipc.py

```python
"""
模拟IPC通信模块
用于Flask后端和模拟脚本之间的进程间通信

通过文件系统实现简单的命令/响应模式：
1. Flask写入命令到 commands/ 目录
2. 模拟脚本轮询命令目录，执行命令并写入响应到 responses/ 目录
3. Flask轮询响应目录获取结果
"""

import os
import json
import time
import uuid
from typing import Dict, Any, Optional, List
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

from ..utils.logger import get_logger

logger = get_logger('mirofish.simulation_ipc')


class CommandType(str, Enum):
    """命令类型"""
    INTERVIEW = "interview"           # 单个Agent采访
    BATCH_INTERVIEW = "batch_interview"  # 批量采访
    CLOSE_ENV = "close_env"           # 关闭环境


class CommandStatus(str, Enum):
    """命令状态"""
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class IPCCommand:
    """IPC命令"""
    command_id: str
    command_type: CommandType
    args: Dict[str, Any]
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "command_id": self.command_id,
            "command_type": self.command_type.value,
            "args": self.args,
            "timestamp": self.timestamp
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'IPCCommand':
        return cls(
            command_id=data["command_id"],
            command_type=CommandType(data["command_type"]),
            args=data.get("args", {}),
            timestamp=data.get("timestamp", datetime.now().isoformat())
        )


@dataclass
class IPCResponse:
    """IPC响应"""
    command_id: str
    status: CommandStatus
    result: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "command_id": self.command_id,
            "status": self.status.value,
            "result": self.result,
            "error": self.error,
            "timestamp": self.timestamp
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'IPCResponse':
        return cls(
            command_id=data["command_id"],
            status=CommandStatus(data["status"]),
            result=data.get("result"),
            error=data.get("error"),
            timestamp=data.get("timestamp", datetime.now().isoformat())
        )


class SimulationIPCClient:
    """
    模拟IPC客户端（Flask端使用）
    
    用于向模拟进程发送命令并等待响应
    """
    
    def __init__(self, simulation_dir: str):
        """
        初始化IPC客户端
        
        Args:
            simulation_dir: 模拟数据目录
        """
        self.simulation_dir = simulation_dir
        self.commands_dir = os.path.join(simulation_dir, "ipc_commands")
        self.responses_dir = os.path.join(simulation_dir, "ipc_responses")
        
        # 确保目录存在
        os.makedirs(self.commands_dir, exist_ok=True)
        os.makedirs(self.responses_dir, exist_ok=True)
    
    def send_command(
        self,
        command_type: CommandType,
        args: Dict[str, Any],
        timeout: float = 60.0,
        poll_interval: float = 0.5
    ) -> IPCResponse:
        """
        发送命令并等待响应
        
        Args:
            command_type: 命令类型
            args: 命令参数
            timeout: 超时时间（秒）
            poll_interval: 轮询间隔（秒）
            
        Returns:
            IPCResponse
            
        Raises:
            TimeoutError: 等待响应超时
        """
        command_id = str(uuid.uuid4())
        command = IPCCommand(
            command_id=command_id,
            command_type=command_type,
            args=args
        )
        
        # 写入命令文件
        command_file = os.path.join(self.commands_dir, f"{command_id}.json")
        with open(command_file, 'w', encoding='utf-8') as f:
            json.dump(command.to_dict(), f, ensure_ascii=False, indent=2)
        
        logger.info(f"发送IPC命令: {command_type.value}, command_id={command_id}")
        
        # 等待响应
        response_file = os.path.join(self.responses_dir, f"{command_id}.json")
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            if os.path.exists(response_file):
                try:
                    with open(response_file, 'r', encoding='utf-8') as f:
                        response_data = json.load(f)
                    response = IPCResponse.from_dict(response_data)
                    
                    # 清理命令和响应文件
                    try:
                        os.remove(command_file)
                        os.remove(response_file)
                    except OSError:
                        pass
                    
                    logger.info(f"收到IPC响应: command_id={command_id}, status={response.status.value}")
                    return response
                except (json.JSONDecodeError, KeyError) as e:
                    logger.warning(f"解析响应失败: {e}")
            
            time.sleep(poll_interval)
        
        # 超时
        logger.error(f"等待IPC响应超时: command_id={command_id}")
        

# ... 文件较长，已截断。总行数：394
```

### backend/app/services/simulation_manager.py

```python
"""
OASIS模拟管理器
管理Twitter和Reddit双平台并行模拟
使用预设脚本 + LLM智能生成配置参数
"""

import os
import json
import shutil
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

from ..config import Config
from ..utils.logger import get_logger
from .zep_entity_reader import ZepEntityReader, FilteredEntities
from .oasis_profile_generator import OasisProfileGenerator, OasisAgentProfile
from .simulation_config_generator import SimulationConfigGenerator, SimulationParameters
from ..utils.locale import t

logger = get_logger('mirofish.simulation')


class SimulationStatus(str, Enum):
    """模拟状态"""
    CREATED = "created"
    PREPARING = "preparing"
    READY = "ready"
    RUNNING = "running"
    PAUSED = "paused"
    STOPPED = "stopped"      # 模拟被手动停止
    COMPLETED = "completed"  # 模拟自然完成
    FAILED = "failed"


class PlatformType(str, Enum):
    """平台类型"""
    TWITTER = "twitter"
    REDDIT = "reddit"


@dataclass
class SimulationState:
    """模拟状态"""
    simulation_id: str
    project_id: str
    graph_id: str
    
    # 平台启用状态
    enable_twitter: bool = True
    enable_reddit: bool = True
    
    # 状态
    status: SimulationStatus = SimulationStatus.CREATED
    
    # 准备阶段数据
    entities_count: int = 0
    profiles_count: int = 0
    entity_types: List[str] = field(default_factory=list)
    
    # 配置生成信息
    config_generated: bool = False
    config_reasoning: str = ""
    
    # 运行时数据
    current_round: int = 0
    twitter_status: str = "not_started"
    reddit_status: str = "not_started"
    
    # 时间戳
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())
    
    # 错误信息
    error: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """完整状态字典（内部使用）"""
        return {
            "simulation_id": self.simulation_id,
            "project_id": self.project_id,
            "graph_id": self.graph_id,
            "enable_twitter": self.enable_twitter,
            "enable_reddit": self.enable_reddit,
            "status": self.status.value,
            "entities_count": self.entities_count,
            "profiles_count": self.profiles_count,
            "entity_types": self.entity_types,
            "config_generated": self.config_generated,
            "config_reasoning": self.config_reasoning,
            "current_round": self.current_round,
            "twitter_status": self.twitter_status,
            "reddit_status": self.reddit_status,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "error": self.error,
        }
    
    def to_simple_dict(self) -> Dict[str, Any]:
        """简化状态字典（API返回使用）"""
        return {
            "simulation_id": self.simulation_id,
            "project_id": self.project_id,
            "graph_id": self.graph_id,
            "status": self.status.value,
            "entities_count": self.entities_count,
            "profiles_count": self.profiles_count,
            "entity_types": self.entity_types,
            "config_generated": self.config_generated,
            "error": self.error,
        }


class SimulationManager:
    """
    模拟管理器
    
    核心功能：
    1. 从Zep图谱读取实体并过滤
    2. 生成OASIS Agent Profile
    3. 使用LLM智能生成模拟配置参数
    4. 准备预设脚本所需的所有文件
    """
    
    # 模拟数据存储目录
    SIMULATION_DATA_DIR = os.path.join(
        os.path.dirname(__file__), 
        '../../uploads/simulations'
    )
    
    def __init__(self):
        # 确保目录存在
        os.makedirs(self.SIMULATION_DATA_DIR, exist_ok=True)
        
        # 内存中的模拟状态缓存
        self._simulations: Dict[str, SimulationState] = {}
    
    def _get_simulation_dir(self, simulation_id: str) -> str:
        """获取模拟数据目录"""
        sim_dir = os.path.join(self.SIMULATION_DATA_DIR, simulation_id)
        os.makedirs(sim_dir, exist_ok=True)
        return sim_dir
    
    def _save_simulation_state(self, state: SimulationState):
        """保存模拟状态到文件"""
        sim_dir = self._get_simulation_dir(state.simulation_id)
        state_file = os.path.join(sim_dir, "state.json")
        
        state.updated_at = datetime.now().isoformat()
        
        with open(state_file, 'w', encoding='utf-8') as f:
            json.dump(state.to_dict(), f, ensure_ascii=False, indent=2)
        
        self._simulations[state.simulation_id] = state
    
    def _load_simulation_state(self, simulation_id: str) -> Optional[SimulationState]:
        """从文件加载模拟状态"""
        if simulation_id in self._simulations:
            return self._simulations[simulation_id]
        
        sim_dir = self._get_simulation_dir(simulation_id)
        state_file = os.path.join(sim_dir, "state.json")
        
        if not os.path.exists(state_file):
            return None
        
        with open(state_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        state = SimulationState(
            simulation_id=simulation_id,
            project_id=data.get("project_id", ""),
            graph_id=data.get("graph_id", ""),
            enable_twitter=data.get("enable_twitter", True),
            enable_reddit=data.get("enable_reddit", True),
            status=SimulationStatus(data.get("status", "created")),
            entities_count=data.get("entities_count", 0),
            profiles_count=data.get("profiles_count", 0),
            entity_types=data.get("entity_types", []),

# ... 文件较长，已截断。总行数：529
```

### backend/app/services/simulation_runner.py

```python
"""
OASIS模拟运行器
在后台运行模拟并记录每个Agent的动作，支持实时状态监控
"""

import os
import sys
import json
import time
import asyncio
import threading
import subprocess
import signal
import atexit
from typing import Dict, Any, List, Optional, Union
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from queue import Queue

from ..config import Config
from ..utils.logger import get_logger
from ..utils.locale import get_locale, set_locale
from .zep_graph_memory_updater import ZepGraphMemoryManager
from .simulation_ipc import SimulationIPCClient, CommandType, IPCResponse

logger = get_logger('mirofish.simulation_runner')

# 标记是否已注册清理函数
_cleanup_registered = False

# 平台检测
IS_WINDOWS = sys.platform == 'win32'


class RunnerStatus(str, Enum):
    """运行器状态"""
    IDLE = "idle"
    STARTING = "starting"
    RUNNING = "running"
    PAUSED = "paused"
    STOPPING = "stopping"
    STOPPED = "stopped"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class AgentAction:
    """Agent动作记录"""
    round_num: int
    timestamp: str
    platform: str  # twitter / reddit
    agent_id: int
    agent_name: str
    action_type: str  # CREATE_POST, LIKE_POST, etc.
    action_args: Dict[str, Any] = field(default_factory=dict)
    result: Optional[str] = None
    success: bool = True
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "round_num": self.round_num,
            "timestamp": self.timestamp,
            "platform": self.platform,
            "agent_id": self.agent_id,
            "agent_name": self.agent_name,
            "action_type": self.action_type,
            "action_args": self.action_args,
            "result": self.result,
            "success": self.success,
        }


@dataclass
class RoundSummary:
    """每轮摘要"""
    round_num: int
    start_time: str
    end_time: Optional[str] = None
    simulated_hour: int = 0
    twitter_actions: int = 0
    reddit_actions: int = 0
    active_agents: List[int] = field(default_factory=list)
    actions: List[AgentAction] = field(default_factory=list)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "round_num": self.round_num,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "simulated_hour": self.simulated_hour,
            "twitter_actions": self.twitter_actions,
            "reddit_actions": self.reddit_actions,
            "active_agents": self.active_agents,
            "actions_count": len(self.actions),
            "actions": [a.to_dict() for a in self.actions],
        }


@dataclass
class SimulationRunState:
    """模拟运行状态（实时）"""
    simulation_id: str
    runner_status: RunnerStatus = RunnerStatus.IDLE
    
    # 进度信息
    current_round: int = 0
    total_rounds: int = 0
    simulated_hours: int = 0
    total_simulation_hours: int = 0
    
    # 各平台独立轮次和模拟时间（用于双平台并行显示）
    twitter_current_round: int = 0
    reddit_current_round: int = 0
    twitter_simulated_hours: int = 0
    reddit_simulated_hours: int = 0
    
    # 平台状态
    twitter_running: bool = False
    reddit_running: bool = False
    twitter_actions_count: int = 0
    reddit_actions_count: int = 0
    
    # 平台完成状态（通过检测 actions.jsonl 中的 simulation_end 事件）
    twitter_completed: bool = False
    reddit_completed: bool = False
    
    # 每轮摘要
    rounds: List[RoundSummary] = field(default_factory=list)
    
    # 最近动作（用于前端实时展示）
    recent_actions: List[AgentAction] = field(default_factory=list)
    max_recent_actions: int = 50
    
    # 时间戳
    started_at: Optional[str] = None
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())
    completed_at: Optional[str] = None
    
    # 错误信息
    error: Optional[str] = None
    
    # 进程ID（用于停止）
    process_pid: Optional[int] = None
    
    def add_action(self, action: AgentAction):
        """添加动作到最近动作列表"""
        self.recent_actions.insert(0, action)
        if len(self.recent_actions) > self.max_recent_actions:
            self.recent_actions = self.recent_actions[:self.max_recent_actions]
        
        if action.platform == "twitter":
            self.twitter_actions_count += 1
        else:
            self.reddit_actions_count += 1
        
        self.updated_at = datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "simulation_id": self.simulation_id,
            "runner_status": self.runner_status.value,
            "current_round": self.current_round,
            "total_rounds": self.total_rounds,
            "simulated_hours": self.simulated_hours,
            "total_simulation_hours": self.total_simulation_hours,
            "progress_percent": round(self.current_round / max(self.total_rounds, 1) * 100, 1),
            # 各平台独立轮次和时间
            "twitter_current_round": self.twitter_current_round,
            "reddit_current_round": self.reddit_current_round,
            "twitter_simulated_hours": self.twitter_simulated_hours,
            "reddit_simulated_hours": self.reddit_simulated_hours,
            "twitter_running": self.twitter_running,
            "reddit_running": self.reddit_running,
            "twitter_completed": self.twitter_completed,
            "reddit_completed": self.reddit_completed,
            "twitter_actions_count": self.twitter_actions_count,
            "reddit_actions_count": self.reddit_actions_count,
            "total_actions_count": self.twitter_actions_count + self.reddit_actions_count,

# ... 文件较长，已截断。总行数：1768
```

### backend/app/services/zep_entity_reader.py

```python
"""
Zep实体读取与过滤服务
从Zep图谱中读取节点，筛选出符合预定义实体类型的节点
"""

import time
from typing import Dict, Any, List, Optional, Set, Callable, TypeVar
from dataclasses import dataclass, field

from zep_cloud.client import Zep

from ..config import Config
from ..utils.logger import get_logger
from ..utils.zep_paging import fetch_all_nodes, fetch_all_edges

logger = get_logger('mirofish.zep_entity_reader')

# 用于泛型返回类型
T = TypeVar('T')


@dataclass
class EntityNode:
    """实体节点数据结构"""
    uuid: str
    name: str
    labels: List[str]
    summary: str
    attributes: Dict[str, Any]
    # 相关的边信息
    related_edges: List[Dict[str, Any]] = field(default_factory=list)
    # 相关的其他节点信息
    related_nodes: List[Dict[str, Any]] = field(default_factory=list)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "uuid": self.uuid,
            "name": self.name,
            "labels": self.labels,
            "summary": self.summary,
            "attributes": self.attributes,
            "related_edges": self.related_edges,
            "related_nodes": self.related_nodes,
        }
    
    def get_entity_type(self) -> Optional[str]:
        """获取实体类型（排除默认的Entity标签）"""
        for label in self.labels:
            if label not in ["Entity", "Node"]:
                return label
        return None


@dataclass
class FilteredEntities:
    """过滤后的实体集合"""
    entities: List[EntityNode]
    entity_types: Set[str]
    total_count: int
    filtered_count: int
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "entities": [e.to_dict() for e in self.entities],
            "entity_types": list(self.entity_types),
            "total_count": self.total_count,
            "filtered_count": self.filtered_count,
        }


class ZepEntityReader:
    """
    Zep实体读取与过滤服务
    
    主要功能：
    1. 从Zep图谱读取所有节点
    2. 筛选出符合预定义实体类型的节点（Labels不只是Entity的节点）
    3. 获取每个实体的相关边和关联节点信息
    """
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or Config.ZEP_API_KEY
        if not self.api_key:
            raise ValueError("ZEP_API_KEY 未配置")
        
        self.client = Zep(api_key=self.api_key)
    
    def _call_with_retry(
        self, 
        func: Callable[[], T], 
        operation_name: str,
        max_retries: int = 3,
        initial_delay: float = 2.0
    ) -> T:
        """
        带重试机制的Zep API调用
        
        Args:
            func: 要执行的函数（无参数的lambda或callable）
            operation_name: 操作名称，用于日志
            max_retries: 最大重试次数（默认3次，即最多尝试3次）
            initial_delay: 初始延迟秒数
            
        Returns:
            API调用结果
        """
        last_exception = None
        delay = initial_delay
        
        for attempt in range(max_retries):
            try:
                return func()
            except Exception as e:
                last_exception = e
                if attempt < max_retries - 1:
                    logger.warning(
                        f"Zep {operation_name} 第 {attempt + 1} 次尝试失败: {str(e)[:100]}, "
                        f"{delay:.1f}秒后重试..."
                    )
                    time.sleep(delay)
                    delay *= 2  # 指数退避
                else:
                    logger.error(f"Zep {operation_name} 在 {max_retries} 次尝试后仍失败: {str(e)}")
        
        raise last_exception
    
    def get_all_nodes(self, graph_id: str) -> List[Dict[str, Any]]:
        """
        获取图谱的所有节点（分页获取）

        Args:
            graph_id: 图谱ID

        Returns:
            节点列表
        """
        logger.info(f"获取图谱 {graph_id} 的所有节点...")

        nodes = fetch_all_nodes(self.client, graph_id)

        nodes_data = []
        for node in nodes:
            nodes_data.append({
                "uuid": getattr(node, 'uuid_', None) or getattr(node, 'uuid', ''),
                "name": node.name or "",
                "labels": node.labels or [],
                "summary": node.summary or "",
                "attributes": node.attributes or {},
            })

        logger.info(f"共获取 {len(nodes_data)} 个节点")
        return nodes_data

    def get_all_edges(self, graph_id: str) -> List[Dict[str, Any]]:
        """
        获取图谱的所有边（分页获取）

        Args:
            graph_id: 图谱ID

        Returns:
            边列表
        """
        logger.info(f"获取图谱 {graph_id} 的所有边...")

        edges = fetch_all_edges(self.client, graph_id)

        edges_data = []
        for edge in edges:
            edges_data.append({
                "uuid": getattr(edge, 'uuid_', None) or getattr(edge, 'uuid', ''),
                "name": edge.name or "",
                "fact": edge.fact or "",
                "source_node_uuid": edge.source_node_uuid,
                "target_node_uuid": edge.target_node_uuid,
                "attributes": edge.attributes or {},
            })

        logger.info(f"共获取 {len(edges_data)} 条边")
        return edges_data

# ... 文件较长，已截断。总行数：437
```

### backend/app/services/zep_graph_memory_updater.py

```python
"""
Zep图谱记忆更新服务
将模拟中的Agent活动动态更新到Zep图谱中
"""

import os
import time
import threading
import json
from typing import Dict, Any, List, Optional, Callable
from dataclasses import dataclass
from datetime import datetime
from queue import Queue, Empty

from zep_cloud.client import Zep

from ..config import Config
from ..utils.logger import get_logger
from ..utils.locale import get_locale, set_locale

logger = get_logger('mirofish.zep_graph_memory_updater')


@dataclass
class AgentActivity:
    """Agent活动记录"""
    platform: str           # twitter / reddit
    agent_id: int
    agent_name: str
    action_type: str        # CREATE_POST, LIKE_POST, etc.
    action_args: Dict[str, Any]
    round_num: int
    timestamp: str
    
    def to_episode_text(self) -> str:
        """
        将活动转换为可以发送给Zep的文本描述
        
        采用自然语言描述格式，让Zep能够从中提取实体和关系
        不添加模拟相关的前缀，避免误导图谱更新
        """
        # 根据不同的动作类型生成不同的描述
        action_descriptions = {
            "CREATE_POST": self._describe_create_post,
            "LIKE_POST": self._describe_like_post,
            "DISLIKE_POST": self._describe_dislike_post,
            "REPOST": self._describe_repost,
            "QUOTE_POST": self._describe_quote_post,
            "FOLLOW": self._describe_follow,
            "CREATE_COMMENT": self._describe_create_comment,
            "LIKE_COMMENT": self._describe_like_comment,
            "DISLIKE_COMMENT": self._describe_dislike_comment,
            "SEARCH_POSTS": self._describe_search,
            "SEARCH_USER": self._describe_search_user,
            "MUTE": self._describe_mute,
        }
        
        describe_func = action_descriptions.get(self.action_type, self._describe_generic)
        description = describe_func()
        
        # 直接返回 "agent名称: 活动描述" 格式，不添加模拟前缀
        return f"{self.agent_name}: {description}"
    
    def _describe_create_post(self) -> str:
        content = self.action_args.get("content", "")
        if content:
            return f"发布了一条帖子：「{content}」"
        return "发布了一条帖子"
    
    def _describe_like_post(self) -> str:
        """点赞帖子 - 包含帖子原文和作者信息"""
        post_content = self.action_args.get("post_content", "")
        post_author = self.action_args.get("post_author_name", "")
        
        if post_content and post_author:
            return f"点赞了{post_author}的帖子：「{post_content}」"
        elif post_content:
            return f"点赞了一条帖子：「{post_content}」"
        elif post_author:
            return f"点赞了{post_author}的一条帖子"
        return "点赞了一条帖子"
    
    def _describe_dislike_post(self) -> str:
        """踩帖子 - 包含帖子原文和作者信息"""
        post_content = self.action_args.get("post_content", "")
        post_author = self.action_args.get("post_author_name", "")
        
        if post_content and post_author:
            return f"踩了{post_author}的帖子：「{post_content}」"
        elif post_content:
            return f"踩了一条帖子：「{post_content}」"
        elif post_author:
            return f"踩了{post_author}的一条帖子"
        return "踩了一条帖子"
    
    def _describe_repost(self) -> str:
        """转发帖子 - 包含原帖内容和作者信息"""
        original_content = self.action_args.get("original_content", "")
        original_author = self.action_args.get("original_author_name", "")
        
        if original_content and original_author:
            return f"转发了{original_author}的帖子：「{original_content}」"
        elif original_content:
            return f"转发了一条帖子：「{original_content}」"
        elif original_author:
            return f"转发了{original_author}的一条帖子"
        return "转发了一条帖子"
    
    def _describe_quote_post(self) -> str:
        """引用帖子 - 包含原帖内容、作者信息和引用评论"""
        original_content = self.action_args.get("original_content", "")
        original_author = self.action_args.get("original_author_name", "")
        quote_content = self.action_args.get("quote_content", "") or self.action_args.get("content", "")
        
        base = ""
        if original_content and original_author:
            base = f"引用了{original_author}的帖子「{original_content}」"
        elif original_content:
            base = f"引用了一条帖子「{original_content}」"
        elif original_author:
            base = f"引用了{original_author}的一条帖子"
        else:
            base = "引用了一条帖子"
        
        if quote_content:
            base += f"，并评论道：「{quote_content}」"
        return base
    
    def _describe_follow(self) -> str:
        """关注用户 - 包含被关注用户的名称"""
        target_user_name = self.action_args.get("target_user_name", "")
        
        if target_user_name:
            return f"关注了用户「{target_user_name}」"
        return "关注了一个用户"
    
    def _describe_create_comment(self) -> str:
        """发表评论 - 包含评论内容和所评论的帖子信息"""
        content = self.action_args.get("content", "")
        post_content = self.action_args.get("post_content", "")
        post_author = self.action_args.get("post_author_name", "")
        
        if content:
            if post_content and post_author:
                return f"在{post_author}的帖子「{post_content}」下评论道：「{content}」"
            elif post_content:
                return f"在帖子「{post_content}」下评论道：「{content}」"
            elif post_author:
                return f"在{post_author}的帖子下评论道：「{content}」"
            return f"评论道：「{content}」"
        return "发表了评论"
    
    def _describe_like_comment(self) -> str:
        """点赞评论 - 包含评论内容和作者信息"""
        comment_content = self.action_args.get("comment_content", "")
        comment_author = self.action_args.get("comment_author_name", "")
        
        if comment_content and comment_author:
            return f"点赞了{comment_author}的评论：「{comment_content}」"
        elif comment_content:
            return f"点赞了一条评论：「{comment_content}」"
        elif comment_author:
            return f"点赞了{comment_author}的一条评论"
        return "点赞了一条评论"
    
    def _describe_dislike_comment(self) -> str:
        """踩评论 - 包含评论内容和作者信息"""
        comment_content = self.action_args.get("comment_content", "")
        comment_author = self.action_args.get("comment_author_name", "")
        
        if comment_content and comment_author:
            return f"踩了{comment_author}的评论：「{comment_content}」"
        elif comment_content:
            return f"踩了一条评论：「{comment_content}」"
        elif comment_author:
            return f"踩了{comment_author}的一条评论"
        return "踩了一条评论"
    
    def _describe_search(self) -> str:
        """搜索帖子 - 包含搜索关键词"""

# ... 文件较长，已截断。总行数：554
```

### backend/app/services/zep_tools.py

```python
"""
Zep检索工具服务
封装图谱搜索、节点读取、边查询等工具，供Report Agent使用

核心检索工具（优化后）：
1. InsightForge（深度洞察检索）- 最强大的混合检索，自动生成子问题并多维度检索
2. PanoramaSearch（广度搜索）- 获取全貌，包括过期内容
3. QuickSearch（简单搜索）- 快速检索
"""

import time
import json
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field

from zep_cloud.client import Zep

from ..config import Config
from ..utils.logger import get_logger
from ..utils.llm_client import LLMClient
from ..utils.locale import get_locale, t
from ..utils.zep_paging import fetch_all_nodes, fetch_all_edges

logger = get_logger('mirofish.zep_tools')


@dataclass
class SearchResult:
    """搜索结果"""
    facts: List[str]
    edges: List[Dict[str, Any]]
    nodes: List[Dict[str, Any]]
    query: str
    total_count: int
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "facts": self.facts,
            "edges": self.edges,
            "nodes": self.nodes,
            "query": self.query,
            "total_count": self.total_count
        }
    
    def to_text(self) -> str:
        """转换为文本格式，供LLM理解"""
        text_parts = [f"搜索查询: {self.query}", f"找到 {self.total_count} 条相关信息"]
        
        if self.facts:
            text_parts.append("\n### 相关事实:")
            for i, fact in enumerate(self.facts, 1):
                text_parts.append(f"{i}. {fact}")
        
        return "\n".join(text_parts)


@dataclass
class NodeInfo:
    """节点信息"""
    uuid: str
    name: str
    labels: List[str]
    summary: str
    attributes: Dict[str, Any]
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "uuid": self.uuid,
            "name": self.name,
            "labels": self.labels,
            "summary": self.summary,
            "attributes": self.attributes
        }
    
    def to_text(self) -> str:
        """转换为文本格式"""
        entity_type = next((l for l in self.labels if l not in ["Entity", "Node"]), "未知类型")
        return f"实体: {self.name} (类型: {entity_type})\n摘要: {self.summary}"


@dataclass
class EdgeInfo:
    """边信息"""
    uuid: str
    name: str
    fact: str
    source_node_uuid: str
    target_node_uuid: str
    source_node_name: Optional[str] = None
    target_node_name: Optional[str] = None
    # 时间信息
    created_at: Optional[str] = None
    valid_at: Optional[str] = None
    invalid_at: Optional[str] = None
    expired_at: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "uuid": self.uuid,
            "name": self.name,
            "fact": self.fact,
            "source_node_uuid": self.source_node_uuid,
            "target_node_uuid": self.target_node_uuid,
            "source_node_name": self.source_node_name,
            "target_node_name": self.target_node_name,
            "created_at": self.created_at,
            "valid_at": self.valid_at,
            "invalid_at": self.invalid_at,
            "expired_at": self.expired_at
        }
    
    def to_text(self, include_temporal: bool = False) -> str:
        """转换为文本格式"""
        source = self.source_node_name or self.source_node_uuid[:8]
        target = self.target_node_name or self.target_node_uuid[:8]
        base_text = f"关系: {source} --[{self.name}]--> {target}\n事实: {self.fact}"
        
        if include_temporal:
            valid_at = self.valid_at or "未知"
            invalid_at = self.invalid_at or "至今"
            base_text += f"\n时效: {valid_at} - {invalid_at}"
            if self.expired_at:
                base_text += f" (已过期: {self.expired_at})"
        
        return base_text
    
    @property
    def is_expired(self) -> bool:
        """是否已过期"""
        return self.expired_at is not None
    
    @property
    def is_invalid(self) -> bool:
        """是否已失效"""
        return self.invalid_at is not None


@dataclass
class InsightForgeResult:
    """
    深度洞察检索结果 (InsightForge)
    包含多个子问题的检索结果，以及综合分析
    """
    query: str
    simulation_requirement: str
    sub_queries: List[str]
    
    # 各维度检索结果
    semantic_facts: List[str] = field(default_factory=list)  # 语义搜索结果
    entity_insights: List[Dict[str, Any]] = field(default_factory=list)  # 实体洞察
    relationship_chains: List[str] = field(default_factory=list)  # 关系链
    
    # 统计信息
    total_facts: int = 0
    total_entities: int = 0
    total_relationships: int = 0
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "query": self.query,
            "simulation_requirement": self.simulation_requirement,
            "sub_queries": self.sub_queries,
            "semantic_facts": self.semantic_facts,
            "entity_insights": self.entity_insights,
            "relationship_chains": self.relationship_chains,
            "total_facts": self.total_facts,
            "total_entities": self.total_entities,
            "total_relationships": self.total_relationships
        }
    
    def to_text(self) -> str:
        """转换为详细的文本格式，供LLM理解"""
        text_parts = [
            f"## 未来预测深度分析",
            f"分析问题: {self.query}",
            f"预测场景: {self.simulation_requirement}",
            f"\n### 预测数据统计",
            f"- 相关预测事实: {self.total_facts}条",
            f"- 涉及实体: {self.total_entities}个",
            f"- 关系链: {self.total_relationships}条"

# ... 文件较长，已截断。总行数：1736
```

### backend/app/utils/zep_paging.py

```python
"""Zep Graph 分页读取工具。

Zep 的 node/edge 列表接口使用 UUID cursor 分页，
本模块封装自动翻页逻辑（含单页重试），对调用方透明地返回完整列表。
"""

from __future__ import annotations

import time
from collections.abc import Callable
from typing import Any

from zep_cloud import InternalServerError
from zep_cloud.client import Zep

from .logger import get_logger

logger = get_logger('mirofish.zep_paging')

_DEFAULT_PAGE_SIZE = 100
_MAX_NODES = 2000
_DEFAULT_MAX_RETRIES = 3
_DEFAULT_RETRY_DELAY = 2.0  # seconds, doubles each retry


def _fetch_page_with_retry(
    api_call: Callable[..., list[Any]],
    *args: Any,
    max_retries: int = _DEFAULT_MAX_RETRIES,
    retry_delay: float = _DEFAULT_RETRY_DELAY,
    page_description: str = "page",
    **kwargs: Any,
) -> list[Any]:
    """单页请求，失败时指数退避重试。仅重试网络/IO类瞬态错误。"""
    if max_retries < 1:
        raise ValueError("max_retries must be >= 1")

    last_exception: Exception | None = None
    delay = retry_delay

    for attempt in range(max_retries):
        try:
            return api_call(*args, **kwargs)
        except (ConnectionError, TimeoutError, OSError, InternalServerError) as e:
            last_exception = e
            if attempt < max_retries - 1:
                logger.warning(
                    f"Zep {page_description} attempt {attempt + 1} failed: {str(e)[:100]}, retrying in {delay:.1f}s..."
                )
                time.sleep(delay)
                delay *= 2
            else:
                logger.error(f"Zep {page_description} failed after {max_retries} attempts: {str(e)}")

    assert last_exception is not None
    raise last_exception


def fetch_all_nodes(
    client: Zep,
    graph_id: str,
    page_size: int = _DEFAULT_PAGE_SIZE,
    max_items: int = _MAX_NODES,
    max_retries: int = _DEFAULT_MAX_RETRIES,
    retry_delay: float = _DEFAULT_RETRY_DELAY,
) -> list[Any]:
    """分页获取图谱节点，最多返回 max_items 条（默认 2000）。每页请求自带重试。"""
    all_nodes: list[Any] = []
    cursor: str | None = None
    page_num = 0

    while True:
        kwargs: dict[str, Any] = {"limit": page_size}
        if cursor is not None:
            kwargs["uuid_cursor"] = cursor

        page_num += 1
        batch = _fetch_page_with_retry(
            client.graph.node.get_by_graph_id,
            graph_id,
            max_retries=max_retries,
            retry_delay=retry_delay,
            page_description=f"fetch nodes page {page_num} (graph={graph_id})",
            **kwargs,
        )
        if not batch:
            break

        all_nodes.extend(batch)
        if len(all_nodes) >= max_items:
            all_nodes = all_nodes[:max_items]
            logger.warning(f"Node count reached limit ({max_items}), stopping pagination for graph {graph_id}")
            break
        if len(batch) < page_size:
            break

        cursor = getattr(batch[-1], "uuid_", None) or getattr(batch[-1], "uuid", None)
        if cursor is None:
            logger.warning(f"Node missing uuid field, stopping pagination at {len(all_nodes)} nodes")
            break

    return all_nodes


def fetch_all_edges(
    client: Zep,
    graph_id: str,
    page_size: int = _DEFAULT_PAGE_SIZE,
    max_retries: int = _DEFAULT_MAX_RETRIES,
    retry_delay: float = _DEFAULT_RETRY_DELAY,
) -> list[Any]:
    """分页获取图谱所有边，返回完整列表。每页请求自带重试。"""
    all_edges: list[Any] = []
    cursor: str | None = None
    page_num = 0

    while True:
        kwargs: dict[str, Any] = {"limit": page_size}
        if cursor is not None:
            kwargs["uuid_cursor"] = cursor

        page_num += 1
        batch = _fetch_page_with_retry(
            client.graph.edge.get_by_graph_id,
            graph_id,
            max_retries=max_retries,
            retry_delay=retry_delay,
            page_description=f"fetch edges page {page_num} (graph={graph_id})",
            **kwargs,
        )
        if not batch:
            break

        all_edges.extend(batch)
        if len(batch) < page_size:
            break

        cursor = getattr(batch[-1], "uuid_", None) or getattr(batch[-1], "uuid", None)
        if cursor is None:
            logger.warning(f"Edge missing uuid field, stopping pagination at {len(all_edges)} edges")
            break

    return all_edges
```

### frontend/src/api/graph.js

```typescript
import service, { requestWithRetry } from './index'

/**
 * 生成本体（上传文档和模拟需求）
 * @param {Object} data - 包含files, simulation_requirement, project_name等
 * @returns {Promise}
 */
export function generateOntology(formData) {
  return requestWithRetry(() => 
    service({
      url: '/api/graph/ontology/generate',
      method: 'post',
      data: formData,
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
  )
}

/**
 * 构建图谱
 * @param {Object} data - 包含project_id, graph_name等
 * @returns {Promise}
 */
export function buildGraph(data) {
  return requestWithRetry(() =>
    service({
      url: '/api/graph/build',
      method: 'post',
      data
    })
  )
}

/**
 * 查询任务状态
 * @param {String} taskId - 任务ID
 * @returns {Promise}
 */
export function getTaskStatus(taskId) {
  return service({
    url: `/api/graph/task/${taskId}`,
    method: 'get'
  })
}

/**
 * 获取图谱数据
 * @param {String} graphId - 图谱ID
 * @returns {Promise}
 */
export function getGraphData(graphId) {
  return service({
    url: `/api/graph/data/${graphId}`,
    method: 'get'
  })
}

/**
 * 获取项目信息
 * @param {String} projectId - 项目ID
 * @returns {Promise}
 */
export function getProject(projectId) {
  return service({
    url: `/api/graph/project/${projectId}`,
    method: 'get'
  })
}
```

### frontend/src/api/report.js

```typescript
import service, { requestWithRetry } from './index'

/**
 * 开始报告生成
 * @param {Object} data - { simulation_id, force_regenerate? }
 */
export const generateReport = (data) => {
  return requestWithRetry(() => service.post('/api/report/generate', data), 3, 1000)
}

/**
 * 获取报告生成状态
 * @param {string} reportId
 */
export const getReportStatus = (reportId) => {
  return service.get(`/api/report/generate/status`, { params: { report_id: reportId } })
}

/**
 * 获取 Agent 日志（增量）
 * @param {string} reportId
 * @param {number} fromLine - 从第几行开始获取
 */
export const getAgentLog = (reportId, fromLine = 0) => {
  return service.get(`/api/report/${reportId}/agent-log`, { params: { from_line: fromLine } })
}

/**
 * 获取控制台日志（增量）
 * @param {string} reportId
 * @param {number} fromLine - 从第几行开始获取
 */
export const getConsoleLog = (reportId, fromLine = 0) => {
  return service.get(`/api/report/${reportId}/console-log`, { params: { from_line: fromLine } })
}

/**
 * 获取报告详情
 * @param {string} reportId
 */
export const getReport = (reportId) => {
  return service.get(`/api/report/${reportId}`)
}

/**
 * 与 Report Agent 对话
 * @param {Object} data - { simulation_id, message, chat_history? }
 */
export const chatWithReport = (data) => {
  return requestWithRetry(() => service.post('/api/report/chat', data), 3, 1000)
}
```

### frontend/src/api/simulation.js

```typescript
import service, { requestWithRetry } from './index'

/**
 * 创建模拟
 * @param {Object} data - { project_id, graph_id?, enable_twitter?, enable_reddit? }
 */
export const createSimulation = (data) => {
  return requestWithRetry(() => service.post('/api/simulation/create', data), 3, 1000)
}

/**
 * 准备模拟环境（异步任务）
 * @param {Object} data - { simulation_id, entity_types?, use_llm_for_profiles?, parallel_profile_count?, force_regenerate? }
 */
export const prepareSimulation = (data) => {
  return requestWithRetry(() => service.post('/api/simulation/prepare', data), 3, 1000)
}

/**
 * 查询准备任务进度
 * @param {Object} data - { task_id?, simulation_id? }
 */
export const getPrepareStatus = (data) => {
  return service.post('/api/simulation/prepare/status', data)
}

/**
 * 获取模拟状态
 * @param {string} simulationId
 */
export const getSimulation = (simulationId) => {
  return service.get(`/api/simulation/${simulationId}`)
}

/**
 * 获取模拟的 Agent Profiles
 * @param {string} simulationId
 * @param {string} platform - 'reddit' | 'twitter'
 */
export const getSimulationProfiles = (simulationId, platform = 'reddit') => {
  return service.get(`/api/simulation/${simulationId}/profiles`, { params: { platform } })
}

/**
 * 实时获取生成中的 Agent Profiles
 * @param {string} simulationId
 * @param {string} platform - 'reddit' | 'twitter'
 */
export const getSimulationProfilesRealtime = (simulationId, platform = 'reddit') => {
  return service.get(`/api/simulation/${simulationId}/profiles/realtime`, { params: { platform } })
}

/**
 * 获取模拟配置
 * @param {string} simulationId
 */
export const getSimulationConfig = (simulationId) => {
  return service.get(`/api/simulation/${simulationId}/config`)
}

/**
 * 实时获取生成中的模拟配置
 * @param {string} simulationId
 * @returns {Promise} 返回配置信息，包含元数据和配置内容
 */
export const getSimulationConfigRealtime = (simulationId) => {
  return service.get(`/api/simulation/${simulationId}/config/realtime`)
}

/**
 * 列出所有模拟
 * @param {string} projectId - 可选，按项目ID过滤
 */
export const listSimulations = (projectId) => {
  const params = projectId ? { project_id: projectId } : {}
  return service.get('/api/simulation/list', { params })
}

/**
 * 启动模拟
 * @param {Object} data - { simulation_id, platform?, max_rounds?, enable_graph_memory_update? }
 */
export const startSimulation = (data) => {
  return requestWithRetry(() => service.post('/api/simulation/start', data), 3, 1000)
}

/**
 * 停止模拟
 * @param {Object} data - { simulation_id }
 */
export const stopSimulation = (data) => {
  return service.post('/api/simulation/stop', data)
}

/**
 * 获取模拟运行实时状态
 * @param {string} simulationId
 */
export const getRunStatus = (simulationId) => {
  return service.get(`/api/simulation/${simulationId}/run-status`)
}

/**
 * 获取模拟运行详细状态（包含最近动作）
 * @param {string} simulationId
 */
export const getRunStatusDetail = (simulationId) => {
  return service.get(`/api/simulation/${simulationId}/run-status/detail`)
}

/**
 * 获取模拟中的帖子
 * @param {string} simulationId
 * @param {string} platform - 'reddit' | 'twitter'
 * @param {number} limit - 返回数量
 * @param {number} offset - 偏移量
 */
export const getSimulationPosts = (simulationId, platform = 'reddit', limit = 50, offset = 0) => {
  return service.get(`/api/simulation/${simulationId}/posts`, {
    params: { platform, limit, offset }
  })
}

/**
 * 获取模拟时间线（按轮次汇总）
 * @param {string} simulationId
 * @param {number} startRound - 起始轮次
 * @param {number} endRound - 结束轮次
 */
export const getSimulationTimeline = (simulationId, startRound = 0, endRound = null) => {
  const params = { start_round: startRound }
  if (endRound !== null) {
    params.end_round = endRound
  }
  return service.get(`/api/simulation/${simulationId}/timeline`, { params })
}

/**
 * 获取Agent统计信息
 * @param {string} simulationId
 */
export const getAgentStats = (simulationId) => {
  return service.get(`/api/simulation/${simulationId}/agent-stats`)
}

/**
 * 获取模拟动作历史
 * @param {string} simulationId
 * @param {Object} params - { limit, offset, platform, agent_id, round_num }
 */
export const getSimulationActions = (simulationId, params = {}) => {
  return service.get(`/api/simulation/${simulationId}/actions`, { params })
}

/**
 * 关闭模拟环境（优雅退出）
 * @param {Object} data - { simulation_id, timeout? }
 */
export const closeSimulationEnv = (data) => {
  return service.post('/api/simulation/close-env', data)
}

/**
 * 获取模拟环境状态
 * @param {Object} data - { simulation_id }
 */
export const getEnvStatus = (data) => {
  return service.post('/api/simulation/env-status', data)
}

/**
 * 批量采访 Agent
 * @param {Object} data - { simulation_id, interviews: [{ agent_id, prompt }] }
 */
export const interviewAgents = (data) => {
  return requestWithRetry(() => service.post('/api/simulation/interview/batch', data), 3, 1000)
}

/**
 * 获取历史模拟列表（带项目详情）

# ... 文件较长，已截断。总行数：187
```

## 13. README 中可能的核心流程摘录

```text
9:<em>A Simple and Universal Swarm Intelligence Engine, Predicting Anything</em>
16:[![Docker](https://img.shields.io/badge/Docker-Build-2496ED?style=flat-square&logo=docker&logoColor=white)](https://hub.docker.com/)
17:[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/666ghj/MiroFish)
68:### 1. Wuhan University Public Opinion Simulation + MiroFish Project Introduction
73:Click the image to watch the complete demo video for prediction using BettaFish-generated "Wuhan University Public Opinion Report"
76:### 2. Dream of the Red Chamber Lost Ending Simulation
86:## 🔄 Workflow
88:1. **Graph Building**: Seed extraction & Individual/collective memory injection & GraphRAG construction
89:2. **Environment Setup**: Entity relationship extraction & Persona generation & Agent configuration injection
90:3. **Simulation**: Dual-platform parallel simulation & Auto-parse prediction requirements & Dynamic temporal memory updates
91:4. **Report Generation**: ReportAgent with rich toolset for deep interaction with post-simulation environment
92:5. **Deep Interaction**: Chat with any agent in the simulated world & Interact with ReportAgent
94:## 🚀 Quick Start
100:| Tool | Version | Description | Check Installation |
106:#### 1. Configure Environment Variables
115:**Required Environment Variables:**
125:# Zep Cloud Configuration
130:#### 2. Install Dependencies
140:# Install Node dependencies (root + frontend)
143:# Install Python dependencies (backend, auto-creates virtual environment)
165:### Option 2: Docker Deployment
193:MiroFish's simulation engine is powered by **[OASIS (Open Agent Social Interaction Simulations)](https://github.com/camel-ai/oasis)**, We sincerely thank the CAMEL-AI team for their open-source contributions!
```

