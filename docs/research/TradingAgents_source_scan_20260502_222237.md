# TradingAgents 源码初步扫描报告

生成时间：2026-05-02 22:22:37
源码路径：/Users/balwyn/Downloads/TradingAgents-main

## 1. Git 信息

未检测到 .git 目录，可能是 GitHub 下载的 zip 解压包。

## 2. 顶层目录

```text
total 1512
drwxrwxr-x@ 22 balwyn  staff     704  2 May 22:19 .
drwx------@ 56 balwyn  staff    1792  2 May 22:18 ..
-rw-rw-r--@  1 balwyn  staff     133  2 May 03:23 .dockerignore
-rw-r--r--@  1 balwyn  staff   14340  2 May 22:19 .DS_Store
-rw-rw-r--@  1 balwyn  staff     203  2 May 03:23 .env.enterprise.example
-rw-rw-r--@  1 balwyn  staff     174  2 May 03:23 .env.example
-rw-rw-r--@  1 balwyn  staff    4586  2 May 03:23 .gitignore
drwxrwxr-x@ 10 balwyn  staff     320  2 May 03:23 assets
-rw-rw-r--@  1 balwyn  staff   13125  2 May 03:23 CHANGELOG.md
drwxrwxr-x@ 10 balwyn  staff     320  2 May 03:23 cli
-rw-rw-r--@  1 balwyn  staff     611  2 May 03:23 docker-compose.yml
-rw-rw-r--@  1 balwyn  staff     530  2 May 03:23 Dockerfile
-rw-rw-r--@  1 balwyn  staff   11357  2 May 03:23 LICENSE
-rw-rw-r--@  1 balwyn  staff    1158  2 May 03:23 main.py
-rw-rw-r--@  1 balwyn  staff    1304  2 May 03:23 pyproject.toml
-rw-rw-r--@  1 balwyn  staff   13439  2 May 03:23 README.md
-rw-rw-r--@  1 balwyn  staff       2  2 May 03:23 requirements.txt
drwxrwxr-x@  3 balwyn  staff      96  2 May 03:23 scripts
-rw-rw-r--@  1 balwyn  staff     637  2 May 03:23 test.py
drwxrwxr-x@ 12 balwyn  staff     384  2 May 03:23 tests
drwxrwxr-x@  8 balwyn  staff     256  2 May 03:23 tradingagents
-rw-rw-r--@  1 balwyn  staff  666506  2 May 03:23 uv.lock
```

## 3. 目录结构，最多 3 层

```text
.
./assets
./assets/cli
./cli
./cli/static
./scripts
./tests
./tradingagents
./tradingagents/agents
./tradingagents/agents/analysts
./tradingagents/agents/managers
./tradingagents/agents/researchers
./tradingagents/agents/risk_mgmt
./tradingagents/agents/trader
./tradingagents/agents/utils
./tradingagents/dataflows
./tradingagents/graph
./tradingagents/llm_clients
```

## 4. 主要文件清单，最多 200 个

```text
./.dockerignore
./.DS_Store
./.env.enterprise.example
./.env.example
./.gitignore
./assets/analyst.png
./assets/cli/cli_init.png
./assets/cli/cli_news.png
./assets/cli/cli_technical.png
./assets/cli/cli_transaction.png
./assets/researcher.png
./assets/risk.png
./assets/schema.png
./assets/TauricResearch.png
./assets/trader.png
./assets/wechat.png
./CHANGELOG.md
./cli/__init__.py
./cli/announcements.py
./cli/config.py
./cli/main.py
./cli/models.py
./cli/static/welcome.txt
./cli/stats_handler.py
./cli/utils.py
./docker-compose.yml
./Dockerfile
./LICENSE
./main.py
./pyproject.toml
./README.md
./requirements.txt
./scripts/smoke_structured_output.py
./test.py
./tests/conftest.py
./tests/test_checkpoint_resume.py
./tests/test_deepseek_reasoning.py
./tests/test_google_api_key.py
./tests/test_memory_log.py
./tests/test_model_validation.py
./tests/test_safe_ticker_component.py
./tests/test_signal_processing.py
./tests/test_structured_agents.py
./tests/test_ticker_symbol_handling.py
./tradingagents/__init__.py
./tradingagents/agents/__init__.py
./tradingagents/agents/analysts/fundamentals_analyst.py
./tradingagents/agents/analysts/market_analyst.py
./tradingagents/agents/analysts/news_analyst.py
./tradingagents/agents/analysts/social_media_analyst.py
./tradingagents/agents/managers/portfolio_manager.py
./tradingagents/agents/managers/research_manager.py
./tradingagents/agents/researchers/bear_researcher.py
./tradingagents/agents/researchers/bull_researcher.py
./tradingagents/agents/risk_mgmt/aggressive_debator.py
./tradingagents/agents/risk_mgmt/conservative_debator.py
./tradingagents/agents/risk_mgmt/neutral_debator.py
./tradingagents/agents/schemas.py
./tradingagents/agents/trader/trader.py
./tradingagents/agents/utils/agent_states.py
./tradingagents/agents/utils/agent_utils.py
./tradingagents/agents/utils/core_stock_tools.py
./tradingagents/agents/utils/fundamental_data_tools.py
./tradingagents/agents/utils/memory.py
./tradingagents/agents/utils/news_data_tools.py
./tradingagents/agents/utils/rating.py
./tradingagents/agents/utils/structured.py
./tradingagents/agents/utils/technical_indicators_tools.py
./tradingagents/dataflows/__init__.py
./tradingagents/dataflows/alpha_vantage_common.py
./tradingagents/dataflows/alpha_vantage_fundamentals.py
./tradingagents/dataflows/alpha_vantage_indicator.py
./tradingagents/dataflows/alpha_vantage_news.py
./tradingagents/dataflows/alpha_vantage_stock.py
./tradingagents/dataflows/alpha_vantage.py
./tradingagents/dataflows/config.py
./tradingagents/dataflows/interface.py
./tradingagents/dataflows/stockstats_utils.py
./tradingagents/dataflows/utils.py
./tradingagents/dataflows/y_finance.py
./tradingagents/dataflows/yfinance_news.py
./tradingagents/default_config.py
./tradingagents/graph/__init__.py
./tradingagents/graph/checkpointer.py
./tradingagents/graph/conditional_logic.py
./tradingagents/graph/propagation.py
./tradingagents/graph/reflection.py
./tradingagents/graph/setup.py
./tradingagents/graph/signal_processing.py
./tradingagents/graph/trading_graph.py
./tradingagents/llm_clients/__init__.py
./tradingagents/llm_clients/anthropic_client.py
./tradingagents/llm_clients/azure_client.py
./tradingagents/llm_clients/base_client.py
./tradingagents/llm_clients/factory.py
./tradingagents/llm_clients/google_client.py
./tradingagents/llm_clients/model_catalog.py
./tradingagents/llm_clients/openai_client.py
./tradingagents/llm_clients/TODO.md
./tradingagents/llm_clients/validators.py
./uv.lock
```

## 5. 文件类型统计

```text
.py: 75
.png: 11
[no_ext]: 5
.md: 3
.txt: 2
.example: 2
.lock: 1
.toml: 1
.yml: 1
```

## 6. 关键项目文件预览


### README.md

```text
<p align="center">
  <img src="assets/TauricResearch.png" style="width: 60%; height: auto;">
</p>

<div align="center" style="line-height: 1;">
  <a href="https://arxiv.org/abs/2412.20138" target="_blank"><img alt="arXiv" src="https://img.shields.io/badge/arXiv-2412.20138-B31B1B?logo=arxiv"/></a>
  <a href="https://discord.com/invite/hk9PGKShPK" target="_blank"><img alt="Discord" src="https://img.shields.io/badge/Discord-TradingResearch-7289da?logo=discord&logoColor=white&color=7289da"/></a>
  <a href="./assets/wechat.png" target="_blank"><img alt="WeChat" src="https://img.shields.io/badge/WeChat-TauricResearch-brightgreen?logo=wechat&logoColor=white"/></a>
  <a href="https://x.com/TauricResearch" target="_blank"><img alt="X Follow" src="https://img.shields.io/badge/X-TauricResearch-white?logo=x&logoColor=white"/></a>
  <br>
  <a href="https://github.com/TauricResearch/" target="_blank"><img alt="Community" src="https://img.shields.io/badge/Join_GitHub_Community-TauricResearch-14C290?logo=discourse"/></a>
</div>

<div align="center">
  <!-- Keep these links. Translations will automatically update with the README. -->
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=de">Deutsch</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=es">Español</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=fr">français</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=ja">日本語</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=ko">한국어</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=pt">Português</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=ru">Русский</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=zh">中文</a>
</div>

---

# TradingAgents: Multi-Agents LLM Financial Trading Framework

## News
- [2026-04] **TradingAgents v0.2.4** released with structured-output agents (Research Manager, Trader, Portfolio Manager), LangGraph checkpoint resume, persistent decision log, DeepSeek/Qwen/GLM/Azure provider support, Docker, and a Windows UTF-8 encoding fix. See [CHANGELOG.md](CHANGELOG.md) for the full list.
- [2026-03] **TradingAgents v0.2.3** released with multi-language support, GPT-5.4 family models, unified model catalog, backtesting date fidelity, and proxy support.
- [2026-03] **TradingAgents v0.2.2** released with GPT-5.4/Gemini 3.1/Claude 4.6 model coverage, five-tier rating scale, OpenAI Responses API, Anthropic effort control, and cross-platform stability.
- [2026-02] **TradingAgents v0.2.0** released with multi-provider LLM support (GPT-5.x, Gemini 3.x, Claude 4.x, Grok 4.x) and improved system architecture.
- [2026-01] **Trading-R1** [Technical Report](https://arxiv.org/abs/2509.11420) released, with [Terminal](https://github.com/TauricResearch/Trading-R1) expected to land soon.

<div align="center">
<a href="https://www.star-history.com/#TauricResearch/TradingAgents&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=TauricResearch/TradingAgents&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=TauricResearch/TradingAgents&type=Date" />
   <img alt="TradingAgents Star History" src="https://api.star-history.com/svg?repos=TauricResearch/TradingAgents&type=Date" style="width: 80%; height: auto;" />
 </picture>
</a>
</div>

> 🎉 **TradingAgents** officially released! We have received numerous inquiries about the work, and we would like to express our thanks for the enthusiasm in our community.
>
> So we decided to fully open-source the framework. Looking forward to building impactful projects with you!

<div align="center">

🚀 [TradingAgents](#tradingagents-framework) | ⚡ [Installation & CLI](#installation-and-cli) | 🎬 [Demo](https://www.youtube.com/watch?v=90gr5lwjIho) | 📦 [Package Usage](#tradingagents-package) | 🤝 [Contributing](#contributing) | 📄 [Citation](#citation)

</div>

## TradingAgents Framework

TradingAgents is a multi-agent trading framework that mirrors the dynamics of real-world trading firms. By deploying specialized LLM-powered agents: from fundamental analysts, sentiment experts, and technical analysts, to trader, risk management team, the platform collaboratively evaluates market conditions and informs trading decisions. Moreover, these agents engage in dynamic discussions to pinpoint the optimal strategy.

<p align="center">
  <img src="assets/schema.png" style="width: 100%; height: auto;">
</p>

> TradingAgents framework is designed for research purposes. Trading performance may vary based on many factors, including the chosen backbone language models, model temperature, trading periods, the quality of data, and other non-deterministic factors. [It is not intended as financial, investment, or trading advice.](https://tauric.ai/disclaimer/)

Our framework decomposes complex trading tasks into specialized roles. This ensures the system achieves a robust, scalable approach to market analysis and decision-making.

### Analyst Team
- Fundamentals Analyst: Evaluates company financials and performance metrics, identifying intrinsic values and potential red flags.
- Sentiment Analyst: Analyzes social media and public sentiment using sentiment scoring algorithms to gauge short-term market mood.
- News Analyst: Monitors global news and macroeconomic indicators, interpreting the impact of events on market conditions.
- Technical Analyst: Utilizes technical indicators (like MACD and RSI) to detect trading patterns and forecast price movements.

<p align="center">
  <img src="assets/analyst.png" width="100%" style="display: inline-block; margin: 0 2%;">
</p>

### Researcher Team
- Comprises both bullish and bearish researchers who critically assess the insights provided by the Analyst Team. Through structured debates, they balance potential gains against inherent risks.

<p align="center">
  <img src="assets/researcher.png" width="70%" style="display: inline-block; margin: 0 2%;">
</p>

### Trader Agent
- Composes reports from the analysts and researchers to make informed trading decisions. It determines the timing and magnitude of trades based on comprehensive market insights.

<p align="center">
  <img src="assets/trader.png" width="70%" style="display: inline-block; margin: 0 2%;">
</p>

### Risk Management and Portfolio Manager
- Continuously evaluates portfolio risk by assessing market volatility, liquidity, and other risk factors. The risk management team evaluates and adjusts trading strategies, providing assessment reports to the Portfolio Manager for final decision.
- The Portfolio Manager approves/rejects the transaction proposal. If approved, the order will be sent to the simulated exchange and executed.

<p align="center">
  <img src="assets/risk.png" width="70%" style="display: inline-block; margin: 0 2%;">
</p>

## Installation and CLI

### Installation

Clone TradingAgents:
```bash
git clone https://github.com/TauricResearch/TradingAgents.git
cd TradingAgents
```

Create a virtual environment in any of your favorite environment managers:
```bash
conda create -n tradingagents python=3.13
conda activate tradingagents
```

Install the package and its dependencies:
```bash
pip install .
```

### Docker

Alternatively, run with Docker:
```bash
cp .env.example .env  # add your API keys
docker compose run --rm tradingagents
```

For local models with Ollama:
```bash
docker compose --profile ollama run --rm tradingagents-ollama
```

### Required APIs

TradingAgents supports multiple LLM providers. Set the API key for your chosen provider:

```bash
export OPENAI_API_KEY=...          # OpenAI (GPT)
export GOOGLE_API_KEY=...          # Google (Gemini)
export ANTHROPIC_API_KEY=...       # Anthropic (Claude)
export XAI_API_KEY=...             # xAI (Grok)
export DEEPSEEK_API_KEY=...        # DeepSeek
export DASHSCOPE_API_KEY=...       # Qwen (Alibaba DashScope)
export ZHIPU_API_KEY=...           # GLM (Zhipu)
export OPENROUTER_API_KEY=...      # OpenRouter
export ALPHA_VANTAGE_API_KEY=...   # Alpha Vantage
```

For enterprise providers (e.g. Azure OpenAI, AWS Bedrock), copy `.env.enterprise.example` to `.env.enterprise` and fill in your credentials.

For local models, configure Ollama with `llm_provider: "ollama"` in your config.

Alternatively, copy `.env.example` to `.env` and fill in your keys:
```bash
cp .env.example .env
```

### CLI Usage

Launch the interactive CLI:
```bash
tradingagents          # installed command
python -m cli.main     # alternative: run directly from source
```
You will see a screen where you can select your desired tickers, analysis date, LLM provider, research depth, and more.

<p align="center">
  <img src="assets/cli/cli_init.png" width="100%" style="display: inline-block; margin: 0 2%;">
</p>

An interface will appear showing results as they load, letting you track the agent's progress as it runs.

<p align="center">
  <img src="assets/cli/cli_news.png" width="100%" style="display: inline-block; margin: 0 2%;">
</p>

<p align="center">
  <img src="assets/cli/cli_transaction.png" width="100%" style="display: inline-block; margin: 0 2%;">
</p>

## TradingAgents Package

### Implementation Details

We built TradingAgents with LangGraph to ensure flexibility and modularity. The framework supports multiple LLM providers: OpenAI, Google, Anthropic, xAI, DeepSeek, Qwen (Alibaba DashScope), GLM (Zhipu), OpenRouter, Ollama for local models, and Azure OpenAI for enterprise.

### Python Usage

To use TradingAgents inside your code, you can import the `tradingagents` module and initialize a `TradingAgentsGraph()` object. The `.propagate()` function will return a decision. You can run `main.py`, here's also a quick example:

```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

ta = TradingAgentsGraph(debug=True, config=DEFAULT_CONFIG.copy())

# forward propagate
_, decision = ta.propagate("NVDA", "2026-01-15")
print(decision)
```

You can also adjust the default configuration to set your own choice of LLMs, debate rounds, etc.

```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "openai"        # openai, google, anthropic, xai, deepseek, qwen, glm, openrouter, ollama, azure
config["deep_think_llm"] = "gpt-5.4"     # Model for complex reasoning
config["quick_think_llm"] = "gpt-5.4-mini" # Model for quick tasks
config["max_debate_rounds"] = 2

ta = TradingAgentsGraph(debug=True, config=config)
_, decision = ta.propagate("NVDA", "2026-01-15")
print(decision)
```

```

### pyproject.toml

```text
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "tradingagents"
version = "0.2.4"
description = "TradingAgents: Multi-Agents LLM Financial Trading Framework"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "langchain-core>=0.3.81",
    "backtrader>=1.9.78.123",
    "langchain-anthropic>=0.3.15",
    "langchain-experimental>=0.3.4",
    "langchain-google-genai>=4.0.0",
    "langchain-openai>=0.3.23",
    "langgraph>=0.4.8",
    "langgraph-checkpoint-sqlite>=2.0.0",
    "pandas>=2.3.0",
    "parsel>=1.10.0",
    "pytz>=2025.2",
    "questionary>=2.1.0",
    "redis>=6.2.0",
    "requests>=2.32.4",
    "rich>=14.0.0",
    "typer>=0.21.0",
    "setuptools>=80.9.0",
    "stockstats>=0.6.5",
    "tqdm>=4.67.1",
    "typing-extensions>=4.14.0",
    "yfinance>=0.2.63",
]

[project.scripts]
tradingagents = "cli.main:app"

[tool.setuptools.packages.find]
include = ["tradingagents*", "cli*"]

[tool.setuptools.package-data]
cli = ["static/*"]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-ra --strict-markers"
markers = [
    "unit: fast isolated unit tests",
    "integration: tests requiring external services",
    "smoke: quick sanity-check tests",
]
filterwarnings = [
    "ignore::DeprecationWarning",
]
```

### requirements.txt

```text
.
```

### LICENSE

```text
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

### Dockerfile

```text
FROM python:3.12-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /build
COPY . .
RUN pip install --no-cache-dir .

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN useradd --create-home appuser
USER appuser
WORKDIR /home/appuser/app

COPY --from=builder --chown=appuser:appuser /build .

ENTRYPOINT ["tradingagents"]
```

### docker-compose.yml

```text
services:
  tradingagents:
    build: .
    env_file:
      - .env
    volumes:
      - tradingagents_data:/home/appuser/.tradingagents
    tty: true
    stdin_open: true

  ollama:
    image: ollama/ollama:latest
    volumes:
      - ollama_data:/root/.ollama
    profiles:
      - ollama

  tradingagents-ollama:
    build: .
    env_file:
      - .env
    environment:
      - LLM_PROVIDER=ollama
    volumes:
      - tradingagents_data:/home/appuser/.tradingagents
    depends_on:
      - ollama
    tty: true
    stdin_open: true
    profiles:
      - ollama

volumes:
  tradingagents_data:
  ollama_data:
```

## 7. Python 文件清单，最多 200 个

```text
./cli/__init__.py
./cli/announcements.py
./cli/config.py
./cli/main.py
./cli/models.py
./cli/stats_handler.py
./cli/utils.py
./main.py
./scripts/smoke_structured_output.py
./test.py
./tests/conftest.py
./tests/test_checkpoint_resume.py
./tests/test_deepseek_reasoning.py
./tests/test_google_api_key.py
./tests/test_memory_log.py
./tests/test_model_validation.py
./tests/test_safe_ticker_component.py
./tests/test_signal_processing.py
./tests/test_structured_agents.py
./tests/test_ticker_symbol_handling.py
./tradingagents/__init__.py
./tradingagents/agents/__init__.py
./tradingagents/agents/analysts/fundamentals_analyst.py
./tradingagents/agents/analysts/market_analyst.py
./tradingagents/agents/analysts/news_analyst.py
./tradingagents/agents/analysts/social_media_analyst.py
./tradingagents/agents/managers/portfolio_manager.py
./tradingagents/agents/managers/research_manager.py
./tradingagents/agents/researchers/bear_researcher.py
./tradingagents/agents/researchers/bull_researcher.py
./tradingagents/agents/risk_mgmt/aggressive_debator.py
./tradingagents/agents/risk_mgmt/conservative_debator.py
./tradingagents/agents/risk_mgmt/neutral_debator.py
./tradingagents/agents/schemas.py
./tradingagents/agents/trader/trader.py
./tradingagents/agents/utils/agent_states.py
./tradingagents/agents/utils/agent_utils.py
./tradingagents/agents/utils/core_stock_tools.py
./tradingagents/agents/utils/fundamental_data_tools.py
./tradingagents/agents/utils/memory.py
./tradingagents/agents/utils/news_data_tools.py
./tradingagents/agents/utils/rating.py
./tradingagents/agents/utils/structured.py
./tradingagents/agents/utils/technical_indicators_tools.py
./tradingagents/dataflows/__init__.py
./tradingagents/dataflows/alpha_vantage_common.py
./tradingagents/dataflows/alpha_vantage_fundamentals.py
./tradingagents/dataflows/alpha_vantage_indicator.py
./tradingagents/dataflows/alpha_vantage_news.py
./tradingagents/dataflows/alpha_vantage_stock.py
./tradingagents/dataflows/alpha_vantage.py
./tradingagents/dataflows/config.py
./tradingagents/dataflows/interface.py
./tradingagents/dataflows/stockstats_utils.py
./tradingagents/dataflows/utils.py
./tradingagents/dataflows/y_finance.py
./tradingagents/dataflows/yfinance_news.py
./tradingagents/default_config.py
./tradingagents/graph/__init__.py
./tradingagents/graph/checkpointer.py
./tradingagents/graph/conditional_logic.py
./tradingagents/graph/propagation.py
./tradingagents/graph/reflection.py
./tradingagents/graph/setup.py
./tradingagents/graph/signal_processing.py
./tradingagents/graph/trading_graph.py
./tradingagents/llm_clients/__init__.py
./tradingagents/llm_clients/anthropic_client.py
./tradingagents/llm_clients/azure_client.py
./tradingagents/llm_clients/base_client.py
./tradingagents/llm_clients/factory.py
./tradingagents/llm_clients/google_client.py
./tradingagents/llm_clients/model_catalog.py
./tradingagents/llm_clients/openai_client.py
./tradingagents/llm_clients/validators.py
```

## 8. Agent / Graph / Workflow / Risk / Memory 关键词扫描

```text
./tests/test_structured_agents.py:3:The Portfolio Manager has its own coverage in tests/test_memory_log.py
./tests/test_structured_agents.py:4:(which exercises the full memory-log → PM injection cycle).  This file
./tests/test_structured_agents.py:7:decision-making agents share the same shape.
./tests/test_structured_agents.py:21:    render_trader_proposal,
./tests/test_structured_agents.py:23:from tradingagents.agents.trader.trader import create_trader
./tests/test_structured_agents.py:35:        md = render_trader_proposal(p)
./tests/test_structured_agents.py:39:        # analyst stop-signal text and any external code that greps for it.
./tests/test_structured_agents.py:48:            position_sizing="6% of portfolio",
./tests/test_structured_agents.py:50:        md = render_trader_proposal(p)
./tests/test_structured_agents.py:54:        assert "**Position Sizing**: 6% of portfolio" in md
./tests/test_structured_agents.py:59:        md = render_trader_proposal(p)
./tests/test_structured_agents.py:95:def _make_trader_state():
./tests/test_structured_agents.py:102:def _structured_trader_llm(captured: dict, proposal: TraderProposal | None = None):
./tests/test_structured_agents.py:104:    prompt and returns a real TraderProposal so render_trader_proposal works.
./tests/test_structured_agents.py:121:class TestTraderAgent:
./tests/test_structured_agents.py:129:            position_sizing="6% of portfolio",
./tests/test_structured_agents.py:131:        llm = _structured_trader_llm(captured, proposal)
./tests/test_structured_agents.py:132:        trader = create_trader(llm)
./tests/test_structured_agents.py:133:        result = trader(_make_trader_state())
./tests/test_structured_agents.py:134:        plan = result["trader_investment_plan"]
./tests/test_structured_agents.py:143:        llm = _structured_trader_llm(captured)
./tests/test_structured_agents.py:144:        trader = create_trader(llm)
./tests/test_structured_agents.py:145:        trader(_make_trader_state())
./tests/test_structured_agents.py:158:        trader = create_trader(llm)
./tests/test_structured_agents.py:159:        result = trader(_make_trader_state())
./tests/test_structured_agents.py:160:        assert result["trader_investment_plan"] == plain_response
./tests/test_structured_agents.py:171:        "investment_debate_state": {
./tests/test_structured_agents.py:172:            "history": "Bull and bear arguments here.",
./tests/test_structured_agents.py:173:            "bull_history": "Bull says...",
./tests/test_structured_agents.py:174:            "bear_history": "Bear says...",
./tests/test_structured_agents.py:176:            "judge_decision": "",
./tests/test_structured_agents.py:199:class TestResearchManagerAgent:
./tests/test_signal_processing.py:14:from tradingagents.graph.signal_processing import SignalProcessor
./tests/test_signal_processing.py:38:        # The exact shape produced by render_pm_decision must always parse.
./tests/test_signal_processing.py:41:            "**Executive Summary**: Enter at $189-192, 6% portfolio cap.\n\n"
./tests/test_signal_processing.py:55:        assert parse_rating("No clear directional signal at this time.") == "Hold"
./tests/test_signal_processing.py:75:        assert sp.process_signal(md) == "Overweight"
./tests/test_signal_processing.py:84:        sp.process_signal("Rating: Buy\nDetails.")
./tests/test_signal_processing.py:90:        assert sp.process_signal("Plain prose without a recommendation.") == "Hold"
./tests/test_checkpoint_resume.py:1:"""Test checkpoint resume: crash mid-analysis, re-run resumes from last node."""
./tests/test_checkpoint_resume.py:9:from langgraph.checkpoint.sqlite import SqliteSaver
./tests/test_checkpoint_resume.py:10:from langgraph.graph import END, StateGraph
./tests/test_checkpoint_resume.py:12:from tradingagents.graph.checkpointer import (
./tests/test_checkpoint_resume.py:13:    checkpoint_step,
./tests/test_checkpoint_resume.py:14:    clear_checkpoint,
./tests/test_checkpoint_resume.py:15:    get_checkpointer,
./tests/test_checkpoint_resume.py:16:    has_checkpoint,
./tests/test_checkpoint_resume.py:38:def _build_graph() -> StateGraph:
./tests/test_checkpoint_resume.py:39:    builder = StateGraph(_SimpleState)
./tests/test_checkpoint_resume.py:40:    builder.add_node("analyst", _node_a)
./tests/test_checkpoint_resume.py:41:    builder.add_node("trader", _node_b)
./tests/test_checkpoint_resume.py:42:    builder.set_entry_point("analyst")
./tests/test_checkpoint_resume.py:43:    builder.add_edge("analyst", "trader")
./tests/test_checkpoint_resume.py:44:    builder.add_edge("trader", END)
./tests/test_checkpoint_resume.py:55:        """Crash at 'trader' node, then resume from checkpoint."""
./tests/test_checkpoint_resume.py:57:        builder = _build_graph()
./tests/test_checkpoint_resume.py:61:        # Run 1: crash at trader node
./tests/test_checkpoint_resume.py:63:        with get_checkpointer(self.tmpdir, self.ticker) as saver:
./tests/test_checkpoint_resume.py:64:            graph = builder.compile(checkpointer=saver)
./tests/test_checkpoint_resume.py:66:                graph.invoke({"count": 0}, config=cfg)
./tests/test_checkpoint_resume.py:68:        # Checkpoint should exist at step 1 (analyst completed)
./tests/test_checkpoint_resume.py:69:        self.assertTrue(has_checkpoint(self.tmpdir, self.ticker, self.date))
./tests/test_checkpoint_resume.py:70:        step = checkpoint_step(self.tmpdir, self.ticker, self.date)
./tests/test_checkpoint_resume.py:73:        # Run 2: resume — trader succeeds this time
./tests/test_checkpoint_resume.py:75:        with get_checkpointer(self.tmpdir, self.ticker) as saver:
./tests/test_checkpoint_resume.py:76:            graph = builder.compile(checkpointer=saver)
./tests/test_checkpoint_resume.py:77:            result = graph.invoke(None, config=cfg)
./tests/test_checkpoint_resume.py:79:        # analyst added 1, trader added 10 → 11
./tests/test_checkpoint_resume.py:82:    def test_clear_checkpoint_allows_fresh_start(self):
./tests/test_checkpoint_resume.py:83:        """After clearing, the graph starts from scratch."""
./tests/test_checkpoint_resume.py:85:        builder = _build_graph()
./tests/test_checkpoint_resume.py:89:        # Create a checkpoint by crashing
./tests/test_checkpoint_resume.py:91:        with get_checkpointer(self.tmpdir, self.ticker) as saver:
./tests/test_checkpoint_resume.py:92:            graph = builder.compile(checkpointer=saver)
./tests/test_checkpoint_resume.py:94:                graph.invoke({"count": 0}, config=cfg)
./tests/test_checkpoint_resume.py:96:        self.assertTrue(has_checkpoint(self.tmpdir, self.ticker, self.date))
./tests/test_checkpoint_resume.py:99:        clear_checkpoint(self.tmpdir, self.ticker, self.date)
./tests/test_checkpoint_resume.py:100:        self.assertFalse(has_checkpoint(self.tmpdir, self.ticker, self.date))
./tests/test_checkpoint_resume.py:104:        with get_checkpointer(self.tmpdir, self.ticker) as saver:
./tests/test_checkpoint_resume.py:105:            graph = builder.compile(checkpointer=saver)
./tests/test_checkpoint_resume.py:106:            result = graph.invoke({"count": 0}, config=cfg)
./tests/test_checkpoint_resume.py:112:        """A different date must NOT resume from an existing checkpoint."""
./tests/test_checkpoint_resume.py:114:        builder = _build_graph()
./tests/test_checkpoint_resume.py:117:        # Run with date1 — crash to leave a checkpoint
./tests/test_checkpoint_resume.py:120:        with get_checkpointer(self.tmpdir, self.ticker) as saver:
./tests/test_checkpoint_resume.py:121:            graph = builder.compile(checkpointer=saver)
./tests/test_checkpoint_resume.py:123:                graph.invoke({"count": 0}, config={"configurable": {"thread_id": tid1}})
./tests/test_checkpoint_resume.py:125:        self.assertTrue(has_checkpoint(self.tmpdir, self.ticker, self.date))
./tests/test_checkpoint_resume.py:127:        # date2 should have no checkpoint
./tests/test_checkpoint_resume.py:128:        self.assertFalse(has_checkpoint(self.tmpdir, self.ticker, date2))
./tests/test_checkpoint_resume.py:135:        with get_checkpointer(self.tmpdir, self.ticker) as saver:
./tests/test_checkpoint_resume.py:136:            graph = builder.compile(checkpointer=saver)
./tests/test_checkpoint_resume.py:137:            result = graph.invoke({"count": 0}, config={"configurable": {"thread_id": tid2}})
./tests/test_checkpoint_resume.py:139:        # Fresh run: analyst +1, trader +10 = 11
./tests/test_checkpoint_resume.py:142:        # Original date checkpoint still exists (untouched)
./tests/test_checkpoint_resume.py:143:        self.assertTrue(has_checkpoint(self.tmpdir, self.ticker, self.date))
./tests/test_deepseek_reasoning.py:44:        # A bare string isn't a message-bearing input; the caller's normal
./tests/test_deepseek_reasoning.py:94:            additional_kwargs={"reasoning_content": "weighed bull case"},
./tests/test_deepseek_reasoning.py:101:        assert assistant_dicts[0]["reasoning_content"] == "weighed bull case"
./tests/test_deepseek_reasoning.py:109:            additional_kwargs={"reasoning_content": "weighed bull case"},
./tests/test_deepseek_reasoning.py:114:        assert assistant_dicts[0]["reasoning_content"] == "weighed bull case"
./tests/test_memory_log.py:7:from tradingagents.agents.utils.memory import TradingMemoryLog
./tests/test_memory_log.py:9:from tradingagents.graph.reflection import Reflector
./tests/test_memory_log.py:10:from tradingagents.graph.trading_graph import TradingAgentsGraph
./tests/test_memory_log.py:11:from tradingagents.graph.propagation import Propagator
./tests/test_memory_log.py:12:from tradingagents.agents.managers.portfolio_manager import create_portfolio_manager
./tests/test_memory_log.py:16:DECISION_BUY = "Rating: Buy\nEnter at $189-192, 6% portfolio cap."
./tests/test_memory_log.py:25:    "Investment Thesis: No clear directional signal at this time."
./tests/test_memory_log.py:33:def make_log(tmp_path, filename="trading_memory.md"):
./tests/test_memory_log.py:34:    config = {"memory_log_path": str(tmp_path / filename)}
./tests/test_memory_log.py:38:def _seed_completed(tmp_path, ticker, date, decision_text, reflection_text, filename="trading_memory.md"):
./tests/test_memory_log.py:42:        f"DECISION:\n{decision_text}\n\n"
./tests/test_memory_log.py:50:def _resolve_entry(log, ticker, date, decision, reflection="Good call."):
./tests/test_memory_log.py:51:    """Store a decision then immediately resolve it via the API."""
./tests/test_memory_log.py:52:    log.store_decision(ticker, date, decision)
./tests/test_memory_log.py:62:    """Minimal AgentState dict for portfolio_manager_node."""
./tests/test_memory_log.py:66:        "risk_debate_state": {
./tests/test_memory_log.py:67:            "history": "Risk debate history.",
./tests/test_memory_log.py:71:            "judge_decision": "",
./tests/test_memory_log.py:82:        "trader_investment_plan": "Trader plan.",
./tests/test_memory_log.py:86:def _structured_pm_llm(captured: dict, decision: PortfolioDecision | None = None):
./tests/test_memory_log.py:88:    prompt and returns a real PortfolioDecision (so render_pm_decision works).
./tests/test_memory_log.py:90:    if decision is None:
./tests/test_memory_log.py:91:        decision = PortfolioDecision(
./tests/test_memory_log.py:94:            investment_thesis="Balanced view; neither side carried the debate.",
./tests/test_memory_log.py:98:        captured.__setitem__("prompt", prompt) or decision
./tests/test_memory_log.py:113:        assert not (tmp_path / "trading_memory.md").exists()
./tests/test_memory_log.py:114:        log.store_decision("NVDA", "2026-01-10", DECISION_BUY)
./tests/test_memory_log.py:115:        assert (tmp_path / "trading_memory.md").exists()
./tests/test_memory_log.py:119:        log.store_decision("NVDA", "2026-01-10", DECISION_BUY)
./tests/test_memory_log.py:120:        log.store_decision("AAPL", "2026-01-11", DECISION_OVERWEIGHT)
./tests/test_memory_log.py:126:    def test_store_decision_idempotent(self, tmp_path):
./tests/test_memory_log.py:127:        """Calling store_decision twice with same (ticker, date) stores only one entry."""
./tests/test_memory_log.py:129:        log.store_decision("NVDA", "2026-01-10", DECISION_BUY)
./tests/test_memory_log.py:130:        log.store_decision("NVDA", "2026-01-10", DECISION_BUY)
./tests/test_memory_log.py:136:        log.store_decision("NVDA", "2026-01-05", DECISION_BUY)
./tests/test_memory_log.py:137:        log.store_decision("NVDA", "2026-01-12", DECISION_SELL)
./tests/test_memory_log.py:157:        log.store_decision("NVDA", "2026-01-10", DECISION_BUY)
./tests/test_memory_log.py:158:        text = (tmp_path / "trading_memory.md").read_text(encoding="utf-8")
./tests/test_memory_log.py:165:        log.store_decision("NVDA", "2026-01-10", DECISION_BUY)
./tests/test_memory_log.py:170:        log.store_decision("AAPL", "2026-01-11", DECISION_OVERWEIGHT)
./tests/test_memory_log.py:175:        log.store_decision("MSFT", "2026-01-12", DECISION_NO_RATING)
./tests/test_memory_log.py:180:        decision = (
./tests/test_memory_log.py:186:        log.store_decision("NVDA", "2026-01-10", decision)
./tests/test_memory_log.py:191:    def test_decision_with_markdown_separator(self, tmp_path):
./tests/test_memory_log.py:192:        """LLM decision containing '---' must not corrupt the entry."""
./tests/test_memory_log.py:193:        decision = "Rating: Buy\n\n---\n\nRisk: elevated volatility."
./tests/test_memory_log.py:195:        log.store_decision("NVDA", "2026-01-10", decision)
./tests/test_memory_log.py:198:        assert "Risk: elevated volatility" in entries[0]["decision"]
./tests/test_memory_log.py:208:        log.store_decision("NVDA", "2026-01-10", DECISION_BUY)
./tests/test_memory_log.py:220:        log.store_decision("NVDA", "2026-01-10", DECISION_BUY)
./tests/test_memory_log.py:221:        log.store_decision("AAPL", "2026-01-11", DECISION_OVERWEIGHT)
./tests/test_memory_log.py:222:        log.store_decision("MSFT", "2026-01-12", DECISION_NO_RATING)
./tests/test_memory_log.py:227:    def test_decision_content_preserved(self, tmp_path):
./tests/test_memory_log.py:229:        log.store_decision("NVDA", "2026-01-10", DECISION_BUY)
./tests/test_memory_log.py:230:        assert log.load_entries()[0]["decision"] == DECISION_BUY.strip()
./tests/test_memory_log.py:237:        log.store_decision("NVDA", "2026-01-10", DECISION_BUY)
./tests/test_memory_log.py:251:        log.store_decision("NVDA", "2026-01-10", DECISION_BUY)
./tests/test_memory_log.py:290:        log.store_decision("NVDA", "2026-01-10", DECISION_BUY)
./tests/test_memory_log.py:306:            "memory_log_path": str(tmp_path / "trading_memory.md"),
./tests/test_memory_log.py:307:            "memory_log_max_entries": 3,
./tests/test_memory_log.py:321:            "memory_log_path": str(tmp_path / "trading_memory.md"),
./tests/test_memory_log.py:322:            "memory_log_max_entries": 2,
./tests/test_memory_log.py:327:        log.store_decision("NVDA", "2026-02-01", DECISION_BUY)
./tests/test_memory_log.py:328:        log.store_decision("NVDA", "2026-02-02", DECISION_OVERWEIGHT)
./tests/test_memory_log.py:340:            "memory_log_path": str(tmp_path / "trading_memory.md"),
./tests/test_memory_log.py:341:            "memory_log_max_entries": 10,
./tests/test_memory_log.py:351:        decision = "**Rating**: Buy\nEnter at $190."
./tests/test_memory_log.py:353:        log.store_decision("NVDA", "2026-01-10", decision)
./tests/test_memory_log.py:358:        decision = "Rating: **Sell**\nExit immediately."
./tests/test_memory_log.py:360:        log.store_decision("NVDA", "2026-01-10", decision)
./tests/test_memory_log.py:365:        decision = (
./tests/test_memory_log.py:371:        log.store_decision("NVDA", "2026-01-10", decision)
./tests/test_memory_log.py:376:        decision = "1. Rating: Buy\nEnter at $190."
./tests/test_memory_log.py:378:        log.store_decision("NVDA", "2026-01-10", decision)
./tests/test_memory_log.py:392:        log.store_decision("NVDA", "2026-01-10", DECISION_BUY)
./tests/test_memory_log.py:394:        text = (tmp_path / "trading_memory.md").read_text(encoding="utf-8")
./tests/test_memory_log.py:402:        log.store_decision("NVDA", "2026-01-10", DECISION_BUY)
./tests/test_memory_log.py:409:        assert e["decision"] == DECISION_BUY.strip()
./tests/test_memory_log.py:414:        log.store_decision("NVDA", "2026-01-10", DECISION_BUY)
./tests/test_memory_log.py:415:        log.store_decision("AAPL", "2026-01-11", "Rating: Hold\nHold AAPL.")
./tests/test_memory_log.py:416:        log.store_decision("MSFT", "2026-01-12", DECISION_SELL)
./tests/test_memory_log.py:429:        log.store_decision("NVDA", "2026-01-10", DECISION_BUY)
./tests/test_memory_log.py:430:        stale_tmp = tmp_path / "trading_memory.tmp"
./tests/test_memory_log.py:446:        log.store_decision("NVDA", "2026-01-10", DECISION_BUY)
./tests/test_memory_log.py:452:        assert e["decision"] == DECISION_BUY.strip()
./tests/test_memory_log.py:457:        raw_text = (tmp_path / "trading_memory.md").read_text(encoding="utf-8")
./tests/test_memory_log.py:460:    # Reflector.reflect_on_final_decision
./tests/test_memory_log.py:462:    def test_reflect_on_final_decision_returns_llm_output(self):
./tests/test_memory_log.py:466:        result = reflector.reflect_on_final_decision(
./tests/test_memory_log.py:467:            final_decision=DECISION_BUY, raw_return=0.042, alpha_return=0.021
./tests/test_memory_log.py:472:    def test_reflect_on_final_decision_includes_returns_in_prompt(self):
./tests/test_memory_log.py:477:        reflector.reflect_on_final_decision(
./tests/test_memory_log.py:478:            final_decision=DECISION_SELL, raw_return=-0.08, alpha_return=-0.05
./tests/test_memory_log.py:491:        mock_graph = MagicMock(spec=TradingAgentsGraph)
./tests/test_memory_log.py:498:            raw, alpha, days = TradingAgentsGraph._fetch_returns(mock_graph, "NVDA", "2026-01-05")
./tests/test_memory_log.py:505:        mock_graph = MagicMock(spec=TradingAgentsGraph)
./tests/test_memory_log.py:510:            raw, alpha, days = TradingAgentsGraph._fetch_returns(mock_graph, "NVDA", "2026-04-19")
./tests/test_memory_log.py:515:        mock_graph = MagicMock(spec=TradingAgentsGraph)
./tests/test_memory_log.py:520:            raw, alpha, days = TradingAgentsGraph._fetch_returns(mock_graph, "XXXXXFAKE", "2026-01-10")
./tests/test_memory_log.py:527:        mock_graph = MagicMock(spec=TradingAgentsGraph)
./tests/test_memory_log.py:534:            raw, alpha, days = TradingAgentsGraph._fetch_returns(mock_graph, "NVDA", "2026-01-05")
./tests/test_memory_log.py:543:        log.store_decision("AAPL", "2026-01-10", DECISION_BUY)
./tests/test_memory_log.py:544:        mock_graph = MagicMock(spec=TradingAgentsGraph)
./tests/test_memory_log.py:545:        mock_graph.memory_log = log
./tests/test_memory_log.py:546:        mock_graph._fetch_returns = MagicMock(return_value=(0.05, 0.02, 5))
./tests/test_memory_log.py:547:        TradingAgentsGraph._resolve_pending_entries(mock_graph, "NVDA")
./tests/test_memory_log.py:548:        mock_graph._fetch_returns.assert_not_called()
./tests/test_memory_log.py:554:        log.store_decision("NVDA", "2026-01-05", DECISION_BUY)
./tests/test_memory_log.py:556:        mock_reflector.reflect_on_final_decision.return_value = "Momentum confirmed."
./tests/test_memory_log.py:557:        mock_graph = MagicMock(spec=TradingAgentsGraph)
./tests/test_memory_log.py:558:        mock_graph.memory_log = log
./tests/test_memory_log.py:559:        mock_graph.reflector = mock_reflector
./tests/test_memory_log.py:560:        mock_graph._fetch_returns = MagicMock(return_value=(0.05, 0.02, 5))
./tests/test_memory_log.py:561:        TradingAgentsGraph._resolve_pending_entries(mock_graph, "NVDA")
./tests/test_memory_log.py:595:        pm_node = create_portfolio_manager(llm)
./tests/test_memory_log.py:598:        assert "Lessons from prior decisions and outcomes" in captured["prompt"]
./tests/test_memory_log.py:605:        pm_node = create_portfolio_manager(llm)
./tests/test_memory_log.py:608:        assert "Lessons from prior decisions" not in captured["prompt"]
./tests/test_memory_log.py:612:        downstream consumers (memory log, signal processor, CLI display)
./tests/test_memory_log.py:615:        decision = PortfolioDecision(
./tests/test_memory_log.py:622:        llm = _structured_pm_llm(captured, decision)
./tests/test_memory_log.py:623:        pm_node = create_portfolio_manager(llm)
./tests/test_memory_log.py:625:        md = result["final_trade_decision"]
./tests/test_memory_log.py:640:        pm_node = create_portfolio_manager(llm)
./tests/test_memory_log.py:642:        assert result["final_trade_decision"] == plain_response
./tests/test_memory_log.py:690:        log.store_decision("NVDA", "2026-01-05", DECISION_BUY)
./tests/test_memory_log.py:709:    def test_financial_situation_memory_removed(self):
./tests/test_memory_log.py:710:        """FinancialSituationMemory must not be importable from the memory module."""
./tests/test_memory_log.py:711:        import tradingagents.agents.utils.memory as m
./tests/test_memory_log.py:715:        """rank_bm25 must not be present in the memory module namespace."""
./tests/test_memory_log.py:716:        import tradingagents.agents.utils.memory as m
./tests/test_memory_log.py:723:    def test_portfolio_manager_no_memory_param(self):
./tests/test_memory_log.py:724:        """create_portfolio_manager accepts only llm; passing memory= raises TypeError."""
./tests/test_memory_log.py:726:        create_portfolio_manager(mock_llm)
./tests/test_memory_log.py:728:            create_portfolio_manager(mock_llm, memory=MagicMock())
./tests/test_memory_log.py:731:        """propagate() completes and stores the decision after the redesign."""
./tests/test_memory_log.py:735:            "final_trade_decision": "Rating: Buy\nBuy NVDA.",
./tests/test_memory_log.py:742:            "investment_debate_state": {
./tests/test_memory_log.py:743:                "bull_history": "", "bear_history": "", "history": "",
./tests/test_memory_log.py:744:                "current_response": "", "judge_decision": "",
./tests/test_memory_log.py:747:            "trader_investment_plan": "",
./tests/test_memory_log.py:748:            "risk_debate_state": {
./tests/test_memory_log.py:750:                "neutral_history": "", "history": "", "judge_decision": "",
./tests/test_memory_log.py:755:        mock_graph = MagicMock()
./tests/test_memory_log.py:756:        mock_graph.memory_log = TradingMemoryLog({"memory_log_path": str(tmp_path / "mem.md")})
./tests/test_memory_log.py:757:        mock_graph.log_states_dict = {}
./tests/test_memory_log.py:758:        mock_graph.debug = False
./tests/test_memory_log.py:759:        mock_graph.config = {"results_dir": str(tmp_path)}
./tests/test_memory_log.py:760:        mock_graph.graph.invoke.return_value = fake_state
./tests/test_memory_log.py:761:        mock_graph.propagator.create_initial_state.return_value = fake_state
./tests/test_memory_log.py:762:        mock_graph.propagator.get_graph_args.return_value = {}
./tests/test_memory_log.py:763:        mock_graph.signal_processor.process_signal.return_value = "Buy"
./tests/test_memory_log.py:764:        # Bind the real _run_graph so propagate's call to self._run_graph executes
./tests/test_memory_log.py:766:        mock_graph._run_graph = functools.partial(
./tests/test_memory_log.py:767:            TradingAgentsGraph._run_graph, mock_graph
./tests/test_memory_log.py:769:        TradingAgentsGraph.propagate(mock_graph, "NVDA", "2026-01-10")
./tests/test_memory_log.py:770:        entries = mock_graph.memory_log.load_entries()
./cli/utils.py:79:def select_analysts() -> List[AnalystType]:
./cli/utils.py:80:    """Select analysts using an interactive checkbox."""
./cli/utils.py:86:        instruction="\n- Press Space to select/unselect analysts\n- Press 'a' to select/unselect all\n- Press Enter when done",
./cli/utils.py:87:        validate=lambda x: len(x) > 0 or "You must select at least one analyst.",
./cli/utils.py:99:        console.print("\n[red]No analysts selected. Exiting...[/red]")
./cli/utils.py:110:        ("Shallow - Quick research, few debate and strategy discussion rounds", 1),
./cli/utils.py:111:        ("Medium - Middle ground, moderate debate rounds and strategy discussion", 3),
./cli/utils.py:112:        ("Deep - Comprehensive research, in depth debate and strategy discussion", 5),
./cli/main.py:27:from tradingagents.graph.trading_graph import TradingAgentsGraph
./cli/main.py:61:    # Report section mapping: section -> (analyst_key for filtering, finalizing_agent)
./cli/main.py:62:    # analyst_key: which analyst selection controls this section (None = always included)
./cli/main.py:70:        "trader_investment_plan": (None, "Trader"),
./cli/main.py:71:        "final_trade_decision": (None, "Portfolio Manager"),
./cli/main.py:82:        self.selected_analysts = []
./cli/main.py:85:    def init_for_analysis(self, selected_analysts):
./cli/main.py:86:        """Initialize agent status and report sections based on selected analysts.
./cli/main.py:89:            selected_analysts: List of analyst type strings (e.g., ["market", "news"])
./cli/main.py:91:        self.selected_analysts = [a.lower() for a in selected_analysts]
./cli/main.py:96:        # Add selected analysts
./cli/main.py:97:        for analyst_key in self.selected_analysts:
./cli/main.py:98:            if analyst_key in self.ANALYST_MAPPING:
./cli/main.py:99:                self.agent_status[self.ANALYST_MAPPING[analyst_key]] = "pending"
./cli/main.py:108:        for section, (analyst_key, _) in self.REPORT_SECTIONS.items():
./cli/main.py:109:            if analyst_key is None or analyst_key in self.selected_analysts:
./cli/main.py:127:        This prevents interim updates (like debate rounds) from counting as completed.
./cli/main.py:178:                "trader_investment_plan": "Trading Team Plan",
./cli/main.py:179:                "final_trade_decision": "Portfolio Management Decision",
./cli/main.py:192:        analyst_sections = ["market_report", "sentiment_report", "news_report", "fundamentals_report"]
./cli/main.py:193:        if any(self.report_sections.get(section) for section in analyst_sections):
./cli/main.py:218:        if self.report_sections.get("trader_investment_plan"):
./cli/main.py:220:            report_parts.append(f"{self.report_sections['trader_investment_plan']}")
./cli/main.py:223:        if self.report_sections.get("final_trade_decision"):
./cli/main.py:225:            report_parts.append(f"{self.report_sections['final_trade_decision']}")
./cli/main.py:527:            "Select the language for analyst reports and final decision"
./cli/main.py:532:    # Step 4: Select analysts
./cli/main.py:535:            "Step 4: Analysts Team", "Select your LLM analyst agents for the analysis"
./cli/main.py:538:    selected_analysts = select_analysts()
./cli/main.py:540:        f"[green]Selected analysts:[/green] {', '.join(analyst.value for analyst in selected_analysts)}"
./cli/main.py:602:        "analysts": selected_analysts,
./cli/main.py:645:    analysts_dir = save_path / "1_analysts"
./cli/main.py:646:    analyst_parts = []
./cli/main.py:648:        analysts_dir.mkdir(exist_ok=True)
./cli/main.py:649:        (analysts_dir / "market.md").write_text(final_state["market_report"], encoding="utf-8")
./cli/main.py:650:        analyst_parts.append(("Market Analyst", final_state["market_report"]))
./cli/main.py:652:        analysts_dir.mkdir(exist_ok=True)
./cli/main.py:653:        (analysts_dir / "sentiment.md").write_text(final_state["sentiment_report"], encoding="utf-8")
./cli/main.py:654:        analyst_parts.append(("Social Analyst", final_state["sentiment_report"]))
./cli/main.py:656:        analysts_dir.mkdir(exist_ok=True)
./cli/main.py:657:        (analysts_dir / "news.md").write_text(final_state["news_report"], encoding="utf-8")
./cli/main.py:658:        analyst_parts.append(("News Analyst", final_state["news_report"]))
./cli/main.py:660:        analysts_dir.mkdir(exist_ok=True)
./cli/main.py:661:        (analysts_dir / "fundamentals.md").write_text(final_state["fundamentals_report"], encoding="utf-8")
./cli/main.py:662:        analyst_parts.append(("Fundamentals Analyst", final_state["fundamentals_report"]))
./cli/main.py:663:    if analyst_parts:
./cli/main.py:664:        content = "\n\n".join(f"### {name}\n{text}" for name, text in analyst_parts)
./cli/main.py:668:    if final_state.get("investment_debate_state"):
./cli/main.py:670:        debate = final_state["investment_debate_state"]
./cli/main.py:672:        if debate.get("bull_history"):
./cli/main.py:674:            (research_dir / "bull.md").write_text(debate["bull_history"], encoding="utf-8")
./cli/main.py:675:            research_parts.append(("Bull Researcher", debate["bull_history"]))
./cli/main.py:676:        if debate.get("bear_history"):
./cli/main.py:678:            (research_dir / "bear.md").write_text(debate["bear_history"], encoding="utf-8")
./cli/main.py:679:            research_parts.append(("Bear Researcher", debate["bear_history"]))
./cli/main.py:680:        if debate.get("judge_decision"):
./cli/main.py:682:            (research_dir / "manager.md").write_text(debate["judge_decision"], encoding="utf-8")
./cli/main.py:683:            research_parts.append(("Research Manager", debate["judge_decision"]))
./cli/main.py:689:    if final_state.get("trader_investment_plan"):
./cli/main.py:692:        (trading_dir / "trader.md").write_text(final_state["trader_investment_plan"], encoding="utf-8")
./cli/main.py:693:        sections.append(f"## III. Trading Team Plan\n\n### Trader\n{final_state['trader_investment_plan']}")
./cli/main.py:696:    if final_state.get("risk_debate_state"):
./cli/main.py:697:        risk_dir = save_path / "4_risk"
./cli/main.py:698:        risk = final_state["risk_debate_state"]
./cli/main.py:699:        risk_parts = []
./cli/main.py:700:        if risk.get("aggressive_history"):
./cli/main.py:701:            risk_dir.mkdir(exist_ok=True)
./cli/main.py:702:            (risk_dir / "aggressive.md").write_text(risk["aggressive_history"], encoding="utf-8")
./cli/main.py:703:            risk_parts.append(("Aggressive Analyst", risk["aggressive_history"]))
./cli/main.py:704:        if risk.get("conservative_history"):
./cli/main.py:705:            risk_dir.mkdir(exist_ok=True)
./cli/main.py:706:            (risk_dir / "conservative.md").write_text(risk["conservative_history"], encoding="utf-8")
./cli/main.py:707:            risk_parts.append(("Conservative Analyst", risk["conservative_history"]))
./cli/main.py:708:        if risk.get("neutral_history"):
./cli/main.py:709:            risk_dir.mkdir(exist_ok=True)
./cli/main.py:710:            (risk_dir / "neutral.md").write_text(risk["neutral_history"], encoding="utf-8")
./cli/main.py:711:            risk_parts.append(("Neutral Analyst", risk["neutral_history"]))
./cli/main.py:712:        if risk_parts:
./cli/main.py:713:            content = "\n\n".join(f"### {name}\n{text}" for name, text in risk_parts)
./cli/main.py:717:        if risk.get("judge_decision"):
./cli/main.py:718:            portfolio_dir = save_path / "5_portfolio"
./cli/main.py:719:            portfolio_dir.mkdir(exist_ok=True)
./cli/main.py:720:            (portfolio_dir / "decision.md").write_text(risk["judge_decision"], encoding="utf-8")
./cli/main.py:721:            sections.append(f"## V. Portfolio Manager Decision\n\n### Portfolio Manager\n{risk['judge_decision']}")
./cli/main.py:735:    analysts = []
./cli/main.py:737:        analysts.append(("Market Analyst", final_state["market_report"]))
./cli/main.py:739:        analysts.append(("Social Analyst", final_state["sentiment_report"]))
./cli/main.py:741:        analysts.append(("News Analyst", final_state["news_report"]))
./cli/main.py:743:        analysts.append(("Fundamentals Analyst", final_state["fundamentals_report"]))
./cli/main.py:744:    if analysts:
./cli/main.py:746:        for title, content in analysts:
./cli/main.py:750:    if final_state.get("investment_debate_state"):
./cli/main.py:751:        debate = final_state["investment_debate_state"]
./cli/main.py:753:        if debate.get("bull_history"):
./cli/main.py:754:            research.append(("Bull Researcher", debate["bull_history"]))
./cli/main.py:755:        if debate.get("bear_history"):
./cli/main.py:756:            research.append(("Bear Researcher", debate["bear_history"]))
./cli/main.py:757:        if debate.get("judge_decision"):
./cli/main.py:758:            research.append(("Research Manager", debate["judge_decision"]))
./cli/main.py:765:    if final_state.get("trader_investment_plan"):
./cli/main.py:767:        console.print(Panel(Markdown(final_state["trader_investment_plan"]), title="Trader", border_style="blue", padding=(1, 2)))
./cli/main.py:770:    if final_state.get("risk_debate_state"):
./cli/main.py:771:        risk = final_state["risk_debate_state"]
./cli/main.py:772:        risk_reports = []
./cli/main.py:773:        if risk.get("aggressive_history"):
./cli/main.py:774:            risk_reports.append(("Aggressive Analyst", risk["aggressive_history"]))
./cli/main.py:775:        if risk.get("conservative_history"):
./cli/main.py:776:            risk_reports.append(("Conservative Analyst", risk["conservative_history"]))
./cli/main.py:777:        if risk.get("neutral_history"):
./cli/main.py:778:            risk_reports.append(("Neutral Analyst", risk["neutral_history"]))
./cli/main.py:779:        if risk_reports:
./cli/main.py:781:            for title, content in risk_reports:
./cli/main.py:785:        if risk.get("judge_decision"):
./cli/main.py:787:            console.print(Panel(Markdown(risk["judge_decision"]), title="Portfolio Manager", border_style="blue", padding=(1, 2)))
./cli/main.py:797:# Ordered list of analysts for status transitions
./cli/main.py:813:def update_analyst_statuses(message_buffer, chunk):
./cli/main.py:814:    """Update analyst statuses based on accumulated report state.
./cli/main.py:820:    - First analyst without report = in_progress
./cli/main.py:821:    - Remaining analysts without reports = pending
./cli/main.py:822:    - When all analysts done, set Bull Researcher to in_progress
./cli/main.py:824:    selected = message_buffer.selected_analysts
./cli/main.py:827:    for analyst_key in ANALYST_ORDER:
./cli/main.py:828:        if analyst_key not in selected:
./cli/main.py:831:        agent_name = ANALYST_AGENT_NAMES[analyst_key]
./cli/main.py:832:        report_key = ANALYST_REPORT_MAP[analyst_key]
./cli/main.py:849:    # When all analysts complete, transition research team to in_progress
./cli/main.py:929:def run_analysis(checkpoint: bool = False):
./cli/main.py:935:    config["max_debate_rounds"] = selections["research_depth"]
./cli/main.py:936:    config["max_risk_discuss_rounds"] = selections["research_depth"]
./cli/main.py:946:    config["checkpoint_enabled"] = checkpoint
./cli/main.py:951:    # Normalize analyst selection to predefined order (selection is a 'set', order is fixed)
./cli/main.py:952:    selected_set = {analyst.value for analyst in selections["analysts"]}
./cli/main.py:953:    selected_analyst_keys = [a for a in ANALYST_ORDER if a in selected_set]
./cli/main.py:955:    # Initialize the graph with callbacks bound to LLMs
```

## 9. 数据源 / LLM / 配置关键词扫描

```text
./tests/test_structured_agents.py:156:        llm.with_structured_output.side_effect = NotImplementedError("provider unsupported")
./tests/test_structured_agents.py:228:        llm.with_structured_output.side_effect = NotImplementedError("provider unsupported")
./tests/conftest.py:9:def pytest_configure(config):
./tests/conftest.py:11:        config.addinivalue_line("markers", f"{marker}: {marker}-level tests")
./tests/conftest.py:14:_API_KEY_ENV_VARS = (
./tests/conftest.py:15:    "OPENAI_API_KEY",
./tests/conftest.py:16:    "GOOGLE_API_KEY",
./tests/conftest.py:17:    "ANTHROPIC_API_KEY",
./tests/conftest.py:18:    "XAI_API_KEY",
./tests/conftest.py:19:    "DEEPSEEK_API_KEY",
./tests/conftest.py:20:    "DASHSCOPE_API_KEY",
./tests/conftest.py:21:    "ZHIPU_API_KEY",
./tests/conftest.py:22:    "OPENROUTER_API_KEY",
./tests/conftest.py:23:    "AZURE_OPENAI_API_KEY",
./tests/conftest.py:24:    "ALPHA_VANTAGE_API_KEY",
./tests/conftest.py:29:def _dummy_api_keys(monkeypatch):
./tests/conftest.py:30:    for env_var in _API_KEY_ENV_VARS:
./tests/test_model_validation.py:7:from tradingagents.llm_clients.model_catalog import get_known_models
./tests/test_model_validation.py:8:from tradingagents.llm_clients.validators import validate_model
./tests/test_model_validation.py:12:    def __init__(self, provider: str, model: str):
./tests/test_model_validation.py:13:        self.provider = provider
./tests/test_model_validation.py:14:        super().__init__(model)
./tests/test_model_validation.py:17:        self.warn_if_unknown_model()
./tests/test_model_validation.py:20:    def validate_model(self) -> bool:
./tests/test_model_validation.py:21:        return validate_model(self.provider, self.model)
./tests/test_model_validation.py:26:    def test_cli_catalog_models_are_all_validator_approved(self):
./tests/test_model_validation.py:27:        for provider, models in get_known_models().items():
./tests/test_model_validation.py:28:            if provider in ("ollama", "openrouter"):
./tests/test_model_validation.py:31:            for model in models:
./tests/test_model_validation.py:32:                with self.subTest(provider=provider, model=model):
./tests/test_model_validation.py:33:                    self.assertTrue(validate_model(provider, model))
./tests/test_model_validation.py:35:    def test_unknown_model_emits_warning_for_strict_provider(self):
./tests/test_model_validation.py:36:        client = DummyLLMClient("openai", "not-a-real-openai-model")
./tests/test_model_validation.py:43:        self.assertIn("not-a-real-openai-model", str(caught[0].message))
./tests/test_model_validation.py:44:        self.assertIn("openai", str(caught[0].message))
./tests/test_model_validation.py:46:    def test_openrouter_and_ollama_accept_custom_models_without_warning(self):
./tests/test_model_validation.py:47:        for provider in ("openrouter", "ollama"):
./tests/test_model_validation.py:48:            client = DummyLLMClient(provider, "custom-model-name")
./tests/test_model_validation.py:50:            with self.subTest(provider=provider):
./tests/test_checkpoint_resume.py:59:        cfg = {"configurable": {"thread_id": tid}}
./tests/test_checkpoint_resume.py:66:                graph.invoke({"count": 0}, config=cfg)
./tests/test_checkpoint_resume.py:77:            result = graph.invoke(None, config=cfg)
./tests/test_checkpoint_resume.py:87:        cfg = {"configurable": {"thread_id": tid}}
./tests/test_checkpoint_resume.py:94:                graph.invoke({"count": 0}, config=cfg)
./tests/test_checkpoint_resume.py:106:            result = graph.invoke({"count": 0}, config=cfg)
./tests/test_checkpoint_resume.py:123:                graph.invoke({"count": 0}, config={"configurable": {"thread_id": tid1}})
./tests/test_checkpoint_resume.py:137:            result = graph.invoke({"count": 0}, config={"configurable": {"thread_id": tid2}})
./tests/test_google_api_key.py:11:    """Verify GoogleClient accepts unified api_key parameter."""
./tests/test_google_api_key.py:14:    def test_api_key_handling(self, mock_chat):
./tests/test_google_api_key.py:16:            ("unified api_key is mapped", {"api_key": "test-key-123"}, "test-key-123"),
./tests/test_google_api_key.py:17:            ("legacy google_api_key still works", {"google_api_key": "legacy-key-456"}, "legacy-key-456"),
./tests/test_google_api_key.py:18:            ("unified api_key takes precedence", {"api_key": "unified", "google_api_key": "legacy"}, "unified"),
./tests/test_google_api_key.py:27:                self.assertEqual(call_kwargs.get("google_api_key"), expected_key)
./tests/test_deepseek_reasoning.py:9:   ``deepseek-reasoner`` so the agent factories' free-text fallback
./tests/test_deepseek_reasoning.py:19:from tradingagents.llm_clients.openai_client import (
./tests/test_deepseek_reasoning.py:57:        os.environ.setdefault("DEEPSEEK_API_KEY", "placeholder")
./tests/test_deepseek_reasoning.py:59:            model="deepseek-v4-flash",
./tests/test_deepseek_reasoning.py:60:            api_key="placeholder",
./tests/test_deepseek_reasoning.py:61:            base_url="https://api.deepseek.com",
./tests/test_deepseek_reasoning.py:70:                "model": "deepseek-v4-flash",
./tests/test_deepseek_reasoning.py:118:# deepseek-reasoner: structured output unavailable, falls through to free-text
./tests/test_deepseek_reasoning.py:126:            model="deepseek-reasoner",
./tests/test_deepseek_reasoning.py:127:            api_key="placeholder",
./tests/test_deepseek_reasoning.py:128:            base_url="https://api.deepseek.com",
./tests/test_deepseek_reasoning.py:139:        """V4 models (non-reasoner) accept tool_choice; structured output works."""
./tests/test_deepseek_reasoning.py:141:            model="deepseek-v4-flash",
./tests/test_deepseek_reasoning.py:142:            api_key="placeholder",
./tests/test_deepseek_reasoning.py:143:            base_url="https://api.deepseek.com",
./tests/test_memory_log.py:34:    config = {"memory_log_path": str(tmp_path / filename)}
./tests/test_memory_log.py:35:    return TradingMemoryLog(config)
./tests/test_memory_log.py:57:    """Minimal DataFrame matching yfinance .history() output shape."""
./tests/test_memory_log.py:286:    # No-op when config is None
./tests/test_memory_log.py:289:        log = TradingMemoryLog(config=None)
./tests/test_memory_log.py:440:        log = TradingMemoryLog(config=None)
./tests/test_memory_log.py:492:        with patch("yfinance.Ticker") as mock_ticker_cls:
./tests/test_memory_log.py:506:        with patch("yfinance.Ticker") as mock_ticker_cls:
./tests/test_memory_log.py:516:        with patch("yfinance.Ticker") as mock_ticker_cls:
./tests/test_memory_log.py:528:        with patch("yfinance.Ticker") as mock_ticker_cls:
./tests/test_memory_log.py:633:        """If a provider does not support with_structured_output, the agent
./tests/test_memory_log.py:634:        falls back to a plain invoke and returns whatever prose the model
./tests/test_memory_log.py:638:        llm.with_structured_output.side_effect = NotImplementedError("provider unsupported")
./tests/test_memory_log.py:759:        mock_graph.config = {"results_dir": str(tmp_path)}
./cli/utils.py:6:from cli.models import AnalystType
./cli/utils.py:7:from tradingagents.llm_clients.model_catalog import get_model_options
./cli/utils.py:137:def _fetch_openrouter_models() -> List[Tuple[str, str]]:
./cli/utils.py:138:    """Fetch available models from the OpenRouter API."""
./cli/utils.py:141:        resp = requests.get("https://openrouter.ai/api/v1/models", timeout=10)
./cli/utils.py:143:        models = resp.json().get("data", [])
./cli/utils.py:144:        return [(m.get("name") or m["id"], m["id"]) for m in models]
./cli/utils.py:146:        console.print(f"\n[yellow]Could not fetch OpenRouter models: {e}[/yellow]")
./cli/utils.py:150:def select_openrouter_model() -> str:
./cli/utils.py:151:    """Select an OpenRouter model from the newest available, or enter a custom ID."""
./cli/utils.py:152:    models = _fetch_openrouter_models()
./cli/utils.py:154:    choices = [questionary.Choice(name, value=mid) for name, mid in models[:5]]
./cli/utils.py:155:    choices.append(questionary.Choice("Custom model ID", value="custom"))
./cli/utils.py:170:            "Enter OpenRouter model ID (e.g. google/gemma-4-26b-a4b-it):",
./cli/utils.py:171:            validate=lambda x: len(x.strip()) > 0 or "Please enter a model ID.",
./cli/utils.py:177:def _prompt_custom_model_id() -> str:
./cli/utils.py:178:    """Prompt user to type a custom model ID."""
./cli/utils.py:180:        "Enter model ID:",
./cli/utils.py:181:        validate=lambda x: len(x.strip()) > 0 or "Please enter a model ID.",
./cli/utils.py:185:def _select_model(provider: str, mode: str) -> str:
./cli/utils.py:186:    """Select a model for the given provider and mode (quick/deep)."""
./cli/utils.py:187:    if provider.lower() == "openrouter":
./cli/utils.py:188:        return select_openrouter_model()
./cli/utils.py:190:    if provider.lower() == "azure":
./cli/utils.py:200:            for display, value in get_model_options(provider, mode)
./cli/utils.py:217:        return _prompt_custom_model_id()
./cli/utils.py:222:def select_shallow_thinking_agent(provider) -> str:
./cli/utils.py:224:    return _select_model(provider, "quick")
./cli/utils.py:227:def select_deep_thinking_agent(provider) -> str:
./cli/utils.py:229:    return _select_model(provider, "deep")
./cli/utils.py:231:def select_llm_provider() -> tuple[str, str | None]:
./cli/utils.py:232:    """Select the LLM provider and its API endpoint."""
./cli/utils.py:233:    # (display_name, provider_key, base_url)
./cli/utils.py:235:        ("OpenAI", "openai", "https://api.openai.com/v1"),
./cli/utils.py:237:        ("Anthropic", "anthropic", "https://api.anthropic.com/"),
./cli/utils.py:239:        ("DeepSeek", "deepseek", "https://api.deepseek.com"),
./cli/utils.py:240:        ("Qwen", "qwen", "https://dashscope.aliyuncs.com/compatible-mode/v1"),
./cli/utils.py:241:        ("GLM", "glm", "https://open.bigmodel.cn/api/paas/v4/"),
./cli/utils.py:244:        ("Ollama", "ollama", "http://localhost:11434/v1"),
./cli/utils.py:250:            questionary.Choice(display, value=(provider_key, url))
./cli/utils.py:251:            for display, provider_key, url in PROVIDERS
./cli/utils.py:264:        console.print("\n[red]No LLM provider selected. Exiting...[/red]")
./cli/utils.py:267:    provider, url = choice
./cli/utils.py:268:    return provider, url
./cli/utils.py:271:def ask_openai_reasoning_effort() -> str:
./cli/utils.py:289:def ask_anthropic_effort() -> str | None:
./cli/utils.py:292:    Controls token usage and response thoroughness on Claude 4.5+ and 4.6 models.
./cli/utils.py:309:def ask_gemini_thinking_config() -> str | None:
./cli/utils.py:310:    """Ask for Gemini thinking configuration.
./cli/utils.py:313:    Client maps to appropriate API param based on model series.
./cli/main.py:7:from dotenv import load_dotenv
./cli/main.py:10:load_dotenv()
./cli/main.py:11:load_dotenv(".env.enterprise", override=False)
./cli/main.py:28:from tradingagents.default_config import DEFAULT_CONFIG
./cli/main.py:29:from cli.models import AnalystType
./cli/main.py:554:            "Step 6: LLM Provider", "Select your LLM provider"
./cli/main.py:557:    selected_llm_provider, backend_url = select_llm_provider()
./cli/main.py:565:    selected_shallow_thinker = select_shallow_thinking_agent(selected_llm_provider)
./cli/main.py:566:    selected_deep_thinker = select_deep_thinking_agent(selected_llm_provider)
./cli/main.py:568:    # Step 8: Provider-specific thinking configuration
./cli/main.py:571:    anthropic_effort = None
./cli/main.py:573:    provider_lower = selected_llm_provider.lower()
./cli/main.py:574:    if provider_lower == "google":
./cli/main.py:581:        thinking_level = ask_gemini_thinking_config()
./cli/main.py:582:    elif provider_lower == "openai":
./cli/main.py:589:        reasoning_effort = ask_openai_reasoning_effort()
./cli/main.py:590:    elif provider_lower == "anthropic":
./cli/main.py:597:        anthropic_effort = ask_anthropic_effort()
./cli/main.py:604:        "llm_provider": selected_llm_provider.lower(),
./cli/main.py:609:        "openai_reasoning_effort": reasoning_effort,
./cli/main.py:610:        "anthropic_effort": anthropic_effort,
./cli/main.py:933:    # Create config with selected research depth
./cli/main.py:934:    config = DEFAULT_CONFIG.copy()
./cli/main.py:935:    config["max_debate_rounds"] = selections["research_depth"]
./cli/main.py:936:    config["max_risk_discuss_rounds"] = selections["research_depth"]
./cli/main.py:937:    config["quick_think_llm"] = selections["shallow_thinker"]
./cli/main.py:938:    config["deep_think_llm"] = selections["deep_thinker"]
./cli/main.py:939:    config["backend_url"] = selections["backend_url"]
./cli/main.py:940:    config["llm_provider"] = selections["llm_provider"].lower()
./cli/main.py:941:    # Provider-specific thinking configuration
./cli/main.py:942:    config["google_thinking_level"] = selections.get("google_thinking_level")
./cli/main.py:943:    config["openai_reasoning_effort"] = selections.get("openai_reasoning_effort")
./cli/main.py:944:    config["anthropic_effort"] = selections.get("anthropic_effort")
./cli/main.py:945:    config["output_language"] = selections.get("output_language", "English")
./cli/main.py:946:    config["checkpoint_enabled"] = checkpoint
./cli/main.py:958:        config=config,
./cli/main.py:970:    results_dir = Path(config["results_dir"]) / selections["ticker"] / selections["analysis_date"]
./cli/main.py:1050:        # Pass callbacks to graph config for tool execution tracking
./cli/announcements.py:6:from cli.config import CLI_CONFIG
./cli/announcements.py:10:    """Fetch announcements from endpoint. Returns dict with announcements and settings."""
./cli/stats_handler.py:30:    def on_chat_model_start(
./cli/stats_handler.py:36:        """Increment LLM call counter when a chat model starts."""
./test.py:2:from tradingagents.dataflows.y_finance import get_YFin_data_online, get_stock_stats_indicators_window, get_balance_sheet as get_yfinance_balance_sheet, get_cashflow as get_yfinance_cashflow, get_income_statement as get_yfinance_income_statement, get_insider_transactions as get_yfinance_insider_transactions
./tradingagents/graph/checkpointer.py:58:        config = {"configurable": {"thread_id": tid}}
./tradingagents/graph/checkpointer.py:59:        cp = saver.get_tuple(config)
./tradingagents/graph/trading_graph.py:10:import yfinance as yf
./tradingagents/graph/trading_graph.py:19:from tradingagents.default_config import DEFAULT_CONFIG
./tradingagents/graph/trading_graph.py:27:from tradingagents.dataflows.config import set_config
./tradingagents/graph/trading_graph.py:57:        config: Dict[str, Any] = None,
./tradingagents/graph/trading_graph.py:65:            config: Configuration dictionary. If None, uses default config
./tradingagents/graph/trading_graph.py:69:        self.config = config or DEFAULT_CONFIG
./tradingagents/graph/trading_graph.py:72:        # Update the interface's config
./tradingagents/graph/trading_graph.py:73:        set_config(self.config)
./tradingagents/graph/trading_graph.py:76:        os.makedirs(self.config["data_cache_dir"], exist_ok=True)
./tradingagents/graph/trading_graph.py:77:        os.makedirs(self.config["results_dir"], exist_ok=True)
./tradingagents/graph/trading_graph.py:79:        # Initialize LLMs with provider-specific thinking configuration
./tradingagents/graph/trading_graph.py:80:        llm_kwargs = self._get_provider_kwargs()
./tradingagents/graph/trading_graph.py:87:            provider=self.config["llm_provider"],
./tradingagents/graph/trading_graph.py:88:            model=self.config["deep_think_llm"],
./tradingagents/graph/trading_graph.py:89:            base_url=self.config.get("backend_url"),
./tradingagents/graph/trading_graph.py:93:            provider=self.config["llm_provider"],
./tradingagents/graph/trading_graph.py:94:            model=self.config["quick_think_llm"],
./tradingagents/graph/trading_graph.py:95:            base_url=self.config.get("backend_url"),
./tradingagents/graph/trading_graph.py:102:        self.memory_log = TradingMemoryLog(self.config)
./tradingagents/graph/trading_graph.py:109:            max_debate_rounds=self.config["max_debate_rounds"],
./tradingagents/graph/trading_graph.py:110:            max_risk_discuss_rounds=self.config["max_risk_discuss_rounds"],
./tradingagents/graph/trading_graph.py:133:    def _get_provider_kwargs(self) -> Dict[str, Any]:
./tradingagents/graph/trading_graph.py:134:        """Get provider-specific kwargs for LLM client creation."""
./tradingagents/graph/trading_graph.py:136:        provider = self.config.get("llm_provider", "").lower()
./tradingagents/graph/trading_graph.py:138:        if provider == "google":
./tradingagents/graph/trading_graph.py:139:            thinking_level = self.config.get("google_thinking_level")
./tradingagents/graph/trading_graph.py:143:        elif provider == "openai":
./tradingagents/graph/trading_graph.py:144:            reasoning_effort = self.config.get("openai_reasoning_effort")
./tradingagents/graph/trading_graph.py:148:        elif provider == "anthropic":
./tradingagents/graph/trading_graph.py:149:            effort = self.config.get("anthropic_effort")
./tradingagents/graph/trading_graph.py:268:        When ``checkpoint_enabled`` is set in config, the graph is recompiled
./tradingagents/graph/trading_graph.py:278:        if self.config.get("checkpoint_enabled"):
./tradingagents/graph/trading_graph.py:280:                self.config["data_cache_dir"], company_name
./tradingagents/graph/trading_graph.py:286:                self.config["data_cache_dir"], company_name, str(trade_date)
./tradingagents/graph/trading_graph.py:313:        if self.config.get("checkpoint_enabled"):
./tradingagents/graph/trading_graph.py:315:            args.setdefault("config", {}).setdefault("configurable", {})["thread_id"] = tid
./tradingagents/graph/trading_graph.py:343:        if self.config.get("checkpoint_enabled"):
./tradingagents/graph/trading_graph.py:345:                self.config["data_cache_dir"], company_name, str(trade_date)
./tradingagents/graph/trading_graph.py:385:        directory = Path(self.config["results_dir"]) / safe_ticker / "TradingAgentsStrategy_logs"
./tradingagents/graph/conditional_logic.py:10:        """Initialize with configuration parameters."""
./tradingagents/graph/setup.py:14:    """Handles the setup and configuration of the agent graph."""
./tradingagents/graph/propagation.py:15:        """Initialize with configuration parameters."""
./tradingagents/graph/propagation.py:64:        config = {"recursion_limit": self.max_recur_limit}
./tradingagents/graph/propagation.py:66:            config["callbacks"] = callbacks
./tradingagents/graph/propagation.py:69:            "config": config,
./tradingagents/agents/managers/portfolio_manager.py:7:today.  When a provider does not expose structured output, the agent falls
./tradingagents/agents/utils/fundamental_data_tools.py:13:    Uses the configured fundamental_data vendor.
./tradingagents/agents/utils/fundamental_data_tools.py:31:    Uses the configured fundamental_data vendor.
./tradingagents/agents/utils/fundamental_data_tools.py:50:    Uses the configured fundamental_data vendor.
./tradingagents/agents/utils/fundamental_data_tools.py:69:    Uses the configured fundamental_data vendor.
./tradingagents/agents/utils/memory.py:19:    def __init__(self, config: dict = None):
./tradingagents/agents/utils/memory.py:20:        cfg = config or {}
./tradingagents/agents/utils/agent_utils.py:24:    """Return a prompt instruction for the configured output language.
./tradingagents/agents/utils/agent_utils.py:30:    from tradingagents.dataflows.config import get_config
./tradingagents/agents/utils/agent_utils.py:31:    lang = get_config().get("output_language", "English")
./tradingagents/agents/utils/news_data_tools.py:13:    Uses the configured news_data vendor.
./tradingagents/agents/utils/news_data_tools.py:31:    Uses the configured news_data vendor.
./tradingagents/agents/utils/news_data_tools.py:47:    Uses the configured news_data vendor.
./tradingagents/agents/utils/structured.py:7:   so the model returns a typed Pydantic instance. If the provider does
./tradingagents/agents/utils/structured.py:8:   not support structured output (rare; mostly older Ollama models), the
./tradingagents/agents/utils/structured.py:12:   (malformed JSON from a weak model, transient provider issue), fall
./tradingagents/agents/utils/structured.py:41:            "%s: provider does not support with_structured_output (%s); "
./tradingagents/agents/utils/structured.py:58:    invocations, a list of message dicts for chat models that take that
./tradingagents/agents/utils/core_stock_tools.py:14:    Uses the configured core_stock_apis vendor.
./tradingagents/agents/utils/technical_indicators_tools.py:14:    Uses the configured technical_indicators vendor.
./tradingagents/agents/analysts/market_analyst.py:8:from tradingagents.dataflows.config import get_config
./tradingagents/agents/analysts/social_media_analyst.py:3:from tradingagents.dataflows.config import get_config
./tradingagents/agents/analysts/news_analyst.py:8:from tradingagents.dataflows.config import get_config
./tradingagents/agents/analysts/fundamentals_analyst.py:11:from tradingagents.dataflows.config import get_config
./tradingagents/agents/schemas.py:9:- Their outputs follow consistent section headers across runs and providers
./tradingagents/agents/schemas.py:10:- Each provider's native structured-output mode is used (json_schema for
./tradingagents/agents/schemas.py:12:- Schema field descriptions become the model's output instructions, freeing
./tradingagents/agents/schemas.py:174:    The model fills every field as part of its primary LLM call; no separate
./tradingagents/agents/schemas.py:175:    extraction pass is required. Field descriptions double as the model's
./tradingagents/dataflows/config.py:1:import tradingagents.default_config as default_config
./tradingagents/dataflows/config.py:4:# Use default config but allow it to be overridden
./tradingagents/dataflows/config.py:5:_config: Optional[Dict] = None
./tradingagents/dataflows/config.py:8:def initialize_config():
./tradingagents/dataflows/config.py:9:    """Initialize the configuration with default values."""
./tradingagents/dataflows/config.py:10:    global _config
./tradingagents/dataflows/config.py:11:    if _config is None:
./tradingagents/dataflows/config.py:12:        _config = default_config.DEFAULT_CONFIG.copy()
./tradingagents/dataflows/config.py:15:def set_config(config: Dict):
./tradingagents/dataflows/config.py:16:    """Update the configuration with custom values."""
./tradingagents/dataflows/config.py:17:    global _config
./tradingagents/dataflows/config.py:18:    if _config is None:
./tradingagents/dataflows/config.py:19:        _config = default_config.DEFAULT_CONFIG.copy()
./tradingagents/dataflows/config.py:20:    _config.update(config)
./tradingagents/dataflows/config.py:23:def get_config() -> Dict:
./tradingagents/dataflows/config.py:24:    """Get the current configuration."""
./tradingagents/dataflows/config.py:25:    if _config is None:
./tradingagents/dataflows/config.py:26:        initialize_config()
./tradingagents/dataflows/config.py:27:    return _config.copy()
./tradingagents/dataflows/config.py:30:# Initialize with default config
./tradingagents/dataflows/config.py:31:initialize_config()
./tradingagents/dataflows/interface.py:7:    get_fundamentals as get_yfinance_fundamentals,
./tradingagents/dataflows/interface.py:8:    get_balance_sheet as get_yfinance_balance_sheet,
./tradingagents/dataflows/interface.py:9:    get_cashflow as get_yfinance_cashflow,
./tradingagents/dataflows/interface.py:10:    get_income_statement as get_yfinance_income_statement,
./tradingagents/dataflows/interface.py:11:    get_insider_transactions as get_yfinance_insider_transactions,
./tradingagents/dataflows/interface.py:13:from .yfinance_news import get_news_yfinance, get_global_news_yfinance
./tradingagents/dataflows/interface.py:28:from .config import get_config
./tradingagents/dataflows/interface.py:64:    "yfinance",
./tradingagents/dataflows/interface.py:73:        "yfinance": get_YFin_data_online,
./tradingagents/dataflows/interface.py:78:        "yfinance": get_stock_stats_indicators_window,
./tradingagents/dataflows/interface.py:83:        "yfinance": get_yfinance_fundamentals,
./tradingagents/dataflows/interface.py:87:        "yfinance": get_yfinance_balance_sheet,
./tradingagents/dataflows/interface.py:91:        "yfinance": get_yfinance_cashflow,
./tradingagents/dataflows/interface.py:95:        "yfinance": get_yfinance_income_statement,
./tradingagents/dataflows/interface.py:100:        "yfinance": get_news_yfinance,
./tradingagents/dataflows/interface.py:103:        "yfinance": get_global_news_yfinance,
./tradingagents/dataflows/interface.py:108:        "yfinance": get_yfinance_insider_transactions,
./tradingagents/dataflows/interface.py:120:    """Get the configured vendor for a data category or specific tool method.
./tradingagents/dataflows/interface.py:121:    Tool-level configuration takes precedence over category-level.
./tradingagents/dataflows/interface.py:123:    config = get_config()
./tradingagents/dataflows/interface.py:125:    # Check tool-level configuration first (if method provided)
./tradingagents/dataflows/interface.py:127:        tool_vendors = config.get("tool_vendors", {})
./tradingagents/dataflows/interface.py:131:    # Fall back to category-level configuration
./tradingagents/dataflows/interface.py:132:    return config.get("data_vendors", {}).get(category, "default")
./tradingagents/dataflows/interface.py:137:    vendor_config = get_vendor(category, method)
./tradingagents/dataflows/interface.py:138:    primary_vendors = [v.strip() for v in vendor_config.split(',')]
./tradingagents/dataflows/stockstats_utils.py:5:import yfinance as yf
./tradingagents/dataflows/stockstats_utils.py:6:from yfinance.exceptions import YFRateLimitError
./tradingagents/dataflows/stockstats_utils.py:10:from .config import get_config
./tradingagents/dataflows/stockstats_utils.py:17:    """Execute a yfinance call with exponential backoff on rate limits.
./tradingagents/dataflows/stockstats_utils.py:19:    yfinance raises YFRateLimitError on HTTP 429 responses but does not
./tradingagents/dataflows/stockstats_utils.py:59:    config = get_config()
./tradingagents/dataflows/stockstats_utils.py:68:    os.makedirs(config["data_cache_dir"], exist_ok=True)
./tradingagents/dataflows/stockstats_utils.py:70:        config["data_cache_dir"],
./tradingagents/dataflows/stockstats_utils.py:99:    yfinance financial statements use fiscal period end dates as columns.
./tradingagents/dataflows/y_finance.py:5:import yfinance as yf
./tradingagents/dataflows/y_finance.py:250:    curr_date: Annotated[str, "current date (not used for yfinance)"] = None
./tradingagents/dataflows/y_finance.py:252:    """Get company fundamentals overview from yfinance."""
./tradingagents/dataflows/y_finance.py:310:    """Get balance sheet data from yfinance."""
./tradingagents/dataflows/y_finance.py:342:    """Get cash flow data from yfinance."""
./tradingagents/dataflows/y_finance.py:374:    """Get income statement data from yfinance."""
./tradingagents/dataflows/y_finance.py:404:    """Get insider transactions data from yfinance."""
./tradingagents/dataflows/utils.py:23:    escapes the configured cache, checkpoint, or results directory.
./tradingagents/dataflows/alpha_vantage_common.py:10:def get_api_key() -> str:
./tradingagents/dataflows/alpha_vantage_common.py:12:    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
./tradingagents/dataflows/alpha_vantage_common.py:13:    if not api_key:
./tradingagents/dataflows/alpha_vantage_common.py:14:        raise ValueError("ALPHA_VANTAGE_API_KEY environment variable is not set.")
./tradingagents/dataflows/alpha_vantage_common.py:15:    return api_key
./tradingagents/dataflows/alpha_vantage_common.py:52:        "apikey": get_api_key(),
./tradingagents/dataflows/yfinance_news.py:1:"""yfinance-based news data fetching functions."""
./tradingagents/dataflows/yfinance_news.py:3:import yfinance as yf
./tradingagents/dataflows/yfinance_news.py:11:    """Extract article data from yfinance news format (handles nested 'content' structure)."""
./tradingagents/dataflows/yfinance_news.py:17:        provider = content.get("provider", {})
./tradingagents/dataflows/yfinance_news.py:18:        publisher = provider.get("displayName", "Unknown")
./tradingagents/dataflows/yfinance_news.py:51:def get_news_yfinance(
./tradingagents/dataflows/yfinance_news.py:57:    Retrieve news for a specific stock ticker using yfinance.
./tradingagents/dataflows/yfinance_news.py:107:def get_global_news_yfinance(
./tradingagents/dataflows/yfinance_news.py:113:    Retrieve global/macro economic news using yfinance Search.
./tradingagents/default_config.py:14:    # LLM settings
./tradingagents/default_config.py:15:    "llm_provider": "openai",
./tradingagents/default_config.py:18:    # When None, each provider's client falls back to its own default endpoint
./tradingagents/default_config.py:19:    # (api.openai.com for OpenAI, generativelanguage.googleapis.com for Gemini, ...).
./tradingagents/default_config.py:20:    # The CLI overrides this per provider when the user picks one. Keeping a
./tradingagents/default_config.py:21:    # provider-specific URL here would leak (e.g. OpenAI's /v1 was previously
./tradingagents/default_config.py:24:    # Provider-specific thinking configuration
./tradingagents/default_config.py:26:    "openai_reasoning_effort": None,    # "medium", "high", "low"
./tradingagents/default_config.py:27:    "anthropic_effort": None,           # "high", "medium", "low"
./tradingagents/default_config.py:34:    # Debate and discussion settings
./tradingagents/default_config.py:38:    # Data vendor configuration
./tradingagents/default_config.py:39:    # Category-level configuration (default for all tools in category)
./tradingagents/default_config.py:41:        "core_stock_apis": "yfinance",       # Options: alpha_vantage, yfinance
./tradingagents/default_config.py:42:        "technical_indicators": "yfinance",  # Options: alpha_vantage, yfinance
./tradingagents/default_config.py:43:        "fundamental_data": "yfinance",      # Options: alpha_vantage, yfinance
./tradingagents/default_config.py:44:        "news_data": "yfinance",             # Options: alpha_vantage, yfinance
./tradingagents/default_config.py:46:    # Tool-level configuration (takes precedence over category-level)
./tradingagents/llm_clients/validators.py:1:"""Model name validators for each provider."""
./tradingagents/llm_clients/validators.py:3:from .model_catalog import get_known_models
./tradingagents/llm_clients/validators.py:7:    provider: models
./tradingagents/llm_clients/validators.py:8:    for provider, models in get_known_models().items()
./tradingagents/llm_clients/validators.py:9:    if provider not in ("ollama", "openrouter")
./tradingagents/llm_clients/validators.py:13:def validate_model(provider: str, model: str) -> bool:
./tradingagents/llm_clients/validators.py:14:    """Check if model name is valid for the given provider.
./tradingagents/llm_clients/validators.py:16:    For ollama, openrouter - any model is accepted.
./tradingagents/llm_clients/validators.py:18:    provider_lower = provider.lower()
./tradingagents/llm_clients/validators.py:20:    if provider_lower in ("ollama", "openrouter"):
./tradingagents/llm_clients/validators.py:23:    if provider_lower not in VALID_MODELS:
./tradingagents/llm_clients/validators.py:26:    return model in VALID_MODELS[provider_lower]
./tradingagents/llm_clients/base_client.py:9:    Multiple providers (OpenAI Responses API, Google Gemini 3) return content
./tradingagents/llm_clients/base_client.py:28:    def __init__(self, model: str, base_url: Optional[str] = None, **kwargs):
./tradingagents/llm_clients/base_client.py:29:        self.model = model
./tradingagents/llm_clients/base_client.py:33:    def get_provider_name(self) -> str:
./tradingagents/llm_clients/base_client.py:34:        """Return the provider name used in warning messages."""
./tradingagents/llm_clients/base_client.py:35:        provider = getattr(self, "provider", None)
./tradingagents/llm_clients/base_client.py:36:        if provider:
./tradingagents/llm_clients/base_client.py:37:            return str(provider)
./tradingagents/llm_clients/base_client.py:40:    def warn_if_unknown_model(self) -> None:
./tradingagents/llm_clients/base_client.py:41:        """Warn when the model is outside the known list for the provider."""
./tradingagents/llm_clients/base_client.py:42:        if self.validate_model():
./tradingagents/llm_clients/base_client.py:47:                f"Model '{self.model}' is not in the known model list for "
./tradingagents/llm_clients/base_client.py:48:                f"provider '{self.get_provider_name()}'. Continuing anyway."
./tradingagents/llm_clients/base_client.py:56:        """Return the configured LLM instance."""
./tradingagents/llm_clients/base_client.py:60:    def validate_model(self) -> bool:
./tradingagents/llm_clients/base_client.py:61:        """Validate that the model is supported by this client."""
./tradingagents/llm_clients/azure_client.py:4:from langchain_openai import AzureChatOpenAI
./tradingagents/llm_clients/azure_client.py:7:from .validators import validate_model
./tradingagents/llm_clients/azure_client.py:10:    "timeout", "max_retries", "api_key", "reasoning_effort",
./tradingagents/llm_clients/azure_client.py:18:    def invoke(self, input, config=None, **kwargs):
./tradingagents/llm_clients/azure_client.py:19:        return normalize_content(super().invoke(input, config, **kwargs))
./tradingagents/llm_clients/azure_client.py:26:        AZURE_OPENAI_API_KEY: API key
./tradingagents/llm_clients/azure_client.py:27:        AZURE_OPENAI_ENDPOINT: Endpoint URL (e.g. https://<resource>.openai.azure.com/)
./tradingagents/llm_clients/azure_client.py:32:    def __init__(self, model: str, base_url: Optional[str] = None, **kwargs):
./tradingagents/llm_clients/azure_client.py:33:        super().__init__(model, base_url, **kwargs)
./tradingagents/llm_clients/azure_client.py:36:        """Return configured AzureChatOpenAI instance."""
./tradingagents/llm_clients/azure_client.py:37:        self.warn_if_unknown_model()
./tradingagents/llm_clients/azure_client.py:40:            "model": self.model,
./tradingagents/llm_clients/azure_client.py:41:            "azure_deployment": os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME", self.model),
./tradingagents/llm_clients/azure_client.py:50:    def validate_model(self) -> bool:
./tradingagents/llm_clients/azure_client.py:51:        """Azure accepts any deployed model name."""
./tradingagents/llm_clients/factory.py:7:    "openai", "xai", "deepseek", "qwen", "glm", "ollama", "openrouter",
./tradingagents/llm_clients/factory.py:12:    provider: str,
./tradingagents/llm_clients/factory.py:13:    model: str,
./tradingagents/llm_clients/factory.py:17:    """Create an LLM client for the specified provider.
./tradingagents/llm_clients/factory.py:24:        provider: LLM provider name
./tradingagents/llm_clients/factory.py:25:        model: Model name/identifier
./tradingagents/llm_clients/factory.py:27:        **kwargs: Additional provider-specific arguments
./tradingagents/llm_clients/factory.py:33:        ValueError: If provider is not supported
./tradingagents/llm_clients/factory.py:35:    provider_lower = provider.lower()
./tradingagents/llm_clients/factory.py:37:    if provider_lower in _OPENAI_COMPATIBLE:
```

## 10. 入口文件 / CLI / 示例关键词扫描

```text
./tests/conftest.py:35:def mock_llm_client():
./tests/conftest.py:36:    client = MagicMock()
./tests/conftest.py:37:    client.get_llm.return_value = MagicMock()
./tests/conftest.py:39:        "tradingagents.llm_clients.factory.create_llm_client",
./tests/conftest.py:40:        return_value=client,
./tests/conftest.py:42:        yield client
./tests/test_model_validation.py:6:from tradingagents.llm_clients.base_client import BaseLLMClient
./tests/test_model_validation.py:7:from tradingagents.llm_clients.model_catalog import get_known_models
./tests/test_model_validation.py:8:from tradingagents.llm_clients.validators import validate_model
./tests/test_model_validation.py:26:    def test_cli_catalog_models_are_all_validator_approved(self):
./tests/test_model_validation.py:36:        client = DummyLLMClient("openai", "not-a-real-openai-model")
./tests/test_model_validation.py:40:            client.get_llm()
./tests/test_model_validation.py:48:            client = DummyLLMClient(provider, "custom-model-name")
./tests/test_model_validation.py:53:                    client.get_llm()
./tests/test_safe_ticker_component.py:51:if __name__ == "__main__":
./tests/test_safe_ticker_component.py:52:    unittest.main()
./tests/test_checkpoint_resume.py:146:if __name__ == "__main__":
./tests/test_checkpoint_resume.py:147:    unittest.main()
./tests/test_ticker_symbol_handling.py:5:from cli.utils import normalize_ticker_symbol
./tests/test_ticker_symbol_handling.py:20:if __name__ == "__main__":
./tests/test_ticker_symbol_handling.py:21:    unittest.main()
./tests/test_google_api_key.py:6:from tradingagents.llm_clients.google_client import GoogleClient
./tests/test_google_api_key.py:13:    @patch("tradingagents.llm_clients.google_client.NormalizedChatGoogleGenerativeAI")
./tests/test_google_api_key.py:24:                client = GoogleClient("gemini-2.5-flash", **kwargs)
./tests/test_google_api_key.py:25:                client.get_llm()
./tests/test_google_api_key.py:30:if __name__ == "__main__":
./tests/test_google_api_key.py:31:    unittest.main()
./tests/test_deepseek_reasoning.py:19:from tradingagents.llm_clients.openai_client import (
./tests/test_deepseek_reasoning.py:56:    def _client(self):
./tests/test_deepseek_reasoning.py:67:        client = self._client()
./tests/test_deepseek_reasoning.py:68:        result = client._create_chat_result(
./tests/test_deepseek_reasoning.py:91:        client = self._client()
./tests/test_deepseek_reasoning.py:97:        payload = client._get_request_payload([prior, new_user])
./tests/test_deepseek_reasoning.py:106:        client = self._client()
./tests/test_deepseek_reasoning.py:112:        payload = client._get_request_payload(prompt_value)
./tests/test_deepseek_reasoning.py:125:        client = DeepSeekChatOpenAI(
./tests/test_deepseek_reasoning.py:136:            client.with_structured_output(_Sample)
./tests/test_deepseek_reasoning.py:140:        client = DeepSeekChatOpenAI(
./tests/test_deepseek_reasoning.py:152:        wrapped = client.with_structured_output(_Sample)
./cli/utils.py:6:from cli.models import AnalystType
./cli/utils.py:7:from tradingagents.llm_clients.model_catalog import get_model_options
./cli/main.py:3:import typer
./cli/main.py:29:from cli.models import AnalystType
./cli/main.py:30:from cli.utils import *
./cli/main.py:31:from cli.announcements import fetch_announcements, display_announcements
./cli/main.py:32:from cli.stats_handler import StatsCallbackHandler
./cli/main.py:36:app = typer.Typer(
./cli/main.py:506:            "Enter the exact ticker symbol to analyze, including exchange suffix when needed (examples: SPY, CNC.TO, 7203.T, 0700.HK)",
./cli/main.py:617:    return typer.prompt("", default="SPY")
./cli/main.py:623:        date_str = typer.prompt(
./cli/main.py:1178:    save_choice = typer.prompt("Save report?", default="Y").strip().upper()
./cli/main.py:1182:        save_path_str = typer.prompt(
./cli/main.py:1195:    display_choice = typer.prompt("\nDisplay full report on screen?", default="Y").strip().upper()
./cli/main.py:1202:    checkpoint: bool = typer.Option(
./cli/main.py:1207:    clear_checkpoints: bool = typer.Option(
./cli/main.py:1220:if __name__ == "__main__":
./cli/announcements.py:6:from cli.config import CLI_CONFIG
./tradingagents/graph/trading_graph.py:16:from tradingagents.llm_clients import create_llm_client
./tradingagents/graph/trading_graph.py:86:        deep_client = create_llm_client(
./tradingagents/graph/trading_graph.py:92:        quick_client = create_llm_client(
./tradingagents/graph/trading_graph.py:99:        self.deep_thinking_llm = deep_client.get_llm()
./tradingagents/graph/trading_graph.py:100:        self.quick_thinking_llm = quick_client.get_llm()
./tradingagents/graph/trading_graph.py:134:        """Get provider-specific kwargs for LLM client creation."""
./tradingagents/agents/researchers/bull_researcher.py:31:Use this information to deliver a compelling bull argument, refute the bear's concerns, and engage in a dynamic debate that demonstrates the strengths of the bull position.
./tradingagents/agents/researchers/bear_researcher.py:20:- Competitive Weaknesses: Emphasize vulnerabilities such as weaker market positioning, declining innovation, or threats from competitors.
./tradingagents/agents/researchers/bear_researcher.py:33:Use this information to deliver a compelling bear argument, refute the bull's claims, and engage in a dynamic debate that demonstrates the risks and weaknesses of investing in the stock.
./tradingagents/agents/risk_mgmt/conservative_debator.py:31:Engage by questioning their optimism and emphasizing the potential downsides they may have overlooked. Address each of their counterpoints to showcase why a conservative stance is ultimately the safest path for the firm's assets. Focus on debating and critiquing their arguments to demonstrate the strength of a low-risk strategy over their approaches. Output conversationally as if you are speaking without any special formatting."""
./tradingagents/agents/risk_mgmt/aggressive_debator.py:23:Your task is to create a compelling case for the trader's decision by questioning and critiquing the conservative and neutral stances to demonstrate why your high-reward perspective offers the best path forward. Incorporate insights from the following sources into your arguments:
./tradingagents/agents/utils/structured.py:16:all three agents log the same warnings when fallback fires.
./tradingagents/dataflows/alpha_vantage_stock.py:14:        symbol: The name of the equity. For example: symbol=IBM
./tradingagents/dataflows/yfinance_news.py:20:        # Get URL from canonicalUrl or clickThroughUrl
./tradingagents/dataflows/yfinance_news.py:21:        url_obj = content.get("canonicalUrl") or content.get("clickThroughUrl") or {}
./tradingagents/default_config.py:18:    # When None, each provider's client falls back to its own default endpoint
./tradingagents/llm_clients/base_client.py:26:    """Abstract base class for LLM clients."""
./tradingagents/llm_clients/base_client.py:61:        """Validate that the model is supported by this client."""
./tradingagents/llm_clients/azure_client.py:6:from .base_client import BaseLLMClient, normalize_content
./tradingagents/llm_clients/azure_client.py:11:    "callbacks", "http_client", "http_async_client",
./tradingagents/llm_clients/__init__.py:1:from .base_client import BaseLLMClient
./tradingagents/llm_clients/__init__.py:2:from .factory import create_llm_client
./tradingagents/llm_clients/__init__.py:4:__all__ = ["BaseLLMClient", "create_llm_client"]
./tradingagents/llm_clients/factory.py:3:from .base_client import BaseLLMClient
./tradingagents/llm_clients/factory.py:11:def create_llm_client(
./tradingagents/llm_clients/factory.py:17:    """Create an LLM client for the specified provider.
./tradingagents/llm_clients/factory.py:38:        from .openai_client import OpenAIClient
./tradingagents/llm_clients/factory.py:42:        from .anthropic_client import AnthropicClient
./tradingagents/llm_clients/factory.py:46:        from .google_client import GoogleClient
./tradingagents/llm_clients/factory.py:50:        from .azure_client import AzureOpenAIClient
./tradingagents/llm_clients/google_client.py:5:from .base_client import BaseLLMClient, normalize_content
./tradingagents/llm_clients/google_client.py:34:        for key in ("timeout", "max_retries", "callbacks", "http_client", "http_async_client"):
./tradingagents/llm_clients/openai_client.py:7:from .base_client import BaseLLMClient, normalize_content
./tradingagents/llm_clients/openai_client.py:53:    """DeepSeek-specific overrides on top of the OpenAI-compatible client.
./tradingagents/llm_clients/openai_client.py:109:    "api_key", "callbacks", "http_client", "http_async_client",
./tradingagents/llm_clients/openai_client.py:148:        # client (e.g. a corporate proxy) takes precedence over the
./tradingagents/llm_clients/anthropic_client.py:5:from .base_client import BaseLLMClient, normalize_content
./tradingagents/llm_clients/anthropic_client.py:10:    "callbacks", "http_client", "http_async_client", "effort",
./scripts/smoke_structured_output.py:23:import argparse
./scripts/smoke_structured_output.py:31:from tradingagents.llm_clients import create_llm_client
./scripts/smoke_structured_output.py:107:def main() -> int:
./scripts/smoke_structured_output.py:108:    parser = argparse.ArgumentParser(description=__doc__)
./scripts/smoke_structured_output.py:122:    # Build the LLM clients via the framework's factory.
./scripts/smoke_structured_output.py:123:    deep_client = create_llm_client(provider=args.provider, model=deep_model)
./scripts/smoke_structured_output.py:124:    quick_client = create_llm_client(provider=args.provider, model=quick_model)
./scripts/smoke_structured_output.py:125:    deep_llm = deep_client.get_llm()
./scripts/smoke_structured_output.py:126:    quick_llm = quick_client.get_llm()
./scripts/smoke_structured_output.py:175:if __name__ == "__main__":
./scripts/smoke_structured_output.py:176:    sys.exit(main())
```

## 11. 疑似核心源码文件预览


### tests/test_checkpoint_resume.py

```python
"""Test checkpoint resume: crash mid-analysis, re-run resumes from last node."""

import sqlite3
import tempfile
import unittest
from pathlib import Path
from typing import TypedDict

from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import END, StateGraph

from tradingagents.graph.checkpointer import (
    checkpoint_step,
    clear_checkpoint,
    get_checkpointer,
    has_checkpoint,
    thread_id,
)

# Mutable flag to simulate crash on first run
_should_crash = False


class _SimpleState(TypedDict):
    count: int


def _node_a(state: _SimpleState) -> dict:
    return {"count": state["count"] + 1}


def _node_b(state: _SimpleState) -> dict:
    if _should_crash:
        raise RuntimeError("simulated mid-analysis crash")
    return {"count": state["count"] + 10}


def _build_graph() -> StateGraph:
    builder = StateGraph(_SimpleState)
    builder.add_node("analyst", _node_a)
    builder.add_node("trader", _node_b)
    builder.set_entry_point("analyst")
    builder.add_edge("analyst", "trader")
    builder.add_edge("trader", END)
    return builder


class TestCheckpointResume(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        self.ticker = "TEST"
        self.date = "2026-04-20"

    def test_crash_and_resume(self):
        """Crash at 'trader' node, then resume from checkpoint."""
        global _should_crash
        builder = _build_graph()
        tid = thread_id(self.ticker, self.date)
        cfg = {"configurable": {"thread_id": tid}}

        # Run 1: crash at trader node
        _should_crash = True
        with get_checkpointer(self.tmpdir, self.ticker) as saver:
            graph = builder.compile(checkpointer=saver)
            with self.assertRaises(RuntimeError):
                graph.invoke({"count": 0}, config=cfg)

        # Checkpoint should exist at step 1 (analyst completed)
        self.assertTrue(has_checkpoint(self.tmpdir, self.ticker, self.date))
        step = checkpoint_step(self.tmpdir, self.ticker, self.date)
        self.assertEqual(step, 1)

        # Run 2: resume — trader succeeds this time
        _should_crash = False
        with get_checkpointer(self.tmpdir, self.ticker) as saver:
            graph = builder.compile(checkpointer=saver)
            result = graph.invoke(None, config=cfg)

        # analyst added 1, trader added 10 → 11
        self.assertEqual(result["count"], 11)

    def test_clear_checkpoint_allows_fresh_start(self):
        """After clearing, the graph starts from scratch."""
        global _should_crash
        builder = _build_graph()
        tid = thread_id(self.ticker, self.date)
        cfg = {"configurable": {"thread_id": tid}}

        # Create a checkpoint by crashing
        _should_crash = True
        with get_checkpointer(self.tmpdir, self.ticker) as saver:
            graph = builder.compile(checkpointer=saver)
            with self.assertRaises(RuntimeError):
                graph.invoke({"count": 0}, config=cfg)

        self.assertTrue(has_checkpoint(self.tmpdir, self.ticker, self.date))

        # Clear it
        clear_checkpoint(self.tmpdir, self.ticker, self.date)
        self.assertFalse(has_checkpoint(self.tmpdir, self.ticker, self.date))

        # Fresh run succeeds from scratch
        _should_crash = False
        with get_checkpointer(self.tmpdir, self.ticker) as saver:
            graph = builder.compile(checkpointer=saver)
            result = graph.invoke({"count": 0}, config=cfg)

        self.assertEqual(result["count"], 11)


    def test_different_date_starts_fresh(self):
        """A different date must NOT resume from an existing checkpoint."""
        global _should_crash
        builder = _build_graph()
        date2 = "2026-04-21"

        # Run with date1 — crash to leave a checkpoint
        _should_crash = True
        tid1 = thread_id(self.ticker, self.date)
        with get_checkpointer(self.tmpdir, self.ticker) as saver:
            graph = builder.compile(checkpointer=saver)
            with self.assertRaises(RuntimeError):
                graph.invoke({"count": 0}, config={"configurable": {"thread_id": tid1}})

        self.assertTrue(has_checkpoint(self.tmpdir, self.ticker, self.date))

        # date2 should have no checkpoint
        self.assertFalse(has_checkpoint(self.tmpdir, self.ticker, date2))

        # Run with date2 — should start fresh and succeed
        _should_crash = False
        tid2 = thread_id(self.ticker, date2)
        self.assertNotEqual(tid1, tid2)

        with get_checkpointer(self.tmpdir, self.ticker) as saver:
            graph = builder.compile(checkpointer=saver)
            result = graph.invoke({"count": 0}, config={"configurable": {"thread_id": tid2}})

        # Fresh run: analyst +1, trader +10 = 11
        self.assertEqual(result["count"], 11)

        # Original date checkpoint still exists (untouched)
        self.assertTrue(has_checkpoint(self.tmpdir, self.ticker, self.date))


if __name__ == "__main__":
    unittest.main()
```

### tests/test_memory_log.py

```python
"""Tests for TradingMemoryLog — storage, deferred reflection, PM injection, legacy removal."""

import pytest
import pandas as pd
from unittest.mock import MagicMock, patch

from tradingagents.agents.utils.memory import TradingMemoryLog
from tradingagents.agents.schemas import PortfolioDecision, PortfolioRating
from tradingagents.graph.reflection import Reflector
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.graph.propagation import Propagator
from tradingagents.agents.managers.portfolio_manager import create_portfolio_manager

_SEP = TradingMemoryLog._SEPARATOR

DECISION_BUY = "Rating: Buy\nEnter at $189-192, 6% portfolio cap."
DECISION_OVERWEIGHT = (
    "Rating: Overweight\n"
    "Executive Summary: Moderate position, await confirmation.\n"
    "Investment Thesis: Strong fundamentals but near-term headwinds."
)
DECISION_SELL = "Rating: Sell\nExit position immediately."
DECISION_NO_RATING = (
    "Executive Summary: Complex situation with multiple competing factors.\n"
    "Investment Thesis: No clear directional signal at this time."
)


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def make_log(tmp_path, filename="trading_memory.md"):
    config = {"memory_log_path": str(tmp_path / filename)}
    return TradingMemoryLog(config)


def _seed_completed(tmp_path, ticker, date, decision_text, reflection_text, filename="trading_memory.md"):
    """Write a completed entry directly to file, bypassing the API."""
    entry = (
        f"[{date} | {ticker} | Buy | +1.0% | +0.5% | 5d]\n\n"
        f"DECISION:\n{decision_text}\n\n"
        f"REFLECTION:\n{reflection_text}"
        + _SEP
    )
    with open(tmp_path / filename, "a", encoding="utf-8") as f:
        f.write(entry)


def _resolve_entry(log, ticker, date, decision, reflection="Good call."):
    """Store a decision then immediately resolve it via the API."""
    log.store_decision(ticker, date, decision)
    log.update_with_outcome(ticker, date, 0.05, 0.02, 5, reflection)


def _price_df(prices):
    """Minimal DataFrame matching yfinance .history() output shape."""
    return pd.DataFrame({"Close": prices})


def _make_pm_state(past_context=""):
    """Minimal AgentState dict for portfolio_manager_node."""
    return {
        "company_of_interest": "NVDA",
        "past_context": past_context,
        "risk_debate_state": {
            "history": "Risk debate history.",
            "aggressive_history": "",
            "conservative_history": "",
            "neutral_history": "",
            "judge_decision": "",
            "current_aggressive_response": "",
            "current_conservative_response": "",
            "current_neutral_response": "",
            "count": 1,
        },
        "market_report": "Market report.",
        "sentiment_report": "Sentiment report.",
        "news_report": "News report.",
        "fundamentals_report": "Fundamentals report.",
        "investment_plan": "Research plan.",
        "trader_investment_plan": "Trader plan.",
    }


def _structured_pm_llm(captured: dict, decision: PortfolioDecision | None = None):
    """Build a MagicMock LLM whose with_structured_output binding captures the
    prompt and returns a real PortfolioDecision (so render_pm_decision works).
    """
    if decision is None:
        decision = PortfolioDecision(
            rating=PortfolioRating.HOLD,
            executive_summary="Hold the position; await catalyst.",
            investment_thesis="Balanced view; neither side carried the debate.",
        )
    structured = MagicMock()
    structured.invoke.side_effect = lambda prompt: (
        captured.__setitem__("prompt", prompt) or decision
    )
    llm = MagicMock()
    llm.with_structured_output.return_value = structured
    return llm


# ---------------------------------------------------------------------------
# Core: storage and read path
# ---------------------------------------------------------------------------

class TestTradingMemoryLogCore:

    def test_store_creates_file(self, tmp_path):
        log = make_log(tmp_path)
        assert not (tmp_path / "trading_memory.md").exists()
        log.store_decision("NVDA", "2026-01-10", DECISION_BUY)
        assert (tmp_path / "trading_memory.md").exists()

    def test_store_appends_not_overwrites(self, tmp_path):
        log = make_log(tmp_path)
        log.store_decision("NVDA", "2026-01-10", DECISION_BUY)
        log.store_decision("AAPL", "2026-01-11", DECISION_OVERWEIGHT)
        entries = log.load_entries()
        assert len(entries) == 2
        assert entries[0]["ticker"] == "NVDA"
        assert entries[1]["ticker"] == "AAPL"

    def test_store_decision_idempotent(self, tmp_path):
        """Calling store_decision twice with same (ticker, date) stores only one entry."""
        log = make_log(tmp_path)
        log.store_decision("NVDA", "2026-01-10", DECISION_BUY)
        log.store_decision("NVDA", "2026-01-10", DECISION_BUY)
        assert len(log.load_entries()) == 1

    def test_batch_update_resolves_multiple_entries(self, tmp_path):
        """batch_update_with_outcomes resolves multiple pending entries in one write."""
        log = make_log(tmp_path)
        log.store_decision("NVDA", "2026-01-05", DECISION_BUY)
        log.store_decision("NVDA", "2026-01-12", DECISION_SELL)

        updates = [
            {"ticker": "NVDA", "trade_date": "2026-01-05",
             "raw_return": 0.05, "alpha_return": 0.02, "holding_days": 5,
             "reflection": "First correct."},
            {"ticker": "NVDA", "trade_date": "2026-01-12",
             "raw_return": -0.03, "alpha_return": -0.01, "holding_days": 5,
             "reflection": "Second correct."},
        ]
        log.batch_update_with_outcomes(updates)

        entries = log.load_entries()
        assert len(entries) == 2
        assert all(not e["pending"] for e in entries)
        assert entries[0]["reflection"] == "First correct."
        assert entries[1]["reflection"] == "Second correct."

    def test_pending_tag_format(self, tmp_path):
        log = make_log(tmp_path)
        log.store_decision("NVDA", "2026-01-10", DECISION_BUY)
        text = (tmp_path / "trading_memory.md").read_text(encoding="utf-8")
        assert "[2026-01-10 | NVDA | Buy | pending]" in text

    # Rating parsing

    def test_rating_parsed_buy(self, tmp_path):
        log = make_log(tmp_path)
        log.store_decision("NVDA", "2026-01-10", DECISION_BUY)
        assert log.load_entries()[0]["rating"] == "Buy"

    def test_rating_parsed_overweight(self, tmp_path):
        log = make_log(tmp_path)
        log.store_decision("AAPL", "2026-01-11", DECISION_OVERWEIGHT)
        assert log.load_entries()[0]["rating"] == "Overweight"

    def test_rating_fallback_hold(self, tmp_path):
        log = make_log(tmp_path)
        log.store_decision("MSFT", "2026-01-12", DECISION_NO_RATING)
        assert log.load_entries()[0]["rating"] == "Hold"

    def test_rating_priority_over_prose(self, tmp_path):
        """'Rating: X' label wins even when an opposing rating word appears earlier in prose."""
        decision = (

# ... 文件较长，已截断。总行数：773
```

### tests/test_structured_agents.py

```python
"""Tests for structured-output agents (Trader and Research Manager).

The Portfolio Manager has its own coverage in tests/test_memory_log.py
(which exercises the full memory-log → PM injection cycle).  This file
covers the parallel schemas, render functions, and graceful-fallback
behavior we added for the Trader and Research Manager so all three
decision-making agents share the same shape.
"""

from unittest.mock import MagicMock

import pytest

from tradingagents.agents.managers.research_manager import create_research_manager
from tradingagents.agents.schemas import (
    PortfolioRating,
    ResearchPlan,
    TraderAction,
    TraderProposal,
    render_research_plan,
    render_trader_proposal,
)
from tradingagents.agents.trader.trader import create_trader


# ---------------------------------------------------------------------------
# Render functions
# ---------------------------------------------------------------------------


@pytest.mark.unit
class TestRenderTraderProposal:
    def test_minimal_required_fields(self):
        p = TraderProposal(action=TraderAction.HOLD, reasoning="Balanced setup; no edge.")
        md = render_trader_proposal(p)
        assert "**Action**: Hold" in md
        assert "**Reasoning**: Balanced setup; no edge." in md
        # The trailing FINAL TRANSACTION PROPOSAL line is preserved for the
        # analyst stop-signal text and any external code that greps for it.
        assert "FINAL TRANSACTION PROPOSAL: **HOLD**" in md

    def test_optional_fields_included_when_present(self):
        p = TraderProposal(
            action=TraderAction.BUY,
            reasoning="Strong technicals + fundamentals.",
            entry_price=189.5,
            stop_loss=178.0,
            position_sizing="6% of portfolio",
        )
        md = render_trader_proposal(p)
        assert "**Action**: Buy" in md
        assert "**Entry Price**: 189.5" in md
        assert "**Stop Loss**: 178.0" in md
        assert "**Position Sizing**: 6% of portfolio" in md
        assert "FINAL TRANSACTION PROPOSAL: **BUY**" in md

    def test_optional_fields_omitted_when_absent(self):
        p = TraderProposal(action=TraderAction.SELL, reasoning="Guidance cut.")
        md = render_trader_proposal(p)
        assert "Entry Price" not in md
        assert "Stop Loss" not in md
        assert "Position Sizing" not in md
        assert "FINAL TRANSACTION PROPOSAL: **SELL**" in md


@pytest.mark.unit
class TestRenderResearchPlan:
    def test_required_fields(self):
        p = ResearchPlan(
            recommendation=PortfolioRating.OVERWEIGHT,
            rationale="Bull case carried; tailwinds intact.",
            strategic_actions="Build position over two weeks; cap at 5%.",
        )
        md = render_research_plan(p)
        assert "**Recommendation**: Overweight" in md
        assert "**Rationale**: Bull case carried" in md
        assert "**Strategic Actions**: Build position" in md

    def test_all_5_tier_ratings_render(self):
        for rating in PortfolioRating:
            p = ResearchPlan(
                recommendation=rating,
                rationale="r",
                strategic_actions="s",
            )
            md = render_research_plan(p)
            assert f"**Recommendation**: {rating.value}" in md


# ---------------------------------------------------------------------------
# Trader agent: structured happy path + fallback
# ---------------------------------------------------------------------------


def _make_trader_state():
    return {
        "company_of_interest": "NVDA",
        "investment_plan": "**Recommendation**: Buy\n**Rationale**: ...\n**Strategic Actions**: ...",
    }


def _structured_trader_llm(captured: dict, proposal: TraderProposal | None = None):
    """Build a MagicMock LLM whose with_structured_output binding captures the
    prompt and returns a real TraderProposal so render_trader_proposal works.
    """
    if proposal is None:
        proposal = TraderProposal(
            action=TraderAction.BUY,
            reasoning="Strong setup.",
        )
    structured = MagicMock()
    structured.invoke.side_effect = lambda prompt: (
        captured.__setitem__("prompt", prompt) or proposal
    )
    llm = MagicMock()
    llm.with_structured_output.return_value = structured
    return llm


@pytest.mark.unit
class TestTraderAgent:
    def test_structured_path_produces_rendered_markdown(self):
        captured = {}
        proposal = TraderProposal(
            action=TraderAction.BUY,
            reasoning="AI capex cycle intact; institutional flows constructive.",
            entry_price=189.5,
            stop_loss=178.0,
            position_sizing="6% of portfolio",
        )
        llm = _structured_trader_llm(captured, proposal)
        trader = create_trader(llm)
        result = trader(_make_trader_state())
        plan = result["trader_investment_plan"]
        assert "**Action**: Buy" in plan
        assert "**Entry Price**: 189.5" in plan
        assert "FINAL TRANSACTION PROPOSAL: **BUY**" in plan
        # The same rendered markdown is also added to messages for downstream agents.
        assert plan in result["messages"][0].content

    def test_prompt_includes_investment_plan(self):
        captured = {}
        llm = _structured_trader_llm(captured)
        trader = create_trader(llm)
        trader(_make_trader_state())
        # The investment plan is in the user message of the captured prompt.
        prompt = captured["prompt"]
        assert any("Proposed Investment Plan" in m["content"] for m in prompt)

    def test_falls_back_to_freetext_when_structured_unavailable(self):
        plain_response = (
            "**Action**: Sell\n\nGuidance cut hits margins.\n\n"
            "FINAL TRANSACTION PROPOSAL: **SELL**"
        )
        llm = MagicMock()
        llm.with_structured_output.side_effect = NotImplementedError("provider unsupported")
        llm.invoke.return_value = MagicMock(content=plain_response)
        trader = create_trader(llm)
        result = trader(_make_trader_state())
        assert result["trader_investment_plan"] == plain_response


# ---------------------------------------------------------------------------
# Research Manager agent: structured happy path + fallback
# ---------------------------------------------------------------------------


def _make_rm_state():
    return {
        "company_of_interest": "NVDA",
        "investment_debate_state": {
            "history": "Bull and bear arguments here.",
            "bull_history": "Bull says...",
            "bear_history": "Bear says...",
            "current_response": "",
            "judge_decision": "",
            "count": 1,
        },
    }


# ... 文件较长，已截断。总行数：232
```

### tradingagents/__init__.py

```python
```

### tradingagents/default_config.py

```python
import os

_TRADINGAGENTS_HOME = os.path.join(os.path.expanduser("~"), ".tradingagents")

DEFAULT_CONFIG = {
    "project_dir": os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
    "results_dir": os.getenv("TRADINGAGENTS_RESULTS_DIR", os.path.join(_TRADINGAGENTS_HOME, "logs")),
    "data_cache_dir": os.getenv("TRADINGAGENTS_CACHE_DIR", os.path.join(_TRADINGAGENTS_HOME, "cache")),
    "memory_log_path": os.getenv("TRADINGAGENTS_MEMORY_LOG_PATH", os.path.join(_TRADINGAGENTS_HOME, "memory", "trading_memory.md")),
    # Optional cap on the number of resolved memory log entries. When set,
    # the oldest resolved entries are pruned once this limit is exceeded.
    # Pending entries are never pruned. None disables rotation entirely.
    "memory_log_max_entries": None,
    # LLM settings
    "llm_provider": "openai",
    "deep_think_llm": "gpt-5.4",
    "quick_think_llm": "gpt-5.4-mini",
    # When None, each provider's client falls back to its own default endpoint
    # (api.openai.com for OpenAI, generativelanguage.googleapis.com for Gemini, ...).
    # The CLI overrides this per provider when the user picks one. Keeping a
    # provider-specific URL here would leak (e.g. OpenAI's /v1 was previously
    # being forwarded to Gemini, producing malformed request URLs).
    "backend_url": None,
    # Provider-specific thinking configuration
    "google_thinking_level": None,      # "high", "minimal", etc.
    "openai_reasoning_effort": None,    # "medium", "high", "low"
    "anthropic_effort": None,           # "high", "medium", "low"
    # Checkpoint/resume: when True, LangGraph saves state after each node
    # so a crashed run can resume from the last successful step.
    "checkpoint_enabled": False,
    # Output language for analyst reports and final decision
    # Internal agent debate stays in English for reasoning quality
    "output_language": "English",
    # Debate and discussion settings
    "max_debate_rounds": 1,
    "max_risk_discuss_rounds": 1,
    "max_recur_limit": 100,
    # Data vendor configuration
    # Category-level configuration (default for all tools in category)
    "data_vendors": {
        "core_stock_apis": "yfinance",       # Options: alpha_vantage, yfinance
        "technical_indicators": "yfinance",  # Options: alpha_vantage, yfinance
        "fundamental_data": "yfinance",      # Options: alpha_vantage, yfinance
        "news_data": "yfinance",             # Options: alpha_vantage, yfinance
    },
    # Tool-level configuration (takes precedence over category-level)
    "tool_vendors": {
        # Example: "get_stock_data": "alpha_vantage",  # Override category default
    },
}
```

### tradingagents/agents/__init__.py

```python
from .utils.agent_utils import create_msg_delete
from .utils.agent_states import AgentState, InvestDebateState, RiskDebateState

from .analysts.fundamentals_analyst import create_fundamentals_analyst
from .analysts.market_analyst import create_market_analyst
from .analysts.news_analyst import create_news_analyst
from .analysts.social_media_analyst import create_social_media_analyst

from .researchers.bear_researcher import create_bear_researcher
from .researchers.bull_researcher import create_bull_researcher

from .risk_mgmt.aggressive_debator import create_aggressive_debator
from .risk_mgmt.conservative_debator import create_conservative_debator
from .risk_mgmt.neutral_debator import create_neutral_debator

from .managers.research_manager import create_research_manager
from .managers.portfolio_manager import create_portfolio_manager

from .trader.trader import create_trader

__all__ = [
    "AgentState",
    "create_msg_delete",
    "InvestDebateState",
    "RiskDebateState",
    "create_bear_researcher",
    "create_bull_researcher",
    "create_research_manager",
    "create_fundamentals_analyst",
    "create_market_analyst",
    "create_neutral_debator",
    "create_news_analyst",
    "create_aggressive_debator",
    "create_portfolio_manager",
    "create_conservative_debator",
    "create_social_media_analyst",
    "create_trader",
]
```

### tradingagents/agents/schemas.py

```python
"""Pydantic schemas used by agents that produce structured output.

The framework's primary artifact is still prose: each agent's natural-language
reasoning is what users read in the saved markdown reports and what the
downstream agents read as context.  Structured output is layered onto the
three decision-making agents (Research Manager, Trader, Portfolio Manager)
so that:

- Their outputs follow consistent section headers across runs and providers
- Each provider's native structured-output mode is used (json_schema for
  OpenAI/xAI, response_schema for Gemini, tool-use for Anthropic)
- Schema field descriptions become the model's output instructions, freeing
  the prompt body to focus on context and the rating-scale guidance
- A render helper turns the parsed Pydantic instance back into the same
  markdown shape the rest of the system already consumes, so display,
  memory log, and saved reports keep working unchanged
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Shared rating types
# ---------------------------------------------------------------------------


class PortfolioRating(str, Enum):
    """5-tier rating used by the Research Manager and Portfolio Manager."""

    BUY = "Buy"
    OVERWEIGHT = "Overweight"
    HOLD = "Hold"
    UNDERWEIGHT = "Underweight"
    SELL = "Sell"


class TraderAction(str, Enum):
    """3-tier transaction direction used by the Trader.

    The Trader's job is to translate the Research Manager's investment plan
    into a concrete transaction proposal: should the desk execute a Buy, a
    Sell, or sit on Hold this round.  Position sizing and the nuanced
    Overweight / Underweight calls happen later at the Portfolio Manager.
    """

    BUY = "Buy"
    HOLD = "Hold"
    SELL = "Sell"


# ---------------------------------------------------------------------------
# Research Manager
# ---------------------------------------------------------------------------


class ResearchPlan(BaseModel):
    """Structured investment plan produced by the Research Manager.

    Hand-off to the Trader: the recommendation pins the directional view,
    the rationale captures which side of the bull/bear debate carried the
    argument, and the strategic actions translate that into concrete
    instructions the trader can execute against.
    """

    recommendation: PortfolioRating = Field(
        description=(
            "The investment recommendation. Exactly one of Buy / Overweight / "
            "Hold / Underweight / Sell. Reserve Hold for situations where the "
            "evidence on both sides is genuinely balanced; otherwise commit to "
            "the side with the stronger arguments."
        ),
    )
    rationale: str = Field(
        description=(
            "Conversational summary of the key points from both sides of the "
            "debate, ending with which arguments led to the recommendation. "
            "Speak naturally, as if to a teammate."
        ),
    )
    strategic_actions: str = Field(
        description=(
            "Concrete steps for the trader to implement the recommendation, "
            "including position sizing guidance consistent with the rating."
        ),
    )


def render_research_plan(plan: ResearchPlan) -> str:
    """Render a ResearchPlan to markdown for storage and the trader's prompt context."""
    return "\n".join([
        f"**Recommendation**: {plan.recommendation.value}",
        "",
        f"**Rationale**: {plan.rationale}",
        "",
        f"**Strategic Actions**: {plan.strategic_actions}",
    ])


# ---------------------------------------------------------------------------
# Trader
# ---------------------------------------------------------------------------


class TraderProposal(BaseModel):
    """Structured transaction proposal produced by the Trader.

    The trader reads the Research Manager's investment plan and the analyst
    reports, then turns them into a concrete transaction: what action to
    take, the reasoning that justifies it, and the practical levels for
    entry, stop-loss, and sizing.
    """

    action: TraderAction = Field(
        description="The transaction direction. Exactly one of Buy / Hold / Sell.",
    )
    reasoning: str = Field(
        description=(
            "The case for this action, anchored in the analysts' reports and "
            "the research plan. Two to four sentences."
        ),
    )
    entry_price: Optional[float] = Field(
        default=None,
        description="Optional entry price target in the instrument's quote currency.",
    )
    stop_loss: Optional[float] = Field(
        default=None,
        description="Optional stop-loss price in the instrument's quote currency.",
    )
    position_sizing: Optional[str] = Field(
        default=None,
        description="Optional sizing guidance, e.g. '5% of portfolio'.",
    )


def render_trader_proposal(proposal: TraderProposal) -> str:
    """Render a TraderProposal to markdown.

    The trailing ``FINAL TRANSACTION PROPOSAL: **BUY/HOLD/SELL**`` line is
    preserved for backward compatibility with the analyst stop-signal text
    and any external code that greps for it.
    """
    parts = [
        f"**Action**: {proposal.action.value}",
        "",
        f"**Reasoning**: {proposal.reasoning}",
    ]
    if proposal.entry_price is not None:
        parts.extend(["", f"**Entry Price**: {proposal.entry_price}"])
    if proposal.stop_loss is not None:
        parts.extend(["", f"**Stop Loss**: {proposal.stop_loss}"])
    if proposal.position_sizing:
        parts.extend(["", f"**Position Sizing**: {proposal.position_sizing}"])
    parts.extend([
        "",
        f"FINAL TRANSACTION PROPOSAL: **{proposal.action.value.upper()}**",
    ])
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Portfolio Manager
# ---------------------------------------------------------------------------


class PortfolioDecision(BaseModel):
    """Structured output produced by the Portfolio Manager.

    The model fills every field as part of its primary LLM call; no separate
    extraction pass is required. Field descriptions double as the model's
    output instructions, so the prompt body only needs to convey context and
    the rating-scale guidance.
    """

    rating: PortfolioRating = Field(

# ... 文件较长，已截断。总行数：228
```

### tradingagents/dataflows/__init__.py

```python
```

### tradingagents/dataflows/alpha_vantage.py

```python
# Import functions from specialized modules
from .alpha_vantage_stock import get_stock
from .alpha_vantage_indicator import get_indicator
from .alpha_vantage_fundamentals import get_fundamentals, get_balance_sheet, get_cashflow, get_income_statement
from .alpha_vantage_news import get_news, get_global_news, get_insider_transactions
```

### tradingagents/dataflows/alpha_vantage_common.py

```python
import os
import requests
import pandas as pd
import json
from datetime import datetime
from io import StringIO

API_BASE_URL = "https://www.alphavantage.co/query"

def get_api_key() -> str:
    """Retrieve the API key for Alpha Vantage from environment variables."""
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    if not api_key:
        raise ValueError("ALPHA_VANTAGE_API_KEY environment variable is not set.")
    return api_key

def format_datetime_for_api(date_input) -> str:
    """Convert various date formats to YYYYMMDDTHHMM format required by Alpha Vantage API."""
    if isinstance(date_input, str):
        # If already in correct format, return as-is
        if len(date_input) == 13 and 'T' in date_input:
            return date_input
        # Try to parse common date formats
        try:
            dt = datetime.strptime(date_input, "%Y-%m-%d")
            return dt.strftime("%Y%m%dT0000")
        except ValueError:
            try:
                dt = datetime.strptime(date_input, "%Y-%m-%d %H:%M")
                return dt.strftime("%Y%m%dT%H%M")
            except ValueError:
                raise ValueError(f"Unsupported date format: {date_input}")
    elif isinstance(date_input, datetime):
        return date_input.strftime("%Y%m%dT%H%M")
    else:
        raise ValueError(f"Date must be string or datetime object, got {type(date_input)}")

class AlphaVantageRateLimitError(Exception):
    """Exception raised when Alpha Vantage API rate limit is exceeded."""
    pass

def _make_api_request(function_name: str, params: dict) -> dict | str:
    """Helper function to make API requests and handle responses.
    
    Raises:
        AlphaVantageRateLimitError: When API rate limit is exceeded
    """
    # Create a copy of params to avoid modifying the original
    api_params = params.copy()
    api_params.update({
        "function": function_name,
        "apikey": get_api_key(),
        "source": "trading_agents",
    })
    
    # Handle entitlement parameter if present in params or global variable
    current_entitlement = globals().get('_current_entitlement')
    entitlement = api_params.get("entitlement") or current_entitlement
    
    if entitlement:
        api_params["entitlement"] = entitlement
    elif "entitlement" in api_params:
        # Remove entitlement if it's None or empty
        api_params.pop("entitlement", None)
    
    response = requests.get(API_BASE_URL, params=api_params)
    response.raise_for_status()

    response_text = response.text
    
    # Check if response is JSON (error responses are typically JSON)
    try:
        response_json = json.loads(response_text)
        # Check for rate limit error
        if "Information" in response_json:
            info_message = response_json["Information"]
            if "rate limit" in info_message.lower() or "api key" in info_message.lower():
                raise AlphaVantageRateLimitError(f"Alpha Vantage rate limit exceeded: {info_message}")
    except json.JSONDecodeError:
        # Response is not JSON (likely CSV data), which is normal
        pass

    return response_text



def _filter_csv_by_date_range(csv_data: str, start_date: str, end_date: str) -> str:
    """
    Filter CSV data to include only rows within the specified date range.

    Args:
        csv_data: CSV string from Alpha Vantage API
        start_date: Start date in yyyy-mm-dd format
        end_date: End date in yyyy-mm-dd format

    Returns:
        Filtered CSV string
    """
    if not csv_data or csv_data.strip() == "":
        return csv_data

    try:
        # Parse CSV data
        df = pd.read_csv(StringIO(csv_data))

        # Assume the first column is the date column (timestamp)
        date_col = df.columns[0]
        df[date_col] = pd.to_datetime(df[date_col])

        # Filter by date range
        start_dt = pd.to_datetime(start_date)
        end_dt = pd.to_datetime(end_date)

        filtered_df = df[(df[date_col] >= start_dt) & (df[date_col] <= end_dt)]

        # Convert back to CSV string
        return filtered_df.to_csv(index=False)

    except Exception as e:
        # If filtering fails, return original data with a warning
        print(f"Warning: Failed to filter CSV data by date range: {e}")
        return csv_data
```

### tradingagents/dataflows/alpha_vantage_fundamentals.py

```python
from .alpha_vantage_common import _make_api_request


def _filter_reports_by_date(result, curr_date: str):
    """Filter annualReports/quarterlyReports to exclude entries after curr_date.

    Prevents look-ahead bias by removing fiscal periods that end after
    the simulation's current date.
    """
    if not curr_date or not isinstance(result, dict):
        return result
    for key in ("annualReports", "quarterlyReports"):
        if key in result:
            result[key] = [
                r for r in result[key]
                if r.get("fiscalDateEnding", "") <= curr_date
            ]
    return result


def get_fundamentals(ticker: str, curr_date: str = None) -> str:
    """
    Retrieve comprehensive fundamental data for a given ticker symbol using Alpha Vantage.

    Args:
        ticker (str): Ticker symbol of the company
        curr_date (str): Current date you are trading at, yyyy-mm-dd (not used for Alpha Vantage)

    Returns:
        str: Company overview data including financial ratios and key metrics
    """
    params = {
        "symbol": ticker,
    }

    return _make_api_request("OVERVIEW", params)


def get_balance_sheet(ticker: str, freq: str = "quarterly", curr_date: str = None):
    """Retrieve balance sheet data for a given ticker symbol using Alpha Vantage."""
    result = _make_api_request("BALANCE_SHEET", {"symbol": ticker})
    return _filter_reports_by_date(result, curr_date)


def get_cashflow(ticker: str, freq: str = "quarterly", curr_date: str = None):
    """Retrieve cash flow statement data for a given ticker symbol using Alpha Vantage."""
    result = _make_api_request("CASH_FLOW", {"symbol": ticker})
    return _filter_reports_by_date(result, curr_date)


def get_income_statement(ticker: str, freq: str = "quarterly", curr_date: str = None):
    """Retrieve income statement data for a given ticker symbol using Alpha Vantage."""
    result = _make_api_request("INCOME_STATEMENT", {"symbol": ticker})
    return _filter_reports_by_date(result, curr_date)

```

### tradingagents/dataflows/alpha_vantage_indicator.py

```python
from .alpha_vantage_common import _make_api_request

def get_indicator(
    symbol: str,
    indicator: str,
    curr_date: str,
    look_back_days: int,
    interval: str = "daily",
    time_period: int = 14,
    series_type: str = "close"
) -> str:
    """
    Returns Alpha Vantage technical indicator values over a time window.

    Args:
        symbol: ticker symbol of the company
        indicator: technical indicator to get the analysis and report of
        curr_date: The current trading date you are trading on, YYYY-mm-dd
        look_back_days: how many days to look back
        interval: Time interval (daily, weekly, monthly)
        time_period: Number of data points for calculation
        series_type: The desired price type (close, open, high, low)

    Returns:
        String containing indicator values and description
    """
    from datetime import datetime
    from dateutil.relativedelta import relativedelta

    supported_indicators = {
        "close_50_sma": ("50 SMA", "close"),
        "close_200_sma": ("200 SMA", "close"),
        "close_10_ema": ("10 EMA", "close"),
        "macd": ("MACD", "close"),
        "macds": ("MACD Signal", "close"),
        "macdh": ("MACD Histogram", "close"),
        "rsi": ("RSI", "close"),
        "boll": ("Bollinger Middle", "close"),
        "boll_ub": ("Bollinger Upper Band", "close"),
        "boll_lb": ("Bollinger Lower Band", "close"),
        "atr": ("ATR", None),
        "vwma": ("VWMA", "close")
    }

    indicator_descriptions = {
        "close_50_sma": "50 SMA: A medium-term trend indicator. Usage: Identify trend direction and serve as dynamic support/resistance. Tips: It lags price; combine with faster indicators for timely signals.",
        "close_200_sma": "200 SMA: A long-term trend benchmark. Usage: Confirm overall market trend and identify golden/death cross setups. Tips: It reacts slowly; best for strategic trend confirmation rather than frequent trading entries.",
        "close_10_ema": "10 EMA: A responsive short-term average. Usage: Capture quick shifts in momentum and potential entry points. Tips: Prone to noise in choppy markets; use alongside longer averages for filtering false signals.",
        "macd": "MACD: Computes momentum via differences of EMAs. Usage: Look for crossovers and divergence as signals of trend changes. Tips: Confirm with other indicators in low-volatility or sideways markets.",
        "macds": "MACD Signal: An EMA smoothing of the MACD line. Usage: Use crossovers with the MACD line to trigger trades. Tips: Should be part of a broader strategy to avoid false positives.",
        "macdh": "MACD Histogram: Shows the gap between the MACD line and its signal. Usage: Visualize momentum strength and spot divergence early. Tips: Can be volatile; complement with additional filters in fast-moving markets.",
        "rsi": "RSI: Measures momentum to flag overbought/oversold conditions. Usage: Apply 70/30 thresholds and watch for divergence to signal reversals. Tips: In strong trends, RSI may remain extreme; always cross-check with trend analysis.",
        "boll": "Bollinger Middle: A 20 SMA serving as the basis for Bollinger Bands. Usage: Acts as a dynamic benchmark for price movement. Tips: Combine with the upper and lower bands to effectively spot breakouts or reversals.",
        "boll_ub": "Bollinger Upper Band: Typically 2 standard deviations above the middle line. Usage: Signals potential overbought conditions and breakout zones. Tips: Confirm signals with other tools; prices may ride the band in strong trends.",
        "boll_lb": "Bollinger Lower Band: Typically 2 standard deviations below the middle line. Usage: Indicates potential oversold conditions. Tips: Use additional analysis to avoid false reversal signals.",
        "atr": "ATR: Averages true range to measure volatility. Usage: Set stop-loss levels and adjust position sizes based on current market volatility. Tips: It's a reactive measure, so use it as part of a broader risk management strategy.",
        "vwma": "VWMA: A moving average weighted by volume. Usage: Confirm trends by integrating price action with volume data. Tips: Watch for skewed results from volume spikes; use in combination with other volume analyses."
    }

    if indicator not in supported_indicators:
        raise ValueError(
            f"Indicator {indicator} is not supported. Please choose from: {list(supported_indicators.keys())}"
        )

    curr_date_dt = datetime.strptime(curr_date, "%Y-%m-%d")
    before = curr_date_dt - relativedelta(days=look_back_days)

    # Get the full data for the period instead of making individual calls
    _, required_series_type = supported_indicators[indicator]

    # Use the provided series_type or fall back to the required one
    if required_series_type:
        series_type = required_series_type

    try:
        # Get indicator data for the period
        if indicator == "close_50_sma":
            data = _make_api_request("SMA", {
                "symbol": symbol,
                "interval": interval,
                "time_period": "50",
                "series_type": series_type,
                "datatype": "csv"
            })
        elif indicator == "close_200_sma":
            data = _make_api_request("SMA", {
                "symbol": symbol,
                "interval": interval,
                "time_period": "200",
                "series_type": series_type,
                "datatype": "csv"
            })
        elif indicator == "close_10_ema":
            data = _make_api_request("EMA", {
                "symbol": symbol,
                "interval": interval,
                "time_period": "10",
                "series_type": series_type,
                "datatype": "csv"
            })
        elif indicator == "macd":
            data = _make_api_request("MACD", {
                "symbol": symbol,
                "interval": interval,
                "series_type": series_type,
                "datatype": "csv"
            })
        elif indicator == "macds":
            data = _make_api_request("MACD", {
                "symbol": symbol,
                "interval": interval,
                "series_type": series_type,
                "datatype": "csv"
            })
        elif indicator == "macdh":
            data = _make_api_request("MACD", {
                "symbol": symbol,
                "interval": interval,
                "series_type": series_type,
                "datatype": "csv"
            })
        elif indicator == "rsi":
            data = _make_api_request("RSI", {
                "symbol": symbol,
                "interval": interval,
                "time_period": str(time_period),
                "series_type": series_type,
                "datatype": "csv"
            })
        elif indicator in ["boll", "boll_ub", "boll_lb"]:
            data = _make_api_request("BBANDS", {
                "symbol": symbol,
                "interval": interval,
                "time_period": "20",
                "series_type": series_type,
                "datatype": "csv"
            })
        elif indicator == "atr":
            data = _make_api_request("ATR", {
                "symbol": symbol,
                "interval": interval,
                "time_period": str(time_period),
                "datatype": "csv"
            })
        elif indicator == "vwma":
            # Alpha Vantage doesn't have direct VWMA, so we'll return an informative message
            # In a real implementation, this would need to be calculated from OHLCV data
            return f"## VWMA (Volume Weighted Moving Average) for {symbol}:\n\nVWMA calculation requires OHLCV data and is not directly available from Alpha Vantage API.\nThis indicator would need to be calculated from the raw stock data using volume-weighted price averaging.\n\n{indicator_descriptions.get('vwma', 'No description available.')}"
        else:
            return f"Error: Indicator {indicator} not implemented yet."

        # Parse CSV data and extract values for the date range
        lines = data.strip().split('\n')
        if len(lines) < 2:
            return f"Error: No data returned for {indicator}"

        # Parse header and data
        header = [col.strip() for col in lines[0].split(',')]
        try:
            date_col_idx = header.index('time')
        except ValueError:
            return f"Error: 'time' column not found in data for {indicator}. Available columns: {header}"

        # Map internal indicator names to expected CSV column names from Alpha Vantage
        col_name_map = {
            "macd": "MACD", "macds": "MACD_Signal", "macdh": "MACD_Hist",
            "boll": "Real Middle Band", "boll_ub": "Real Upper Band", "boll_lb": "Real Lower Band",
            "rsi": "RSI", "atr": "ATR", "close_10_ema": "EMA",
            "close_50_sma": "SMA", "close_200_sma": "SMA"
        }

        target_col_name = col_name_map.get(indicator)

        if not target_col_name:
            # Default to the second column if no specific mapping exists
            value_col_idx = 1
        else:
            try:
                value_col_idx = header.index(target_col_name)
            except ValueError:

# ... 文件较长，已截断。总行数：222
```

### tradingagents/dataflows/alpha_vantage_news.py

```python
from .alpha_vantage_common import _make_api_request, format_datetime_for_api

def get_news(ticker, start_date, end_date) -> dict[str, str] | str:
    """Returns live and historical market news & sentiment data from premier news outlets worldwide.

    Covers stocks, cryptocurrencies, forex, and topics like fiscal policy, mergers & acquisitions, IPOs.

    Args:
        ticker: Stock symbol for news articles.
        start_date: Start date for news search.
        end_date: End date for news search.

    Returns:
        Dictionary containing news sentiment data or JSON string.
    """

    params = {
        "tickers": ticker,
        "time_from": format_datetime_for_api(start_date),
        "time_to": format_datetime_for_api(end_date),
    }

    return _make_api_request("NEWS_SENTIMENT", params)

def get_global_news(curr_date, look_back_days: int = 7, limit: int = 50) -> dict[str, str] | str:
    """Returns global market news & sentiment data without ticker-specific filtering.

    Covers broad market topics like financial markets, economy, and more.

    Args:
        curr_date: Current date in yyyy-mm-dd format.
        look_back_days: Number of days to look back (default 7).
        limit: Maximum number of articles (default 50).

    Returns:
        Dictionary containing global news sentiment data or JSON string.
    """
    from datetime import datetime, timedelta

    # Calculate start date
    curr_dt = datetime.strptime(curr_date, "%Y-%m-%d")
    start_dt = curr_dt - timedelta(days=look_back_days)
    start_date = start_dt.strftime("%Y-%m-%d")

    params = {
        "topics": "financial_markets,economy_macro,economy_monetary",
        "time_from": format_datetime_for_api(start_date),
        "time_to": format_datetime_for_api(curr_date),
        "limit": str(limit),
    }

    return _make_api_request("NEWS_SENTIMENT", params)


def get_insider_transactions(symbol: str) -> dict[str, str] | str:
    """Returns latest and historical insider transactions by key stakeholders.

    Covers transactions by founders, executives, board members, etc.

    Args:
        symbol: Ticker symbol. Example: "IBM".

    Returns:
        Dictionary containing insider transaction data or JSON string.
    """

    params = {
        "symbol": symbol,
    }

    return _make_api_request("INSIDER_TRANSACTIONS", params)
```

### tradingagents/dataflows/alpha_vantage_stock.py

```python
from datetime import datetime
from .alpha_vantage_common import _make_api_request, _filter_csv_by_date_range

def get_stock(
    symbol: str,
    start_date: str,
    end_date: str
) -> str:
    """
    Returns raw daily OHLCV values, adjusted close values, and historical split/dividend events
    filtered to the specified date range.

    Args:
        symbol: The name of the equity. For example: symbol=IBM
        start_date: Start date in yyyy-mm-dd format
        end_date: End date in yyyy-mm-dd format

    Returns:
        CSV string containing the daily adjusted time series data filtered to the date range.
    """
    # Parse dates to determine the range
    start_dt = datetime.strptime(start_date, "%Y-%m-%d")
    today = datetime.now()

    # Choose outputsize based on whether the requested range is within the latest 100 days
    # Compact returns latest 100 data points, so check if start_date is recent enough
    days_from_today_to_start = (today - start_dt).days
    outputsize = "compact" if days_from_today_to_start < 100 else "full"

    params = {
        "symbol": symbol,
        "outputsize": outputsize,
        "datatype": "csv",
    }

    response = _make_api_request("TIME_SERIES_DAILY_ADJUSTED", params)

    return _filter_csv_by_date_range(response, start_date, end_date)
```

### tradingagents/dataflows/config.py

```python
import tradingagents.default_config as default_config
from typing import Dict, Optional

# Use default config but allow it to be overridden
_config: Optional[Dict] = None


def initialize_config():
    """Initialize the configuration with default values."""
    global _config
    if _config is None:
        _config = default_config.DEFAULT_CONFIG.copy()


def set_config(config: Dict):
    """Update the configuration with custom values."""
    global _config
    if _config is None:
        _config = default_config.DEFAULT_CONFIG.copy()
    _config.update(config)


def get_config() -> Dict:
    """Get the current configuration."""
    if _config is None:
        initialize_config()
    return _config.copy()


# Initialize with default config
initialize_config()
```

### tradingagents/dataflows/interface.py

```python
from typing import Annotated

# Import from vendor-specific modules
from .y_finance import (
    get_YFin_data_online,
    get_stock_stats_indicators_window,
    get_fundamentals as get_yfinance_fundamentals,
    get_balance_sheet as get_yfinance_balance_sheet,
    get_cashflow as get_yfinance_cashflow,
    get_income_statement as get_yfinance_income_statement,
    get_insider_transactions as get_yfinance_insider_transactions,
)
from .yfinance_news import get_news_yfinance, get_global_news_yfinance
from .alpha_vantage import (
    get_stock as get_alpha_vantage_stock,
    get_indicator as get_alpha_vantage_indicator,
    get_fundamentals as get_alpha_vantage_fundamentals,
    get_balance_sheet as get_alpha_vantage_balance_sheet,
    get_cashflow as get_alpha_vantage_cashflow,
    get_income_statement as get_alpha_vantage_income_statement,
    get_insider_transactions as get_alpha_vantage_insider_transactions,
    get_news as get_alpha_vantage_news,
    get_global_news as get_alpha_vantage_global_news,
)
from .alpha_vantage_common import AlphaVantageRateLimitError

# Configuration and routing logic
from .config import get_config

# Tools organized by category
TOOLS_CATEGORIES = {
    "core_stock_apis": {
        "description": "OHLCV stock price data",
        "tools": [
            "get_stock_data"
        ]
    },
    "technical_indicators": {
        "description": "Technical analysis indicators",
        "tools": [
            "get_indicators"
        ]
    },
    "fundamental_data": {
        "description": "Company fundamentals",
        "tools": [
            "get_fundamentals",
            "get_balance_sheet",
            "get_cashflow",
            "get_income_statement"
        ]
    },
    "news_data": {
        "description": "News and insider data",
        "tools": [
            "get_news",
            "get_global_news",
            "get_insider_transactions",
        ]
    }
}

VENDOR_LIST = [
    "yfinance",
    "alpha_vantage",
]

# Mapping of methods to their vendor-specific implementations
VENDOR_METHODS = {
    # core_stock_apis
    "get_stock_data": {
        "alpha_vantage": get_alpha_vantage_stock,
        "yfinance": get_YFin_data_online,
    },
    # technical_indicators
    "get_indicators": {
        "alpha_vantage": get_alpha_vantage_indicator,
        "yfinance": get_stock_stats_indicators_window,
    },
    # fundamental_data
    "get_fundamentals": {
        "alpha_vantage": get_alpha_vantage_fundamentals,
        "yfinance": get_yfinance_fundamentals,
    },
    "get_balance_sheet": {
        "alpha_vantage": get_alpha_vantage_balance_sheet,
        "yfinance": get_yfinance_balance_sheet,
    },
    "get_cashflow": {
        "alpha_vantage": get_alpha_vantage_cashflow,
        "yfinance": get_yfinance_cashflow,
    },
    "get_income_statement": {
        "alpha_vantage": get_alpha_vantage_income_statement,
        "yfinance": get_yfinance_income_statement,
    },
    # news_data
    "get_news": {
        "alpha_vantage": get_alpha_vantage_news,
        "yfinance": get_news_yfinance,
    },
    "get_global_news": {
        "yfinance": get_global_news_yfinance,
        "alpha_vantage": get_alpha_vantage_global_news,
    },
    "get_insider_transactions": {
        "alpha_vantage": get_alpha_vantage_insider_transactions,
        "yfinance": get_yfinance_insider_transactions,
    },
}

def get_category_for_method(method: str) -> str:
    """Get the category that contains the specified method."""
    for category, info in TOOLS_CATEGORIES.items():
        if method in info["tools"]:
            return category
    raise ValueError(f"Method '{method}' not found in any category")

def get_vendor(category: str, method: str = None) -> str:
    """Get the configured vendor for a data category or specific tool method.
    Tool-level configuration takes precedence over category-level.
    """
    config = get_config()

    # Check tool-level configuration first (if method provided)
    if method:
        tool_vendors = config.get("tool_vendors", {})
        if method in tool_vendors:
            return tool_vendors[method]

    # Fall back to category-level configuration
    return config.get("data_vendors", {}).get(category, "default")

def route_to_vendor(method: str, *args, **kwargs):
    """Route method calls to appropriate vendor implementation with fallback support."""
    category = get_category_for_method(method)
    vendor_config = get_vendor(category, method)
    primary_vendors = [v.strip() for v in vendor_config.split(',')]

    if method not in VENDOR_METHODS:
        raise ValueError(f"Method '{method}' not supported")

    # Build fallback chain: primary vendors first, then remaining available vendors
    all_available_vendors = list(VENDOR_METHODS[method].keys())
    fallback_vendors = primary_vendors.copy()
    for vendor in all_available_vendors:
        if vendor not in fallback_vendors:
            fallback_vendors.append(vendor)

    for vendor in fallback_vendors:
        if vendor not in VENDOR_METHODS[method]:
            continue

        vendor_impl = VENDOR_METHODS[method][vendor]
        impl_func = vendor_impl[0] if isinstance(vendor_impl, list) else vendor_impl

        try:
            return impl_func(*args, **kwargs)
        except AlphaVantageRateLimitError:
            continue  # Only rate limits trigger fallback

    raise RuntimeError(f"No available vendor for '{method}'")
```

### tradingagents/dataflows/stockstats_utils.py

```python
import time
import logging

import pandas as pd
import yfinance as yf
from yfinance.exceptions import YFRateLimitError
from stockstats import wrap
from typing import Annotated
import os
from .config import get_config
from .utils import safe_ticker_component

logger = logging.getLogger(__name__)


def yf_retry(func, max_retries=3, base_delay=2.0):
    """Execute a yfinance call with exponential backoff on rate limits.

    yfinance raises YFRateLimitError on HTTP 429 responses but does not
    retry them internally. This wrapper adds retry logic specifically
    for rate limits. Other exceptions propagate immediately.
    """
    for attempt in range(max_retries + 1):
        try:
            return func()
        except YFRateLimitError:
            if attempt < max_retries:
                delay = base_delay * (2 ** attempt)
                logger.warning(f"Yahoo Finance rate limited, retrying in {delay:.0f}s (attempt {attempt + 1}/{max_retries})")
                time.sleep(delay)
            else:
                raise


def _clean_dataframe(data: pd.DataFrame) -> pd.DataFrame:
    """Normalize a stock DataFrame for stockstats: parse dates, drop invalid rows, fill price gaps."""
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    data = data.dropna(subset=["Date"])

    price_cols = [c for c in ["Open", "High", "Low", "Close", "Volume"] if c in data.columns]
    data[price_cols] = data[price_cols].apply(pd.to_numeric, errors="coerce")
    data = data.dropna(subset=["Close"])
    data[price_cols] = data[price_cols].ffill().bfill()

    return data


def load_ohlcv(symbol: str, curr_date: str) -> pd.DataFrame:
    """Fetch OHLCV data with caching, filtered to prevent look-ahead bias.

    Downloads 15 years of data up to today and caches per symbol. On
    subsequent calls the cache is reused. Rows after curr_date are
    filtered out so backtests never see future prices.
    """
    # Reject ticker values that would escape the cache directory when
    # interpolated into the cache filename (e.g. ``../../tmp/x``).
    safe_symbol = safe_ticker_component(symbol)

    config = get_config()
    curr_date_dt = pd.to_datetime(curr_date)

    # Cache uses a fixed window (15y to today) so one file per symbol
    today_date = pd.Timestamp.today()
    start_date = today_date - pd.DateOffset(years=5)
    start_str = start_date.strftime("%Y-%m-%d")
    end_str = today_date.strftime("%Y-%m-%d")

    os.makedirs(config["data_cache_dir"], exist_ok=True)
    data_file = os.path.join(
        config["data_cache_dir"],
        f"{safe_symbol}-YFin-data-{start_str}-{end_str}.csv",
    )

    if os.path.exists(data_file):
        data = pd.read_csv(data_file, on_bad_lines="skip", encoding="utf-8")
    else:
        data = yf_retry(lambda: yf.download(
            symbol,
            start=start_str,
            end=end_str,
            multi_level_index=False,
            progress=False,
            auto_adjust=True,
        ))
        data = data.reset_index()
        data.to_csv(data_file, index=False, encoding="utf-8")

    data = _clean_dataframe(data)

    # Filter to curr_date to prevent look-ahead bias in backtesting
    data = data[data["Date"] <= curr_date_dt]

    return data


def filter_financials_by_date(data: pd.DataFrame, curr_date: str) -> pd.DataFrame:
    """Drop financial statement columns (fiscal period timestamps) after curr_date.

    yfinance financial statements use fiscal period end dates as columns.
    Columns after curr_date represent future data and are removed to
    prevent look-ahead bias.
    """
    if not curr_date or data.empty:
        return data
    cutoff = pd.Timestamp(curr_date)
    mask = pd.to_datetime(data.columns, errors="coerce") <= cutoff
    return data.loc[:, mask]


class StockstatsUtils:
    @staticmethod
    def get_stock_stats(
        symbol: Annotated[str, "ticker symbol for the company"],
        indicator: Annotated[
            str, "quantitative indicators based off of the stock data for the company"
        ],
        curr_date: Annotated[
            str, "curr date for retrieving stock price data, YYYY-mm-dd"
        ],
    ):
        data = load_ohlcv(symbol, curr_date)
        df = wrap(data)
        df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")
        curr_date_str = pd.to_datetime(curr_date).strftime("%Y-%m-%d")

        df[indicator]  # trigger stockstats to calculate the indicator
        matching_rows = df[df["Date"].str.startswith(curr_date_str)]

        if not matching_rows.empty:
            indicator_value = matching_rows[indicator].values[0]
            return indicator_value
        else:
            return "N/A: Not a trading day (weekend or holiday)"
```

### tradingagents/dataflows/utils.py

```python
import os
import re
import json
import pandas as pd
from datetime import date, timedelta, datetime
from typing import Annotated

SavePathType = Annotated[str, "File path to save data. If None, data is not saved."]

# Tickers can contain letters, digits, dot, dash, underscore, and caret
# (for index symbols like ^GSPC). Anything else is rejected so the value
# never escapes a containing directory when interpolated into a path.
_TICKER_PATH_RE = re.compile(r"^[A-Za-z0-9._\-\^]+$")


def safe_ticker_component(value: str, *, max_len: int = 32) -> str:
    """Validate ``value`` is safe to interpolate into a filesystem path.

    Tickers come from user CLI input or from LLM tool calls, both of which
    can be influenced by attacker-controlled content (e.g. prompt injection
    embedded in fetched news). Without validation, a value like
    ``"../../../etc/foo"`` flows into ``os.path.join`` / ``Path /`` and
    escapes the configured cache, checkpoint, or results directory.

    Returns ``value`` unchanged when it matches the allowed pattern; raises
    ``ValueError`` otherwise.
    """
    if not isinstance(value, str) or not value:
        raise ValueError(f"ticker must be a non-empty string, got {value!r}")
    if len(value) > max_len:
        raise ValueError(f"ticker exceeds {max_len} chars: {value!r}")
    if not _TICKER_PATH_RE.fullmatch(value):
        raise ValueError(
            f"ticker contains characters not allowed in a filesystem path: {value!r}"
        )
    # The regex above allows '.', so values like '.', '..', '...' would pass,
    # and as a path component they traverse the parent directory. Reject any
    # value that's only dots.
    if set(value) == {"."}:
        raise ValueError(f"ticker cannot consist solely of dots: {value!r}")
    return value


def save_output(data: pd.DataFrame, tag: str, save_path: SavePathType = None) -> None:
    if save_path:
        data.to_csv(save_path, encoding="utf-8")
        print(f"{tag} saved to {save_path}")


def get_current_date():
    return date.today().strftime("%Y-%m-%d")


def decorate_all_methods(decorator):
    def class_decorator(cls):
        for attr_name, attr_value in cls.__dict__.items():
            if callable(attr_value):
                setattr(cls, attr_name, decorator(attr_value))
        return cls

    return class_decorator


def get_next_weekday(date):

    if not isinstance(date, datetime):
        date = datetime.strptime(date, "%Y-%m-%d")

    if date.weekday() >= 5:
        days_to_add = 7 - date.weekday()
        next_weekday = date + timedelta(days=days_to_add)
        return next_weekday
    else:
        return date
```

### tradingagents/dataflows/y_finance.py

```python
from typing import Annotated
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import yfinance as yf
import os
from .stockstats_utils import StockstatsUtils, _clean_dataframe, yf_retry, load_ohlcv, filter_financials_by_date

def get_YFin_data_online(
    symbol: Annotated[str, "ticker symbol of the company"],
    start_date: Annotated[str, "Start date in yyyy-mm-dd format"],
    end_date: Annotated[str, "End date in yyyy-mm-dd format"],
):

    datetime.strptime(start_date, "%Y-%m-%d")
    datetime.strptime(end_date, "%Y-%m-%d")

    # Create ticker object
    ticker = yf.Ticker(symbol.upper())

    # Fetch historical data for the specified date range
    data = yf_retry(lambda: ticker.history(start=start_date, end=end_date))

    # Check if data is empty
    if data.empty:
        return (
            f"No data found for symbol '{symbol}' between {start_date} and {end_date}"
        )

    # Remove timezone info from index for cleaner output
    if data.index.tz is not None:
        data.index = data.index.tz_localize(None)

    # Round numerical values to 2 decimal places for cleaner display
    numeric_columns = ["Open", "High", "Low", "Close", "Adj Close"]
    for col in numeric_columns:
        if col in data.columns:
            data[col] = data[col].round(2)

    # Convert DataFrame to CSV string
    csv_string = data.to_csv()

    # Add header information
    header = f"# Stock data for {symbol.upper()} from {start_date} to {end_date}\n"
    header += f"# Total records: {len(data)}\n"
    header += f"# Data retrieved on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

    return header + csv_string

def get_stock_stats_indicators_window(
    symbol: Annotated[str, "ticker symbol of the company"],
    indicator: Annotated[str, "technical indicator to get the analysis and report of"],
    curr_date: Annotated[
        str, "The current trading date you are trading on, YYYY-mm-dd"
    ],
    look_back_days: Annotated[int, "how many days to look back"],
) -> str:

    best_ind_params = {
        # Moving Averages
        "close_50_sma": (
            "50 SMA: A medium-term trend indicator. "
            "Usage: Identify trend direction and serve as dynamic support/resistance. "
            "Tips: It lags price; combine with faster indicators for timely signals."
        ),
        "close_200_sma": (
            "200 SMA: A long-term trend benchmark. "
            "Usage: Confirm overall market trend and identify golden/death cross setups. "
            "Tips: It reacts slowly; best for strategic trend confirmation rather than frequent trading entries."
        ),
        "close_10_ema": (
            "10 EMA: A responsive short-term average. "
            "Usage: Capture quick shifts in momentum and potential entry points. "
            "Tips: Prone to noise in choppy markets; use alongside longer averages for filtering false signals."
        ),
        # MACD Related
        "macd": (
            "MACD: Computes momentum via differences of EMAs. "
            "Usage: Look for crossovers and divergence as signals of trend changes. "
            "Tips: Confirm with other indicators in low-volatility or sideways markets."
        ),
        "macds": (
            "MACD Signal: An EMA smoothing of the MACD line. "
            "Usage: Use crossovers with the MACD line to trigger trades. "
            "Tips: Should be part of a broader strategy to avoid false positives."
        ),
        "macdh": (
            "MACD Histogram: Shows the gap between the MACD line and its signal. "
            "Usage: Visualize momentum strength and spot divergence early. "
            "Tips: Can be volatile; complement with additional filters in fast-moving markets."
        ),
        # Momentum Indicators
        "rsi": (
            "RSI: Measures momentum to flag overbought/oversold conditions. "
            "Usage: Apply 70/30 thresholds and watch for divergence to signal reversals. "
            "Tips: In strong trends, RSI may remain extreme; always cross-check with trend analysis."
        ),
        # Volatility Indicators
        "boll": (
            "Bollinger Middle: A 20 SMA serving as the basis for Bollinger Bands. "
            "Usage: Acts as a dynamic benchmark for price movement. "
            "Tips: Combine with the upper and lower bands to effectively spot breakouts or reversals."
        ),
        "boll_ub": (
            "Bollinger Upper Band: Typically 2 standard deviations above the middle line. "
            "Usage: Signals potential overbought conditions and breakout zones. "
            "Tips: Confirm signals with other tools; prices may ride the band in strong trends."
        ),
        "boll_lb": (
            "Bollinger Lower Band: Typically 2 standard deviations below the middle line. "
            "Usage: Indicates potential oversold conditions. "
            "Tips: Use additional analysis to avoid false reversal signals."
        ),
        "atr": (
            "ATR: Averages true range to measure volatility. "
            "Usage: Set stop-loss levels and adjust position sizes based on current market volatility. "
            "Tips: It's a reactive measure, so use it as part of a broader risk management strategy."
        ),
        # Volume-Based Indicators
        "vwma": (
            "VWMA: A moving average weighted by volume. "
            "Usage: Confirm trends by integrating price action with volume data. "
            "Tips: Watch for skewed results from volume spikes; use in combination with other volume analyses."
        ),
        "mfi": (
            "MFI: The Money Flow Index is a momentum indicator that uses both price and volume to measure buying and selling pressure. "
            "Usage: Identify overbought (>80) or oversold (<20) conditions and confirm the strength of trends or reversals. "
            "Tips: Use alongside RSI or MACD to confirm signals; divergence between price and MFI can indicate potential reversals."
        ),
    }

    if indicator not in best_ind_params:
        raise ValueError(
            f"Indicator {indicator} is not supported. Please choose from: {list(best_ind_params.keys())}"
        )

    end_date = curr_date
    curr_date_dt = datetime.strptime(curr_date, "%Y-%m-%d")
    before = curr_date_dt - relativedelta(days=look_back_days)

    # Optimized: Get stock data once and calculate indicators for all dates
    try:
        indicator_data = _get_stock_stats_bulk(symbol, indicator, curr_date)
        
        # Generate the date range we need
        current_dt = curr_date_dt
        date_values = []
        
        while current_dt >= before:
            date_str = current_dt.strftime('%Y-%m-%d')
            
            # Look up the indicator value for this date
            if date_str in indicator_data:
                indicator_value = indicator_data[date_str]
            else:
                indicator_value = "N/A: Not a trading day (weekend or holiday)"
            
            date_values.append((date_str, indicator_value))
            current_dt = current_dt - relativedelta(days=1)
        
        # Build the result string
        ind_string = ""
        for date_str, value in date_values:
            ind_string += f"{date_str}: {value}\n"
        
    except Exception as e:
        print(f"Error getting bulk stockstats data: {e}")
        # Fallback to original implementation if bulk method fails
        ind_string = ""
        curr_date_dt = datetime.strptime(curr_date, "%Y-%m-%d")
        while curr_date_dt >= before:
            indicator_value = get_stockstats_indicator(
                symbol, indicator, curr_date_dt.strftime("%Y-%m-%d")
            )
            ind_string += f"{curr_date_dt.strftime('%Y-%m-%d')}: {indicator_value}\n"
            curr_date_dt = curr_date_dt - relativedelta(days=1)

    result_str = (
        f"## {indicator} values from {before.strftime('%Y-%m-%d')} to {end_date}:\n\n"
        + ind_string

# ... 文件较长，已截断。总行数：422
```

### tradingagents/dataflows/yfinance_news.py

```python
"""yfinance-based news data fetching functions."""

import yfinance as yf
from datetime import datetime
from dateutil.relativedelta import relativedelta

from .stockstats_utils import yf_retry


def _extract_article_data(article: dict) -> dict:
    """Extract article data from yfinance news format (handles nested 'content' structure)."""
    # Handle nested content structure
    if "content" in article:
        content = article["content"]
        title = content.get("title", "No title")
        summary = content.get("summary", "")
        provider = content.get("provider", {})
        publisher = provider.get("displayName", "Unknown")

        # Get URL from canonicalUrl or clickThroughUrl
        url_obj = content.get("canonicalUrl") or content.get("clickThroughUrl") or {}
        link = url_obj.get("url", "")

        # Get publish date
        pub_date_str = content.get("pubDate", "")
        pub_date = None
        if pub_date_str:
            try:
                pub_date = datetime.fromisoformat(pub_date_str.replace("Z", "+00:00"))
            except (ValueError, AttributeError):
                pass

        return {
            "title": title,
            "summary": summary,
            "publisher": publisher,
            "link": link,
            "pub_date": pub_date,
        }
    else:
        # Fallback for flat structure
        return {
            "title": article.get("title", "No title"),
            "summary": article.get("summary", ""),
            "publisher": article.get("publisher", "Unknown"),
            "link": article.get("link", ""),
            "pub_date": None,
        }


def get_news_yfinance(
    ticker: str,
    start_date: str,
    end_date: str,
) -> str:
    """
    Retrieve news for a specific stock ticker using yfinance.

    Args:
        ticker: Stock ticker symbol (e.g., "AAPL")
        start_date: Start date in yyyy-mm-dd format
        end_date: End date in yyyy-mm-dd format

    Returns:
        Formatted string containing news articles
    """
    try:
        stock = yf.Ticker(ticker)
        news = yf_retry(lambda: stock.get_news(count=20))

        if not news:
            return f"No news found for {ticker}"

        # Parse date range for filtering
        start_dt = datetime.strptime(start_date, "%Y-%m-%d")
        end_dt = datetime.strptime(end_date, "%Y-%m-%d")

        news_str = ""
        filtered_count = 0

        for article in news:
            data = _extract_article_data(article)

            # Filter by date if publish time is available
            if data["pub_date"]:
                pub_date_naive = data["pub_date"].replace(tzinfo=None)
                if not (start_dt <= pub_date_naive <= end_dt + relativedelta(days=1)):
                    continue

            news_str += f"### {data['title']} (source: {data['publisher']})\n"
            if data["summary"]:
                news_str += f"{data['summary']}\n"
            if data["link"]:
                news_str += f"Link: {data['link']}\n"
            news_str += "\n"
            filtered_count += 1

        if filtered_count == 0:
            return f"No news found for {ticker} between {start_date} and {end_date}"

        return f"## {ticker} News, from {start_date} to {end_date}:\n\n{news_str}"

    except Exception as e:
        return f"Error fetching news for {ticker}: {str(e)}"


def get_global_news_yfinance(
    curr_date: str,
    look_back_days: int = 7,
    limit: int = 10,
) -> str:
    """
    Retrieve global/macro economic news using yfinance Search.

    Args:
        curr_date: Current date in yyyy-mm-dd format
        look_back_days: Number of days to look back
        limit: Maximum number of articles to return

    Returns:
        Formatted string containing global news articles
    """
    # Search queries for macro/global news
    search_queries = [
        "stock market economy",
        "Federal Reserve interest rates",
        "inflation economic outlook",
        "global markets trading",
    ]

    all_news = []
    seen_titles = set()

    try:
        for query in search_queries:
            search = yf_retry(lambda q=query: yf.Search(
                query=q,
                news_count=limit,
                enable_fuzzy_query=True,
            ))

            if search.news:
                for article in search.news:
                    # Handle both flat and nested structures
                    if "content" in article:
                        data = _extract_article_data(article)
                        title = data["title"]
                    else:
                        title = article.get("title", "")

                    # Deduplicate by title
                    if title and title not in seen_titles:
                        seen_titles.add(title)
                        all_news.append(article)

            if len(all_news) >= limit:
                break

        if not all_news:
            return f"No global news found for {curr_date}"

        # Calculate date range
        curr_dt = datetime.strptime(curr_date, "%Y-%m-%d")
        start_dt = curr_dt - relativedelta(days=look_back_days)
        start_date = start_dt.strftime("%Y-%m-%d")

        news_str = ""
        for article in all_news[:limit]:
            # Handle both flat and nested structures
            if "content" in article:
                data = _extract_article_data(article)
                # Skip articles published after curr_date (look-ahead guard)
                if data.get("pub_date"):
                    pub_naive = data["pub_date"].replace(tzinfo=None) if hasattr(data["pub_date"], "replace") else data["pub_date"]
                    if pub_naive > curr_dt + relativedelta(days=1):
                        continue
                title = data["title"]
                publisher = data["publisher"]
                link = data["link"]
                summary = data["summary"]

# ... 文件较长，已截断。总行数：197
```

### tradingagents/graph/__init__.py

```python
# TradingAgents/graph/__init__.py

from .trading_graph import TradingAgentsGraph
from .conditional_logic import ConditionalLogic
from .setup import GraphSetup
from .propagation import Propagator
from .reflection import Reflector
from .signal_processing import SignalProcessor

__all__ = [
    "TradingAgentsGraph",
    "ConditionalLogic",
    "GraphSetup",
    "Propagator",
    "Reflector",
    "SignalProcessor",
]
```

### tradingagents/graph/checkpointer.py

```python
"""LangGraph checkpoint support for resumable analysis runs.

Per-ticker SQLite databases so concurrent tickers don't contend.
"""

from __future__ import annotations

import hashlib
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Generator

from langgraph.checkpoint.sqlite import SqliteSaver

from tradingagents.dataflows.utils import safe_ticker_component


def _db_path(data_dir: str | Path, ticker: str) -> Path:
    """Return the SQLite checkpoint DB path for a ticker."""
    # Reject ticker values that would escape the checkpoints directory.
    safe = safe_ticker_component(ticker).upper()
    p = Path(data_dir) / "checkpoints"
    p.mkdir(parents=True, exist_ok=True)
    return p / f"{safe}.db"


def thread_id(ticker: str, date: str) -> str:
    """Deterministic thread ID for a ticker+date pair."""
    return hashlib.sha256(f"{ticker.upper()}:{date}".encode()).hexdigest()[:16]


@contextmanager
def get_checkpointer(data_dir: str | Path, ticker: str) -> Generator[SqliteSaver, None, None]:
    """Context manager yielding a SqliteSaver backed by a per-ticker DB."""
    db = _db_path(data_dir, ticker)
    conn = sqlite3.connect(str(db), check_same_thread=False)
    try:
        saver = SqliteSaver(conn)
        saver.setup()
        yield saver
    finally:
        conn.close()


def has_checkpoint(data_dir: str | Path, ticker: str, date: str) -> bool:
    """Check whether a resumable checkpoint exists for ticker+date."""
    return checkpoint_step(data_dir, ticker, date) is not None


def checkpoint_step(data_dir: str | Path, ticker: str, date: str) -> int | None:
    """Return the step number of the latest checkpoint, or None if none exists."""
    db = _db_path(data_dir, ticker)
    if not db.exists():
        return None
    tid = thread_id(ticker, date)
    with get_checkpointer(data_dir, ticker) as saver:
        config = {"configurable": {"thread_id": tid}}
        cp = saver.get_tuple(config)
        if cp is None:
            return None
        return cp.metadata.get("step")


def clear_all_checkpoints(data_dir: str | Path) -> int:
    """Remove all checkpoint DBs. Returns number of files deleted."""
    cp_dir = Path(data_dir) / "checkpoints"
    if not cp_dir.exists():
        return 0
    dbs = list(cp_dir.glob("*.db"))
    for db in dbs:
        db.unlink()
    return len(dbs)


def clear_checkpoint(data_dir: str | Path, ticker: str, date: str) -> None:
    """Remove checkpoint for a specific ticker+date by deleting the thread's rows."""
    db = _db_path(data_dir, ticker)
    if not db.exists():
        return
    tid = thread_id(ticker, date)
    conn = sqlite3.connect(str(db))
    try:
        for table in ("writes", "checkpoints"):
            conn.execute(f"DELETE FROM {table} WHERE thread_id = ?", (tid,))
        conn.commit()
    except sqlite3.OperationalError:
        pass
    finally:
        conn.close()
```

### tradingagents/graph/conditional_logic.py

```python
# TradingAgents/graph/conditional_logic.py

from tradingagents.agents.utils.agent_states import AgentState


class ConditionalLogic:
    """Handles conditional logic for determining graph flow."""

    def __init__(self, max_debate_rounds=1, max_risk_discuss_rounds=1):
        """Initialize with configuration parameters."""
        self.max_debate_rounds = max_debate_rounds
        self.max_risk_discuss_rounds = max_risk_discuss_rounds

    def should_continue_market(self, state: AgentState):
        """Determine if market analysis should continue."""
        messages = state["messages"]
        last_message = messages[-1]
        if last_message.tool_calls:
            return "tools_market"
        return "Msg Clear Market"

    def should_continue_social(self, state: AgentState):
        """Determine if social media analysis should continue."""
        messages = state["messages"]
        last_message = messages[-1]
        if last_message.tool_calls:
            return "tools_social"
        return "Msg Clear Social"

    def should_continue_news(self, state: AgentState):
        """Determine if news analysis should continue."""
        messages = state["messages"]
        last_message = messages[-1]
        if last_message.tool_calls:
            return "tools_news"
        return "Msg Clear News"

    def should_continue_fundamentals(self, state: AgentState):
        """Determine if fundamentals analysis should continue."""
        messages = state["messages"]
        last_message = messages[-1]
        if last_message.tool_calls:
            return "tools_fundamentals"
        return "Msg Clear Fundamentals"

    def should_continue_debate(self, state: AgentState) -> str:
        """Determine if debate should continue."""

        if (
            state["investment_debate_state"]["count"] >= 2 * self.max_debate_rounds
        ):  # 3 rounds of back-and-forth between 2 agents
            return "Research Manager"
        if state["investment_debate_state"]["current_response"].startswith("Bull"):
            return "Bear Researcher"
        return "Bull Researcher"

    def should_continue_risk_analysis(self, state: AgentState) -> str:
        """Determine if risk analysis should continue."""
        if (
            state["risk_debate_state"]["count"] >= 3 * self.max_risk_discuss_rounds
        ):  # 3 rounds of back-and-forth between 3 agents
            return "Portfolio Manager"
        if state["risk_debate_state"]["latest_speaker"].startswith("Aggressive"):
            return "Conservative Analyst"
        if state["risk_debate_state"]["latest_speaker"].startswith("Conservative"):
            return "Neutral Analyst"
        return "Aggressive Analyst"
```

### tradingagents/graph/propagation.py

```python
# TradingAgents/graph/propagation.py

from typing import Dict, Any, List, Optional
from tradingagents.agents.utils.agent_states import (
    AgentState,
    InvestDebateState,
    RiskDebateState,
)


class Propagator:
    """Handles state initialization and propagation through the graph."""

    def __init__(self, max_recur_limit=100):
        """Initialize with configuration parameters."""
        self.max_recur_limit = max_recur_limit

    def create_initial_state(
        self, company_name: str, trade_date: str, past_context: str = ""
    ) -> Dict[str, Any]:
        """Create the initial state for the agent graph."""
        return {
            "messages": [("human", company_name)],
            "company_of_interest": company_name,
            "trade_date": str(trade_date),
            "past_context": past_context,
            "investment_debate_state": InvestDebateState(
                {
                    "bull_history": "",
                    "bear_history": "",
                    "history": "",
                    "current_response": "",
                    "judge_decision": "",
                    "count": 0,
                }
            ),
            "risk_debate_state": RiskDebateState(
                {
                    "aggressive_history": "",
                    "conservative_history": "",
                    "neutral_history": "",
                    "history": "",
                    "latest_speaker": "",
                    "current_aggressive_response": "",
                    "current_conservative_response": "",
                    "current_neutral_response": "",
                    "judge_decision": "",
                    "count": 0,
                }
            ),
            "market_report": "",
            "fundamentals_report": "",
            "sentiment_report": "",
            "news_report": "",
        }

    def get_graph_args(self, callbacks: Optional[List] = None) -> Dict[str, Any]:
        """Get arguments for the graph invocation.

        Args:
            callbacks: Optional list of callback handlers for tool execution tracking.
                       Note: LLM callbacks are handled separately via LLM constructor.
        """
        config = {"recursion_limit": self.max_recur_limit}
        if callbacks:
            config["callbacks"] = callbacks
        return {
            "stream_mode": "values",
            "config": config,
        }
```

### tradingagents/graph/reflection.py

```python
# TradingAgents/graph/reflection.py

from typing import Any


class Reflector:
    """Handles reflection on trading decisions."""

    def __init__(self, quick_thinking_llm: Any):
        """Initialize the reflector with an LLM."""
        self.quick_thinking_llm = quick_thinking_llm
        self.log_reflection_prompt = self._get_log_reflection_prompt()

    def _get_log_reflection_prompt(self) -> str:
        """Concise prompt for reflect_on_final_decision (Phase B log entries).

        Produces 2-4 sentences of plain prose — compact enough to be re-injected
        into future agent prompts without bloating the context window.
        """
        return (
            "You are a trading analyst reviewing your own past decision now that the outcome is known.\n"
            "Write exactly 2-4 sentences of plain prose (no bullets, no headers, no markdown).\n\n"
            "Cover in order:\n"
            "1. Was the directional call correct? (cite the alpha figure)\n"
            "2. Which part of the investment thesis held or failed?\n"
            "3. One concrete lesson to apply to the next similar analysis.\n\n"
            "Be specific and terse. Your output will be stored verbatim in a decision log "
            "and re-read by future analysts, so every word must earn its place."
        )

    def reflect_on_final_decision(
        self,
        final_decision: str,
        raw_return: float,
        alpha_return: float,
    ) -> str:
        """Single reflection call on the final trade decision with outcome context.

        Used by Phase B deferred reflection. The final_trade_decision already
        synthesises all analyst insights, so no separate market context is needed.
        """
        messages = [
            ("system", self.log_reflection_prompt),
            (
                "human",
                (
                    f"Raw return: {raw_return:+.1%}\n"
                    f"Alpha vs SPY: {alpha_return:+.1%}\n\n"
                    f"Final Decision:\n{final_decision}"
                ),
            ),
        ]
        return self.quick_thinking_llm.invoke(messages).content
```

### tradingagents/graph/setup.py

```python
# TradingAgents/graph/setup.py

from typing import Any, Dict
from langgraph.graph import END, START, StateGraph
from langgraph.prebuilt import ToolNode

from tradingagents.agents import *
from tradingagents.agents.utils.agent_states import AgentState

from .conditional_logic import ConditionalLogic


class GraphSetup:
    """Handles the setup and configuration of the agent graph."""

    def __init__(
        self,
        quick_thinking_llm: Any,
        deep_thinking_llm: Any,
        tool_nodes: Dict[str, ToolNode],
        conditional_logic: ConditionalLogic,
    ):
        """Initialize with required components."""
        self.quick_thinking_llm = quick_thinking_llm
        self.deep_thinking_llm = deep_thinking_llm
        self.tool_nodes = tool_nodes
        self.conditional_logic = conditional_logic

    def setup_graph(
        self, selected_analysts=["market", "social", "news", "fundamentals"]
    ):
        """Set up and compile the agent workflow graph.

        Args:
            selected_analysts (list): List of analyst types to include. Options are:
                - "market": Market analyst
                - "social": Social media analyst
                - "news": News analyst
                - "fundamentals": Fundamentals analyst
        """
        if len(selected_analysts) == 0:
            raise ValueError("Trading Agents Graph Setup Error: no analysts selected!")

        # Create analyst nodes
        analyst_nodes = {}
        delete_nodes = {}
        tool_nodes = {}

        if "market" in selected_analysts:
            analyst_nodes["market"] = create_market_analyst(
                self.quick_thinking_llm
            )
            delete_nodes["market"] = create_msg_delete()
            tool_nodes["market"] = self.tool_nodes["market"]

        if "social" in selected_analysts:
            analyst_nodes["social"] = create_social_media_analyst(
                self.quick_thinking_llm
            )
            delete_nodes["social"] = create_msg_delete()
            tool_nodes["social"] = self.tool_nodes["social"]

        if "news" in selected_analysts:
            analyst_nodes["news"] = create_news_analyst(
                self.quick_thinking_llm
            )
            delete_nodes["news"] = create_msg_delete()
            tool_nodes["news"] = self.tool_nodes["news"]

        if "fundamentals" in selected_analysts:
            analyst_nodes["fundamentals"] = create_fundamentals_analyst(
                self.quick_thinking_llm
            )
            delete_nodes["fundamentals"] = create_msg_delete()
            tool_nodes["fundamentals"] = self.tool_nodes["fundamentals"]

        # Create researcher and manager nodes
        bull_researcher_node = create_bull_researcher(self.quick_thinking_llm)
        bear_researcher_node = create_bear_researcher(self.quick_thinking_llm)
        research_manager_node = create_research_manager(self.deep_thinking_llm)
        trader_node = create_trader(self.quick_thinking_llm)

        # Create risk analysis nodes
        aggressive_analyst = create_aggressive_debator(self.quick_thinking_llm)
        neutral_analyst = create_neutral_debator(self.quick_thinking_llm)
        conservative_analyst = create_conservative_debator(self.quick_thinking_llm)
        portfolio_manager_node = create_portfolio_manager(self.deep_thinking_llm)

        # Create workflow
        workflow = StateGraph(AgentState)

        # Add analyst nodes to the graph
        for analyst_type, node in analyst_nodes.items():
            workflow.add_node(f"{analyst_type.capitalize()} Analyst", node)
            workflow.add_node(
                f"Msg Clear {analyst_type.capitalize()}", delete_nodes[analyst_type]
            )
            workflow.add_node(f"tools_{analyst_type}", tool_nodes[analyst_type])

        # Add other nodes
        workflow.add_node("Bull Researcher", bull_researcher_node)
        workflow.add_node("Bear Researcher", bear_researcher_node)
        workflow.add_node("Research Manager", research_manager_node)
        workflow.add_node("Trader", trader_node)
        workflow.add_node("Aggressive Analyst", aggressive_analyst)
        workflow.add_node("Neutral Analyst", neutral_analyst)
        workflow.add_node("Conservative Analyst", conservative_analyst)
        workflow.add_node("Portfolio Manager", portfolio_manager_node)

        # Define edges
        # Start with the first analyst
        first_analyst = selected_analysts[0]
        workflow.add_edge(START, f"{first_analyst.capitalize()} Analyst")

        # Connect analysts in sequence
        for i, analyst_type in enumerate(selected_analysts):
            current_analyst = f"{analyst_type.capitalize()} Analyst"
            current_tools = f"tools_{analyst_type}"
            current_clear = f"Msg Clear {analyst_type.capitalize()}"

            # Add conditional edges for current analyst
            workflow.add_conditional_edges(
                current_analyst,
                getattr(self.conditional_logic, f"should_continue_{analyst_type}"),
                [current_tools, current_clear],
            )
            workflow.add_edge(current_tools, current_analyst)

            # Connect to next analyst or to Bull Researcher if this is the last analyst
            if i < len(selected_analysts) - 1:
                next_analyst = f"{selected_analysts[i+1].capitalize()} Analyst"
                workflow.add_edge(current_clear, next_analyst)
            else:
                workflow.add_edge(current_clear, "Bull Researcher")

        # Add remaining edges
        workflow.add_conditional_edges(
            "Bull Researcher",
            self.conditional_logic.should_continue_debate,
            {
                "Bear Researcher": "Bear Researcher",
                "Research Manager": "Research Manager",
            },
        )
        workflow.add_conditional_edges(
            "Bear Researcher",
            self.conditional_logic.should_continue_debate,
            {
                "Bull Researcher": "Bull Researcher",
                "Research Manager": "Research Manager",
            },
        )
        workflow.add_edge("Research Manager", "Trader")
        workflow.add_edge("Trader", "Aggressive Analyst")
        workflow.add_conditional_edges(
            "Aggressive Analyst",
            self.conditional_logic.should_continue_risk_analysis,
            {
                "Conservative Analyst": "Conservative Analyst",
                "Portfolio Manager": "Portfolio Manager",
            },
        )
        workflow.add_conditional_edges(
            "Conservative Analyst",
            self.conditional_logic.should_continue_risk_analysis,
            {
                "Neutral Analyst": "Neutral Analyst",
                "Portfolio Manager": "Portfolio Manager",
            },
        )
        workflow.add_conditional_edges(
            "Neutral Analyst",
            self.conditional_logic.should_continue_risk_analysis,
            {
                "Aggressive Analyst": "Aggressive Analyst",
                "Portfolio Manager": "Portfolio Manager",
            },
        )

        workflow.add_edge("Portfolio Manager", END)

# ... 文件较长，已截断。总行数：182
```

### tradingagents/graph/signal_processing.py

```python
"""Extract the 5-tier portfolio rating from the Portfolio Manager's decision.

The Portfolio Manager produces a typed ``PortfolioDecision`` via structured
output and renders it to markdown that always carries a ``**Rating**: X``
header (see :func:`tradingagents.agents.schemas.render_pm_decision`).  The
deterministic heuristic in :mod:`tradingagents.agents.utils.rating` is more
than sufficient to extract that rating; no extra LLM call is needed.

This module exists for backwards compatibility with callers that expect a
``SignalProcessor.process_signal(text)`` interface.
"""

from __future__ import annotations

from typing import Any

from tradingagents.agents.utils.rating import parse_rating


class SignalProcessor:
    """Read the 5-tier rating out of a Portfolio Manager decision."""

    def __init__(self, quick_thinking_llm: Any = None):
        # The LLM argument is accepted for backwards compatibility but no
        # longer used: the PM's structured output guarantees the rating is
        # parseable from the rendered markdown without a second LLM call.
        self.quick_thinking_llm = quick_thinking_llm

    def process_signal(self, full_signal: str) -> str:
        """Return one of Buy / Overweight / Hold / Underweight / Sell."""
        return parse_rating(full_signal)
```

### tradingagents/graph/trading_graph.py

```python
# TradingAgents/graph/trading_graph.py

import logging
import os
from pathlib import Path
import json
from datetime import datetime, timedelta
from typing import Dict, Any, Tuple, List, Optional

import yfinance as yf

logger = logging.getLogger(__name__)

from langgraph.prebuilt import ToolNode

from tradingagents.llm_clients import create_llm_client

from tradingagents.agents import *
from tradingagents.default_config import DEFAULT_CONFIG
from tradingagents.agents.utils.memory import TradingMemoryLog
from tradingagents.dataflows.utils import safe_ticker_component
from tradingagents.agents.utils.agent_states import (
    AgentState,
    InvestDebateState,
    RiskDebateState,
)
from tradingagents.dataflows.config import set_config

# Import the new abstract tool methods from agent_utils
from tradingagents.agents.utils.agent_utils import (
    get_stock_data,
    get_indicators,
    get_fundamentals,
    get_balance_sheet,
    get_cashflow,
    get_income_statement,
    get_news,
    get_insider_transactions,
    get_global_news
)

from .checkpointer import checkpoint_step, clear_checkpoint, get_checkpointer, thread_id
from .conditional_logic import ConditionalLogic
from .setup import GraphSetup
from .propagation import Propagator
from .reflection import Reflector
from .signal_processing import SignalProcessor


class TradingAgentsGraph:
    """Main class that orchestrates the trading agents framework."""

    def __init__(
        self,
        selected_analysts=["market", "social", "news", "fundamentals"],
        debug=False,
        config: Dict[str, Any] = None,
        callbacks: Optional[List] = None,
    ):
        """Initialize the trading agents graph and components.

        Args:
            selected_analysts: List of analyst types to include
            debug: Whether to run in debug mode
            config: Configuration dictionary. If None, uses default config
            callbacks: Optional list of callback handlers (e.g., for tracking LLM/tool stats)
        """
        self.debug = debug
        self.config = config or DEFAULT_CONFIG
        self.callbacks = callbacks or []

        # Update the interface's config
        set_config(self.config)

        # Create necessary directories
        os.makedirs(self.config["data_cache_dir"], exist_ok=True)
        os.makedirs(self.config["results_dir"], exist_ok=True)

        # Initialize LLMs with provider-specific thinking configuration
        llm_kwargs = self._get_provider_kwargs()

        # Add callbacks to kwargs if provided (passed to LLM constructor)
        if self.callbacks:
            llm_kwargs["callbacks"] = self.callbacks

        deep_client = create_llm_client(
            provider=self.config["llm_provider"],
            model=self.config["deep_think_llm"],
            base_url=self.config.get("backend_url"),
            **llm_kwargs,
        )
        quick_client = create_llm_client(
            provider=self.config["llm_provider"],
            model=self.config["quick_think_llm"],
            base_url=self.config.get("backend_url"),
            **llm_kwargs,
        )

        self.deep_thinking_llm = deep_client.get_llm()
        self.quick_thinking_llm = quick_client.get_llm()
        
        self.memory_log = TradingMemoryLog(self.config)

        # Create tool nodes
        self.tool_nodes = self._create_tool_nodes()

        # Initialize components
        self.conditional_logic = ConditionalLogic(
            max_debate_rounds=self.config["max_debate_rounds"],
            max_risk_discuss_rounds=self.config["max_risk_discuss_rounds"],
        )
        self.graph_setup = GraphSetup(
            self.quick_thinking_llm,
            self.deep_thinking_llm,
            self.tool_nodes,
            self.conditional_logic,
        )

        self.propagator = Propagator()
        self.reflector = Reflector(self.quick_thinking_llm)
        self.signal_processor = SignalProcessor(self.quick_thinking_llm)

        # State tracking
        self.curr_state = None
        self.ticker = None
        self.log_states_dict = {}  # date to full state dict

        # Set up the graph: keep the workflow for recompilation with a checkpointer.
        self.workflow = self.graph_setup.setup_graph(selected_analysts)
        self.graph = self.workflow.compile()
        self._checkpointer_ctx = None

    def _get_provider_kwargs(self) -> Dict[str, Any]:
        """Get provider-specific kwargs for LLM client creation."""
        kwargs = {}
        provider = self.config.get("llm_provider", "").lower()

        if provider == "google":
            thinking_level = self.config.get("google_thinking_level")
            if thinking_level:
                kwargs["thinking_level"] = thinking_level

        elif provider == "openai":
            reasoning_effort = self.config.get("openai_reasoning_effort")
            if reasoning_effort:
                kwargs["reasoning_effort"] = reasoning_effort

        elif provider == "anthropic":
            effort = self.config.get("anthropic_effort")
            if effort:
                kwargs["effort"] = effort

        return kwargs

    def _create_tool_nodes(self) -> Dict[str, ToolNode]:
        """Create tool nodes for different data sources using abstract methods."""
        return {
            "market": ToolNode(
                [
                    # Core stock data tools
                    get_stock_data,
                    # Technical indicators
                    get_indicators,
                ]
            ),
            "social": ToolNode(
                [
                    # News tools for social media analysis
                    get_news,
                ]
            ),
            "news": ToolNode(
                [
                    # News and insider information
                    get_news,
                    get_global_news,
                    get_insider_transactions,
                ]
            ),
            "fundamentals": ToolNode(

# ... 文件较长，已截断。总行数：394
```

### tradingagents/llm_clients/__init__.py

```python
from .base_client import BaseLLMClient
from .factory import create_llm_client

__all__ = ["BaseLLMClient", "create_llm_client"]
```

### tradingagents/llm_clients/anthropic_client.py

```python
from typing import Any, Optional

from langchain_anthropic import ChatAnthropic

from .base_client import BaseLLMClient, normalize_content
from .validators import validate_model

_PASSTHROUGH_KWARGS = (
    "timeout", "max_retries", "api_key", "max_tokens",
    "callbacks", "http_client", "http_async_client", "effort",
)


class NormalizedChatAnthropic(ChatAnthropic):
    """ChatAnthropic with normalized content output.

    Claude models with extended thinking or tool use return content as a
    list of typed blocks. This normalizes to string for consistent
    downstream handling.
    """

    def invoke(self, input, config=None, **kwargs):
        return normalize_content(super().invoke(input, config, **kwargs))


class AnthropicClient(BaseLLMClient):
    """Client for Anthropic Claude models."""

    def __init__(self, model: str, base_url: Optional[str] = None, **kwargs):
        super().__init__(model, base_url, **kwargs)

    def get_llm(self) -> Any:
        """Return configured ChatAnthropic instance."""
        self.warn_if_unknown_model()
        llm_kwargs = {"model": self.model}

        if self.base_url:
            llm_kwargs["base_url"] = self.base_url

        for key in _PASSTHROUGH_KWARGS:
            if key in self.kwargs:
                llm_kwargs[key] = self.kwargs[key]

        return NormalizedChatAnthropic(**llm_kwargs)

    def validate_model(self) -> bool:
        """Validate model for Anthropic."""
        return validate_model("anthropic", self.model)
```
