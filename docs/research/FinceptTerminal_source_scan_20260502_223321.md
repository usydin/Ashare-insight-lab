# FinceptTerminal 源码初步扫描报告

生成时间：2026-05-02 22:33:21
源码路径：/Users/balwyn/Downloads/FinceptTerminal-main

## 1. Git 信息

未检测到 .git 目录，可能是 GitHub 下载的 zip 解压包。

## 2. 顶层目录

```text
total 776
drwxrwxr-x@ 16 balwyn  staff     512  1 May 22:07 .
drwx------@ 57 balwyn  staff    1824  2 May 22:31 ..
-rw-rw-r--@  1 balwyn  staff     308  1 May 22:07 .dockerignore
-rw-rw-r--@  1 balwyn  staff      42  1 May 22:07 .gitattributes
drwxrwxr-x@ 10 balwyn  staff     320  1 May 22:07 .github
-rw-rw-r--@  1 balwyn  staff    4882  1 May 22:07 .gitignore
-rw-rw-r--@  1 balwyn  staff   11705  1 May 22:07 Dockerfile
drwxrwxr-x@ 11 balwyn  staff     352  1 May 22:07 docs
-rw-rw-r--@  1 balwyn  staff  307520  1 May 22:07 fincept_icon.ico
drwxrwxr-x@ 20 balwyn  staff     640  1 May 22:07 fincept-qt
-rw-rw-r--@  1 balwyn  staff    3298  1 May 22:07 funding.json
drwxrwxr-x@  9 balwyn  staff     288  1 May 22:07 images
-rw-rw-r--@  1 balwyn  staff   14750  1 May 22:07 LICENSE
-rw-rw-r--@  1 balwyn  staff   19928  1 May 22:07 README.md
-rwxr-xr-x@  1 balwyn  staff    9582  1 May 22:07 setup.sh
-rw-rw-r--@  1 balwyn  staff    1760  1 May 22:07 updates.json
```

## 3. 目录结构，最多 4 层

```text
.
./.github
./.github/ISSUE_TEMPLATE
./.github/PULL_REQUEST_TEMPLATE
./.github/scripts
./.github/workflows
./docs
./docs/translations
./fincept-qt
./fincept-qt/.claude
./fincept-qt/cmake
./fincept-qt/cmake/patches
./fincept-qt/docs
./fincept-qt/docs/agents
./fincept-qt/docs/datahub-phases
./fincept-qt/packaging
./fincept-qt/packaging/installer
./fincept-qt/packaging/installer/config
./fincept-qt/packaging/installer/packages
./fincept-qt/packaging/linux
./fincept-qt/plans
./fincept-qt/resources
./fincept-qt/resources/wallet
./fincept-qt/resources/wallet/vendor
./fincept-qt/scripts
./fincept-qt/scripts/agents
./fincept-qt/scripts/agents/_tools
./fincept-qt/scripts/agents/deepagents
./fincept-qt/scripts/agents/EconomicAgents
./fincept-qt/scripts/agents/finagent_core
./fincept-qt/scripts/agents/GeopoliticsAgents
./fincept-qt/scripts/agents/hedgeFundAgents
./fincept-qt/scripts/agents/rdagents
./fincept-qt/scripts/agents/TraderInvestorsAgent
./fincept-qt/scripts/agno_trading
./fincept-qt/scripts/agno_trading/agents
./fincept-qt/scripts/agno_trading/config
./fincept-qt/scripts/agno_trading/core
./fincept-qt/scripts/agno_trading/db
./fincept-qt/scripts/agno_trading/framework
./fincept-qt/scripts/agno_trading/tools
./fincept-qt/scripts/agno_trading/utils
./fincept-qt/scripts/ai_quant_lab
./fincept-qt/scripts/algo_trading
./fincept-qt/scripts/alpha_arena
./fincept-qt/scripts/alpha_arena/config
./fincept-qt/scripts/alpha_arena/core
./fincept-qt/scripts/alpha_arena/types
./fincept-qt/scripts/alpha_arena/utils
./fincept-qt/scripts/Analytics
./fincept-qt/scripts/Analytics/alternateInvestment
./fincept-qt/scripts/Analytics/backtesting
./fincept-qt/scripts/Analytics/corporateFinance
./fincept-qt/scripts/Analytics/derivatives
./fincept-qt/scripts/Analytics/economics
./fincept-qt/scripts/Analytics/equityInvestment
./fincept-qt/scripts/Analytics/ffn_wrapper
./fincept-qt/scripts/Analytics/finanicalanalysis
./fincept-qt/scripts/Analytics/finrl
./fincept-qt/scripts/Analytics/fixedIncome
./fincept-qt/scripts/Analytics/fortitudo_tech_wrapper
./fincept-qt/scripts/Analytics/functime_wrapper
./fincept-qt/scripts/Analytics/gluonts_wrapper
./fincept-qt/scripts/Analytics/gs_quant_wrapper
./fincept-qt/scripts/Analytics/pmdarima_wrapper
./fincept-qt/scripts/Analytics/portfolioManagement
./fincept-qt/scripts/Analytics/py_vollib_wrapper
./fincept-qt/scripts/Analytics/pypme_wrapper
./fincept-qt/scripts/Analytics/pyportfolioopt_wrapper
./fincept-qt/scripts/Analytics/python_skfolio_lib
./fincept-qt/scripts/Analytics/quant
./fincept-qt/scripts/Analytics/statsmodels_wrapper
./fincept-qt/scripts/Analytics/talipp_wrapper
./fincept-qt/scripts/Analytics/technical_analysis
./fincept-qt/scripts/Analytics/tsmoothie_wrapper
./fincept-qt/scripts/Analytics/vnpy_wrapper
./fincept-qt/scripts/exchange
./fincept-qt/scripts/mcp
./fincept-qt/scripts/mcp/edgar
./fincept-qt/scripts/strategies
./fincept-qt/scripts/strategies/alphas
./fincept-qt/scripts/strategies/benchmarks
./fincept-qt/scripts/strategies/Execution
./fincept-qt/scripts/strategies/fincept_engine
./fincept-qt/scripts/strategies/Portfolio
./fincept-qt/scripts/strategies/Risk
./fincept-qt/scripts/strategies/Selection
./fincept-qt/scripts/technicals
./fincept-qt/scripts/vision_quant
./fincept-qt/scripts/vision_quant/models
./fincept-qt/scripts/voice
./fincept-qt/src
./fincept-qt/src/ai_chat
./fincept-qt/src/app
./fincept-qt/src/auth
./fincept-qt/src/auth/lock
./fincept-qt/src/core
./fincept-qt/src/core/actions
./fincept-qt/src/core/components
./fincept-qt/src/core/config
./fincept-qt/src/core/crash
./fincept-qt/src/core/debug
./fincept-qt/src/core/events
./fincept-qt/src/core/identity
./fincept-qt/src/core/keys
./fincept-qt/src/core/layout
./fincept-qt/src/core/logging
./fincept-qt/src/core/net
./fincept-qt/src/core/panel
./fincept-qt/src/core/profile
./fincept-qt/src/core/report
./fincept-qt/src/core/result
./fincept-qt/src/core/screen
./fincept-qt/src/core/session
./fincept-qt/src/core/symbol
./fincept-qt/src/core/telemetry
./fincept-qt/src/core/window
./fincept-qt/src/datahub
./fincept-qt/src/mcp
./fincept-qt/src/mcp/dispatch
./fincept-qt/src/mcp/tools
./fincept-qt/src/network
./fincept-qt/src/network/http
./fincept-qt/src/network/websocket
./fincept-qt/src/python
./fincept-qt/src/screens
./fincept-qt/src/screens/about
./fincept-qt/src/screens/agent_config
./fincept-qt/src/screens/ai_quant_lab
./fincept-qt/src/screens/akshare
./fincept-qt/src/screens/algo_trading
./fincept-qt/src/screens/alpha_arena
./fincept-qt/src/screens/alt_investments
./fincept-qt/src/screens/asia_markets
./fincept-qt/src/screens/auth
./fincept-qt/src/screens/backtesting
./fincept-qt/src/screens/chat_mode
./fincept-qt/src/screens/code_editor
./fincept-qt/src/screens/crypto_center
./fincept-qt/src/screens/crypto_trading
./fincept-qt/src/screens/dashboard
./fincept-qt/src/screens/data_mapping
./fincept-qt/src/screens/data_sources
./fincept-qt/src/screens/dbnomics
./fincept-qt/src/screens/derivatives
./fincept-qt/src/screens/devtools
./fincept-qt/src/screens/docs
./fincept-qt/src/screens/economics
./fincept-qt/src/screens/equity_research
./fincept-qt/src/screens/equity_trading
./fincept-qt/src/screens/excel
./fincept-qt/src/screens/file_manager
./fincept-qt/src/screens/forum
./fincept-qt/src/screens/geopolitics
./fincept-qt/src/screens/gov_data
./fincept-qt/src/screens/info
./fincept-qt/src/screens/launchpad
./fincept-qt/src/screens/ma_analytics
./fincept-qt/src/screens/maritime
./fincept-qt/src/screens/markets
./fincept-qt/src/screens/mcp_servers
./fincept-qt/src/screens/news
./fincept-qt/src/screens/node_editor
./fincept-qt/src/screens/notes
./fincept-qt/src/screens/polymarket
./fincept-qt/src/screens/portfolio
./fincept-qt/src/screens/profile
./fincept-qt/src/screens/quantlib
./fincept-qt/src/screens/recovery
./fincept-qt/src/screens/relationship_map
./fincept-qt/src/screens/report_builder
./fincept-qt/src/screens/settings
./fincept-qt/src/screens/setup
./fincept-qt/src/screens/support
./fincept-qt/src/screens/surface_analytics
./fincept-qt/src/screens/trade_viz
./fincept-qt/src/screens/watchlist
./fincept-qt/src/services
./fincept-qt/src/services/agents
./fincept-qt/src/services/ai_quant_lab
./fincept-qt/src/services/akshare
./fincept-qt/src/services/algo_trading
./fincept-qt/src/services/alpha_arena
./fincept-qt/src/services/asia_markets
./fincept-qt/src/services/backtesting
./fincept-qt/src/services/billing
./fincept-qt/src/services/crypto
./fincept-qt/src/services/data_normalization
./fincept-qt/src/services/databento
./fincept-qt/src/services/dbnomics
./fincept-qt/src/services/economics
./fincept-qt/src/services/equity
./fincept-qt/src/services/file_manager
./fincept-qt/src/services/forum
./fincept-qt/src/services/geopolitics
./fincept-qt/src/services/gov_data
./fincept-qt/src/services/ma_analytics
./fincept-qt/src/services/maritime
./fincept-qt/src/services/markets
./fincept-qt/src/services/news
./fincept-qt/src/services/notifications
./fincept-qt/src/services/polymarket
./fincept-qt/src/services/portfolio
./fincept-qt/src/services/prediction
./fincept-qt/src/services/pushpins
./fincept-qt/src/services/python_cli
./fincept-qt/src/services/quantlib
./fincept-qt/src/services/relationship_map
./fincept-qt/src/services/report_builder
./fincept-qt/src/services/sectors
./fincept-qt/src/services/stt
./fincept-qt/src/services/tts
./fincept-qt/src/services/updater
./fincept-qt/src/services/voice_trigger
./fincept-qt/src/services/wallet
./fincept-qt/src/services/workflow
./fincept-qt/src/services/workspace
./fincept-qt/src/storage
./fincept-qt/src/storage/cache
./fincept-qt/src/storage/repositories
./fincept-qt/src/storage/secure
./fincept-qt/src/storage/sqlite
./fincept-qt/src/storage/workspace
./fincept-qt/src/trading
./fincept-qt/src/trading/auth
./fincept-qt/src/trading/brokers
./fincept-qt/src/trading/exchanges
./fincept-qt/src/trading/instruments
./fincept-qt/src/trading/websocket
./fincept-qt/src/ui
./fincept-qt/src/ui/charts
./fincept-qt/src/ui/command
./fincept-qt/src/ui/components
./fincept-qt/src/ui/debug
./fincept-qt/src/ui/error
./fincept-qt/src/ui/markdown
./fincept-qt/src/ui/navigation
./fincept-qt/src/ui/notifications
./fincept-qt/src/ui/pushpins
./fincept-qt/src/ui/tables
./fincept-qt/src/ui/theme
./fincept-qt/src/ui/widgets
./fincept-qt/src/ui/workspace
./fincept-qt/tests
./fincept-qt/tests/datahub
./fincept-qt/tests/mcp
./images
```

## 4. 主要文件清单，最多 300 个

```text
./.dockerignore
./.gitattributes
./.github/CONTRIBUTING.md
./.github/FUNDING.yml
./.github/ISSUE_TEMPLATE/bug_report.md
./.github/ISSUE_TEMPLATE/config.yml
./.github/ISSUE_TEMPLATE/documentation.md
./.github/ISSUE_TEMPLATE/feature_request.md
./.github/ISSUE_TEMPLATE/improvement.md
./.github/ISSUE_TEMPLATE/performance_issues.md
./.github/labels.json
./.github/MAINTAINERS.md
./.github/PULL_REQUEST_TEMPLATE/pull_request_for_terminal.md
./.github/scripts/generate_updates_manifest.py
./.github/scripts/sync_scripts.sh
./.github/scripts/update_readme_table.py
./.github/workflows/build-cpp.yml
./.github/workflows/lint.yml
./.github/workflows/pr-gate.yml
./.github/workflows/pr-stale-close.yml
./.github/workflows/release.yml
./.github/workflows/sync-labels.yml
./.github/workflows/sync-repo-topics.yml
./.github/workflows/test-setup.yml
./.github/workflows/translate-readme.yml
./.gitignore
./Dockerfile
./docs/ARCHITECTURE.md
./docs/CODE_OF_CONDUCT.md
./docs/COMMERCIAL_LICENSE.md
./docs/CONTRIBUTING.md
./docs/CPP_CONTRIBUTOR_GUIDE.md
./docs/CRYPTO_WALLET_CONNECT.md
./docs/GETTING_STARTED.md
./docs/PYTHON_CONTRIBUTOR_GUIDE.md
./docs/translations/README.de.md
./docs/translations/README.es.md
./docs/translations/README.fr.md
./docs/translations/README.hi.md
./docs/translations/README.ja.md
./docs/translations/README.ko.md
./docs/translations/README.zh-CN.md
./fincept_icon.ico
./fincept-qt/.clang-format
./fincept-qt/.clang-tidy
./fincept-qt/.clangd
./fincept-qt/.claude/scheduled_tasks.lock
./fincept-qt/.cppcheck-suppressions
./fincept-qt/build-clang.pid
./fincept-qt/cmake/patches/qgeoview_remove_agl.cmake
./fincept-qt/cmake/prune_scripts_junk.cmake
./fincept-qt/CMakeLists.txt
./fincept-qt/CMakePresets.json
./fincept-qt/DATAHUB_ARCHITECTURE.md
./fincept-qt/DATAHUB_PHASES.md
./fincept-qt/docs/agents/datahub-guide.md
./fincept-qt/docs/ANGELONE_QT_CROSSCHECK.md
./fincept-qt/docs/backtesting-provider-process.md
./fincept-qt/docs/CRYPTO_CENTER_PHASE_2.md
./fincept-qt/docs/CRYPTO_CENTER_PHASE_3.md
./fincept-qt/docs/CRYPTO_CENTER_PHASE_4.md
./fincept-qt/docs/CRYPTO_CENTER_PHASE_5.md
./fincept-qt/docs/CRYPTO_WALLET_CONNECT.md
./fincept-qt/docs/DATAHUB_TOPICS.md
./fincept-qt/docs/datahub-phases/phase-02-market-data-pilot.md
./fincept-qt/docs/datahub-phases/phase-03-market-data-full-migration.md
./fincept-qt/docs/datahub-phases/phase-04-websocket-producers.md
./fincept-qt/docs/datahub-phases/phase-05-news.md
./fincept-qt/docs/datahub-phases/phase-06-economics-dbnomics.md
./fincept-qt/docs/datahub-phases/phase-07-broker-account-streams.md
./fincept-qt/docs/datahub-phases/phase-08-geopolitics-maritime-govdata.md
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md
./fincept-qt/docs/datahub-phases/phase-10-enforcement-cleanup.md
./fincept-qt/docs/MCP_TOOLS_GUIDE.md
./fincept-qt/docs/polymarket_api_links.txt
./fincept-qt/packaging/installer/config/.gitkeep
./fincept-qt/packaging/linux/AppImageBuilder.yml
./fincept-qt/packaging/linux/AppRun
./fincept-qt/packaging/linux/fincept-terminal.appdata.xml
./fincept-qt/packaging/linux/fincept-terminal.desktop
./fincept-qt/plans/crypto-center-future-phases.md
./fincept-qt/plans/crypto-center-phase-2.md
./fincept-qt/plans/crypto-center-security-walkthrough.md
./fincept-qt/plans/crypto-center-wallet-connect.md
./fincept-qt/resources/app.rc.in
./fincept-qt/resources/component_catalog.json
./fincept-qt/resources/demo_portfolio.json
./fincept-qt/resources/fincept.ico
./fincept-qt/resources/requirements-numpy1.txt
./fincept-qt/resources/requirements-numpy2.txt
./fincept-qt/resources/wallet/connect.html
./fincept-qt/resources/wallet/swap.html
./fincept-qt/resources/wallet/vendor/README.md
./fincept-qt/resources/wallet/vendor/web3.js
./fincept-qt/scripts/.gitkeep
./fincept-qt/scripts/abs_data.py
./fincept-qt/scripts/acled_data.py
./fincept-qt/scripts/adb_data_extended.py
./fincept-qt/scripts/adb_data.py
./fincept-qt/scripts/afdb_data.py
./fincept-qt/scripts/agents/_tools/apply_economic_agents.py
./fincept-qt/scripts/agents/_tools/apply_geopolitics_batch1.py
./fincept-qt/scripts/agents/_tools/apply_geopolitics_batch2.py
./fincept-qt/scripts/agents/_tools/apply_geopolitics_batch3.py
./fincept-qt/scripts/agents/_tools/apply_geopolitics_batch4.py
./fincept-qt/scripts/agents/_tools/apply_trader_investors_batch1.py
./fincept-qt/scripts/agents/_tools/apply_trader_investors_batch2.py
./fincept-qt/scripts/agents/_tools/apply_trader_investors_batch3.py
./fincept-qt/scripts/agents/_tools/migrate_bundled_configs.py
./fincept-qt/scripts/agents/_tools/verify_all_agents.py
./fincept-qt/scripts/agents/deepagents/__init__.py
./fincept-qt/scripts/agents/deepagents/agent.py
./fincept-qt/scripts/agents/deepagents/backends.py
./fincept-qt/scripts/agents/deepagents/cli.py
./fincept-qt/scripts/agents/deepagents/models.py
./fincept-qt/scripts/agents/deepagents/orchestrator.py
./fincept-qt/scripts/agents/deepagents/subagents.py
./fincept-qt/scripts/agents/finagent_core/__init__.py
./fincept-qt/scripts/agents/finagent_core/agent_factory.py
./fincept-qt/scripts/agents/finagent_core/agent_loader.py
./fincept-qt/scripts/agents/finagent_core/config_loader.py
./fincept-qt/scripts/agents/finagent_core/core_agent_stream.py
./fincept-qt/scripts/agents/finagent_core/core_agent.py
./fincept-qt/scripts/agents/finagent_core/execution_planner.py
./fincept-qt/scripts/agents/finagent_core/main.py
./fincept-qt/scripts/agents/finagent_core/paper_trading_bridge.py
./fincept-qt/scripts/agents/finagent_core/persona_registry.py
./fincept-qt/scripts/agents/finagent_core/persona_runtime.py
./fincept-qt/scripts/agents/finagent_core/README.md
./fincept-qt/scripts/agents/finagent_core/repositories.py
./fincept-qt/scripts/agents/finagent_core/resources.py
./fincept-qt/scripts/agents/finagent_core/super_agent.py
./fincept-qt/scripts/agents/finagent_core/task_state.py
./fincept-qt/scripts/agents/GeopoliticsAgents/README.md
./fincept-qt/scripts/agents/rdagents/__init__.py
./fincept-qt/scripts/agents/rdagents/cli.py
./fincept-qt/scripts/agents/rdagents/config.py
./fincept-qt/scripts/agents/rdagents/loops.py
./fincept-qt/scripts/agents/rdagents/mcp_server.py
./fincept-qt/scripts/agents/rdagents/mcp_tools.py
./fincept-qt/scripts/agents/rdagents/task_manager.py
./fincept-qt/scripts/agents/README.md
./fincept-qt/scripts/agno_trading_service.py
./fincept-qt/scripts/agno_trading/__init__.py
./fincept-qt/scripts/agno_trading/agents/__init__.py
./fincept-qt/scripts/agno_trading/config/__init__.py
./fincept-qt/scripts/agno_trading/config/models.py
./fincept-qt/scripts/agno_trading/config/settings.py
./fincept-qt/scripts/agno_trading/core/__init__.py
./fincept-qt/scripts/agno_trading/core/agent_evolution.py
./fincept-qt/scripts/agno_trading/core/agent_manager.py
./fincept-qt/scripts/agno_trading/core/auto_trader.py
./fincept-qt/scripts/agno_trading/core/base_agent.py
./fincept-qt/scripts/agno_trading/core/debate_orchestrator.py
./fincept-qt/scripts/agno_trading/core/trade_executor.py
./fincept-qt/scripts/agno_trading/core/workflow_engine.py
./fincept-qt/scripts/agno_trading/db/database_manager.py
./fincept-qt/scripts/agno_trading/db/schema.sql
./fincept-qt/scripts/agno_trading/framework/__init__.py
./fincept-qt/scripts/agno_trading/framework/base_composer.py
./fincept-qt/scripts/agno_trading/framework/base_execution.py
./fincept-qt/scripts/agno_trading/framework/base_features.py
./fincept-qt/scripts/agno_trading/framework/base_portfolio.py
./fincept-qt/scripts/agno_trading/framework/competition_runtime.py
./fincept-qt/scripts/agno_trading/framework/decision_coordinator.py
./fincept-qt/scripts/agno_trading/framework/features_pipeline.py
./fincept-qt/scripts/agno_trading/framework/llm_composer.py
./fincept-qt/scripts/agno_trading/framework/market_data_source.py
./fincept-qt/scripts/agno_trading/framework/paper_execution.py
./fincept-qt/scripts/agno_trading/framework/portfolio_service.py
./fincept-qt/scripts/agno_trading/framework/types.py
./fincept-qt/scripts/agno_trading/tools/__init__.py
./fincept-qt/scripts/agno_trading/tools/kraken_api.py
./fincept-qt/scripts/agno_trading/tools/market_data.py
./fincept-qt/scripts/agno_trading/tools/news_sentiment.py
./fincept-qt/scripts/agno_trading/tools/portfolio_tools.py
./fincept-qt/scripts/agno_trading/tools/technical_indicators.py
./fincept-qt/scripts/agno_trading/utils/__init__.py
./fincept-qt/scripts/agno_trading/utils/confidence_scorer.py
./fincept-qt/scripts/agno_trading/utils/tp_sl_calculator.py
./fincept-qt/scripts/ai_quant_lab/qlib_advanced_backtest.py
./fincept-qt/scripts/ai_quant_lab/qlib_advanced_models.py
./fincept-qt/scripts/ai_quant_lab/qlib_data_processors.py
./fincept-qt/scripts/ai_quant_lab/qlib_evaluation.py
./fincept-qt/scripts/ai_quant_lab/qlib_feature_engineering.py
./fincept-qt/scripts/ai_quant_lab/qlib_high_frequency.py
./fincept-qt/scripts/ai_quant_lab/qlib_meta_learning.py
./fincept-qt/scripts/ai_quant_lab/qlib_online_learning.py
./fincept-qt/scripts/ai_quant_lab/qlib_portfolio_opt.py
./fincept-qt/scripts/ai_quant_lab/qlib_reporting_legacy.py
./fincept-qt/scripts/ai_quant_lab/qlib_reporting.py
./fincept-qt/scripts/ai_quant_lab/qlib_rl.py
./fincept-qt/scripts/ai_quant_lab/qlib_rolling_retraining.py
./fincept-qt/scripts/ai_quant_lab/qlib_service.py
./fincept-qt/scripts/ai_quant_lab/qlib_strategy.py
./fincept-qt/scripts/ai_quant_lab/README.md
./fincept-qt/scripts/aisstream_data.py
./fincept-qt/scripts/akshare_alternative.py
./fincept-qt/scripts/akshare_analysis.py
./fincept-qt/scripts/akshare_bonds.py
./fincept-qt/scripts/akshare_company_info.py
./fincept-qt/scripts/akshare_crypto.py
./fincept-qt/scripts/akshare_currency.py
./fincept-qt/scripts/akshare_data.py
./fincept-qt/scripts/akshare_derivatives.py
./fincept-qt/scripts/akshare_economics_china.py
./fincept-qt/scripts/akshare_economics_global.py
./fincept-qt/scripts/akshare_energy.py
./fincept-qt/scripts/akshare_funds_expanded.py
./fincept-qt/scripts/akshare_futures.py
./fincept-qt/scripts/akshare_index.py
./fincept-qt/scripts/akshare_macro.py
./fincept-qt/scripts/akshare_misc.py
./fincept-qt/scripts/akshare_news.py
./fincept-qt/scripts/akshare_reits.py
./fincept-qt/scripts/akshare_stocks_board.py
./fincept-qt/scripts/akshare_stocks_financial.py
./fincept-qt/scripts/akshare_stocks_funds.py
./fincept-qt/scripts/akshare_stocks_historical.py
./fincept-qt/scripts/akshare_stocks_holders.py
./fincept-qt/scripts/akshare_stocks_hot.py
./fincept-qt/scripts/akshare_stocks_margin.py
./fincept-qt/scripts/akshare_stocks_realtime.py
./fincept-qt/scripts/algo_trading/__init__.py
./fincept-qt/scripts/algo_trading/algo_live_runner.py
./fincept-qt/scripts/algo_trading/algo_manager.py
./fincept-qt/scripts/algo_trading/backtest_engine.py
./fincept-qt/scripts/algo_trading/condition_evaluator.py
./fincept-qt/scripts/algo_trading/indicators.py
./fincept-qt/scripts/algo_trading/python_backtest_engine.py
./fincept-qt/scripts/algo_trading/scanner_engine.py
./fincept-qt/scripts/alpha_arena/__init__.py
./fincept-qt/scripts/alpha_arena/config/__init__.py
./fincept-qt/scripts/alpha_arena/config/agent_cards.py
./fincept-qt/scripts/alpha_arena/config/trading_styles.py
./fincept-qt/scripts/alpha_arena/core/__init__.py
./fincept-qt/scripts/alpha_arena/core/agent_manager.py
./fincept-qt/scripts/alpha_arena/core/base_agent.py
./fincept-qt/scripts/alpha_arena/core/broker_adapter.py
./fincept-qt/scripts/alpha_arena/core/competition.py
./fincept-qt/scripts/alpha_arena/core/database.py
./fincept-qt/scripts/alpha_arena/core/evaluation.py
./fincept-qt/scripts/alpha_arena/core/features_pipeline.py
./fincept-qt/scripts/alpha_arena/core/grid_agent.py
./fincept-qt/scripts/alpha_arena/core/guardrails.py
./fincept-qt/scripts/alpha_arena/core/hitl.py
./fincept-qt/scripts/alpha_arena/core/market_data.py
./fincept-qt/scripts/alpha_arena/core/memory_adapter.py
./fincept-qt/scripts/alpha_arena/core/paper_trading_bridge.py
./fincept-qt/scripts/alpha_arena/core/paper_trading.py
./fincept-qt/scripts/alpha_arena/core/portfolio_metrics.py
./fincept-qt/scripts/alpha_arena/core/research_agent.py
./fincept-qt/scripts/alpha_arena/core/sentiment_agent.py
./fincept-qt/scripts/alpha_arena/main.py
./fincept-qt/scripts/alpha_arena/types/__init__.py
./fincept-qt/scripts/alpha_arena/types/models.py
./fincept-qt/scripts/alpha_arena/types/responses.py
./fincept-qt/scripts/alpha_arena/utils/__init__.py
./fincept-qt/scripts/alpha_arena/utils/logging.py
./fincept-qt/scripts/alpha_arena/utils/uuid.py
./fincept-qt/scripts/alpha_spread_data.py
./fincept-qt/scripts/alpha_vantage_extra_data.py
./fincept-qt/scripts/alphavantage_data.py
./fincept-qt/scripts/alternative_me_data.py
./fincept-qt/scripts/Analytics/alternateInvestment/asset_location.py
./fincept-qt/scripts/Analytics/alternateInvestment/base_analytics.py
./fincept-qt/scripts/Analytics/alternateInvestment/cli.py
./fincept-qt/scripts/Analytics/alternateInvestment/config.py
./fincept-qt/scripts/Analytics/alternateInvestment/convertible_bonds.py
./fincept-qt/scripts/Analytics/alternateInvestment/covered_calls.py
./fincept-qt/scripts/Analytics/alternateInvestment/data_handler.py
./fincept-qt/scripts/Analytics/alternateInvestment/digital_assets.py
./fincept-qt/scripts/Analytics/alternateInvestment/emerging_market_bonds.py
./fincept-qt/scripts/Analytics/alternateInvestment/equity_indexed_annuities.py
./fincept-qt/scripts/Analytics/alternateInvestment/fixed_annuities.py
./fincept-qt/scripts/Analytics/alternateInvestment/hedge_funds.py
./fincept-qt/scripts/Analytics/alternateInvestment/high_yield_bonds.py
./fincept-qt/scripts/Analytics/alternateInvestment/inflation_protected.py
./fincept-qt/scripts/Analytics/alternateInvestment/leveraged_funds.py
./fincept-qt/scripts/Analytics/alternateInvestment/managed_futures.py
./fincept-qt/scripts/Analytics/alternateInvestment/market_config.py
./fincept-qt/scripts/Analytics/alternateInvestment/market_neutral.py
./fincept-qt/scripts/Analytics/alternateInvestment/natural_resources.py
./fincept-qt/scripts/Analytics/alternateInvestment/performance_metrics.py
./fincept-qt/scripts/Analytics/alternateInvestment/precious_metals.py
./fincept-qt/scripts/Analytics/alternateInvestment/preferred_stocks.py
./fincept-qt/scripts/Analytics/alternateInvestment/private_capital.py
./fincept-qt/scripts/Analytics/alternateInvestment/real_estate.py
./fincept-qt/scripts/Analytics/alternateInvestment/risk_analyzer.py
./fincept-qt/scripts/Analytics/alternateInvestment/sri_funds.py
./fincept-qt/scripts/Analytics/alternateInvestment/stable_value.py
./fincept-qt/scripts/Analytics/alternateInvestment/structured_products.py
./fincept-qt/scripts/Analytics/alternateInvestment/variable_annuities.py
./fincept-qt/scripts/Analytics/corporateFinance/__init__.py
./fincept-qt/scripts/Analytics/corporateFinance/config.py
./fincept-qt/scripts/Analytics/derivatives/analytics.py
./fincept-qt/scripts/Analytics/derivatives/arbitrage.py
./fincept-qt/scripts/Analytics/derivatives/core.py
./fincept-qt/scripts/Analytics/derivatives/forward_commitments.py
./fincept-qt/scripts/Analytics/derivatives/market_data.py
```

## 5. 文件类型统计

```text
.py: 1434
.h: 694
.cpp: 660
.md: 78
.json: 30
.txt: 20
[no_ext]: 15
.yml: 12
.png: 6
.sh: 3
.ico: 2
.cmake: 2
.html: 2
.svg: 1
.pid: 1
.in: 1
.lock: 1
.ps1: 1
.sql: 1
.js: 1
.xml: 1
.desktop: 1
.qs: 1
```

## 6. 关键项目文件预览

### README.md

```text
# Fincept Terminal

<div align="center">

[![License: AGPL-3.0](https://img.shields.io/badge/license-AGPL--3.0-C06524)](https://github.com/Fincept-Corporation/FinceptTerminal/blob/main/LICENSE)
[![C++20](https://img.shields.io/badge/C%2B%2B-20-00599C?logo=cplusplus)](https://isocpp.org/)
[![Qt6](https://img.shields.io/badge/Qt-6-41CD52?logo=qt&logoColor=white)](https://www.qt.io/)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Hits](https://hits.sh/github.com/Fincept-Corporation/FinceptTerminal.svg?label=Visits)](https://hits.sh/github.com/Fincept-Corporation/FinceptTerminal/)

<a href="https://trendshift.io/repositories/17028" target="_blank"><img src="https://trendshift.io/api/badge/repositories/17028" alt="Fincept-Corporation%2FFinceptTerminal | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

[![GitHub Stars](https://img.shields.io/github/stars/Fincept-Corporation/FinceptTerminal?style=social)](https://github.com/Fincept-Corporation/FinceptTerminal/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/Fincept-Corporation/FinceptTerminal?style=social)](https://github.com/Fincept-Corporation/FinceptTerminal/network/members)
[![GitHub Watchers](https://img.shields.io/github/watchers/Fincept-Corporation/FinceptTerminal?style=social)](https://github.com/Fincept-Corporation/FinceptTerminal/watchers)
[![GitHub Release](https://img.shields.io/github/v/release/Fincept-Corporation/FinceptTerminal?color=brightgreen&logo=github)](https://github.com/Fincept-Corporation/FinceptTerminal/releases)
[![GitHub Issues](https://img.shields.io/github/issues/Fincept-Corporation/FinceptTerminal)](https://github.com/Fincept-Corporation/FinceptTerminal/issues)

[![X](https://img.shields.io/badge/-X-000000?style=flat-square&logo=x&logoColor=white)](https://x.com/finceptcorp) [![Twitter](https://img.shields.io/badge/-Twitter-1DA1F2?style=flat-square&logo=twitter&logoColor=white)](https://twitter.com/intent/tweet?text=Check%20out%20FinceptTerminal&url=https%3A//github.com/Fincept-Corporation/FinceptTerminal/) [![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Fincept-Corporation/FinceptTerminal/) [![Facebook](https://img.shields.io/badge/-Facebook-1877F2?style=flat-square&logo=facebook&logoColor=white)](https://www.facebook.com/sharer/sharer.php?u=https%3A//github.com/Fincept-Corporation/FinceptTerminal/) [![Reddit](https://img.shields.io/badge/-Reddit-FF4500?style=flat-square&logo=reddit&logoColor=white)](https://www.reddit.com/r/finceptTerminal/) [![WhatsApp](https://img.shields.io/badge/-WhatsApp-25D366?style=flat-square&logo=whatsapp&logoColor=white)](https://api.whatsapp.com/send?text=Check%20out%20FinceptTerminal%3A%20https%3A//github.com/Fincept-Corporation/FinceptTerminal/)

### **Your Thinking is the Only Limit. The Data Isn't.**

State-of-the-art financial intelligence platform with institutional-grade financial analytics, AI automation, and unlimited data connectivity.

[📥 Download](https://github.com/Fincept-Corporation/FinceptTerminal/releases) · [⚖️ License](https://github.com/Fincept-Corporation/FinceptTerminal/blob/main/docs/COMMERCIAL_LICENSE.md) · [💬 Discussions](https://github.com/Fincept-Corporation/FinceptTerminal/discussions) · [💬 Discord](https://discord.gg/ae87a8ygbN) · [🤝 Partner](https://github.com/Fincept-Corporation/FinceptTerminal/blob/main/docs/COMMERCIAL_LICENSE.md)

![Fincept Terminal](https://raw.githubusercontent.com/Fincept-Corporation/FinceptTerminal/main/images/FinceptBanner.png)

<table>
  <tr>
    <td align="center" width="25%"><a href="https://raw.githubusercontent.com/Fincept-Corporation/FinceptTerminal/main/images/EquityResearch.png"><img src="https://raw.githubusercontent.com/Fincept-Corporation/FinceptTerminal/main/images/EquityResearch.png" width="100%"/></a><br/><sub><b>Equity Research</b></sub></td>
    <td align="center" width="25%"><a href="https://raw.githubusercontent.com/Fincept-Corporation/FinceptTerminal/main/images/Portfolio.png"><img src="https://raw.githubusercontent.com/Fincept-Corporation/FinceptTerminal/main/images/Portfolio.png" width="100%"/></a><br/><sub><b>Portfolio</b></sub></td>
    <td align="center" width="25%"><a href="https://raw.githubusercontent.com/Fincept-Corporation/FinceptTerminal/main/images/News.png"><img src="https://raw.githubusercontent.com/Fincept-Corporation/FinceptTerminal/main/images/News.png" width="100%"/></a><br/><sub><b>News</b></sub></td>
    <td align="center" width="25%"><a href="https://raw.githubusercontent.com/Fincept-Corporation/FinceptTerminal/main/images/NodeEditor.png"><img src="https://raw.githubusercontent.com/Fincept-Corporation/FinceptTerminal/main/images/NodeEditor.png" width="100%"/></a><br/><sub><b>Node Editor</b></sub></td>
  </tr>
</table>

</div>

---

## About

**Fincept Terminal v4** is a pure native C++20 desktop application. It uses **Qt6** for UI and rendering, embedded **Python** for analytics, and delivers Bloomberg-terminal-class performance in a single native binary.

---

## Features

| **Feature** | **Description** |
|-------------|-----------------|
| 📊 **Multi-Asset Analytics** | DCF models, portfolio optimization, risk metrics (VaR, Sharpe), derivatives pricing across equity, fixed income, derivatives, portfolio, and alternatives via embedded Python |
| 🤖 **AI Agents** | 37 agents across Trader/Investor (Buffett, Graham, Lynch, Munger, Klarman, Marks…), Economic, and Geopolitics frameworks; local LLM support; multi-provider (OpenAI, Anthropic, Gemini, Groq, DeepSeek, MiniMax, OpenRouter, Ollama) |
| 🌐 **100+ Data Connectors** | DBnomics, Polygon, Kraken, Yahoo Finance, FRED, IMF, World Bank, AkShare, government APIs, plus optional alternative-data overlays such as Adanos market sentiment for equity research |
| 📈 **Real-Time Trading** | Crypto (Kraken/HyperLiquid WebSocket), equity, algo trading, paper trading engine, 16 broker integrations (Zerodha, Angel One, Upstox, Fyers, Dhan, Groww, Kotak, IIFL, 5paisa, AliceBlue, Shoonya, Motilal, IBKR, Alpaca, Tradier, Saxo) |
| 🔬 **QuantLib Suite** | 18 quantitative analysis modules — pricing, risk, stochastic, volatility, fixed income |
| 🚢 **Global Intelligence** | Maritime tracking, geopolitical analysis, relationship mapping, satellite data |
| 🎨 **Visual Workflows** | Node editor for automation pipelines, MCP tool integration |
| 🧠 **AI Quant Lab** | ML models, factor discovery, HFT, reinforcement learning trading |

---

## Installation

<!-- DOWNLOAD-TABLE-START -->
### Option 1 — Download Installer (Recommended)

Latest release: **v4.0.2** — [View all releases](https://github.com/Fincept-Corporation/FinceptTerminal/releases/tag/v4.0.2)

| Platform | Download | Run |
|----------|----------|-----|
| **Windows x64** | [FinceptTerminal-Windows-x64-setup.exe](https://github.com/Fincept-Corporation/FinceptTerminal/releases/download/v4.0.2/FinceptTerminal-4.0.2-windows-x64-setup.exe) | Run installer → launch `FinceptTerminal.exe` |
| **Linux x64** | [FinceptTerminal-Linux-x64.run](https://github.com/Fincept-Corporation/FinceptTerminal/releases/download/v4.0.2/FinceptTerminal-4.0.2-linux-x64-setup.run) | `chmod +x` → run installer |
| **macOS Apple Silicon** | [FinceptTerminal-macOS-arm64.dmg](https://github.com/Fincept-Corporation/FinceptTerminal/releases/download/v4.0.2/FinceptTerminal-4.0.2-macos-arm64-setup.dmg) | Open DMG → drag to Applications |
<!-- DOWNLOAD-TABLE-END -->

---

### Option 2 — Quick Start (One-Click Build)

Clone and run the setup script — it installs all dependencies and builds the app automatically:

```bash
# Linux / macOS
git clone https://github.com/Fincept-Corporation/FinceptTerminal.git
cd FinceptTerminal
chmod +x setup.sh && ./setup.sh
```

The script handles: compiler check, CMake, Qt6, Python, build, and launch.

> **Windows:** No setup script — use the manual build steps in Option 4 below. It's just two commands.

---

### Option 3 — Docker (CI / Developer Environments)

> **Note:** Docker is intended for CI/CD testing and development environments only.
> For the best experience, use the pre-built installers in **Option 1** above.
> Docker requires Linux with X11. Windows and macOS are not supported.

```bash
# Build from source (Linux + X11 required)
git clone https://github.com/Fincept-Corporation/FinceptTerminal.git
cd FinceptTerminal
docker build -t fincept-terminal .
docker run --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix fincept-terminal
```

---

### Option 4 — Build from Source (Manual)

> **Versions are pinned.** Use the exact versions below. Newer or older versions are unsupported and may fail to build or produce unstable binaries.

#### Prerequisites (exact versions)

| Tool | Pinned Version | Notes |
|------|----------------|-------|
| **Git** | latest | — |
| **CMake** | **3.27.7** | [Download](https://cmake.org/download/) |
| **Ninja** | **1.11.1** | [Download](https://github.com/ninja-build/ninja/releases) |
| **C++ compiler** | **MSVC 19.38** (VS 2022 17.8) / **GCC 12.3** / **Apple Clang 15.0** (Xcode 15.2) | C++20 required |
| **Qt** | **6.8.3** | [Qt Online Installer](https://www.qt.io/download-qt-installer) |
| **Python** | **3.11.9** | [python.org](https://www.python.org/downloads/release/python-3119/) |
| **Platform SDK** | Win10 SDK 10.0.22621.0 / macOS SDK 14.0 (deploy 11.0+) / glibc 2.31+ | — |

#### Install Qt 6.8.3

**Windows:** Qt Online Installer → select `Qt 6.8.3 > MSVC 2022 64-bit` (install path: `C:/Qt/6.8.3/msvc2022_64`)

**Linux:** Qt Online Installer → `Qt 6.8.3 > Desktop gcc 64-bit` (install path: `~/Qt/6.8.3/gcc_64`). **Or** for system packages, install `qt6-base-dev qt6-charts-dev qt6-tools-dev qt6-base-private-dev libqt6websockets6-dev libgl1-mesa-dev` — note system packages may be a different 6.x minor.

**macOS:** Qt Online Installer → `Qt 6.8.3 > macOS` (install path: `~/Qt/6.8.3/macos`)

#### Build (using CMake presets — recommended)

```bash
git clone https://github.com/Fincept-Corporation/FinceptTerminal.git
cd FinceptTerminal/fincept-qt
```

**Step 1 — Configure** (one-time, or after `CMakeLists.txt` changes):
```powershell
cmake --preset win-release      # Windows (PowerShell)
cmake --preset linux-release    # Linux
cmake --preset macos-release    # macOS
```

**Step 2 — Compile** (run this for every code change):
```powershell
cmake --build --preset win-release      # Windows
cmake --build --preset linux-release    # Linux
cmake --build --preset macos-release    # macOS
```

Debug variants: replace `release` with `debug` (e.g. `win-debug`, `linux-debug`, `macos-debug`).

> **Windows prerequisite:** The PowerShell profile at `~/Documents/PowerShell/Microsoft.PowerShell_profile.ps1`
> auto-initializes VS 2022 on every new terminal — open a fresh PowerShell and cmake works directly.

#### Build (manual — if presets can't resolve your Qt path)

```powershell
# Windows (PowerShell)
cmake -B build/win-release -G Ninja -DCMAKE_BUILD_TYPE=Release `
  -DCMAKE_PREFIX_PATH="C:/Qt/6.8.3/msvc2022_64"
cmake --build build/win-release
```

```bash
# Linux
cmake -B build/linux-release -G Ninja -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_PREFIX_PATH="$HOME/Qt/6.8.3/gcc_64"
cmake --build build/linux-release

# macOS
cmake -B build/macos-release -G Ninja -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_OSX_DEPLOYMENT_TARGET=11.0 \
  -DCMAKE_PREFIX_PATH="$HOME/Qt/6.8.3/macos"
cmake --build build/macos-release
```

#### Run

```bash
./build/<preset>/FinceptTerminal         # Linux / macOS (preset build)
.\build\<preset>\FinceptTerminal.exe     # Windows (preset build)
```

#### Troubleshooting

1. **"Could not find Qt6 6.8.3"** — verify `CMAKE_PREFIX_PATH` points to the Qt 6.8.3 install, not 6.5/6.6/6.8.
2. **MSVC version error** — use VS 2022 17.8+ (MSVC 19.38+). Check with `cl /?`.
3. **Need to unblock with a different Qt minor?** Pass `-DFINCEPT_ALLOW_QT_DRIFT=ON` (local testing only — never for releases or CI).
4. Clean rebuild: delete `build/<preset>/` and re-run configure.

---

## What Sets Us Apart

**Fincept Terminal** is an open-source financial platform built for those who refuse to be limited by traditional software. We compete on **analytics depth** and **data accessibility** — not on insider info or exclusive feeds.

Recent builds also support optional **Adanos Market Sentiment** connectivity in **Data Sources → Alternative Data**. When configured, Equity Research can surface cross-source retail sentiment snapshots across Reddit, X, finance news, and Polymarket. Without an active Adanos connection, the feature remains dormant and the rest of the app behaves exactly as before.

- **Native performance** — C++20 with Qt6, no Electron/web overhead
- **Single binary** — no Node.js, no browser runtime, no JavaScript bundler
- **Full buy-side analyst toolkit** — equity, portfolio, derivatives, fixed income, corporate finance, alternatives
- **100+ data connectors** — from Yahoo Finance to government databases
- **Free & Open Source** (AGPL-3.0) with commercial licenses available

---

## Roadmap

| Timeline | Milestone |
|----------|-----------|
| **Shipped** | Real-time streaming, 16 broker integrations, multi-account trading, PIN authentication, theme system |
| **Q2 2026** | Options strategy builder, multi-portfolio management, 50+ AI agents |
| **Q3 2026** | Programmatic API, ML training UI, institutional features |
| **Future** | Mobile companion, cloud sync, community marketplace |

---

## Contributing

We're building the future of financial analysis — together.

**Contribute:** New data connectors, AI agents, analytics modules, C++ screens, documentation

- [Contributing Guide](docs/CONTRIBUTING.md)
- [C++ Contributing Guide](fincept-qt/CONTRIBUTING.md)
- [Python Contributor Guide](docs/PYTHON_CONTRIBUTOR_GUIDE.md)
- [Report Bug](https://github.com/Fincept-Corporation/FinceptTerminal/issues)
- [Request Feature](https://github.com/Fincept-Corporation/FinceptTerminal/discussions)

---

## Support the Project

```

### LICENSE

```text
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007

Copyright (C) 2025-2026 Fincept Corporation

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.

================================================================================
                          DUAL LICENSING NOTICE
================================================================================

Fincept Terminal is dual-licensed. Every user must comply with ONE of the
following licenses:

1. AGPL-3.0 (Open Source)
   - Free for personal use, individual learning, academic research by
     individual students, and open-source contribution to this repository.
   - Requires sharing modifications if distributed or made available as a
     network service.
   - Full text: https://www.gnu.org/licenses/agpl-3.0.html

2. Fincept Commercial License
   - REQUIRED for any business or internal company use, regardless of
     revenue, size, or duration.
   - Required for SaaS, cloud, hosted, white-label, or resale offerings.
   - Required for forks that remove or replace Fincept's APIs, data
     sources, or service endpoints, where used commercially or internally.
   - See: docs/COMMERCIAL_LICENSE.md

The AGPL-3.0 option is NOT available for Commercial Use as defined in
docs/COMMERCIAL_LICENSE.md, Section 3. Commercial Use without an executed
Commercial License is a breach of copyright and is subject to the full
range of remedies set forth in docs/COMMERCIAL_LICENSE.md.

================================================================================
              CLONING / FORKING / MODIFICATION DOES NOT GRANT
                     COMMERCIAL OR INTERNAL-USE RIGHTS
================================================================================

Cloning, forking, downloading, building, or modifying this repository does
NOT grant any right to use Fincept Terminal — or any Modified Version or
Derivative Work — for Commercial Use. Internal use within any for-profit
organization, government body, fund, or revenue-generating non-profit is
Commercial Use and requires a paid Commercial License.

The license attaches to the codebase and any Derivative Work of it, not to
specific API integrations. Removing, replacing, disabling, or rewiring
Fincept's APIs, data sources, or service endpoints does NOT sever or
extinguish the licensing obligation.

================================================================================
                       FINCEPT DATA & API SERVICES
================================================================================

The Fincept Terminal software is offered under AGPL-3.0 for non-commercial
use as described above.

Fincept Data Sources and APIs are separate services subject to:
- Commercial License: USD 10,200 / year
- University & Academic License: USD 799 / month (20 accounts)
- Free for individual personal and educational use only

================================================================================
                            TRADEMARK NOTICE
================================================================================

"Fincept", "Fincept Terminal", "Fincept Corporation", and the Fincept logo
are trademarks of Fincept Corporation. All rights reserved.

You may not use these marks — or any colorable imitation, transliteration,
abbreviation, translation, or variation or derivative thereof — without
prior written permission from Fincept Corporation, except as strictly
necessary to comply with AGPL-3.0 attribution requirements.

Removal, replacement, or rebranding of these marks in any fork or
Derivative Work does NOT extinguish Fincept Corporation's rights in the
underlying Software, nor does it sever the licensing obligations attaching
to the codebase.

The Fincept Trade Dress — including screen layouts, color palette,
terminal command syntax, ticker conventions, function-code conventions,
keyboard shortcut conventions, dashboard widget vocabulary, and overall
visual identity of Fincept Terminal — is also protected. Substantially
similar replication, even with branding removed, is prohibited.

Use of the trademarks or trade dress to promote derivative works or
competing products is strictly prohibited.

================================================================================
                         ADDITIONAL RESTRICTIONS
================================================================================

While AGPL-3.0 grants broad freedoms for non-commercial use, the following
additional restrictions apply to all users of this Software:

1. NETWORK USE REQUIREMENT (AGPL § 13)
   If you run a modified version as a network service (SaaS, cloud
   platform, web application), you MUST:
   - Provide users with access to the complete source code
   - Clearly indicate the source is available
   - Make the source available via download or repository access

2. ATTRIBUTION REQUIREMENT
   You must retain all copyright notices, attribution statements, and
   this license file in any distribution or Derivative Work.

3. TRADEMARK RESTRICTIONS
   - Cannot use "Fincept" or related marks without permission
   - Cannot imply endorsement by Fincept Corporation
   - Must clearly differentiate Derivative Works from the official version
   - Cannot replicate Fincept Trade Dress

4. COMMERCIAL & INTERNAL-USE RESTRICTION
   - Commercial Use of any kind requires a Commercial License
   - Internal corporate use is Commercial Use, regardless of whether the
     Software is exposed to third parties
   - Forks that strip or replace Fincept APIs are still subject to the
     Commercial License requirement

================================================================================
                     CONTRIBUTOR LICENSE AGREEMENT (CLA)
================================================================================

By contributing to Fincept Terminal (via pull request, patch, comment,
issue, or any other means), each contributor agrees to the following terms:

1. ASSIGNMENT AND LICENSE-IN. To the maximum extent permitted by law, each
   contribution is a work made for hire owned by Fincept Corporation. To
   the extent any contribution is not a work made for hire, the contributor
   hereby presently and unconditionally ASSIGNS to Fincept Corporation all
   right, title, and interest in and to the contribution, including all
   copyright, moral rights (waived to the maximum extent permitted), and
   related rights. Without limiting the foregoing, the contributor grants
   Fincept Corporation a perpetual, worldwide, non-exclusive, royalty-free,
   irrevocable, sublicensable license — with the right to sublicense
   through multiple tiers — to use, reproduce, modify, distribute,
   sublicense, and relicense the contribution under AGPL-3.0, the Fincept
   Commercial License, and any future license selected by Fincept
   Corporation.

2. NO JOINT AUTHORSHIP. Each contributor expressly disclaims any claim of
   joint authorship in the Software as a whole or in any other
   contributor's contributions. Contributing does NOT grant the contributor
   any license to the Software as a whole, to any other contributor's
   contributions, or to Commercial Use of the Software.

3. WARRANTY AND INDEMNITY. Each contributor warrants that (a) the
   contribution is the contributor's original work or is properly attributed
   and licensed for the contribution; (b) the contributor has the legal
   right to make the contribution and grant the rights herein; (c) the
   contribution is free of any obligations to any current or former
   employer, client, university, or third party that would conflict with
   this assignment; and (d) the contribution does not infringe any
   third-party rights. The contributor shall indemnify, defend, and hold
   harmless Fincept Corporation from any breach of these warranties.

4. AS-IS. Contributions are provided "AS IS" without warranties of any
   kind beyond the warranties in Section 3 above.

5. NO COMMERCIAL RIGHTS BACK. Contributing does NOT grant the contributor
   Commercial Use rights, license-back rights, or access to Fincept Data
   Sources or APIs for commercial purposes.

================================================================================
                       WHEN A COMMERCIAL LICENSE IS REQUIRED
================================================================================

You NEED a Commercial License if you:
- Use Fincept Terminal for any business purpose, paid or free
- Use Fincept Terminal internally at a company, fund, or for-profit entity
  (regardless of whether it is exposed to third parties)
- Are a startup at any stage, including pre-revenue and pre-product
- Are a hedge fund, prop firm, bank, brokerage, asset manager, family
  office, fintech, or exchange
- Offer Fincept Terminal as SaaS, PaaS, or any hosted service
- White-label, rebrand, distribute, or resell Fincept Terminal
- Maintain or operate a fork that strips or replaces Fincept APIs and use
  it commercially or internally
- Engage a third-party developer, integrator, or consultancy to build,
  modify, deploy, host, or customize Fincept Terminal for any of the above

You do NOT need a Commercial License if you:
- Use Fincept Terminal for personal learning on your own machine
- Are an individual student conducting non-commercial research
- Are contributing to the open-source project

When in doubt, assume a Commercial License is required and email
support@fincept.in.

================================================================================
                      ENFORCEMENT, PENALTIES & LIABILITY
================================================================================

Fincept Corporation actively monitors public code repositories, container
registries, application stores, cloud marketplaces, SaaS platforms, and
trademark registers for unlicensed Commercial Use of Fincept Terminal,
Modified Versions, and Derivative Works.

Unauthorized Commercial Use is subject to liquidated damages, including
(without limitation):

  * USD 50,000 per organization per year for unauthorized internal
    corporate use (or 5x the then-current Commercial License fee,
    whichever is greater)
  * USD 250,000 per offering for unauthorized SaaS, hosting, or resale,
    plus full disgorgement of revenue
  * USD 100,000 per organization for unauthorized fork-and-replace-API
    deployments, plus 5x the Commercial License fee for each year of use
  * USD 150,000 per element for unauthorized use of Fincept Marks or
    Fincept Trade Dress
  * USD 10,000 per day for continued use after notice of breach

In addition, Fincept Corporation will pursue:
- Backdated license fees from the date of first unauthorized use, with
  18% annual interest
- Disgorgement of all profits, revenue, and cost savings derived from
  unauthorized use
- DMCA takedowns (17 U.S.C. § 512), notices under the Information
  Technology Act, 2000 (India), and equivalent foreign statutes
- Cease-and-desist letters and civil action for copyright and trademark
  infringement
- Criminal complaints under the Copyright Act, 1957 (India) §§ 63-63B
  and equivalent foreign laws
- All attorneys' fees, court costs, expert fees, and investigation costs

JOINT AND SEVERAL LIABILITY. Any organization that engages, hires, or
contracts with a third-party developer, integrator, IT consultancy,
outsourcing vendor, freelancer, or offshore development center to build,
modify, deploy, fork, host, or customize Fincept Terminal or any
```

### Dockerfile

```text
# syntax=docker/dockerfile:1.6
# ─────────────────────────────────────────────────────────────────────────────
# Fincept Terminal — multi-stage, multi-arch Docker build
#
# One Dockerfile, all hosts. Works for Docker Desktop on Windows/macOS (they
# run Linux containers) and native Linux hosts. Windows/macOS native installers
# (.exe / .dmg) are produced by .github/workflows/release.yml on platform
# runners — Docker cannot build those, by design.
#
# Architecture auto-detection
# ───────────────────────────
# BuildKit sets TARGETARCH automatically (`amd64` or `arm64`). The build picks
# the right Qt kit, Kitware CMake tarball, and apt architecture for us:
#
#   docker build -t fincept/terminal:4.0.2 .
#       → auto-detects host arch via BuildKit
#
#   docker buildx build --platform linux/amd64,linux/arm64 \
#       -t fincept/terminal:4.0.2 --push .
#       → cross-build both archs in one go
#
# Pins (must match fincept-qt/CMakeLists.txt + release.yml):
#   • Qt 6.8.3 EXACT                — aqtinstall (linux_gcc_64 / linux_gcc_arm64)
#   • GCC ≥ 12.3                    — Debian trixie g++-13
#   • CMake 3.27.7                  — Kitware prebuilt (x86_64 / aarch64)
#   • QT_MODULES = qtcharts qtwebsockets qtmultimedia
#
# Run (X11 on Linux host):
#   docker run --rm -it --net=host \
#     -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix \
#     fincept/terminal:4.0.2
# ─────────────────────────────────────────────────────────────────────────────

# ── Stage 1: Build ───────────────────────────────────────────────────────────
# `--platform=$BUILDPLATFORM` pins the builder stage to the native host arch —
# this avoids emulation overhead for toolchain work. Qt + CMake tarballs are
# picked for $TARGETARCH so the produced binary matches the requested target.
# When building for the native arch (no --platform override), BUILDPLATFORM
# and TARGETPLATFORM are equal and this is a plain native build.
FROM --platform=$BUILDPLATFORM debian:trixie-slim AS builder

# BuildKit-provided args. Valid values we care about: TARGETARCH ∈ {amd64, arm64}.
ARG TARGETARCH
ARG TARGETPLATFORM
ARG BUILDPLATFORM

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8

# Pins — overridable via `--build-arg` if you need to bump without editing.
ARG QT_VERSION=6.8.3
ARG CMAKE_VERSION=3.27.7

# Architecture-dependent values. Qt 6.8 introduced `linux_gcc_arm64` as the
# aqtinstall arch for Linux on ARM; the on-disk install path is still
# `gcc_arm64`. x86_64 maps to `linux_gcc_64` / `gcc_64` (the 6.8 rename).
#
# We resolve these once in a short shell block and persist them as /etc/build.env
# so later RUN steps can re-source them. Doing the resolution in-image (rather
# than as additional ARGs) keeps the `docker build` CLI simple.
RUN set -eux; \
    case "${TARGETARCH}" in \
      amd64) \
        QT_ARCH_AQT=linux_gcc_64; \
        QT_ARCH_PATH=gcc_64; \
        CMAKE_ASSET="cmake-${CMAKE_VERSION}-linux-x86_64.sh"; \
        ;; \
      arm64) \
        QT_ARCH_AQT=linux_gcc_arm64; \
        QT_ARCH_PATH=gcc_arm64; \
        CMAKE_ASSET="cmake-${CMAKE_VERSION}-linux-aarch64.sh"; \
        ;; \
      *) echo "Unsupported TARGETARCH: ${TARGETARCH}" >&2; exit 1 ;; \
    esac; \
    { \
      echo "QT_ARCH_AQT=${QT_ARCH_AQT}"; \
      echo "QT_ARCH_PATH=${QT_ARCH_PATH}"; \
      echo "CMAKE_ASSET=${CMAKE_ASSET}"; \
      echo "QT_VERSION=${QT_VERSION}"; \
      echo "CMAKE_VERSION=${CMAKE_VERSION}"; \
    } > /etc/build.env; \
    cat /etc/build.env

# Build toolchain + Qt build/link-time system deps. Mirrors the
# "Install system dependencies" step in release.yml (build-linux job).
# The -dev packages pull in their non-dev runtime counterparts; the extra
# `libglib2.0-0t64` / `libicu76` / `libdouble-conversion3` / `libpcre2-16-0`
# lines below are for Qt's own build-time tools (rcc, moc, uic) — they are
# binaries shipped inside the aqtinstall Qt kit and must be able to dlopen
# these at build time, not just link-time.
RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates curl wget git \
        ninja-build \
        g++-13 gcc-13 \
        python3 python3-pip python3-venv \
        pkg-config file \
        libssl-dev \
        libgl1-mesa-dev libglu1-mesa-dev \
        libxkbcommon-dev libxkbcommon-x11-dev \
        libxcb1-dev libxcb-cursor-dev libxcb-icccm4-dev libxcb-image0-dev \
        libxcb-keysyms1-dev libxcb-randr0-dev libxcb-render-util0-dev \
        libxcb-shape0-dev libxcb-sync-dev libxcb-xfixes0-dev \
        libxcb-xinerama0-dev libxcb-xkb-dev libxcb-util-dev \
        libfontconfig1-dev libfreetype6-dev libdbus-1-dev \
        libglib2.0-0t64 libicu-dev libdouble-conversion3 \
        libpcre2-16-0 libpcre2-8-0 zlib1g \
        # Qt Multimedia linkage — prebuilt libQt6Multimedia.so references
        # PulseAudio + GStreamer symbols that must resolve at link time.
        libpulse-dev \
        libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev \
        libasound2-dev \
    && update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-13 60 \
    && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-13 60 \
    && rm -rf /var/lib/apt/lists/*

# CMake pinned to 3.27.7 — Kitware ships prebuilt installers for both x86_64
# and aarch64. Debian's apt cmake drifts behind the project's EXACT pin.
RUN . /etc/build.env \
    && wget -q "https://github.com/Kitware/CMake/releases/download/v${CMAKE_VERSION}/${CMAKE_ASSET}" -O /tmp/cmake.sh \
    && chmod +x /tmp/cmake.sh \
    && /tmp/cmake.sh --skip-license --prefix=/usr/local \
    && rm /tmp/cmake.sh \
    && cmake --version

# Qt 6.8.3 via aqtinstall. Modules match QT_MODULES in release.yml. Retry
# loop rides through transient drops from the Qt mirror. --break-system-packages
# is required on trixie's PEP 668 pip.
ENV QT_ROOT=/opt/Qt
RUN . /etc/build.env \
    && pip3 install --break-system-packages --no-cache-dir aqtinstall \
    && for attempt in 1 2 3 4 5; do \
         python3 -m aqt install-qt linux desktop "${QT_VERSION}" "${QT_ARCH_AQT}" \
           --outputdir "${QT_ROOT}" \
           --modules qtcharts qtwebsockets qtmultimedia \
         && break \
         || { echo "aqtinstall attempt ${attempt} failed, retrying in 5s..."; sleep 5; }; \
       done

# ── Build Fincept Terminal ───────────────────────────────────────────────────
WORKDIR /src
COPY fincept-qt/ ./fincept-qt/

WORKDIR /src/fincept-qt
RUN . /etc/build.env \
    && export CMAKE_PREFIX_PATH="${QT_ROOT}/${QT_VERSION}/${QT_ARCH_PATH}" \
    && export PATH="${CMAKE_PREFIX_PATH}/bin:${PATH}" \
    && rm -rf build \
    && cmake -B build -G Ninja \
         -DCMAKE_BUILD_TYPE=Release \
         -DCMAKE_PREFIX_PATH="${CMAKE_PREFIX_PATH}" \
         -DOPENSSL_ROOT_DIR=/usr \
    && cmake --build build --parallel 4 \
    && strip build/FinceptTerminal

# ── Stage 2: Runtime ─────────────────────────────────────────────────────────
# Pinned to $TARGETPLATFORM so the final image actually matches the arch the
# user requested (even when buildx cross-builds from a different BUILDPLATFORM).
# Minimal runtime: we bundle Qt 6.8.3 from the builder stage so the image does
# not depend on Debian's (older) Qt packages. Qt pulls in EGL, GL, XCB, audio,
# Kerberos, and the glib-networking TLS backend — missing any of these causes
# HTTPS to silently fail or the app to crash on launch.
FROM --platform=$TARGETPLATFORM debian:trixie-slim AS runtime

ARG TARGETARCH
ARG QT_VERSION=6.8.3

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8

RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates \
        python3 python3-pip python3-venv \
        # GL / EGL — Qt platform plugins need EGL even with xcb
        libegl1 libgl1 libglx-mesa0 libglu1-mesa \
        # XCB platform plugin stack
        libxcb1 libxcb-cursor0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 \
        libxcb-randr0 libxcb-render-util0 libxcb-shape0 libxcb-sync1 \
        libxcb-xfixes0 libxcb-xinerama0 libxcb-xkb1 libxcb-util1 libxcb-glx0 \
        libxkbcommon0 libxkbcommon-x11-0 \
        # Core Qt runtime dependencies
        libglib2.0-0t64 libdbus-1-3 libfontconfig1 libfreetype6 \
        libx11-6 libx11-xcb1 \
        # TLS backend for QNetworkAccessManager (without it HTTPS silently fails)
        glib-networking \
        # Network auth — Kerberos
        libgssapi-krb5-2 \
        # Qt Multimedia audio backends (optional module, but linked when present)
        libpulse0 libasound2t64 libpipewire-0.3-0t64 \
        # Wayland client libs — WSLg / modern Linux desktops. Without
        # libwayland-cursor, Qt's wayland plugin fails to dlopen.
        libwayland-client0 libwayland-cursor0 libwayland-egl1 \
        libdecor-0-0 libxkbcommon0 \
        # Used by embedded Python analytics
        libopenblas0 \
    && rm -rf /var/lib/apt/lists/*

# Resolve the on-disk Qt arch path for this target. Same mapping as builder.
RUN set -eux; \
    case "${TARGETARCH}" in \
      amd64) echo "gcc_64"   > /etc/qt_arch ;; \
      arm64) echo "gcc_arm64" > /etc/qt_arch ;; \
      *) echo "Unsupported TARGETARCH: ${TARGETARCH}" >&2; exit 1 ;; \
    esac

ENV QT_ROOT=/opt/Qt

# Bundle Qt 6.8.3 libs + plugins from builder stage. The builder writes under
# /opt/Qt/${QT_VERSION}/${arch-dependent}/ — the whole /opt/Qt tree copies
# cleanly for either arch, since only one kit is installed per build.
COPY --from=builder /opt/Qt /opt/Qt

# LD_LIBRARY_PATH / QT_PLUGIN_PATH / QT_QPA_PLATFORM_PLUGIN_PATH are resolved
# at container start by the ENTRYPOINT wrapper so they pick up the correct
# per-arch subdirectory (gcc_64 vs gcc_arm64) without needing a shell.
ENV QT_QPA_PLATFORM=xcb

WORKDIR /app
COPY --from=builder /src/fincept-qt/build/FinceptTerminal ./FinceptTerminal
COPY --from=builder /src/fincept-qt/scripts              ./scripts
COPY --from=builder /src/fincept-qt/resources            ./resources

# QGeoView is a FetchContent dependency built as a shared library next to the
# binary on Linux. Copy it into /usr/local/lib so the map widget can dlopen it.
COPY --from=builder /src/fincept-qt/build/_deps/qgeoview-build/lib/ /usr/local/lib/
RUN ldconfig \
    && chmod +x ./FinceptTerminal

# Tiny wrapper resolves QT_PREFIX at runtime (cannot expand $(cat ...) in ENV).
RUN { \
      echo '#!/bin/sh'; \
      echo 'set -e'; \
      echo 'QT_ARCH="$(cat /etc/qt_arch)"'; \
      echo 'QT_PREFIX="${QT_ROOT}/'"${QT_VERSION}"'/${QT_ARCH}"'; \
      echo 'export LD_LIBRARY_PATH="${QT_PREFIX}/lib:/usr/local/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"'; \
      echo 'export QT_PLUGIN_PATH="${QT_PREFIX}/plugins"'; \
      echo 'export QT_QPA_PLATFORM_PLUGIN_PATH="${QT_PREFIX}/plugins/platforms"'; \
      echo 'exec /app/FinceptTerminal "$@"'; \
    } > /usr/local/bin/fincept-entrypoint.sh \
```

## 7. 许可证关键词扫描

```text
./setup.sh:31:echo "  Fincept Terminal v4.0.1 — Setup"
./setup.sh:163:    # Modules required to compile Fincept (match find_package COMPONENTS)
./setup.sh:198:BIN="$APP_DIR/build/$PRESET/FinceptTerminal"
./setup.sh:199:[ "$PLATFORM" = "macos" ] && BIN="$APP_DIR/build/$PRESET/FinceptTerminal.app/Contents/MacOS/FinceptTerminal"
./funding.json:7:    "name": "Fincept Corporation",
./funding.json:9:    "description": "Fincept Corporation develops the Fincept Terminal, a state-of-the-art open-source financial intelligence platform with institutional-grade financial analytics, AI automation, and unlimited data connectivity. We build professional-grade financial tools that compete on analytics depth and data accessibility.",
./funding.json:11:      "url": "https://github.com/Fincept-Corporation/FinceptTerminal"
./funding.json:17:      "name": "Fincept Terminal",
./funding.json:20:        "url": "https://github.com/Fincept-Corporation/FinceptTerminal"
./funding.json:23:        "url": "https://github.com/Fincept-Corporation/FinceptTerminal"
./funding.json:25:      "licenses": [
./funding.json:26:        "spdx:AGPL-3.0"
./funding.json:56:        "description": "Support the development of Fincept Terminal with a one-time contribution to fund feature development, infrastructure, and maintenance.",
./LICENSE:4:Copyright (C) 2025-2026 Fincept Corporation
./LICENSE:6:This program is free software: you can redistribute it and/or modify
./LICENSE:17:along with this program. If not, see <https://www.gnu.org/licenses/>.
./LICENSE:23:Fincept Terminal is dual-licensed. Every user must comply with ONE of the
./LICENSE:24:following licenses:
./LICENSE:26:1. AGPL-3.0 (Open Source)
./LICENSE:31:   - Full text: https://www.gnu.org/licenses/agpl-3.0.html
./LICENSE:33:2. Fincept Commercial License
./LICENSE:37:   - Required for forks that remove or replace Fincept's APIs, data
./LICENSE:38:     sources, or service endpoints, where used commercially or internally.
./LICENSE:41:The AGPL-3.0 option is NOT available for Commercial Use as defined in
./LICENSE:43:Commercial License is a breach of copyright and is subject to the full
./LICENSE:52:NOT grant any right to use Fincept Terminal — or any Modified Version or
./LICENSE:57:The license attaches to the codebase and any Derivative Work of it, not to
./LICENSE:59:Fincept's APIs, data sources, or service endpoints does NOT sever or
./LICENSE:66:The Fincept Terminal software is offered under AGPL-3.0 for non-commercial
./LICENSE:69:Fincept Data Sources and APIs are separate services subject to:
./LICENSE:78:"Fincept", "Fincept Terminal", "Fincept Corporation", and the Fincept logo
./LICENSE:79:are trademarks of Fincept Corporation. All rights reserved.
./LICENSE:83:prior written permission from Fincept Corporation, except as strictly
./LICENSE:84:necessary to comply with AGPL-3.0 attribution requirements.
./LICENSE:87:Derivative Work does NOT extinguish Fincept Corporation's rights in the
./LICENSE:91:The Fincept Trade Dress — including screen layouts, color palette,
./LICENSE:94:visual identity of Fincept Terminal — is also protected. Substantially
./LICENSE:104:While AGPL-3.0 grants broad freedoms for non-commercial use, the following
./LICENSE:107:1. NETWORK USE REQUIREMENT (AGPL § 13)
./LICENSE:110:   - Provide users with access to the complete source code
./LICENSE:115:   You must retain all copyright notices, attribution statements, and
./LICENSE:116:   this license file in any distribution or Derivative Work.
./LICENSE:119:   - Cannot use "Fincept" or related marks without permission
./LICENSE:120:   - Cannot imply endorsement by Fincept Corporation
./LICENSE:122:   - Cannot replicate Fincept Trade Dress
./LICENSE:128:   - Forks that strip or replace Fincept APIs are still subject to the
./LICENSE:135:By contributing to Fincept Terminal (via pull request, patch, comment,
./LICENSE:139:   contribution is a work made for hire owned by Fincept Corporation. To
./LICENSE:141:   hereby presently and unconditionally ASSIGNS to Fincept Corporation all
./LICENSE:143:   copyright, moral rights (waived to the maximum extent permitted), and
./LICENSE:145:   Fincept Corporation a perpetual, worldwide, non-exclusive, royalty-free,
./LICENSE:146:   irrevocable, sublicensable license — with the right to sublicense
./LICENSE:148:   sublicense, and relicense the contribution under AGPL-3.0, the Fincept
./LICENSE:149:   Commercial License, and any future license selected by Fincept
./LICENSE:155:   any license to the Software as a whole, to any other contributor's
./LICENSE:160:   and licensed for the contribution; (b) the contributor has the legal
./LICENSE:166:   harmless Fincept Corporation from any breach of these warranties.
./LICENSE:172:   Commercial Use rights, license-back rights, or access to Fincept Data
./LICENSE:173:   Sources or APIs for commercial purposes.
./LICENSE:180:- Use Fincept Terminal for any business purpose, paid or free
./LICENSE:181:- Use Fincept Terminal internally at a company, fund, or for-profit entity
./LICENSE:186:- Offer Fincept Terminal as SaaS, PaaS, or any hosted service
./LICENSE:187:- White-label, rebrand, distribute, or resell Fincept Terminal
./LICENSE:188:- Maintain or operate a fork that strips or replaces Fincept APIs and use
./LICENSE:189:  it commercially or internally
./LICENSE:191:  modify, deploy, host, or customize Fincept Terminal for any of the above
./LICENSE:194:- Use Fincept Terminal for personal learning on your own machine
./LICENSE:195:- Are an individual student conducting non-commercial research
./LICENSE:205:Fincept Corporation actively monitors public code repositories, container
./LICENSE:207:trademark registers for unlicensed Commercial Use of Fincept Terminal,
./LICENSE:220:  * USD 150,000 per element for unauthorized use of Fincept Marks or
./LICENSE:221:    Fincept Trade Dress
./LICENSE:224:In addition, Fincept Corporation will pursue:
./LICENSE:225:- Backdated license fees from the date of first unauthorized use, with
./LICENSE:231:- Cease-and-desist letters and civil action for copyright and trademark
./LICENSE:240:modify, deploy, fork, host, or customize Fincept Terminal or any
./LICENSE:242:party for any unauthorized Commercial Use, breach of license, or
./LICENSE:246:acquirers. The duty to verify license compliance is non-delegable.
./LICENSE:258:exclusive jurisdiction. Fincept Corporation reserves the right to seek
./LICENSE:269:Repository:    https://github.com/Fincept-Corporation/FinceptTerminal
./LICENSE:270:Documentation: https://github.com/Fincept-Corporation/FinceptTerminal/tree/main/docs
./LICENSE:279:                  subsequent version published by Fincept Corporation. The
./LICENSE:282:Software Version: 4.0.2 (current release; license applies to all releases,
./LICENSE:287:originally published. Any commercial or internal-corporate use of any
./LICENSE:288:version of Fincept Terminal — past, present, or future — is subject to
./Dockerfile:3:# Fincept Terminal — multi-stage, multi-arch Docker build
./Dockerfile:122:    && /tmp/cmake.sh --skip-license --prefix=/usr/local \
./Dockerfile:140:# ── Build Fincept Terminal ───────────────────────────────────────────────────
./Dockerfile:154:    && strip build/FinceptTerminal
./Dockerfile:220:COPY --from=builder /src/fincept-qt/build/FinceptTerminal ./FinceptTerminal
./Dockerfile:228:    && chmod +x ./FinceptTerminal
./Dockerfile:239:      echo 'exec /app/FinceptTerminal "$@"'; \
./updates.json:7:      "download-url": "https://github.com/Fincept-Corporation/FinceptTerminal/releases/download/v4.0.2/FinceptTerminal-4.0.2-windows-x64-setup.exe",
./updates.json:9:      "open-url": "https://github.com/Fincept-Corporation/FinceptTerminal/releases/tag/v4.0.2",
./updates.json:10:      "changelog": "Fincept Terminal v4.0.2 \u2014 see release notes at https://github.com/Fincept-Corporation/FinceptTerminal/releases/tag/v4.0.2"
./updates.json:14:      "download-url": "https://github.com/Fincept-Corporation/FinceptTerminal/releases/download/v4.0.2/FinceptTerminal-4.0.2-linux-x64-setup.run",
./updates.json:16:      "open-url": "https://github.com/Fincept-Corporation/FinceptTerminal/releases/tag/v4.0.2",
./updates.json:17:      "changelog": "Fincept Terminal v4.0.2 \u2014 see release notes at https://github.com/Fincept-Corporation/FinceptTerminal/releases/tag/v4.0.2"
./updates.json:21:      "download-url": "https://github.com/Fincept-Corporation/FinceptTerminal/releases/download/v4.0.2/FinceptTerminal-4.0.2-macos-arm64-setup.dmg",
./updates.json:23:      "open-url": "https://github.com/Fincept-Corporation/FinceptTerminal/releases/tag/v4.0.2",
./updates.json:24:      "changelog": "Fincept Terminal v4.0.2 \u2014 see release notes at https://github.com/Fincept-Corporation/FinceptTerminal/releases/tag/v4.0.2"
./docs/CRYPTO_WALLET_CONNECT.md:3:The **Crypto Center** is where Fincept Terminal reads your $FNCPT identity. It shows your public address, SOL balance, $FNCPT balance, and live USD value. **Your private keys never touch the terminal.**
./docs/CRYPTO_WALLET_CONNECT.md:33:2. In Fincept Terminal: **Navigate → Crypto → Crypto Center**.
./docs/CRYPTO_WALLET_CONNECT.md:37:6. Phantom shows a second prompt: a *signed message* request. Verify it begins with `Fincept Terminal wallet-connect challenge.` then click **Sign**.
./docs/CODE_OF_CONDUCT.md:5:We pledge to make participation in the Fincept Terminal community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity.
./docs/CODE_OF_CONDUCT.md:131:- **GitHub Issues:** https://github.com/Fincept-Corporation/FinceptTerminal/issues
./docs/CODE_OF_CONDUCT.md:132:- **GitHub Discussions:** https://github.com/Fincept-Corporation/FinceptTerminal/discussions
./docs/COMMERCIAL_LICENSE.md:1:# Fincept Terminal — Commercial License
./docs/COMMERCIAL_LICENSE.md:4:**In effect from:** April 30, 2026 (and continuing in force until superseded by a subsequent version published by Fincept Corporation)
./docs/COMMERCIAL_LICENSE.md:5:**Licensor:** Fincept Corporation (a company organized under the laws of India)
./docs/COMMERCIAL_LICENSE.md:12:> ⚠️ **Cloning, forking, downloading, building, or modifying this repository does NOT grant any right to use Fincept Terminal — or any Derivative Work of it — for Commercial Use.**
./docs/COMMERCIAL_LICENSE.md:13:> A separate, paid Commercial License executed with Fincept Corporation is required for any Commercial Use, including **internal use within any for-profit organization**, even where Fincept's data sources, APIs, or service endpoints have been removed, replaced, or rewired.
./docs/COMMERCIAL_LICENSE.md:15:This document is a plain-language summary **and** the operative commercial-licensing terms of Fincept Terminal. It supplements — and in case of conflict, governs over — the AGPL-3.0 license under which the Software is also made available for non-commercial purposes.
./docs/COMMERCIAL_LICENSE.md:21:Fincept Corporation is the sole copyright holder of the Software. As copyright holder, Fincept Corporation offers the Software under **two alternative, independent licenses**, and a user must select and comply with **one** of them:
./docs/COMMERCIAL_LICENSE.md:23:1. **GNU Affero General Public License v3.0 (AGPL-3.0)** — for personal use, individual learning, academic research by individual students, and open-source contribution. Full text: [`/LICENSE`](../LICENSE).
./docs/COMMERCIAL_LICENSE.md:24:2. **Fincept Commercial License** — for any Commercial Use, as defined in Section 3 below.
./docs/COMMERCIAL_LICENSE.md:26:**The Commercial License is not a modification of, addition to, or restriction upon the AGPL-3.0.** It is an alternative license offered by the copyright holder. A user who engages in Commercial Use is required to obtain rights under the Commercial License because the AGPL-3.0 grant offered by Fincept Corporation **never extended to Commercial Use** — Commercial Use was never within the scope of the AGPL-3.0 offer made by the copyright holder. Accordingly, the restrictions in this document do not constitute "further restrictions" within the meaning of AGPL-3.0 § 7; they define the scope of an *alternative* license offering.
./docs/COMMERCIAL_LICENSE.md:28:A user engaging in Commercial Use without an executed Commercial License is in breach of copyright and subject to all remedies set forth in Sections 12, 13, and 14.
./docs/COMMERCIAL_LICENSE.md:30:**Acceptance.** Each act of downloading, cloning, forking, building, executing, distributing, modifying, or otherwise using the Software constitutes affirmative acceptance of this License in its then-current published form. Continued use after publication of any new version of this License constitutes acceptance of the new version. A user who does not accept this License must immediately cease use and destroy all copies. The public availability of this License at the Fincept Terminal repository, in every release artifact, and embedded in the Software constitutes constructive notice to all users worldwide.
./docs/COMMERCIAL_LICENSE.md:38:- **"Software"** means the source code, object code, binaries, scripts (including all Python scripts in the `scripts/` tree), configuration, documentation, assets, build artifacts, container images, virtual-machine images, model weights and parameters trained or fine-tuned using the Software, datasets, embeddings, feature stores, and any output materially derived from the foregoing, contained in or produced by the Fincept Terminal repository at https://github.com/Fincept-Corporation/FinceptTerminal, in any branch, tag, release, fork, mirror, or commit, in whole or in part. Each script, module, file, broker integration, screen, MCP tool, agent framework, and Python wrapper is severable for purposes of demonstrating use, but **not severable for purposes of escaping this License**. Use of any one component constitutes use of the Software. No portion of the Software qualifies as a "System Library," "Standard Interface," or "Major Component" within the meaning of any open-source license definition.
./docs/COMMERCIAL_LICENSE.md:42:- **"Derivative Work"** means any software, work product, or system, in source or object form, that is based on, incorporates, links to (statically or dynamically), wraps, calls into, embeds, invokes via API, RPC, message queue, file drop, screen scrape, or any intermediation, or substantially reproduces the Software or any portion thereof. Derivative Work includes, without limitation, any version produced by: (i) compilation of the Software's source tree with or without modification; (ii) replacement, removal, disabling, or rewiring of any module, API, data integration, or service endpoint while retaining any other portion of the Software; (iii) translation, porting, or rewriting of any part of the Software into another programming language or runtime while preserving its architecture, screen layouts, workflow, sequence-structure-and-organization, MCP tool taxonomy, broker abstraction layer, agent framework hierarchy, terminal command syntax, function-code conventions, or feature set; (iv) translation of UI text, terminal commands, or function codes into another language or alphabet; (v) any work whose primary purpose, value, or functionality is materially derived from the Software; or (vi) any system that consumes, accesses, or operates upon the output, datasets, embeddings, model weights, or feature stores produced by the Software. The use of any portion of the Software comprising more than fifty (50) lines of source code, any single source file, any named function or class, any data schema, or any analytical algorithm or workflow expressed in the Software constitutes a Derivative Work; these thresholds are illustrative minima and not safe harbors. The number of intermediate hops, wrappers, gateways, proxies, or microservices between a user and the Software is irrelevant. Substantial similarity in non-literal elements is presumed to be a Derivative Work, with the burden on the alleged infringer to rebut by clear and convincing evidence.
./docs/COMMERCIAL_LICENSE.md:52:  (d) Any installation on or execution upon hardware, networks, virtual machines, containers, cloud accounts, or infrastructure owned, leased, controlled, paid for, or sponsored by any for-profit entity, governmental body, or organization, irrespective of whether the entity directed, knew of, or sanctioned the installation. The "personal use" exemption applies only to natural persons using personally owned and personally paid-for hardware for non-commercial purposes outside the course of employment;
./docs/COMMERCIAL_LICENSE.md:54:  (e) Use of any Modified Version, including any version in which Fincept-provided data sources, APIs, integrations, or service endpoints have been removed, replaced, rewired, or substituted with Licensee's or any third party's data sources, APIs, integrations, or service endpoints;
./docs/COMMERCIAL_LICENSE.md:60:  (h) Bundling, aggregation, integration, or co-installation of the Software with Licensee's products, regardless of any "mere aggregation" exemption recognized in any open-source license;
./docs/COMMERCIAL_LICENSE.md:68:- **"Fincept Marks"** means the names, logos, and trade dress "Fincept", "Fincept Terminal", "Fincept Corporation", and any colorable imitation, transliteration, abbreviation, translation, or variation or derivative thereof.
./docs/COMMERCIAL_LICENSE.md:70:- **"Fincept Trade Dress"** means the distinctive look and feel of Fincept Terminal, including screen layouts, color palette, terminal command syntax, ticker conventions, function-code conventions, keyboard shortcut conventions, dashboard widget vocabulary, and overall visual identity.
./docs/COMMERCIAL_LICENSE.md:72:- **"Licensor"** means Fincept Corporation. **"Licensee"** means the natural or legal person exercising rights under this License.
./docs/COMMERCIAL_LICENSE.md:81:- **Internal use within any company, fund, government body, or for-profit organization** — even if the Software is never exposed to third parties, even after Fincept APIs have been removed or replaced
./docs/COMMERCIAL_LICENSE.md:86:- Forks that strip out, replace, disable, or rewire Fincept APIs, data sources, or service endpoints, when used for Commercial Use
./docs/COMMERCIAL_LICENSE.md:89:- Any use that competes with, substitutes for, or substantially replicates the functionality of Fincept Terminal or any product or service offered by Licensor
./docs/COMMERCIAL_LICENSE.md:97:The AGPL-3.0 grant attached to the public repository permits a user, for non-commercial purposes only, to view, study, modify, and redistribute the Software under AGPL-3.0 terms. **It does not grant any of the following**, all of which require a separate Commercial License:
./docs/COMMERCIAL_LICENSE.md:101:3. The right to remove, replace, disable, or rewire Fincept's APIs, data integrations, or service endpoints and then use the resulting Modified Version or Derivative Work commercially or internally
./docs/COMMERCIAL_LICENSE.md:102:4. The right to use, reproduce, or imitate any of the Fincept Marks or Fincept Trade Dress in any forked, derivative, rebranded, or successor product
./docs/COMMERCIAL_LICENSE.md:103:5. The right to relicense, sublicense, sell, lease, or offer paid access to the Software or any Derivative Work
./docs/COMMERCIAL_LICENSE.md:104:6. Any rights in or to Fincept-operated data services, API endpoints, hosted infrastructure, or proprietary datasets
./docs/COMMERCIAL_LICENSE.md:106:The license attaches to the **codebase and any Derivative Work of it**, not to specific API integrations. **Substituting Fincept APIs with your own — or with any third party's — does not sever or extinguish the licensing obligation.**
./docs/COMMERCIAL_LICENSE.md:112:Licensee shall not use the Fincept Marks in connection with any product, service, repository, distribution, or marketing, except as expressly authorized in advance and in writing by Licensor. **Removal, replacement, or rebranding of the Fincept Marks in any fork or Derivative Work does not extinguish Licensor's rights in the underlying Software, nor does it sever the licensing obligations attaching to the codebase.**
./docs/COMMERCIAL_LICENSE.md:114:Licensee acknowledges that the value of the Fincept Marks lies not only in the literal trademark text but in the Fincept Trade Dress. Licensee shall not, in any forked, derivative, or successor product, replicate the Fincept Trade Dress in a manner likely to cause confusion, mistake, deception, association, or initial-interest confusion as to source or affiliation, even where the literal Fincept Marks have been removed or replaced. **Translation of UI text, terminal commands, function codes, or screen names into another language or alphabet does not extinguish trade-dress protection.** Renaming, abbreviating, or substituting individual screen names, function codes, terminal commands, or keyboard shortcuts does not avoid trade-dress liability where the underlying *system* of conventions is substantially preserved. Any product that retains substantially similar Fincept Trade Dress shall be deemed a Derivative Work for all purposes of this License, and any Commercial Use thereof requires a Commercial License from Licensor.
./docs/COMMERCIAL_LICENSE.md:116:**Comparative Advertising.** Any use of the Fincept Marks or Fincept Trade Dress in marketing, sales materials, demos, RFP responses, screenshots, or product comparisons by a for-profit competitor or its agents constitutes commercial use of the Marks and is prohibited absent express written permission, irrespective of any nominative-fair-use or comparative-advertising defense.
./docs/COMMERCIAL_LICENSE.md:120:Any Derivative Work that is publicly distributed in source-available form shall prominently display the notice: *"Derived from Fincept Terminal © Fincept Corporation; use of this Derivative Work for Commercial Use requires a separate Commercial License from Fincept Corporation, support@fincept.in."*
./docs/COMMERCIAL_LICENSE.md:128:| **Commercial License** | **USD 10,200 / year** per organization | Full Commercial Use rights for one legal entity; Fincept Data & API access; 65,000 credits/month (resets monthly); additional credits available for purchase |
./docs/COMMERCIAL_LICENSE.md:130:| **University & Academic** | **USD 799 / month** | 20 accounts for teaching and research at an accredited educational institution; Fincept Data access included; non-commercial classroom use only |
./docs/COMMERCIAL_LICENSE.md:133:Credits are consumed by Fincept Data Sources and API calls. When credits are exhausted, Licensee may purchase additional credits or wait for the monthly reset. Fees are payable annually in advance and non-refundable except as expressly stated.
./docs/COMMERCIAL_LICENSE.md:139:Subject to the terms of this License, Licensor grants Licensee a non-exclusive, worldwide, royalty-bearing license under Licensor's patent claims to make, have made, use, offer to sell, sell, import, and have imported the Software, solely as authorized hereunder.
./docs/COMMERCIAL_LICENSE.md:141:**If Licensee, or any entity controlling, controlled by, or under common control with Licensee, institutes patent litigation (including a cross-claim or counterclaim in a lawsuit) against any entity alleging that the Software, its use, or any contribution to it constitutes direct or contributory patent infringement, then any patent licenses granted to Licensee under this License shall terminate as of the date such litigation is filed.** Patent claims arising from modifications introduced by Licensee are not licensed.
./docs/COMMERCIAL_LICENSE.md:149:**Annual Self-Attestation.** Every for-profit user of the Software shall submit, by 31 January of each calendar year, a written attestation to support@fincept.in stating its license status, the number of users, the number of deployments, and the legal entity name(s) using the Software. Failure to file the attestation is a per se breach triggering the liquidated damages set forth in Section 13.
./docs/COMMERCIAL_LICENSE.md:151:**Privacy and Trade-Secret Limitations.** Where applicable data-protection law (including the EU General Data Protection Regulation, the Digital Personal Data Protection Act, 2023 (India), or analogous statutes) restricts disclosure of personal data, Licensor shall accept anonymized or pseudonymized data sufficient to verify compliance, comprising at minimum: (i) total user count, (ii) total deployment count, (iii) entity legal name, and (iv) hashed code-base fingerprints. Licensee bears the cost of any data-protection compliance for audit response. Where Licensee asserts trade-secret protection over its source code, Licensor will accept code review by an escrow agent operating under attorney-client privilege, with results delivered as compliance status only. Confidentiality obligations to third parties (NDAs with Licensee's clients) shall not impair Licensor's audit rights; Licensee shall use commercially reasonable efforts to obtain any necessary client consent or shall provide redacted equivalent information. Where applicable foreign blocking statute genuinely prevents disclosure, Licensee shall provide equivalent information from a permitted jurisdiction or pay liquidated damages in lieu of audit pursuant to Section 13.
./docs/COMMERCIAL_LICENSE.md:153:**Disclosure of Third-Party Developers.** Upon Licensor's written request, Licensee shall provide, within ten (10) business days: (a) the legal name and contact details of any Third-Party Developer engaged with the Software; (b) the scope of work; (c) copies of the relevant engagement agreement or statement of work, redacted only as to commercial pricing terms; and (d) a list of all repositories, deployment locations, and personnel with access to the Software.
./docs/COMMERCIAL_LICENSE.md:167:THE SOFTWARE IS PROVIDED "AS IS" AND "AS AVAILABLE," WITHOUT WARRANTY OF ANY KIND, EXPRESS, IMPLIED, OR STATUTORY, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NON-INFRINGEMENT, ACCURACY, RELIABILITY, OR THAT THE SOFTWARE WILL BE UNINTERRUPTED OR ERROR-FREE. NO INFORMATION OR ADVICE OBTAINED FROM LICENSOR SHALL CREATE ANY WARRANTY NOT EXPRESSLY STATED HEREIN. THE SOFTWARE IS NOT INTENDED FOR USE IN, AND IS NOT WARRANTED FOR USE IN, ANY APPLICATION WHERE FAILURE COULD RESULT IN FINANCIAL LOSS, REGULATORY VIOLATION, OR PERSONAL INJURY. NOTHING IN THE SOFTWARE OR ANY OUTPUT GENERATED BY IT CONSTITUTES INVESTMENT, LEGAL, TAX, ACCOUNTING, OR FINANCIAL ADVICE.
./docs/COMMERCIAL_LICENSE.md:173:Licensor actively monitors public code repositories, container registries, application stores, cloud marketplaces, SaaS platforms, and trademark registers for unlicensed Commercial Use of the Software, Modified Versions, and Derivative Works. Licensor reserves the right, without prior notice, to:
./docs/COMMERCIAL_LICENSE.md:177:3. Seek injunctive and monetary relief, including statutory damages, disgorgement of profits, and recovery of unpaid license fees calculated at the then-current Commercial License rate retroactive to first unauthorized use, plus interest, attorneys' fees, and costs;
./docs/COMMERCIAL_LICENSE.md:178:4. Pursue trademark infringement, passing-off, and unfair-competition claims for misuse of the Fincept Marks or Fincept Trade Dress;
./docs/COMMERCIAL_LICENSE.md:181:If you believe you may be using the Software commercially without a license, contact **support@fincept.in** for a good-faith resolution path.
./docs/COMMERCIAL_LICENSE.md:189:(i) actual damages flowing from unauthorized Commercial Use are inherently difficult to quantify because they include (a) lost Commercial License revenue that cannot be recovered through later licensing, (b) loss of competitive advantage and market share, (c) erosion of the dual-licensing business model that funds the open-source codebase, (d) costs of detection, monitoring, investigation, and enforcement against widespread unauthorized internal use, and (e) reputational and goodwill harm;
./docs/COMMERCIAL_LICENSE.md:202:| **Unauthorized commercial distribution, hosting, SaaS, or resale** of the Software or any Derivative Work | **USD 250,000** per distinct offering, plus disgorgement of all revenue derived therefrom |
./docs/COMMERCIAL_LICENSE.md:203:| **Unauthorized fork that replaces, removes, or rewires Fincept APIs and is used commercially or internally** | **USD 100,000** per organization, plus 5× the then-current Commercial License fee for each year of use, plus full backdated license fees from first unauthorized use |
./docs/COMMERCIAL_LICENSE.md:204:| **Unauthorized use of Fincept Marks or Fincept Trade Dress** in a forked, derivative, or rebranded product | **USD 150,000** per mark or trade-dress element, plus mandatory injunction, plus disgorgement of profits |
./docs/COMMERCIAL_LICENSE.md:210:1. All unpaid license fees, calculated retroactively at the then-current Commercial License rate from the date of first unauthorized use, plus interest at 18% per annum or the maximum permitted by law, whichever is lower;
./docs/COMMERCIAL_LICENSE.md:216:The liquidated damages stated above are **per violation, cumulative**, and apply **per year of unauthorized use**. Liquidated damages do not constitute a license fee, do not retroactively legitimize unauthorized use, and do not waive Licensor's right to seek injunctive relief, criminal prosecution, or any other remedy.
./docs/COMMERCIAL_LICENSE.md:226:1. **Joint and Several Liability.** The contracting company (the entity for whose benefit the work is performed) and each Third-Party Developer engaged by it (and any subcontractor of such Third-Party Developer) are each fully liable, individually and together, for the entirety of any damages, liquidated damages, license fees, disgorgement, and costs owed to Licensor. Licensor may pursue any one or more of them, in any combination, for the full amount.
./docs/COMMERCIAL_LICENSE.md:228:2. **No Defense of Delegation.** A contracting company cannot escape liability by claiming that the Third-Party Developer was solely responsible, that the contracting company did not write the code, that the Third-Party Developer represented the work as licensed, or that the contracting company did not know the Software was Fincept Terminal or a Derivative Work. The duty to verify license compliance is **non-delegable**.
./docs/COMMERCIAL_LICENSE.md:230:3. **No Defense of Lack of Knowledge.** Public availability of this License, the LICENSE file, the README, and the license notices embedded in the Software constitutes constructive notice. Ignorance of the license terms is not a defense for either the contracting company or the Third-Party Developer.
./docs/COMMERCIAL_LICENSE.md:234:   **Acquirer Liability.** An acquirer of any entity that has used the Software is jointly and severally liable for unauthorized use occurring before, during, and after the acquisition, irrespective of whether the transaction is structured as an asset purchase, stock purchase, merger, or otherwise, and irrespective of any non-assumption clause in the acquisition agreement. Acquirers are deemed to assume Software-license liabilities by operation of this License, with notice provided by the public availability hereof. Licensee shall conduct or commission a software-composition analysis (SCA) before deploying any third-party software with finance functionality; failure to do so constitutes willful blindness.
./docs/COMMERCIAL_LICENSE.md:236:   **Standstill on Transfer.** Upon receipt of any cease-and-desist notice, audit demand, or notice of breach, Licensee shall not transfer, license, assign, or sub-license the Software, any Derivative Work, related personnel, or related infrastructure to any affiliate or third party without Licensor's prior written consent. Any such transfer is void as against Licensor.
./docs/COMMERCIAL_LICENSE.md:244:8. **Public Notice Obligation.** Upon Licensor's request, a contracting company that engages a Third-Party Developer to work with the Software must provide Licensor, within ten (10) business days, with: (a) the legal name and contact details of the Third-Party Developer; (b) the scope of work; (c) copies of the relevant engagement agreement or statement of work redacted only as to commercial pricing terms; and (d) a list of all repositories, deployment locations, and personnel with access to the Software.
./docs/COMMERCIAL_LICENSE.md:254:TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, IN NO EVENT SHALL LICENSOR'S AGGREGATE LIABILITY UNDER OR IN CONNECTION WITH THIS LICENSE EXCEED THE TOTAL FEES PAID BY LICENSEE TO LICENSOR IN THE TWELVE (12) MONTHS IMMEDIATELY PRECEDING THE EVENT GIVING RISE TO LIABILITY, OR ONE HUNDRED INDIAN RUPEES (₹100), WHICHEVER IS GREATER. IN NO EVENT SHALL LICENSOR BE LIABLE FOR INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, EXEMPLARY, OR PUNITIVE DAMAGES, LOST PROFITS, LOST DATA, LOSS OF GOODWILL, OR TRADING LOSSES, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. THESE LIMITATIONS APPLY REGARDLESS OF THE FORM OF ACTION, WHETHER IN CONTRACT, TORT, STRICT LIABILITY, OR OTHERWISE.
./docs/COMMERCIAL_LICENSE.md:268:**No Waiver, Estoppel, or Acquiescence.** No silence, inaction, delay, public communication, social-media post, marketing statement, conference talk, or course of dealing by Licensor shall constitute a waiver, license, estoppel, acquiescence, laches, or implied license. Public-facing marketing or media that describes the Software as "free" or "open source" refers exclusively to the AGPL-3.0 option for individual non-commercial users and shall not be construed as a Commercial Use license, an implied license, a waiver, or a representation. Licensee may not rely on Licensor's failure to enforce against any third party.
./docs/COMMERCIAL_LICENSE.md:288:**Notices.** Notices to Licensor must be sent to support@fincept.in with a copy by registered post to Fincept Corporation's registered office.
./docs/COMMERCIAL_LICENSE.md:292:**Non-Transferability.** Licenses are non-transferable. Annual licenses renew yearly unless cancelled with thirty (30) days' notice prior to the renewal date.
./docs/COMMERCIAL_LICENSE.md:307:"Fincept", "Fincept Terminal", and the Fincept logo are trademarks of Fincept Corporation. All rights reserved. Use of these marks — including in any forked, derivative, rebranded, or commercial product — requires prior written permission.
./docs/COMMERCIAL_LICENSE.md:309:© 2025–2026 Fincept Corporation. All rights reserved.
./docs/COMMERCIAL_LICENSE.md:315:**Status:** Current and binding. These terms remain in full force and effect indefinitely until expressly superseded by a subsequent version published by Fincept Corporation at this location. The date above marks the most recent revision; it is **not** an expiry date.
./docs/COMMERCIAL_LICENSE.md:317:**Scope of Application.** This License governs all current and future use of the Software, including use of historical versions, regardless of when those versions were originally published. Any Commercial Use of any version of Fincept Terminal — past, present, or future, including any branch, tag, release, or commit — is subject to the terms of this License.
./docs/COMMERCIAL_LICENSE.md:319:For the open-source license terms, see [`/LICENSE`](../LICENSE).
./docs/ARCHITECTURE.md:1:# Fincept Terminal Architecture
./docs/ARCHITECTURE.md:4:This document provides a comprehensive overview of Fincept Terminal v4's architecture — a native C++20 desktop application.
./docs/ARCHITECTURE.md:298:- **GitHub Issues:** https://github.com/Fincept-Corporation/FinceptTerminal/issues
./docs/CPP_CONTRIBUTOR_GUIDE.md:3:This guide covers C++ development for Fincept Terminal — 40+ screens, core infrastructure, trading engine, and Qt6 UI.
./docs/CPP_CONTRIBUTOR_GUIDE.md:231:**Questions?** Open an issue on [GitHub](https://github.com/Fincept-Corporation/FinceptTerminal).
./docs/GETTING_STARTED.md:1:# Getting Started with Fincept Terminal Development
./docs/GETTING_STARTED.md:4:Welcome to Fincept Terminal! This guide will get you from zero to your first contribution.
./docs/GETTING_STARTED.md:8:## What is Fincept Terminal?
./docs/GETTING_STARTED.md:10:Fincept Terminal is an **open-source financial analysis platform** — a free, open-source alternative to Bloomberg Terminal. Version 4 is a native C++20 application built with Qt6.
./docs/GETTING_STARTED.md:40:> **Use exactly these versions.** Fincept Terminal's CMake build enforces them with `FATAL_ERROR` checks. Newer/older versions will refuse to configure.
./docs/GETTING_STARTED.md:88:git clone https://github.com/Fincept-Corporation/FinceptTerminal.git
./docs/GETTING_STARTED.md:89:cd FinceptTerminal/fincept-qt
./docs/GETTING_STARTED.md:97:./build/linux-release/FinceptTerminal              # Linux
./docs/GETTING_STARTED.md:98:./build/macos-release/FinceptTerminal.app/Contents/MacOS/FinceptTerminal   # macOS
./docs/GETTING_STARTED.md:99:.\build\win-release\FinceptTerminal.exe            # Windows
./docs/GETTING_STARTED.md:109:**Expected Result:** Fincept Terminal window should open, showing the login screen.
./docs/GETTING_STARTED.md:126:FinceptTerminal/
./docs/GETTING_STARTED.md:129:│   ├── src/                        ← C++ source code
./docs/GETTING_STARTED.md:312:| GitHub Issues | https://github.com/Fincept-Corporation/FinceptTerminal/issues |
./docs/GETTING_STARTED.md:313:| GitHub Discussions | https://github.com/Fincept-Corporation/FinceptTerminal/discussions |
./docs/GETTING_STARTED.md:320:- Pick an issue: https://github.com/Fincept-Corporation/FinceptTerminal/issues
./docs/CONTRIBUTING.md:1:# Contributing to Fincept Terminal
./docs/CONTRIBUTING.md:3:Fincept Terminal is an open-source native C++20/Qt6 financial intelligence platform with 50+ screens, embedded Python analytics, and 100+ data connectors. This guide is the canonical **how-to** for contributors — build, architecture, conventions.
./docs/CONTRIBUTING.md:74:git clone https://github.com/Fincept-Corporation/FinceptTerminal.git
./docs/CONTRIBUTING.md:75:cd FinceptTerminal
./docs/CONTRIBUTING.md:113:.\build\win-release\FinceptTerminal.exe                                           # Windows
./docs/CONTRIBUTING.md:114:./build/linux-release/FinceptTerminal                                             # Linux
./docs/CONTRIBUTING.md:115:./build/macos-release/FinceptTerminal.app/Contents/MacOS/FinceptTerminal          # macOS
./docs/CONTRIBUTING.md:258:| Issues       | [GitHub Issues](https://github.com/Fincept-Corporation/FinceptTerminal/issues) |
./docs/CONTRIBUTING.md:259:| Discussions  | [GitHub Discussions](https://github.com/Fincept-Corporation/FinceptTerminal/discussions) |
./docs/CONTRIBUTING.md:267:**Repository:** https://github.com/Fincept-Corporation/FinceptTerminal
./docs/CONTRIBUTING.md:268:**License:** AGPL-3.0-or-later
./docs/translations/README.hi.md:5:[![License: AGPL-3.0](https://img.shields.io/badge/license-AGPL--3.0-C06524)](https://github.com/Fincept-Corporation/FinceptTerminal/blob/main/LICENSE)[![C++20](https://img.shields.io/badge/C%2B%2B-20-00599C?logo=cplusplus)](https://isocpp.org/)[![Qt6](https://img.shields.io/badge/Qt-6-41CD52?logo=qt&logoColor=white)](https://www.qt.io/)[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)[![Hits](https://hits.sh/github.com/Fincept-Corporation/FinceptTerminal.svg?label=Visits)](https://hits.sh/github.com/Fincept-Corporation/FinceptTerminal/)
./docs/translations/README.hi.md:7:[![Twitter](https://img.shields.io/badge/-Twitter-1DA1F2?style=flat-square&logo=twitter&logoColor=white)](https://twitter.com/intent/tweet?text=Check%20out%20FinceptTerminal&url=https%3A//github.com/Fincept-Corporation/FinceptTerminal/)[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Fincept-Corporation/FinceptTerminal/)[![Facebook](https://img.shields.io/badge/-Facebook-1877F2?style=flat-square&logo=facebook&logoColor=white)](https://www.facebook.com/sharer/sharer.php?u=https%3A//github.com/Fincept-Corporation/FinceptTerminal/)[![Reddit](https://img.shields.io/badge/-Reddit-FF4500?style=flat-square&logo=reddit&logoColor=white)](https://www.reddit.com/submit?url=https%3A//github.com/Fincept-Corporation/FinceptTerminal/&title=FinceptTerminal)[![WhatsApp](https://img.shields.io/badge/-WhatsApp-25D366?style=flat-square&logo=whatsapp&logoColor=white)](https://api.whatsapp.com/send?text=Check%20out%20FinceptTerminal%3A%20https%3A//github.com/Fincept-Corporation/FinceptTerminal/)
./docs/translations/README.hi.md:13:[📥 Download](https://github.com/Fincept-Corporation/FinceptTerminal/releases)·[📚 दस्तावेज़](https://github.com/Fincept-Corporation/FinceptTerminal/tree/main/docs)·[💬चर्चाएँ](https://github.com/Fincept-Corporation/FinceptTerminal/discussions)·[💬 कलह](https://discord.gg/ae87a8ygbN)·[🤝साथी](https://github.com/Fincept-Corporation/FinceptTerminal/blob/main/docs/COMMERCIAL_LICENSE.md)
./docs/translations/README.hi.md:15:![Fincept Terminal](https://raw.githubusercontent.com/Fincept-Corporation/FinceptTerminal/main/images/Dashboard.png)
./docs/translations/README.hi.md:46:पूर्व-निर्मित बायनेरिज़ पर उपलब्ध हैं[पेज जारी करता है](https://github.com/Fincept-Corporation/FinceptTerminal/releases). किसी निर्माण उपकरण की आवश्यकता नहीं है - बस निकालें और चलाएं।
./docs/translations/README.hi.md:50:| **विंडोज़ x64**           | `FinceptTerminal-Windows-x64.zip`        | निकालें →`FinceptTerminal.exe`                       |
./docs/translations/README.hi.md:51:| **विंडोज़ एआरएम64**       | `FinceptTerminal-Windows-arm64.zip`      | निकालें →`FinceptTerminal.exe`                       |
./docs/translations/README.hi.md:52:| **लिनक्स x64**            | `FinceptTerminal-Linux-x86_64.AppImage`  | `chmod +x`→`./FinceptTerminal-Linux-x86_64.AppImage` |
./docs/translations/README.hi.md:53:| **macOS (एप्पल सिलिकॉन)** | `FinceptTerminal-macOS-arm64.tar.gz`     | निकालें →`./FinceptTerminal`                         |
./docs/translations/README.hi.md:54:| **मैकओएस (इंटेल)**        | `FinceptTerminal-macOS-x64.tar.gz`       | निकालें →`./FinceptTerminal`                         |
./docs/translations/README.hi.md:55:| **मैकओएस (यूनिवर्सल)**    | `FinceptTerminal-macOS-universal.tar.gz` | निकालें →`./FinceptTerminal`                         |
./docs/translations/README.hi.md:65:git clone https://github.com/Fincept-Corporation/FinceptTerminal.git
./docs/translations/README.hi.md:66:cd FinceptTerminal
./docs/translations/README.hi.md:72:git clone https://github.com/Fincept-Corporation/FinceptTerminal.git
./docs/translations/README.hi.md:73:cd FinceptTerminal
./docs/translations/README.hi.md:90:git clone https://github.com/Fincept-Corporation/FinceptTerminal.git
./docs/translations/README.hi.md:91:cd FinceptTerminal
./docs/translations/README.hi.md:112:> cd FinceptTerminal/fincept-qt
./docs/translations/README.hi.md:163:git clone https://github.com/Fincept-Corporation/FinceptTerminal.git
./docs/translations/README.hi.md:164:cd FinceptTerminal/fincept-qt
./docs/translations/README.hi.md:178:./build/FinceptTerminal              # Linux / macOS
./docs/translations/README.hi.md:179:.\build\Release\FinceptTerminal.exe  # Windows
./docs/translations/README.hi.md:220:-   [रिपोर्ट बग](https://github.com/Fincept-Corporation/FinceptTerminal/issues)
./docs/translations/README.hi.md:221:-   [फ़ीचर का अनुरोध करें](https://github.com/Fincept-Corporation/FinceptTerminal/discussions)
./docs/translations/README.hi.md:236:[विश्वविद्यालय लाइसेंसिंग विवरण](https://github.com/Fincept-Corporation/FinceptTerminal/blob/main/docs/COMMERCIAL_LICENSE.md)
./docs/translations/README.hi.md:254:-   विवरण:[वाणिज्यिक लाइसेंस गाइड](https://github.com/Fincept-Corporation/FinceptTerminal/blob/main/docs/COMMERCIAL_LICENSE.md)
./docs/translations/README.hi.md:269:<a href="https://star-history.com/#Fincept-Corporation/FinceptTerminal&Date">
./docs/translations/README.hi.md:271:   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=Fincept-Corporation/FinceptTerminal&type=Date&theme=dark" />
./docs/translations/README.hi.md:272:   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=Fincept-Corporation/FinceptTerminal&type=Date" />
./docs/translations/README.hi.md:273:   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=Fincept-Corporation/FinceptTerminal&type=Date" />
./docs/translations/README.fr.md:1:# Terminal Fincept
./docs/translations/README.fr.md:5:[![License: AGPL-3.0](https://img.shields.io/badge/license-AGPL--3.0-C06524)](https://github.com/Fincept-Corporation/FinceptTerminal/blob/main/LICENSE)[![C++20](https://img.shields.io/badge/C%2B%2B-20-00599C?logo=cplusplus)](https://isocpp.org/)[![Qt6](https://img.shields.io/badge/Qt-6-41CD52?logo=qt&logoColor=white)](https://www.qt.io/)[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)[![Hits](https://hits.sh/github.com/Fincept-Corporation/FinceptTerminal.svg?label=Visits)](https://hits.sh/github.com/Fincept-Corporation/FinceptTerminal/)
./docs/translations/README.fr.md:7:[![Twitter](https://img.shields.io/badge/-Twitter-1DA1F2?style=flat-square&logo=twitter&logoColor=white)](https://twitter.com/intent/tweet?text=Check%20out%20FinceptTerminal&url=https%3A//github.com/Fincept-Corporation/FinceptTerminal/)[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Fincept-Corporation/FinceptTerminal/)[![Facebook](https://img.shields.io/badge/-Facebook-1877F2?style=flat-square&logo=facebook&logoColor=white)](https://www.facebook.com/sharer/sharer.php?u=https%3A//github.com/Fincept-Corporation/FinceptTerminal/)[![Reddit](https://img.shields.io/badge/-Reddit-FF4500?style=flat-square&logo=reddit&logoColor=white)](https://www.reddit.com/submit?url=https%3A//github.com/Fincept-Corporation/FinceptTerminal/&title=FinceptTerminal)[![WhatsApp](https://img.shields.io/badge/-WhatsApp-25D366?style=flat-square&logo=whatsapp&logoColor=white)](https://api.whatsapp.com/send?text=Check%20out%20FinceptTerminal%3A%20https%3A//github.com/Fincept-Corporation/FinceptTerminal/)
./docs/translations/README.fr.md:13:[📥 Télécharger](https://github.com/Fincept-Corporation/FinceptTerminal/releases)·[📚 Documents](https://github.com/Fincept-Corporation/FinceptTerminal/tree/main/docs)·[💬 Discussions](https://github.com/Fincept-Corporation/FinceptTerminal/discussions)·[💬 Discorde](https://discord.gg/ae87a8ygbN)·[🤝 Partenaire](https://github.com/Fincept-Corporation/FinceptTerminal/blob/main/docs/COMMERCIAL_LICENSE.md)
./docs/translations/README.fr.md:15:![Fincept Terminal](https://raw.githubusercontent.com/Fincept-Corporation/FinceptTerminal/main/images/Dashboard.png)
./docs/translations/README.fr.md:23:**Fincept Terminal vch**est une application de bureau C++20 purement native. Il utilise**Qt6**pour l'interface utilisateur et le rendu, intégré**Python**pour l'analyse et offre des performances de classe terminal Bloomberg dans un seul binaire natif.
./docs/translations/README.fr.md:46:Des binaires prédéfinis sont disponibles sur le[Page des versions](https://github.com/Fincept-Corporation/FinceptTerminal/releases). Aucun outil de construction requis : il suffit d'extraire et d'exécuter.
./docs/translations/README.fr.md:50:| **Windows x64**            | `FinceptTerminal-Windows-x64.zip`        | Extraire →`FinceptTerminal.exe`                      |
./docs/translations/README.fr.md:51:| **WindowsARM64**           | `FinceptTerminal-Windows-arm64.zip`      | Extraire →`FinceptTerminal.exe`                      |
./docs/translations/README.fr.md:52:| **Linuxx64**               | `FinceptTerminal-Linux-x86_64.AppImage`  | `chmod +x`→`./FinceptTerminal-Linux-x86_64.AppImage` |
./docs/translations/README.fr.md:53:| **macOS (Apple Silicium)** | `FinceptTerminal-macOS-arm64.tar.gz`     | Extraire →`./FinceptTerminal`                        |
./docs/translations/README.fr.md:54:| **macOS (Intel)**          | `FinceptTerminal-macOS-x64.tar.gz`       | Extraire →`./FinceptTerminal`                        |
./docs/translations/README.fr.md:55:| **macOS (universel)**      | `FinceptTerminal-macOS-universal.tar.gz` | Extraire →`./FinceptTerminal`                        |
./docs/translations/README.fr.md:65:git clone https://github.com/Fincept-Corporation/FinceptTerminal.git
./docs/translations/README.fr.md:66:cd FinceptTerminal
./docs/translations/README.fr.md:72:git clone https://github.com/Fincept-Corporation/FinceptTerminal.git
./docs/translations/README.fr.md:73:cd FinceptTerminal
./docs/translations/README.fr.md:90:git clone https://github.com/Fincept-Corporation/FinceptTerminal.git
./docs/translations/README.fr.md:91:cd FinceptTerminal
./docs/translations/README.fr.md:112:> cd FinceptTerminal/fincept-qt
./docs/translations/README.fr.md:162:git clone https://github.com/Fincept-Corporation/FinceptTerminal.git
./docs/translations/README.fr.md:163:cd FinceptTerminal/fincept-qt
./docs/translations/README.fr.md:177:./build/FinceptTerminal              # Linux / macOS
./docs/translations/README.fr.md:178:.\build\Release\FinceptTerminal.exe  # Windows
./docs/translations/README.fr.md:187:**Terminal Fincept**est une plateforme financière open source conçue pour ceux qui refusent d'être limités par les logiciels traditionnels. Nous sommes en compétition sur**profondeur d'analyse**et**accessibilité des données**– pas sur les informations privilégiées ou les flux exclusifs.
./docs/translations/README.fr.md:195:-   **Gratuit et open source**(AGPL-3.0) avec licences commerciales disponibles
./docs/translations/README.fr.md:219:-   [Signaler un bug](https://github.com/Fincept-Corporation/FinceptTerminal/issues)
./docs/translations/README.fr.md:220:-   [Fonctionnalité de demande](https://github.com/Fincept-Corporation/FinceptTerminal/discussions)
./docs/translations/README.fr.md:229:-   Accès complet aux données et API Fincept
./docs/translations/README.fr.md:235:[Détails de la licence universitaire](https://github.com/Fincept-Corporation/FinceptTerminal/blob/main/docs/COMMERCIAL_LICENSE.md)
./docs/translations/README.fr.md:241:**Double licence : AGPL-3.0 (Open Source) + Commerciale**
./docs/translations/README.fr.md:243:### Source ouverte (AGPL-3.0)
./docs/translations/README.fr.md:245:-   Gratuit pour un usage personnel, éducatif et non commercial
./docs/translations/README.fr.md:249:### Licence commerciale
./docs/translations/README.fr.md:251:-   Requis pour un usage professionnel ou pour accéder commercialement aux données/API Fincept
./docs/translations/README.fr.md:253:-   Détails:[Guide des licences commerciales](https://github.com/Fincept-Corporation/FinceptTerminal/blob/main/docs/COMMERCIAL_LICENSE.md)
./docs/translations/README.fr.md:257:« Fincept Terminal » et « Fincept » sont des marques commerciales de Fincept Corporation.
./docs/translations/README.fr.md:259:© 2025-2026 Fincept Corporation. Tous droits réservés.
./docs/translations/README.fr.md:268:<a href="https://star-history.com/#Fincept-Corporation/FinceptTerminal&Date">
./docs/translations/README.fr.md:270:   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=Fincept-Corporation/FinceptTerminal&type=Date&theme=dark" />
./docs/translations/README.fr.md:271:   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=Fincept-Corporation/FinceptTerminal&type=Date" />
./docs/translations/README.fr.md:272:   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=Fincept-Corporation/FinceptTerminal&type=Date" />
./docs/translations/README.es.md:1:# Terminal Fincept
./docs/translations/README.es.md:5:[![License: AGPL-3.0](https://img.shields.io/badge/license-AGPL--3.0-C06524)](https://github.com/Fincept-Corporation/FinceptTerminal/blob/main/LICENSE)[![C++20](https://img.shields.io/badge/C%2B%2B-20-00599C?logo=cplusplus)](https://isocpp.org/)[![Qt6](https://img.shields.io/badge/Qt-6-41CD52?logo=qt&logoColor=white)](https://www.qt.io/)[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)[![Hits](https://hits.sh/github.com/Fincept-Corporation/FinceptTerminal.svg?label=Visits)](https://hits.sh/github.com/Fincept-Corporation/FinceptTerminal/)
./docs/translations/README.es.md:7:[![Twitter](https://img.shields.io/badge/-Twitter-1DA1F2?style=flat-square&logo=twitter&logoColor=white)](https://twitter.com/intent/tweet?text=Check%20out%20FinceptTerminal&url=https%3A//github.com/Fincept-Corporation/FinceptTerminal/)[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Fincept-Corporation/FinceptTerminal/)[![Facebook](https://img.shields.io/badge/-Facebook-1877F2?style=flat-square&logo=facebook&logoColor=white)](https://www.facebook.com/sharer/sharer.php?u=https%3A//github.com/Fincept-Corporation/FinceptTerminal/)[![Reddit](https://img.shields.io/badge/-Reddit-FF4500?style=flat-square&logo=reddit&logoColor=white)](https://www.reddit.com/submit?url=https%3A//github.com/Fincept-Corporation/FinceptTerminal/&title=FinceptTerminal)[![WhatsApp](https://img.shields.io/badge/-WhatsApp-25D366?style=flat-square&logo=whatsapp&logoColor=white)](https://api.whatsapp.com/send?text=Check%20out%20FinceptTerminal%3A%20https%3A//github.com/Fincept-Corporation/FinceptTerminal/)
./docs/translations/README.es.md:13:[📥 Descargar](https://github.com/Fincept-Corporation/FinceptTerminal/releases)·[📚 Documentos](https://github.com/Fincept-Corporation/FinceptTerminal/tree/main/docs)·[💬 Discusiones](https://github.com/Fincept-Corporation/FinceptTerminal/discussions)·[💬 Discordia](https://discord.gg/ae87a8ygbN)·[🤝 Socio](https://github.com/Fincept-Corporation/FinceptTerminal/blob/main/docs/COMMERCIAL_LICENSE.md)
./docs/translations/README.es.md:15:![Fincept Terminal](https://raw.githubusercontent.com/Fincept-Corporation/FinceptTerminal/main/images/Dashboard.png)
./docs/translations/README.es.md:46:Los archivos binarios prediseñados están disponibles en[Página de lanzamientos](https://github.com/Fincept-Corporation/FinceptTerminal/releases). No se requieren herramientas de compilación: simplemente extraiga y ejecute.
./docs/translations/README.es.md:50:| **Ventanas x64**          | `FinceptTerminal-Windows-x64.zip`        | Extraer →`FinceptTerminal.exe`                       |
./docs/translations/README.es.md:51:| **ventanas ARM64**        | `FinceptTerminal-Windows-arm64.zip`      | Extraer →`FinceptTerminal.exe`                       |
./docs/translations/README.es.md:52:| **Linuxx64**              | `FinceptTerminal-Linux-x86_64.AppImage`  | `chmod +x`→`./FinceptTerminal-Linux-x86_64.AppImage` |
./docs/translations/README.es.md:53:| **macOS (Apple Silicio)** | `FinceptTerminal-macOS-arm64.tar.gz`     | Extraer →`./FinceptTerminal`                         |
./docs/translations/README.es.md:54:| **MacOS (Intel)**         | `FinceptTerminal-macOS-x64.tar.gz`       | Extraer →`./FinceptTerminal`                         |
./docs/translations/README.es.md:55:| **macOS (universal)**     | `FinceptTerminal-macOS-universal.tar.gz` | Extraer →`./FinceptTerminal`                         |
./docs/translations/README.es.md:65:git clone https://github.com/Fincept-Corporation/FinceptTerminal.git
./docs/translations/README.es.md:66:cd FinceptTerminal
./docs/translations/README.es.md:72:git clone https://github.com/Fincept-Corporation/FinceptTerminal.git
./docs/translations/README.es.md:73:cd FinceptTerminal
./docs/translations/README.es.md:90:git clone https://github.com/Fincept-Corporation/FinceptTerminal.git
./docs/translations/README.es.md:91:cd FinceptTerminal
./docs/translations/README.es.md:112:> cd FinceptTerminal/fincept-qt
./docs/translations/README.es.md:122:**Terminal Fincept**es una plataforma financiera de código abierto creada para aquellos que se niegan a verse limitados por el software tradicional. Competimos en**profundidad analítica**y**accesibilidad a los datos**– no en información privilegiada ni en feeds exclusivos.
./docs/translations/README.es.md:130:-   **Gratis y de código abierto**(AGPL-3.0) con licencias comerciales disponibles
./docs/translations/README.es.md:154:-   [Informar error](https://github.com/Fincept-Corporation/FinceptTerminal/issues)
```

## 8. C++ / Qt / GUI 关键词扫描

```text
./.github/scripts/generate_updates_manifest.py:8:    REPO     "owner/name" (e.g. "Fincept-Corporation/FinceptTerminal").
./.github/scripts/generate_updates_manifest.py:37:        ("windows-x64",     re.compile(rf"FinceptTerminal-{re.escape(version)}-windows-x64-setup\.exe$")),
./.github/scripts/generate_updates_manifest.py:38:        ("windows-arm64",   re.compile(rf"FinceptTerminal-{re.escape(version)}-windows-arm64-setup\.exe$")),
./.github/scripts/generate_updates_manifest.py:39:        ("linux-x64",       re.compile(rf"FinceptTerminal-{re.escape(version)}-linux-x64-setup\.run$")),
./.github/scripts/generate_updates_manifest.py:40:        ("linux-arm64",     re.compile(rf"FinceptTerminal-{re.escape(version)}-linux-arm64-setup\.run$")),
./.github/scripts/generate_updates_manifest.py:41:        ("macos-arm64",     re.compile(rf"FinceptTerminal-{re.escape(version)}-macos-arm64-setup\.(dmg|exe)$")),
./.github/scripts/generate_updates_manifest.py:42:        ("macos-x64",       re.compile(rf"FinceptTerminal-{re.escape(version)}-macos-x64-setup\.(dmg|exe)$")),
./.github/scripts/generate_updates_manifest.py:43:        ("macos-universal", re.compile(rf"FinceptTerminal-{re.escape(version)}-macos-universal-setup\.(dmg|exe)$")),
./.github/scripts/generate_updates_manifest.py:68:            "changelog": f"Fincept Terminal v{version} — see release notes at {release_url}",
./fincept-qt/tests/datahub/test_datahub.cpp:1:// Fincept Terminal — DataHub Phase 1 unit tests
./fincept-qt/tests/datahub/test_datahub.cpp:4:// app-wide plumbing. Uses Qt Test.
./fincept-qt/tests/mcp/test_validator.cpp:5:// and unknown-key tolerance. Uses Qt Test.
./fincept-qt/scripts/scb_data.py:133:            'User-Agent': 'Fincept-Terminal/1.0',
./fincept-qt/scripts/adb_data.py:4:Returns JSON output for Qt/C++ integration
./fincept-qt/scripts/nber_data.py:3:Fetches NBER (National Bureau of Economic Research) business cycle dates,
./fincept-qt/scripts/algo_trading/backtest_engine.py:429:        candidate = os.path.join(appdata, 'Fincept', 'FinceptTerminal', 'fincept.db')
./fincept-qt/scripts/algo_trading/scanner_engine.py:35:        candidate = os.path.join(appdata, 'Fincept', 'FinceptTerminal', 'fincept.db')
./fincept-qt/scripts/algo_trading/algo_manager.py:28:        candidate = os.path.join(appdata, 'Fincept', 'FinceptTerminal', 'fincept.db')
./fincept-qt/scripts/hdx_data.py:17:USER_AGENT = "FinceptTerminal_GeopoliticsAnalytics/3.0"
./fincept-qt/scripts/akshare_index.py:544:    "index_news_sentiment": {"func": get_index_news_sentiment_scope, "desc": "News sentiment index", "category": "Other Index"},
./fincept-qt/scripts/alpha_arena/types/responses.py:334:        content=f"{model_name}: Portfolio ${portfolio_value:,.2f} (P&L: ${total_pnl:+,.2f})",
./fincept-qt/scripts/alpha_arena/types/models.py:158:class PortfolioState(BaseModel):
./fincept-qt/scripts/alpha_arena/types/models.py:233:    portfolio_value_before: Optional[float] = Field(None, description="Portfolio before trade")
./fincept-qt/scripts/alpha_arena/types/models.py:234:    portfolio_value_after: Optional[float] = Field(None, description="Portfolio after trade")
./fincept-qt/scripts/alpha_arena/types/models.py:329:    portfolios: Dict[str, PortfolioState] = Field(default_factory=dict, description="Model portfolios")
./fincept-qt/scripts/alpha_arena/types/models.py:343:    portfolio_value: float = Field(..., description="Portfolio value")
./fincept-qt/scripts/alpha_arena/types/__init__.py:16:    PortfolioState,
./fincept-qt/scripts/alpha_arena/types/__init__.py:45:    "PortfolioState",
./fincept-qt/scripts/alpha_arena/core/paper_trading.py:14:    PortfolioState,
./fincept-qt/scripts/alpha_arena/core/paper_trading.py:32:    - Portfolio state management
./fincept-qt/scripts/alpha_arena/core/paper_trading.py:51:        # Portfolio state
./fincept-qt/scripts/alpha_arena/core/paper_trading.py:58:    def get_portfolio_state(self, current_prices: Dict[str, float] = None) -> PortfolioState:
./fincept-qt/scripts/alpha_arena/core/paper_trading.py:66:            PortfolioState with current values
./fincept-qt/scripts/alpha_arena/core/paper_trading.py:92:        return PortfolioState(
./fincept-qt/scripts/alpha_arena/core/hitl.py:168:            description="Portfolio drawdown exceeds 20%",
./fincept-qt/scripts/alpha_arena/core/competition.py:23:    PortfolioState,
./fincept-qt/scripts/alpha_arena/core/competition.py:573:    def get_portfolio_states(self) -> Dict[str, PortfolioState]:
./fincept-qt/scripts/alpha_arena/core/base_agent.py:8:- Portfolio metrics tracking
./fincept-qt/scripts/alpha_arena/core/base_agent.py:20:    PortfolioState,
./fincept-qt/scripts/alpha_arena/core/base_agent.py:48:        PortfolioAnalyzer,
./fincept-qt/scripts/alpha_arena/core/base_agent.py:49:        PortfolioMetrics,
./fincept-qt/scripts/alpha_arena/core/base_agent.py:55:    logger.debug("Portfolio metrics not available")
./fincept-qt/scripts/alpha_arena/core/base_agent.py:138:    - Portfolio metrics tracking
./fincept-qt/scripts/alpha_arena/core/base_agent.py:167:        # Portfolio metrics
./fincept-qt/scripts/alpha_arena/core/base_agent.py:169:        self._portfolio_analyzer: Optional[PortfolioAnalyzer] = None
./fincept-qt/scripts/alpha_arena/core/base_agent.py:184:            logger.info(f"Portfolio metrics initialized for {self.name}")
./fincept-qt/scripts/alpha_arena/core/base_agent.py:228:        portfolio: PortfolioState,
./fincept-qt/scripts/alpha_arena/core/base_agent.py:247:        portfolio: PortfolioState,
./fincept-qt/scripts/alpha_arena/core/base_agent.py:292:        - portfolio: PortfolioState
./fincept-qt/scripts/alpha_arena/core/base_agent.py:617:        portfolio: PortfolioState,
./fincept-qt/scripts/alpha_arena/core/base_agent.py:779:        portfolio: PortfolioState,
./fincept-qt/scripts/alpha_arena/core/base_agent.py:799:        portfolio: PortfolioState,
./fincept-qt/scripts/alpha_arena/core/base_agent.py:808:        portfolio: PortfolioState,
./fincept-qt/scripts/alpha_arena/core/base_agent.py:889:  Total Portfolio Value: ${portfolio.portfolio_value:,.2f}
./fincept-qt/scripts/alpha_arena/core/base_agent.py:1168:        portfolio: PortfolioState,
./fincept-qt/scripts/alpha_arena/core/base_agent.py:1242:        portfolio: PortfolioState,
./fincept-qt/scripts/alpha_arena/core/database.py:29:    """Get the path to the main Fincept Terminal database for paper trading integration."""
./fincept-qt/scripts/alpha_arena/core/database.py:320:        """Save decision to main Fincept Terminal database."""
./fincept-qt/scripts/alpha_arena/core/database.py:426:        """Save snapshot to main Fincept Terminal database."""
./fincept-qt/scripts/alpha_arena/core/database.py:519:        """Save leaderboard to main Fincept Terminal database."""
./fincept-qt/scripts/alpha_arena/core/__init__.py:9:- Portfolio metrics with Sharpe ratio
./fincept-qt/scripts/alpha_arena/core/__init__.py:11:- Research agent for SEC filings
./fincept-qt/scripts/alpha_arena/core/__init__.py:34:    PortfolioAnalyzer,
./fincept-qt/scripts/alpha_arena/core/__init__.py:35:    PortfolioMetrics,
./fincept-qt/scripts/alpha_arena/core/__init__.py:55:    ResearchAgent,
./fincept-qt/scripts/alpha_arena/core/__init__.py:56:    ResearchReport,
./fincept-qt/scripts/alpha_arena/core/__init__.py:79:    NewsArticle,
./fincept-qt/scripts/alpha_arena/core/__init__.py:109:    # Portfolio metrics
./fincept-qt/scripts/alpha_arena/core/__init__.py:110:    "PortfolioAnalyzer",
./fincept-qt/scripts/alpha_arena/core/__init__.py:111:    "PortfolioMetrics",
./fincept-qt/scripts/alpha_arena/core/__init__.py:127:    # Research
./fincept-qt/scripts/alpha_arena/core/__init__.py:128:    "ResearchAgent",
./fincept-qt/scripts/alpha_arena/core/__init__.py:129:    "ResearchReport",
./fincept-qt/scripts/alpha_arena/core/__init__.py:150:    "NewsArticle",
./fincept-qt/scripts/alpha_arena/core/sentiment_agent.py:37:class NewsArticle:
./fincept-qt/scripts/alpha_arena/core/sentiment_agent.py:137:            logger.info("GNews available for sentiment analysis")
./fincept-qt/scripts/alpha_arena/core/sentiment_agent.py:139:            logger.warning("GNews not available - using limited sentiment analysis")
./fincept-qt/scripts/alpha_arena/core/sentiment_agent.py:199:    ) -> List[NewsArticle]:
./fincept-qt/scripts/alpha_arena/core/sentiment_agent.py:209:            List of NewsArticle objects
./fincept-qt/scripts/alpha_arena/core/sentiment_agent.py:229:                logger.warning(f"News fetch failed: {data.get('error')}")
./fincept-qt/scripts/alpha_arena/core/sentiment_agent.py:241:                articles.append(NewsArticle(
./fincept-qt/scripts/alpha_arena/core/portfolio_metrics.py:2:Portfolio Metrics for Alpha Arena
./fincept-qt/scripts/alpha_arena/core/portfolio_metrics.py:17:from alpha_arena.types.models import PortfolioState, TradeResult
./fincept-qt/scripts/alpha_arena/core/portfolio_metrics.py:24:class PortfolioMetrics:
./fincept-qt/scripts/alpha_arena/core/portfolio_metrics.py:126:class PortfolioAnalyzer:
./fincept-qt/scripts/alpha_arena/core/portfolio_metrics.py:131:    - Portfolio value history for drawdown/volatility
./fincept-qt/scripts/alpha_arena/core/portfolio_metrics.py:185:    def calculate_metrics(self) -> PortfolioMetrics:
./fincept-qt/scripts/alpha_arena/core/portfolio_metrics.py:187:        metrics = PortfolioMetrics()
./fincept-qt/scripts/alpha_arena/core/portfolio_metrics.py:262:        Sharpe = (Portfolio Return - Risk-Free Rate) / Portfolio Volatility
./fincept-qt/scripts/alpha_arena/core/portfolio_metrics.py:382:_analyzers: Dict[str, PortfolioAnalyzer] = {}
./fincept-qt/scripts/alpha_arena/core/portfolio_metrics.py:385:def get_analyzer(model_name: str, initial_capital: float = 10000.0) -> PortfolioAnalyzer:
./fincept-qt/scripts/alpha_arena/core/portfolio_metrics.py:388:        _analyzers[model_name] = PortfolioAnalyzer(initial_capital=initial_capital)
./fincept-qt/scripts/alpha_arena/core/paper_trading_bridge.py:33:class Portfolio:
./fincept-qt/scripts/alpha_arena/core/paper_trading_bridge.py:98:class BridgePortfolioState:
./fincept-qt/scripts/alpha_arena/core/paper_trading_bridge.py:99:    """Portfolio state with calculated values (bridge-specific format)."""
./fincept-qt/scripts/alpha_arena/core/paper_trading_bridge.py:430:    def get_portfolio(self) -> Optional[Portfolio]:
./fincept-qt/scripts/alpha_arena/core/paper_trading_bridge.py:446:                return Portfolio(
./fincept-qt/scripts/alpha_arena/core/paper_trading_bridge.py:809:    def get_portfolio_state(self, prices: Dict[str, float]) -> BridgePortfolioState:
./fincept-qt/scripts/alpha_arena/core/paper_trading_bridge.py:816:            return BridgePortfolioState(
./fincept-qt/scripts/alpha_arena/core/paper_trading_bridge.py:856:        # Portfolio value = cash + positions value
./fincept-qt/scripts/alpha_arena/core/paper_trading_bridge.py:862:        return BridgePortfolioState(
./fincept-qt/scripts/alpha_arena/core/paper_trading_bridge.py:890:            logger.info(f"Portfolio {self.portfolio_id} reset to initial state")
./fincept-qt/scripts/alpha_arena/core/paper_trading_bridge.py:969:                reason="Portfolio not initialized",
./fincept-qt/scripts/alpha_arena/core/paper_trading_bridge.py:1206:                reason="Portfolio not initialized",
./fincept-qt/scripts/alpha_arena/core/research_agent.py:2:Research Agent for Alpha Arena
./fincept-qt/scripts/alpha_arena/core/research_agent.py:6:- News analysis
./fincept-qt/scripts/alpha_arena/core/research_agent.py:111:class ResearchReport:
./fincept-qt/scripts/alpha_arena/core/research_agent.py:175:class ResearchAgent(BaseAgent):
./fincept-qt/scripts/alpha_arena/core/research_agent.py:177:    Research Agent for gathering and analyzing company information.
./fincept-qt/scripts/alpha_arena/core/research_agent.py:182:    def __init__(self, name: str = "ResearchAgent"):
./fincept-qt/scripts/alpha_arena/core/research_agent.py:185:        self._cache: Dict[str, ResearchReport] = {}
./fincept-qt/scripts/alpha_arena/core/research_agent.py:210:        yield StreamResponse(content="Research agent stream not implemented", event="info")
./fincept-qt/scripts/alpha_arena/core/research_agent.py:317:    async def generate_report(self, ticker: str, use_cache: bool = True) -> ResearchReport:
./fincept-qt/scripts/alpha_arena/core/research_agent.py:326:            ResearchReport with all available data
./fincept-qt/scripts/alpha_arena/core/research_agent.py:338:        report = ResearchReport(symbol=ticker)
./fincept-qt/scripts/alpha_arena/core/research_agent.py:362:    def _generate_summary(self, report: ResearchReport) -> str:
./fincept-qt/scripts/alpha_arena/core/research_agent.py:396:_research_agent: Optional[ResearchAgent] = None
./fincept-qt/scripts/alpha_arena/core/research_agent.py:399:async def get_research_agent() -> ResearchAgent:
./fincept-qt/scripts/alpha_arena/core/research_agent.py:403:        _research_agent = ResearchAgent()
./fincept-qt/scripts/alpha_arena/core/features_pipeline.py:95:    """News and sentiment features"""
./fincept-qt/scripts/alpha_arena/core/grid_agent.py:17:    PortfolioState,
./fincept-qt/scripts/alpha_arena/core/grid_agent.py:268:        portfolio: PortfolioState,
./fincept-qt/scripts/alpha_arena/config/trading_styles.py:334:- News and developments drive value
./fincept-qt/scripts/alpha_arena/__init__.py:23:    PortfolioState,
./fincept-qt/scripts/alpha_arena/__init__.py:47:    "PortfolioState",
./fincept-qt/scripts/alpha_arena/main.py:137:        # Portfolio metrics actions
./fincept-qt/scripts/alpha_arena/main.py:151:        # Research actions
./fincept-qt/scripts/alpha_arena/main.py:780:            "real_time_portfolio_updates",  # NEW: Portfolio updates after trades
./fincept-qt/scripts/alpha_arena/main.py:924:# Portfolio Metrics Handlers
./fincept-qt/scripts/alpha_arena/main.py:930:        from alpha_arena.core.portfolio_metrics import PortfolioAnalyzer
./fincept-qt/scripts/alpha_arena/main.py:961:            analyzer = PortfolioAnalyzer(initial_capital=initial_capital)
./fincept-qt/scripts/alpha_arena/main.py:1105:# Research Handlers
./fincept-qt/scripts/canada_gov_api.py:46:            'User-Agent': 'Fincept-Terminal/1.0'
./fincept-qt/scripts/canada_gov_api.py:477:            'User-Agent': 'Fincept-Terminal/1.0'
./fincept-qt/scripts/akshare_alternative.py:4:Returns JSON output for Qt/C++ integration
./fincept-qt/scripts/fiscal_data.py:4:Returns JSON output for Qt/C++ integration
./fincept-qt/scripts/fiscal_data.py:52:            'User-Agent': 'Fincept-Terminal/1.0 (fiscaldata-api-wrapper)',
./fincept-qt/scripts/databento_provider.py:4:Institutional-grade market data fetching for Surface Analytics.
./fincept-qt/scripts/databento_provider.py:126:    Databento API wrapper for Surface Analytics.
./fincept-qt/scripts/databento_provider.py:828:        Used by the Surface Analytics control panel to populate the OPRA-venue
./fincept-qt/scripts/databento_provider.py:864:        Return per-schema available date range for a dataset. Surface Analytics
./fincept-qt/scripts/databento_provider.py:908:        in-force universe. Used by the Surface Analytics asset-search field.
./fincept-qt/scripts/databento_provider.py:1746:    # Surface Analytics — derived surface builders
./fincept-qt/scripts/databento_provider.py:3313:        # ── Surface Analytics derived commands ─────────────────────────────
./fincept-qt/scripts/crossref_data.py:22:    session.headers.update({"User-Agent": f"FinceptTerminal/4.0 (mailto:{POLITE_EMAIL})"})
./fincept-qt/scripts/bnr_data.py:83:            "User-Agent": "Fincept-Terminal/4.0.2",
./fincept-qt/scripts/news_correlation.py:2:News Correlation Engine — Signal detection, Country Instability Index,
./fincept-qt/scripts/akshare_stocks_board.py:321:    # Research
./fincept-qt/scripts/akshare_stocks_board.py:322:    "stock_institute_recommend": {"func": get_stock_institute_recommend, "desc": "Institution recommendations", "category": "Research"},
./fincept-qt/scripts/akshare_stocks_board.py:323:    "stock_institute_recommend_detail": {"func": get_stock_institute_recommend_detail, "desc": "Recommendation detail", "category": "Research"},
./fincept-qt/scripts/akshare_stocks_board.py:324:    "stock_research_report_em": {"func": get_stock_research_report_em, "desc": "Research report", "category": "Research"},
./fincept-qt/scripts/akshare_stocks_board.py:325:    "stock_jgdy_tj_em": {"func": get_stock_jgdy_tj_em, "desc": "Research statistics", "category": "Research"},
./fincept-qt/scripts/akshare_stocks_board.py:326:    "stock_jgdy_detail_em": {"func": get_stock_jgdy_detail_em, "desc": "Research detail", "category": "Research"},
./fincept-qt/scripts/openafrica_api.py:49:            'User-Agent': 'Fincept-Terminal/1.0 (openAFRICA API Wrapper)'
./fincept-qt/scripts/swiss_gov_api.py:367:            'User-Agent': 'Fincept-Terminal/1.0'
./fincept-qt/scripts/swiss_gov_api.py:896:            'User-Agent': 'Fincept-Terminal/1.0'
./fincept-qt/scripts/datagovuk_api.py:46:            'User-Agent': 'Fincept-Terminal/1.0'
./fincept-qt/scripts/datagovuk_api.py:478:            'User-Agent': 'Fincept-Terminal/1.0'
./fincept-qt/scripts/polymarket_quant_bot.py:787:        # ── Portfolio summary ──────────────────────────────────────
./fincept-qt/scripts/worldbank_data.py:5:Returns JSON output for Qt/C++ integration
./fincept-qt/scripts/overpass_api_data.py:18:session.headers.update({"User-Agent": "FinceptTerminal/4.0 (support@fincept.in)"})
./fincept-qt/scripts/equity_talipp.py:2:equity_talipp.py — TALIpp technical indicator computation for Equity Research tab
./fincept-qt/scripts/nominatim_data.py:19:    "User-Agent": "FinceptTerminal/4.0 (support@fincept.in)",
./fincept-qt/scripts/polymarket.py:31:            "User-Agent": "FinceptTerminal/4.0.2",
./fincept-qt/scripts/usda_ers_data.py:3:USDA Economic Research Service: food prices, farm income, commodity outlooks,
./fincept-qt/scripts/data_gov_hk_api.py:59:            'User-Agent': 'Fincept-Terminal/1.0',
./fincept-qt/scripts/mnb_data.py:91:            "User-Agent":   "Fincept-Terminal/4.0.2",
./fincept-qt/scripts/estat_japan_api.py:64:            'User-Agent': 'Fincept-Terminal/1.0'
./fincept-qt/scripts/universal_ckan_api.py:132:            'User-Agent': 'Fincept-Terminal/1.0',
./fincept-qt/scripts/strategies/BasicTemplateFuturesFrameworkWithExtendedMarketAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/BasicTemplateFuturesFrameworkWithExtendedMarketAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/NumeraiSignalExportDemonstrationAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/NumeraiSignalExportDemonstrationAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/NumeraiSignalExportDemonstrationAlgorithm.py:72:        targets = [PortfolioTarget(symbol, (i+1) / denominator) for i, symbol in enumerate(symbols)]
./fincept-qt/scripts/strategies/SectorWeightingFrameworkAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/SectorWeightingFrameworkAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/SectorWeightingFrameworkAlgorithm.py:34:        self.set_portfolio_construction(SectorWeightingPortfolioConstructionModel())
./fincept-qt/scripts/strategies/ConstituentsQC500GeneratorAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/ConstituentsQC500GeneratorAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/AlgorithmModeAndDeploymentTargetAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/AlgorithmModeAndDeploymentTargetAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/MeanVarianceOptimizationFrameworkAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/MeanVarianceOptimizationFrameworkAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/MeanVarianceOptimizationFrameworkAlgorithm.py:9:# Description: Mean Variance Optimization algorithm Uses the HistoricalReturnsAlphaModel and the MeanVarianceOptimizationPortfolioCo...
./fincept-qt/scripts/strategies/MeanVarianceOptimizationFrameworkAlgorithm.py:13:from Portfolio.MeanVarianceOptimizationPortfolioConstructionModel import *
./fincept-qt/scripts/strategies/MeanVarianceOptimizationFrameworkAlgorithm.py:17:### Uses the HistoricalReturnsAlphaModel and the MeanVarianceOptimizationPortfolioConstructionModel
./fincept-qt/scripts/strategies/MeanVarianceOptimizationFrameworkAlgorithm.py:42:        self.set_portfolio_construction(MeanVarianceOptimizationPortfolioConstructionModel())
./fincept-qt/scripts/strategies/BaseFrameworkRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/BaseFrameworkRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/FundamentalUniverseSelectionRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/FundamentalUniverseSelectionRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/IndexOptionShortPutOTMExpiryRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/IndexOptionShortPutOTMExpiryRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/HourSplitRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/HourSplitRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/BasicTemplateIndexDailyAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/BasicTemplateIndexDailyAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/BasicTemplateIndexDailyAlgorithm.py:46:        if not self.Portfolio.Invested:
./fincept-qt/scripts/strategies/BasicTemplateOptionsDailyAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/BasicTemplateOptionsDailyAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/ConsolidateDifferentTickTypesRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/ConsolidateDifferentTickTypesRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/UserDefinedUniverseAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/UserDefinedUniverseAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/UpdateOrderRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/UpdateOrderRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/UpdateOrderRegressionAlgorithm.py:27:        # Fincept Terminal Strategy Engine - Symbol Configuration
./fincept-qt/scripts/strategies/CustomSettlementModelRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/CustomSettlementModelRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/CustomSettlementModelRegressionAlgorithm.py:36:            raise Exception(f"It was expected to have 10101 USD in Portfolio, but was {self.portfolio.cash_book[Currencies.USD].amount}")
./fincept-qt/scripts/strategies/CustomSettlementModelRegressionAlgorithm.py:40:            raise Exception(f"It was expected to have 10000 USD in Portfolio, but was {self.portfolio.cash_book[Currencies.USD].amount}")
./fincept-qt/scripts/strategies/IndustryStandardSecurityIdentifiersRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/IndustryStandardSecurityIdentifiersRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/PytorchNeuralNetworkAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/PytorchNeuralNetworkAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/ConsolidateHourBarsIntoDailyBarsRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/ConsolidateHourBarsIntoDailyBarsRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/BasicTemplateOptionStrategyAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/BasicTemplateOptionStrategyAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/OptionChainsMultipleFullDataRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/OptionChainsMultipleFullDataRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/GetParameterRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/GetParameterRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/PandasDataFrameFromMultipleTickTypeTickHistoryRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/PandasDataFrameFromMultipleTickTypeTickHistoryRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/AddOptionContractFromUniverseRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/AddOptionContractFromUniverseRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/FuturesMomentumAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/FuturesMomentumAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/BasicTemplateLibrary.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/BasicTemplateLibrary.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/FundamentalRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/FundamentalRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/MarketOnCloseOrderBufferExtendedMarketHoursRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/MarketOnCloseOrderBufferExtendedMarketHoursRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/IndexOptionBearPutSpreadAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/IndexOptionBearPutSpreadAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/SetCustomSettlementModelRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/SetCustomSettlementModelRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/OptionPriceModelForSupportedEuropeanOptionRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/OptionPriceModelForSupportedEuropeanOptionRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/HistoryTickRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/HistoryTickRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/BasicTemplateCfdAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/BasicTemplateCfdAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/IndexOptionCallButterflyAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/IndexOptionCallButterflyAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/OptionUniverseFilterGreeksRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/OptionUniverseFilterGreeksRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/CoarseFineOptionUniverseChainRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/CoarseFineOptionUniverseChainRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/StopLimitOrderRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/StopLimitOrderRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/FutureOptionDailyRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/FutureOptionDailyRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/DropboxCoarseFineAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/DropboxCoarseFineAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/BasicTemplateFuturesWithExtendedMarketAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/BasicTemplateFuturesWithExtendedMarketAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/OptionUniverseFilterGreeksShortcutsRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/OptionUniverseFilterGreeksShortcutsRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/LongAndShortButterflyCallStrategiesAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/LongAndShortButterflyCallStrategiesAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/PearsonCorrelationPairsTradingAlphaModelFrameworkAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/PearsonCorrelationPairsTradingAlphaModelFrameworkAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/PearsonCorrelationPairsTradingAlphaModelFrameworkAlgorithm.py:43:        self.set_portfolio_construction(EqualWeightingPortfolioConstructionModel())
./fincept-qt/scripts/strategies/IndexOptionCallCalendarSpreadAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/IndexOptionCallCalendarSpreadAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/LimitIfTouchedRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/LimitIfTouchedRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/StochasticIndicatorWarmsUpProperlyRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/StochasticIndicatorWarmsUpProperlyRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/LimitFillRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/LimitFillRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/LimitFillRegressionAlgorithm.py:30:        # Fincept Terminal Strategy Engine - Symbol Configuration
./fincept-qt/scripts/strategies/ObjectStoreExampleAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/ObjectStoreExampleAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/RegressionChannelAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/RegressionChannelAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/CustomDataUniverseScheduledRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/CustomDataUniverseScheduledRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/MarketOnOpenOnCloseAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/MarketOnOpenOnCloseAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/MarketOnOpenOnCloseAlgorithm.py:26:        # Fincept Terminal Strategy Engine - Symbol Configuration
./fincept-qt/scripts/strategies/ClassicRenkoConsolidatorAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/ClassicRenkoConsolidatorAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/CorrectConsolidatedBarTypeForTickTypesAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/CorrectConsolidatedBarTypeForTickTypesAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/HistoryWithDifferentDataNormalizationModeRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/HistoryWithDifferentDataNormalizationModeRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/BasicTemplateAxosAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/BasicTemplateAxosAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/BasicTemplateFrameworkAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/BasicTemplateFrameworkAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/BasicTemplateFrameworkAlgorithm.py:33:        # Fincept Terminal Strategy Engine - Symbol Configuration
./fincept-qt/scripts/strategies/BasicTemplateFrameworkAlgorithm.py:45:        self.set_portfolio_construction(EqualWeightingPortfolioConstructionModel(Resolution.DAILY))
./fincept-qt/scripts/strategies/BasicTemplateFrameworkAlgorithm.py:47:        # self.set_portfolio_construction(EqualWeightingPortfolioConstructionModel(timedelta(2)))
./fincept-qt/scripts/strategies/BasicTemplateFrameworkAlgorithm.py:49:        # self.set_portfolio_construction(EqualWeightingPortfolioConstructionModel(Expiry.END_OF_WEEK))
./fincept-qt/scripts/strategies/QuitAfterInitializationRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/QuitAfterInitializationRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/UnregisterIndicatorRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/UnregisterIndicatorRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/IndicatorSelectorsWorkWithDifferentOptions.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/IndicatorSelectorsWorkWithDifferentOptions.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/RangeConsolidatorWithTickAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/RangeConsolidatorWithTickAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/CoarseFundamentalTop3Algorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/CoarseFundamentalTop3Algorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/PortfolioRebalanceOnDateRulesRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/PortfolioRebalanceOnDateRulesRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/PortfolioRebalanceOnDateRulesRegressionAlgorithm.py:8:# Category: Portfolio Management
./fincept-qt/scripts/strategies/PortfolioRebalanceOnDateRulesRegressionAlgorithm.py:18:class PortfolioRebalanceOnDateRulesRegressionAlgorithm(QCAlgorithm):
./fincept-qt/scripts/strategies/PortfolioRebalanceOnDateRulesRegressionAlgorithm.py:24:        # Order margin value has to have a minimum of 0.5% of Portfolio value, allows filtering out small trades and reduce fees.
./fincept-qt/scripts/strategies/PortfolioRebalanceOnDateRulesRegressionAlgorithm.py:40:        self.set_portfolio_construction(EqualWeightingPortfolioConstructionModel(self.date_rules.every(DayOfWeek.WEDNESDAY)))
./fincept-qt/scripts/strategies/BubbleAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/BubbleAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/OptionChainApisConsistencyRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/OptionChainApisConsistencyRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/FutureStopMarketOrderOnExtendedHoursRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/FutureStopMarketOrderOnExtendedHoursRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/DynamicSecurityDataRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/DynamicSecurityDataRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/BasicTemplateIndexAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/BasicTemplateIndexAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/ScheduledQueuingAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/ScheduledQueuingAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/ScheduledQueuingAlgorithm.py:26:        self.set_portfolio_construction(EqualWeightingPortfolioConstructionModel())
./fincept-qt/scripts/strategies/BasicTemplateOptionsFilterUniverseAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/BasicTemplateOptionsFilterUniverseAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/CoarseFineAsyncUniverseRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/CoarseFineAsyncUniverseRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/SelectUniverseSymbolsFromIDRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/SelectUniverseSymbolsFromIDRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/LongAndShortCallCalendarSpreadStrategiesAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/LongAndShortCallCalendarSpreadStrategiesAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/HourReverseSplitRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/HourReverseSplitRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/CustomBrokerageSideOrderHandlingRegressionPartialAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/CustomBrokerageSideOrderHandlingRegressionPartialAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/BasicTemplateFuturesWithExtendedMarketHourlyAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/BasicTemplateFuturesWithExtendedMarketHourlyAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/UniverseSelectionDefinitionsAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/UniverseSelectionDefinitionsAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/FutureOptionCallOTMExpiryRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/FutureOptionCallOTMExpiryRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/InsightScoringRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/InsightScoringRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/InsightScoringRegressionAlgorithm.py:29:        self.set_portfolio_construction(EqualWeightingPortfolioConstructionModel(Resolution.DAILY))
./fincept-qt/scripts/strategies/BasicTemplateForexAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/BasicTemplateForexAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/SecurityCustomPropertiesAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/SecurityCustomPropertiesAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/IndexOptionBuySellCallIntradayRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/IndexOptionBuySellCallIntradayRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/RangeConsolidatorAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/RangeConsolidatorAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/ShortableProviderOrdersRejectedRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/ShortableProviderOrdersRejectedRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/MaximumSectorExposureRiskManagementModelFrameworkRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/MaximumSectorExposureRiskManagementModelFrameworkRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/CapmAlphaRankingFrameworkAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/CapmAlphaRankingFrameworkAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/CapmAlphaRankingFrameworkAlgorithm.py:34:        self.set_portfolio_construction(EqualWeightingPortfolioConstructionModel())
./fincept-qt/scripts/strategies/RiskParityPortfolioAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/RiskParityPortfolioAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/RiskParityPortfolioAlgorithm.py:9:# Description: Example algorithm of using RiskParityPortfolioConstructionModel
./fincept-qt/scripts/strategies/RiskParityPortfolioAlgorithm.py:13:from Portfolio.RiskParityPortfolioConstructionModel import *
./fincept-qt/scripts/strategies/RiskParityPortfolioAlgorithm.py:15:class RiskParityPortfolioAlgorithm(QCAlgorithm):
./fincept-qt/scripts/strategies/RiskParityPortfolioAlgorithm.py:16:    '''Example algorithm of using RiskParityPortfolioConstructionModel'''
./fincept-qt/scripts/strategies/RiskParityPortfolioAlgorithm.py:28:        self.set_portfolio_construction(RiskParityPortfolioConstructionModel())
./fincept-qt/scripts/strategies/CompositeRiskManagementModelFrameworkAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/CompositeRiskManagementModelFrameworkAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/CompositeRiskManagementModelFrameworkAlgorithm.py:32:        self.set_portfolio_construction(EqualWeightingPortfolioConstructionModel())
./fincept-qt/scripts/strategies/HistoryWithDifferentDataMappingModeRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/HistoryWithDifferentDataMappingModeRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/ClassicRangeConsolidatorAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/ClassicRangeConsolidatorAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/FutureOptionShortCallITMExpiryRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/FutureOptionShortCallITMExpiryRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/live_runner.py:3:Fincept Terminal - Live Strategy Runner
./fincept-qt/scripts/strategies/PythonDictionaryFeatureRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/PythonDictionaryFeatureRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/PythonDictionaryFeatureRegressionAlgorithm.py:9:# Description: Example algorithm showing that Slice, Securities and Portfolio behave as a Python Dictionary
./fincept-qt/scripts/strategies/PythonDictionaryFeatureRegressionAlgorithm.py:15:### Example algorithm showing that Slice, Securities and Portfolio behave as a Python Dictionary
./fincept-qt/scripts/strategies/PythonDictionaryFeatureRegressionAlgorithm.py:18:    '''Example algorithm showing that Slice, Securities and Portfolio behave as a Python Dictionary'''
./fincept-qt/scripts/strategies/PythonDictionaryFeatureRegressionAlgorithm.py:83:            raise Exception('AIG (string) is not in Portfolio')
./fincept-qt/scripts/strategies/PythonDictionaryFeatureRegressionAlgorithm.py:86:            raise Exception('AIG (Symbol) is not in Portfolio')
./fincept-qt/scripts/strategies/LongAndShortButterflyPutStrategiesAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/LongAndShortButterflyPutStrategiesAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/BasicTemplateOptionEquityStrategyAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/BasicTemplateOptionEquityStrategyAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/EmaCrossUniverseSelectionFrameworkAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/EmaCrossUniverseSelectionFrameworkAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/EmaCrossUniverseSelectionFrameworkAlgorithm.py:15:from Portfolio.EqualWeightingPortfolioConstructionModel import EqualWeightingPortfolioConstructionModel
./fincept-qt/scripts/strategies/EmaCrossUniverseSelectionFrameworkAlgorithm.py:39:        self.set_portfolio_construction(EqualWeightingPortfolioConstructionModel())
./fincept-qt/scripts/strategies/LongOnlyAlphaStreamAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/LongOnlyAlphaStreamAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/LongOnlyAlphaStreamAlgorithm.py:9:# Description: Basic template framework algorithm uses framework components to define the algorithm. Shows EqualWeightingPortfolioCo...
./fincept-qt/scripts/strategies/LongOnlyAlphaStreamAlgorithm.py:14:from Portfolio.EqualWeightingPortfolioConstructionModel import EqualWeightingPortfolioConstructionModel
./fincept-qt/scripts/strategies/LongOnlyAlphaStreamAlgorithm.py:20:### Shows EqualWeightingPortfolioConstructionModel.long_only() application
./fincept-qt/scripts/strategies/LongOnlyAlphaStreamAlgorithm.py:39:        self.set_portfolio_construction(EqualWeightingPortfolioConstructionModel(Resolution.DAILY, PortfolioBias.LONG))
./fincept-qt/scripts/strategies/LongOnlyAlphaStreamAlgorithm.py:42:        # Order margin value has to have a minimum of 0.5% of Portfolio value, allows filtering out small trades and reduce fees.
./fincept-qt/scripts/strategies/AlgorithmImports.py:2:# Fincept Terminal - AlgorithmImports Shim
./fincept-qt/scripts/strategies/OptionSplitRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/OptionSplitRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/BybitCryptoRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/BybitCryptoRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/BybitCryptoRegressionAlgorithm.py:73:        self.log(f"{self.time} - TotalPortfolioValue: {self.portfolio.total_portfolio_value}")
./fincept-qt/scripts/strategies/BasicTemplateIndiaAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/BasicTemplateIndiaAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/BasicTemplateIndiaAlgorithm.py:30:        # Fincept Terminal Strategy Engine - Symbol Configuration
./fincept-qt/scripts/strategies/OptionPriceModelForUnsupportedAmericanOptionRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/OptionPriceModelForUnsupportedAmericanOptionRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/HistoryAuxiliaryDataRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/HistoryAuxiliaryDataRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/InceptionDateSelectionRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/InceptionDateSelectionRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/FutureOptionPutOTMExpiryRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/FutureOptionPutOTMExpiryRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/CustomBrokerageModelRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/CustomBrokerageModelRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/CustomDataBitcoinAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/CustomDataBitcoinAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/DividendAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/DividendAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/DividendAlgorithm.py:28:        # Fincept Terminal Strategy Engine - Symbol Configuration
./fincept-qt/scripts/strategies/NoUniverseSelectorRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/NoUniverseSelectorRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/NakedPutStrategyAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/NakedPutStrategyAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/LongAndShortStrangleStrategiesAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/LongAndShortStrangleStrategiesAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/FutureOptionPutITMExpiryRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/FutureOptionPutITMExpiryRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/FutureOptionPutITMExpiryRegressionAlgorithm.py:82:        self.log(f"{self.time} -- {order_event.symbol} :: Price: {self.securities[order_event.symbol].holdings.price} Qty: {self.securities[order_event.symbol].holdings.quantity} Direction: {order_event.direction} Msg: {order_event.message}")
./fincept-qt/scripts/strategies/FutureOptionHourlyRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/FutureOptionHourlyRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/AutoRegressiveIntegratedMovingAverageRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/AutoRegressiveIntegratedMovingAverageRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/OptionChainedUniverseSelectionModelRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/OptionChainedUniverseSelectionModelRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/LiveFeaturesAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/LiveFeaturesAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/OptionIndicatorsRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/OptionIndicatorsRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/TickDataFilteringAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/TickDataFilteringAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/OptionPriceModelForUnsupportedEuropeanOptionTimeSpanWarmupRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/OptionPriceModelForUnsupportedEuropeanOptionTimeSpanWarmupRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/IndicatorHistoryAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/IndicatorHistoryAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/SectorExposureRiskFrameworkAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/SectorExposureRiskFrameworkAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/SectorExposureRiskFrameworkAlgorithm.py:13:from Portfolio.EqualWeightingPortfolioConstructionModel import EqualWeightingPortfolioConstructionModel
./fincept-qt/scripts/strategies/SectorExposureRiskFrameworkAlgorithm.py:38:        self.set_portfolio_construction(EqualWeightingPortfolioConstructionModel())
./fincept-qt/scripts/strategies/IndicatorWarmupAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/IndicatorWarmupAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/IndicatorWarmupAlgorithm.py:29:        # Fincept Terminal Strategy Engine - Symbol Configuration
./fincept-qt/scripts/strategies/IndexOptionPutButterflyAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/IndexOptionPutButterflyAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/FutureOptionShortCallOTMExpiryRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/FutureOptionShortCallOTMExpiryRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/CustomPartialFillModelAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/CustomPartialFillModelAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/BasicTemplateOptionsHistoryAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/BasicTemplateOptionsHistoryAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/CustomDataLinkedIconicTypeAddDataCoarseSelectionRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/CustomDataLinkedIconicTypeAddDataCoarseSelectionRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/ETFGlobalRotationAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/ETFGlobalRotationAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/BlackLittermanPortfolioOptimizationFrameworkAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/BlackLittermanPortfolioOptimizationFrameworkAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/BlackLittermanPortfolioOptimizationFrameworkAlgorithm.py:8:# Category: Portfolio Management
./fincept-qt/scripts/strategies/BlackLittermanPortfolioOptimizationFrameworkAlgorithm.py:9:# Description: Black-Litterman framework algorithm Uses the HistoricalReturnsAlphaModel and the BlackLittermanPortfolioConstructionM...
./fincept-qt/scripts/strategies/BlackLittermanPortfolioOptimizationFrameworkAlgorithm.py:15:from Portfolio.BlackLittermanOptimizationPortfolioConstructionModel import *
./fincept-qt/scripts/strategies/BlackLittermanPortfolioOptimizationFrameworkAlgorithm.py:16:from Portfolio.UnconstrainedMeanVariancePortfolioOptimizer import UnconstrainedMeanVariancePortfolioOptimizer
./fincept-qt/scripts/strategies/BlackLittermanPortfolioOptimizationFrameworkAlgorithm.py:21:### Uses the HistoricalReturnsAlphaModel and the BlackLittermanPortfolioConstructionModel
./fincept-qt/scripts/strategies/BlackLittermanPortfolioOptimizationFrameworkAlgorithm.py:27:class BlackLittermanPortfolioOptimizationFrameworkAlgorithm(QCAlgorithm):
./fincept-qt/scripts/strategies/BlackLittermanPortfolioOptimizationFrameworkAlgorithm.py:35:        # Order margin value has to have a minimum of 0.5% of Portfolio value, allows filtering out small trades and reduce fees.
./fincept-qt/scripts/strategies/BlackLittermanPortfolioOptimizationFrameworkAlgorithm.py:45:        optimizer = UnconstrainedMeanVariancePortfolioOptimizer()
./fincept-qt/scripts/strategies/BlackLittermanPortfolioOptimizationFrameworkAlgorithm.py:50:        self.set_portfolio_construction(BlackLittermanOptimizationPortfolioConstructionModel(optimizer = optimizer))
./fincept-qt/scripts/strategies/MarginCallEventsAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/MarginCallEventsAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/OptionOpenInterestRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/OptionOpenInterestRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/BasicTemplateFuturesWithExtendedMarketDailyAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/BasicTemplateFuturesWithExtendedMarketDailyAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/BybitCustomDataCryptoRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/BybitCustomDataCryptoRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/BasicTemplateFuturesAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/BasicTemplateFuturesAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/CustomDataIndicatorExtensionsAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/CustomDataIndicatorExtensionsAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/TiingoPriceAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/TiingoPriceAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/SetEquityDataNormalizationModeOnAddEquity.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/SetEquityDataNormalizationModeOnAddEquity.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/FutureOptionCallITMExpiryRegressionAlgorithm.py:2:# Fincept Terminal - Strategy Engine
./fincept-qt/scripts/strategies/FutureOptionCallITMExpiryRegressionAlgorithm.py:5:# https://github.com/Fincept-Corporation/FinceptTerminal
./fincept-qt/scripts/strategies/FutureOptionCallITMExpiryRegressionAlgorithm.py:83:        self.log(f"{self.time} -- {order_event.symbol} :: Price: {self.securities[order_event.symbol].holdings.price} Qty: {self.securities[order_event.symbol].holdings.quantity} Direction: {order_event.direction} Msg: {order_event.message}")
```

## 9. Python / Quant / AI / Data Connector 关键词扫描

```text
./funding.json:18:      "description": "Native C++20 financial intelligence terminal built with Dear ImGui and embedded Python. Features full multi-asset analytics across equity, portfolio, derivatives, fixed income, and alternatives, 20+ AI investor personas, 100+ data connectors, visual workflow automation, maritime tracking, and geopolitical intelligence frameworks. A professional alternative to Bloomberg Terminal, built for analysts who refuse to be limited by traditional software.",
./funding.json:33:        "portfolio-management",
./funding.json:80:        "description": "Grants to fund specific development initiatives: advanced AI agents, additional data connectors, mobile applications, institutional features, and infrastructure scaling.",
./LICENSE:59:Fincept's APIs, data sources, or service endpoints does NOT sever or
./docs/CODE_OF_CONDUCT.md:47:- Responsible market data handling
./docs/CODE_OF_CONDUCT.md:62:- Verify data source accuracy
./docs/COMMERCIAL_LICENSE.md:13:> A separate, paid Commercial License executed with Fincept Corporation is required for any Commercial Use, including **internal use within any for-profit organization**, even where Fincept's data sources, APIs, or service endpoints have been removed, replaced, or rewired.
./docs/COMMERCIAL_LICENSE.md:38:- **"Software"** means the source code, object code, binaries, scripts (including all Python scripts in the `scripts/` tree), configuration, documentation, assets, build artifacts, container images, virtual-machine images, model weights and parameters trained or fine-tuned using the Software, datasets, embeddings, feature stores, and any output materially derived from the foregoing, contained in or produced by the Fincept Terminal repository at https://github.com/Fincept-Corporation/FinceptTerminal, in any branch, tag, release, fork, mirror, or commit, in whole or in part. Each script, module, file, broker integration, screen, MCP tool, agent framework, and Python wrapper is severable for purposes of demonstrating use, but **not severable for purposes of escaping this License**. Use of any one component constitutes use of the Software. No portion of the Software qualifies as a "System Library," "Standard Interface," or "Major Component" within the meaning of any open-source license definition.
./docs/COMMERCIAL_LICENSE.md:40:- **"Modified Version"** means any version of the Software that has been altered, including by the addition, removal, replacement, rewiring, disabling, substitution, translation, porting, or refactoring of any module, file, function, screen, API, data integration, service endpoint, or analytical algorithm.
./docs/COMMERCIAL_LICENSE.md:42:- **"Derivative Work"** means any software, work product, or system, in source or object form, that is based on, incorporates, links to (statically or dynamically), wraps, calls into, embeds, invokes via API, RPC, message queue, file drop, screen scrape, or any intermediation, or substantially reproduces the Software or any portion thereof. Derivative Work includes, without limitation, any version produced by: (i) compilation of the Software's source tree with or without modification; (ii) replacement, removal, disabling, or rewiring of any module, API, data integration, or service endpoint while retaining any other portion of the Software; (iii) translation, porting, or rewriting of any part of the Software into another programming language or runtime while preserving its architecture, screen layouts, workflow, sequence-structure-and-organization, MCP tool taxonomy, broker abstraction layer, agent framework hierarchy, terminal command syntax, function-code conventions, or feature set; (iv) translation of UI text, terminal commands, or function codes into another language or alphabet; (v) any work whose primary purpose, value, or functionality is materially derived from the Software; or (vi) any system that consumes, accesses, or operates upon the output, datasets, embeddings, model weights, or feature stores produced by the Software. The use of any portion of the Software comprising more than fifty (50) lines of source code, any single source file, any named function or class, any data schema, or any analytical algorithm or workflow expressed in the Software constitutes a Derivative Work; these thresholds are illustrative minima and not safe harbors. The number of intermediate hops, wrappers, gateways, proxies, or microservices between a user and the Software is irrelevant. Substantial similarity in non-literal elements is presumed to be a Derivative Work, with the burden on the alleged infringer to rebut by clear and convincing evidence.
./docs/COMMERCIAL_LICENSE.md:54:  (e) Use of any Modified Version, including any version in which Fincept-provided data sources, APIs, integrations, or service endpoints have been removed, replaced, rewired, or substituted with Licensee's or any third party's data sources, APIs, integrations, or service endpoints;
./docs/COMMERCIAL_LICENSE.md:66:  **The substitution of data sources or APIs does not, in any circumstance, convert Commercial Use into non-Commercial Use.** **The personal-use exemption is narrowly construed and applies only to a natural person using personally owned hardware for purposes wholly unrelated to any business, employment, or revenue-generating activity.**
./docs/COMMERCIAL_LICENSE.md:86:- Forks that strip out, replace, disable, or rewire Fincept APIs, data sources, or service endpoints, when used for Commercial Use
./docs/COMMERCIAL_LICENSE.md:116:**Comparative Advertising.** Any use of the Fincept Marks or Fincept Trade Dress in marketing, sales materials, demos, RFP responses, screenshots, or product comparisons by a for-profit competitor or its agents constitutes commercial use of the Marks and is prohibited absent express written permission, irrespective of any nominative-fair-use or comparative-advertising defense.
./docs/COMMERCIAL_LICENSE.md:151:**Privacy and Trade-Secret Limitations.** Where applicable data-protection law (including the EU General Data Protection Regulation, the Digital Personal Data Protection Act, 2023 (India), or analogous statutes) restricts disclosure of personal data, Licensor shall accept anonymized or pseudonymized data sufficient to verify compliance, comprising at minimum: (i) total user count, (ii) total deployment count, (iii) entity legal name, and (iv) hashed code-base fingerprints. Licensee bears the cost of any data-protection compliance for audit response. Where Licensee asserts trade-secret protection over its source code, Licensor will accept code review by an escrow agent operating under attorney-client privilege, with results delivered as compliance status only. Confidentiality obligations to third parties (NDAs with Licensee's clients) shall not impair Licensor's audit rights; Licensee shall use commercially reasonable efforts to obtain any necessary client consent or shall provide redacted equivalent information. Where applicable foreign blocking statute genuinely prevents disclosure, Licensee shall provide equivalent information from a permitted jurisdiction or pay liquidated damages in lieu of audit pursuant to Section 13.
./docs/COMMERCIAL_LICENSE.md:264:**Concurrent Forums (at Licensor's Election).** In addition to Delhi, Licensor may, at its sole election, bring proceedings in any forum in which Licensee is resident, incorporated, has assets, operates the Software, or directs services derived from the Software. Licensee consents in advance to non-exclusive jurisdiction in any such forum. Licensee irrevocably appoints Licensor as its agent for service of process in any jurisdiction in which Licensee operates, maintains assets, or directs services derived from the Software, where permitted by local law.
./docs/ARCHITECTURE.md:24:│  │  Screens  │  │ Services │  │  Trading │  │  MCP Integration │ │
./docs/ARCHITECTURE.md:89:│   ├── charts/ChartFactory.cpp/h   # Qt6 Charts factory
./docs/CPP_CONTRIBUTOR_GUIDE.md:43:- **MCP Integration** — Model Context Protocol for AI tools
./docs/CPP_CONTRIBUTOR_GUIDE.md:70:│   ├── charts/ChartFactory.cpp/h   # Qt6 Charts factory
./docs/CPP_CONTRIBUTOR_GUIDE.md:212:refactor: extract market data service from dashboard
./docs/GETTING_STARTED.md:21:- Integrate 100+ data sources (stocks, crypto, forex, economic data, news, etc.)
./docs/GETTING_STARTED.md:32:- **Embedded Python** — Access to vast ecosystem of financial libraries (yfinance, pandas, etc.)
./docs/GETTING_STARTED.md:116:2. **Navigate to Markets tab** — Should see market data
./docs/GETTING_STARTED.md:160:│   │   ├── agents/                 ← AI agent frameworks
./docs/GETTING_STARTED.md:202:| Add a data fetcher | `scripts/yfinance_data.py` (as template) |
./docs/GETTING_STARTED.md:218:**Add a Python Data Fetcher** — Follow the pattern in `scripts/yfinance_data.py` to create a wrapper for a new free API.
./docs/GETTING_STARTED.md:236:# Follow yfinance_data.py pattern: CLI args → JSON stdout
./docs/GETTING_STARTED.md:263:git commit -m "fix: resolve market data loading crash"
./docs/GETTING_STARTED.md:297:python scripts/yfinance_data.py quote AAPL
./docs/CONTRIBUTING.md:3:Fincept Terminal is an open-source native C++20/Qt6 financial intelligence platform with 50+ screens, embedded Python analytics, and 100+ data connectors. This guide is the canonical **how-to** for contributors — build, architecture, conventions.
./docs/CONTRIBUTING.md:29:| Python        | Analytics scripts, AI agents, data fetchers                       |
./docs/CONTRIBUTING.md:30:| Data sources  | Broker integrations, government / market data connectors          |
./docs/CONTRIBUTING.md:151:├── services/         # 18 service domains — market data, news, agents, workflow, etc.
./docs/CONTRIBUTING.md:162:├── Analytics/        # Analytics modules — equity, portfolio, derivatives,
./docs/CONTRIBUTING.md:164:├── agents/           # AI agent frameworks (finagent_core, Geopolitics, HedgeFund, …)
./docs/CONTRIBUTING.md:165:├── ai_quant_lab/     # ML, factor discovery, HFT, RL trading, vision quant
./docs/CONTRIBUTING.md:166:├── agno_trading/     # Agno-based trading agents
./docs/CONTRIBUTING.md:200:- **P2.** Lazy screen construction — use `register_factory()` for any screen that fetches data.
./docs/CONTRIBUTING.md:218:refactor/broker-http
./docs/CONTRIBUTING.md:230:Types: feat, fix, docs, refactor, test, chore, perf
./docs/CONTRIBUTING.md:249:| [Python Guide](./PYTHON_CONTRIBUTOR_GUIDE.md)           | Analytics modules, data fetchers, AI agents, PythonRunner contract |
./docs/translations/README.fr.md:31:| 📊**Analyses multi-actifs**              | Modèles DCF, optimisation de portefeuille, mesures de risque (VaR, Sharpe), tarification des produits dérivés sur actions, taux, dérivés, portefeuille et alternatifs via Python intégré                                                          |
./docs/translations/README.fr.md:32:| 🤖**AI Agents**                          | Plus de 20 personnalités d'investisseurs (Buffett, Dalio, Graham), stratégies de hedge funds, support LLM local, multi-fournisseurs (OpenAI, Anthropic, Gemini, Groq, DeepSeek, MiniMax, OpenRouter, Ollama)                                       |
./docs/translations/README.fr.md:33:| 🌐**Plus de 100 connecteurs de données** | DBnomics, Polygon, Kraken, Yahoo Finance, FRED, FMI, Banque mondiale, AkShare, API gouvernementales, ainsi que des superpositions de données alternatives facultatives telles que le sentiment du marché Adanos pour la recherche sur les actions. |
./docs/translations/README.fr.md:34:| 📈**Trading en temps réel**              | Crypto (Kraken/HyperLiquid WebSocket), actions, trading algo, moteur de trading papier                                                                                                                                                             |
./docs/translations/README.fr.md:35:| 🔬**QuantLib Suite**                     | 18 modules d'analyse quantitative — tarification, risque, stochastique, volatilité, titres à revenu fixe                                                                                                                                           |
./docs/translations/README.fr.md:37:| 🎨**Flux de travail visuels**            | Éditeur de nœuds pour les pipelines d'automatisation, intégration de l'outil MCP                                                                                                                                                                   |
./docs/translations/README.fr.md:194:-   **Plus de 100 connecteurs de données**— de Yahoo Finance aux bases de données gouvernementales
./docs/translations/README.fr.md:203:| **T1 2026** | Streaming en temps réel, backtesting avancé, intégrations de courtiers                       |
./docs/translations/README.fr.md:204:| **Q2 2026** | Constructeur de stratégie d'options, gestion multi-portefeuilles, plus de 50 agents IA       |
./docs/translations/README.fr.md:214:**Contribuer:**Nouveaux connecteurs de données, agents IA, modules d'analyse, écrans C++, documentation
./docs/translations/README.es.md:31:| 📊**Análisis multiactivo**           | Modelos DCF, optimización de cartera, métricas de riesgo (VaR, Sharpe), valoración de derivados en renta variable, renta fija, derivados, cartera y alternativos a través de Python integrado                                              |
./docs/translations/README.es.md:32:| 🤖**Agentes de IA**                  | Más de 20 personas de inversores (Buffett, Dalio, Graham), estrategias de fondos de cobertura, soporte de LLM local, múltiples proveedores (OpenAI, Anthropic, Gemini, Groq, DeepSeek, MiniMax, OpenRouter, Ollama)                        |
./docs/translations/README.es.md:33:| 🌐**Más de 100 conectores de datos** | DBnomics, Polygon, Kraken, Yahoo Finance, FRED, FMI, Banco Mundial, AkShare, API gubernamentales, además de superposiciones de datos alternativos opcionales, como el sentimiento del mercado de Adanos para la investigación de acciones. |
./docs/translations/README.es.md:34:| 📈**Comercio en tiempo real**        | Cripto (Kraken/HyperLiquid WebSocket), acciones, comercio algorítmico, motor de comercio de papel                                                                                                                                          |
./docs/translations/README.es.md:35:| 🔬**Suite QuantLib**                 | 18 módulos de análisis cuantitativo: fijación de precios, riesgo, estocástico, volatilidad, renta fija                                                                                                                                     |
./docs/translations/README.es.md:37:| 🎨**Flujos de trabajo visuales**     | Editor de nodos para canales de automatización, integración de herramientas MCP                                                                                                                                                            |
./docs/translations/README.es.md:38:| 🧠**Laboratorio cuantitativo de IA** | Modelos de aprendizaje automático, descubrimiento de factores, HFT, comercio de aprendizaje por refuerzo                                                                                                                                   |
./docs/translations/README.es.md:129:-   **Más de 100 conectores de datos**— desde Yahoo Finance hasta las bases de datos gubernamentales
./docs/translations/README.es.md:138:| **Primer trimestre de 2026** | Transmisión en tiempo real, backtesting avanzado, integraciones de corredores                                    |
./docs/translations/README.es.md:139:| **vómitos 2026**             | Creador de estrategias de opciones, gestión de carteras múltiples, más de 50 agentes de IA                       |
./docs/translations/README.es.md:149:**Contribuir:**Nuevos conectores de datos, agentes de IA, módulos de análisis, pantallas C++, documentación
./docs/translations/README.de.md:31:| 📊**Multi-Asset-Analyse**      | DCF-Modelle, Portfoliooptimierung, Risikometriken (VaR, Sharpe), Derivatpreisgestaltung über Aktien, Anleihen, Derivate, Portfolio und Alternativen via eingebettetes Python                          |
./docs/translations/README.de.md:32:| 🤖**KI-Agenten**               | Über 20 Investorenpersönlichkeiten (Buffett, Dalio, Graham), Hedgefonds-Strategien, lokale LLM-Unterstützung, Multi-Provider (OpenAI, Anthropic, Gemini, Groq, DeepSeek, MiniMax, OpenRouter, Ollama) |
./docs/translations/README.de.md:33:| 🌐**Über 100 Datenanschlüsse** | DBnomics, Polygon, Kraken, Yahoo Finance, FRED, IWF, Weltbank, AkShare, Regierungs-APIs sowie optionale alternative Daten-Overlays wie Adanos-Marktstimmung für Aktienanalysen                        |
./docs/translations/README.de.md:34:| 📈**Echtzeithandel**           | Krypto (Kraken/HyperLiquid WebSocket), Aktien, Algo-Handel, Papierhandelsmaschine                                                                                                                     |
./docs/translations/README.de.md:35:| 🔬**QuantLib Suite**           | 18 quantitative Analysemodule – Preisgestaltung, Risiko, Stochastik, Volatilität, festverzinsliche Wertpapiere                                                                                        |
./docs/translations/README.de.md:37:| 🎨**Visuelle Arbeitsabläufe**  | Knoteneditor für Automatisierungspipelines, MCP-Tool-Integration                                                                                                                                      |
./docs/translations/README.de.md:129:-   **Über 100 Datenanschlüsse**– von Yahoo Finance bis hin zu Regierungsdatenbanken
./docs/translations/README.ja.md:31:| 📊**マルチアセット分析**    | DCF モデル、ポートフォリオの最適化、リスク指標 (VaR、Sharpe)、株式・債券・デリバティブ・ポートフォリオ・オルタナティブ全般のデリバティブ価格設定を組み込み Python により提供                                       |
./docs/translations/README.ja.md:32:| 🤖**AIエージェント**      | 20 人以上の投資家ペルソナ (バフェット、ダリオ、グラハム)、ヘッジファンド戦略、ローカル LLM サポート、マルチプロバイダー (OpenAI、Anthropic、Gemini、Groq、DeepSeek、MiniMax、OpenRouter、Ollama) |
./docs/translations/README.ja.md:33:| 🌐**100以上のデータコネクタ** | DBnomics、Polygon、Kraken、Yahoo Finance、FRED、IMF、世界銀行、AkShare、政府 API、さらに株式調査のための Adanos 市場センチメントなどのオプションの代替データ オーバーレイ                 |
./docs/translations/README.ja.md:34:| 📈**リアルタイム取引**      | 暗号 (Kraken/HyperLiquid WebSocket)、株式、アルゴ取引、ペーパー取引エンジン                                                                               |
./docs/translations/README.ja.md:37:| 🎨**ビジュアルワークフロー**   | 自動化パイプライン用のノードエディター、MCPツール統合                                                                                                        |
./docs/translations/README.ja.md:180:-   **100以上のデータコネクタ**— Yahoo Financeから政府データベースまで
./docs/translations/README.zh-CN.md:31:| 📊**多资产分析**      | DCF 模型、投资组合优化、风险指标（VaR、夏普）、跨股票、固定收益、衍生品、投资组合及另类投资的衍生品定价，通过嵌入式 Python 实现                                       |
./docs/translations/README.zh-CN.md:32:| 🤖**人工智能代理**      | 20 多个投资者角色（巴菲特、戴利奥、格雷厄姆）、对冲基金策略、本地法学硕士支持、多提供商（OpenAI、Anthropic、Gemini、Groq、DeepSeek、MiniMax、OpenRouter、Ollama） |
./docs/translations/README.zh-CN.md:33:| 🌐**100 多个数据连接器** | DBnomics、Polygon、Kraken、雅虎财经、FRED、IMF、世界银行、AkShare、政府 API，以及可选的替代数据叠加，例如用于股票研究的 Adanos 市场情绪                    |
./docs/translations/README.zh-CN.md:34:| 📈**实时交易**        | 加密货币（Kraken/HyperLiquid WebSocket）、股权、算法交易、纸质交易引擎                                                              |
./docs/translations/README.zh-CN.md:37:| 🎨**可视化工作流程**     | 用于自动化管道、MCP 工具集成的节点编辑器                                                                                         |
./docs/translations/README.ko.md:31:| 📊**멀티 자산 분석**        | DCF 모델, 포트폴리오 최적화, 위험 지표(VaR, Sharpe), 주식·채권·파생상품·포트폴리오·대체투자 전반의 파생 상품 가격을 내장된 Python을 통해 제공                                                  |
./docs/translations/README.ko.md:32:| 🤖**AI 에이전트**          | 20명 이상의 투자자 페르소나(Buffett, Dalio, Graham), 헤지 펀드 전략, 현지 LLM 지원, 다중 제공자(OpenAI, Anthropic, Gemini, Groq, DeepSeek, MiniMax, OpenRouter, Ollama) |
./docs/translations/README.ko.md:33:| 🌐**100개 이상의 데이터 커넥터** | DBnomics, Polygon, Kraken, Yahoo Finance, FRED, IMF, World Bank, AkShare, 정부 API 및 주식 조사를 위한 Adanos 시장 심리와 같은 선택적 대체 데이터 오버레이                 |
./docs/translations/README.ko.md:34:| 📈**실시간 거래**           | 암호화폐(Kraken/HyperLiquid WebSocket), 주식, 알고 트레이딩, 종이 트레이딩 엔진                                                                                   |
./docs/translations/README.ko.md:35:| 🔬**QuantLib 스위트**     | 18개의 정량 분석 ​​모듈 — 가격 책정, 리스크, 확률론적, 변동성, 채권                                                                                                   |
./docs/translations/README.ko.md:37:| 🎨**시각적 워크플로**         | 자동화 파이프라인을 위한 노드 편집기, MCP 도구 통합                                                                                                               |
./docs/translations/README.ko.md:180:-   **100개 이상의 데이터 커넥터**— Yahoo Finance에서 정부 데이터베이스까지
./docs/PYTHON_CONTRIBUTOR_GUIDE.md:12:- **34 Analytics modules** — Financial calculations, portfolio optimization, ML models
./docs/PYTHON_CONTRIBUTOR_GUIDE.md:13:- **80+ Data fetchers** — APIs for market data, economics, government sources
./docs/PYTHON_CONTRIBUTOR_GUIDE.md:31:│   ├── portfolioManagement/           # Portfolio optimization
./docs/PYTHON_CONTRIBUTOR_GUIDE.md:38:│   ├── backtesting/                   # Strategy backtesting
./docs/PYTHON_CONTRIBUTOR_GUIDE.md:42:│   ├── pyportfolioopt_wrapper/        # Portfolio optimization
./docs/PYTHON_CONTRIBUTOR_GUIDE.md:44:│   ├── skfolio_wrapper.py             # Scikit-portfolio
./docs/PYTHON_CONTRIBUTOR_GUIDE.md:45:│   ├── riskfoliolib_wrapper.py        # Risk-folio lib
./docs/PYTHON_CONTRIBUTOR_GUIDE.md:53:├── agents/                            # AI agents
./docs/PYTHON_CONTRIBUTOR_GUIDE.md:55:│   ├── finagent_core/                 # Core agent framework
./docs/PYTHON_CONTRIBUTOR_GUIDE.md:58:├── agno_trading/                      # Trading agents
./docs/PYTHON_CONTRIBUTOR_GUIDE.md:63:├── yfinance_data.py                   # Yahoo Finance
./docs/PYTHON_CONTRIBUTOR_GUIDE.md:65:├── imf_data.py                        # IMF data
./docs/PYTHON_CONTRIBUTOR_GUIDE.md:66:├── worldbank_data.py                  # World Bank
./docs/PYTHON_CONTRIBUTOR_GUIDE.md:74:├── databento_provider.py              # Databento market data
./docs/PYTHON_CONTRIBUTOR_GUIDE.md:76:├── akshare_*.py                       # 20+ Chinese market scripts
./docs/PYTHON_CONTRIBUTOR_GUIDE.md:105:python Analytics/portfolioManagement/optimize.py '{"symbols":["AAPL","MSFT"]}'
./docs/PYTHON_CONTRIBUTOR_GUIDE.md:180:python yfinance_data.py quote AAPL
./docs/PYTHON_CONTRIBUTOR_GUIDE.md:195:| `yfinance` | Yahoo Finance API |
./docs/PYTHON_CONTRIBUTOR_GUIDE.md:196:| `akshare` | Chinese market data |
./docs/PYTHON_CONTRIBUTOR_GUIDE.md:197:| `pyportfolioopt` | Portfolio optimization |
./docs/PYTHON_CONTRIBUTOR_GUIDE.md:202:| `langchain` | LLM integration |
./README.md:52:| 📊 **Multi-Asset Analytics** | DCF models, portfolio optimization, risk metrics (VaR, Sharpe), derivatives pricing across equity, fixed income, derivatives, portfolio, and alternatives via embedded Python |
./README.md:53:| 🤖 **AI Agents** | 37 agents across Trader/Investor (Buffett, Graham, Lynch, Munger, Klarman, Marks…), Economic, and Geopolitics frameworks; local LLM support; multi-provider (OpenAI, Anthropic, Gemini, Groq, DeepSeek, MiniMax, OpenRouter, Ollama) |
./README.md:54:| 🌐 **100+ Data Connectors** | DBnomics, Polygon, Kraken, Yahoo Finance, FRED, IMF, World Bank, AkShare, government APIs, plus optional alternative-data overlays such as Adanos market sentiment for equity research |
./README.md:55:| 📈 **Real-Time Trading** | Crypto (Kraken/HyperLiquid WebSocket), equity, algo trading, paper trading engine, 16 broker integrations (Zerodha, Angel One, Upstox, Fyers, Dhan, Groww, Kotak, IIFL, 5paisa, AliceBlue, Shoonya, Motilal, IBKR, Alpaca, Tradier, Saxo) |
./README.md:56:| 🔬 **QuantLib Suite** | 18 quantitative analysis modules — pricing, risk, stochastic, volatility, fixed income |
./README.md:58:| 🎨 **Visual Workflows** | Node editor for automation pipelines, MCP tool integration |
./README.md:59:| 🧠 **AI Quant Lab** | ML models, factor discovery, HFT, reinforcement learning trading |
./README.md:208:- **Full buy-side analyst toolkit** — equity, portfolio, derivatives, fixed income, corporate finance, alternatives
./README.md:209:- **100+ data connectors** — from Yahoo Finance to government databases
./README.md:219:| **Q2 2026** | Options strategy builder, multi-portfolio management, 50+ AI agents |
./README.md:229:**Contribute:** New data connectors, AI agents, analytics modules, C++ screens, documentation
./README.md:270:- Equity, portfolio, derivatives, fixed income, and economics analytics built-in
./README.md:281:> A paid Commercial License is required for **any** business or internal company use — including forks that remove or replace Fincept's APIs with your own data sources. See **[Commercial License](https://github.com/Fincept-Corporation/FinceptTerminal/blob/main/docs/COMMERCIAL_LICENSE.md)** for binding terms.
./.gitignore:62:agents.md
./.gitignore:124:# ── Duplicate nested agents folder ───────────────────────────
./.gitignore:125:fincept-qt/scripts/agents/agents/
./.gitignore:141:# ── Editor/refactor backups ───────────────────────────────────
./.github/labels.json:7:  { "name": "spam",                 "color": "b60205", "description": "Obvious farming / LLM-slop PRs. Closed manually." },
./.github/MAINTAINERS.md:43:- **1 substantive feature** reviewed and accepted (new screen, new broker integration, new data source, major refactor).
./.github/CONTRIBUTING.md:59:The PR description must explain the user-visible effect and the reasoning. "Small improvements" / "fix bug" / "update code" / "minor refactor" are not acceptable descriptions — the PR will be closed.
./.github/CONTRIBUTING.md:86:- **1 substantive feature** contribution reviewed and accepted (new screen, new broker integration, new data source, major refactor).
./.github/PULL_REQUEST_TEMPLATE/pull_request_for_terminal.md:29:- [ ] Refactoring (with linked issue)
./fincept-qt/packaging/linux/fincept-terminal.appdata.xml:11:      featuring real-time market data, AI-powered analytics, multi-broker trading,
./fincept-qt/packaging/linux/fincept-terminal.appdata.xml:12:      portfolio management, and 1300+ Python analytics scripts.
./fincept-qt/packaging/linux/fincept-terminal.appdata.xml:15:      <li>Real-time crypto and equity trading (Kraken, HyperLiquid, 18+ brokers)</li>
./fincept-qt/packaging/linux/fincept-terminal.appdata.xml:16:      <li>AI chat with multiple LLM providers (OpenAI, Anthropic, Groq, Ollama)</li>
./fincept-qt/packaging/linux/fincept-terminal.appdata.xml:19:      <li>Visual workflow node editor with risk management</li>
./fincept-qt/packaging/linux/fincept-terminal.desktop:6:Comment=Professional financial data terminal with AI analytics, trading, and market data
./fincept-qt/packaging/linux/fincept-terminal.desktop:14:Keywords=finance;trading;stocks;crypto;portfolio;AI;analytics;markets;
./fincept-qt/packaging/installer/packages/com.fincept.terminal.core/meta/license.txt:27:   - Free to use with your own data sources
./fincept-qt/packaging/installer/packages/com.fincept.terminal.core/meta/license.txt:118:- Use with your own data sources (non-commercial)
./fincept-qt/packaging/installer/packages/com.fincept.terminal.core/meta/installscript.qs:97:            "Keywords=finance;trading;stocks;crypto;portfolio;AI;analytics;markets;\n"
./fincept-qt/packaging/installer/packages/com.fincept.terminal.core/meta/installscript.qs:121:        "  - Databases (chat history, portfolio, watchlists)\n" +
./fincept-qt/CMakeLists.txt:651:    # Workspace persistence (Phase 2 — multi-window refactor)
./fincept-qt/CMakeLists.txt:660:    src/storage/sqlite/migrations/v003_data_mcp_agents.cpp
./fincept-qt/CMakeLists.txt:663:    src/storage/sqlite/migrations/v006_portfolio_multi.cpp
./fincept-qt/CMakeLists.txt:675:    # Workspace persistence (multi-window refactor Phase 2/4/10)
./fincept-qt/CMakeLists.txt:708:    # LLM Profiles — multi-provider support
./fincept-qt/CMakeLists.txt:720:    # LLM tools toggle
./fincept-qt/CMakeLists.txt:752:# MCP — Model Context Protocol system
./fincept-qt/CMakeLists.txt:753:set(MCP_SOURCES
./fincept-qt/CMakeLists.txt:806:    # Native Kraken WebSocket v2 client
./fincept-qt/CMakeLists.txt:807:    src/trading/exchanges/kraken/KrakenSymbolMapper.cpp
./fincept-qt/CMakeLists.txt:808:    src/trading/exchanges/kraken/KrakenBook.cpp
./fincept-qt/CMakeLists.txt:809:    src/trading/exchanges/kraken/KrakenWsClient.cpp
./fincept-qt/CMakeLists.txt:845:    src/services/akshare/AkShareService.cpp
./fincept-qt/CMakeLists.txt:868:    src/services/backtesting/BacktestingService.cpp
./fincept-qt/CMakeLists.txt:870:    src/services/portfolio/PortfolioService.cpp
./fincept-qt/CMakeLists.txt:871:    src/services/portfolio/PortfolioAnalyticsService.cpp
./fincept-qt/CMakeLists.txt:872:    src/services/quantlib/QuantLibClient.cpp
./fincept-qt/CMakeLists.txt:874:    src/services/agents/AgentService.cpp
./fincept-qt/CMakeLists.txt:1156:    src/screens/data_sources/connectors/RelationalDatabases.cpp
./fincept-qt/CMakeLists.txt:1157:    src/screens/data_sources/connectors/NoSqlDatabases.cpp
./fincept-qt/CMakeLists.txt:1158:    src/screens/data_sources/connectors/TimeSeriesDatabases.cpp
./fincept-qt/CMakeLists.txt:1159:    src/screens/data_sources/connectors/FileSources.cpp
./fincept-qt/CMakeLists.txt:1160:    src/screens/data_sources/connectors/ApiStreaming.cpp
./fincept-qt/CMakeLists.txt:1161:    src/screens/data_sources/connectors/CloudStorage.cpp
./fincept-qt/CMakeLists.txt:1162:    src/screens/data_sources/connectors/MarketData.cpp
./fincept-qt/CMakeLists.txt:1163:    src/screens/data_sources/connectors/SearchWarehouse.cpp
./fincept-qt/CMakeLists.txt:1164:    src/screens/data_sources/connectors/AlternativeData.cpp
./fincept-qt/CMakeLists.txt:1165:    src/screens/data_sources/connectors/OpenBanking.cpp
./fincept-qt/CMakeLists.txt:1202:    src/screens/akshare/AkShareScreen.cpp
./fincept-qt/CMakeLists.txt:1233:    src/screens/backtesting/BacktestingScreen.cpp
./fincept-qt/CMakeLists.txt:1301:    # MCP Servers
./fincept-qt/CMakeLists.txt:1304:    # QuantLib Suite
./fincept-qt/CMakeLists.txt:1305:    src/screens/quantlib/QuantLibScreen.cpp
./fincept-qt/CMakeLists.txt:1323:    src/screens/portfolio/PortfolioScreen.cpp
./fincept-qt/CMakeLists.txt:1324:    src/screens/portfolio/PortfolioCommandBar.cpp
./fincept-qt/CMakeLists.txt:1325:    src/screens/portfolio/PortfolioStatsRibbon.cpp
./fincept-qt/CMakeLists.txt:1326:    src/screens/portfolio/PortfolioStatusBar.cpp
./fincept-qt/CMakeLists.txt:1327:    src/screens/portfolio/PortfolioDialogs.cpp
./fincept-qt/CMakeLists.txt:1328:    src/screens/portfolio/PortfolioHeatmap.cpp
./fincept-qt/CMakeLists.txt:1329:    src/screens/portfolio/PortfolioPerfChart.cpp
./fincept-qt/CMakeLists.txt:1330:    src/screens/portfolio/PortfolioSectorPanel.cpp
./fincept-qt/CMakeLists.txt:1331:    src/screens/portfolio/PortfolioBlotter.cpp
./fincept-qt/CMakeLists.txt:1332:    src/screens/portfolio/PortfolioTxnPanel.cpp
./fincept-qt/CMakeLists.txt:1333:    src/screens/portfolio/PortfolioSparkline.cpp
./fincept-qt/CMakeLists.txt:1334:    src/screens/portfolio/PortfolioOrderPanel.cpp
./fincept-qt/CMakeLists.txt:1335:    src/screens/portfolio/PortfolioDetailWrapper.cpp
./fincept-qt/CMakeLists.txt:1336:    src/screens/portfolio/views/AnalyticsSectorsView.cpp
./fincept-qt/CMakeLists.txt:1337:    src/screens/portfolio/views/PerformanceRiskView.cpp
./fincept-qt/CMakeLists.txt:1338:    src/screens/portfolio/views/RiskManagementView.cpp
./fincept-qt/CMakeLists.txt:1339:    src/screens/portfolio/views/PortfolioOptimizationView.cpp
./fincept-qt/CMakeLists.txt:1340:    src/screens/portfolio/views/QuantStatsView.cpp
./fincept-qt/CMakeLists.txt:1341:    src/screens/portfolio/views/ReportsView.cpp
./fincept-qt/CMakeLists.txt:1342:    src/screens/portfolio/views/CustomIndexView.cpp
./fincept-qt/CMakeLists.txt:1343:    src/screens/portfolio/views/PlanningView.cpp
./fincept-qt/CMakeLists.txt:1344:    src/screens/portfolio/views/EconomicsView.cpp
./fincept-qt/CMakeLists.txt:1345:    src/screens/portfolio/PortfolioFFNView.cpp
./fincept-qt/CMakeLists.txt:1346:    src/screens/portfolio/PortfolioInsightsPanel.cpp
./fincept-qt/CMakeLists.txt:1347:    src/screens/agent_config/AgentConfigScreen.cpp
./fincept-qt/CMakeLists.txt:1348:    src/screens/agent_config/AgentsViewPanel.cpp
./fincept-qt/CMakeLists.txt:1349:    src/screens/agent_config/SystemViewPanel.cpp
./fincept-qt/CMakeLists.txt:1350:    src/screens/agent_config/CreateAgentPanel.cpp
./fincept-qt/CMakeLists.txt:1351:    src/screens/agent_config/ToolsViewPanel.cpp
./fincept-qt/CMakeLists.txt:1352:    src/screens/agent_config/AgentChatPanel.cpp
./fincept-qt/CMakeLists.txt:1353:    src/screens/agent_config/TeamsViewPanel.cpp
./fincept-qt/CMakeLists.txt:1354:    src/screens/agent_config/WorkflowsViewPanel.cpp
./fincept-qt/CMakeLists.txt:1355:    src/screens/agent_config/PlannerViewPanel.cpp
./fincept-qt/CMakeLists.txt:1414:    src/screens/agent_config/AgentChatPanel.cpp
./fincept-qt/CMakeLists.txt:1415:    src/screens/agent_config/AgentConfigScreen.cpp
./fincept-qt/CMakeLists.txt:1416:    src/screens/agent_config/AgentsViewPanel.cpp
./fincept-qt/CMakeLists.txt:1417:    src/screens/agent_config/CreateAgentPanel.cpp
./fincept-qt/CMakeLists.txt:1418:    src/screens/agent_config/PlannerViewPanel.cpp
./fincept-qt/CMakeLists.txt:1419:    src/screens/agent_config/SystemViewPanel.cpp
./fincept-qt/CMakeLists.txt:1420:    src/screens/agent_config/TeamsViewPanel.cpp
./fincept-qt/CMakeLists.txt:1421:    src/screens/agent_config/ToolsViewPanel.cpp
./fincept-qt/CMakeLists.txt:1422:    src/screens/agent_config/WorkflowsViewPanel.cpp
./fincept-qt/CMakeLists.txt:1436:    src/screens/akshare/AkShareScreen.cpp
./fincept-qt/CMakeLists.txt:1450:    src/screens/backtesting/BacktestingScreen.cpp
./fincept-qt/CMakeLists.txt:1473:    src/screens/data_sources/connectors/RelationalDatabases.cpp
./fincept-qt/CMakeLists.txt:1474:    src/screens/data_sources/connectors/NoSqlDatabases.cpp
./fincept-qt/CMakeLists.txt:1475:    src/screens/data_sources/connectors/TimeSeriesDatabases.cpp
./fincept-qt/CMakeLists.txt:1476:    src/screens/data_sources/connectors/FileSources.cpp
./fincept-qt/CMakeLists.txt:1477:    src/screens/data_sources/connectors/ApiStreaming.cpp
./fincept-qt/CMakeLists.txt:1478:    src/screens/data_sources/connectors/CloudStorage.cpp
./fincept-qt/CMakeLists.txt:1479:    src/screens/data_sources/connectors/MarketData.cpp
./fincept-qt/CMakeLists.txt:1480:    src/screens/data_sources/connectors/SearchWarehouse.cpp
./fincept-qt/CMakeLists.txt:1481:    src/screens/data_sources/connectors/AlternativeData.cpp
./fincept-qt/CMakeLists.txt:1482:    src/screens/data_sources/connectors/OpenBanking.cpp
./fincept-qt/CMakeLists.txt:1624:    src/screens/portfolio/PortfolioInsightsPanel.cpp
./fincept-qt/CMakeLists.txt:1625:    src/screens/portfolio/PortfolioBlotter.cpp
./fincept-qt/CMakeLists.txt:1626:    src/screens/portfolio/PortfolioCommandBar.cpp
./fincept-qt/CMakeLists.txt:1627:    src/screens/portfolio/PortfolioDetailWrapper.cpp
./fincept-qt/CMakeLists.txt:1628:    src/screens/portfolio/PortfolioDialogs.cpp
./fincept-qt/CMakeLists.txt:1629:    src/screens/portfolio/PortfolioFFNView.cpp
./fincept-qt/CMakeLists.txt:1630:    src/screens/portfolio/PortfolioHeatmap.cpp
./fincept-qt/CMakeLists.txt:1631:    src/screens/portfolio/PortfolioOrderPanel.cpp
./fincept-qt/CMakeLists.txt:1632:    src/screens/portfolio/PortfolioPerfChart.cpp
./fincept-qt/CMakeLists.txt:1633:    src/screens/portfolio/PortfolioScreen.cpp
./fincept-qt/CMakeLists.txt:1634:    src/screens/portfolio/PortfolioTxnPanel.cpp
./fincept-qt/CMakeLists.txt:1635:    src/screens/portfolio/PortfolioSectorPanel.cpp
./fincept-qt/CMakeLists.txt:1636:    src/screens/portfolio/PortfolioSparkline.cpp
./fincept-qt/CMakeLists.txt:1637:    src/screens/portfolio/PortfolioStatsRibbon.cpp
./fincept-qt/CMakeLists.txt:1638:    src/screens/portfolio/PortfolioStatusBar.cpp
./fincept-qt/CMakeLists.txt:1639:    src/screens/portfolio/views/AnalyticsSectorsView.cpp
./fincept-qt/CMakeLists.txt:1640:    src/screens/portfolio/views/CustomIndexView.cpp
./fincept-qt/CMakeLists.txt:1641:    src/screens/portfolio/views/EconomicsView.cpp
./fincept-qt/CMakeLists.txt:1642:    src/screens/portfolio/views/PerformanceRiskView.cpp
./fincept-qt/CMakeLists.txt:1643:    src/screens/portfolio/views/PlanningView.cpp
./fincept-qt/CMakeLists.txt:1644:    src/screens/portfolio/views/PortfolioOptimizationView.cpp
./fincept-qt/CMakeLists.txt:1645:    src/screens/portfolio/views/QuantStatsView.cpp
./fincept-qt/CMakeLists.txt:1646:    src/screens/portfolio/views/ReportsView.cpp
./fincept-qt/CMakeLists.txt:1647:    src/screens/portfolio/views/RiskManagementView.cpp
./fincept-qt/CMakeLists.txt:1698:    src/storage/sqlite/migrations/v003_data_mcp_agents.cpp
./fincept-qt/CMakeLists.txt:1701:    src/storage/sqlite/migrations/v006_portfolio_multi.cpp
./fincept-qt/CMakeLists.txt:1762:# MCP core + tools: each defines TAG or kTimeoutMs in shared namespaces —
./fincept-qt/CMakeLists.txt:1887:    ${MCP_SOURCES}
./fincept-qt/CMakeLists.txt:2305:# that must never ship — backup folders (agents.deleted.*), test caches,
./fincept-qt/CMakeLists.txt:2625:        DESCRIPTION  "1300+ Python analytics scripts (equity, derivatives, portfolio, quant)"
./fincept-qt/cmake/prune_scripts_junk.cmake:6:#   - *.deleted.* / *.bak / *.orig  — leftover backups from refactors
./fincept-qt/DATAHUB_ARCHITECTURE.md:6:**Scope:** In-process pub/sub data layer for the entire terminal (markets, news, economics, broker streams, geopolitics, agents, WebSockets).
./fincept-qt/DATAHUB_ARCHITECTURE.md:21:**Goal:** one fetch per (symbol, source) at any moment, fanned out to every subscriber — markets, dashboard, watchlist, portfolio, AI chat, MCP tools, agents — via a single push primitive.
./fincept-qt/DATAHUB_ARCHITECTURE.md:50:econ:dbnomics:IMF/IFS/USA.PCPI_IX.Q
./fincept-qt/DATAHUB_ARCHITECTURE.md:56:agent:hedgefund:run:42
./fincept-qt/DATAHUB_ARCHITECTURE.md:66:Any `QObject` (widget, screen, service, MCP tool) that calls `DataHub::subscribe(owner, topic, slot)`.
./fincept-qt/DATAHUB_ARCHITECTURE.md:354:`ForexWidget`, and `CommoditiesWidget` (all are factory functions that
./fincept-qt/DATAHUB_ARCHITECTURE.md:396:Dashboard's `IndicesWidget`, `WatchlistWidget`, `QuoteTableWidget`, markets panel, portfolio blotter — all of them subscribing to overlapping symbols — trigger **one** `refresh()` call per hub tick. The Python process spawns once.
./fincept-qt/DATAHUB_ARCHITECTURE.md:403:// ExchangeService wraps the Kraken WebSocket
./fincept-qt/DATAHUB_ARCHITECTURE.md:420:Crypto trading screen, dashboard crypto widget, MCP `CryptoTradingTools`, agents — all subscribe to `ws:kraken:BTC-USD` and receive every tick. One WebSocket connection serves everyone.
./fincept-qt/DATAHUB_ARCHITECTURE.md:479:A dev-only screen (behind a feature flag) shows live topic table — useful for catching "why is X still fetching when nothing is visible" bugs. Also surfaced through MCP so AI chat can inspect hub state.
./fincept-qt/DATAHUB_ARCHITECTURE.md:500:3. **Request-response commands** (agent runs, LLM calls) — stay **outside** the hub. They're commands, not data. `AgentService::run(...)` and `LlmService::complete(...)` keep their existing APIs.
./fincept-qt/plans/crypto-center-wallet-connect.md:31:| D8 | Screen registration | **Lazy** (`router_->register_factory(...)`) per P2 |
./fincept-qt/plans/crypto-center-wallet-connect.md:127:- `src/app/main.cpp` — register `CryptoCenterScreen` factory; bootstrap `WalletService` singleton; register producers with hub.
./fincept-qt/plans/crypto-center-wallet-connect.md:191:- After router is built: `router_->register_factory("crypto_center", []{ return new CryptoCenterScreen(...); });`.
./fincept-qt/plans/crypto-center-wallet-connect.md:229:- Verification: nav shows item, click routes to screen, lazy factory triggers first time only.
./fincept-qt/plans/crypto-center-wallet-connect.md:292:- [ ] Screen registered with `register_factory()` (P2 enforced).
./fincept-qt/plans/crypto-center-future-phases.md:132:3. **Fee discount** — every paid feature in the terminal (deep backtest, AI report, premium screen) accepts $FNCPT at a 30 % discount. HoldingsBar lights up the chip; TRADE tab shows projected savings given current balance.
./fincept-qt/plans/crypto-center-future-phases.md:145:│ ROUTE       PumpSwap (auto)                    │  │   Deep backtests       │
./fincept-qt/plans/crypto-center-future-phases.md:252:│ GOLD      10k+ veFNCPT       all agents + arena    [achieved]               │
./fincept-qt/plans/crypto-center-future-phases.md:293:- **AI Quant Lab**: locked behind Silver+. The screen factory checks tier on `showEvent`; if insufficient, renders a "UPGRADE" pill that deep-links back to the STAKE tab.
./fincept-qt/plans/crypto-center-future-phases.md:382:- **Switchboard** — custom OOB queries (HTTP fetch from NOAA, IMF).
./fincept-qt/plans/crypto-center-future-phases.md:548:| 4 | Phase 4 (MARKETS) | Highest engineering risk; benefits most from a captive holder base. |
./fincept-qt/plans/crypto-center-future-phases.md:559:- **Auto-trading bots.** `agent:*` topics already exist for that — we don't double-build.
./fincept-qt/plans/crypto-center-future-phases.md:598:| **4** | MARKETS | `FinceptInternalAdapter` (joins `PredictionExchangeRegistry`); panel reads via Qt signals | `prediction:fincept:markets`, `prediction:fincept:orderbook:*`, `prediction:fincept:price:*` (policies registered, no producer publishing yet) | **Yes** — curated 3-market dataset emitted via `markets_ready` signal | Deploy `fincept_market` Anchor program; stand up `markets.fincept.in`; configure `fincept.markets_endpoint`, `fincept.market_program_id` |
./fincept-qt/plans/crypto-center-phase-2.md:45:| D9 | Fee-discount threshold | **1,000 $FNCPT** for **30 %** off AI reports / deep backtests / premium screens. | Same as earlier rev. Phase 3's TierService will override based on staked weight. |
./fincept-qt/plans/crypto-center-phase-2.md:286:**Goal:** Crypto Center shows **every** asset the user holds (SOL + every SPL token), with a USD price for each, a portfolio total at the top, and TRADE's swap dropdown populated from real holdings instead of a hard-coded `[SOL, $FNCPT]` pair. Today's FNCPT-only flow only worked because the user happened to be looking at a token they held; the moment someone wants to sell BONK or USDC for $FNCPT, the panel falls over.
./fincept-qt/plans/crypto-center-phase-2.md:591:2. **Jupiter rate limits.** The `tokens/v2` endpoint rate-limited me during planning. The price endpoint is fine. We refresh metadata once a day so the rate-limit risk is low; but cold-start on a fresh install needs to handle a 429 by retrying with backoff.
./fincept-qt/plans/crypto-center-phase-2.md:627:- Constants: `kThresholdRaw = 1_000 * 10^6` (1,000 $FNCPT, 6 decimals); `kDiscountPct = 30`; `kAppliedSkus = {"ai-report", "deep-backtest", "premium-screen"}`.
./fincept-qt/plans/crypto-center-phase-2.md:665:3. **PumpPortal MITM.** TLS pinning would close the residual risk; out of scope this phase, listed as Phase 2.5 polish.
./fincept-qt/resources/requirements-numpy1.txt:14:backtesting==0.6.5
./fincept-qt/resources/requirements-numpy2.txt:19:yfinance==0.2.66
./fincept-qt/resources/requirements-numpy2.txt:25:akshare>=1.14.0
./fincept-qt/resources/requirements-numpy2.txt:61:# LLM and AI
./fincept-qt/resources/requirements-numpy2.txt:113:rdagent==0.8.0
./fincept-qt/resources/requirements-numpy2.txt:114:deepagents==0.4.12
./fincept-qt/resources/requirements-numpy2.txt:118:# Polymarket uses EIP-712 signing via py_clob_client (Polygon wallet);
./fincept-qt/resources/demo_portfolio.json:3:  "portfolio_name": "Demo Portfolio",
./fincept-qt/resources/wallet/vendor/web3.js:13:/*! noble-curves - MIT License (c) 2022 Paul Miller (paulmillr.com) */const _0n$2=BigInt(0),_1n$4=BigInt(1),_2n$3=BigInt(2),_8n$1=BigInt(8);const VERIFY_DEFAULT={zip215:true};function validateOpts$1(curve){const opts=validateBasic(curve);validateObject(curve,{hash:"function",a:"bigint",d:"bigint",randomBytes:"function"},{adjustScalarBytes:"function",domain:"function",uvRatio:"function",mapToCurve:"function"});return Object.freeze({...opts})}function twistedEdwards(curveDef){const CURVE=validateOpts$1(curveDef);const{Fp:Fp,n:CURVE_ORDER,prehash:prehash,hash:cHash,randomBytes:randomBytes,nByteLength:nByteLength,h:cofactor}=CURVE;const MASK=_2n$3<<BigInt(nByteLength*8)-_1n$4;const modP=Fp.create;const Fn=Field(CURVE.n,CURVE.nBitLength);const uvRatio=CURVE.uvRatio||((u,v)=>{try{return{isValid:true,value:Fp.sqrt(u*Fp.inv(v))}}catch(e){return{isValid:false,value:_0n$2}}});const adjustScalarBytes=CURVE.adjustScalarBytes||(bytes=>bytes);const domain=CURVE.domain||((data,ctx,phflag)=>{abool("phflag",phflag);if(ctx.length||phflag)throw new Error("Contexts/pre-hash are not supported");return data});function aCoordinate(title,n){aInRange("coordinate "+title,n,_0n$2,MASK)}function assertPoint(other){if(!(other instanceof Point))throw new Error("ExtendedPoint expected")}const toAffineMemo=memoized(((p,iz)=>{const{ex:x,ey:y,ez:z}=p;const is0=p.is0();if(iz==null)iz=is0?_8n$1:Fp.inv(z);const ax=modP(x*iz);const ay=modP(y*iz);const zz=modP(z*iz);if(is0)return{x:_0n$2,y:_1n$4};if(zz!==_1n$4)throw new Error("invZ was invalid");return{x:ax,y:ay}}));const assertValidMemo=memoized((p=>{const{a:a,d:d}=CURVE;if(p.is0())throw new Error("bad point: ZERO");const{ex:X,ey:Y,ez:Z,et:T}=p;const X2=modP(X*X);const Y2=modP(Y*Y);const Z2=modP(Z*Z);const Z4=modP(Z2*Z2);const aX2=modP(X2*a);const left=modP(Z2*modP(aX2+Y2));const right=modP(Z4+modP(d*modP(X2*Y2)));if(left!==right)throw new Error("bad point: equation left != right (1)");const XY=modP(X*Y);const ZT=modP(Z*T);if(XY!==ZT)throw new Error("bad point: equation left != right (2)");return true}));class Point{constructor(ex,ey,ez,et){this.ex=ex;this.ey=ey;this.ez=ez;this.et=et;aCoordinate("x",ex);aCoordinate("y",ey);aCoordinate("z",ez);aCoordinate("t",et);Object.freeze(this)}get x(){return this.toAffine().x}get y(){return this.toAffine().y}static fromAffine(p){if(p instanceof Point)throw new Error("extended point not allowed");const{x:x,y:y}=p||{};aCoordinate("x",x);aCoordinate("y",y);return new Point(x,y,_1n$4,modP(x*y))}static normalizeZ(points){const toInv=Fp.invertBatch(points.map((p=>p.ez)));return points.map(((p,i)=>p.toAffine(toInv[i]))).map(Point.fromAffine)}static msm(points,scalars){return pippenger(Point,Fn,points,scalars)}_setWindowSize(windowSize){wnaf.setWindowSize(this,windowSize)}assertValidity(){assertValidMemo(this)}equals(other){assertPoint(other);const{ex:X1,ey:Y1,ez:Z1}=this;const{ex:X2,ey:Y2,ez:Z2}=other;const X1Z2=modP(X1*Z2);const X2Z1=modP(X2*Z1);const Y1Z2=modP(Y1*Z2);const Y2Z1=modP(Y2*Z1);return X1Z2===X2Z1&&Y1Z2===Y2Z1}is0(){return this.equals(Point.ZERO)}negate(){return new Point(modP(-this.ex),this.ey,this.ez,modP(-this.et))}double(){const{a:a}=CURVE;const{ex:X1,ey:Y1,ez:Z1}=this;const A=modP(X1*X1);const B=modP(Y1*Y1);const C=modP(_2n$3*modP(Z1*Z1));const D=modP(a*A);const x1y1=X1+Y1;const E=modP(modP(x1y1*x1y1)-A-B);const G=D+B;const F=G-C;const H=D-B;const X3=modP(E*F);const Y3=modP(G*H);const T3=modP(E*H);const Z3=modP(F*G);return new Point(X3,Y3,Z3,T3)}add(other){assertPoint(other);const{a:a,d:d}=CURVE;const{ex:X1,ey:Y1,ez:Z1,et:T1}=this;const{ex:X2,ey:Y2,ez:Z2,et:T2}=other;if(a===BigInt(-1)){const A=modP((Y1-X1)*(Y2+X2));const B=modP((Y1+X1)*(Y2-X2));const F=modP(B-A);if(F===_0n$2)return this.double();const C=modP(Z1*_2n$3*T2);const D=modP(T1*_2n$3*Z2);const E=D+C;const G=B+A;const H=D-C;const X3=modP(E*F);const Y3=modP(G*H);const T3=modP(E*H);const Z3=modP(F*G);return new Point(X3,Y3,Z3,T3)}const A=modP(X1*X2);const B=modP(Y1*Y2);const C=modP(T1*d*T2);const D=modP(Z1*Z2);const E=modP((X1+Y1)*(X2+Y2)-A-B);const F=D-C;const G=D+C;const H=modP(B-a*A);const X3=modP(E*F);const Y3=modP(G*H);const T3=modP(E*H);const Z3=modP(F*G);return new Point(X3,Y3,Z3,T3)}subtract(other){return this.add(other.negate())}wNAF(n){return wnaf.wNAFCached(this,n,Point.normalizeZ)}multiply(scalar){const n=scalar;aInRange("scalar",n,_1n$4,CURVE_ORDER);const{p:p,f:f}=this.wNAF(n);return Point.normalizeZ([p,f])[0]}multiplyUnsafe(scalar,acc=Point.ZERO){const n=scalar;aInRange("scalar",n,_0n$2,CURVE_ORDER);if(n===_0n$2)return I;if(this.is0()||n===_1n$4)return this;return wnaf.wNAFCachedUnsafe(this,n,Point.normalizeZ,acc)}isSmallOrder(){return this.multiplyUnsafe(cofactor).is0()}isTorsionFree(){return wnaf.unsafeLadder(this,CURVE_ORDER).is0()}toAffine(iz){return toAffineMemo(this,iz)}clearCofactor(){const{h:cofactor}=CURVE;if(cofactor===_1n$4)return this;return this.multiplyUnsafe(cofactor)}static fromHex(hex,zip215=false){const{d:d,a:a}=CURVE;const len=Fp.BYTES;hex=ensureBytes("pointHex",hex,len);abool("zip215",zip215);const normed=hex.slice();const lastByte=hex[len-1];normed[len-1]=lastByte&~128;const y=bytesToNumberLE(normed);const max=zip215?MASK:Fp.ORDER;aInRange("pointHex.y",y,_0n$2,max);const y2=modP(y*y);const u=modP(y2-_1n$4);const v=modP(d*y2-a);let{isValid:isValid,value:x}=uvRatio(u,v);if(!isValid)throw new Error("Point.fromHex: invalid y coordinate");const isXOdd=(x&_1n$4)===_1n$4;const isLastByteOdd=(lastByte&128)!==0;if(!zip215&&x===_0n$2&&isLastByteOdd)throw new Error("Point.fromHex: x=0 and x_0=1");if(isLastByteOdd!==isXOdd)x=modP(-x);return Point.fromAffine({x:x,y:y})}static fromPrivateKey(privKey){return getExtendedPublicKey(privKey).point}toRawBytes(){const{x:x,y:y}=this.toAffine();const bytes=numberToBytesLE(y,Fp.BYTES);bytes[bytes.length-1]|=x&_1n$4?128:0;return bytes}toHex(){return bytesToHex(this.toRawBytes())}}Point.BASE=new Point(CURVE.Gx,CURVE.Gy,_1n$4,modP(CURVE.Gx*CURVE.Gy));Point.ZERO=new Point(_0n$2,_1n$4,_1n$4,_0n$2);const{BASE:G,ZERO:I}=Point;const wnaf=wNAF(Point,nByteLength*8);function modN(a){return mod(a,CURVE_ORDER)}function modN_LE(hash){return modN(bytesToNumberLE(hash))}function getExtendedPublicKey(key){const len=Fp.BYTES;key=ensureBytes("private key",key,len);const hashed=ensureBytes("hashed private key",cHash(key),2*len);const head=adjustScalarBytes(hashed.slice(0,len));const prefix=hashed.slice(len,2*len);const scalar=modN_LE(head);const point=G.multiply(scalar);const pointBytes=point.toRawBytes();return{head:head,prefix:prefix,scalar:scalar,point:point,pointBytes:pointBytes}}function getPublicKey(privKey){return getExtendedPublicKey(privKey).pointBytes}function hashDomainToScalar(context=new Uint8Array,...msgs){const msg=concatBytes(...msgs);return modN_LE(cHash(domain(msg,ensureBytes("context",context),!!prehash)))}function sign(msg,privKey,options={}){msg=ensureBytes("message",msg);if(prehash)msg=prehash(msg);const{prefix:prefix,scalar:scalar,pointBytes:pointBytes}=getExtendedPublicKey(privKey);const r=hashDomainToScalar(options.context,prefix,msg);const R=G.multiply(r).toRawBytes();const k=hashDomainToScalar(options.context,R,pointBytes,msg);const s=modN(r+k*scalar);aInRange("signature.s",s,_0n$2,CURVE_ORDER);const res=concatBytes(R,numberToBytesLE(s,Fp.BYTES));return ensureBytes("result",res,Fp.BYTES*2)}const verifyOpts=VERIFY_DEFAULT;function verify(sig,msg,publicKey,options=verifyOpts){const{context:context,zip215:zip215}=options;const len=Fp.BYTES;sig=ensureBytes("signature",sig,2*len);msg=ensureBytes("message",msg);publicKey=ensureBytes("publicKey",publicKey,len);if(zip215!==undefined)abool("zip215",zip215);if(prehash)msg=prehash(msg);const s=bytesToNumberLE(sig.slice(len,2*len));let A,R,SB;try{A=Point.fromHex(publicKey,zip215);R=Point.fromHex(sig.slice(0,len),zip215);SB=G.multiplyUnsafe(s)}catch(error){return false}if(!zip215&&A.isSmallOrder())return false;const k=hashDomainToScalar(context,R.toRawBytes(),A.toRawBytes(),msg);const RkA=R.add(A.multiplyUnsafe(k));return RkA.subtract(SB).clearCofactor().equals(Point.ZERO)}G._setWindowSize(8);const utils={getExtendedPublicKey:getExtendedPublicKey,randomPrivateKey:()=>randomBytes(Fp.BYTES),precompute(windowSize=8,point=Point.BASE){point._setWindowSize(windowSize);point.multiply(BigInt(3));return point}};return{CURVE:CURVE,getPublicKey:getPublicKey,sign:sign,verify:verify,ExtendedPoint:Point,utils:utils}}
./fincept-qt/resources/wallet/vendor/web3.js:16:/*! noble-hashes - MIT License (c) 2022 Paul Miller (paulmillr.com) */const u32=arr=>new Uint32Array(arr.buffer,arr.byteOffset,Math.floor(arr.byteLength/4));const createView=arr=>new DataView(arr.buffer,arr.byteOffset,arr.byteLength);const rotr=(word,shift)=>word<<32-shift|word>>>shift;const isLE=(()=>new Uint8Array(new Uint32Array([287454020]).buffer)[0]===68)();const byteSwap=word=>word<<24&4278190080|word<<8&16711680|word>>>8&65280|word>>>24&255;function byteSwap32(arr){for(let i=0;i<arr.length;i++){arr[i]=byteSwap(arr[i])}}function utf8ToBytes(str){if(typeof str!=="string")throw new Error("utf8ToBytes expected string, got "+typeof str);return new Uint8Array((new TextEncoder).encode(str))}function toBytes(data){if(typeof data==="string")data=utf8ToBytes(data);abytes(data);return data}class Hash{clone(){return this._cloneInto()}}function wrapConstructor(hashCons){const hashC=msg=>hashCons().update(toBytes(msg)).digest();const tmp=hashCons();hashC.outputLen=tmp.outputLen;hashC.blockLen=tmp.blockLen;hashC.create=()=>hashCons();return hashC}function setBigUint64(view,byteOffset,value,isLE){if(typeof view.setBigUint64==="function")return view.setBigUint64(byteOffset,value,isLE);const _32n=BigInt(32);const _u32_max=BigInt(4294967295);const wh=Number(value>>_32n&_u32_max);const wl=Number(value&_u32_max);const h=isLE?4:0;const l=isLE?0:4;view.setUint32(byteOffset+h,wh,isLE);view.setUint32(byteOffset+l,wl,isLE)}const Chi=(a,b,c)=>a&b^~a&c;const Maj=(a,b,c)=>a&b^a&c^b&c;class HashMD extends Hash{constructor(blockLen,outputLen,padOffset,isLE){super();this.blockLen=blockLen;this.outputLen=outputLen;this.padOffset=padOffset;this.isLE=isLE;this.finished=false;this.length=0;this.pos=0;this.destroyed=false;this.buffer=new Uint8Array(blockLen);this.view=createView(this.buffer)}update(data){aexists(this);const{view:view,buffer:buffer,blockLen:blockLen}=this;data=toBytes(data);const len=data.length;for(let pos=0;pos<len;){const take=Math.min(blockLen-this.pos,len-pos);if(take===blockLen){const dataView=createView(data);for(;blockLen<=len-pos;pos+=blockLen)this.process(dataView,pos);continue}buffer.set(data.subarray(pos,pos+take),this.pos);this.pos+=take;pos+=take;if(this.pos===blockLen){this.process(view,0);this.pos=0}}this.length+=data.length;this.roundClean();return this}digestInto(out){aexists(this);aoutput(out,this);this.finished=true;const{buffer:buffer,view:view,blockLen:blockLen,isLE:isLE}=this;let{pos:pos}=this;buffer[pos++]=128;this.buffer.subarray(pos).fill(0);if(this.padOffset>blockLen-pos){this.process(view,0);pos=0}for(let i=pos;i<blockLen;i++)buffer[i]=0;setBigUint64(view,blockLen-8,BigInt(this.length*8),isLE);this.process(view,0);const oview=createView(out);const len=this.outputLen;if(len%4)throw new Error("_sha2: outputLen should be aligned to 32bit");const outLen=len/4;const state=this.get();if(outLen>state.length)throw new Error("_sha2: outputLen bigger than state");for(let i=0;i<outLen;i++)oview.setUint32(4*i,state[i],isLE)}digest(){const{buffer:buffer,outputLen:outputLen}=this;this.digestInto(buffer);const res=buffer.slice(0,outputLen);this.destroy();return res}_cloneInto(to){to||(to=new this.constructor);to.set(...this.get());const{blockLen:blockLen,buffer:buffer,length:length,finished:finished,destroyed:destroyed,pos:pos}=this;to.length=length;to.pos=pos;to.finished=finished;to.destroyed=destroyed;if(length%blockLen)to.buffer.set(buffer);return to}}const SHA256_K$1=new Uint32Array([1116352408,1899447441,3049323471,3921009573,961987163,1508970993,2453635748,2870763221,3624381080,310598401,607225278,1426881987,1925078388,2162078206,2614888103,3248222580,3835390401,4022224774,264347078,604807628,770255983,1249150122,1555081692,1996064986,2554220882,2821834349,2952996808,3210313671,3336571891,3584528711,113926993,338241895,666307205,773529912,1294757372,1396182291,1695183700,1986661051,2177026350,2456956037,2730485921,2820302411,3259730800,3345764771,3516065817,3600352804,4094571909,275423344,430227734,506948616,659060556,883997877,958139571,1322822218,1537002063,1747873779,1955562222,2024104815,2227730452,2361852424,2428436474,2756734187,3204031479,3329325298]);const SHA256_IV$1=new Uint32Array([1779033703,3144134277,1013904242,2773480762,1359893119,2600822924,528734635,1541459225]);const SHA256_W$1=new Uint32Array(64);let SHA256$1=class SHA256 extends HashMD{constructor(){super(64,32,8,false);this.A=SHA256_IV$1[0]|0;this.B=SHA256_IV$1[1]|0;this.C=SHA256_IV$1[2]|0;this.D=SHA256_IV$1[3]|0;this.E=SHA256_IV$1[4]|0;this.F=SHA256_IV$1[5]|0;this.G=SHA256_IV$1[6]|0;this.H=SHA256_IV$1[7]|0}get(){const{A:A,B:B,C:C,D:D,E:E,F:F,G:G,H:H}=this;return[A,B,C,D,E,F,G,H]}set(A,B,C,D,E,F,G,H){this.A=A|0;this.B=B|0;this.C=C|0;this.D=D|0;this.E=E|0;this.F=F|0;this.G=G|0;this.H=H|0}process(view,offset){for(let i=0;i<16;i++,offset+=4)SHA256_W$1[i]=view.getUint32(offset,false);for(let i=16;i<64;i++){const W15=SHA256_W$1[i-15];const W2=SHA256_W$1[i-2];const s0=rotr(W15,7)^rotr(W15,18)^W15>>>3;const s1=rotr(W2,17)^rotr(W2,19)^W2>>>10;SHA256_W$1[i]=s1+SHA256_W$1[i-7]+s0+SHA256_W$1[i-16]|0}let{A:A,B:B,C:C,D:D,E:E,F:F,G:G,H:H}=this;for(let i=0;i<64;i++){const sigma1=rotr(E,6)^rotr(E,11)^rotr(E,25);const T1=H+sigma1+Chi(E,F,G)+SHA256_K$1[i]+SHA256_W$1[i]|0;const sigma0=rotr(A,2)^rotr(A,13)^rotr(A,22);const T2=sigma0+Maj(A,B,C)|0;H=G;G=F;F=E;E=D+T1|0;D=C;C=B;B=A;A=T1+T2|0}A=A+this.A|0;B=B+this.B|0;C=C+this.C|0;D=D+this.D|0;E=E+this.E|0;F=F+this.F|0;G=G+this.G|0;H=H+this.H|0;this.set(A,B,C,D,E,F,G,H)}roundClean(){SHA256_W$1.fill(0)}destroy(){this.set(0,0,0,0,0,0,0,0);this.buffer.fill(0)}};const sha256$1=wrapConstructor((()=>new SHA256$1));var lib={};var encoding_lib={};var hasRequiredEncoding_lib;function requireEncoding_lib(){if(hasRequiredEncoding_lib)return encoding_lib;hasRequiredEncoding_lib=1;function inRange(a,min,max){return min<=a&&a<=max}function ToDictionary(o){if(o===undefined)return{};if(o===Object(o))return o;throw TypeError("Could not convert argument to dictionary")}function stringToCodePoints(string){var s=String(string);var n=s.length;var i=0;var u=[];while(i<n){var c=s.charCodeAt(i);if(c<55296||c>57343){u.push(c)}else if(56320<=c&&c<=57343){u.push(65533)}else if(55296<=c&&c<=56319){if(i===n-1){u.push(65533)}else{var d=string.charCodeAt(i+1);if(56320<=d&&d<=57343){var a=c&1023;var b=d&1023;u.push(65536+(a<<10)+b);i+=1}else{u.push(65533)}}}i+=1}return u}function codePointsToString(code_points){var s="";for(var i=0;i<code_points.length;++i){var cp=code_points[i];if(cp<=65535){s+=String.fromCharCode(cp)}else{cp-=65536;s+=String.fromCharCode((cp>>10)+55296,(cp&1023)+56320)}}return s}var end_of_stream=-1;function Stream(tokens){this.tokens=[].slice.call(tokens)}Stream.prototype={endOfStream:function(){return!this.tokens.length},read:function(){if(!this.tokens.length)return end_of_stream;return this.tokens.shift()},prepend:function(token){if(Array.isArray(token)){var tokens=token;while(tokens.length)this.tokens.unshift(tokens.pop())}else{this.tokens.unshift(token)}},push:function(token){if(Array.isArray(token)){var tokens=token;while(tokens.length)this.tokens.push(tokens.shift())}else{this.tokens.push(token)}}};var finished=-1;function decoderError(fatal,opt_code_point){if(fatal)throw TypeError("Decoder error");return opt_code_point||65533}var DEFAULT_ENCODING="utf-8";function TextDecoder(encoding,options){if(!(this instanceof TextDecoder)){return new TextDecoder(encoding,options)}encoding=encoding!==undefined?String(encoding).toLowerCase():DEFAULT_ENCODING;if(encoding!==DEFAULT_ENCODING){throw new Error("Encoding not supported. Only utf-8 is supported")}options=ToDictionary(options);this._streaming=false;this._BOMseen=false;this._decoder=null;this._fatal=Boolean(options["fatal"]);this._ignoreBOM=Boolean(options["ignoreBOM"]);Object.defineProperty(this,"encoding",{value:"utf-8"});Object.defineProperty(this,"fatal",{value:this._fatal});Object.defineProperty(this,"ignoreBOM",{value:this._ignoreBOM})}TextDecoder.prototype={decode:function decode(input,options){var bytes;if(typeof input==="object"&&input instanceof ArrayBuffer){bytes=new Uint8Array(input)}else if(typeof input==="object"&&"buffer"in input&&input.buffer instanceof ArrayBuffer){bytes=new Uint8Array(input.buffer,input.byteOffset,input.byteLength)}else{bytes=new Uint8Array(0)}options=ToDictionary(options);if(!this._streaming){this._decoder=new UTF8Decoder({fatal:this._fatal});this._BOMseen=false}this._streaming=Boolean(options["stream"]);var input_stream=new Stream(bytes);var code_points=[];var result;while(!input_stream.endOfStream()){result=this._decoder.handler(input_stream,input_stream.read());if(result===finished)break;if(result===null)continue;if(Array.isArray(result))code_points.push.apply(code_points,result);else code_points.push(result)}if(!this._streaming){do{result=this._decoder.handler(input_stream,input_stream.read());if(result===finished)break;if(result===null)continue;if(Array.isArray(result))code_points.push.apply(code_points,result);else code_points.push(result)}while(!input_stream.endOfStream());this._decoder=null}if(code_points.length){if(["utf-8"].indexOf(this.encoding)!==-1&&!this._ignoreBOM&&!this._BOMseen){if(code_points[0]===65279){this._BOMseen=true;code_points.shift()}else{this._BOMseen=true}}}return codePointsToString(code_points)}};function TextEncoder(encoding,options){if(!(this instanceof TextEncoder))return new TextEncoder(encoding,options);encoding=encoding!==undefined?String(encoding).toLowerCase():DEFAULT_ENCODING;if(encoding!==DEFAULT_ENCODING){throw new Error("Encoding not supported. Only utf-8 is supported")}options=ToDictionary(options);this._streaming=false;this._encoder=null;this._options={fatal:Boolean(options["fatal"])};Object.defineProperty(this,"encoding",{value:"utf-8"})}TextEncoder.prototype={encode:function encode(opt_string,options){opt_string=opt_string?String(opt_string):"";options=ToDictionary(options);if(!this._streaming)this._encoder=new UTF8Encoder(this._options);this._streaming=Boolean(options["stream"]);var bytes=[];var input_stream=new Stream(stringToCodePoints(opt_string));var result;while(!input_stream.endOfStream()){result=this._encoder.handler(input_stream,input_stream.read());if(result===finished)break;if(Array.isArray(result))bytes.push.apply(bytes,result);else bytes.push(result)}if(!this._streaming){while(true){result=this._encoder.handler(input_stream,input_stream.read());if(result===finished)break;if(Array.isArray(result))bytes.push.apply(bytes,result);else bytes.push(result)}this._encoder=null}return new Uint8Array(bytes)}};function UTF8Decoder(options){var fatal=options.fatal;var utf8_code_point=0,utf8_bytes_seen=0,utf8_bytes_needed=0,utf8_lower_boundary=128,utf8_upper_boundary=191;this.handler=function(stream,bite){if(bite===end_of_stream&&utf8_bytes_needed!==0){utf8_bytes_needed=0;return decoderError(fatal)}if(bite===end_of_stream)return finished;if(utf8_bytes_needed===0){if(inRange(bite,0,127)){return bite}if(inRange(bite,194,223)){utf8_bytes_needed=1;utf8_code_point=bite-192}else if(inRange(bite,224,239)){if(bite===224)utf8_lower_boundary=160;if(bite===237)utf8_upper_boundary=159;utf8_bytes_needed=2;utf8_code_point=bite-224}else if(inRange(bite,240,244)){if(bite===240)utf8_lower_boundary=144;if(bite===244)utf8_upper_boundary=143;utf8_bytes_needed=3;utf8_code_point=bite-240}else{return decoderError(fatal)}utf8_code_point=utf8_code_point<<6*utf8_bytes_needed;return null}if(!inRange(bite,utf8_lower_boundary,utf8_upper_boundary)){utf8_code_point=utf8_bytes_needed=utf8_bytes_seen=0;utf8_lower_boundary=128;utf8_upper_boundary=191;stream.prepend(bite);return decoderError(fatal)}utf8_lower_boundary=128;utf8_upper_boundary=191;utf8_bytes_seen+=1;utf8_code_point+=bite-128<<6*(utf8_bytes_needed-utf8_bytes_seen);if(utf8_bytes_seen!==utf8_bytes_needed)return null;var code_point=utf8_code_point;utf8_code_point=utf8_bytes_needed=utf8_bytes_seen=0;return code_point}}function UTF8Encoder(options){options.fatal;this.handler=function(stream,code_point){if(code_point===end_of_stream)return finished;if(inRange(code_point,0,127))return code_point;var count,offset;if(inRange(code_point,128,2047)){count=1;offset=192}else if(inRange(code_point,2048,65535)){count=2;offset=224}else if(inRange(code_point,65536,1114111)){count=3;offset=240}var bytes=[(code_point>>6*count)+offset];while(count>0){var temp=code_point>>6*(count-1);bytes.push(128|temp&63);count-=1}return bytes}}encoding_lib.TextEncoder=TextEncoder;encoding_lib.TextDecoder=TextDecoder;return encoding_lib}var hasRequiredLib;function requireLib(){if(hasRequiredLib)return lib;hasRequiredLib=1;var __createBinding=lib&&lib.__createBinding||(Object.create?function(o,m,k,k2){if(k2===undefined)k2=k;Object.defineProperty(o,k2,{enumerable:true,get:function(){return m[k]}})}:function(o,m,k,k2){if(k2===undefined)k2=k;o[k2]=m[k]});var __setModuleDefault=lib&&lib.__setModuleDefault||(Object.create?function(o,v){Object.defineProperty(o,"default",{enumerable:true,value:v})}:function(o,v){o["default"]=v});var __decorate=lib&&lib.__decorate||function(decorators,target,key,desc){var c=arguments.length,r=c<3?target:desc===null?desc=Object.getOwnPropertyDescriptor(target,key):desc,d;if(typeof Reflect==="object"&&typeof Reflect.decorate==="function")r=Reflect.decorate(decorators,target,key,desc);else for(var i=decorators.length-1;i>=0;i--)if(d=decorators[i])r=(c<3?d(r):c>3?d(target,key,r):d(target,key))||r;return c>3&&r&&Object.defineProperty(target,key,r),r};var __importStar=lib&&lib.__importStar||function(mod){if(mod&&mod.__esModule)return mod;var result={};if(mod!=null)for(var k in mod)if(k!=="default"&&Object.hasOwnProperty.call(mod,k))__createBinding(result,mod,k);__setModuleDefault(result,mod);return result};var __importDefault=lib&&lib.__importDefault||function(mod){return mod&&mod.__esModule?mod:{default:mod}};Object.defineProperty(lib,"__esModule",{value:true});lib.deserializeUnchecked=lib.deserialize=lib.serialize=lib.BinaryReader=lib.BinaryWriter=lib.BorshError=lib.baseDecode=lib.baseEncode=void 0;const bn_js_1=__importDefault(requireBn());const bs58_1=__importDefault(requireBs58());const encoding=__importStar(requireEncoding_lib());const ResolvedTextDecoder=typeof TextDecoder!=="function"?encoding.TextDecoder:TextDecoder;const textDecoder=new ResolvedTextDecoder("utf-8",{fatal:true});function baseEncode(value){if(typeof value==="string"){value=Buffer.from(value,"utf8")}return bs58_1.default.encode(Buffer.from(value))}lib.baseEncode=baseEncode;function baseDecode(value){return Buffer.from(bs58_1.default.decode(value))}lib.baseDecode=baseDecode;const INITIAL_LENGTH=1024;class BorshError extends Error{constructor(message){super(message);this.fieldPath=[];this.originalMessage=message}addToFieldPath(fieldName){this.fieldPath.splice(0,0,fieldName);this.message=this.originalMessage+": "+this.fieldPath.join(".")}}lib.BorshError=BorshError;class BinaryWriter{constructor(){this.buf=Buffer.alloc(INITIAL_LENGTH);this.length=0}maybeResize(){if(this.buf.length<16+this.length){this.buf=Buffer.concat([this.buf,Buffer.alloc(INITIAL_LENGTH)])}}writeU8(value){this.maybeResize();this.buf.writeUInt8(value,this.length);this.length+=1}writeU16(value){this.maybeResize();this.buf.writeUInt16LE(value,this.length);this.length+=2}writeU32(value){this.maybeResize();this.buf.writeUInt32LE(value,this.length);this.length+=4}writeU64(value){this.maybeResize();this.writeBuffer(Buffer.from(new bn_js_1.default(value).toArray("le",8)))}writeU128(value){this.maybeResize();this.writeBuffer(Buffer.from(new bn_js_1.default(value).toArray("le",16)))}writeU256(value){this.maybeResize();this.writeBuffer(Buffer.from(new bn_js_1.default(value).toArray("le",32)))}writeU512(value){this.maybeResize();this.writeBuffer(Buffer.from(new bn_js_1.default(value).toArray("le",64)))}writeBuffer(buffer){this.buf=Buffer.concat([Buffer.from(this.buf.subarray(0,this.length)),buffer,Buffer.alloc(INITIAL_LENGTH)]);this.length+=buffer.length}writeString(str){this.maybeResize();const b=Buffer.from(str,"utf8");this.writeU32(b.length);this.writeBuffer(b)}writeFixedArray(array){this.writeBuffer(Buffer.from(array))}writeArray(array,fn){this.maybeResize();this.writeU32(array.length);for(const elem of array){this.maybeResize();fn(elem)}}toArray(){return this.buf.subarray(0,this.length)}}lib.BinaryWriter=BinaryWriter;function handlingRangeError(target,propertyKey,propertyDescriptor){const originalMethod=propertyDescriptor.value;propertyDescriptor.value=function(...args){try{return originalMethod.apply(this,args)}catch(e){if(e instanceof RangeError){const code=e.code;if(["ERR_BUFFER_OUT_OF_BOUNDS","ERR_OUT_OF_RANGE"].indexOf(code)>=0){throw new BorshError("Reached the end of buffer when deserializing")}}throw e}}}class BinaryReader{constructor(buf){this.buf=buf;this.offset=0}readU8(){const value=this.buf.readUInt8(this.offset);this.offset+=1;return value}readU16(){const value=this.buf.readUInt16LE(this.offset);this.offset+=2;return value}readU32(){const value=this.buf.readUInt32LE(this.offset);this.offset+=4;return value}readU64(){const buf=this.readBuffer(8);return new bn_js_1.default(buf,"le")}readU128(){const buf=this.readBuffer(16);return new bn_js_1.default(buf,"le")}readU256(){const buf=this.readBuffer(32);return new bn_js_1.default(buf,"le")}readU512(){const buf=this.readBuffer(64);return new bn_js_1.default(buf,"le")}readBuffer(len){if(this.offset+len>this.buf.length){throw new BorshError(`Expected buffer length ${len} isn't within bounds`)}const result=this.buf.slice(this.offset,this.offset+len);this.offset+=len;return result}readString(){const len=this.readU32();const buf=this.readBuffer(len);try{return textDecoder.decode(buf)}catch(e){throw new BorshError(`Error decoding UTF-8 string: ${e}`)}}readFixedArray(len){return new Uint8Array(this.readBuffer(len))}readArray(fn){const len=this.readU32();const result=Array();for(let i=0;i<len;++i){result.push(fn())}return result}}__decorate([handlingRangeError],BinaryReader.prototype,"readU8",null);__decorate([handlingRangeError],BinaryReader.prototype,"readU16",null);__decorate([handlingRangeError],BinaryReader.prototype,"readU32",null);__decorate([handlingRangeError],BinaryReader.prototype,"readU64",null);__decorate([handlingRangeError],BinaryReader.prototype,"readU128",null);__decorate([handlingRangeError],BinaryReader.prototype,"readU256",null);__decorate([handlingRangeError],BinaryReader.prototype,"readU512",null);__decorate([handlingRangeError],BinaryReader.prototype,"readString",null);__decorate([handlingRangeError],BinaryReader.prototype,"readFixedArray",null);__decorate([handlingRangeError],BinaryReader.prototype,"readArray",null);lib.BinaryReader=BinaryReader;function capitalizeFirstLetter(string){return string.charAt(0).toUpperCase()+string.slice(1)}function serializeField(schema,fieldName,value,fieldType,writer){try{if(typeof fieldType==="string"){writer[`write${capitalizeFirstLetter(fieldType)}`](value)}else if(fieldType instanceof Array){if(typeof fieldType[0]==="number"){if(value.length!==fieldType[0]){throw new BorshError(`Expecting byte array of length ${fieldType[0]}, but got ${value.length} bytes`)}writer.writeFixedArray(value)}else if(fieldType.length===2&&typeof fieldType[1]==="number"){if(value.length!==fieldType[1]){throw new BorshError(`Expecting byte array of length ${fieldType[1]}, but got ${value.length} bytes`)}for(let i=0;i<fieldType[1];i++){serializeField(schema,null,value[i],fieldType[0],writer)}}else{writer.writeArray(value,(item=>{serializeField(schema,fieldName,item,fieldType[0],writer)}))}}else if(fieldType.kind!==undefined){switch(fieldType.kind){case"option":{if(value===null||value===undefined){writer.writeU8(0)}else{writer.writeU8(1);serializeField(schema,fieldName,value,fieldType.type,writer)}break}case"map":{writer.writeU32(value.size);value.forEach(((val,key)=>{serializeField(schema,fieldName,key,fieldType.key,writer);serializeField(schema,fieldName,val,fieldType.value,writer)}));break}default:throw new BorshError(`FieldType ${fieldType} unrecognized`)}}else{serializeStruct(schema,value,writer)}}catch(error){if(error instanceof BorshError){error.addToFieldPath(fieldName)}throw error}}function serializeStruct(schema,obj,writer){if(typeof obj.borshSerialize==="function"){obj.borshSerialize(writer);return}const structSchema=schema.get(obj.constructor);if(!structSchema){throw new BorshError(`Class ${obj.constructor.name} is missing in schema`)}if(structSchema.kind==="struct"){structSchema.fields.map((([fieldName,fieldType])=>{serializeField(schema,fieldName,obj[fieldName],fieldType,writer)}))}else if(structSchema.kind==="enum"){const name=obj[structSchema.field];for(let idx=0;idx<structSchema.values.length;++idx){const[fieldName,fieldType]=structSchema.values[idx];if(fieldName===name){writer.writeU8(idx);serializeField(schema,fieldName,obj[fieldName],fieldType,writer);break}}}else{throw new BorshError(`Unexpected schema kind: ${structSchema.kind} for ${obj.constructor.name}`)}}function serialize(schema,obj,Writer=BinaryWriter){const writer=new Writer;serializeStruct(schema,obj,writer);return writer.toArray()}lib.serialize=serialize;function deserializeField(schema,fieldName,fieldType,reader){try{if(typeof fieldType==="string"){return reader[`read${capitalizeFirstLetter(fieldType)}`]()}if(fieldType instanceof Array){if(typeof fieldType[0]==="number"){return reader.readFixedArray(fieldType[0])}else if(typeof fieldType[1]==="number"){const arr=[];for(let i=0;i<fieldType[1];i++){arr.push(deserializeField(schema,null,fieldType[0],reader))}return arr}else{return reader.readArray((()=>deserializeField(schema,fieldName,fieldType[0],reader)))}}if(fieldType.kind==="option"){const option=reader.readU8();if(option){return deserializeField(schema,fieldName,fieldType.type,reader)}return undefined}if(fieldType.kind==="map"){let map=new Map;const length=reader.readU32();for(let i=0;i<length;i++){const key=deserializeField(schema,fieldName,fieldType.key,reader);const val=deserializeField(schema,fieldName,fieldType.value,reader);map.set(key,val)}return map}return deserializeStruct(schema,fieldType,reader)}catch(error){if(error instanceof BorshError){error.addToFieldPath(fieldName)}throw error}}function deserializeStruct(schema,classType,reader){if(typeof classType.borshDeserialize==="function"){return classType.borshDeserialize(reader)}const structSchema=schema.get(classType);if(!structSchema){throw new BorshError(`Class ${classType.name} is missing in schema`)}if(structSchema.kind==="struct"){const result={};for(const[fieldName,fieldType]of schema.get(classType).fields){result[fieldName]=deserializeField(schema,fieldName,fieldType,reader)}return new classType(result)}if(structSchema.kind==="enum"){const idx=reader.readU8();if(idx>=structSchema.values.length){throw new BorshError(`Enum index: ${idx} is out of range`)}const[fieldName,fieldType]=structSchema.values[idx];const fieldValue=deserializeField(schema,fieldName,fieldType,reader);return new classType({[fieldName]:fieldValue})}throw new BorshError(`Unexpected schema kind: ${structSchema.kind} for ${classType.constructor.name}`)}function deserialize(schema,classType,buffer,Reader=BinaryReader){const reader=new Reader(buffer);const result=deserializeStruct(schema,classType,reader);if(reader.offset<buffer.length){throw new BorshError(`Unexpected ${buffer.length-reader.offset} bytes after deserialized data`)}return result}lib.deserialize=deserialize;function deserializeUnchecked(schema,classType,buffer,Reader=BinaryReader){const reader=new Reader(buffer);return deserializeStruct(schema,classType,reader)}lib.deserializeUnchecked=deserializeUnchecked;return lib}var libExports=requireLib();let Struct$1=class Struct{constructor(properties){Object.assign(this,properties)}encode(){return bufferExports.Buffer.from(libExports.serialize(SOLANA_SCHEMA,this))}static decode(data){return libExports.deserialize(SOLANA_SCHEMA,this,data)}static decodeUnchecked(data){return libExports.deserializeUnchecked(SOLANA_SCHEMA,this,data)}};class Enum extends Struct$1{constructor(properties){super(properties);this.enum="";if(Object.keys(properties).length!==1){throw new Error("Enum can only take single value")}Object.keys(properties).map((key=>{this.enum=key}))}}const SOLANA_SCHEMA=new Map;var _PublicKey;const MAX_SEED_LENGTH=32;const PUBLIC_KEY_LENGTH=32;function isPublicKeyData(value){return value._bn!==undefined}let uniquePublicKeyCounter=1;class PublicKey extends Struct$1{constructor(value){super({});this._bn=void 0;if(isPublicKeyData(value)){this._bn=value._bn}else{if(typeof value==="string"){const decoded=bs58.decode(value);if(decoded.length!=PUBLIC_KEY_LENGTH){throw new Error(`Invalid public key input`)}this._bn=new BN(decoded)}else{this._bn=new BN(value)}if(this._bn.byteLength()>PUBLIC_KEY_LENGTH){throw new Error(`Invalid public key input`)}}}static unique(){const key=new PublicKey(uniquePublicKeyCounter);uniquePublicKeyCounter+=1;return new PublicKey(key.toBuffer())}equals(publicKey){return this._bn.eq(publicKey._bn)}toBase58(){return bs58.encode(this.toBytes())}toJSON(){return this.toBase58()}toBytes(){const buf=this.toBuffer();return new Uint8Array(buf.buffer,buf.byteOffset,buf.byteLength)}toBuffer(){const b=this._bn.toArrayLike(bufferExports.Buffer);if(b.length===PUBLIC_KEY_LENGTH){return b}const zeroPad=bufferExports.Buffer.alloc(32);b.copy(zeroPad,32-b.length);return zeroPad}get[Symbol.toStringTag](){return`PublicKey(${this.toString()})`}toString(){return this.toBase58()}static async createWithSeed(fromPublicKey,seed,programId){const buffer=bufferExports.Buffer.concat([fromPublicKey.toBuffer(),bufferExports.Buffer.from(seed),programId.toBuffer()]);const publicKeyBytes=sha256$1(buffer);return new PublicKey(publicKeyBytes)}static createProgramAddressSync(seeds,programId){let buffer=bufferExports.Buffer.alloc(0);seeds.forEach((function(seed){if(seed.length>MAX_SEED_LENGTH){throw new TypeError(`Max seed length exceeded`)}buffer=bufferExports.Buffer.concat([buffer,toBuffer(seed)])}));buffer=bufferExports.Buffer.concat([buffer,programId.toBuffer(),bufferExports.Buffer.from("ProgramDerivedAddress")]);const publicKeyBytes=sha256$1(buffer);if(isOnCurve(publicKeyBytes)){throw new Error(`Invalid seeds, address must fall off the curve`)}return new PublicKey(publicKeyBytes)}static async createProgramAddress(seeds,programId){return this.createProgramAddressSync(seeds,programId)}static findProgramAddressSync(seeds,programId){let nonce=255;let address;while(nonce!=0){try{const seedsWithNonce=seeds.concat(bufferExports.Buffer.from([nonce]));address=this.createProgramAddressSync(seedsWithNonce,programId)}catch(err){if(err instanceof TypeError){throw err}nonce--;continue}return[address,nonce]}throw new Error(`Unable to find a viable program address nonce`)}static async findProgramAddress(seeds,programId){return this.findProgramAddressSync(seeds,programId)}static isOnCurve(pubkeyData){const pubkey=new PublicKey(pubkeyData);return isOnCurve(pubkey.toBytes())}}_PublicKey=PublicKey;PublicKey.default=new _PublicKey("11111111111111111111111111111111");SOLANA_SCHEMA.set(PublicKey,{kind:"struct",fields:[["_bn","u256"]]});class Account{constructor(secretKey){this._publicKey=void 0;this._secretKey=void 0;if(secretKey){const secretKeyBuffer=toBuffer(secretKey);if(secretKey.length!==64){throw new Error("bad secret key size")}this._publicKey=secretKeyBuffer.slice(32,64);this._secretKey=secretKeyBuffer.slice(0,32)}else{this._secretKey=toBuffer(generatePrivateKey());this._publicKey=toBuffer(getPublicKey(this._secretKey))}}get publicKey(){return new PublicKey(this._publicKey)}get secretKey(){return bufferExports.Buffer.concat([this._secretKey,this._publicKey],64)}}const BPF_LOADER_DEPRECATED_PROGRAM_ID=new PublicKey("BPFLoader1111111111111111111111111111111111");var Layout={};var hasRequiredLayout;function requireLayout(){if(hasRequiredLayout)return Layout;hasRequiredLayout=1;Object.defineProperty(Layout,"__esModule",{value:true});Layout.s16=Layout.s8=Layout.nu64be=Layout.u48be=Layout.u40be=Layout.u32be=Layout.u24be=Layout.u16be=Layout.nu64=Layout.u48=Layout.u40=Layout.u32=Layout.u24=Layout.u16=Layout.u8=Layout.offset=Layout.greedy=Layout.Constant=Layout.UTF8=Layout.CString=Layout.Blob=Layout.Boolean=Layout.BitField=Layout.BitStructure=Layout.VariantLayout=Layout.Union=Layout.UnionLayoutDiscriminator=Layout.UnionDiscriminator=Layout.Structure=Layout.Sequence=Layout.DoubleBE=Layout.Double=Layout.FloatBE=Layout.Float=Layout.NearInt64BE=Layout.NearInt64=Layout.NearUInt64BE=Layout.NearUInt64=Layout.IntBE=Layout.Int=Layout.UIntBE=Layout.UInt=Layout.OffsetLayout=Layout.GreedyCount=Layout.ExternalLayout=Layout.bindConstructorLayout=Layout.nameWithProperty=Layout.Layout=Layout.uint8ArrayToBuffer=Layout.checkUint8Array=void 0;Layout.constant=Layout.utf8=Layout.cstr=Layout.blob=Layout.unionLayoutDiscriminator=Layout.union=Layout.seq=Layout.bits=Layout.struct=Layout.f64be=Layout.f64=Layout.f32be=Layout.f32=Layout.ns64be=Layout.s48be=Layout.s40be=Layout.s32be=Layout.s24be=Layout.s16be=Layout.ns64=Layout.s48=Layout.s40=Layout.s32=Layout.s24=void 0;const buffer_1=requireBuffer();function checkUint8Array(b){if(!(b instanceof Uint8Array)){throw new TypeError("b must be a Uint8Array")}}Layout.checkUint8Array=checkUint8Array;function uint8ArrayToBuffer(b){checkUint8Array(b);return buffer_1.Buffer.from(b.buffer,b.byteOffset,b.length)}Layout.uint8ArrayToBuffer=uint8ArrayToBuffer;let Layout$1=class Layout{constructor(span,property){if(!Number.isInteger(span)){throw new TypeError("span must be an integer")}this.span=span;this.property=property}makeDestinationObject(){return{}}getSpan(b,offset){if(0>this.span){throw new RangeError("indeterminate span")}return this.span}replicate(property){const rv=Object.create(this.constructor.prototype);Object.assign(rv,this);rv.property=property;return rv}fromArray(values){return undefined}};Layout.Layout=Layout$1;function nameWithProperty(name,lo){if(lo.property){return name+"["+lo.property+"]"}return name}Layout.nameWithProperty=nameWithProperty;function bindConstructorLayout(Class,layout){if("function"!==typeof Class){throw new TypeError("Class must be constructor")}if(Object.prototype.hasOwnProperty.call(Class,"layout_")){throw new Error("Class is already bound to a layout")}if(!(layout&&layout instanceof Layout$1)){throw new TypeError("layout must be a Layout")}if(Object.prototype.hasOwnProperty.call(layout,"boundConstructor_")){throw new Error("layout is already bound to a constructor")}Class.layout_=layout;layout.boundConstructor_=Class;layout.makeDestinationObject=()=>new Class;Object.defineProperty(Class.prototype,"encode",{value(b,offset){return layout.encode(this,b,offset)},writable:true});Object.defineProperty(Class,"decode",{value(b,offset){return layout.decode(b,offset)},writable:true})}Layout.bindConstructorLayout=bindConstructorLayout;class ExternalLayout extends Layout$1{isCount(){throw new Error("ExternalLayout is abstract")}}Layout.ExternalLayout=ExternalLayout;class GreedyCount extends ExternalLayout{constructor(elementSpan=1,property){if(!Number.isInteger(elementSpan)||0>=elementSpan){throw new TypeError("elementSpan must be a (positive) integer")}super(-1,property);this.elementSpan=elementSpan}isCount(){return true}decode(b,offset=0){checkUint8Array(b);const rem=b.length-offset;return Math.floor(rem/this.elementSpan)}encode(src,b,offset){return 0}}Layout.GreedyCount=GreedyCount;class OffsetLayout extends ExternalLayout{constructor(layout,offset=0,property){if(!(layout instanceof Layout$1)){throw new TypeError("layout must be a Layout")}if(!Number.isInteger(offset)){throw new TypeError("offset must be integer or undefined")}super(layout.span,property||layout.property);this.layout=layout;this.offset=offset}isCount(){return this.layout instanceof UInt||this.layout instanceof UIntBE}decode(b,offset=0){return this.layout.decode(b,offset+this.offset)}encode(src,b,offset=0){return this.layout.encode(src,b,offset+this.offset)}}Layout.OffsetLayout=OffsetLayout;class UInt extends Layout$1{constructor(span,property){super(span,property);if(6<this.span){throw new RangeError("span must not exceed 6 bytes")}}decode(b,offset=0){return uint8ArrayToBuffer(b).readUIntLE(offset,this.span)}encode(src,b,offset=0){uint8ArrayToBuffer(b).writeUIntLE(src,offset,this.span);return this.span}}Layout.UInt=UInt;class UIntBE extends Layout$1{constructor(span,property){super(span,property);if(6<this.span){throw new RangeError("span must not exceed 6 bytes")}}decode(b,offset=0){return uint8ArrayToBuffer(b).readUIntBE(offset,this.span)}encode(src,b,offset=0){uint8ArrayToBuffer(b).writeUIntBE(src,offset,this.span);return this.span}}Layout.UIntBE=UIntBE;class Int extends Layout$1{constructor(span,property){super(span,property);if(6<this.span){throw new RangeError("span must not exceed 6 bytes")}}decode(b,offset=0){return uint8ArrayToBuffer(b).readIntLE(offset,this.span)}encode(src,b,offset=0){uint8ArrayToBuffer(b).writeIntLE(src,offset,this.span);return this.span}}Layout.Int=Int;class IntBE extends Layout$1{constructor(span,property){super(span,property);if(6<this.span){throw new RangeError("span must not exceed 6 bytes")}}decode(b,offset=0){return uint8ArrayToBuffer(b).readIntBE(offset,this.span)}encode(src,b,offset=0){uint8ArrayToBuffer(b).writeIntBE(src,offset,this.span);return this.span}}Layout.IntBE=IntBE;const V2E32=Math.pow(2,32);function divmodInt64(src){const hi32=Math.floor(src/V2E32);const lo32=src-hi32*V2E32;return{hi32:hi32,lo32:lo32}}function roundedInt64(hi32,lo32){return hi32*V2E32+lo32}class NearUInt64 extends Layout$1{constructor(property){super(8,property)}decode(b,offset=0){const buffer=uint8ArrayToBuffer(b);const lo32=buffer.readUInt32LE(offset);const hi32=buffer.readUInt32LE(offset+4);return roundedInt64(hi32,lo32)}encode(src,b,offset=0){const split=divmodInt64(src);const buffer=uint8ArrayToBuffer(b);buffer.writeUInt32LE(split.lo32,offset);buffer.writeUInt32LE(split.hi32,offset+4);return 8}}Layout.NearUInt64=NearUInt64;class NearUInt64BE extends Layout$1{constructor(property){super(8,property)}decode(b,offset=0){const buffer=uint8ArrayToBuffer(b);const hi32=buffer.readUInt32BE(offset);const lo32=buffer.readUInt32BE(offset+4);return roundedInt64(hi32,lo32)}encode(src,b,offset=0){const split=divmodInt64(src);const buffer=uint8ArrayToBuffer(b);buffer.writeUInt32BE(split.hi32,offset);buffer.writeUInt32BE(split.lo32,offset+4);return 8}}Layout.NearUInt64BE=NearUInt64BE;class NearInt64 extends Layout$1{constructor(property){super(8,property)}decode(b,offset=0){const buffer=uint8ArrayToBuffer(b);const lo32=buffer.readUInt32LE(offset);const hi32=buffer.readInt32LE(offset+4);return roundedInt64(hi32,lo32)}encode(src,b,offset=0){const split=divmodInt64(src);const buffer=uint8ArrayToBuffer(b);buffer.writeUInt32LE(split.lo32,offset);buffer.writeInt32LE(split.hi32,offset+4);return 8}}Layout.NearInt64=NearInt64;class NearInt64BE extends Layout$1{constructor(property){super(8,property)}decode(b,offset=0){const buffer=uint8ArrayToBuffer(b);const hi32=buffer.readInt32BE(offset);const lo32=buffer.readUInt32BE(offset+4);return roundedInt64(hi32,lo32)}encode(src,b,offset=0){const split=divmodInt64(src);const buffer=uint8ArrayToBuffer(b);buffer.writeInt32BE(split.hi32,offset);buffer.writeUInt32BE(split.lo32,offset+4);return 8}}Layout.NearInt64BE=NearInt64BE;class Float extends Layout$1{constructor(property){super(4,property)}decode(b,offset=0){return uint8ArrayToBuffer(b).readFloatLE(offset)}encode(src,b,offset=0){uint8ArrayToBuffer(b).writeFloatLE(src,offset);return 4}}Layout.Float=Float;class FloatBE extends Layout$1{constructor(property){super(4,property)}decode(b,offset=0){return uint8ArrayToBuffer(b).readFloatBE(offset)}encode(src,b,offset=0){uint8ArrayToBuffer(b).writeFloatBE(src,offset);return 4}}Layout.FloatBE=FloatBE;class Double extends Layout$1{constructor(property){super(8,property)}decode(b,offset=0){return uint8ArrayToBuffer(b).readDoubleLE(offset)}encode(src,b,offset=0){uint8ArrayToBuffer(b).writeDoubleLE(src,offset);return 8}}Layout.Double=Double;class DoubleBE extends Layout$1{constructor(property){super(8,property)}decode(b,offset=0){return uint8ArrayToBuffer(b).readDoubleBE(offset)}encode(src,b,offset=0){uint8ArrayToBuffer(b).writeDoubleBE(src,offset);return 8}}Layout.DoubleBE=DoubleBE;class Sequence extends Layout$1{constructor(elementLayout,count,property){if(!(elementLayout instanceof Layout$1)){throw new TypeError("elementLayout must be a Layout")}if(!(count instanceof ExternalLayout&&count.isCount()||Number.isInteger(count)&&0<=count)){throw new TypeError("count must be non-negative integer "+"or an unsigned integer ExternalLayout")}let span=-1;if(!(count instanceof ExternalLayout)&&0<elementLayout.span){span=count*elementLayout.span}super(span,property);this.elementLayout=elementLayout;this.count=count}getSpan(b,offset=0){if(0<=this.span){return this.span}let span=0;let count=this.count;if(count instanceof ExternalLayout){count=count.decode(b,offset)}if(0<this.elementLayout.span){span=count*this.elementLayout.span}else{let idx=0;while(idx<count){span+=this.elementLayout.getSpan(b,offset+span);++idx}}return span}decode(b,offset=0){const rv=[];let i=0;let count=this.count;if(count instanceof ExternalLayout){count=count.decode(b,offset)}while(i<count){rv.push(this.elementLayout.decode(b,offset));offset+=this.elementLayout.getSpan(b,offset);i+=1}return rv}encode(src,b,offset=0){const elo=this.elementLayout;const span=src.reduce(((span,v)=>span+elo.encode(v,b,offset+span)),0);if(this.count instanceof ExternalLayout){this.count.encode(src.length,b,offset)}return span}}Layout.Sequence=Sequence;class Structure extends Layout$1{constructor(fields,property,decodePrefixes){if(!(Array.isArray(fields)&&fields.reduce(((acc,v)=>acc&&v instanceof Layout$1),true))){throw new TypeError("fields must be array of Layout instances")}if("boolean"===typeof property&&undefined===decodePrefixes){decodePrefixes=property;property=undefined}for(const fd of fields){if(0>fd.span&&undefined===fd.property){throw new Error("fields cannot contain unnamed variable-length layout")}}let span=-1;try{span=fields.reduce(((span,fd)=>span+fd.getSpan()),0)}catch(e){}super(span,property);this.fields=fields;this.decodePrefixes=!!decodePrefixes}getSpan(b,offset=0){if(0<=this.span){return this.span}let span=0;try{span=this.fields.reduce(((span,fd)=>{const fsp=fd.getSpan(b,offset);offset+=fsp;return span+fsp}),0)}catch(e){throw new RangeError("indeterminate span")}return span}decode(b,offset=0){checkUint8Array(b);const dest=this.makeDestinationObject();for(const fd of this.fields){if(undefined!==fd.property){dest[fd.property]=fd.decode(b,offset)}offset+=fd.getSpan(b,offset);if(this.decodePrefixes&&b.length===offset){break}}return dest}encode(src,b,offset=0){const firstOffset=offset;let lastOffset=0;let lastWrote=0;for(const fd of this.fields){let span=fd.span;lastWrote=0<span?span:0;if(undefined!==fd.property){const fv=src[fd.property];if(undefined!==fv){lastWrote=fd.encode(fv,b,offset);if(0>span){span=fd.getSpan(b,offset)}}}lastOffset=offset;offset+=span}return lastOffset+lastWrote-firstOffset}fromArray(values){const dest=this.makeDestinationObject();for(const fd of this.fields){if(undefined!==fd.property&&0<values.length){dest[fd.property]=values.shift()}}return dest}layoutFor(property){if("string"!==typeof property){throw new TypeError("property must be string")}for(const fd of this.fields){if(fd.property===property){return fd}}return undefined}offsetOf(property){if("string"!==typeof property){throw new TypeError("property must be string")}let offset=0;for(const fd of this.fields){if(fd.property===property){return offset}if(0>fd.span){offset=-1}else if(0<=offset){offset+=fd.span}}return undefined}}Layout.Structure=Structure;class UnionDiscriminator{constructor(property){this.property=property}decode(b,offset){throw new Error("UnionDiscriminator is abstract")}encode(src,b,offset){throw new Error("UnionDiscriminator is abstract")}}Layout.UnionDiscriminator=UnionDiscriminator;class UnionLayoutDiscriminator extends UnionDiscriminator{constructor(layout,property){if(!(layout instanceof ExternalLayout&&layout.isCount())){throw new TypeError("layout must be an unsigned integer ExternalLayout")}super(property||layout.property||"variant");this.layout=layout}decode(b,offset){return this.layout.decode(b,offset)}encode(src,b,offset){return this.layout.encode(src,b,offset)}}Layout.UnionLayoutDiscriminator=UnionLayoutDiscriminator;class Union extends Layout$1{constructor(discr,defaultLayout,property){let discriminator;if(discr instanceof UInt||discr instanceof UIntBE){discriminator=new UnionLayoutDiscriminator(new OffsetLayout(discr))}else if(discr instanceof ExternalLayout&&discr.isCount()){discriminator=new UnionLayoutDiscriminator(discr)}else if(!(discr instanceof UnionDiscriminator)){throw new TypeError("discr must be a UnionDiscriminator "+"or an unsigned integer layout")}else{discriminator=discr}if(undefined===defaultLayout){defaultLayout=null}if(!(null===defaultLayout||defaultLayout instanceof Layout$1)){throw new TypeError("defaultLayout must be null or a Layout")}if(null!==defaultLayout){if(0>defaultLayout.span){throw new Error("defaultLayout must have constant span")}if(undefined===defaultLayout.property){defaultLayout=defaultLayout.replicate("content")}}let span=-1;if(defaultLayout){span=defaultLayout.span;if(0<=span&&(discr instanceof UInt||discr instanceof UIntBE)){span+=discriminator.layout.span}}super(span,property);this.discriminator=discriminator;this.usesPrefixDiscriminator=discr instanceof UInt||discr instanceof UIntBE;this.defaultLayout=defaultLayout;this.registry={};let boundGetSourceVariant=this.defaultGetSourceVariant.bind(this);this.getSourceVariant=function(src){return boundGetSourceVariant(src)};this.configGetSourceVariant=function(gsv){boundGetSourceVariant=gsv.bind(this)}}getSpan(b,offset=0){if(0<=this.span){return this.span}const vlo=this.getVariant(b,offset);if(!vlo){throw new Error("unable to determine span for unrecognized variant")}return vlo.getSpan(b,offset)}defaultGetSourceVariant(src){if(Object.prototype.hasOwnProperty.call(src,this.discriminator.property)){if(this.defaultLayout&&this.defaultLayout.property&&Object.prototype.hasOwnProperty.call(src,this.defaultLayout.property)){return undefined}const vlo=this.registry[src[this.discriminator.property]];if(vlo&&(!vlo.layout||vlo.property&&Object.prototype.hasOwnProperty.call(src,vlo.property))){return vlo}}else{for(const tag in this.registry){const vlo=this.registry[tag];if(vlo.property&&Object.prototype.hasOwnProperty.call(src,vlo.property)){return vlo}}}throw new Error("unable to infer src variant")}decode(b,offset=0){let dest;const dlo=this.discriminator;const discr=dlo.decode(b,offset);const clo=this.registry[discr];if(undefined===clo){const defaultLayout=this.defaultLayout;let contentOffset=0;if(this.usesPrefixDiscriminator){contentOffset=dlo.layout.span}dest=this.makeDestinationObject();dest[dlo.property]=discr;dest[defaultLayout.property]=defaultLayout.decode(b,offset+contentOffset)}else{dest=clo.decode(b,offset)}return dest}encode(src,b,offset=0){const vlo=this.getSourceVariant(src);if(undefined===vlo){const dlo=this.discriminator;const clo=this.defaultLayout;let contentOffset=0;if(this.usesPrefixDiscriminator){contentOffset=dlo.layout.span}dlo.encode(src[dlo.property],b,offset);return contentOffset+clo.encode(src[clo.property],b,offset+contentOffset)}return vlo.encode(src,b,offset)}addVariant(variant,layout,property){const rv=new VariantLayout(this,variant,layout,property);this.registry[variant]=rv;return rv}getVariant(vb,offset=0){let variant;if(vb instanceof Uint8Array){variant=this.discriminator.decode(vb,offset)}else{variant=vb}return this.registry[variant]}}Layout.Union=Union;class VariantLayout extends Layout$1{constructor(union,variant,layout,property){if(!(union instanceof Union)){throw new TypeError("union must be a Union")}if(!Number.isInteger(variant)||0>variant){throw new TypeError("variant must be a (non-negative) integer")}if("string"===typeof layout&&undefined===property){property=layout;layout=null}if(layout){if(!(layout instanceof Layout$1)){throw new TypeError("layout must be a Layout")}if(null!==union.defaultLayout&&0<=layout.span&&layout.span>union.defaultLayout.span){throw new Error("variant span exceeds span of containing union")}if("string"!==typeof property){throw new TypeError("variant must have a String property")}}let span=union.span;if(0>union.span){span=layout?layout.span:0;if(0<=span&&union.usesPrefixDiscriminator){span+=union.discriminator.layout.span}}super(span,property);this.union=union;this.variant=variant;this.layout=layout||null}getSpan(b,offset=0){if(0<=this.span){return this.span}let contentOffset=0;if(this.union.usesPrefixDiscriminator){contentOffset=this.union.discriminator.layout.span}let span=0;if(this.layout){span=this.layout.getSpan(b,offset+contentOffset)}return contentOffset+span}decode(b,offset=0){const dest=this.makeDestinationObject();if(this!==this.union.getVariant(b,offset)){throw new Error("variant mismatch")}let contentOffset=0;if(this.union.usesPrefixDiscriminator){contentOffset=this.union.discriminator.layout.span}if(this.layout){dest[this.property]=this.layout.decode(b,offset+contentOffset)}else if(this.property){dest[this.property]=true}else if(this.union.usesPrefixDiscriminator){dest[this.union.discriminator.property]=this.variant}return dest}encode(src,b,offset=0){let contentOffset=0;if(this.union.usesPrefixDiscriminator){contentOffset=this.union.discriminator.layout.span}if(this.layout&&!Object.prototype.hasOwnProperty.call(src,this.property)){throw new TypeError("variant lacks property "+this.property)}this.union.discriminator.encode(this.variant,b,offset);let span=contentOffset;if(this.layout){this.layout.encode(src[this.property],b,offset+contentOffset);span+=this.layout.getSpan(b,offset+contentOffset);if(0<=this.union.span&&span>this.union.span){throw new Error("encoded variant overruns containing union")}}return span}fromArray(values){if(this.layout){return this.layout.fromArray(values)}return undefined}}Layout.VariantLayout=VariantLayout;function fixBitwiseResult(v){if(0>v){v+=4294967296}return v}class BitStructure extends Layout$1{constructor(word,msb,property){if(!(word instanceof UInt||word instanceof UIntBE)){throw new TypeError("word must be a UInt or UIntBE layout")}if("string"===typeof msb&&undefined===property){property=msb;msb=false}if(4<word.span){throw new RangeError("word cannot exceed 32 bits")}super(word.span,property);this.word=word;this.msb=!!msb;this.fields=[];let value=0;this._packedSetValue=function(v){value=fixBitwiseResult(v);return this};this._packedGetValue=function(){return value}}decode(b,offset=0){const dest=this.makeDestinationObject();const value=this.word.decode(b,offset);this._packedSetValue(value);for(const fd of this.fields){if(undefined!==fd.property){dest[fd.property]=fd.decode(b)}}return dest}encode(src,b,offset=0){const value=this.word.decode(b,offset);this._packedSetValue(value);for(const fd of this.fields){if(undefined!==fd.property){const fv=src[fd.property];if(undefined!==fv){fd.encode(fv)}}}return this.word.encode(this._packedGetValue(),b,offset)}addField(bits,property){const bf=new BitField(this,bits,property);this.fields.push(bf);return bf}addBoolean(property){const bf=new Boolean(this,property);this.fields.push(bf);return bf}fieldFor(property){if("string"!==typeof property){throw new TypeError("property must be string")}for(const fd of this.fields){if(fd.property===property){return fd}}return undefined}}Layout.BitStructure=BitStructure;class BitField{constructor(container,bits,property){if(!(container instanceof BitStructure)){throw new TypeError("container must be a BitStructure")}if(!Number.isInteger(bits)||0>=bits){throw new TypeError("bits must be positive integer")}const totalBits=8*container.span;const usedBits=container.fields.reduce(((sum,fd)=>sum+fd.bits),0);if(bits+usedBits>totalBits){throw new Error("bits too long for span remainder ("+(totalBits-usedBits)+" of "+totalBits+" remain)")}this.container=container;this.bits=bits;this.valueMask=(1<<bits)-1;if(32===bits){this.valueMask=4294967295}this.start=usedBits;if(this.container.msb){this.start=totalBits-usedBits-bits}this.wordMask=fixBitwiseResult(this.valueMask<<this.start);this.property=property}decode(b,offset){const word=this.container._packedGetValue();const wordValue=fixBitwiseResult(word&this.wordMask);const value=wordValue>>>this.start;return value}encode(value){if("number"!==typeof value||!Number.isInteger(value)||value!==fixBitwiseResult(value&this.valueMask)){throw new TypeError(nameWithProperty("BitField.encode",this)+" value must be integer not exceeding "+this.valueMask)}const word=this.container._packedGetValue();const wordValue=fixBitwiseResult(value<<this.start);this.container._packedSetValue(fixBitwiseResult(word&~this.wordMask)|wordValue)}}Layout.BitField=BitField;class Boolean extends BitField{constructor(container,property){super(container,1,property)}decode(b,offset){return!!super.decode(b,offset)}encode(value){if("boolean"===typeof value){value=+value}super.encode(value)}}Layout.Boolean=Boolean;class Blob extends Layout$1{constructor(length,property){if(!(length instanceof ExternalLayout&&length.isCount()||Number.isInteger(length)&&0<=length)){throw new TypeError("length must be positive integer "+"or an unsigned integer ExternalLayout")}let span=-1;if(!(length instanceof ExternalLayout)){span=length}super(span,property);this.length=length}getSpan(b,offset){let span=this.span;if(0>span){span=this.length.decode(b,offset)}return span}decode(b,offset=0){let span=this.span;if(0>span){span=this.length.decode(b,offset)}return uint8ArrayToBuffer(b).slice(offset,offset+span)}encode(src,b,offset){let span=this.length;if(this.length instanceof ExternalLayout){span=src.length}if(!(src instanceof Uint8Array&&span===src.length)){throw new TypeError(nameWithProperty("Blob.encode",this)+" requires (length "+span+") Uint8Array as src")}if(offset+span>b.length){throw new RangeError("encoding overruns Uint8Array")}const srcBuffer=uint8ArrayToBuffer(src);uint8ArrayToBuffer(b).write(srcBuffer.toString("hex"),offset,span,"hex");if(this.length instanceof ExternalLayout){this.length.encode(span,b,offset)}return span}}Layout.Blob=Blob;class CString extends Layout$1{constructor(property){super(-1,property)}getSpan(b,offset=0){checkUint8Array(b);let idx=offset;while(idx<b.length&&0!==b[idx]){idx+=1}return 1+idx-offset}decode(b,offset=0){const span=this.getSpan(b,offset);return uint8ArrayToBuffer(b).slice(offset,offset+span-1).toString("utf-8")}encode(src,b,offset=0){if("string"!==typeof src){src=String(src)}const srcb=buffer_1.Buffer.from(src,"utf8");const span=srcb.length;if(offset+span>b.length){throw new RangeError("encoding overruns Buffer")}const buffer=uint8ArrayToBuffer(b);srcb.copy(buffer,offset);buffer[offset+span]=0;return span+1}}Layout.CString=CString;class UTF8 extends Layout$1{constructor(maxSpan,property){if("string"===typeof maxSpan&&undefined===property){property=maxSpan;maxSpan=undefined}if(undefined===maxSpan){maxSpan=-1}else if(!Number.isInteger(maxSpan)){throw new TypeError("maxSpan must be an integer")}super(-1,property);this.maxSpan=maxSpan}getSpan(b,offset=0){checkUint8Array(b);return b.length-offset}decode(b,offset=0){const span=this.getSpan(b,offset);if(0<=this.maxSpan&&this.maxSpan<span){throw new RangeError("text length exceeds maxSpan")}return uint8ArrayToBuffer(b).slice(offset,offset+span).toString("utf-8")}encode(src,b,offset=0){if("string"!==typeof src){src=String(src)}const srcb=buffer_1.Buffer.from(src,"utf8");const span=srcb.length;if(0<=this.maxSpan&&this.maxSpan<span){throw new RangeError("text length exceeds maxSpan")}if(offset+span>b.length){throw new RangeError("encoding overruns Buffer")}srcb.copy(uint8ArrayToBuffer(b),offset);return span}}Layout.UTF8=UTF8;class Constant extends Layout$1{constructor(value,property){super(0,property);this.value=value}decode(b,offset){return this.value}encode(src,b,offset){return 0}}Layout.Constant=Constant;Layout.greedy=(elementSpan,property)=>new GreedyCount(elementSpan,property);Layout.offset=(layout,offset,property)=>new OffsetLayout(layout,offset,property);Layout.u8=property=>new UInt(1,property);Layout.u16=property=>new UInt(2,property);Layout.u24=property=>new UInt(3,property);Layout.u32=property=>new UInt(4,property);Layout.u40=property=>new UInt(5,property);Layout.u48=property=>new UInt(6,property);Layout.nu64=property=>new NearUInt64(property);Layout.u16be=property=>new UIntBE(2,property);Layout.u24be=property=>new UIntBE(3,property);Layout.u32be=property=>new UIntBE(4,property);Layout.u40be=property=>new UIntBE(5,property);Layout.u48be=property=>new UIntBE(6,property);Layout.nu64be=property=>new NearUInt64BE(property);Layout.s8=property=>new Int(1,property);Layout.s16=property=>new Int(2,property);Layout.s24=property=>new Int(3,property);Layout.s32=property=>new Int(4,property);Layout.s40=property=>new Int(5,property);Layout.s48=property=>new Int(6,property);Layout.ns64=property=>new NearInt64(property);Layout.s16be=property=>new IntBE(2,property);Layout.s24be=property=>new IntBE(3,property);Layout.s32be=property=>new IntBE(4,property);Layout.s40be=property=>new IntBE(5,property);Layout.s48be=property=>new IntBE(6,property);Layout.ns64be=property=>new NearInt64BE(property);Layout.f32=property=>new Float(property);Layout.f32be=property=>new FloatBE(property);Layout.f64=property=>new Double(property);Layout.f64be=property=>new DoubleBE(property);Layout.struct=(fields,property,decodePrefixes)=>new Structure(fields,property,decodePrefixes);Layout.bits=(word,msb,property)=>new BitStructure(word,msb,property);Layout.seq=(elementLayout,count,property)=>new Sequence(elementLayout,count,property);Layout.union=(discr,defaultLayout,property)=>new Union(discr,defaultLayout,property);Layout.unionLayoutDiscriminator=(layout,property)=>new UnionLayoutDiscriminator(layout,property);Layout.blob=(length,property)=>new Blob(length,property);Layout.cstr=property=>new CString(property);Layout.utf8=(maxSpan,property)=>new UTF8(maxSpan,property);Layout.constant=(value,property)=>new Constant(value,property);return Layout}var LayoutExports=requireLayout();const PACKET_DATA_SIZE=1280-40-8;const VERSION_PREFIX_MASK=127;const SIGNATURE_LENGTH_IN_BYTES=64;class TransactionExpiredBlockheightExceededError extends Error{constructor(signature){super(`Signature ${signature} has expired: block height exceeded.`);this.signature=void 0;this.signature=signature}}Object.defineProperty(TransactionExpiredBlockheightExceededError.prototype,"name",{value:"TransactionExpiredBlockheightExceededError"});class TransactionExpiredTimeoutError extends Error{constructor(signature,timeoutSeconds){super(`Transaction was not confirmed in ${timeoutSeconds.toFixed(2)} seconds. It is `+"unknown if it succeeded or failed. Check signature "+`${signature} using the Solana Explorer or CLI tools.`);this.signature=void 0;this.signature=signature}}Object.defineProperty(TransactionExpiredTimeoutError.prototype,"name",{value:"TransactionExpiredTimeoutError"});class TransactionExpiredNonceInvalidError extends Error{constructor(signature){super(`Signature ${signature} has expired: the nonce is no longer valid.`);this.signature=void 0;this.signature=signature}}Object.defineProperty(TransactionExpiredNonceInvalidError.prototype,"name",{value:"TransactionExpiredNonceInvalidError"});class MessageAccountKeys{constructor(staticAccountKeys,accountKeysFromLookups){this.staticAccountKeys=void 0;this.accountKeysFromLookups=void 0;this.staticAccountKeys=staticAccountKeys;this.accountKeysFromLookups=accountKeysFromLookups}keySegments(){const keySegments=[this.staticAccountKeys];if(this.accountKeysFromLookups){keySegments.push(this.accountKeysFromLookups.writable);keySegments.push(this.accountKeysFromLookups.readonly)}return keySegments}get(index){for(const keySegment of this.keySegments()){if(index<keySegment.length){return keySegment[index]}else{index-=keySegment.length}}return}get length(){return this.keySegments().flat().length}compileInstructions(instructions){const U8_MAX=255;if(this.length>U8_MAX+1){throw new Error("Account index overflow encountered during compilation")}const keyIndexMap=new Map;this.keySegments().flat().forEach(((key,index)=>{keyIndexMap.set(key.toBase58(),index)}));const findKeyIndex=key=>{const keyIndex=keyIndexMap.get(key.toBase58());if(keyIndex===undefined)throw new Error("Encountered an unknown instruction account key during compilation");return keyIndex};return instructions.map((instruction=>({programIdIndex:findKeyIndex(instruction.programId),accountKeyIndexes:instruction.keys.map((meta=>findKeyIndex(meta.pubkey))),data:instruction.data})))}}const publicKey=(property="publicKey")=>LayoutExports.blob(32,property);const signature=(property="signature")=>LayoutExports.blob(64,property);const rustString=(property="string")=>{const rsl=LayoutExports.struct([LayoutExports.u32("length"),LayoutExports.u32("lengthPadding"),LayoutExports.blob(LayoutExports.offset(LayoutExports.u32(),-8),"chars")],property);const _decode=rsl.decode.bind(rsl);const _encode=rsl.encode.bind(rsl);const rslShim=rsl;rslShim.decode=(b,offset)=>{const data=_decode(b,offset);return data["chars"].toString()};rslShim.encode=(str,b,offset)=>{const data={chars:bufferExports.Buffer.from(str,"utf8")};return _encode(data,b,offset)};rslShim.alloc=str=>LayoutExports.u32().span+LayoutExports.u32().span+bufferExports.Buffer.from(str,"utf8").length;return rslShim};const authorized=(property="authorized")=>LayoutExports.struct([publicKey("staker"),publicKey("withdrawer")],property);const lockup=(property="lockup")=>LayoutExports.struct([LayoutExports.ns64("unixTimestamp"),LayoutExports.ns64("epoch"),publicKey("custodian")],property);const voteInit=(property="voteInit")=>LayoutExports.struct([publicKey("nodePubkey"),publicKey("authorizedVoter"),publicKey("authorizedWithdrawer"),LayoutExports.u8("commission")],property);const voteAuthorizeWithSeedArgs=(property="voteAuthorizeWithSeedArgs")=>LayoutExports.struct([LayoutExports.u32("voteAuthorizationType"),publicKey("currentAuthorityDerivedKeyOwnerPubkey"),rustString("currentAuthorityDerivedKeySeed"),publicKey("newAuthorized")],property);function getAlloc(type,fields){const getItemAlloc=item=>{if(item.span>=0){return item.span}else if(typeof item.alloc==="function"){return item.alloc(fields[item.property])}else if("count"in item&&"elementLayout"in item){const field=fields[item.property];if(Array.isArray(field)){return field.length*getItemAlloc(item.elementLayout)}}else if("fields"in item){return getAlloc({layout:item},fields[item.property])}return 0};let alloc=0;type.layout.fields.forEach((item=>{alloc+=getItemAlloc(item)}));return alloc}function decodeLength(bytes){let len=0;let size=0;for(;;){let elem=bytes.shift();len|=(elem&127)<<size*7;size+=1;if((elem&128)===0){break}}return len}function encodeLength(bytes,len){let rem_len=len;for(;;){let elem=rem_len&127;rem_len>>=7;if(rem_len==0){bytes.push(elem);break}else{elem|=128;bytes.push(elem)}}}function assert$1(condition,message){if(!condition){throw new Error(message||"Assertion failed")}}class CompiledKeys{constructor(payer,keyMetaMap){this.payer=void 0;this.keyMetaMap=void 0;this.payer=payer;this.keyMetaMap=keyMetaMap}static compile(instructions,payer){const keyMetaMap=new Map;const getOrInsertDefault=pubkey=>{const address=pubkey.toBase58();let keyMeta=keyMetaMap.get(address);if(keyMeta===undefined){keyMeta={isSigner:false,isWritable:false,isInvoked:false};keyMetaMap.set(address,keyMeta)}return keyMeta};const payerKeyMeta=getOrInsertDefault(payer);payerKeyMeta.isSigner=true;payerKeyMeta.isWritable=true;for(const ix of instructions){getOrInsertDefault(ix.programId).isInvoked=true;for(const accountMeta of ix.keys){const keyMeta=getOrInsertDefault(accountMeta.pubkey);keyMeta.isSigner||=accountMeta.isSigner;keyMeta.isWritable||=accountMeta.isWritable}}return new CompiledKeys(payer,keyMetaMap)}getMessageComponents(){const mapEntries=[...this.keyMetaMap.entries()];assert$1(mapEntries.length<=256,"Max static account keys length exceeded");const writableSigners=mapEntries.filter((([,meta])=>meta.isSigner&&meta.isWritable));const readonlySigners=mapEntries.filter((([,meta])=>meta.isSigner&&!meta.isWritable));const writableNonSigners=mapEntries.filter((([,meta])=>!meta.isSigner&&meta.isWritable));const readonlyNonSigners=mapEntries.filter((([,meta])=>!meta.isSigner&&!meta.isWritable));const header={numRequiredSignatures:writableSigners.length+readonlySigners.length,numReadonlySignedAccounts:readonlySigners.length,numReadonlyUnsignedAccounts:readonlyNonSigners.length};{assert$1(writableSigners.length>0,"Expected at least one writable signer key");const[payerAddress]=writableSigners[0];assert$1(payerAddress===this.payer.toBase58(),"Expected first writable signer key to be the fee payer")}const staticAccountKeys=[...writableSigners.map((([address])=>new PublicKey(address))),...readonlySigners.map((([address])=>new PublicKey(address))),...writableNonSigners.map((([address])=>new PublicKey(address))),...readonlyNonSigners.map((([address])=>new PublicKey(address)))];return[header,staticAccountKeys]}extractTableLookup(lookupTable){const[writableIndexes,drainedWritableKeys]=this.drainKeysFoundInLookupTable(lookupTable.state.addresses,(keyMeta=>!keyMeta.isSigner&&!keyMeta.isInvoked&&keyMeta.isWritable));const[readonlyIndexes,drainedReadonlyKeys]=this.drainKeysFoundInLookupTable(lookupTable.state.addresses,(keyMeta=>!keyMeta.isSigner&&!keyMeta.isInvoked&&!keyMeta.isWritable));if(writableIndexes.length===0&&readonlyIndexes.length===0){return}return[{accountKey:lookupTable.key,writableIndexes:writableIndexes,readonlyIndexes:readonlyIndexes},{writable:drainedWritableKeys,readonly:drainedReadonlyKeys}]}drainKeysFoundInLookupTable(lookupTableEntries,keyMetaFilter){const lookupTableIndexes=new Array;const drainedKeys=new Array;for(const[address,keyMeta]of this.keyMetaMap.entries()){if(keyMetaFilter(keyMeta)){const key=new PublicKey(address);const lookupTableIndex=lookupTableEntries.findIndex((entry=>entry.equals(key)));if(lookupTableIndex>=0){assert$1(lookupTableIndex<256,"Max lookup table index exceeded");lookupTableIndexes.push(lookupTableIndex);drainedKeys.push(key);this.keyMetaMap.delete(address)}}}return[lookupTableIndexes,drainedKeys]}}const END_OF_BUFFER_ERROR_MESSAGE="Reached end of buffer unexpectedly";function guardedShift(byteArray){if(byteArray.length===0){throw new Error(END_OF_BUFFER_ERROR_MESSAGE)}return byteArray.shift()}function guardedSplice(byteArray,...args){const[start]=args;if(args.length===2?start+(args[1]??0)>byteArray.length:start>=byteArray.length){throw new Error(END_OF_BUFFER_ERROR_MESSAGE)}return byteArray.splice(...args)}class Message{constructor(args){this.header=void 0;this.accountKeys=void 0;this.recentBlockhash=void 0;this.instructions=void 0;this.indexToProgramIds=new Map;this.header=args.header;this.accountKeys=args.accountKeys.map((account=>new PublicKey(account)));this.recentBlockhash=args.recentBlockhash;this.instructions=args.instructions;this.instructions.forEach((ix=>this.indexToProgramIds.set(ix.programIdIndex,this.accountKeys[ix.programIdIndex])))}get version(){return"legacy"}get staticAccountKeys(){return this.accountKeys}get compiledInstructions(){return this.instructions.map((ix=>({programIdIndex:ix.programIdIndex,accountKeyIndexes:ix.accounts,data:bs58.decode(ix.data)})))}get addressTableLookups(){return[]}getAccountKeys(){return new MessageAccountKeys(this.staticAccountKeys)}static compile(args){const compiledKeys=CompiledKeys.compile(args.instructions,args.payerKey);const[header,staticAccountKeys]=compiledKeys.getMessageComponents();const accountKeys=new MessageAccountKeys(staticAccountKeys);const instructions=accountKeys.compileInstructions(args.instructions).map((ix=>({programIdIndex:ix.programIdIndex,accounts:ix.accountKeyIndexes,data:bs58.encode(ix.data)})));return new Message({header:header,accountKeys:staticAccountKeys,recentBlockhash:args.recentBlockhash,instructions:instructions})}isAccountSigner(index){return index<this.header.numRequiredSignatures}isAccountWritable(index){const numSignedAccounts=this.header.numRequiredSignatures;if(index>=this.header.numRequiredSignatures){const unsignedAccountIndex=index-numSignedAccounts;const numUnsignedAccounts=this.accountKeys.length-numSignedAccounts;const numWritableUnsignedAccounts=numUnsignedAccounts-this.header.numReadonlyUnsignedAccounts;return unsignedAccountIndex<numWritableUnsignedAccounts}else{const numWritableSignedAccounts=numSignedAccounts-this.header.numReadonlySignedAccounts;return index<numWritableSignedAccounts}}isProgramId(index){return this.indexToProgramIds.has(index)}programIds(){return[...this.indexToProgramIds.values()]}nonProgramIds(){return this.accountKeys.filter(((_,index)=>!this.isProgramId(index)))}serialize(){const numKeys=this.accountKeys.length;let keyCount=[];encodeLength(keyCount,numKeys);const instructions=this.instructions.map((instruction=>{const{accounts:accounts,programIdIndex:programIdIndex}=instruction;const data=Array.from(bs58.decode(instruction.data));let keyIndicesCount=[];encodeLength(keyIndicesCount,accounts.length);let dataCount=[];encodeLength(dataCount,data.length);return{programIdIndex:programIdIndex,keyIndicesCount:bufferExports.Buffer.from(keyIndicesCount),keyIndices:accounts,dataLength:bufferExports.Buffer.from(dataCount),data:data}}));let instructionCount=[];encodeLength(instructionCount,instructions.length);let instructionBuffer=bufferExports.Buffer.alloc(PACKET_DATA_SIZE);bufferExports.Buffer.from(instructionCount).copy(instructionBuffer);let instructionBufferLength=instructionCount.length;instructions.forEach((instruction=>{const instructionLayout=LayoutExports.struct([LayoutExports.u8("programIdIndex"),LayoutExports.blob(instruction.keyIndicesCount.length,"keyIndicesCount"),LayoutExports.seq(LayoutExports.u8("keyIndex"),instruction.keyIndices.length,"keyIndices"),LayoutExports.blob(instruction.dataLength.length,"dataLength"),LayoutExports.seq(LayoutExports.u8("userdatum"),instruction.data.length,"data")]);const length=instructionLayout.encode(instruction,instructionBuffer,instructionBufferLength);instructionBufferLength+=length}));instructionBuffer=instructionBuffer.slice(0,instructionBufferLength);const signDataLayout=LayoutExports.struct([LayoutExports.blob(1,"numRequiredSignatures"),LayoutExports.blob(1,"numReadonlySignedAccounts"),LayoutExports.blob(1,"numReadonlyUnsignedAccounts"),LayoutExports.blob(keyCount.length,"keyCount"),LayoutExports.seq(publicKey("key"),numKeys,"keys"),publicKey("recentBlockhash")]);const transaction={numRequiredSignatures:bufferExports.Buffer.from([this.header.numRequiredSignatures]),numReadonlySignedAccounts:bufferExports.Buffer.from([this.header.numReadonlySignedAccounts]),numReadonlyUnsignedAccounts:bufferExports.Buffer.from([this.header.numReadonlyUnsignedAccounts]),keyCount:bufferExports.Buffer.from(keyCount),keys:this.accountKeys.map((key=>toBuffer(key.toBytes()))),recentBlockhash:bs58.decode(this.recentBlockhash)};let signData=bufferExports.Buffer.alloc(2048);const length=signDataLayout.encode(transaction,signData);instructionBuffer.copy(signData,length);return signData.slice(0,length+instructionBuffer.length)}static from(buffer){let byteArray=[...buffer];const numRequiredSignatures=guardedShift(byteArray);if(numRequiredSignatures!==(numRequiredSignatures&VERSION_PREFIX_MASK)){throw new Error("Versioned messages must be deserialized with VersionedMessage.deserialize()")}const numReadonlySignedAccounts=guardedShift(byteArray);const numReadonlyUnsignedAccounts=guardedShift(byteArray);const accountCount=decodeLength(byteArray);let accountKeys=[];for(let i=0;i<accountCount;i++){const account=guardedSplice(byteArray,0,PUBLIC_KEY_LENGTH);accountKeys.push(new PublicKey(bufferExports.Buffer.from(account)))}const recentBlockhash=guardedSplice(byteArray,0,PUBLIC_KEY_LENGTH);const instructionCount=decodeLength(byteArray);let instructions=[];for(let i=0;i<instructionCount;i++){const programIdIndex=guardedShift(byteArray);const accountCount=decodeLength(byteArray);const accounts=guardedSplice(byteArray,0,accountCount);const dataLength=decodeLength(byteArray);const dataSlice=guardedSplice(byteArray,0,dataLength);const data=bs58.encode(bufferExports.Buffer.from(dataSlice));instructions.push({programIdIndex:programIdIndex,accounts:accounts,data:data})}const messageArgs={header:{numRequiredSignatures:numRequiredSignatures,numReadonlySignedAccounts:numReadonlySignedAccounts,numReadonlyUnsignedAccounts:numReadonlyUnsignedAccounts},recentBlockhash:bs58.encode(bufferExports.Buffer.from(recentBlockhash)),accountKeys:accountKeys,instructions:instructions};return new Message(messageArgs)}}class MessageV0{constructor(args){this.header=void 0;this.staticAccountKeys=void 0;this.recentBlockhash=void 0;this.compiledInstructions=void 0;this.addressTableLookups=void 0;this.header=args.header;this.staticAccountKeys=args.staticAccountKeys;this.recentBlockhash=args.recentBlockhash;this.compiledInstructions=args.compiledInstructions;this.addressTableLookups=args.addressTableLookups}get version(){return 0}get numAccountKeysFromLookups(){let count=0;for(const lookup of this.addressTableLookups){count+=lookup.readonlyIndexes.length+lookup.writableIndexes.length}return count}getAccountKeys(args){let accountKeysFromLookups;if(args&&"accountKeysFromLookups"in args&&args.accountKeysFromLookups){if(this.numAccountKeysFromLookups!=args.accountKeysFromLookups.writable.length+args.accountKeysFromLookups.readonly.length){throw new Error("Failed to get account keys because of a mismatch in the number of account keys from lookups")}accountKeysFromLookups=args.accountKeysFromLookups}else if(args&&"addressLookupTableAccounts"in args&&args.addressLookupTableAccounts){accountKeysFromLookups=this.resolveAddressTableLookups(args.addressLookupTableAccounts)}else if(this.addressTableLookups.length>0){throw new Error("Failed to get account keys because address table lookups were not resolved")}return new MessageAccountKeys(this.staticAccountKeys,accountKeysFromLookups)}isAccountSigner(index){return index<this.header.numRequiredSignatures}isAccountWritable(index){const numSignedAccounts=this.header.numRequiredSignatures;const numStaticAccountKeys=this.staticAccountKeys.length;if(index>=numStaticAccountKeys){const lookupAccountKeysIndex=index-numStaticAccountKeys;const numWritableLookupAccountKeys=this.addressTableLookups.reduce(((count,lookup)=>count+lookup.writableIndexes.length),0);return lookupAccountKeysIndex<numWritableLookupAccountKeys}else if(index>=this.header.numRequiredSignatures){const unsignedAccountIndex=index-numSignedAccounts;const numUnsignedAccounts=numStaticAccountKeys-numSignedAccounts;const numWritableUnsignedAccounts=numUnsignedAccounts-this.header.numReadonlyUnsignedAccounts;return unsignedAccountIndex<numWritableUnsignedAccounts}else{const numWritableSignedAccounts=numSignedAccounts-this.header.numReadonlySignedAccounts;return index<numWritableSignedAccounts}}resolveAddressTableLookups(addressLookupTableAccounts){const accountKeysFromLookups={writable:[],readonly:[]};for(const tableLookup of this.addressTableLookups){const tableAccount=addressLookupTableAccounts.find((account=>account.key.equals(tableLookup.accountKey)));if(!tableAccount){throw new Error(`Failed to find address lookup table account for table key ${tableLookup.accountKey.toBase58()}`)}for(const index of tableLookup.writableIndexes){if(index<tableAccount.state.addresses.length){accountKeysFromLookups.writable.push(tableAccount.state.addresses[index])}else{throw new Error(`Failed to find address for index ${index} in address lookup table ${tableLookup.accountKey.toBase58()}`)}}for(const index of tableLookup.readonlyIndexes){if(index<tableAccount.state.addresses.length){accountKeysFromLookups.readonly.push(tableAccount.state.addresses[index])}else{throw new Error(`Failed to find address for index ${index} in address lookup table ${tableLookup.accountKey.toBase58()}`)}}}return accountKeysFromLookups}static compile(args){const compiledKeys=CompiledKeys.compile(args.instructions,args.payerKey);const addressTableLookups=new Array;const accountKeysFromLookups={writable:new Array,readonly:new Array};const lookupTableAccounts=args.addressLookupTableAccounts||[];for(const lookupTable of lookupTableAccounts){const extractResult=compiledKeys.extractTableLookup(lookupTable);if(extractResult!==undefined){const[addressTableLookup,{writable:writable,readonly:readonly}]=extractResult;addressTableLookups.push(addressTableLookup);accountKeysFromLookups.writable.push(...writable);accountKeysFromLookups.readonly.push(...readonly)}}const[header,staticAccountKeys]=compiledKeys.getMessageComponents();const accountKeys=new MessageAccountKeys(staticAccountKeys,accountKeysFromLookups);const compiledInstructions=accountKeys.compileInstructions(args.instructions);return new MessageV0({header:header,staticAccountKeys:staticAccountKeys,recentBlockhash:args.recentBlockhash,compiledInstructions:compiledInstructions,addressTableLookups:addressTableLookups})}serialize(){const encodedStaticAccountKeysLength=Array();encodeLength(encodedStaticAccountKeysLength,this.staticAccountKeys.length);const serializedInstructions=this.serializeInstructions();const encodedInstructionsLength=Array();encodeLength(encodedInstructionsLength,this.compiledInstructions.length);const serializedAddressTableLookups=this.serializeAddressTableLookups();const encodedAddressTableLookupsLength=Array();encodeLength(encodedAddressTableLookupsLength,this.addressTableLookups.length);const messageLayout=LayoutExports.struct([LayoutExports.u8("prefix"),LayoutExports.struct([LayoutExports.u8("numRequiredSignatures"),LayoutExports.u8("numReadonlySignedAccounts"),LayoutExports.u8("numReadonlyUnsignedAccounts")],"header"),LayoutExports.blob(encodedStaticAccountKeysLength.length,"staticAccountKeysLength"),LayoutExports.seq(publicKey(),this.staticAccountKeys.length,"staticAccountKeys"),publicKey("recentBlockhash"),LayoutExports.blob(encodedInstructionsLength.length,"instructionsLength"),LayoutExports.blob(serializedInstructions.length,"serializedInstructions"),LayoutExports.blob(encodedAddressTableLookupsLength.length,"addressTableLookupsLength"),LayoutExports.blob(serializedAddressTableLookups.length,"serializedAddressTableLookups")]);const serializedMessage=new Uint8Array(PACKET_DATA_SIZE);const MESSAGE_VERSION_0_PREFIX=1<<7;const serializedMessageLength=messageLayout.encode({prefix:MESSAGE_VERSION_0_PREFIX,header:this.header,staticAccountKeysLength:new Uint8Array(encodedStaticAccountKeysLength),staticAccountKeys:this.staticAccountKeys.map((key=>key.toBytes())),recentBlockhash:bs58.decode(this.recentBlockhash),instructionsLength:new Uint8Array(encodedInstructionsLength),serializedInstructions:serializedInstructions,addressTableLookupsLength:new Uint8Array(encodedAddressTableLookupsLength),serializedAddressTableLookups:serializedAddressTableLookups},serializedMessage);return serializedMessage.slice(0,serializedMessageLength)}serializeInstructions(){let serializedLength=0;const serializedInstructions=new Uint8Array(PACKET_DATA_SIZE);for(const instruction of this.compiledInstructions){const encodedAccountKeyIndexesLength=Array();encodeLength(encodedAccountKeyIndexesLength,instruction.accountKeyIndexes.length);const encodedDataLength=Array();encodeLength(encodedDataLength,instruction.data.length);const instructionLayout=LayoutExports.struct([LayoutExports.u8("programIdIndex"),LayoutExports.blob(encodedAccountKeyIndexesLength.length,"encodedAccountKeyIndexesLength"),LayoutExports.seq(LayoutExports.u8(),instruction.accountKeyIndexes.length,"accountKeyIndexes"),LayoutExports.blob(encodedDataLength.length,"encodedDataLength"),LayoutExports.blob(instruction.data.length,"data")]);serializedLength+=instructionLayout.encode({programIdIndex:instruction.programIdIndex,encodedAccountKeyIndexesLength:new Uint8Array(encodedAccountKeyIndexesLength),accountKeyIndexes:instruction.accountKeyIndexes,encodedDataLength:new Uint8Array(encodedDataLength),data:instruction.data},serializedInstructions,serializedLength)}return serializedInstructions.slice(0,serializedLength)}serializeAddressTableLookups(){let serializedLength=0;const serializedAddressTableLookups=new Uint8Array(PACKET_DATA_SIZE);for(const lookup of this.addressTableLookups){const encodedWritableIndexesLength=Array();encodeLength(encodedWritableIndexesLength,lookup.writableIndexes.length);const encodedReadonlyIndexesLength=Array();encodeLength(encodedReadonlyIndexesLength,lookup.readonlyIndexes.length);const addressTableLookupLayout=LayoutExports.struct([publicKey("accountKey"),LayoutExports.blob(encodedWritableIndexesLength.length,"encodedWritableIndexesLength"),LayoutExports.seq(LayoutExports.u8(),lookup.writableIndexes.length,"writableIndexes"),LayoutExports.blob(encodedReadonlyIndexesLength.length,"encodedReadonlyIndexesLength"),LayoutExports.seq(LayoutExports.u8(),lookup.readonlyIndexes.length,"readonlyIndexes")]);serializedLength+=addressTableLookupLayout.encode({accountKey:lookup.accountKey.toBytes(),encodedWritableIndexesLength:new Uint8Array(encodedWritableIndexesLength),writableIndexes:lookup.writableIndexes,encodedReadonlyIndexesLength:new Uint8Array(encodedReadonlyIndexesLength),readonlyIndexes:lookup.readonlyIndexes},serializedAddressTableLookups,serializedLength)}return serializedAddressTableLookups.slice(0,serializedLength)}static deserialize(serializedMessage){let byteArray=[...serializedMessage];const prefix=guardedShift(byteArray);const maskedPrefix=prefix&VERSION_PREFIX_MASK;assert$1(prefix!==maskedPrefix,`Expected versioned message but received legacy message`);const version=maskedPrefix;assert$1(version===0,`Expected versioned message with version 0 but found version ${version}`);const header={numRequiredSignatures:guardedShift(byteArray),numReadonlySignedAccounts:guardedShift(byteArray),numReadonlyUnsignedAccounts:guardedShift(byteArray)};const staticAccountKeys=[];const staticAccountKeysLength=decodeLength(byteArray);for(let i=0;i<staticAccountKeysLength;i++){staticAccountKeys.push(new PublicKey(guardedSplice(byteArray,0,PUBLIC_KEY_LENGTH)))}const recentBlockhash=bs58.encode(guardedSplice(byteArray,0,PUBLIC_KEY_LENGTH));const instructionCount=decodeLength(byteArray);const compiledInstructions=[];for(let i=0;i<instructionCount;i++){const programIdIndex=guardedShift(byteArray);const accountKeyIndexesLength=decodeLength(byteArray);const accountKeyIndexes=guardedSplice(byteArray,0,accountKeyIndexesLength);const dataLength=decodeLength(byteArray);const data=new Uint8Array(guardedSplice(byteArray,0,dataLength));compiledInstructions.push({programIdIndex:programIdIndex,accountKeyIndexes:accountKeyIndexes,data:data})}const addressTableLookupsCount=decodeLength(byteArray);const addressTableLookups=[];for(let i=0;i<addressTableLookupsCount;i++){const accountKey=new PublicKey(guardedSplice(byteArray,0,PUBLIC_KEY_LENGTH));const writableIndexesLength=decodeLength(byteArray);const writableIndexes=guardedSplice(byteArray,0,writableIndexesLength);const readonlyIndexesLength=decodeLength(byteArray);const readonlyIndexes=guardedSplice(byteArray,0,readonlyIndexesLength);addressTableLookups.push({accountKey:accountKey,writableIndexes:writableIndexes,readonlyIndexes:readonlyIndexes})}return new MessageV0({header:header,staticAccountKeys:staticAccountKeys,recentBlockhash:recentBlockhash,compiledInstructions:compiledInstructions,addressTableLookups:addressTableLookups})}}const VersionedMessage={deserializeMessageVersion(serializedMessage){const prefix=serializedMessage[0];const maskedPrefix=prefix&VERSION_PREFIX_MASK;if(maskedPrefix===prefix){return"legacy"}return maskedPrefix},deserialize:serializedMessage=>{const version=VersionedMessage.deserializeMessageVersion(serializedMessage);if(version==="legacy"){return Message.from(serializedMessage)}if(version===0){return MessageV0.deserialize(serializedMessage)}else{throw new Error(`Transaction message version ${version} deserialization is not supported`)}}};let TransactionStatus=function(TransactionStatus){TransactionStatus[TransactionStatus["BLOCKHEIGHT_EXCEEDED"]=0]="BLOCKHEIGHT_EXCEEDED";TransactionStatus[TransactionStatus["PROCESSED"]=1]="PROCESSED";TransactionStatus[TransactionStatus["TIMED_OUT"]=2]="TIMED_OUT";TransactionStatus[TransactionStatus["NONCE_INVALID"]=3]="NONCE_INVALID";return TransactionStatus}({});const DEFAULT_SIGNATURE=bufferExports.Buffer.alloc(SIGNATURE_LENGTH_IN_BYTES).fill(0);class TransactionInstruction{constructor(opts){this.keys=void 0;this.programId=void 0;this.data=bufferExports.Buffer.alloc(0);this.programId=opts.programId;this.keys=opts.keys;if(opts.data){this.data=opts.data}}toJSON(){return{keys:this.keys.map((({pubkey:pubkey,isSigner:isSigner,isWritable:isWritable})=>({pubkey:pubkey.toJSON(),isSigner:isSigner,isWritable:isWritable}))),programId:this.programId.toJSON(),data:[...this.data]}}}class Transaction{get signature(){if(this.signatures.length>0){return this.signatures[0].signature}return null}constructor(opts){this.signatures=[];this.feePayer=void 0;this.instructions=[];this.recentBlockhash=void 0;this.lastValidBlockHeight=void 0;this.nonceInfo=void 0;this.minNonceContextSlot=void 0;this._message=void 0;this._json=void 0;if(!opts){return}if(opts.feePayer){this.feePayer=opts.feePayer}if(opts.signatures){this.signatures=opts.signatures}if(Object.prototype.hasOwnProperty.call(opts,"nonceInfo")){const{minContextSlot:minContextSlot,nonceInfo:nonceInfo}=opts;this.minNonceContextSlot=minContextSlot;this.nonceInfo=nonceInfo}else if(Object.prototype.hasOwnProperty.call(opts,"lastValidBlockHeight")){const{blockhash:blockhash,lastValidBlockHeight:lastValidBlockHeight}=opts;this.recentBlockhash=blockhash;this.lastValidBlockHeight=lastValidBlockHeight}else{const{recentBlockhash:recentBlockhash,nonceInfo:nonceInfo}=opts;if(nonceInfo){this.nonceInfo=nonceInfo}this.recentBlockhash=recentBlockhash}}toJSON(){return{recentBlockhash:this.recentBlockhash||null,feePayer:this.feePayer?this.feePayer.toJSON():null,nonceInfo:this.nonceInfo?{nonce:this.nonceInfo.nonce,nonceInstruction:this.nonceInfo.nonceInstruction.toJSON()}:null,instructions:this.instructions.map((instruction=>instruction.toJSON())),signers:this.signatures.map((({publicKey:publicKey})=>publicKey.toJSON()))}}add(...items){if(items.length===0){throw new Error("No instructions")}items.forEach((item=>{if("instructions"in item){this.instructions=this.instructions.concat(item.instructions)}else if("data"in item&&"programId"in item&&"keys"in item){this.instructions.push(item)}else{this.instructions.push(new TransactionInstruction(item))}}));return this}compileMessage(){if(this._message&&JSON.stringify(this.toJSON())===JSON.stringify(this._json)){return this._message}let recentBlockhash;let instructions;if(this.nonceInfo){recentBlockhash=this.nonceInfo.nonce;if(this.instructions[0]!=this.nonceInfo.nonceInstruction){instructions=[this.nonceInfo.nonceInstruction,...this.instructions]}else{instructions=this.instructions}}else{recentBlockhash=this.recentBlockhash;instructions=this.instructions}if(!recentBlockhash){throw new Error("Transaction recentBlockhash required")}if(instructions.length<1){console.warn("No instructions provided")}let feePayer;if(this.feePayer){feePayer=this.feePayer}else if(this.signatures.length>0&&this.signatures[0].publicKey){feePayer=this.signatures[0].publicKey}else{throw new Error("Transaction fee payer required")}for(let i=0;i<instructions.length;i++){if(instructions[i].programId===undefined){throw new Error(`Transaction instruction index ${i} has undefined program id`)}}const programIds=[];const accountMetas=[];instructions.forEach((instruction=>{instruction.keys.forEach((accountMeta=>{accountMetas.push({...accountMeta})}));const programId=instruction.programId.toString();if(!programIds.includes(programId)){programIds.push(programId)}}));programIds.forEach((programId=>{accountMetas.push({pubkey:new PublicKey(programId),isSigner:false,isWritable:false})}));const uniqueMetas=[];accountMetas.forEach((accountMeta=>{const pubkeyString=accountMeta.pubkey.toString();const uniqueIndex=uniqueMetas.findIndex((x=>x.pubkey.toString()===pubkeyString));if(uniqueIndex>-1){uniqueMetas[uniqueIndex].isWritable=uniqueMetas[uniqueIndex].isWritable||accountMeta.isWritable;uniqueMetas[uniqueIndex].isSigner=uniqueMetas[uniqueIndex].isSigner||accountMeta.isSigner}else{uniqueMetas.push(accountMeta)}}));uniqueMetas.sort((function(x,y){if(x.isSigner!==y.isSigner){return x.isSigner?-1:1}if(x.isWritable!==y.isWritable){return x.isWritable?-1:1}const options={localeMatcher:"best fit",usage:"sort",sensitivity:"variant",ignorePunctuation:false,numeric:false,caseFirst:"lower"};return x.pubkey.toBase58().localeCompare(y.pubkey.toBase58(),"en",options)}));const feePayerIndex=uniqueMetas.findIndex((x=>x.pubkey.equals(feePayer)));if(feePayerIndex>-1){const[payerMeta]=uniqueMetas.splice(feePayerIndex,1);payerMeta.isSigner=true;payerMeta.isWritable=true;uniqueMetas.unshift(payerMeta)}else{uniqueMetas.unshift({pubkey:feePayer,isSigner:true,isWritable:true})}for(const signature of this.signatures){const uniqueIndex=uniqueMetas.findIndex((x=>x.pubkey.equals(signature.publicKey)));if(uniqueIndex>-1){if(!uniqueMetas[uniqueIndex].isSigner){uniqueMetas[uniqueIndex].isSigner=true;console.warn("Transaction references a signature that is unnecessary, "+"only the fee payer and instruction signer accounts should sign a transaction. "+"This behavior is deprecated and will throw an error in the next major version release.")}}else{throw new Error(`unknown signer: ${signature.publicKey.toString()}`)}}let numRequiredSignatures=0;let numReadonlySignedAccounts=0;let numReadonlyUnsignedAccounts=0;const signedKeys=[];const unsignedKeys=[];uniqueMetas.forEach((({pubkey:pubkey,isSigner:isSigner,isWritable:isWritable})=>{if(isSigner){signedKeys.push(pubkey.toString());numRequiredSignatures+=1;if(!isWritable){numReadonlySignedAccounts+=1}}else{unsignedKeys.push(pubkey.toString());if(!isWritable){numReadonlyUnsignedAccounts+=1}}}));const accountKeys=signedKeys.concat(unsignedKeys);const compiledInstructions=instructions.map((instruction=>{const{data:data,programId:programId}=instruction;return{programIdIndex:accountKeys.indexOf(programId.toString()),accounts:instruction.keys.map((meta=>accountKeys.indexOf(meta.pubkey.toString()))),data:bs58.encode(data)}}));compiledInstructions.forEach((instruction=>{assert$1(instruction.programIdIndex>=0);instruction.accounts.forEach((keyIndex=>assert$1(keyIndex>=0)))}));return new Message({header:{numRequiredSignatures:numRequiredSignatures,numReadonlySignedAccounts:numReadonlySignedAccounts,numReadonlyUnsignedAccounts:numReadonlyUnsignedAccounts},accountKeys:accountKeys,recentBlockhash:recentBlockhash,instructions:compiledInstructions})}_compile(){const message=this.compileMessage();const signedKeys=message.accountKeys.slice(0,message.header.numRequiredSignatures);if(this.signatures.length===signedKeys.length){const valid=this.signatures.every(((pair,index)=>signedKeys[index].equals(pair.publicKey)));if(valid)return message}this.signatures=signedKeys.map((publicKey=>({signature:null,publicKey:publicKey})));return message}serializeMessage(){return this._compile().serialize()}async getEstimatedFee(connection){return(await connection.getFeeForMessage(this.compileMessage())).value}setSigners(...signers){if(signers.length===0){throw new Error("No signers")}const seen=new Set;this.signatures=signers.filter((publicKey=>{const key=publicKey.toString();if(seen.has(key)){return false}else{seen.add(key);return true}})).map((publicKey=>({signature:null,publicKey:publicKey})))}sign(...signers){if(signers.length===0){throw new Error("No signers")}const seen=new Set;const uniqueSigners=[];for(const signer of signers){const key=signer.publicKey.toString();if(seen.has(key)){continue}else{seen.add(key);uniqueSigners.push(signer)}}this.signatures=uniqueSigners.map((signer=>({signature:null,publicKey:signer.publicKey})));const message=this._compile();this._partialSign(message,...uniqueSigners)}partialSign(...signers){if(signers.length===0){throw new Error("No signers")}const seen=new Set;const uniqueSigners=[];for(const signer of signers){const key=signer.publicKey.toString();if(seen.has(key)){continue}else{seen.add(key);uniqueSigners.push(signer)}}const message=this._compile();this._partialSign(message,...uniqueSigners)}_partialSign(message,...signers){const signData=message.serialize();signers.forEach((signer=>{const signature=sign(signData,signer.secretKey);this._addSignature(signer.publicKey,toBuffer(signature))}))}addSignature(pubkey,signature){this._compile();this._addSignature(pubkey,signature)}_addSignature(pubkey,signature){assert$1(signature.length===64);const index=this.signatures.findIndex((sigpair=>pubkey.equals(sigpair.publicKey)));if(index<0){throw new Error(`unknown signer: ${pubkey.toString()}`)}this.signatures[index].signature=bufferExports.Buffer.from(signature)}verifySignatures(requireAllSignatures=true){const signatureErrors=this._getMessageSignednessErrors(this.serializeMessage(),requireAllSignatures);return!signatureErrors}_getMessageSignednessErrors(message,requireAllSignatures){const errors={};for(const{signature:signature,publicKey:publicKey}of this.signatures){if(signature===null){if(requireAllSignatures){(errors.missing||=[]).push(publicKey)}}else{if(!verify(signature,message,publicKey.toBytes())){(errors.invalid||=[]).push(publicKey)}}}return errors.invalid||errors.missing?errors:undefined}serialize(config){const{requireAllSignatures:requireAllSignatures,verifySignatures:verifySignatures}=Object.assign({requireAllSignatures:true,verifySignatures:true},config);const signData=this.serializeMessage();if(verifySignatures){const sigErrors=this._getMessageSignednessErrors(signData,requireAllSignatures);if(sigErrors){let errorMessage="Signature verification failed.";if(sigErrors.invalid){errorMessage+=`\nInvalid signature for public key${sigErrors.invalid.length===1?"":"(s)"} [\`${sigErrors.invalid.map((p=>p.toBase58())).join("`, `")}\`].`}if(sigErrors.missing){errorMessage+=`\nMissing signature for public key${sigErrors.missing.length===1?"":"(s)"} [\`${sigErrors.missing.map((p=>p.toBase58())).join("`, `")}\`].`}throw new Error(errorMessage)}}return this._serialize(signData)}_serialize(signData){const{signatures:signatures}=this;const signatureCount=[];encodeLength(signatureCount,signatures.length);const transactionLength=signatureCount.length+signatures.length*64+signData.length;const wireTransaction=bufferExports.Buffer.alloc(transactionLength);assert$1(signatures.length<256);bufferExports.Buffer.from(signatureCount).copy(wireTransaction,0);signatures.forEach((({signature:signature},index)=>{if(signature!==null){assert$1(signature.length===64,`signature has invalid length`);bufferExports.Buffer.from(signature).copy(wireTransaction,signatureCount.length+index*64)}}));signData.copy(wireTransaction,signatureCount.length+signatures.length*64);assert$1(wireTransaction.length<=PACKET_DATA_SIZE,`Transaction too large: ${wireTransaction.length} > ${PACKET_DATA_SIZE}`);return wireTransaction}get keys(){assert$1(this.instructions.length===1);return this.instructions[0].keys.map((keyObj=>keyObj.pubkey))}get programId(){assert$1(this.instructions.length===1);return this.instructions[0].programId}get data(){assert$1(this.instructions.length===1);return this.instructions[0].data}static from(buffer){let byteArray=[...buffer];const signatureCount=decodeLength(byteArray);let signatures=[];for(let i=0;i<signatureCount;i++){const signature=guardedSplice(byteArray,0,SIGNATURE_LENGTH_IN_BYTES);signatures.push(bs58.encode(bufferExports.Buffer.from(signature)))}return Transaction.populate(Message.from(byteArray),signatures)}static populate(message,signatures=[]){const transaction=new Transaction;transaction.recentBlockhash=message.recentBlockhash;if(message.header.numRequiredSignatures>0){transaction.feePayer=message.accountKeys[0]}signatures.forEach(((signature,index)=>{const sigPubkeyPair={signature:signature==bs58.encode(DEFAULT_SIGNATURE)?null:bs58.decode(signature),publicKey:message.accountKeys[index]};transaction.signatures.push(sigPubkeyPair)}));message.instructions.forEach((instruction=>{const keys=instruction.accounts.map((account=>{const pubkey=message.accountKeys[account];return{pubkey:pubkey,isSigner:transaction.signatures.some((keyObj=>keyObj.publicKey.toString()===pubkey.toString()))||message.isAccountSigner(account),isWritable:message.isAccountWritable(account)}}));transaction.instructions.push(new TransactionInstruction({keys:keys,programId:message.accountKeys[instruction.programIdIndex],data:bs58.decode(instruction.data)}))}));transaction._message=message;transaction._json=transaction.toJSON();return transaction}}class TransactionMessage{constructor(args){this.payerKey=void 0;this.instructions=void 0;this.recentBlockhash=void 0;this.payerKey=args.payerKey;this.instructions=args.instructions;this.recentBlockhash=args.recentBlockhash}static decompile(message,args){const{header:header,compiledInstructions:compiledInstructions,recentBlockhash:recentBlockhash}=message;const{numRequiredSignatures:numRequiredSignatures,numReadonlySignedAccounts:numReadonlySignedAccounts,numReadonlyUnsignedAccounts:numReadonlyUnsignedAccounts}=header;const numWritableSignedAccounts=numRequiredSignatures-numReadonlySignedAccounts;assert$1(numWritableSignedAccounts>0,"Message header is invalid");const numWritableUnsignedAccounts=message.staticAccountKeys.length-numRequiredSignatures-numReadonlyUnsignedAccounts;assert$1(numWritableUnsignedAccounts>=0,"Message header is invalid");const accountKeys=message.getAccountKeys(args);const payerKey=accountKeys.get(0);if(payerKey===undefined){throw new Error("Failed to decompile message because no account keys were found")}const instructions=[];for(const compiledIx of compiledInstructions){const keys=[];for(const keyIndex of compiledIx.accountKeyIndexes){const pubkey=accountKeys.get(keyIndex);if(pubkey===undefined){throw new Error(`Failed to find key for account key index ${keyIndex}`)}const isSigner=keyIndex<numRequiredSignatures;let isWritable;if(isSigner){isWritable=keyIndex<numWritableSignedAccounts}else if(keyIndex<accountKeys.staticAccountKeys.length){isWritable=keyIndex-numRequiredSignatures<numWritableUnsignedAccounts}else{isWritable=keyIndex-accountKeys.staticAccountKeys.length<accountKeys.accountKeysFromLookups.writable.length}keys.push({pubkey:pubkey,isSigner:keyIndex<header.numRequiredSignatures,isWritable:isWritable})}const programId=accountKeys.get(compiledIx.programIdIndex);if(programId===undefined){throw new Error(`Failed to find program id for program id index ${compiledIx.programIdIndex}`)}instructions.push(new TransactionInstruction({programId:programId,data:toBuffer(compiledIx.data),keys:keys}))}return new TransactionMessage({payerKey:payerKey,instructions:instructions,recentBlockhash:recentBlockhash})}compileToLegacyMessage(){return Message.compile({payerKey:this.payerKey,recentBlockhash:this.recentBlockhash,instructions:this.instructions})}compileToV0Message(addressLookupTableAccounts){return MessageV0.compile({payerKey:this.payerKey,recentBlockhash:this.recentBlockhash,instructions:this.instructions,addressLookupTableAccounts:addressLookupTableAccounts})}}class VersionedTransaction{get version(){return this.message.version}constructor(message,signatures){this.signatures=void 0;this.message=void 0;if(signatures!==undefined){assert$1(signatures.length===message.header.numRequiredSignatures,"Expected signatures length to be equal to the number of required signatures");this.signatures=signatures}else{const defaultSignatures=[];for(let i=0;i<message.header.numRequiredSignatures;i++){defaultSignatures.push(new Uint8Array(SIGNATURE_LENGTH_IN_BYTES))}this.signatures=defaultSignatures}this.message=message}serialize(){const serializedMessage=this.message.serialize();const encodedSignaturesLength=Array();encodeLength(encodedSignaturesLength,this.signatures.length);const transactionLayout=LayoutExports.struct([LayoutExports.blob(encodedSignaturesLength.length,"encodedSignaturesLength"),LayoutExports.seq(signature(),this.signatures.length,"signatures"),LayoutExports.blob(serializedMessage.length,"serializedMessage")]);const serializedTransaction=new Uint8Array(2048);const serializedTransactionLength=transactionLayout.encode({encodedSignaturesLength:new Uint8Array(encodedSignaturesLength),signatures:this.signatures,serializedMessage:serializedMessage},serializedTransaction);return serializedTransaction.slice(0,serializedTransactionLength)}static deserialize(serializedTransaction){let byteArray=[...serializedTransaction];const signatures=[];const signaturesLength=decodeLength(byteArray);for(let i=0;i<signaturesLength;i++){signatures.push(new Uint8Array(guardedSplice(byteArray,0,SIGNATURE_LENGTH_IN_BYTES)))}const message=VersionedMessage.deserialize(new Uint8Array(byteArray));return new VersionedTransaction(message,signatures)}sign(signers){const messageData=this.message.serialize();const signerPubkeys=this.message.staticAccountKeys.slice(0,this.message.header.numRequiredSignatures);for(const signer of signers){const signerIndex=signerPubkeys.findIndex((pubkey=>pubkey.equals(signer.publicKey)));assert$1(signerIndex>=0,`Cannot sign with non signer key ${signer.publicKey.toBase58()}`);this.signatures[signerIndex]=sign(messageData,signer.secretKey)}}addSignature(publicKey,signature){assert$1(signature.byteLength===64,"Signature must be 64 bytes long");const signerPubkeys=this.message.staticAccountKeys.slice(0,this.message.header.numRequiredSignatures);const signerIndex=signerPubkeys.findIndex((pubkey=>pubkey.equals(publicKey)));assert$1(signerIndex>=0,`Can not add signature; \`${publicKey.toBase58()}\` is not required to sign this transaction`);this.signatures[signerIndex]=signature}}const NUM_TICKS_PER_SECOND=160;const DEFAULT_TICKS_PER_SLOT=64;const NUM_SLOTS_PER_SECOND=NUM_TICKS_PER_SECOND/DEFAULT_TICKS_PER_SLOT;const MS_PER_SLOT=1e3/NUM_SLOTS_PER_SECOND;const SYSVAR_CLOCK_PUBKEY=new PublicKey("SysvarC1ock11111111111111111111111111111111");const SYSVAR_EPOCH_SCHEDULE_PUBKEY=new PublicKey("SysvarEpochSchedu1e111111111111111111111111");const SYSVAR_INSTRUCTIONS_PUBKEY=new PublicKey("Sysvar1nstructions1111111111111111111111111");const SYSVAR_RECENT_BLOCKHASHES_PUBKEY=new PublicKey("SysvarRecentB1ockHashes11111111111111111111");const SYSVAR_RENT_PUBKEY=new PublicKey("SysvarRent111111111111111111111111111111111");const SYSVAR_REWARDS_PUBKEY=new PublicKey("SysvarRewards111111111111111111111111111111");const SYSVAR_SLOT_HASHES_PUBKEY=new PublicKey("SysvarS1otHashes111111111111111111111111111");const SYSVAR_SLOT_HISTORY_PUBKEY=new PublicKey("SysvarS1otHistory11111111111111111111111111");const SYSVAR_STAKE_HISTORY_PUBKEY=new PublicKey("SysvarStakeHistory1111111111111111111111111");class SendTransactionError extends Error{constructor({action:action,signature:signature,transactionMessage:transactionMessage,logs:logs}){const maybeLogsOutput=logs?`Logs: \n${JSON.stringify(logs.slice(-10),null,2)}. `:"";const guideText="\nCatch the `SendTransactionError` and call `getLogs()` on it for full details.";let message;switch(action){case"send":message=`Transaction ${signature} resulted in an error. \n`+`${transactionMessage}. `+maybeLogsOutput+guideText;break;case"simulate":message=`Simulation failed. \nMessage: ${transactionMessage}. \n`+maybeLogsOutput+guideText;break;default:{message=`Unknown action '${(a=>a)(action)}'`}}super(message);this.signature=void 0;this.transactionMessage=void 0;this.transactionLogs=void 0;this.signature=signature;this.transactionMessage=transactionMessage;this.transactionLogs=logs?logs:undefined}get transactionError(){return{message:this.transactionMessage,logs:Array.isArray(this.transactionLogs)?this.transactionLogs:undefined}}get logs(){const cachedLogs=this.transactionLogs;if(cachedLogs!=null&&typeof cachedLogs==="object"&&"then"in cachedLogs){return undefined}return cachedLogs}async getLogs(connection){if(!Array.isArray(this.transactionLogs)){this.transactionLogs=new Promise(((resolve,reject)=>{connection.getTransaction(this.signature).then((tx=>{if(tx&&tx.meta&&tx.meta.logMessages){const logs=tx.meta.logMessages;this.transactionLogs=logs;resolve(logs)}else{reject(new Error("Log messages not found"))}})).catch(reject)}))}return await this.transactionLogs}}const SolanaJSONRPCErrorCode={JSON_RPC_SERVER_ERROR_BLOCK_CLEANED_UP:-32001,JSON_RPC_SERVER_ERROR_SEND_TRANSACTION_PREFLIGHT_FAILURE:-32002,JSON_RPC_SERVER_ERROR_TRANSACTION_SIGNATURE_VERIFICATION_FAILURE:-32003,JSON_RPC_SERVER_ERROR_BLOCK_NOT_AVAILABLE:-32004,JSON_RPC_SERVER_ERROR_NODE_UNHEALTHY:-32005,JSON_RPC_SERVER_ERROR_TRANSACTION_PRECOMPILE_VERIFICATION_FAILURE:-32006,JSON_RPC_SERVER_ERROR_SLOT_SKIPPED:-32007,JSON_RPC_SERVER_ERROR_NO_SNAPSHOT:-32008,JSON_RPC_SERVER_ERROR_LONG_TERM_STORAGE_SLOT_SKIPPED:-32009,JSON_RPC_SERVER_ERROR_KEY_EXCLUDED_FROM_SECONDARY_INDEX:-32010,JSON_RPC_SERVER_ERROR_TRANSACTION_HISTORY_NOT_AVAILABLE:-32011,JSON_RPC_SCAN_ERROR:-32012,JSON_RPC_SERVER_ERROR_TRANSACTION_SIGNATURE_LEN_MISMATCH:-32013,JSON_RPC_SERVER_ERROR_BLOCK_STATUS_NOT_AVAILABLE_YET:-32014,JSON_RPC_SERVER_ERROR_UNSUPPORTED_TRANSACTION_VERSION:-32015,JSON_RPC_SERVER_ERROR_MIN_CONTEXT_SLOT_NOT_REACHED:-32016};class SolanaJSONRPCError extends Error{constructor({code:code,message:message,data:data},customMessage){super(customMessage!=null?`${customMessage}: ${message}`:message);this.code=void 0;this.data=void 0;this.code=code;this.data=data;this.name="SolanaJSONRPCError"}}async function sendAndConfirmTransaction(connection,transaction,signers,options){const sendOptions=options&&{skipPreflight:options.skipPreflight,preflightCommitment:options.preflightCommitment||options.commitment,maxRetries:options.maxRetries,minContextSlot:options.minContextSlot};const signature=await connection.sendTransaction(transaction,signers,sendOptions);let status;if(transaction.recentBlockhash!=null&&transaction.lastValidBlockHeight!=null){status=(await connection.confirmTransaction({abortSignal:options?.abortSignal,signature:signature,blockhash:transaction.recentBlockhash,lastValidBlockHeight:transaction.lastValidBlockHeight},options&&options.commitment)).value}else if(transaction.minNonceContextSlot!=null&&transaction.nonceInfo!=null){const{nonceInstruction:nonceInstruction}=transaction.nonceInfo;const nonceAccountPubkey=nonceInstruction.keys[0].pubkey;status=(await connection.confirmTransaction({abortSignal:options?.abortSignal,minContextSlot:transaction.minNonceContextSlot,nonceAccountPubkey:nonceAccountPubkey,nonceValue:transaction.nonceInfo.nonce,signature:signature},options&&options.commitment)).value}else{if(options?.abortSignal!=null){console.warn("sendAndConfirmTransaction(): A transaction with a deprecated confirmation strategy was "+"supplied along with an `abortSignal`. Only transactions having `lastValidBlockHeight` "+"or a combination of `nonceInfo` and `minNonceContextSlot` are abortable.")}status=(await connection.confirmTransaction(signature,options&&options.commitment)).value}if(status.err){if(signature!=null){throw new SendTransactionError({action:"send",signature:signature,transactionMessage:`Status: (${JSON.stringify(status)})`})}throw new Error(`Transaction ${signature} failed (${JSON.stringify(status)})`)}return signature}function sleep(ms){return new Promise((resolve=>setTimeout(resolve,ms)))}function encodeData(type,fields){const allocLength=type.layout.span>=0?type.layout.span:getAlloc(type,fields);const data=bufferExports.Buffer.alloc(allocLength);const layoutFields=Object.assign({instruction:type.index},fields);type.layout.encode(layoutFields,data);return data}function decodeData$1(type,buffer){let data;try{data=type.layout.decode(buffer)}catch(err){throw new Error("invalid instruction; "+err)}if(data.instruction!==type.index){throw new Error(`invalid instruction; instruction index mismatch ${data.instruction} != ${type.index}`)}return data}const FeeCalculatorLayout=LayoutExports.nu64("lamportsPerSignature");const NonceAccountLayout=LayoutExports.struct([LayoutExports.u32("version"),LayoutExports.u32("state"),publicKey("authorizedPubkey"),publicKey("nonce"),LayoutExports.struct([FeeCalculatorLayout],"feeCalculator")]);const NONCE_ACCOUNT_LENGTH=NonceAccountLayout.span;class NonceAccount{constructor(args){this.authorizedPubkey=void 0;this.nonce=void 0;this.feeCalculator=void 0;this.authorizedPubkey=args.authorizedPubkey;this.nonce=args.nonce;this.feeCalculator=args.feeCalculator}static fromAccountData(buffer){const nonceAccount=NonceAccountLayout.decode(toBuffer(buffer),0);return new NonceAccount({authorizedPubkey:new PublicKey(nonceAccount.authorizedPubkey),nonce:new PublicKey(nonceAccount.nonce).toString(),feeCalculator:nonceAccount.feeCalculator})}}var browser$1={};var hasRequiredBrowser$1;function requireBrowser$1(){if(hasRequiredBrowser$1)return browser$1;hasRequiredBrowser$1=1;Object.defineProperty(browser$1,"__esModule",{value:true});function toBigIntLE(buf){{const reversed=Buffer.from(buf);reversed.reverse();const hex=reversed.toString("hex");if(hex.length===0){return BigInt(0)}return BigInt(`0x${hex}`)}}browser$1.toBigIntLE=toBigIntLE;function toBigIntBE(buf){{const hex=buf.toString("hex");if(hex.length===0){return BigInt(0)}return BigInt(`0x${hex}`)}}browser$1.toBigIntBE=toBigIntBE;function toBufferLE(num,width){{const hex=num.toString(16);const buffer=Buffer.from(hex.padStart(width*2,"0").slice(0,width*2),"hex");buffer.reverse();return buffer}}browser$1.toBufferLE=toBufferLE;function toBufferBE(num,width){{const hex=num.toString(16);return Buffer.from(hex.padStart(width*2,"0").slice(0,width*2),"hex")}}browser$1.toBufferBE=toBufferBE;return browser$1}var browserExports$1=requireBrowser$1();const encodeDecode=layout=>{const decode=layout.decode.bind(layout);const encode=layout.encode.bind(layout);return{decode:decode,encode:encode}};const bigInt=length=>property=>{const layout=LayoutExports.blob(length,property);const{encode:encode,decode:decode}=encodeDecode(layout);const bigIntLayout=layout;bigIntLayout.decode=(buffer,offset)=>{const src=decode(buffer,offset);return browserExports$1.toBigIntLE(bufferExports.Buffer.from(src))};bigIntLayout.encode=(bigInt,buffer,offset)=>{const src=browserExports$1.toBufferLE(bigInt,length);return encode(src,buffer,offset)};return bigIntLayout};const u64=bigInt(8);class SystemInstruction{constructor(){}static decodeInstructionType(instruction){this.checkProgramId(instruction.programId);const instructionTypeLayout=LayoutExports.u32("instruction");const typeIndex=instructionTypeLayout.decode(instruction.data);let type;for(const[ixType,layout]of Object.entries(SYSTEM_INSTRUCTION_LAYOUTS)){if(layout.index==typeIndex){type=ixType;break}}if(!type){throw new Error("Instruction type incorrect; not a SystemInstruction")}return type}static decodeCreateAccount(instruction){this.checkProgramId(instruction.programId);this.checkKeyLength(instruction.keys,2);const{lamports:lamports,space:space,programId:programId}=decodeData$1(SYSTEM_INSTRUCTION_LAYOUTS.Create,instruction.data);return{fromPubkey:instruction.keys[0].pubkey,newAccountPubkey:instruction.keys[1].pubkey,lamports:lamports,space:space,programId:new PublicKey(programId)}}static decodeTransfer(instruction){this.checkProgramId(instruction.programId);this.checkKeyLength(instruction.keys,2);const{lamports:lamports}=decodeData$1(SYSTEM_INSTRUCTION_LAYOUTS.Transfer,instruction.data);return{fromPubkey:instruction.keys[0].pubkey,toPubkey:instruction.keys[1].pubkey,lamports:lamports}}static decodeTransferWithSeed(instruction){this.checkProgramId(instruction.programId);this.checkKeyLength(instruction.keys,3);const{lamports:lamports,seed:seed,programId:programId}=decodeData$1(SYSTEM_INSTRUCTION_LAYOUTS.TransferWithSeed,instruction.data);return{fromPubkey:instruction.keys[0].pubkey,basePubkey:instruction.keys[1].pubkey,toPubkey:instruction.keys[2].pubkey,lamports:lamports,seed:seed,programId:new PublicKey(programId)}}static decodeAllocate(instruction){this.checkProgramId(instruction.programId);this.checkKeyLength(instruction.keys,1);const{space:space}=decodeData$1(SYSTEM_INSTRUCTION_LAYOUTS.Allocate,instruction.data);return{accountPubkey:instruction.keys[0].pubkey,space:space}}static decodeAllocateWithSeed(instruction){this.checkProgramId(instruction.programId);this.checkKeyLength(instruction.keys,1);const{base:base,seed:seed,space:space,programId:programId}=decodeData$1(SYSTEM_INSTRUCTION_LAYOUTS.AllocateWithSeed,instruction.data);return{accountPubkey:instruction.keys[0].pubkey,basePubkey:new PublicKey(base),seed:seed,space:space,programId:new PublicKey(programId)}}static decodeAssign(instruction){this.checkProgramId(instruction.programId);this.checkKeyLength(instruction.keys,1);const{programId:programId}=decodeData$1(SYSTEM_INSTRUCTION_LAYOUTS.Assign,instruction.data);return{accountPubkey:instruction.keys[0].pubkey,programId:new PublicKey(programId)}}static decodeAssignWithSeed(instruction){this.checkProgramId(instruction.programId);this.checkKeyLength(instruction.keys,1);const{base:base,seed:seed,programId:programId}=decodeData$1(SYSTEM_INSTRUCTION_LAYOUTS.AssignWithSeed,instruction.data);return{accountPubkey:instruction.keys[0].pubkey,basePubkey:new PublicKey(base),seed:seed,programId:new PublicKey(programId)}}static decodeCreateWithSeed(instruction){this.checkProgramId(instruction.programId);this.checkKeyLength(instruction.keys,2);const{base:base,seed:seed,lamports:lamports,space:space,programId:programId}=decodeData$1(SYSTEM_INSTRUCTION_LAYOUTS.CreateWithSeed,instruction.data);return{fromPubkey:instruction.keys[0].pubkey,newAccountPubkey:instruction.keys[1].pubkey,basePubkey:new PublicKey(base),seed:seed,lamports:lamports,space:space,programId:new PublicKey(programId)}}static decodeNonceInitialize(instruction){this.checkProgramId(instruction.programId);this.checkKeyLength(instruction.keys,3);const{authorized:authorized}=decodeData$1(SYSTEM_INSTRUCTION_LAYOUTS.InitializeNonceAccount,instruction.data);return{noncePubkey:instruction.keys[0].pubkey,authorizedPubkey:new PublicKey(authorized)}}static decodeNonceAdvance(instruction){this.checkProgramId(instruction.programId);this.checkKeyLength(instruction.keys,3);decodeData$1(SYSTEM_INSTRUCTION_LAYOUTS.AdvanceNonceAccount,instruction.data);return{noncePubkey:instruction.keys[0].pubkey,authorizedPubkey:instruction.keys[2].pubkey}}static decodeNonceWithdraw(instruction){this.checkProgramId(instruction.programId);this.checkKeyLength(instruction.keys,5);const{lamports:lamports}=decodeData$1(SYSTEM_INSTRUCTION_LAYOUTS.WithdrawNonceAccount,instruction.data);return{noncePubkey:instruction.keys[0].pubkey,toPubkey:instruction.keys[1].pubkey,authorizedPubkey:instruction.keys[4].pubkey,lamports:lamports}}static decodeNonceAuthorize(instruction){this.checkProgramId(instruction.programId);this.checkKeyLength(instruction.keys,2);const{authorized:authorized}=decodeData$1(SYSTEM_INSTRUCTION_LAYOUTS.AuthorizeNonceAccount,instruction.data);return{noncePubkey:instruction.keys[0].pubkey,authorizedPubkey:instruction.keys[1].pubkey,newAuthorizedPubkey:new PublicKey(authorized)}}static checkProgramId(programId){if(!programId.equals(SystemProgram.programId)){throw new Error("invalid instruction; programId is not SystemProgram")}}static checkKeyLength(keys,expectedLength){if(keys.length<expectedLength){throw new Error(`invalid instruction; found ${keys.length} keys, expected at least ${expectedLength}`)}}}const SYSTEM_INSTRUCTION_LAYOUTS=Object.freeze({Create:{index:0,layout:LayoutExports.struct([LayoutExports.u32("instruction"),LayoutExports.ns64("lamports"),LayoutExports.ns64("space"),publicKey("programId")])},Assign:{index:1,layout:LayoutExports.struct([LayoutExports.u32("instruction"),publicKey("programId")])},Transfer:{index:2,layout:LayoutExports.struct([LayoutExports.u32("instruction"),u64("lamports")])},CreateWithSeed:{index:3,layout:LayoutExports.struct([LayoutExports.u32("instruction"),publicKey("base"),rustString("seed"),LayoutExports.ns64("lamports"),LayoutExports.ns64("space"),publicKey("programId")])},AdvanceNonceAccount:{index:4,layout:LayoutExports.struct([LayoutExports.u32("instruction")])},WithdrawNonceAccount:{index:5,layout:LayoutExports.struct([LayoutExports.u32("instruction"),LayoutExports.ns64("lamports")])},InitializeNonceAccount:{index:6,layout:LayoutExports.struct([LayoutExports.u32("instruction"),publicKey("authorized")])},AuthorizeNonceAccount:{index:7,layout:LayoutExports.struct([LayoutExports.u32("instruction"),publicKey("authorized")])},Allocate:{index:8,layout:LayoutExports.struct([LayoutExports.u32("instruction"),LayoutExports.ns64("space")])},AllocateWithSeed:{index:9,layout:LayoutExports.struct([LayoutExports.u32("instruction"),publicKey("base"),rustString("seed"),LayoutExports.ns64("space"),publicKey("programId")])},AssignWithSeed:{index:10,layout:LayoutExports.struct([LayoutExports.u32("instruction"),publicKey("base"),rustString("seed"),publicKey("programId")])},TransferWithSeed:{index:11,layout:LayoutExports.struct([LayoutExports.u32("instruction"),u64("lamports"),rustString("seed"),publicKey("programId")])},UpgradeNonceAccount:{index:12,layout:LayoutExports.struct([LayoutExports.u32("instruction")])}});class SystemProgram{constructor(){}static createAccount(params){const type=SYSTEM_INSTRUCTION_LAYOUTS.Create;const data=encodeData(type,{lamports:params.lamports,space:params.space,programId:toBuffer(params.programId.toBuffer())});return new TransactionInstruction({keys:[{pubkey:params.fromPubkey,isSigner:true,isWritable:true},{pubkey:params.newAccountPubkey,isSigner:true,isWritable:true}],programId:this.programId,data:data})}static transfer(params){let data;let keys;if("basePubkey"in params){const type=SYSTEM_INSTRUCTION_LAYOUTS.TransferWithSeed;data=encodeData(type,{lamports:BigInt(params.lamports),seed:params.seed,programId:toBuffer(params.programId.toBuffer())});keys=[{pubkey:params.fromPubkey,isSigner:false,isWritable:true},{pubkey:params.basePubkey,isSigner:true,isWritable:false},{pubkey:params.toPubkey,isSigner:false,isWritable:true}]}else{const type=SYSTEM_INSTRUCTION_LAYOUTS.Transfer;data=encodeData(type,{lamports:BigInt(params.lamports)});keys=[{pubkey:params.fromPubkey,isSigner:true,isWritable:true},{pubkey:params.toPubkey,isSigner:false,isWritable:true}]}return new TransactionInstruction({keys:keys,programId:this.programId,data:data})}static assign(params){let data;let keys;if("basePubkey"in params){const type=SYSTEM_INSTRUCTION_LAYOUTS.AssignWithSeed;data=encodeData(type,{base:toBuffer(params.basePubkey.toBuffer()),seed:params.seed,programId:toBuffer(params.programId.toBuffer())});keys=[{pubkey:params.accountPubkey,isSigner:false,isWritable:true},{pubkey:params.basePubkey,isSigner:true,isWritable:false}]}else{const type=SYSTEM_INSTRUCTION_LAYOUTS.Assign;data=encodeData(type,{programId:toBuffer(params.programId.toBuffer())});keys=[{pubkey:params.accountPubkey,isSigner:true,isWritable:true}]}return new TransactionInstruction({keys:keys,programId:this.programId,data:data})}static createAccountWithSeed(params){const type=SYSTEM_INSTRUCTION_LAYOUTS.CreateWithSeed;const data=encodeData(type,{base:toBuffer(params.basePubkey.toBuffer()),seed:params.seed,lamports:params.lamports,space:params.space,programId:toBuffer(params.programId.toBuffer())});let keys=[{pubkey:params.fromPubkey,isSigner:true,isWritable:true},{pubkey:params.newAccountPubkey,isSigner:false,isWritable:true}];if(!params.basePubkey.equals(params.fromPubkey)){keys.push({pubkey:params.basePubkey,isSigner:true,isWritable:false})}return new TransactionInstruction({keys:keys,programId:this.programId,data:data})}static createNonceAccount(params){const transaction=new Transaction;if("basePubkey"in params&&"seed"in params){transaction.add(SystemProgram.createAccountWithSeed({fromPubkey:params.fromPubkey,newAccountPubkey:params.noncePubkey,basePubkey:params.basePubkey,seed:params.seed,lamports:params.lamports,space:NONCE_ACCOUNT_LENGTH,programId:this.programId}))}else{transaction.add(SystemProgram.createAccount({fromPubkey:params.fromPubkey,newAccountPubkey:params.noncePubkey,lamports:params.lamports,space:NONCE_ACCOUNT_LENGTH,programId:this.programId}))}const initParams={noncePubkey:params.noncePubkey,authorizedPubkey:params.authorizedPubkey};transaction.add(this.nonceInitialize(initParams));return transaction}static nonceInitialize(params){const type=SYSTEM_INSTRUCTION_LAYOUTS.InitializeNonceAccount;const data=encodeData(type,{authorized:toBuffer(params.authorizedPubkey.toBuffer())});const instructionData={keys:[{pubkey:params.noncePubkey,isSigner:false,isWritable:true},{pubkey:SYSVAR_RECENT_BLOCKHASHES_PUBKEY,isSigner:false,isWritable:false},{pubkey:SYSVAR_RENT_PUBKEY,isSigner:false,isWritable:false}],programId:this.programId,data:data};return new TransactionInstruction(instructionData)}static nonceAdvance(params){const type=SYSTEM_INSTRUCTION_LAYOUTS.AdvanceNonceAccount;const data=encodeData(type);const instructionData={keys:[{pubkey:params.noncePubkey,isSigner:false,isWritable:true},{pubkey:SYSVAR_RECENT_BLOCKHASHES_PUBKEY,isSigner:false,isWritable:false},{pubkey:params.authorizedPubkey,isSigner:true,isWritable:false}],programId:this.programId,data:data};return new TransactionInstruction(instructionData)}static nonceWithdraw(params){const type=SYSTEM_INSTRUCTION_LAYOUTS.WithdrawNonceAccount;const data=encodeData(type,{lamports:params.lamports});return new TransactionInstruction({keys:[{pubkey:params.noncePubkey,isSigner:false,isWritable:true},{pubkey:params.toPubkey,isSigner:false,isWritable:true},{pubkey:SYSVAR_RECENT_BLOCKHASHES_PUBKEY,isSigner:false,isWritable:false},{pubkey:SYSVAR_RENT_PUBKEY,isSigner:false,isWritable:false},{pubkey:params.authorizedPubkey,isSigner:true,isWritable:false}],programId:this.programId,data:data})}static nonceAuthorize(params){const type=SYSTEM_INSTRUCTION_LAYOUTS.AuthorizeNonceAccount;const data=encodeData(type,{authorized:toBuffer(params.newAuthorizedPubkey.toBuffer())});return new TransactionInstruction({keys:[{pubkey:params.noncePubkey,isSigner:false,isWritable:true},{pubkey:params.authorizedPubkey,isSigner:true,isWritable:false}],programId:this.programId,data:data})}static allocate(params){let data;let keys;if("basePubkey"in params){const type=SYSTEM_INSTRUCTION_LAYOUTS.AllocateWithSeed;data=encodeData(type,{base:toBuffer(params.basePubkey.toBuffer()),seed:params.seed,space:params.space,programId:toBuffer(params.programId.toBuffer())});keys=[{pubkey:params.accountPubkey,isSigner:false,isWritable:true},{pubkey:params.basePubkey,isSigner:true,isWritable:false}]}else{const type=SYSTEM_INSTRUCTION_LAYOUTS.Allocate;data=encodeData(type,{space:params.space});keys=[{pubkey:params.accountPubkey,isSigner:true,isWritable:true}]}return new TransactionInstruction({keys:keys,programId:this.programId,data:data})}}SystemProgram.programId=new PublicKey("11111111111111111111111111111111");const CHUNK_SIZE=PACKET_DATA_SIZE-300;class Loader{constructor(){}static getMinNumSignatures(dataLength){return 2*(Math.ceil(dataLength/Loader.chunkSize)+1+1)}static async load(connection,payer,program,programId,data){{const balanceNeeded=await connection.getMinimumBalanceForRentExemption(data.length);const programInfo=await connection.getAccountInfo(program.publicKey,"confirmed");let transaction=null;if(programInfo!==null){if(programInfo.executable){console.error("Program load failed, account is already executable");return false}if(programInfo.data.length!==data.length){transaction=transaction||new Transaction;transaction.add(SystemProgram.allocate({accountPubkey:program.publicKey,space:data.length}))}if(!programInfo.owner.equals(programId)){transaction=transaction||new Transaction;transaction.add(SystemProgram.assign({accountPubkey:program.publicKey,programId:programId}))}if(programInfo.lamports<balanceNeeded){transaction=transaction||new Transaction;transaction.add(SystemProgram.transfer({fromPubkey:payer.publicKey,toPubkey:program.publicKey,lamports:balanceNeeded-programInfo.lamports}))}}else{transaction=(new Transaction).add(SystemProgram.createAccount({fromPubkey:payer.publicKey,newAccountPubkey:program.publicKey,lamports:balanceNeeded>0?balanceNeeded:1,space:data.length,programId:programId}))}if(transaction!==null){await sendAndConfirmTransaction(connection,transaction,[payer,program],{commitment:"confirmed"})}}const dataLayout=LayoutExports.struct([LayoutExports.u32("instruction"),LayoutExports.u32("offset"),LayoutExports.u32("bytesLength"),LayoutExports.u32("bytesLengthPadding"),LayoutExports.seq(LayoutExports.u8("byte"),LayoutExports.offset(LayoutExports.u32(),-8),"bytes")]);const chunkSize=Loader.chunkSize;let offset=0;let array=data;let transactions=[];while(array.length>0){const bytes=array.slice(0,chunkSize);const data=bufferExports.Buffer.alloc(chunkSize+16);dataLayout.encode({instruction:0,offset:offset,bytes:bytes,bytesLength:0,bytesLengthPadding:0},data);const transaction=(new Transaction).add({keys:[{pubkey:program.publicKey,isSigner:true,isWritable:true}],programId:programId,data:data});transactions.push(sendAndConfirmTransaction(connection,transaction,[payer,program],{commitment:"confirmed"}));if(connection._rpcEndpoint.includes("solana.com")){const REQUESTS_PER_SECOND=4;await sleep(1e3/REQUESTS_PER_SECOND)}offset+=chunkSize;array=array.slice(chunkSize)}await Promise.all(transactions);{const dataLayout=LayoutExports.struct([LayoutExports.u32("instruction")]);const data=bufferExports.Buffer.alloc(dataLayout.span);dataLayout.encode({instruction:1},data);const transaction=(new Transaction).add({keys:[{pubkey:program.publicKey,isSigner:true,isWritable:true},{pubkey:SYSVAR_RENT_PUBKEY,isSigner:false,isWritable:false}],programId:programId,data:data});const deployCommitment="processed";const finalizeSignature=await connection.sendTransaction(transaction,[payer,program],{preflightCommitment:deployCommitment});const{context:context,value:value}=await connection.confirmTransaction({signature:finalizeSignature,lastValidBlockHeight:transaction.lastValidBlockHeight,blockhash:transaction.recentBlockhash},deployCommitment);if(value.err){throw new Error(`Transaction ${finalizeSignature} failed (${JSON.stringify(value)})`)}while(true){try{const currentSlot=await connection.getSlot({commitment:deployCommitment});if(currentSlot>context.slot){break}}catch{}await new Promise((resolve=>setTimeout(resolve,Math.round(MS_PER_SLOT/2))))}}return true}}Loader.chunkSize=CHUNK_SIZE;const BPF_LOADER_PROGRAM_ID=new PublicKey("BPFLoader2111111111111111111111111111111111");class BpfLoader{static getMinNumSignatures(dataLength){return Loader.getMinNumSignatures(dataLength)}static load(connection,payer,program,elf,loaderProgramId){return Loader.load(connection,payer,program,loaderProgramId,elf)}}var fastStableStringify$1;var hasRequiredFastStableStringify;function requireFastStableStringify(){if(hasRequiredFastStableStringify)return fastStableStringify$1;hasRequiredFastStableStringify=1;var objToString=Object.prototype.toString;var objKeys=Object.keys||function(obj){var keys=[];for(var name in obj){keys.push(name)}return keys};function stringify(val,isArrayProp){var i,max,str,keys,key,propVal,toStr;if(val===true){return"true"}if(val===false){return"false"}switch(typeof val){case"object":if(val===null){return null}else if(val.toJSON&&typeof val.toJSON==="function"){return stringify(val.toJSON(),isArrayProp)}else{toStr=objToString.call(val);if(toStr==="[object Array]"){str="[";max=val.length-1;for(i=0;i<max;i++){str+=stringify(val[i],true)+","}if(max>-1){str+=stringify(val[i],true)}return str+"]"}else if(toStr==="[object Object]"){keys=objKeys(val).sort();max=keys.length;str="";i=0;while(i<max){key=keys[i];propVal=stringify(val[key],false);if(propVal!==undefined){if(str){str+=","}str+=JSON.stringify(key)+":"+propVal}i++}return"{"+str+"}"}else{return JSON.stringify(val)}}case"function":case"undefined":return isArrayProp?null:undefined;case"string":return JSON.stringify(val);default:return isFinite(val)?val:null}}fastStableStringify$1=function(val){var returnVal=stringify(val,false);if(returnVal!==undefined){return""+returnVal}};return fastStableStringify$1}var fastStableStringifyExports=requireFastStableStringify();var fastStableStringify=getDefaultExportFromCjs(fastStableStringifyExports);class StructError extends TypeError{constructor(failure,failures){let cached;const{message:message,explanation:explanation,...rest}=failure;const{path:path}=failure;const msg=path.length===0?message:`At path: ${path.join(".")} -- ${message}`;super(explanation??msg);if(explanation!=null)this.cause=msg;Object.assign(this,rest);this.name=this.constructor.name;this.failures=()=>cached??(cached=[failure,...failures()])}}function isIterable(x){return isObject(x)&&typeof x[Symbol.iterator]==="function"}function isObject(x){return typeof x==="object"&&x!=null}function isNonArrayObject(x){return isObject(x)&&!Array.isArray(x)}function print(value){if(typeof value==="symbol"){return value.toString()}return typeof value==="string"?JSON.stringify(value):`${value}`}function shiftIterator(input){const{done:done,value:value}=input.next();return done?undefined:value}function toFailure(result,context,struct,value){if(result===true){return}else if(result===false){result={}}else if(typeof result==="string"){result={message:result}}const{path:path,branch:branch}=context;const{type:type}=struct;const{refinement:refinement,message:message=`Expected a value of type \`${type}\`${refinement?` with refinement \`${refinement}\``:""}, but received: \`${print(value)}\``}=result;return{value:value,type:type,refinement:refinement,key:path[path.length-1],path:path,branch:branch,...result,message:message}}function*toFailures(result,context,struct,value){if(!isIterable(result)){result=[result]}for(const r of result){const failure=toFailure(r,context,struct,value);if(failure){yield failure}}}function*run(value,struct,options={}){const{path:path=[],branch:branch=[value],coerce:coerce=false,mask:mask=false}=options;const ctx={path:path,branch:branch,mask:mask};if(coerce){value=struct.coercer(value,ctx)}let status="valid";for(const failure of struct.validator(value,ctx)){failure.explanation=options.message;status="not_valid";yield[failure,undefined]}for(let[k,v,s]of struct.entries(value,ctx)){const ts=run(v,s,{path:k===undefined?path:[...path,k],branch:k===undefined?branch:[...branch,v],coerce:coerce,mask:mask,message:options.message});for(const t of ts){if(t[0]){status=t[0].refinement!=null?"not_refined":"not_valid";yield[t[0],undefined]}else if(coerce){v=t[1];if(k===undefined){value=v}else if(value instanceof Map){value.set(k,v)}else if(value instanceof Set){value.add(v)}else if(isObject(value)){if(v!==undefined||k in value)value[k]=v}}}}if(status!=="not_valid"){for(const failure of struct.refiner(value,ctx)){failure.explanation=options.message;status="not_refined";yield[failure,undefined]}}if(status==="valid"){yield[undefined,value]}}class Struct{constructor(props){const{type:type,schema:schema,validator:validator,refiner:refiner,coercer:coercer=(value=>value),entries:entries=function*(){}}=props;this.type=type;this.schema=schema;this.entries=entries;this.coercer=coercer;if(validator){this.validator=(value,context)=>{const result=validator(value,context);return toFailures(result,context,this,value)}}else{this.validator=()=>[]}if(refiner){this.refiner=(value,context)=>{const result=refiner(value,context);return toFailures(result,context,this,value)}}else{this.refiner=()=>[]}}assert(value,message){return assert(value,this,message)}create(value,message){return create(value,this,message)}is(value){return is(value,this)}mask(value,message){return mask(value,this,message)}validate(value,options={}){return validate$1(value,this,options)}}function assert(value,struct,message){const result=validate$1(value,struct,{message:message});if(result[0]){throw result[0]}}function create(value,struct,message){const result=validate$1(value,struct,{coerce:true,message:message});if(result[0]){throw result[0]}else{return result[1]}}function mask(value,struct,message){const result=validate$1(value,struct,{coerce:true,mask:true,message:message});if(result[0]){throw result[0]}else{return result[1]}}function is(value,struct){const result=validate$1(value,struct);return!result[0]}function validate$1(value,struct,options={}){const tuples=run(value,struct,options);const tuple=shiftIterator(tuples);if(tuple[0]){const error=new StructError(tuple[0],(function*(){for(const t of tuples){if(t[0]){yield t[0]}}}));return[error,undefined]}else{const v=tuple[1];return[undefined,v]}}function define(name,validator){return new Struct({type:name,schema:null,validator:validator})}function any(){return define("any",(()=>true))}function array(Element){return new Struct({type:"array",schema:Element,*entries(value){if(Element&&Array.isArray(value)){for(const[i,v]of value.entries()){yield[i,v,Element]}}},coercer(value){return Array.isArray(value)?value.slice():value},validator(value){return Array.isArray(value)||`Expected an array value, but received: ${print(value)}`}})}function boolean(){return define("boolean",(value=>typeof value==="boolean"))}function instance(Class){return define("instance",(value=>value instanceof Class||`Expected a \`${Class.name}\` instance, but received: ${print(value)}`))}function literal(constant){const description=print(constant);const t=typeof constant;return new Struct({type:"literal",schema:t==="string"||t==="number"||t==="boolean"?constant:null,validator(value){return value===constant||`Expected the literal \`${description}\`, but received: ${print(value)}`}})}function never(){return define("never",(()=>false))}function nullable(struct){return new Struct({...struct,validator:(value,ctx)=>value===null||struct.validator(value,ctx),refiner:(value,ctx)=>value===null||struct.refiner(value,ctx)})}function number(){return define("number",(value=>typeof value==="number"&&!isNaN(value)||`Expected a number, but received: ${print(value)}`))}function optional(struct){return new Struct({...struct,validator:(value,ctx)=>value===undefined||struct.validator(value,ctx),refiner:(value,ctx)=>value===undefined||struct.refiner(value,ctx)})}function record(Key,Value){return new Struct({type:"record",schema:null,*entries(value){if(isObject(value)){for(const k in value){const v=value[k];yield[k,k,Key];yield[k,v,Value]}}},validator(value){return isNonArrayObject(value)||`Expected an object, but received: ${print(value)}`},coercer(value){return isNonArrayObject(value)?{...value}:value}})}function string(){return define("string",(value=>typeof value==="string"||`Expected a string, but received: ${print(value)}`))}function tuple(Structs){const Never=never();return new Struct({type:"tuple",schema:null,*entries(value){if(Array.isArray(value)){const length=Math.max(Structs.length,value.length);for(let i=0;i<length;i++){yield[i,value[i],Structs[i]||Never]}}},validator(value){return Array.isArray(value)||`Expected an array, but received: ${print(value)}`},coercer(value){return Array.isArray(value)?value.slice():value}})}function type(schema){const keys=Object.keys(schema);return new Struct({type:"type",schema:schema,*entries(value){if(isObject(value)){for(const k of keys){yield[k,value[k],schema[k]]}}},validator(value){return isNonArrayObject(value)||`Expected an object, but received: ${print(value)}`},coercer(value){return isNonArrayObject(value)?{...value}:value}})}function union(Structs){const description=Structs.map((s=>s.type)).join(" | ");return new Struct({type:"union",schema:null,coercer(value,ctx){for(const S of Structs){const[error,coerced]=S.validate(value,{coerce:true,mask:ctx.mask});if(!error){return coerced}}return value},validator(value,ctx){const failures=[];for(const S of Structs){const[...tuples]=run(value,S,ctx);const[first]=tuples;if(!first[0]){return[]}else{for(const[failure]of tuples){if(failure){failures.push(failure)}}}}return[`Expected the value to satisfy a union of \`${description}\`, but received: ${print(value)}`,...failures]}})}function unknown(){return define("unknown",(()=>true))}function coerce(struct,condition,coercer){return new Struct({...struct,coercer:(value,ctx)=>is(value,condition)?struct.coercer(coercer(value,ctx),ctx):struct.coercer(value,ctx)})}var getRandomValues;var rnds8=new Uint8Array(16);function rng(){if(!getRandomValues){getRandomValues=typeof crypto!=="undefined"&&crypto.getRandomValues&&crypto.getRandomValues.bind(crypto)||typeof msCrypto!=="undefined"&&typeof msCrypto.getRandomValues==="function"&&msCrypto.getRandomValues.bind(msCrypto);if(!getRandomValues){throw new Error("crypto.getRandomValues() not supported. See https://github.com/uuidjs/uuid#getrandomvalues-not-supported")}}return getRandomValues(rnds8)}var REGEX=/^(?:[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}|00000000-0000-0000-0000-000000000000)$/i;function validate(uuid){return typeof uuid==="string"&&REGEX.test(uuid)}var byteToHex=[];for(var i=0;i<256;++i){byteToHex.push((i+256).toString(16).substr(1))}function stringify(arr){var offset=arguments.length>1&&arguments[1]!==undefined?arguments[1]:0;var uuid=(byteToHex[arr[offset+0]]+byteToHex[arr[offset+1]]+byteToHex[arr[offset+2]]+byteToHex[arr[offset+3]]+"-"+byteToHex[arr[offset+4]]+byteToHex[arr[offset+5]]+"-"+byteToHex[arr[offset+6]]+byteToHex[arr[offset+7]]+"-"+byteToHex[arr[offset+8]]+byteToHex[arr[offset+9]]+"-"+byteToHex[arr[offset+10]]+byteToHex[arr[offset+11]]+byteToHex[arr[offset+12]]+byteToHex[arr[offset+13]]+byteToHex[arr[offset+14]]+byteToHex[arr[offset+15]]).toLowerCase();if(!validate(uuid)){throw TypeError("Stringified UUID is invalid")}return uuid}var _nodeId;var _clockseq;var _lastMSecs=0;var _lastNSecs=0;function v1(options,buf,offset){var i=buf&&offset||0;var b=buf||new Array(16);options=options||{};var node=options.node||_nodeId;var clockseq=options.clockseq!==undefined?options.clockseq:_clockseq;if(node==null||clockseq==null){var seedBytes=options.random||(options.rng||rng)();if(node==null){node=_nodeId=[seedBytes[0]|1,seedBytes[1],seedBytes[2],seedBytes[3],seedBytes[4],seedBytes[5]]}if(clockseq==null){clockseq=_clockseq=(seedBytes[6]<<8|seedBytes[7])&16383}}var msecs=options.msecs!==undefined?options.msecs:Date.now();var nsecs=options.nsecs!==undefined?options.nsecs:_lastNSecs+1;var dt=msecs-_lastMSecs+(nsecs-_lastNSecs)/1e4;if(dt<0&&options.clockseq===undefined){clockseq=clockseq+1&16383}if((dt<0||msecs>_lastMSecs)&&options.nsecs===undefined){nsecs=0}if(nsecs>=1e4){throw new Error("uuid.v1(): Can't create more than 10M uuids/sec")}_lastMSecs=msecs;_lastNSecs=nsecs;_clockseq=clockseq;msecs+=122192928e5;var tl=((msecs&268435455)*1e4+nsecs)%4294967296;b[i++]=tl>>>24&255;b[i++]=tl>>>16&255;b[i++]=tl>>>8&255;b[i++]=tl&255;var tmh=msecs/4294967296*1e4&268435455;b[i++]=tmh>>>8&255;b[i++]=tmh&255;b[i++]=tmh>>>24&15|16;b[i++]=tmh>>>16&255;b[i++]=clockseq>>>8|128;b[i++]=clockseq&255;for(var n=0;n<6;++n){b[i+n]=node[n]}return buf||stringify(b)}function parse(uuid){if(!validate(uuid)){throw TypeError("Invalid UUID")}var v;var arr=new Uint8Array(16);arr[0]=(v=parseInt(uuid.slice(0,8),16))>>>24;arr[1]=v>>>16&255;arr[2]=v>>>8&255;arr[3]=v&255;arr[4]=(v=parseInt(uuid.slice(9,13),16))>>>8;arr[5]=v&255;arr[6]=(v=parseInt(uuid.slice(14,18),16))>>>8;arr[7]=v&255;arr[8]=(v=parseInt(uuid.slice(19,23),16))>>>8;arr[9]=v&255;arr[10]=(v=parseInt(uuid.slice(24,36),16))/1099511627776&255;arr[11]=v/4294967296&255;arr[12]=v>>>24&255;arr[13]=v>>>16&255;arr[14]=v>>>8&255;arr[15]=v&255;return arr}function stringToBytes(str){str=unescape(encodeURIComponent(str));var bytes=[];for(var i=0;i<str.length;++i){bytes.push(str.charCodeAt(i))}return bytes}var DNS="6ba7b810-9dad-11d1-80b4-00c04fd430c8";var URL="6ba7b811-9dad-11d1-80b4-00c04fd430c8";function v35(name,version,hashfunc){function generateUUID(value,namespace,buf,offset){if(typeof value==="string"){value=stringToBytes(value)}if(typeof namespace==="string"){namespace=parse(namespace)}if(namespace.length!==16){throw TypeError("Namespace must be array-like (16 iterable integer values, 0-255)")}var bytes=new Uint8Array(16+value.length);bytes.set(namespace);bytes.set(value,namespace.length);bytes=hashfunc(bytes);bytes[6]=bytes[6]&15|version;bytes[8]=bytes[8]&63|128;if(buf){offset=offset||0;for(var i=0;i<16;++i){buf[offset+i]=bytes[i]}return buf}return stringify(bytes)}try{generateUUID.name=name}catch(err){}generateUUID.DNS=DNS;generateUUID.URL=URL;return generateUUID}function md5(bytes){if(typeof bytes==="string"){var msg=unescape(encodeURIComponent(bytes));bytes=new Uint8Array(msg.length);for(var i=0;i<msg.length;++i){bytes[i]=msg.charCodeAt(i)}}return md5ToHexEncodedArray(wordsToMd5(bytesToWords(bytes),bytes.length*8))}function md5ToHexEncodedArray(input){var output=[];var length32=input.length*32;var hexTab="0123456789abcdef";for(var i=0;i<length32;i+=8){var x=input[i>>5]>>>i%32&255;var hex=parseInt(hexTab.charAt(x>>>4&15)+hexTab.charAt(x&15),16);output.push(hex)}return output}function getOutputLength(inputLength8){return(inputLength8+64>>>9<<4)+14+1}function wordsToMd5(x,len){x[len>>5]|=128<<len%32;x[getOutputLength(len)-1]=len;var a=1732584193;var b=-271733879;var c=-1732584194;var d=271733878;for(var i=0;i<x.length;i+=16){var olda=a;var oldb=b;var oldc=c;var oldd=d;a=md5ff(a,b,c,d,x[i],7,-680876936);d=md5ff(d,a,b,c,x[i+1],12,-389564586);c=md5ff(c,d,a,b,x[i+2],17,606105819);b=md5ff(b,c,d,a,x[i+3],22,-1044525330);a=md5ff(a,b,c,d,x[i+4],7,-176418897);d=md5ff(d,a,b,c,x[i+5],12,1200080426);c=md5ff(c,d,a,b,x[i+6],17,-1473231341);b=md5ff(b,c,d,a,x[i+7],22,-45705983);a=md5ff(a,b,c,d,x[i+8],7,1770035416);d=md5ff(d,a,b,c,x[i+9],12,-1958414417);c=md5ff(c,d,a,b,x[i+10],17,-42063);b=md5ff(b,c,d,a,x[i+11],22,-1990404162);a=md5ff(a,b,c,d,x[i+12],7,1804603682);d=md5ff(d,a,b,c,x[i+13],12,-40341101);c=md5ff(c,d,a,b,x[i+14],17,-1502002290);b=md5ff(b,c,d,a,x[i+15],22,1236535329);a=md5gg(a,b,c,d,x[i+1],5,-165796510);d=md5gg(d,a,b,c,x[i+6],9,-1069501632);c=md5gg(c,d,a,b,x[i+11],14,643717713);b=md5gg(b,c,d,a,x[i],20,-373897302);a=md5gg(a,b,c,d,x[i+5],5,-701558691);d=md5gg(d,a,b,c,x[i+10],9,38016083);c=md5gg(c,d,a,b,x[i+15],14,-660478335);b=md5gg(b,c,d,a,x[i+4],20,-405537848);a=md5gg(a,b,c,d,x[i+9],5,568446438);d=md5gg(d,a,b,c,x[i+14],9,-1019803690);c=md5gg(c,d,a,b,x[i+3],14,-187363961);b=md5gg(b,c,d,a,x[i+8],20,1163531501);a=md5gg(a,b,c,d,x[i+13],5,-1444681467);d=md5gg(d,a,b,c,x[i+2],9,-51403784);c=md5gg(c,d,a,b,x[i+7],14,1735328473);b=md5gg(b,c,d,a,x[i+12],20,-1926607734);a=md5hh(a,b,c,d,x[i+5],4,-378558);d=md5hh(d,a,b,c,x[i+8],11,-2022574463);c=md5hh(c,d,a,b,x[i+11],16,1839030562);b=md5hh(b,c,d,a,x[i+14],23,-35309556);a=md5hh(a,b,c,d,x[i+1],4,-1530992060);d=md5hh(d,a,b,c,x[i+4],11,1272893353);c=md5hh(c,d,a,b,x[i+7],16,-155497632);b=md5hh(b,c,d,a,x[i+10],23,-1094730640);a=md5hh(a,b,c,d,x[i+13],4,681279174);d=md5hh(d,a,b,c,x[i],11,-358537222);c=md5hh(c,d,a,b,x[i+3],16,-722521979);b=md5hh(b,c,d,a,x[i+6],23,76029189);a=md5hh(a,b,c,d,x[i+9],4,-640364487);d=md5hh(d,a,b,c,x[i+12],11,-421815835);c=md5hh(c,d,a,b,x[i+15],16,530742520);b=md5hh(b,c,d,a,x[i+2],23,-995338651);a=md5ii(a,b,c,d,x[i],6,-198630844);d=md5ii(d,a,b,c,x[i+7],10,1126891415);c=md5ii(c,d,a,b,x[i+14],15,-1416354905);b=md5ii(b,c,d,a,x[i+5],21,-57434055);a=md5ii(a,b,c,d,x[i+12],6,1700485571);d=md5ii(d,a,b,c,x[i+3],10,-1894986606);c=md5ii(c,d,a,b,x[i+10],15,-1051523);b=md5ii(b,c,d,a,x[i+1],21,-2054922799);a=md5ii(a,b,c,d,x[i+8],6,1873313359);d=md5ii(d,a,b,c,x[i+15],10,-30611744);c=md5ii(c,d,a,b,x[i+6],15,-1560198380);b=md5ii(b,c,d,a,x[i+13],21,1309151649);a=md5ii(a,b,c,d,x[i+4],6,-145523070);d=md5ii(d,a,b,c,x[i+11],10,-1120210379);c=md5ii(c,d,a,b,x[i+2],15,718787259);b=md5ii(b,c,d,a,x[i+9],21,-343485551);a=safeAdd(a,olda);b=safeAdd(b,oldb);c=safeAdd(c,oldc);d=safeAdd(d,oldd)}return[a,b,c,d]}function bytesToWords(input){if(input.length===0){return[]}var length8=input.length*8;var output=new Uint32Array(getOutputLength(length8));for(var i=0;i<length8;i+=8){output[i>>5]|=(input[i/8]&255)<<i%32}return output}function safeAdd(x,y){var lsw=(x&65535)+(y&65535);var msw=(x>>16)+(y>>16)+(lsw>>16);return msw<<16|lsw&65535}function bitRotateLeft(num,cnt){return num<<cnt|num>>>32-cnt}function md5cmn(q,a,b,x,s,t){return safeAdd(bitRotateLeft(safeAdd(safeAdd(a,q),safeAdd(x,t)),s),b)}function md5ff(a,b,c,d,x,s,t){return md5cmn(b&c|~b&d,a,b,x,s,t)}function md5gg(a,b,c,d,x,s,t){return md5cmn(b&d|c&~d,a,b,x,s,t)}function md5hh(a,b,c,d,x,s,t){return md5cmn(b^c^d,a,b,x,s,t)}function md5ii(a,b,c,d,x,s,t){return md5cmn(c^(b|~d),a,b,x,s,t)}var v3=v35("v3",48,md5);function v4(options,buf,offset){options=options||{};var rnds=options.random||(options.rng||rng)();rnds[6]=rnds[6]&15|64;rnds[8]=rnds[8]&63|128;if(buf){offset=offset||0;for(var i=0;i<16;++i){buf[offset+i]=rnds[i]}return buf}return stringify(rnds)}function f(s,x,y,z){switch(s){case 0:return x&y^~x&z;case 1:return x^y^z;case 2:return x&y^x&z^y&z;case 3:return x^y^z}}function ROTL(x,n){return x<<n|x>>>32-n}function sha1(bytes){var K=[1518500249,1859775393,2400959708,3395469782];var H=[1732584193,4023233417,2562383102,271733878,3285377520];if(typeof bytes==="string"){var msg=unescape(encodeURIComponent(bytes));bytes=[];for(var i=0;i<msg.length;++i){bytes.push(msg.charCodeAt(i))}}else if(!Array.isArray(bytes)){bytes=Array.prototype.slice.call(bytes)}bytes.push(128);var l=bytes.length/4+2;var N=Math.ceil(l/16);var M=new Array(N);for(var _i=0;_i<N;++_i){var arr=new Uint32Array(16);for(var j=0;j<16;++j){arr[j]=bytes[_i*64+j*4]<<24|bytes[_i*64+j*4+1]<<16|bytes[_i*64+j*4+2]<<8|bytes[_i*64+j*4+3]}M[_i]=arr}M[N-1][14]=(bytes.length-1)*8/Math.pow(2,32);M[N-1][14]=Math.floor(M[N-1][14]);M[N-1][15]=(bytes.length-1)*8&4294967295;for(var _i2=0;_i2<N;++_i2){var W=new Uint32Array(80);for(var t=0;t<16;++t){W[t]=M[_i2][t]}for(var _t=16;_t<80;++_t){W[_t]=ROTL(W[_t-3]^W[_t-8]^W[_t-14]^W[_t-16],1)}var a=H[0];var b=H[1];var c=H[2];var d=H[3];var e=H[4];for(var _t2=0;_t2<80;++_t2){var s=Math.floor(_t2/20);var T=ROTL(a,5)+f(s,b,c,d)+e+K[s]+W[_t2]>>>0;e=d;d=c;c=ROTL(b,30)>>>0;b=a;a=T}H[0]=H[0]+a>>>0;H[1]=H[1]+b>>>0;H[2]=H[2]+c>>>0;H[3]=H[3]+d>>>0;H[4]=H[4]+e>>>0}return[H[0]>>24&255,H[0]>>16&255,H[0]>>8&255,H[0]&255,H[1]>>24&255,H[1]>>16&255,H[1]>>8&255,H[1]&255,H[2]>>24&255,H[2]>>16&255,H[2]>>8&255,H[2]&255,H[3]>>24&255,H[3]>>16&255,H[3]>>8&255,H[3]&255,H[4]>>24&255,H[4]>>16&255,H[4]>>8&255,H[4]&255]}var v5=v35("v5",80,sha1);var nil="00000000-0000-0000-0000-000000000000";function version(uuid){if(!validate(uuid)){throw TypeError("Invalid UUID")}return parseInt(uuid.substr(14,1),16)}var esmBrowser=Object.freeze({__proto__:null,NIL:nil,parse:parse,stringify:stringify,v1:v1,v3:v3,v4:v4,v5:v5,validate:validate,version:version});var require$$0=getAugmentedNamespace(esmBrowser);var generateRequest_1;var hasRequiredGenerateRequest;function requireGenerateRequest(){if(hasRequiredGenerateRequest)return generateRequest_1;hasRequiredGenerateRequest=1;const uuid=require$$0.v4;const generateRequest=function(method,params,id,options){if(typeof method!=="string"){throw new TypeError(method+" must be a string")}options=options||{};const version=typeof options.version==="number"?options.version:2;if(version!==1&&version!==2){throw new TypeError(version+" must be 1 or 2")}const request={method:method};if(version===2){request.jsonrpc="2.0"}if(params){if(typeof params!=="object"&&!Array.isArray(params)){throw new TypeError(params+" must be an object, array or omitted")}request.params=params}if(typeof id==="undefined"){const generator=typeof options.generator==="function"?options.generator:function(){return uuid()};request.id=generator(request,options)}else if(version===2&&id===null){if(options.notificationIdNull){request.id=null}}else{request.id=id}return request};generateRequest_1=generateRequest;return generateRequest_1}var browser;var hasRequiredBrowser;function requireBrowser(){if(hasRequiredBrowser)return browser;hasRequiredBrowser=1;const uuid=require$$0.v4;const generateRequest=requireGenerateRequest();const ClientBrowser=function(callServer,options){if(!(this instanceof ClientBrowser)){return new ClientBrowser(callServer,options)}if(!options){options={}}this.options={reviver:typeof options.reviver!=="undefined"?options.reviver:null,replacer:typeof options.replacer!=="undefined"?options.replacer:null,generator:typeof options.generator!=="undefined"?options.generator:function(){return uuid()},version:typeof options.version!=="undefined"?options.version:2,notificationIdNull:typeof options.notificationIdNull==="boolean"?options.notificationIdNull:false};this.callServer=callServer};browser=ClientBrowser;ClientBrowser.prototype.request=function(method,params,id,callback){const self=this;let request=null;const isBatch=Array.isArray(method)&&typeof params==="function";if(this.options.version===1&&isBatch){throw new TypeError("JSON-RPC 1.0 does not support batching")}const isRaw=!isBatch&&method&&typeof method==="object"&&typeof params==="function";if(isBatch||isRaw){callback=params;request=method}else{if(typeof id==="function"){callback=id;id=undefined}const hasCallback=typeof callback==="function";try{request=generateRequest(method,params,id,{generator:this.options.generator,version:this.options.version,notificationIdNull:this.options.notificationIdNull})}catch(err){if(hasCallback){return callback(err)}throw err}if(!hasCallback){return request}}let message;try{message=JSON.stringify(request,this.options.replacer)}catch(err){return callback(err)}this.callServer(message,(function(err,response){self._parseResponse(err,response,callback)}));return request};ClientBrowser.prototype._parseResponse=function(err,responseText,callback){if(err){callback(err);return}if(!responseText){return callback()}let response;try{response=JSON.parse(responseText,this.options.reviver)}catch(err){return callback(err)}if(callback.length===3){if(Array.isArray(response)){const isError=function(res){return typeof res.error!=="undefined"};const isNotError=function(res){return!isError(res)};return callback(null,response.filter(isError),response.filter(isNotError))}else{return callback(null,response.error,response.result)}}callback(null,response)};return browser}var browserExports=requireBrowser();var RpcClient=getDefaultExportFromCjs(browserExports);const MINIMUM_SLOT_PER_EPOCH=32;function trailingZeros(n){let trailingZeros=0;while(n>1){n/=2;trailingZeros++}return trailingZeros}function nextPowerOfTwo(n){if(n===0)return 1;n--;n|=n>>1;n|=n>>2;n|=n>>4;n|=n>>8;n|=n>>16;n|=n>>32;return n+1}class EpochSchedule{constructor(slotsPerEpoch,leaderScheduleSlotOffset,warmup,firstNormalEpoch,firstNormalSlot){this.slotsPerEpoch=void 0;this.leaderScheduleSlotOffset=void 0;this.warmup=void 0;this.firstNormalEpoch=void 0;this.firstNormalSlot=void 0;this.slotsPerEpoch=slotsPerEpoch;this.leaderScheduleSlotOffset=leaderScheduleSlotOffset;this.warmup=warmup;this.firstNormalEpoch=firstNormalEpoch;this.firstNormalSlot=firstNormalSlot}getEpoch(slot){return this.getEpochAndSlotIndex(slot)[0]}getEpochAndSlotIndex(slot){if(slot<this.firstNormalSlot){const epoch=trailingZeros(nextPowerOfTwo(slot+MINIMUM_SLOT_PER_EPOCH+1))-trailingZeros(MINIMUM_SLOT_PER_EPOCH)-1;const epochLen=this.getSlotsInEpoch(epoch);const slotIndex=slot-(epochLen-MINIMUM_SLOT_PER_EPOCH);return[epoch,slotIndex]}else{const normalSlotIndex=slot-this.firstNormalSlot;const normalEpochIndex=Math.floor(normalSlotIndex/this.slotsPerEpoch);const epoch=this.firstNormalEpoch+normalEpochIndex;const slotIndex=normalSlotIndex%this.slotsPerEpoch;return[epoch,slotIndex]}}getFirstSlotInEpoch(epoch){if(epoch<=this.firstNormalEpoch){return(Math.pow(2,epoch)-1)*MINIMUM_SLOT_PER_EPOCH}else{return(epoch-this.firstNormalEpoch)*this.slotsPerEpoch+this.firstNormalSlot}}getLastSlotInEpoch(epoch){return this.getFirstSlotInEpoch(epoch)+this.getSlotsInEpoch(epoch)-1}getSlotsInEpoch(epoch){if(epoch<this.firstNormalEpoch){return Math.pow(2,epoch+trailingZeros(MINIMUM_SLOT_PER_EPOCH))}else{return this.slotsPerEpoch}}}var fetchImpl=globalThis.fetch;var eventemitter3={exports:{}};var hasRequiredEventemitter3;function requireEventemitter3(){if(hasRequiredEventemitter3)return eventemitter3.exports;hasRequiredEventemitter3=1;(function(module){var has=Object.prototype.hasOwnProperty,prefix="~";function Events(){}if(Object.create){Events.prototype=Object.create(null);if(!(new Events).__proto__)prefix=false}function EE(fn,context,once){this.fn=fn;this.context=context;this.once=once||false}function addListener(emitter,event,fn,context,once){if(typeof fn!=="function"){throw new TypeError("The listener must be a function")}var listener=new EE(fn,context||emitter,once),evt=prefix?prefix+event:event;if(!emitter._events[evt])emitter._events[evt]=listener,emitter._eventsCount++;else if(!emitter._events[evt].fn)emitter._events[evt].push(listener);else emitter._events[evt]=[emitter._events[evt],listener];return emitter}function clearEvent(emitter,evt){if(--emitter._eventsCount===0)emitter._events=new Events;else delete emitter._events[evt]}function EventEmitter(){this._events=new Events;this._eventsCount=0}EventEmitter.prototype.eventNames=function eventNames(){var names=[],events,name;if(this._eventsCount===0)return names;for(name in events=this._events){if(has.call(events,name))names.push(prefix?name.slice(1):name)}if(Object.getOwnPropertySymbols){return names.concat(Object.getOwnPropertySymbols(events))}return names};EventEmitter.prototype.listeners=function listeners(event){var evt=prefix?prefix+event:event,handlers=this._events[evt];if(!handlers)return[];if(handlers.fn)return[handlers.fn];for(var i=0,l=handlers.length,ee=new Array(l);i<l;i++){ee[i]=handlers[i].fn}return ee};EventEmitter.prototype.listenerCount=function listenerCount(event){var evt=prefix?prefix+event:event,listeners=this._events[evt];if(!listeners)return 0;if(listeners.fn)return 1;return listeners.length};EventEmitter.prototype.emit=function emit(event,a1,a2,a3,a4,a5){var evt=prefix?prefix+event:event;if(!this._events[evt])return false;var listeners=this._events[evt],len=arguments.length,args,i;if(listeners.fn){if(listeners.once)this.removeListener(event,listeners.fn,undefined,true);switch(len){case 1:return listeners.fn.call(listeners.context),true;case 2:return listeners.fn.call(listeners.context,a1),true;case 3:return listeners.fn.call(listeners.context,a1,a2),true;case 4:return listeners.fn.call(listeners.context,a1,a2,a3),true;case 5:return listeners.fn.call(listeners.context,a1,a2,a3,a4),true;case 6:return listeners.fn.call(listeners.context,a1,a2,a3,a4,a5),true}for(i=1,args=new Array(len-1);i<len;i++){args[i-1]=arguments[i]}listeners.fn.apply(listeners.context,args)}else{var length=listeners.length,j;for(i=0;i<length;i++){if(listeners[i].once)this.removeListener(event,listeners[i].fn,undefined,true);switch(len){case 1:listeners[i].fn.call(listeners[i].context);break;case 2:listeners[i].fn.call(listeners[i].context,a1);break;case 3:listeners[i].fn.call(listeners[i].context,a1,a2);break;case 4:listeners[i].fn.call(listeners[i].context,a1,a2,a3);break;default:if(!args)for(j=1,args=new Array(len-1);j<len;j++){args[j-1]=arguments[j]}listeners[i].fn.apply(listeners[i].context,args)}}}return true};EventEmitter.prototype.on=function on(event,fn,context){return addListener(this,event,fn,context,false)};EventEmitter.prototype.once=function once(event,fn,context){return addListener(this,event,fn,context,true)};EventEmitter.prototype.removeListener=function removeListener(event,fn,context,once){var evt=prefix?prefix+event:event;if(!this._events[evt])return this;if(!fn){clearEvent(this,evt);return this}var listeners=this._events[evt];if(listeners.fn){if(listeners.fn===fn&&(!once||listeners.once)&&(!context||listeners.context===context)){clearEvent(this,evt)}}else{for(var i=0,events=[],length=listeners.length;i<length;i++){if(listeners[i].fn!==fn||once&&!listeners[i].once||context&&listeners[i].context!==context){events.push(listeners[i])}}if(events.length)this._events[evt]=events.length===1?events[0]:events;else clearEvent(this,evt)}return this};EventEmitter.prototype.removeAllListeners=function removeAllListeners(event){var evt;if(event){evt=prefix?prefix+event:event;if(this._events[evt])clearEvent(this,evt)}else{this._events=new Events;this._eventsCount=0}return this};EventEmitter.prototype.off=EventEmitter.prototype.removeListener;EventEmitter.prototype.addListener=EventEmitter.prototype.on;EventEmitter.prefixed=prefix;EventEmitter.EventEmitter=EventEmitter;{module.exports=EventEmitter}})(eventemitter3);return eventemitter3.exports}var eventemitter3Exports=requireEventemitter3();var EventEmitter=getDefaultExportFromCjs(eventemitter3Exports);var WebSocketBrowserImpl=class extends EventEmitter{socket;constructor(address,options,protocols){super();this.socket=new window.WebSocket(address,protocols);this.socket.onopen=()=>this.emit("open");this.socket.onmessage=event=>this.emit("message",event.data);this.socket.onerror=error=>this.emit("error",error);this.socket.onclose=event=>{this.emit("close",event.code,event.reason)}}send(data,optionsOrCallback,callback){const cb=callback||optionsOrCallback;try{this.socket.send(data);cb()}catch(error){cb(error)}}close(code,reason){this.socket.close(code,reason)}addEventListener(type,listener,options){this.socket.addEventListener(type,listener,options)}};function WebSocket(address,options){return new WebSocketBrowserImpl(address,options)}var DefaultDataPack=class{encode(value){return JSON.stringify(value)}decode(value){return JSON.parse(value)}};var CommonClient=class extends EventEmitter{address;rpc_id;queue;options;autoconnect;ready;reconnect;reconnect_timer_id;reconnect_interval;max_reconnects;rest_options;current_reconnects;generate_request_id;socket;webSocketFactory;dataPack;constructor(webSocketFactory,address="ws://localhost:8080",{autoconnect:autoconnect=true,reconnect:reconnect=true,reconnect_interval:reconnect_interval=1e3,max_reconnects:max_reconnects=5,...rest_options}={},generate_request_id,dataPack){super();this.webSocketFactory=webSocketFactory;this.queue={};this.rpc_id=0;this.address=address;this.autoconnect=autoconnect;this.ready=false;this.reconnect=reconnect;this.reconnect_timer_id=void 0;this.reconnect_interval=reconnect_interval;this.max_reconnects=max_reconnects;this.rest_options=rest_options;this.current_reconnects=0;this.generate_request_id=generate_request_id||(()=>++this.rpc_id);if(!dataPack)this.dataPack=new DefaultDataPack;else this.dataPack=dataPack;if(this.autoconnect)this._connect(this.address,{autoconnect:this.autoconnect,reconnect:this.reconnect,reconnect_interval:this.reconnect_interval,max_reconnects:this.max_reconnects,...this.rest_options})}connect(){if(this.socket)return;this._connect(this.address,{autoconnect:this.autoconnect,reconnect:this.reconnect,reconnect_interval:this.reconnect_interval,max_reconnects:this.max_reconnects,...this.rest_options})}call(method,params,timeout,ws_opts){if(!ws_opts&&"object"===typeof timeout){ws_opts=timeout;timeout=null}return new Promise(((resolve,reject)=>{if(!this.ready)return reject(new Error("socket not ready"));const rpc_id=this.generate_request_id(method,params);const message={jsonrpc:"2.0",method:method,params:params||void 0,id:rpc_id};this.socket.send(this.dataPack.encode(message),ws_opts,(error=>{if(error)return reject(error);this.queue[rpc_id]={promise:[resolve,reject]};if(timeout){this.queue[rpc_id].timeout=setTimeout((()=>{delete this.queue[rpc_id];reject(new Error("reply timeout"))}),timeout)}}))}))}async login(params){const resp=await this.call("rpc.login",params);if(!resp)throw new Error("authentication failed");return resp}async listMethods(){return await this.call("__listMethods")}notify(method,params){return new Promise(((resolve,reject)=>{if(!this.ready)return reject(new Error("socket not ready"));const message={jsonrpc:"2.0",method:method,params:params};this.socket.send(this.dataPack.encode(message),(error=>{if(error)return reject(error);resolve()}))}))}async subscribe(event){if(typeof event==="string")event=[event];const result=await this.call("rpc.on",event);if(typeof event==="string"&&result[event]!=="ok")throw new Error("Failed subscribing to an event '"+event+"' with: "+result[event]);return result}async unsubscribe(event){if(typeof event==="string")event=[event];const result=await this.call("rpc.off",event);if(typeof event==="string"&&result[event]!=="ok")throw new Error("Failed unsubscribing from an event with: "+result);return result}close(code,data){this.socket.close(code||1e3,data)}setAutoReconnect(reconnect){this.reconnect=reconnect}setReconnectInterval(interval){this.reconnect_interval=interval}setMaxReconnects(max_reconnects){this.max_reconnects=max_reconnects}_connect(address,options){clearTimeout(this.reconnect_timer_id);this.socket=this.webSocketFactory(address,options);this.socket.addEventListener("open",(()=>{this.ready=true;this.emit("open");this.current_reconnects=0}));this.socket.addEventListener("message",(({data:message})=>{if(message instanceof ArrayBuffer)message=bufferExports.Buffer.from(message).toString();try{message=this.dataPack.decode(message)}catch(error){return}if(message.notification&&this.listeners(message.notification).length){if(!Object.keys(message.params).length)return this.emit(message.notification);const args=[message.notification];if(message.params.constructor===Object)args.push(message.params);else for(let i=0;i<message.params.length;i++)args.push(message.params[i]);return Promise.resolve().then((()=>{this.emit.apply(this,args)}))}if(!this.queue[message.id]){if(message.method){return Promise.resolve().then((()=>{this.emit(message.method,message?.params)}))}return}if("error"in message==="result"in message)this.queue[message.id].promise[1](new Error('Server response malformed. Response must include either "result" or "error", but not both.'));if(this.queue[message.id].timeout)clearTimeout(this.queue[message.id].timeout);if(message.error)this.queue[message.id].promise[1](message.error);else this.queue[message.id].promise[0](message.result);delete this.queue[message.id]}));this.socket.addEventListener("error",(error=>this.emit("error",error)));this.socket.addEventListener("close",(({code:code,reason:reason})=>{if(this.ready)setTimeout((()=>this.emit("close",code,reason)),0);this.ready=false;this.socket=void 0;if(code===1e3)return;this.current_reconnects++;if(this.reconnect&&(this.max_reconnects>this.current_reconnects||this.max_reconnects===0))this.reconnect_timer_id=setTimeout((()=>this._connect(address,options)),this.reconnect_interval)}))}};class RpcWebSocketClient extends CommonClient{constructor(address,options,generate_request_id){const webSocketFactory=url=>{const rpc=WebSocket(url,{autoconnect:true,max_reconnects:5,reconnect:true,reconnect_interval:1e3,...options});if("socket"in rpc){this.underlyingSocket=rpc.socket}else{this.underlyingSocket=rpc}return rpc};super(webSocketFactory,address,options,generate_request_id);this.underlyingSocket=void 0}call(...args){const readyState=this.underlyingSocket?.readyState;if(readyState===1){return super.call(...args)}return Promise.reject(new Error("Tried to call a JSON-RPC method `"+args[0]+"` but the socket was not `CONNECTING` or `OPEN` (`readyState` was "+readyState+")"))}notify(...args){const readyState=this.underlyingSocket?.readyState;if(readyState===1){return super.notify(...args)}return Promise.reject(new Error("Tried to send a JSON-RPC notification `"+args[0]+"` but the socket was not `CONNECTING` or `OPEN` (`readyState` was "+readyState+")"))}}function decodeData(type,data){let decoded;try{decoded=type.layout.decode(data)}catch(err){throw new Error("invalid instruction; "+err)}if(decoded.typeIndex!==type.index){throw new Error(`invalid account data; account type mismatch ${decoded.typeIndex} != ${type.index}`)}return decoded}const LOOKUP_TABLE_META_SIZE=56;class AddressLookupTableAccount{constructor(args){this.key=void 0;this.state=void 0;this.key=args.key;this.state=args.state}isActive(){const U64_MAX=BigInt("0xffffffffffffffff");return this.state.deactivationSlot===U64_MAX}static deserialize(accountData){const meta=decodeData(LookupTableMetaLayout,accountData);const serializedAddressesLen=accountData.length-LOOKUP_TABLE_META_SIZE;assert$1(serializedAddressesLen>=0,"lookup table is invalid");assert$1(serializedAddressesLen%32===0,"lookup table is invalid");const numSerializedAddresses=serializedAddressesLen/32;const{addresses:addresses}=LayoutExports.struct([LayoutExports.seq(publicKey(),numSerializedAddresses,"addresses")]).decode(accountData.slice(LOOKUP_TABLE_META_SIZE));return{deactivationSlot:meta.deactivationSlot,lastExtendedSlot:meta.lastExtendedSlot,lastExtendedSlotStartIndex:meta.lastExtendedStartIndex,authority:meta.authority.length!==0?new PublicKey(meta.authority[0]):undefined,addresses:addresses.map((address=>new PublicKey(address)))}}}const LookupTableMetaLayout={index:1,layout:LayoutExports.struct([LayoutExports.u32("typeIndex"),u64("deactivationSlot"),LayoutExports.nu64("lastExtendedSlot"),LayoutExports.u8("lastExtendedStartIndex"),LayoutExports.u8(),LayoutExports.seq(publicKey(),LayoutExports.offset(LayoutExports.u8(),-1),"authority")])};const URL_RE=/^[^:]+:\/\/([^:[]+|\[[^\]]+\])(:\d+)?(.*)/i;function makeWebsocketUrl(endpoint){const matches=endpoint.match(URL_RE);if(matches==null){throw TypeError(`Failed to validate endpoint URL \`${endpoint}\``)}const[_,hostish,portWithColon,rest]=matches;const protocol=endpoint.startsWith("https:")?"wss:":"ws:";const startPort=portWithColon==null?null:parseInt(portWithColon.slice(1),10);const websocketPort=startPort==null?"":`:${startPort+1}`;return`${protocol}//${hostish}${websocketPort}${rest}`}const PublicKeyFromString=coerce(instance(PublicKey),string(),(value=>new PublicKey(value)));const RawAccountDataResult=tuple([string(),literal("base64")]);const BufferFromRawAccountData=coerce(instance(bufferExports.Buffer),RawAccountDataResult,(value=>bufferExports.Buffer.from(value[0],"base64")));const BLOCKHASH_CACHE_TIMEOUT_MS=30*1e3;function assertEndpointUrl(putativeUrl){if(/^https?:/.test(putativeUrl)===false){throw new TypeError("Endpoint URL must start with `http:` or `https:`.")}return putativeUrl}function extractCommitmentFromConfig(commitmentOrConfig){let commitment;let config;if(typeof commitmentOrConfig==="string"){commitment=commitmentOrConfig}else if(commitmentOrConfig){const{commitment:specifiedCommitment,...specifiedConfig}=commitmentOrConfig;commitment=specifiedCommitment;config=specifiedConfig}return{commitment:commitment,config:config}}function applyDefaultMemcmpEncodingToFilters(filters){return filters.map((filter=>"memcmp"in filter?{...filter,memcmp:{...filter.memcmp,encoding:filter.memcmp.encoding??"base58"}}:filter))}function createRpcResult(result){return union([type({jsonrpc:literal("2.0"),id:string(),result:result}),type({jsonrpc:literal("2.0"),id:string(),error:type({code:unknown(),message:string(),data:optional(any())})})])}const UnknownRpcResult=createRpcResult(unknown());function jsonRpcResult(schema){return coerce(createRpcResult(schema),UnknownRpcResult,(value=>{if("error"in value){return value}else{return{...value,result:create(value.result,schema)}}}))}function jsonRpcResultAndContext(value){return jsonRpcResult(type({context:type({slot:number()}),value:value}))}function notificationResultAndContext(value){return type({context:type({slot:number()}),value:value})}function versionedMessageFromResponse(version,response){if(version===0){return new MessageV0({header:response.header,staticAccountKeys:response.accountKeys.map((accountKey=>new PublicKey(accountKey))),recentBlockhash:response.recentBlockhash,compiledInstructions:response.instructions.map((ix=>({programIdIndex:ix.programIdIndex,accountKeyIndexes:ix.accounts,data:bs58.decode(ix.data)}))),addressTableLookups:response.addressTableLookups})}else{return new Message(response)}}const GetInflationGovernorResult=type({foundation:number(),foundationTerm:number(),initial:number(),taper:number(),terminal:number()});const GetInflationRewardResult=jsonRpcResult(array(nullable(type({epoch:number(),effectiveSlot:number(),amount:number(),postBalance:number(),commission:optional(nullable(number()))}))));const GetRecentPrioritizationFeesResult=array(type({slot:number(),prioritizationFee:number()}));const GetInflationRateResult=type({total:number(),validator:number(),foundation:number(),epoch:number()});const GetEpochInfoResult=type({epoch:number(),slotIndex:number(),slotsInEpoch:number(),absoluteSlot:number(),blockHeight:optional(number()),transactionCount:optional(number())});const GetEpochScheduleResult=type({slotsPerEpoch:number(),leaderScheduleSlotOffset:number(),warmup:boolean(),firstNormalEpoch:number(),firstNormalSlot:number()});const GetLeaderScheduleResult=record(string(),array(number()));const TransactionErrorResult=nullable(union([type({}),string()]));const SignatureStatusResult=type({err:TransactionErrorResult});const SignatureReceivedResult=literal("receivedSignature");const VersionResult=type({"solana-core":string(),"feature-set":optional(number())});const ParsedInstructionStruct=type({program:string(),programId:PublicKeyFromString,parsed:unknown()});const PartiallyDecodedInstructionStruct=type({programId:PublicKeyFromString,accounts:array(PublicKeyFromString),data:string()});const SimulatedTransactionResponseStruct=jsonRpcResultAndContext(type({err:nullable(union([type({}),string()])),logs:nullable(array(string())),accounts:optional(nullable(array(nullable(type({executable:boolean(),owner:string(),lamports:number(),data:array(string()),rentEpoch:optional(number())}))))),unitsConsumed:optional(number()),returnData:optional(nullable(type({programId:string(),data:tuple([string(),literal("base64")])}))),innerInstructions:optional(nullable(array(type({index:number(),instructions:array(union([ParsedInstructionStruct,PartiallyDecodedInstructionStruct]))}))))}));const BlockProductionResponseStruct=jsonRpcResultAndContext(type({byIdentity:record(string(),array(number())),range:type({firstSlot:number(),lastSlot:number()})}));function createRpcClient(url,httpHeaders,customFetch,fetchMiddleware,disableRetryOnRateLimit,httpAgent){const fetch=customFetch?customFetch:fetchImpl;let agent;{if(httpAgent!=null){console.warn("You have supplied an `httpAgent` when creating a `Connection` in a browser environment."+"It has been ignored; `httpAgent` is only used in Node environments.")}}let fetchWithMiddleware;if(fetchMiddleware){fetchWithMiddleware=async(info,init)=>{const modifiedFetchArgs=await new Promise(((resolve,reject)=>{try{fetchMiddleware(info,init,((modifiedInfo,modifiedInit)=>resolve([modifiedInfo,modifiedInit])))}catch(error){reject(error)}}));return await fetch(...modifiedFetchArgs)}}const clientBrowser=new RpcClient((async(request,callback)=>{const options={method:"POST",body:request,agent:agent,headers:Object.assign({"Content-Type":"application/json"},httpHeaders||{},COMMON_HTTP_HEADERS)};try{let too_many_requests_retries=5;let res;let waitTime=500;for(;;){if(fetchWithMiddleware){res=await fetchWithMiddleware(url,options)}else{res=await fetch(url,options)}if(res.status!==429){break}if(disableRetryOnRateLimit===true){break}too_many_requests_retries-=1;if(too_many_requests_retries===0){break}console.error(`Server responded with ${res.status} ${res.statusText}.  Retrying after ${waitTime}ms delay...`);await sleep(waitTime);waitTime*=2}const text=await res.text();if(res.ok){callback(null,text)}else{callback(new Error(`${res.status} ${res.statusText}: ${text}`))}}catch(err){if(err instanceof Error)callback(err)}}),{});return clientBrowser}function createRpcRequest(client){return(method,args)=>new Promise(((resolve,reject)=>{client.request(method,args,((err,response)=>{if(err){reject(err);return}resolve(response)}))}))}function createRpcBatchRequest(client){return requests=>new Promise(((resolve,reject)=>{if(requests.length===0)resolve([]);const batch=requests.map((params=>client.request(params.methodName,params.args)));client.request(batch,((err,response)=>{if(err){reject(err);return}resolve(response)}))}))}const GetInflationGovernorRpcResult=jsonRpcResult(GetInflationGovernorResult);const GetInflationRateRpcResult=jsonRpcResult(GetInflationRateResult);const GetRecentPrioritizationFeesRpcResult=jsonRpcResult(GetRecentPrioritizationFeesResult);const GetEpochInfoRpcResult=jsonRpcResult(GetEpochInfoResult);const GetEpochScheduleRpcResult=jsonRpcResult(GetEpochScheduleResult);const GetLeaderScheduleRpcResult=jsonRpcResult(GetLeaderScheduleResult);const SlotRpcResult=jsonRpcResult(number());const GetSupplyRpcResult=jsonRpcResultAndContext(type({total:number(),circulating:number(),nonCirculating:number(),nonCirculatingAccounts:array(PublicKeyFromString)}));const TokenAmountResult=type({amount:string(),uiAmount:nullable(number()),decimals:number(),uiAmountString:optional(string())});const GetTokenLargestAccountsResult=jsonRpcResultAndContext(array(type({address:PublicKeyFromString,amount:string(),uiAmount:nullable(number()),decimals:number(),uiAmountString:optional(string())})));const GetTokenAccountsByOwner=jsonRpcResultAndContext(array(type({pubkey:PublicKeyFromString,account:type({executable:boolean(),owner:PublicKeyFromString,lamports:number(),data:BufferFromRawAccountData,rentEpoch:number()})})));const ParsedAccountDataResult=type({program:string(),parsed:unknown(),space:number()});const GetParsedTokenAccountsByOwner=jsonRpcResultAndContext(array(type({pubkey:PublicKeyFromString,account:type({executable:boolean(),owner:PublicKeyFromString,lamports:number(),data:ParsedAccountDataResult,rentEpoch:number()})})));const GetLargestAccountsRpcResult=jsonRpcResultAndContext(array(type({lamports:number(),address:PublicKeyFromString})));const AccountInfoResult=type({executable:boolean(),owner:PublicKeyFromString,lamports:number(),data:BufferFromRawAccountData,rentEpoch:number()});const KeyedAccountInfoResult=type({pubkey:PublicKeyFromString,account:AccountInfoResult});const ParsedOrRawAccountData=coerce(union([instance(bufferExports.Buffer),ParsedAccountDataResult]),union([RawAccountDataResult,ParsedAccountDataResult]),(value=>{if(Array.isArray(value)){return create(value,BufferFromRawAccountData)}else{return value}}));const ParsedAccountInfoResult=type({executable:boolean(),owner:PublicKeyFromString,lamports:number(),data:ParsedOrRawAccountData,rentEpoch:number()});const KeyedParsedAccountInfoResult=type({pubkey:PublicKeyFromString,account:ParsedAccountInfoResult});const StakeActivationResult=type({state:union([literal("active"),literal("inactive"),literal("activating"),literal("deactivating")]),active:number(),inactive:number()});const GetConfirmedSignaturesForAddress2RpcResult=jsonRpcResult(array(type({signature:string(),slot:number(),err:TransactionErrorResult,memo:nullable(string()),blockTime:optional(nullable(number()))})));const GetSignaturesForAddressRpcResult=jsonRpcResult(array(type({signature:string(),slot:number(),err:TransactionErrorResult,memo:nullable(string()),blockTime:optional(nullable(number()))})));const AccountNotificationResult=type({subscription:number(),result:notificationResultAndContext(AccountInfoResult)});const ProgramAccountInfoResult=type({pubkey:PublicKeyFromString,account:AccountInfoResult});const ProgramAccountNotificationResult=type({subscription:number(),result:notificationResultAndContext(ProgramAccountInfoResult)});const SlotInfoResult=type({parent:number(),slot:number(),root:number()});const SlotNotificationResult=type({subscription:number(),result:SlotInfoResult});const SlotUpdateResult=union([type({type:union([literal("firstShredReceived"),literal("completed"),literal("optimisticConfirmation"),literal("root")]),slot:number(),timestamp:number()}),type({type:literal("createdBank"),parent:number(),slot:number(),timestamp:number()}),type({type:literal("frozen"),slot:number(),timestamp:number(),stats:type({numTransactionEntries:number(),numSuccessfulTransactions:number(),numFailedTransactions:number(),maxTransactionsPerEntry:number()})}),type({type:literal("dead"),slot:number(),timestamp:number(),err:string()})]);const SlotUpdateNotificationResult=type({subscription:number(),result:SlotUpdateResult});const SignatureNotificationResult=type({subscription:number(),result:notificationResultAndContext(union([SignatureStatusResult,SignatureReceivedResult]))});const RootNotificationResult=type({subscription:number(),result:number()});const ContactInfoResult=type({pubkey:string(),gossip:nullable(string()),tpu:nullable(string()),rpc:nullable(string()),version:nullable(string())});const VoteAccountInfoResult=type({votePubkey:string(),nodePubkey:string(),activatedStake:number(),epochVoteAccount:boolean(),epochCredits:array(tuple([number(),number(),number()])),commission:number(),lastVote:number(),rootSlot:nullable(number())});const GetVoteAccounts=jsonRpcResult(type({current:array(VoteAccountInfoResult),delinquent:array(VoteAccountInfoResult)}));const ConfirmationStatus=union([literal("processed"),literal("confirmed"),literal("finalized")]);const SignatureStatusResponse=type({slot:number(),confirmations:nullable(number()),err:TransactionErrorResult,confirmationStatus:optional(ConfirmationStatus)});const GetSignatureStatusesRpcResult=jsonRpcResultAndContext(array(nullable(SignatureStatusResponse)));const GetMinimumBalanceForRentExemptionRpcResult=jsonRpcResult(number());const AddressTableLookupStruct=type({accountKey:PublicKeyFromString,writableIndexes:array(number()),readonlyIndexes:array(number())});const ConfirmedTransactionResult=type({signatures:array(string()),message:type({accountKeys:array(string()),header:type({numRequiredSignatures:number(),numReadonlySignedAccounts:number(),numReadonlyUnsignedAccounts:number()}),instructions:array(type({accounts:array(number()),data:string(),programIdIndex:number()})),recentBlockhash:string(),addressTableLookups:optional(array(AddressTableLookupStruct))})});const AnnotatedAccountKey=type({pubkey:PublicKeyFromString,signer:boolean(),writable:boolean(),source:optional(union([literal("transaction"),literal("lookupTable")]))});const ConfirmedTransactionAccountsModeResult=type({accountKeys:array(AnnotatedAccountKey),signatures:array(string())});const ParsedInstructionResult=type({parsed:unknown(),program:string(),programId:PublicKeyFromString});const RawInstructionResult=type({accounts:array(PublicKeyFromString),data:string(),programId:PublicKeyFromString});const InstructionResult=union([RawInstructionResult,ParsedInstructionResult]);const UnknownInstructionResult=union([type({parsed:unknown(),program:string(),programId:string()}),type({accounts:array(string()),data:string(),programId:string()})]);const ParsedOrRawInstruction=coerce(InstructionResult,UnknownInstructionResult,(value=>{if("accounts"in value){return create(value,RawInstructionResult)}else{return create(value,ParsedInstructionResult)}}));const ParsedConfirmedTransactionResult=type({signatures:array(string()),message:type({accountKeys:array(AnnotatedAccountKey),instructions:array(ParsedOrRawInstruction),recentBlockhash:string(),addressTableLookups:optional(nullable(array(AddressTableLookupStruct)))})});const TokenBalanceResult=type({accountIndex:number(),mint:string(),owner:optional(string()),programId:optional(string()),uiTokenAmount:TokenAmountResult});const LoadedAddressesResult=type({writable:array(PublicKeyFromString),readonly:array(PublicKeyFromString)});const ConfirmedTransactionMetaResult=type({err:TransactionErrorResult,fee:number(),innerInstructions:optional(nullable(array(type({index:number(),instructions:array(type({accounts:array(number()),data:string(),programIdIndex:number()}))})))),preBalances:array(number()),postBalances:array(number()),logMessages:optional(nullable(array(string()))),preTokenBalances:optional(nullable(array(TokenBalanceResult))),postTokenBalances:optional(nullable(array(TokenBalanceResult))),loadedAddresses:optional(LoadedAddressesResult),computeUnitsConsumed:optional(number())});const ParsedConfirmedTransactionMetaResult=type({err:TransactionErrorResult,fee:number(),innerInstructions:optional(nullable(array(type({index:number(),instructions:array(ParsedOrRawInstruction)})))),preBalances:array(number()),postBalances:array(number()),logMessages:optional(nullable(array(string()))),preTokenBalances:optional(nullable(array(TokenBalanceResult))),postTokenBalances:optional(nullable(array(TokenBalanceResult))),loadedAddresses:optional(LoadedAddressesResult),computeUnitsConsumed:optional(number())});const TransactionVersionStruct=union([literal(0),literal("legacy")]);const RewardsResult=type({pubkey:string(),lamports:number(),postBalance:nullable(number()),rewardType:nullable(string()),commission:optional(nullable(number()))});const GetBlockRpcResult=jsonRpcResult(nullable(type({blockhash:string(),previousBlockhash:string(),parentSlot:number(),transactions:array(type({transaction:ConfirmedTransactionResult,meta:nullable(ConfirmedTransactionMetaResult),version:optional(TransactionVersionStruct)})),rewards:optional(array(RewardsResult)),blockTime:nullable(number()),blockHeight:nullable(number())})));const GetNoneModeBlockRpcResult=jsonRpcResult(nullable(type({blockhash:string(),previousBlockhash:string(),parentSlot:number(),rewards:optional(array(RewardsResult)),blockTime:nullable(number()),blockHeight:nullable(number())})));const GetAccountsModeBlockRpcResult=jsonRpcResult(nullable(type({blockhash:string(),previousBlockhash:string(),parentSlot:number(),transactions:array(type({transaction:ConfirmedTransactionAccountsModeResult,meta:nullable(ConfirmedTransactionMetaResult),version:optional(TransactionVersionStruct)})),rewards:optional(array(RewardsResult)),blockTime:nullable(number()),blockHeight:nullable(number())})));const GetParsedBlockRpcResult=jsonRpcResult(nullable(type({blockhash:string(),previousBlockhash:string(),parentSlot:number(),transactions:array(type({transaction:ParsedConfirmedTransactionResult,meta:nullable(ParsedConfirmedTransactionMetaResult),version:optional(TransactionVersionStruct)})),rewards:optional(array(RewardsResult)),blockTime:nullable(number()),blockHeight:nullable(number())})));const GetParsedAccountsModeBlockRpcResult=jsonRpcResult(nullable(type({blockhash:string(),previousBlockhash:string(),parentSlot:number(),transactions:array(type({transaction:ConfirmedTransactionAccountsModeResult,meta:nullable(ParsedConfirmedTransactionMetaResult),version:optional(TransactionVersionStruct)})),rewards:optional(array(RewardsResult)),blockTime:nullable(number()),blockHeight:nullable(number())})));const GetParsedNoneModeBlockRpcResult=jsonRpcResult(nullable(type({blockhash:string(),previousBlockhash:string(),parentSlot:number(),rewards:optional(array(RewardsResult)),blockTime:nullable(number()),blockHeight:nullable(number())})));const GetConfirmedBlockRpcResult=jsonRpcResult(nullable(type({blockhash:string(),previousBlockhash:string(),parentSlot:number(),transactions:array(type({transaction:ConfirmedTransactionResult,meta:nullable(ConfirmedTransactionMetaResult)})),rewards:optional(array(RewardsResult)),blockTime:nullable(number())})));const GetBlockSignaturesRpcResult=jsonRpcResult(nullable(type({blockhash:string(),previousBlockhash:string(),parentSlot:number(),signatures:array(string()),blockTime:nullable(number())})));const GetTransactionRpcResult=jsonRpcResult(nullable(type({slot:number(),meta:nullable(ConfirmedTransactionMetaResult),blockTime:optional(nullable(number())),transaction:ConfirmedTransactionResult,version:optional(TransactionVersionStruct)})));const GetParsedTransactionRpcResult=jsonRpcResult(nullable(type({slot:number(),transaction:ParsedConfirmedTransactionResult,meta:nullable(ParsedConfirmedTransactionMetaResult),blockTime:optional(nullable(number())),version:optional(TransactionVersionStruct)})));const GetRecentBlockhashAndContextRpcResult=jsonRpcResultAndContext(type({blockhash:string(),feeCalculator:type({lamportsPerSignature:number()})}));const GetLatestBlockhashRpcResult=jsonRpcResultAndContext(type({blockhash:string(),lastValidBlockHeight:number()}));const IsBlockhashValidRpcResult=jsonRpcResultAndContext(boolean());const PerfSampleResult=type({slot:number(),numTransactions:number(),numSlots:number(),samplePeriodSecs:number()});const GetRecentPerformanceSamplesRpcResult=jsonRpcResult(array(PerfSampleResult));const GetFeeCalculatorRpcResult=jsonRpcResultAndContext(nullable(type({feeCalculator:type({lamportsPerSignature:number()})})));const RequestAirdropRpcResult=jsonRpcResult(string());const SendTransactionRpcResult=jsonRpcResult(string());const LogsResult=type({err:TransactionErrorResult,logs:array(string()),signature:string()});const LogsNotificationResult=type({result:notificationResultAndContext(LogsResult),subscription:number()});const COMMON_HTTP_HEADERS={"solana-client":`js/${"1.95.8"}`};class Connection{constructor(endpoint,_commitmentOrConfig){this._commitment=void 0;this._confirmTransactionInitialTimeout=void 0;this._rpcEndpoint=void 0;this._rpcWsEndpoint=void 0;this._rpcClient=void 0;this._rpcRequest=void 0;this._rpcBatchRequest=void 0;this._rpcWebSocket=void 0;this._rpcWebSocketConnected=false;this._rpcWebSocketHeartbeat=null;this._rpcWebSocketIdleTimeout=null;this._rpcWebSocketGeneration=0;this._disableBlockhashCaching=false;this._pollingBlockhash=false;this._blockhashInfo={latestBlockhash:null,lastFetch:0,transactionSignatures:[],simulatedSignatures:[]};this._nextClientSubscriptionId=0;this._subscriptionDisposeFunctionsByClientSubscriptionId={};this._subscriptionHashByClientSubscriptionId={};this._subscriptionStateChangeCallbacksByHash={};this._subscriptionCallbacksByServerSubscriptionId={};this._subscriptionsByHash={};this._subscriptionsAutoDisposedByRpc=new Set;this.getBlockHeight=(()=>{const requestPromises={};return async commitmentOrConfig=>{const{commitment:commitment,config:config}=extractCommitmentFromConfig(commitmentOrConfig);const args=this._buildArgs([],commitment,undefined,config);const requestHash=fastStableStringify(args);requestPromises[requestHash]=requestPromises[requestHash]??(async()=>{try{const unsafeRes=await this._rpcRequest("getBlockHeight",args);const res=create(unsafeRes,jsonRpcResult(number()));if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get block height information")}return res.result}finally{delete requestPromises[requestHash]}})();return await requestPromises[requestHash]}})();let wsEndpoint;let httpHeaders;let fetch;let fetchMiddleware;let disableRetryOnRateLimit;let httpAgent;if(_commitmentOrConfig&&typeof _commitmentOrConfig==="string"){this._commitment=_commitmentOrConfig}else if(_commitmentOrConfig){this._commitment=_commitmentOrConfig.commitment;this._confirmTransactionInitialTimeout=_commitmentOrConfig.confirmTransactionInitialTimeout;wsEndpoint=_commitmentOrConfig.wsEndpoint;httpHeaders=_commitmentOrConfig.httpHeaders;fetch=_commitmentOrConfig.fetch;fetchMiddleware=_commitmentOrConfig.fetchMiddleware;disableRetryOnRateLimit=_commitmentOrConfig.disableRetryOnRateLimit;httpAgent=_commitmentOrConfig.httpAgent}this._rpcEndpoint=assertEndpointUrl(endpoint);this._rpcWsEndpoint=wsEndpoint||makeWebsocketUrl(endpoint);this._rpcClient=createRpcClient(endpoint,httpHeaders,fetch,fetchMiddleware,disableRetryOnRateLimit,httpAgent);this._rpcRequest=createRpcRequest(this._rpcClient);this._rpcBatchRequest=createRpcBatchRequest(this._rpcClient);this._rpcWebSocket=new RpcWebSocketClient(this._rpcWsEndpoint,{autoconnect:false,max_reconnects:Infinity});this._rpcWebSocket.on("open",this._wsOnOpen.bind(this));this._rpcWebSocket.on("error",this._wsOnError.bind(this));this._rpcWebSocket.on("close",this._wsOnClose.bind(this));this._rpcWebSocket.on("accountNotification",this._wsOnAccountNotification.bind(this));this._rpcWebSocket.on("programNotification",this._wsOnProgramAccountNotification.bind(this));this._rpcWebSocket.on("slotNotification",this._wsOnSlotNotification.bind(this));this._rpcWebSocket.on("slotsUpdatesNotification",this._wsOnSlotUpdatesNotification.bind(this));this._rpcWebSocket.on("signatureNotification",this._wsOnSignatureNotification.bind(this));this._rpcWebSocket.on("rootNotification",this._wsOnRootNotification.bind(this));this._rpcWebSocket.on("logsNotification",this._wsOnLogsNotification.bind(this))}get commitment(){return this._commitment}get rpcEndpoint(){return this._rpcEndpoint}async getBalanceAndContext(publicKey,commitmentOrConfig){const{commitment:commitment,config:config}=extractCommitmentFromConfig(commitmentOrConfig);const args=this._buildArgs([publicKey.toBase58()],commitment,undefined,config);const unsafeRes=await this._rpcRequest("getBalance",args);const res=create(unsafeRes,jsonRpcResultAndContext(number()));if("error"in res){throw new SolanaJSONRPCError(res.error,`failed to get balance for ${publicKey.toBase58()}`)}return res.result}async getBalance(publicKey,commitmentOrConfig){return await this.getBalanceAndContext(publicKey,commitmentOrConfig).then((x=>x.value)).catch((e=>{throw new Error("failed to get balance of account "+publicKey.toBase58()+": "+e)}))}async getBlockTime(slot){const unsafeRes=await this._rpcRequest("getBlockTime",[slot]);const res=create(unsafeRes,jsonRpcResult(nullable(number())));if("error"in res){throw new SolanaJSONRPCError(res.error,`failed to get block time for slot ${slot}`)}return res.result}async getMinimumLedgerSlot(){const unsafeRes=await this._rpcRequest("minimumLedgerSlot",[]);const res=create(unsafeRes,jsonRpcResult(number()));if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get minimum ledger slot")}return res.result}async getFirstAvailableBlock(){const unsafeRes=await this._rpcRequest("getFirstAvailableBlock",[]);const res=create(unsafeRes,SlotRpcResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get first available block")}return res.result}async getSupply(config){let configArg={};if(typeof config==="string"){configArg={commitment:config}}else if(config){configArg={...config,commitment:config&&config.commitment||this.commitment}}else{configArg={commitment:this.commitment}}const unsafeRes=await this._rpcRequest("getSupply",[configArg]);const res=create(unsafeRes,GetSupplyRpcResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get supply")}return res.result}async getTokenSupply(tokenMintAddress,commitment){const args=this._buildArgs([tokenMintAddress.toBase58()],commitment);const unsafeRes=await this._rpcRequest("getTokenSupply",args);const res=create(unsafeRes,jsonRpcResultAndContext(TokenAmountResult));if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get token supply")}return res.result}async getTokenAccountBalance(tokenAddress,commitment){const args=this._buildArgs([tokenAddress.toBase58()],commitment);const unsafeRes=await this._rpcRequest("getTokenAccountBalance",args);const res=create(unsafeRes,jsonRpcResultAndContext(TokenAmountResult));if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get token account balance")}return res.result}async getTokenAccountsByOwner(ownerAddress,filter,commitmentOrConfig){const{commitment:commitment,config:config}=extractCommitmentFromConfig(commitmentOrConfig);let _args=[ownerAddress.toBase58()];if("mint"in filter){_args.push({mint:filter.mint.toBase58()})}else{_args.push({programId:filter.programId.toBase58()})}const args=this._buildArgs(_args,commitment,"base64",config);const unsafeRes=await this._rpcRequest("getTokenAccountsByOwner",args);const res=create(unsafeRes,GetTokenAccountsByOwner);if("error"in res){throw new SolanaJSONRPCError(res.error,`failed to get token accounts owned by account ${ownerAddress.toBase58()}`)}return res.result}async getParsedTokenAccountsByOwner(ownerAddress,filter,commitment){let _args=[ownerAddress.toBase58()];if("mint"in filter){_args.push({mint:filter.mint.toBase58()})}else{_args.push({programId:filter.programId.toBase58()})}const args=this._buildArgs(_args,commitment,"jsonParsed");const unsafeRes=await this._rpcRequest("getTokenAccountsByOwner",args);const res=create(unsafeRes,GetParsedTokenAccountsByOwner);if("error"in res){throw new SolanaJSONRPCError(res.error,`failed to get token accounts owned by account ${ownerAddress.toBase58()}`)}return res.result}async getLargestAccounts(config){const arg={...config,commitment:config&&config.commitment||this.commitment};const args=arg.filter||arg.commitment?[arg]:[];const unsafeRes=await this._rpcRequest("getLargestAccounts",args);const res=create(unsafeRes,GetLargestAccountsRpcResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get largest accounts")}return res.result}async getTokenLargestAccounts(mintAddress,commitment){const args=this._buildArgs([mintAddress.toBase58()],commitment);const unsafeRes=await this._rpcRequest("getTokenLargestAccounts",args);const res=create(unsafeRes,GetTokenLargestAccountsResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get token largest accounts")}return res.result}async getAccountInfoAndContext(publicKey,commitmentOrConfig){const{commitment:commitment,config:config}=extractCommitmentFromConfig(commitmentOrConfig);const args=this._buildArgs([publicKey.toBase58()],commitment,"base64",config);const unsafeRes=await this._rpcRequest("getAccountInfo",args);const res=create(unsafeRes,jsonRpcResultAndContext(nullable(AccountInfoResult)));if("error"in res){throw new SolanaJSONRPCError(res.error,`failed to get info about account ${publicKey.toBase58()}`)}return res.result}async getParsedAccountInfo(publicKey,commitmentOrConfig){const{commitment:commitment,config:config}=extractCommitmentFromConfig(commitmentOrConfig);const args=this._buildArgs([publicKey.toBase58()],commitment,"jsonParsed",config);const unsafeRes=await this._rpcRequest("getAccountInfo",args);const res=create(unsafeRes,jsonRpcResultAndContext(nullable(ParsedAccountInfoResult)));if("error"in res){throw new SolanaJSONRPCError(res.error,`failed to get info about account ${publicKey.toBase58()}`)}return res.result}async getAccountInfo(publicKey,commitmentOrConfig){try{const res=await this.getAccountInfoAndContext(publicKey,commitmentOrConfig);return res.value}catch(e){throw new Error("failed to get info about account "+publicKey.toBase58()+": "+e)}}async getMultipleParsedAccounts(publicKeys,rawConfig){const{commitment:commitment,config:config}=extractCommitmentFromConfig(rawConfig);const keys=publicKeys.map((key=>key.toBase58()));const args=this._buildArgs([keys],commitment,"jsonParsed",config);const unsafeRes=await this._rpcRequest("getMultipleAccounts",args);const res=create(unsafeRes,jsonRpcResultAndContext(array(nullable(ParsedAccountInfoResult))));if("error"in res){throw new SolanaJSONRPCError(res.error,`failed to get info for accounts ${keys}`)}return res.result}async getMultipleAccountsInfoAndContext(publicKeys,commitmentOrConfig){const{commitment:commitment,config:config}=extractCommitmentFromConfig(commitmentOrConfig);const keys=publicKeys.map((key=>key.toBase58()));const args=this._buildArgs([keys],commitment,"base64",config);const unsafeRes=await this._rpcRequest("getMultipleAccounts",args);const res=create(unsafeRes,jsonRpcResultAndContext(array(nullable(AccountInfoResult))));if("error"in res){throw new SolanaJSONRPCError(res.error,`failed to get info for accounts ${keys}`)}return res.result}async getMultipleAccountsInfo(publicKeys,commitmentOrConfig){const res=await this.getMultipleAccountsInfoAndContext(publicKeys,commitmentOrConfig);return res.value}async getStakeActivation(publicKey,commitmentOrConfig,epoch){const{commitment:commitment,config:config}=extractCommitmentFromConfig(commitmentOrConfig);const args=this._buildArgs([publicKey.toBase58()],commitment,undefined,{...config,epoch:epoch!=null?epoch:config?.epoch});const unsafeRes=await this._rpcRequest("getStakeActivation",args);const res=create(unsafeRes,jsonRpcResult(StakeActivationResult));if("error"in res){throw new SolanaJSONRPCError(res.error,`failed to get Stake Activation ${publicKey.toBase58()}`)}return res.result}async getProgramAccounts(programId,configOrCommitment){const{commitment:commitment,config:config}=extractCommitmentFromConfig(configOrCommitment);const{encoding:encoding,...configWithoutEncoding}=config||{};const args=this._buildArgs([programId.toBase58()],commitment,encoding||"base64",{...configWithoutEncoding,...configWithoutEncoding.filters?{filters:applyDefaultMemcmpEncodingToFilters(configWithoutEncoding.filters)}:null});const unsafeRes=await this._rpcRequest("getProgramAccounts",args);const baseSchema=array(KeyedAccountInfoResult);const res=configWithoutEncoding.withContext===true?create(unsafeRes,jsonRpcResultAndContext(baseSchema)):create(unsafeRes,jsonRpcResult(baseSchema));if("error"in res){throw new SolanaJSONRPCError(res.error,`failed to get accounts owned by program ${programId.toBase58()}`)}return res.result}async getParsedProgramAccounts(programId,configOrCommitment){const{commitment:commitment,config:config}=extractCommitmentFromConfig(configOrCommitment);const args=this._buildArgs([programId.toBase58()],commitment,"jsonParsed",config);const unsafeRes=await this._rpcRequest("getProgramAccounts",args);const res=create(unsafeRes,jsonRpcResult(array(KeyedParsedAccountInfoResult)));if("error"in res){throw new SolanaJSONRPCError(res.error,`failed to get accounts owned by program ${programId.toBase58()}`)}return res.result}async confirmTransaction(strategy,commitment){let rawSignature;if(typeof strategy=="string"){rawSignature=strategy}else{const config=strategy;if(config.abortSignal?.aborted){return Promise.reject(config.abortSignal.reason)}rawSignature=config.signature}let decodedSignature;try{decodedSignature=bs58.decode(rawSignature)}catch(err){throw new Error("signature must be base58 encoded: "+rawSignature)}assert$1(decodedSignature.length===64,"signature has invalid length");if(typeof strategy==="string"){return await this.confirmTransactionUsingLegacyTimeoutStrategy({commitment:commitment||this.commitment,signature:rawSignature})}else if("lastValidBlockHeight"in strategy){return await this.confirmTransactionUsingBlockHeightExceedanceStrategy({commitment:commitment||this.commitment,strategy:strategy})}else{return await this.confirmTransactionUsingDurableNonceStrategy({commitment:commitment||this.commitment,strategy:strategy})}}getCancellationPromise(signal){return new Promise(((_,reject)=>{if(signal==null){return}if(signal.aborted){reject(signal.reason)}else{signal.addEventListener("abort",(()=>{reject(signal.reason)}))}}))}getTransactionConfirmationPromise({commitment:commitment,signature:signature}){let signatureSubscriptionId;let disposeSignatureSubscriptionStateChangeObserver;let done=false;const confirmationPromise=new Promise(((resolve,reject)=>{try{signatureSubscriptionId=this.onSignature(signature,((result,context)=>{signatureSubscriptionId=undefined;const response={context:context,value:result};resolve({__type:TransactionStatus.PROCESSED,response:response})}),commitment);const subscriptionSetupPromise=new Promise((resolveSubscriptionSetup=>{if(signatureSubscriptionId==null){resolveSubscriptionSetup()}else{disposeSignatureSubscriptionStateChangeObserver=this._onSubscriptionStateChange(signatureSubscriptionId,(nextState=>{if(nextState==="subscribed"){resolveSubscriptionSetup()}}))}}));(async()=>{await subscriptionSetupPromise;if(done)return;const response=await this.getSignatureStatus(signature);if(done)return;if(response==null){return}const{context:context,value:value}=response;if(value==null){return}if(value?.err){reject(value.err)}else{switch(commitment){case"confirmed":case"single":case"singleGossip":{if(value.confirmationStatus==="processed"){return}break}case"finalized":case"max":case"root":{if(value.confirmationStatus==="processed"||value.confirmationStatus==="confirmed"){return}break}case"processed":case"recent":}done=true;resolve({__type:TransactionStatus.PROCESSED,response:{context:context,value:value}})}})()}catch(err){reject(err)}}));const abortConfirmation=()=>{if(disposeSignatureSubscriptionStateChangeObserver){disposeSignatureSubscriptionStateChangeObserver();disposeSignatureSubscriptionStateChangeObserver=undefined}if(signatureSubscriptionId!=null){this.removeSignatureListener(signatureSubscriptionId);signatureSubscriptionId=undefined}};return{abortConfirmation:abortConfirmation,confirmationPromise:confirmationPromise}}async confirmTransactionUsingBlockHeightExceedanceStrategy({commitment:commitment,strategy:{abortSignal:abortSignal,lastValidBlockHeight:lastValidBlockHeight,signature:signature}}){let done=false;const expiryPromise=new Promise((resolve=>{const checkBlockHeight=async()=>{try{const blockHeight=await this.getBlockHeight(commitment);return blockHeight}catch(_e){return-1}};(async()=>{let currentBlockHeight=await checkBlockHeight();if(done)return;while(currentBlockHeight<=lastValidBlockHeight){await sleep(1e3);if(done)return;currentBlockHeight=await checkBlockHeight();if(done)return}resolve({__type:TransactionStatus.BLOCKHEIGHT_EXCEEDED})})()}));const{abortConfirmation:abortConfirmation,confirmationPromise:confirmationPromise}=this.getTransactionConfirmationPromise({commitment:commitment,signature:signature});const cancellationPromise=this.getCancellationPromise(abortSignal);let result;try{const outcome=await Promise.race([cancellationPromise,confirmationPromise,expiryPromise]);if(outcome.__type===TransactionStatus.PROCESSED){result=outcome.response}else{throw new TransactionExpiredBlockheightExceededError(signature)}}finally{done=true;abortConfirmation()}return result}async confirmTransactionUsingDurableNonceStrategy({commitment:commitment,strategy:{abortSignal:abortSignal,minContextSlot:minContextSlot,nonceAccountPubkey:nonceAccountPubkey,nonceValue:nonceValue,signature:signature}}){let done=false;const expiryPromise=new Promise((resolve=>{let currentNonceValue=nonceValue;let lastCheckedSlot=null;const getCurrentNonceValue=async()=>{try{const{context:context,value:nonceAccount}=await this.getNonceAndContext(nonceAccountPubkey,{commitment:commitment,minContextSlot:minContextSlot});lastCheckedSlot=context.slot;return nonceAccount?.nonce}catch(e){return currentNonceValue}};(async()=>{currentNonceValue=await getCurrentNonceValue();if(done)return;while(true){if(nonceValue!==currentNonceValue){resolve({__type:TransactionStatus.NONCE_INVALID,slotInWhichNonceDidAdvance:lastCheckedSlot});return}await sleep(2e3);if(done)return;currentNonceValue=await getCurrentNonceValue();if(done)return}})()}));const{abortConfirmation:abortConfirmation,confirmationPromise:confirmationPromise}=this.getTransactionConfirmationPromise({commitment:commitment,signature:signature});const cancellationPromise=this.getCancellationPromise(abortSignal);let result;try{const outcome=await Promise.race([cancellationPromise,confirmationPromise,expiryPromise]);if(outcome.__type===TransactionStatus.PROCESSED){result=outcome.response}else{let signatureStatus;while(true){const status=await this.getSignatureStatus(signature);if(status==null){break}if(status.context.slot<(outcome.slotInWhichNonceDidAdvance??minContextSlot)){await sleep(400);continue}signatureStatus=status;break}if(signatureStatus?.value){const commitmentForStatus=commitment||"finalized";const{confirmationStatus:confirmationStatus}=signatureStatus.value;switch(commitmentForStatus){case"processed":case"recent":if(confirmationStatus!=="processed"&&confirmationStatus!=="confirmed"&&confirmationStatus!=="finalized"){throw new TransactionExpiredNonceInvalidError(signature)}break;case"confirmed":case"single":case"singleGossip":if(confirmationStatus!=="confirmed"&&confirmationStatus!=="finalized"){throw new TransactionExpiredNonceInvalidError(signature)}break;case"finalized":case"max":case"root":if(confirmationStatus!=="finalized"){throw new TransactionExpiredNonceInvalidError(signature)}break;default:(_=>{})(commitmentForStatus)}result={context:signatureStatus.context,value:{err:signatureStatus.value.err}}}else{throw new TransactionExpiredNonceInvalidError(signature)}}}finally{done=true;abortConfirmation()}return result}async confirmTransactionUsingLegacyTimeoutStrategy({commitment:commitment,signature:signature}){let timeoutId;const expiryPromise=new Promise((resolve=>{let timeoutMs=this._confirmTransactionInitialTimeout||60*1e3;switch(commitment){case"processed":case"recent":case"single":case"confirmed":case"singleGossip":{timeoutMs=this._confirmTransactionInitialTimeout||30*1e3;break}}timeoutId=setTimeout((()=>resolve({__type:TransactionStatus.TIMED_OUT,timeoutMs:timeoutMs})),timeoutMs)}));const{abortConfirmation:abortConfirmation,confirmationPromise:confirmationPromise}=this.getTransactionConfirmationPromise({commitment:commitment,signature:signature});let result;try{const outcome=await Promise.race([confirmationPromise,expiryPromise]);if(outcome.__type===TransactionStatus.PROCESSED){result=outcome.response}else{throw new TransactionExpiredTimeoutError(signature,outcome.timeoutMs/1e3)}}finally{clearTimeout(timeoutId);abortConfirmation()}return result}async getClusterNodes(){const unsafeRes=await this._rpcRequest("getClusterNodes",[]);const res=create(unsafeRes,jsonRpcResult(array(ContactInfoResult)));if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get cluster nodes")}return res.result}async getVoteAccounts(commitment){const args=this._buildArgs([],commitment);const unsafeRes=await this._rpcRequest("getVoteAccounts",args);const res=create(unsafeRes,GetVoteAccounts);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get vote accounts")}return res.result}async getSlot(commitmentOrConfig){const{commitment:commitment,config:config}=extractCommitmentFromConfig(commitmentOrConfig);const args=this._buildArgs([],commitment,undefined,config);const unsafeRes=await this._rpcRequest("getSlot",args);const res=create(unsafeRes,jsonRpcResult(number()));if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get slot")}return res.result}async getSlotLeader(commitmentOrConfig){const{commitment:commitment,config:config}=extractCommitmentFromConfig(commitmentOrConfig);const args=this._buildArgs([],commitment,undefined,config);const unsafeRes=await this._rpcRequest("getSlotLeader",args);const res=create(unsafeRes,jsonRpcResult(string()));if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get slot leader")}return res.result}async getSlotLeaders(startSlot,limit){const args=[startSlot,limit];const unsafeRes=await this._rpcRequest("getSlotLeaders",args);const res=create(unsafeRes,jsonRpcResult(array(PublicKeyFromString)));if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get slot leaders")}return res.result}async getSignatureStatus(signature,config){const{context:context,value:values}=await this.getSignatureStatuses([signature],config);assert$1(values.length===1);const value=values[0];return{context:context,value:value}}async getSignatureStatuses(signatures,config){const params=[signatures];if(config){params.push(config)}const unsafeRes=await this._rpcRequest("getSignatureStatuses",params);const res=create(unsafeRes,GetSignatureStatusesRpcResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get signature status")}return res.result}async getTransactionCount(commitmentOrConfig){const{commitment:commitment,config:config}=extractCommitmentFromConfig(commitmentOrConfig);const args=this._buildArgs([],commitment,undefined,config);const unsafeRes=await this._rpcRequest("getTransactionCount",args);const res=create(unsafeRes,jsonRpcResult(number()));if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get transaction count")}return res.result}async getTotalSupply(commitment){const result=await this.getSupply({commitment:commitment,excludeNonCirculatingAccountsList:true});return result.value.total}async getInflationGovernor(commitment){const args=this._buildArgs([],commitment);const unsafeRes=await this._rpcRequest("getInflationGovernor",args);const res=create(unsafeRes,GetInflationGovernorRpcResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get inflation")}return res.result}async getInflationReward(addresses,epoch,commitmentOrConfig){const{commitment:commitment,config:config}=extractCommitmentFromConfig(commitmentOrConfig);const args=this._buildArgs([addresses.map((pubkey=>pubkey.toBase58()))],commitment,undefined,{...config,epoch:epoch!=null?epoch:config?.epoch});const unsafeRes=await this._rpcRequest("getInflationReward",args);const res=create(unsafeRes,GetInflationRewardResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get inflation reward")}return res.result}async getInflationRate(){const unsafeRes=await this._rpcRequest("getInflationRate",[]);const res=create(unsafeRes,GetInflationRateRpcResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get inflation rate")}return res.result}async getEpochInfo(commitmentOrConfig){const{commitment:commitment,config:config}=extractCommitmentFromConfig(commitmentOrConfig);const args=this._buildArgs([],commitment,undefined,config);const unsafeRes=await this._rpcRequest("getEpochInfo",args);const res=create(unsafeRes,GetEpochInfoRpcResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get epoch info")}return res.result}async getEpochSchedule(){const unsafeRes=await this._rpcRequest("getEpochSchedule",[]);const res=create(unsafeRes,GetEpochScheduleRpcResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get epoch schedule")}const epochSchedule=res.result;return new EpochSchedule(epochSchedule.slotsPerEpoch,epochSchedule.leaderScheduleSlotOffset,epochSchedule.warmup,epochSchedule.firstNormalEpoch,epochSchedule.firstNormalSlot)}async getLeaderSchedule(){const unsafeRes=await this._rpcRequest("getLeaderSchedule",[]);const res=create(unsafeRes,GetLeaderScheduleRpcResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get leader schedule")}return res.result}async getMinimumBalanceForRentExemption(dataLength,commitment){const args=this._buildArgs([dataLength],commitment);const unsafeRes=await this._rpcRequest("getMinimumBalanceForRentExemption",args);const res=create(unsafeRes,GetMinimumBalanceForRentExemptionRpcResult);if("error"in res){console.warn("Unable to fetch minimum balance for rent exemption");return 0}return res.result}async getRecentBlockhashAndContext(commitment){const args=this._buildArgs([],commitment);const unsafeRes=await this._rpcRequest("getRecentBlockhash",args);const res=create(unsafeRes,GetRecentBlockhashAndContextRpcResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get recent blockhash")}return res.result}async getRecentPerformanceSamples(limit){const unsafeRes=await this._rpcRequest("getRecentPerformanceSamples",limit?[limit]:[]);const res=create(unsafeRes,GetRecentPerformanceSamplesRpcResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get recent performance samples")}return res.result}async getFeeCalculatorForBlockhash(blockhash,commitment){const args=this._buildArgs([blockhash],commitment);const unsafeRes=await this._rpcRequest("getFeeCalculatorForBlockhash",args);const res=create(unsafeRes,GetFeeCalculatorRpcResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get fee calculator")}const{context:context,value:value}=res.result;return{context:context,value:value!==null?value.feeCalculator:null}}async getFeeForMessage(message,commitment){const wireMessage=toBuffer(message.serialize()).toString("base64");const args=this._buildArgs([wireMessage],commitment);const unsafeRes=await this._rpcRequest("getFeeForMessage",args);const res=create(unsafeRes,jsonRpcResultAndContext(nullable(number())));if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get fee for message")}if(res.result===null){throw new Error("invalid blockhash")}return res.result}async getRecentPrioritizationFees(config){const accounts=config?.lockedWritableAccounts?.map((key=>key.toBase58()));const args=accounts?.length?[accounts]:[];const unsafeRes=await this._rpcRequest("getRecentPrioritizationFees",args);const res=create(unsafeRes,GetRecentPrioritizationFeesRpcResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get recent prioritization fees")}return res.result}async getRecentBlockhash(commitment){try{const res=await this.getRecentBlockhashAndContext(commitment);return res.value}catch(e){throw new Error("failed to get recent blockhash: "+e)}}async getLatestBlockhash(commitmentOrConfig){try{const res=await this.getLatestBlockhashAndContext(commitmentOrConfig);return res.value}catch(e){throw new Error("failed to get recent blockhash: "+e)}}async getLatestBlockhashAndContext(commitmentOrConfig){const{commitment:commitment,config:config}=extractCommitmentFromConfig(commitmentOrConfig);const args=this._buildArgs([],commitment,undefined,config);const unsafeRes=await this._rpcRequest("getLatestBlockhash",args);const res=create(unsafeRes,GetLatestBlockhashRpcResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get latest blockhash")}return res.result}async isBlockhashValid(blockhash,rawConfig){const{commitment:commitment,config:config}=extractCommitmentFromConfig(rawConfig);const args=this._buildArgs([blockhash],commitment,undefined,config);const unsafeRes=await this._rpcRequest("isBlockhashValid",args);const res=create(unsafeRes,IsBlockhashValidRpcResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to determine if the blockhash `"+blockhash+"`is valid")}return res.result}async getVersion(){const unsafeRes=await this._rpcRequest("getVersion",[]);const res=create(unsafeRes,jsonRpcResult(VersionResult));if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get version")}return res.result}async getGenesisHash(){const unsafeRes=await this._rpcRequest("getGenesisHash",[]);const res=create(unsafeRes,jsonRpcResult(string()));if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get genesis hash")}return res.result}async getBlock(slot,rawConfig){const{commitment:commitment,config:config}=extractCommitmentFromConfig(rawConfig);const args=this._buildArgsAtLeastConfirmed([slot],commitment,undefined,config);const unsafeRes=await this._rpcRequest("getBlock",args);try{switch(config?.transactionDetails){case"accounts":{const res=create(unsafeRes,GetAccountsModeBlockRpcResult);if("error"in res){throw res.error}return res.result}case"none":{const res=create(unsafeRes,GetNoneModeBlockRpcResult);if("error"in res){throw res.error}return res.result}default:{const res=create(unsafeRes,GetBlockRpcResult);if("error"in res){throw res.error}const{result:result}=res;return result?{...result,transactions:result.transactions.map((({transaction:transaction,meta:meta,version:version})=>({meta:meta,transaction:{...transaction,message:versionedMessageFromResponse(version,transaction.message)},version:version})))}:null}}}catch(e){throw new SolanaJSONRPCError(e,"failed to get confirmed block")}}async getParsedBlock(slot,rawConfig){const{commitment:commitment,config:config}=extractCommitmentFromConfig(rawConfig);const args=this._buildArgsAtLeastConfirmed([slot],commitment,"jsonParsed",config);const unsafeRes=await this._rpcRequest("getBlock",args);try{switch(config?.transactionDetails){case"accounts":{const res=create(unsafeRes,GetParsedAccountsModeBlockRpcResult);if("error"in res){throw res.error}return res.result}case"none":{const res=create(unsafeRes,GetParsedNoneModeBlockRpcResult);if("error"in res){throw res.error}return res.result}default:{const res=create(unsafeRes,GetParsedBlockRpcResult);if("error"in res){throw res.error}return res.result}}}catch(e){throw new SolanaJSONRPCError(e,"failed to get block")}}async getBlockProduction(configOrCommitment){let extra;let commitment;if(typeof configOrCommitment==="string"){commitment=configOrCommitment}else if(configOrCommitment){const{commitment:c,...rest}=configOrCommitment;commitment=c;extra=rest}const args=this._buildArgs([],commitment,"base64",extra);const unsafeRes=await this._rpcRequest("getBlockProduction",args);const res=create(unsafeRes,BlockProductionResponseStruct);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get block production information")}return res.result}async getTransaction(signature,rawConfig){const{commitment:commitment,config:config}=extractCommitmentFromConfig(rawConfig);const args=this._buildArgsAtLeastConfirmed([signature],commitment,undefined,config);const unsafeRes=await this._rpcRequest("getTransaction",args);const res=create(unsafeRes,GetTransactionRpcResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get transaction")}const result=res.result;if(!result)return result;return{...result,transaction:{...result.transaction,message:versionedMessageFromResponse(result.version,result.transaction.message)}}}async getParsedTransaction(signature,commitmentOrConfig){const{commitment:commitment,config:config}=extractCommitmentFromConfig(commitmentOrConfig);const args=this._buildArgsAtLeastConfirmed([signature],commitment,"jsonParsed",config);const unsafeRes=await this._rpcRequest("getTransaction",args);const res=create(unsafeRes,GetParsedTransactionRpcResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get transaction")}return res.result}async getParsedTransactions(signatures,commitmentOrConfig){const{commitment:commitment,config:config}=extractCommitmentFromConfig(commitmentOrConfig);const batch=signatures.map((signature=>{const args=this._buildArgsAtLeastConfirmed([signature],commitment,"jsonParsed",config);return{methodName:"getTransaction",args:args}}));const unsafeRes=await this._rpcBatchRequest(batch);const res=unsafeRes.map((unsafeRes=>{const res=create(unsafeRes,GetParsedTransactionRpcResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get transactions")}return res.result}));return res}async getTransactions(signatures,commitmentOrConfig){const{commitment:commitment,config:config}=extractCommitmentFromConfig(commitmentOrConfig);const batch=signatures.map((signature=>{const args=this._buildArgsAtLeastConfirmed([signature],commitment,undefined,config);return{methodName:"getTransaction",args:args}}));const unsafeRes=await this._rpcBatchRequest(batch);const res=unsafeRes.map((unsafeRes=>{const res=create(unsafeRes,GetTransactionRpcResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get transactions")}const result=res.result;if(!result)return result;return{...result,transaction:{...result.transaction,message:versionedMessageFromResponse(result.version,result.transaction.message)}}}));return res}async getConfirmedBlock(slot,commitment){const args=this._buildArgsAtLeastConfirmed([slot],commitment);const unsafeRes=await this._rpcRequest("getConfirmedBlock",args);const res=create(unsafeRes,GetConfirmedBlockRpcResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get confirmed block")}const result=res.result;if(!result){throw new Error("Confirmed block "+slot+" not found")}const block={...result,transactions:result.transactions.map((({transaction:transaction,meta:meta})=>{const message=new Message(transaction.message);return{meta:meta,transaction:{...transaction,message:message}}}))};return{...block,transactions:block.transactions.map((({transaction:transaction,meta:meta})=>({meta:meta,transaction:Transaction.populate(transaction.message,transaction.signatures)})))}}async getBlocks(startSlot,endSlot,commitment){const args=this._buildArgsAtLeastConfirmed(endSlot!==undefined?[startSlot,endSlot]:[startSlot],commitment);const unsafeRes=await this._rpcRequest("getBlocks",args);const res=create(unsafeRes,jsonRpcResult(array(number())));if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get blocks")}return res.result}async getBlockSignatures(slot,commitment){const args=this._buildArgsAtLeastConfirmed([slot],commitment,undefined,{transactionDetails:"signatures",rewards:false});const unsafeRes=await this._rpcRequest("getBlock",args);const res=create(unsafeRes,GetBlockSignaturesRpcResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get block")}const result=res.result;if(!result){throw new Error("Block "+slot+" not found")}return result}async getConfirmedBlockSignatures(slot,commitment){const args=this._buildArgsAtLeastConfirmed([slot],commitment,undefined,{transactionDetails:"signatures",rewards:false});const unsafeRes=await this._rpcRequest("getConfirmedBlock",args);const res=create(unsafeRes,GetBlockSignaturesRpcResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get confirmed block")}const result=res.result;if(!result){throw new Error("Confirmed block "+slot+" not found")}return result}async getConfirmedTransaction(signature,commitment){const args=this._buildArgsAtLeastConfirmed([signature],commitment);const unsafeRes=await this._rpcRequest("getConfirmedTransaction",args);const res=create(unsafeRes,GetTransactionRpcResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get transaction")}const result=res.result;if(!result)return result;const message=new Message(result.transaction.message);const signatures=result.transaction.signatures;return{...result,transaction:Transaction.populate(message,signatures)}}async getParsedConfirmedTransaction(signature,commitment){const args=this._buildArgsAtLeastConfirmed([signature],commitment,"jsonParsed");const unsafeRes=await this._rpcRequest("getConfirmedTransaction",args);const res=create(unsafeRes,GetParsedTransactionRpcResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get confirmed transaction")}return res.result}async getParsedConfirmedTransactions(signatures,commitment){const batch=signatures.map((signature=>{const args=this._buildArgsAtLeastConfirmed([signature],commitment,"jsonParsed");return{methodName:"getConfirmedTransaction",args:args}}));const unsafeRes=await this._rpcBatchRequest(batch);const res=unsafeRes.map((unsafeRes=>{const res=create(unsafeRes,GetParsedTransactionRpcResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get confirmed transactions")}return res.result}));return res}async getConfirmedSignaturesForAddress(address,startSlot,endSlot){let options={};let firstAvailableBlock=await this.getFirstAvailableBlock();while(!("until"in options)){startSlot--;if(startSlot<=0||startSlot<firstAvailableBlock){break}try{const block=await this.getConfirmedBlockSignatures(startSlot,"finalized");if(block.signatures.length>0){options.until=block.signatures[block.signatures.length-1].toString()}}catch(err){if(err instanceof Error&&err.message.includes("skipped")){continue}else{throw err}}}let highestConfirmedRoot=await this.getSlot("finalized");while(!("before"in options)){endSlot++;if(endSlot>highestConfirmedRoot){break}try{const block=await this.getConfirmedBlockSignatures(endSlot);if(block.signatures.length>0){options.before=block.signatures[block.signatures.length-1].toString()}}catch(err){if(err instanceof Error&&err.message.includes("skipped")){continue}else{throw err}}}const confirmedSignatureInfo=await this.getConfirmedSignaturesForAddress2(address,options);return confirmedSignatureInfo.map((info=>info.signature))}async getConfirmedSignaturesForAddress2(address,options,commitment){const args=this._buildArgsAtLeastConfirmed([address.toBase58()],commitment,undefined,options);const unsafeRes=await this._rpcRequest("getConfirmedSignaturesForAddress2",args);const res=create(unsafeRes,GetConfirmedSignaturesForAddress2RpcResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get confirmed signatures for address")}return res.result}async getSignaturesForAddress(address,options,commitment){const args=this._buildArgsAtLeastConfirmed([address.toBase58()],commitment,undefined,options);const unsafeRes=await this._rpcRequest("getSignaturesForAddress",args);const res=create(unsafeRes,GetSignaturesForAddressRpcResult);if("error"in res){throw new SolanaJSONRPCError(res.error,"failed to get signatures for address")}return res.result}async getAddressLookupTable(accountKey,config){const{context:context,value:accountInfo}=await this.getAccountInfoAndContext(accountKey,config);let value=null;if(accountInfo!==null){value=new AddressLookupTableAccount({key:accountKey,state:AddressLookupTableAccount.deserialize(accountInfo.data)})}return{context:context,value:value}}async getNonceAndContext(nonceAccount,commitmentOrConfig){const{context:context,value:accountInfo}=await this.getAccountInfoAndContext(nonceAccount,commitmentOrConfig);let value=null;if(accountInfo!==null){value=NonceAccount.fromAccountData(accountInfo.data)}return{context:context,value:value}}async getNonce(nonceAccount,commitmentOrConfig){return await this.getNonceAndContext(nonceAccount,commitmentOrConfig).then((x=>x.value)).catch((e=>{throw new Error("failed to get nonce for account "+nonceAccount.toBase58()+": "+e)}))}async requestAirdrop(to,lamports){const unsafeRes=await this._rpcRequest("requestAirdrop",[to.toBase58(),lamports]);const res=create(unsafeRes,RequestAirdropRpcResult);if("error"in res){throw new SolanaJSONRPCError(res.error,`airdrop to ${to.toBase58()} failed`)}return res.result}async _blockhashWithExpiryBlockHeight(disableCache){if(!disableCache){while(this._pollingBlockhash){await sleep(100)}const timeSinceFetch=Date.now()-this._blockhashInfo.lastFetch;const expired=timeSinceFetch>=BLOCKHASH_CACHE_TIMEOUT_MS;if(this._blockhashInfo.latestBlockhash!==null&&!expired){return this._blockhashInfo.latestBlockhash}}return await this._pollNewBlockhash()}async _pollNewBlockhash(){this._pollingBlockhash=true;try{const startTime=Date.now();const cachedLatestBlockhash=this._blockhashInfo.latestBlockhash;const cachedBlockhash=cachedLatestBlockhash?cachedLatestBlockhash.blockhash:null;for(let i=0;i<50;i++){const latestBlockhash=await this.getLatestBlockhash("finalized");if(cachedBlockhash!==latestBlockhash.blockhash){this._blockhashInfo={latestBlockhash:latestBlockhash,lastFetch:Date.now(),transactionSignatures:[],simulatedSignatures:[]};return latestBlockhash}await sleep(MS_PER_SLOT/2)}throw new Error(`Unable to obtain a new blockhash after ${Date.now()-startTime}ms`)}finally{this._pollingBlockhash=false}}async getStakeMinimumDelegation(config){const{commitment:commitment,config:configArg}=extractCommitmentFromConfig(config);const args=this._buildArgs([],commitment,"base64",configArg);const unsafeRes=await this._rpcRequest("getStakeMinimumDelegation",args);const res=create(unsafeRes,jsonRpcResultAndContext(number()));if("error"in res){throw new SolanaJSONRPCError(res.error,`failed to get stake minimum delegation`)}return res.result}async simulateTransaction(transactionOrMessage,configOrSigners,includeAccounts){if("message"in transactionOrMessage){const versionedTx=transactionOrMessage;const wireTransaction=versionedTx.serialize();const encodedTransaction=bufferExports.Buffer.from(wireTransaction).toString("base64");if(Array.isArray(configOrSigners)||includeAccounts!==undefined){throw new Error("Invalid arguments")}const config=configOrSigners||{};config.encoding="base64";if(!("commitment"in config)){config.commitment=this.commitment}if(configOrSigners&&typeof configOrSigners==="object"&&"innerInstructions"in configOrSigners){config.innerInstructions=configOrSigners.innerInstructions}const args=[encodedTransaction,config];const unsafeRes=await this._rpcRequest("simulateTransaction",args);const res=create(unsafeRes,SimulatedTransactionResponseStruct);if("error"in res){throw new Error("failed to simulate transaction: "+res.error.message)}return res.result}let transaction;if(transactionOrMessage instanceof Transaction){let originalTx=transactionOrMessage;transaction=new Transaction;transaction.feePayer=originalTx.feePayer;transaction.instructions=transactionOrMessage.instructions;transaction.nonceInfo=originalTx.nonceInfo;transaction.signatures=originalTx.signatures}else{transaction=Transaction.populate(transactionOrMessage);transaction._message=transaction._json=undefined}if(configOrSigners!==undefined&&!Array.isArray(configOrSigners)){throw new Error("Invalid arguments")}const signers=configOrSigners;if(transaction.nonceInfo&&signers){transaction.sign(...signers)}else{let disableCache=this._disableBlockhashCaching;for(;;){const latestBlockhash=await this._blockhashWithExpiryBlockHeight(disableCache);transaction.lastValidBlockHeight=latestBlockhash.lastValidBlockHeight;transaction.recentBlockhash=latestBlockhash.blockhash;if(!signers)break;transaction.sign(...signers);if(!transaction.signature){throw new Error("!signature")}const signature=transaction.signature.toString("base64");if(!this._blockhashInfo.simulatedSignatures.includes(signature)&&!this._blockhashInfo.transactionSignatures.includes(signature)){this._blockhashInfo.simulatedSignatures.push(signature);break}else{disableCache=true}}}const message=transaction._compile();const signData=message.serialize();const wireTransaction=transaction._serialize(signData);const encodedTransaction=wireTransaction.toString("base64");const config={encoding:"base64",commitment:this.commitment};if(includeAccounts){const addresses=(Array.isArray(includeAccounts)?includeAccounts:message.nonProgramIds()).map((key=>key.toBase58()));config["accounts"]={encoding:"base64",addresses:addresses}}if(signers){config.sigVerify=true}if(configOrSigners&&typeof configOrSigners==="object"&&"innerInstructions"in configOrSigners){config.innerInstructions=configOrSigners.innerInstructions}const args=[encodedTransaction,config];const unsafeRes=await this._rpcRequest("simulateTransaction",args);const res=create(unsafeRes,SimulatedTransactionResponseStruct);if("error"in res){let logs;if("data"in res.error){logs=res.error.data.logs;if(logs&&Array.isArray(logs)){const traceIndent="\n    ";const logTrace=traceIndent+logs.join(traceIndent);console.error(res.error.message,logTrace)}}throw new SendTransactionError({action:"simulate",signature:"",transactionMessage:res.error.message,logs:logs})}return res.result}async sendTransaction(transaction,signersOrOptions,options){if("version"in transaction){if(signersOrOptions&&Array.isArray(signersOrOptions)){throw new Error("Invalid arguments")}const wireTransaction=transaction.serialize();return await this.sendRawTransaction(wireTransaction,signersOrOptions)}if(signersOrOptions===undefined||!Array.isArray(signersOrOptions)){throw new Error("Invalid arguments")}const signers=signersOrOptions;if(transaction.nonceInfo){transaction.sign(...signers)}else{let disableCache=this._disableBlockhashCaching;for(;;){const latestBlockhash=await this._blockhashWithExpiryBlockHeight(disableCache);transaction.lastValidBlockHeight=latestBlockhash.lastValidBlockHeight;transaction.recentBlockhash=latestBlockhash.blockhash;transaction.sign(...signers);if(!transaction.signature){throw new Error("!signature")}const signature=transaction.signature.toString("base64");if(!this._blockhashInfo.transactionSignatures.includes(signature)){this._blockhashInfo.transactionSignatures.push(signature);break}else{disableCache=true}}}const wireTransaction=transaction.serialize();return await this.sendRawTransaction(wireTransaction,options)}async sendRawTransaction(rawTransaction,options){const encodedTransaction=toBuffer(rawTransaction).toString("base64");const result=await this.sendEncodedTransaction(encodedTransaction,options);return result}async sendEncodedTransaction(encodedTransaction,options){const config={encoding:"base64"};const skipPreflight=options&&options.skipPreflight;const preflightCommitment=skipPreflight===true?"processed":options&&options.preflightCommitment||this.commitment;if(options&&options.maxRetries!=null){config.maxRetries=options.maxRetries}if(options&&options.minContextSlot!=null){config.minContextSlot=options.minContextSlot}if(skipPreflight){config.skipPreflight=skipPreflight}if(preflightCommitment){config.preflightCommitment=preflightCommitment}const args=[encodedTransaction,config];const unsafeRes=await this._rpcRequest("sendTransaction",args);const res=create(unsafeRes,SendTransactionRpcResult);if("error"in res){let logs=undefined;if("data"in res.error){logs=res.error.data.logs}throw new SendTransactionError({action:skipPreflight?"send":"simulate",signature:"",transactionMessage:res.error.message,logs:logs})}return res.result}_wsOnOpen(){this._rpcWebSocketConnected=true;this._rpcWebSocketHeartbeat=setInterval((()=>{(async()=>{try{await this._rpcWebSocket.notify("ping")}catch{}})()}),5e3);this._updateSubscriptions()}_wsOnError(err){this._rpcWebSocketConnected=false;console.error("ws error:",err.message)}_wsOnClose(code){this._rpcWebSocketConnected=false;this._rpcWebSocketGeneration=(this._rpcWebSocketGeneration+1)%Number.MAX_SAFE_INTEGER;if(this._rpcWebSocketIdleTimeout){clearTimeout(this._rpcWebSocketIdleTimeout);this._rpcWebSocketIdleTimeout=null}if(this._rpcWebSocketHeartbeat){clearInterval(this._rpcWebSocketHeartbeat);this._rpcWebSocketHeartbeat=null}if(code===1e3){this._updateSubscriptions();return}this._subscriptionCallbacksByServerSubscriptionId={};Object.entries(this._subscriptionsByHash).forEach((([hash,subscription])=>{this._setSubscription(hash,{...subscription,state:"pending"})}))}_setSubscription(hash,nextSubscription){const prevState=this._subscriptionsByHash[hash]?.state;this._subscriptionsByHash[hash]=nextSubscription;if(prevState!==nextSubscription.state){const stateChangeCallbacks=this._subscriptionStateChangeCallbacksByHash[hash];if(stateChangeCallbacks){stateChangeCallbacks.forEach((cb=>{try{cb(nextSubscription.state)}catch{}}))}}}_onSubscriptionStateChange(clientSubscriptionId,callback){const hash=this._subscriptionHashByClientSubscriptionId[clientSubscriptionId];if(hash==null){return()=>{}}const stateChangeCallbacks=this._subscriptionStateChangeCallbacksByHash[hash]||=new Set;stateChangeCallbacks.add(callback);return()=>{stateChangeCallbacks.delete(callback);if(stateChangeCallbacks.size===0){delete this._subscriptionStateChangeCallbacksByHash[hash]}}}async _updateSubscriptions(){if(Object.keys(this._subscriptionsByHash).length===0){if(this._rpcWebSocketConnected){this._rpcWebSocketConnected=false;this._rpcWebSocketIdleTimeout=setTimeout((()=>{this._rpcWebSocketIdleTimeout=null;try{this._rpcWebSocket.close()}catch(err){if(err instanceof Error){console.log(`Error when closing socket connection: ${err.message}`)}}}),500)}return}if(this._rpcWebSocketIdleTimeout!==null){clearTimeout(this._rpcWebSocketIdleTimeout);this._rpcWebSocketIdleTimeout=null;this._rpcWebSocketConnected=true}if(!this._rpcWebSocketConnected){this._rpcWebSocket.connect();return}const activeWebSocketGeneration=this._rpcWebSocketGeneration;const isCurrentConnectionStillActive=()=>activeWebSocketGeneration===this._rpcWebSocketGeneration;await Promise.all(Object.keys(this._subscriptionsByHash).map((async hash=>{const subscription=this._subscriptionsByHash[hash];if(subscription===undefined){return}switch(subscription.state){case"pending":case"unsubscribed":if(subscription.callbacks.size===0){delete this._subscriptionsByHash[hash];if(subscription.state==="unsubscribed"){delete this._subscriptionCallbacksByServerSubscriptionId[subscription.serverSubscriptionId]}await this._updateSubscriptions();return}await(async()=>{const{args:args,method:method}=subscription;try{this._setSubscription(hash,{...subscription,state:"subscribing"});const serverSubscriptionId=await this._rpcWebSocket.call(method,args);this._setSubscription(hash,{...subscription,serverSubscriptionId:serverSubscriptionId,state:"subscribed"});this._subscriptionCallbacksByServerSubscriptionId[serverSubscriptionId]=subscription.callbacks;await this._updateSubscriptions()}catch(e){console.error(`Received ${e instanceof Error?"":"JSON-RPC "}error calling \`${method}\``,{args:args,error:e});if(!isCurrentConnectionStillActive()){return}this._setSubscription(hash,{...subscription,state:"pending"});await this._updateSubscriptions()}})();break;case"subscribed":if(subscription.callbacks.size===0){await(async()=>{const{serverSubscriptionId:serverSubscriptionId,unsubscribeMethod:unsubscribeMethod}=subscription;if(this._subscriptionsAutoDisposedByRpc.has(serverSubscriptionId)){this._subscriptionsAutoDisposedByRpc.delete(serverSubscriptionId)}else{this._setSubscription(hash,{...subscription,state:"unsubscribing"});this._setSubscription(hash,{...subscription,state:"unsubscribing"});try{await this._rpcWebSocket.call(unsubscribeMethod,[serverSubscriptionId])}catch(e){if(e instanceof Error){console.error(`${unsubscribeMethod} error:`,e.message)}if(!isCurrentConnectionStillActive()){return}this._setSubscription(hash,{...subscription,state:"subscribed"});await this._updateSubscriptions();return}}this._setSubscription(hash,{...subscription,state:"unsubscribed"});await this._updateSubscriptions()})()}break}})))}_handleServerNotification(serverSubscriptionId,callbackArgs){const callbacks=this._subscriptionCallbacksByServerSubscriptionId[serverSubscriptionId];if(callbacks===undefined){return}callbacks.forEach((cb=>{try{cb(...callbackArgs)}catch(e){console.error(e)}}))}_wsOnAccountNotification(notification){const{result:result,subscription:subscription}=create(notification,AccountNotificationResult);this._handleServerNotification(subscription,[result.value,result.context])}_makeSubscription(subscriptionConfig,args){const clientSubscriptionId=this._nextClientSubscriptionId++;const hash=fastStableStringify([subscriptionConfig.method,args]);const existingSubscription=this._subscriptionsByHash[hash];if(existingSubscription===undefined){this._subscriptionsByHash[hash]={...subscriptionConfig,args:args,callbacks:new Set([subscriptionConfig.callback]),state:"pending"}}else{existingSubscription.callbacks.add(subscriptionConfig.callback)}this._subscriptionHashByClientSubscriptionId[clientSubscriptionId]=hash;this._subscriptionDisposeFunctionsByClientSubscriptionId[clientSubscriptionId]=async()=>{delete this._subscriptionDisposeFunctionsByClientSubscriptionId[clientSubscriptionId];delete this._subscriptionHashByClientSubscriptionId[clientSubscriptionId];const subscription=this._subscriptionsByHash[hash];assert$1(subscription!==undefined,`Could not find a \`Subscription\` when tearing down client subscription #${clientSubscriptionId}`);subscription.callbacks.delete(subscriptionConfig.callback);await this._updateSubscriptions()};this._updateSubscriptions();return clientSubscriptionId}onAccountChange(publicKey,callback,commitmentOrConfig){const{commitment:commitment,config:config}=extractCommitmentFromConfig(commitmentOrConfig);const args=this._buildArgs([publicKey.toBase58()],commitment||this._commitment||"finalized","base64",config);return this._makeSubscription({callback:callback,method:"accountSubscribe",unsubscribeMethod:"accountUnsubscribe"},args)}async removeAccountChangeListener(clientSubscriptionId){await this._unsubscribeClientSubscription(clientSubscriptionId,"account change")}_wsOnProgramAccountNotification(notification){const{result:result,subscription:subscription}=create(notification,ProgramAccountNotificationResult);this._handleServerNotification(subscription,[{accountId:result.value.pubkey,accountInfo:result.value.account},result.context])}onProgramAccountChange(programId,callback,commitmentOrConfig,maybeFilters){const{commitment:commitment,config:config}=extractCommitmentFromConfig(commitmentOrConfig);const args=this._buildArgs([programId.toBase58()],commitment||this._commitment||"finalized","base64",config?config:maybeFilters?{filters:applyDefaultMemcmpEncodingToFilters(maybeFilters)}:undefined);return this._makeSubscription({callback:callback,method:"programSubscribe",unsubscribeMethod:"programUnsubscribe"},args)}async removeProgramAccountChangeListener(clientSubscriptionId){await this._unsubscribeClientSubscription(clientSubscriptionId,"program account change")}onLogs(filter,callback,commitment){const args=this._buildArgs([typeof filter==="object"?{mentions:[filter.toString()]}:filter],commitment||this._commitment||"finalized");return this._makeSubscription({callback:callback,method:"logsSubscribe",unsubscribeMethod:"logsUnsubscribe"},args)}async removeOnLogsListener(clientSubscriptionId){await this._unsubscribeClientSubscription(clientSubscriptionId,"logs")}_wsOnLogsNotification(notification){const{result:result,subscription:subscription}=create(notification,LogsNotificationResult);this._handleServerNotification(subscription,[result.value,result.context])}_wsOnSlotNotification(notification){const{result:result,subscription:subscription}=create(notification,SlotNotificationResult);this._handleServerNotification(subscription,[result])}onSlotChange(callback){return this._makeSubscription({callback:callback,method:"slotSubscribe",unsubscribeMethod:"slotUnsubscribe"},[])}async removeSlotChangeListener(clientSubscriptionId){await this._unsubscribeClientSubscription(clientSubscriptionId,"slot change")}_wsOnSlotUpdatesNotification(notification){const{result:result,subscription:subscription}=create(notification,SlotUpdateNotificationResult);this._handleServerNotification(subscription,[result])}onSlotUpdate(callback){return this._makeSubscription({callback:callback,method:"slotsUpdatesSubscribe",unsubscribeMethod:"slotsUpdatesUnsubscribe"},[])}async removeSlotUpdateListener(clientSubscriptionId){await this._unsubscribeClientSubscription(clientSubscriptionId,"slot update")}async _unsubscribeClientSubscription(clientSubscriptionId,subscriptionName){const dispose=this._subscriptionDisposeFunctionsByClientSubscriptionId[clientSubscriptionId];if(dispose){await dispose()}else{console.warn("Ignored unsubscribe request because an active subscription with id "+`\`${clientSubscriptionId}\` for '${subscriptionName}' events `+"could not be found.")}}_buildArgs(args,override,encoding,extra){const commitment=override||this._commitment;if(commitment||encoding||extra){let options={};if(encoding){options.encoding=encoding}if(commitment){options.commitment=commitment}if(extra){options=Object.assign(options,extra)}args.push(options)}return args}_buildArgsAtLeastConfirmed(args,override,encoding,extra){const commitment=override||this._commitment;if(commitment&&!["confirmed","finalized"].includes(commitment)){throw new Error("Using Connection with default commitment: `"+this._commitment+"`, but method requires at least `confirmed`")}return this._buildArgs(args,override,encoding,extra)}_wsOnSignatureNotification(notification){const{result:result,subscription:subscription}=create(notification,SignatureNotificationResult);if(result.value!=="receivedSignature"){this._subscriptionsAutoDisposedByRpc.add(subscription)}this._handleServerNotification(subscription,result.value==="receivedSignature"?[{type:"received"},result.context]:[{type:"status",result:result.value},result.context])}onSignature(signature,callback,commitment){const args=this._buildArgs([signature],commitment||this._commitment||"finalized");const clientSubscriptionId=this._makeSubscription({callback:(notification,context)=>{if(notification.type==="status"){callback(notification.result,context);try{this.removeSignatureListener(clientSubscriptionId)}catch(_err){}}},method:"signatureSubscribe",unsubscribeMethod:"signatureUnsubscribe"},args);return clientSubscriptionId}onSignatureWithOptions(signature,callback,options){const{commitment:commitment,...extra}={...options,commitment:options&&options.commitment||this._commitment||"finalized"};const args=this._buildArgs([signature],commitment,undefined,extra);const clientSubscriptionId=this._makeSubscription({callback:(notification,context)=>{callback(notification,context);try{this.removeSignatureListener(clientSubscriptionId)}catch(_err){}},method:"signatureSubscribe",unsubscribeMethod:"signatureUnsubscribe"},args);return clientSubscriptionId}async removeSignatureListener(clientSubscriptionId){await this._unsubscribeClientSubscription(clientSubscriptionId,"signature result")}_wsOnRootNotification(notification){const{result:result,subscription:subscription}=create(notification,RootNotificationResult);this._handleServerNotification(subscription,[result])}onRootChange(callback){return this._makeSubscription({callback:callback,method:"rootSubscribe",unsubscribeMethod:"rootUnsubscribe"},[])}async removeRootChangeListener(clientSubscriptionId){await this._unsubscribeClientSubscription(clientSubscriptionId,"root change")}}class Keypair{constructor(keypair){this._keypair=void 0;this._keypair=keypair??generateKeypair()}static generate(){return new Keypair(generateKeypair())}static fromSecretKey(secretKey,options){if(secretKey.byteLength!==64){throw new Error("bad secret key size")}const publicKey=secretKey.slice(32,64);if(!options||!options.skipValidation){const privateScalar=secretKey.slice(0,32);const computedPublicKey=getPublicKey(privateScalar);for(let ii=0;ii<32;ii++){if(publicKey[ii]!==computedPublicKey[ii]){throw new Error("provided secretKey is invalid")}}}return new Keypair({publicKey:publicKey,secretKey:secretKey})}static fromSeed(seed){const publicKey=getPublicKey(seed);const secretKey=new Uint8Array(64);secretKey.set(seed);secretKey.set(publicKey,32);return new Keypair({publicKey:publicKey,secretKey:secretKey})}get publicKey(){return new PublicKey(this._keypair.publicKey)}get secretKey(){return new Uint8Array(this._keypair.secretKey)}}const LOOKUP_TABLE_INSTRUCTION_LAYOUTS=Object.freeze({CreateLookupTable:{index:0,layout:LayoutExports.struct([LayoutExports.u32("instruction"),u64("recentSlot"),LayoutExports.u8("bumpSeed")])},FreezeLookupTable:{index:1,layout:LayoutExports.struct([LayoutExports.u32("instruction")])},ExtendLookupTable:{index:2,layout:LayoutExports.struct([LayoutExports.u32("instruction"),u64(),LayoutExports.seq(publicKey(),LayoutExports.offset(LayoutExports.u32(),-8),"addresses")])},DeactivateLookupTable:{index:3,layout:LayoutExports.struct([LayoutExports.u32("instruction")])},CloseLookupTable:{index:4,layout:LayoutExports.struct([LayoutExports.u32("instruction")])}});class AddressLookupTableInstruction{constructor(){}static decodeInstructionType(instruction){this.checkProgramId(instruction.programId);const instructionTypeLayout=LayoutExports.u32("instruction");const index=instructionTypeLayout.decode(instruction.data);let type;for(const[layoutType,layout]of Object.entries(LOOKUP_TABLE_INSTRUCTION_LAYOUTS)){if(layout.index==index){type=layoutType;break}}if(!type){throw new Error("Invalid Instruction. Should be a LookupTable Instruction")}return type}static decodeCreateLookupTable(instruction){this.checkProgramId(instruction.programId);this.checkKeysLength(instruction.keys,4);const{recentSlot:recentSlot}=decodeData$1(LOOKUP_TABLE_INSTRUCTION_LAYOUTS.CreateLookupTable,instruction.data);return{authority:instruction.keys[1].pubkey,payer:instruction.keys[2].pubkey,recentSlot:Number(recentSlot)}}static decodeExtendLookupTable(instruction){this.checkProgramId(instruction.programId);if(instruction.keys.length<2){throw new Error(`invalid instruction; found ${instruction.keys.length} keys, expected at least 2`)}const{addresses:addresses}=decodeData$1(LOOKUP_TABLE_INSTRUCTION_LAYOUTS.ExtendLookupTable,instruction.data);return{lookupTable:instruction.keys[0].pubkey,authority:instruction.keys[1].pubkey,payer:instruction.keys.length>2?instruction.keys[2].pubkey:undefined,addresses:addresses.map((buffer=>new PublicKey(buffer)))}}static decodeCloseLookupTable(instruction){this.checkProgramId(instruction.programId);this.checkKeysLength(instruction.keys,3);return{lookupTable:instruction.keys[0].pubkey,authority:instruction.keys[1].pubkey,recipient:instruction.keys[2].pubkey}}static decodeFreezeLookupTable(instruction){this.checkProgramId(instruction.programId);this.checkKeysLength(instruction.keys,2);return{lookupTable:instruction.keys[0].pubkey,authority:instruction.keys[1].pubkey}}static decodeDeactivateLookupTable(instruction){this.checkProgramId(instruction.programId);this.checkKeysLength(instruction.keys,2);return{lookupTable:instruction.keys[0].pubkey,authority:instruction.keys[1].pubkey}}static checkProgramId(programId){if(!programId.equals(AddressLookupTableProgram.programId)){throw new Error("invalid instruction; programId is not AddressLookupTable Program")}}static checkKeysLength(keys,expectedLength){if(keys.length<expectedLength){throw new Error(`invalid instruction; found ${keys.length} keys, expected at least ${expectedLength}`)}}}class AddressLookupTableProgram{constructor(){}static createLookupTable(params){const[lookupTableAddress,bumpSeed]=PublicKey.findProgramAddressSync([params.authority.toBuffer(),browserExports$1.toBufferLE(BigInt(params.recentSlot),8)],this.programId);const type=LOOKUP_TABLE_INSTRUCTION_LAYOUTS.CreateLookupTable;const data=encodeData(type,{recentSlot:BigInt(params.recentSlot),bumpSeed:bumpSeed});const keys=[{pubkey:lookupTableAddress,isSigner:false,isWritable:true},{pubkey:params.authority,isSigner:true,isWritable:false},{pubkey:params.payer,isSigner:true,isWritable:true},{pubkey:SystemProgram.programId,isSigner:false,isWritable:false}];return[new TransactionInstruction({programId:this.programId,keys:keys,data:data}),lookupTableAddress]}static freezeLookupTable(params){const type=LOOKUP_TABLE_INSTRUCTION_LAYOUTS.FreezeLookupTable;const data=encodeData(type);const keys=[{pubkey:params.lookupTable,isSigner:false,isWritable:true},{pubkey:params.authority,isSigner:true,isWritable:false}];return new TransactionInstruction({programId:this.programId,keys:keys,data:data})}static extendLookupTable(params){const type=LOOKUP_TABLE_INSTRUCTION_LAYOUTS.ExtendLookupTable;const data=encodeData(type,{addresses:params.addresses.map((addr=>addr.toBytes()))});const keys=[{pubkey:params.lookupTable,isSigner:false,isWritable:true},{pubkey:params.authority,isSigner:true,isWritable:false}];if(params.payer){keys.push({pubkey:params.payer,isSigner:true,isWritable:true},{pubkey:SystemProgram.programId,isSigner:false,isWritable:false})}return new TransactionInstruction({programId:this.programId,keys:keys,data:data})}static deactivateLookupTable(params){const type=LOOKUP_TABLE_INSTRUCTION_LAYOUTS.DeactivateLookupTable;const data=encodeData(type);const keys=[{pubkey:params.lookupTable,isSigner:false,isWritable:true},{pubkey:params.authority,isSigner:true,isWritable:false}];return new TransactionInstruction({programId:this.programId,keys:keys,data:data})}static closeLookupTable(params){const type=LOOKUP_TABLE_INSTRUCTION_LAYOUTS.CloseLookupTable;const data=encodeData(type);const keys=[{pubkey:params.lookupTable,isSigner:false,isWritable:true},{pubkey:params.authority,isSigner:true,isWritable:false},{pubkey:params.recipient,isSigner:false,isWritable:true}];return new TransactionInstruction({programId:this.programId,keys:keys,data:data})}}AddressLookupTableProgram.programId=new PublicKey("AddressLookupTab1e1111111111111111111111111");class ComputeBudgetInstruction{constructor(){}static decodeInstructionType(instruction){this.checkProgramId(instruction.programId);const instructionTypeLayout=LayoutExports.u8("instruction");const typeIndex=instructionTypeLayout.decode(instruction.data);let type;for(const[ixType,layout]of Object.entries(COMPUTE_BUDGET_INSTRUCTION_LAYOUTS)){if(layout.index==typeIndex){type=ixType;break}}if(!type){throw new Error("Instruction type incorrect; not a ComputeBudgetInstruction")}return type}static decodeRequestUnits(instruction){this.checkProgramId(instruction.programId);const{units:units,additionalFee:additionalFee}=decodeData$1(COMPUTE_BUDGET_INSTRUCTION_LAYOUTS.RequestUnits,instruction.data);return{units:units,additionalFee:additionalFee}}static decodeRequestHeapFrame(instruction){this.checkProgramId(instruction.programId);const{bytes:bytes}=decodeData$1(COMPUTE_BUDGET_INSTRUCTION_LAYOUTS.RequestHeapFrame,instruction.data);return{bytes:bytes}}static decodeSetComputeUnitLimit(instruction){this.checkProgramId(instruction.programId);const{units:units}=decodeData$1(COMPUTE_BUDGET_INSTRUCTION_LAYOUTS.SetComputeUnitLimit,instruction.data);return{units:units}}static decodeSetComputeUnitPrice(instruction){this.checkProgramId(instruction.programId);const{microLamports:microLamports}=decodeData$1(COMPUTE_BUDGET_INSTRUCTION_LAYOUTS.SetComputeUnitPrice,instruction.data);return{microLamports:microLamports}}static checkProgramId(programId){if(!programId.equals(ComputeBudgetProgram.programId)){throw new Error("invalid instruction; programId is not ComputeBudgetProgram")}}}const COMPUTE_BUDGET_INSTRUCTION_LAYOUTS=Object.freeze({RequestUnits:{index:0,layout:LayoutExports.struct([LayoutExports.u8("instruction"),LayoutExports.u32("units"),LayoutExports.u32("additionalFee")])},RequestHeapFrame:{index:1,layout:LayoutExports.struct([LayoutExports.u8("instruction"),LayoutExports.u32("bytes")])},SetComputeUnitLimit:{index:2,layout:LayoutExports.struct([LayoutExports.u8("instruction"),LayoutExports.u32("units")])},SetComputeUnitPrice:{index:3,layout:LayoutExports.struct([LayoutExports.u8("instruction"),u64("microLamports")])}});class ComputeBudgetProgram{constructor(){}static requestUnits(params){const type=COMPUTE_BUDGET_INSTRUCTION_LAYOUTS.RequestUnits;const data=encodeData(type,params);return new TransactionInstruction({keys:[],programId:this.programId,data:data})}static requestHeapFrame(params){const type=COMPUTE_BUDGET_INSTRUCTION_LAYOUTS.RequestHeapFrame;const data=encodeData(type,params);return new TransactionInstruction({keys:[],programId:this.programId,data:data})}static setComputeUnitLimit(params){const type=COMPUTE_BUDGET_INSTRUCTION_LAYOUTS.SetComputeUnitLimit;const data=encodeData(type,params);return new TransactionInstruction({keys:[],programId:this.programId,data:data})}static setComputeUnitPrice(params){const type=COMPUTE_BUDGET_INSTRUCTION_LAYOUTS.SetComputeUnitPrice;const data=encodeData(type,{microLamports:BigInt(params.microLamports)});return new TransactionInstruction({keys:[],programId:this.programId,data:data})}}ComputeBudgetProgram.programId=new PublicKey("ComputeBudget111111111111111111111111111111");const PRIVATE_KEY_BYTES$1=64;const PUBLIC_KEY_BYTES$1=32;const SIGNATURE_BYTES=64;const ED25519_INSTRUCTION_LAYOUT=LayoutExports.struct([LayoutExports.u8("numSignatures"),LayoutExports.u8("padding"),LayoutExports.u16("signatureOffset"),LayoutExports.u16("signatureInstructionIndex"),LayoutExports.u16("publicKeyOffset"),LayoutExports.u16("publicKeyInstructionIndex"),LayoutExports.u16("messageDataOffset"),LayoutExports.u16("messageDataSize"),LayoutExports.u16("messageInstructionIndex")]);class Ed25519Program{constructor(){}static createInstructionWithPublicKey(params){const{publicKey:publicKey,message:message,signature:signature,instructionIndex:instructionIndex}=params;assert$1(publicKey.length===PUBLIC_KEY_BYTES$1,`Public Key must be ${PUBLIC_KEY_BYTES$1} bytes but received ${publicKey.length} bytes`);assert$1(signature.length===SIGNATURE_BYTES,`Signature must be ${SIGNATURE_BYTES} bytes but received ${signature.length} bytes`);const publicKeyOffset=ED25519_INSTRUCTION_LAYOUT.span;const signatureOffset=publicKeyOffset+publicKey.length;const messageDataOffset=signatureOffset+signature.length;const numSignatures=1;const instructionData=bufferExports.Buffer.alloc(messageDataOffset+message.length);const index=instructionIndex==null?65535:instructionIndex;ED25519_INSTRUCTION_LAYOUT.encode({numSignatures:numSignatures,padding:0,signatureOffset:signatureOffset,signatureInstructionIndex:index,publicKeyOffset:publicKeyOffset,publicKeyInstructionIndex:index,messageDataOffset:messageDataOffset,messageDataSize:message.length,messageInstructionIndex:index},instructionData);instructionData.fill(publicKey,publicKeyOffset);instructionData.fill(signature,signatureOffset);instructionData.fill(message,messageDataOffset);return new TransactionInstruction({keys:[],programId:Ed25519Program.programId,data:instructionData})}static createInstructionWithPrivateKey(params){const{privateKey:privateKey,message:message,instructionIndex:instructionIndex}=params;assert$1(privateKey.length===PRIVATE_KEY_BYTES$1,`Private key must be ${PRIVATE_KEY_BYTES$1} bytes but received ${privateKey.length} bytes`);try{const keypair=Keypair.fromSecretKey(privateKey);const publicKey=keypair.publicKey.toBytes();const signature=sign(message,keypair.secretKey);return this.createInstructionWithPublicKey({publicKey:publicKey,message:message,signature:signature,instructionIndex:instructionIndex})}catch(error){throw new Error(`Error creating instruction; ${error}`)}}}Ed25519Program.programId=new PublicKey("Ed25519SigVerify111111111111111111111111111");const U32_MASK64=BigInt(2**32-1);const _32n=BigInt(32);function fromBig(n,le=false){if(le)return{h:Number(n&U32_MASK64),l:Number(n>>_32n&U32_MASK64)};return{h:Number(n>>_32n&U32_MASK64)|0,l:Number(n&U32_MASK64)|0}}function split(lst,le=false){let Ah=new Uint32Array(lst.length);let Al=new Uint32Array(lst.length);for(let i=0;i<lst.length;i++){const{h:h,l:l}=fromBig(lst[i],le);[Ah[i],Al[i]]=[h,l]}return[Ah,Al]}const rotlSH=(h,l,s)=>h<<s|l>>>32-s;const rotlSL=(h,l,s)=>l<<s|h>>>32-s;const rotlBH=(h,l,s)=>l<<s-32|h>>>64-s;const rotlBL=(h,l,s)=>h<<s-32|l>>>64-s;const SHA3_PI=[];const SHA3_ROTL=[];const _SHA3_IOTA=[];const _0n$1=BigInt(0);const _1n$2=BigInt(1);const _2n$1=BigInt(2);const _7n=BigInt(7);const _256n=BigInt(256);const _0x71n=BigInt(113);for(let round=0,R=_1n$2,x=1,y=0;round<24;round++){[x,y]=[y,(2*x+3*y)%5];SHA3_PI.push(2*(5*y+x));SHA3_ROTL.push((round+1)*(round+2)/2%64);let t=_0n$1;for(let j=0;j<7;j++){R=(R<<_1n$2^(R>>_7n)*_0x71n)%_256n;if(R&_2n$1)t^=_1n$2<<(_1n$2<<BigInt(j))-_1n$2}_SHA3_IOTA.push(t)}const[SHA3_IOTA_H,SHA3_IOTA_L]=split(_SHA3_IOTA,true);const rotlH=(h,l,s)=>s>32?rotlBH(h,l,s):rotlSH(h,l,s);const rotlL=(h,l,s)=>s>32?rotlBL(h,l,s):rotlSL(h,l,s);function keccakP(s,rounds=24){const B=new Uint32Array(5*2);for(let round=24-rounds;round<24;round++){for(let x=0;x<10;x++)B[x]=s[x]^s[x+10]^s[x+20]^s[x+30]^s[x+40];for(let x=0;x<10;x+=2){const idx1=(x+8)%10;const idx0=(x+2)%10;const B0=B[idx0];const B1=B[idx0+1];const Th=rotlH(B0,B1,1)^B[idx1];const Tl=rotlL(B0,B1,1)^B[idx1+1];for(let y=0;y<50;y+=10){s[x+y]^=Th;s[x+y+1]^=Tl}}let curH=s[2];let curL=s[3];for(let t=0;t<24;t++){const shift=SHA3_ROTL[t];const Th=rotlH(curH,curL,shift);const Tl=rotlL(curH,curL,shift);const PI=SHA3_PI[t];curH=s[PI];curL=s[PI+1];s[PI]=Th;s[PI+1]=Tl}for(let y=0;y<50;y+=10){for(let x=0;x<10;x++)B[x]=s[y+x];for(let x=0;x<10;x++)s[y+x]^=~B[(x+2)%10]&B[(x+4)%10]}s[0]^=SHA3_IOTA_H[round];s[1]^=SHA3_IOTA_L[round]}B.fill(0)}class Keccak extends Hash{constructor(blockLen,suffix,outputLen,enableXOF=false,rounds=24){super();this.blockLen=blockLen;this.suffix=suffix;this.outputLen=outputLen;this.enableXOF=enableXOF;this.rounds=rounds;this.pos=0;this.posOut=0;this.finished=false;this.destroyed=false;anumber(outputLen);if(0>=this.blockLen||this.blockLen>=200)throw new Error("Sha3 supports only keccak-f1600 function");this.state=new Uint8Array(200);this.state32=u32(this.state)}keccak(){if(!isLE)byteSwap32(this.state32);keccakP(this.state32,this.rounds);if(!isLE)byteSwap32(this.state32);this.posOut=0;this.pos=0}update(data){aexists(this);const{blockLen:blockLen,state:state}=this;data=toBytes(data);const len=data.length;for(let pos=0;pos<len;){const take=Math.min(blockLen-this.pos,len-pos);for(let i=0;i<take;i++)state[this.pos++]^=data[pos++];if(this.pos===blockLen)this.keccak()}return this}finish(){if(this.finished)return;this.finished=true;const{state:state,suffix:suffix,pos:pos,blockLen:blockLen}=this;state[pos]^=suffix;if((suffix&128)!==0&&pos===blockLen-1)this.keccak();state[blockLen-1]^=128;this.keccak()}writeInto(out){aexists(this,false);abytes(out);this.finish();const bufferOut=this.state;const{blockLen:blockLen}=this;for(let pos=0,len=out.length;pos<len;){if(this.posOut>=blockLen)this.keccak();const take=Math.min(blockLen-this.posOut,len-pos);out.set(bufferOut.subarray(this.posOut,this.posOut+take),pos);this.posOut+=take;pos+=take}return out}xofInto(out){if(!this.enableXOF)throw new Error("XOF is not possible for this instance");return this.writeInto(out)}xof(bytes){anumber(bytes);return this.xofInto(new Uint8Array(bytes))}digestInto(out){aoutput(out,this);if(this.finished)throw new Error("digest() was already called");this.writeInto(out);this.destroy();return out}digest(){return this.digestInto(new Uint8Array(this.outputLen))}destroy(){this.destroyed=true;this.state.fill(0)}_cloneInto(to){const{blockLen:blockLen,suffix:suffix,outputLen:outputLen,rounds:rounds,enableXOF:enableXOF}=this;to||(to=new Keccak(blockLen,suffix,outputLen,enableXOF,rounds));to.state32.set(this.state32);to.pos=this.pos;to.posOut=this.posOut;to.finished=this.finished;to.rounds=rounds;to.suffix=suffix;to.outputLen=outputLen;to.enableXOF=enableXOF;to.destroyed=this.destroyed;return to}}const gen=(suffix,blockLen,outputLen)=>wrapConstructor((()=>new Keccak(blockLen,suffix,outputLen)));const keccak_256=gen(1,136,256/8);const SHA256_K=new Uint32Array([1116352408,1899447441,3049323471,3921009573,961987163,1508970993,2453635748,2870763221,3624381080,310598401,607225278,1426881987,1925078388,2162078206,2614888103,3248222580,3835390401,4022224774,264347078,604807628,770255983,1249150122,1555081692,1996064986,2554220882,2821834349,2952996808,3210313671,3336571891,3584528711,113926993,338241895,666307205,773529912,1294757372,1396182291,1695183700,1986661051,2177026350,2456956037,2730485921,2820302411,3259730800,3345764771,3516065817,3600352804,4094571909,275423344,430227734,506948616,659060556,883997877,958139571,1322822218,1537002063,1747873779,1955562222,2024104815,2227730452,2361852424,2428436474,2756734187,3204031479,3329325298]);const SHA256_IV=new Uint32Array([1779033703,3144134277,1013904242,2773480762,1359893119,2600822924,528734635,1541459225]);const SHA256_W=new Uint32Array(64);class SHA256 extends HashMD$1{constructor(){super(64,32,8,false);this.A=SHA256_IV[0]|0;this.B=SHA256_IV[1]|0;this.C=SHA256_IV[2]|0;this.D=SHA256_IV[3]|0;this.E=SHA256_IV[4]|0;this.F=SHA256_IV[5]|0;this.G=SHA256_IV[6]|0;this.H=SHA256_IV[7]|0}get(){const{A:A,B:B,C:C,D:D,E:E,F:F,G:G,H:H}=this;return[A,B,C,D,E,F,G,H]}set(A,B,C,D,E,F,G,H){this.A=A|0;this.B=B|0;this.C=C|0;this.D=D|0;this.E=E|0;this.F=F|0;this.G=G|0;this.H=H|0}process(view,offset){for(let i=0;i<16;i++,offset+=4)SHA256_W[i]=view.getUint32(offset,false);for(let i=16;i<64;i++){const W15=SHA256_W[i-15];const W2=SHA256_W[i-2];const s0=rotr$1(W15,7)^rotr$1(W15,18)^W15>>>3;const s1=rotr$1(W2,17)^rotr$1(W2,19)^W2>>>10;SHA256_W[i]=s1+SHA256_W[i-7]+s0+SHA256_W[i-16]|0}let{A:A,B:B,C:C,D:D,E:E,F:F,G:G,H:H}=this;for(let i=0;i<64;i++){const sigma1=rotr$1(E,6)^rotr$1(E,11)^rotr$1(E,25);const T1=H+sigma1+Chi$1(E,F,G)+SHA256_K[i]+SHA256_W[i]|0;const sigma0=rotr$1(A,2)^rotr$1(A,13)^rotr$1(A,22);const T2=sigma0+Maj$1(A,B,C)|0;H=G;G=F;F=E;E=D+T1|0;D=C;C=B;B=A;A=T1+T2|0}A=A+this.A|0;B=B+this.B|0;C=C+this.C|0;D=D+this.D|0;E=E+this.E|0;F=F+this.F|0;G=G+this.G|0;H=H+this.H|0;this.set(A,B,C,D,E,F,G,H)}roundClean(){SHA256_W.fill(0)}destroy(){this.set(0,0,0,0,0,0,0,0);this.buffer.fill(0)}}const sha256=wrapConstructor$1((()=>new SHA256));class HMAC extends Hash$1{constructor(hash,_key){super();this.finished=false;this.destroyed=false;ahash(hash);const key=toBytes$1(_key);this.iHash=hash.create();if(typeof this.iHash.update!=="function")throw new Error("Expected instance of class which extends utils.Hash");this.blockLen=this.iHash.blockLen;this.outputLen=this.iHash.outputLen;const blockLen=this.blockLen;const pad=new Uint8Array(blockLen);pad.set(key.length>blockLen?hash.create().update(key).digest():key);for(let i=0;i<pad.length;i++)pad[i]^=54;this.iHash.update(pad);this.oHash=hash.create();for(let i=0;i<pad.length;i++)pad[i]^=54^92;this.oHash.update(pad);pad.fill(0)}update(buf){aexists$1(this);this.iHash.update(buf);return this}digestInto(out){aexists$1(this);abytes$2(out,this.outputLen);this.finished=true;this.iHash.digestInto(out);this.oHash.update(out);this.oHash.digestInto(out);this.destroy()}digest(){const out=new Uint8Array(this.oHash.outputLen);this.digestInto(out);return out}_cloneInto(to){to||(to=Object.create(Object.getPrototypeOf(this),{}));const{oHash:oHash,iHash:iHash,finished:finished,destroyed:destroyed,blockLen:blockLen,outputLen:outputLen}=this;to=to;to.finished=finished;to.destroyed=destroyed;to.blockLen=blockLen;to.outputLen=outputLen;to.oHash=oHash._cloneInto(to.oHash);to.iHash=iHash._cloneInto(to.iHash);return to}destroy(){this.destroyed=true;this.oHash.destroy();this.iHash.destroy()}}const hmac=(hash,key,message)=>new HMAC(hash,key).update(message).digest();hmac.create=(hash,key)=>new HMAC(hash,key)
./fincept-qt/resources/wallet/vendor/web3.js:17:/*! noble-curves - MIT License (c) 2022 Paul Miller (paulmillr.com) */;function validateSigVerOpts(opts){if(opts.lowS!==undefined)abool("lowS",opts.lowS);if(opts.prehash!==undefined)abool("prehash",opts.prehash)}function validatePointOpts(curve){const opts=validateBasic(curve);validateObject(opts,{a:"field",b:"field"},{allowedPrivateKeyLengths:"array",wrapPrivateKey:"boolean",isTorsionFree:"function",clearCofactor:"function",allowInfinityPoint:"boolean",fromBytes:"function",toBytes:"function"});const{endo:endo,Fp:Fp,a:a}=opts;if(endo){if(!Fp.eql(a,Fp.ZERO)){throw new Error("invalid endomorphism, can only be defined for Koblitz curves that have a=0")}if(typeof endo!=="object"||typeof endo.beta!=="bigint"||typeof endo.splitScalar!=="function"){throw new Error("invalid endomorphism, expected beta: bigint and splitScalar: function")}}return Object.freeze({...opts})}const{bytesToNumberBE:b2n,hexToBytes:h2b}=ut;const DER={Err:class DERErr extends Error{constructor(m=""){super(m)}},_tlv:{encode:(tag,data)=>{const{Err:E}=DER;if(tag<0||tag>256)throw new E("tlv.encode: wrong tag");if(data.length&1)throw new E("tlv.encode: unpadded data");const dataLen=data.length/2;const len=numberToHexUnpadded(dataLen);if(len.length/2&128)throw new E("tlv.encode: long form length too big");const lenLen=dataLen>127?numberToHexUnpadded(len.length/2|128):"";const t=numberToHexUnpadded(tag);return t+lenLen+len+data},decode(tag,data){const{Err:E}=DER;let pos=0;if(tag<0||tag>256)throw new E("tlv.encode: wrong tag");if(data.length<2||data[pos++]!==tag)throw new E("tlv.decode: wrong tlv");const first=data[pos++];const isLong=!!(first&128);let length=0;if(!isLong)length=first;else{const lenLen=first&127;if(!lenLen)throw new E("tlv.decode(long): indefinite length not supported");if(lenLen>4)throw new E("tlv.decode(long): byte length is too big");const lengthBytes=data.subarray(pos,pos+lenLen);if(lengthBytes.length!==lenLen)throw new E("tlv.decode: length bytes not complete");if(lengthBytes[0]===0)throw new E("tlv.decode(long): zero leftmost byte");for(const b of lengthBytes)length=length<<8|b;pos+=lenLen;if(length<128)throw new E("tlv.decode(long): not minimal encoding")}const v=data.subarray(pos,pos+length);if(v.length!==length)throw new E("tlv.decode: wrong value length");return{v:v,l:data.subarray(pos+length)}}},_int:{encode(num){const{Err:E}=DER;if(num<_0n)throw new E("integer: negative integers are not allowed");let hex=numberToHexUnpadded(num);if(Number.parseInt(hex[0],16)&8)hex="00"+hex;if(hex.length&1)throw new E("unexpected DER parsing assertion: unpadded hex");return hex},decode(data){const{Err:E}=DER;if(data[0]&128)throw new E("invalid signature integer: negative");if(data[0]===0&&!(data[1]&128))throw new E("invalid signature integer: unnecessary leading zero");return b2n(data)}},toSig(hex){const{Err:E,_int:int,_tlv:tlv}=DER;const data=typeof hex==="string"?h2b(hex):hex;abytes$1(data);const{v:seqBytes,l:seqLeftBytes}=tlv.decode(48,data);if(seqLeftBytes.length)throw new E("invalid signature: left bytes after parsing");const{v:rBytes,l:rLeftBytes}=tlv.decode(2,seqBytes);const{v:sBytes,l:sLeftBytes}=tlv.decode(2,rLeftBytes);if(sLeftBytes.length)throw new E("invalid signature: left bytes after parsing");return{r:int.decode(rBytes),s:int.decode(sBytes)}},hexFromSig(sig){const{_tlv:tlv,_int:int}=DER;const rs=tlv.encode(2,int.encode(sig.r));const ss=tlv.encode(2,int.encode(sig.s));const seq=rs+ss;return tlv.encode(48,seq)}};const _0n=BigInt(0),_1n$1=BigInt(1);BigInt(2);const _3n=BigInt(3);BigInt(4);function weierstrassPoints(opts){const CURVE=validatePointOpts(opts);const{Fp:Fp}=CURVE;const Fn=Field(CURVE.n,CURVE.nBitLength);const toBytes=CURVE.toBytes||((_c,point,_isCompressed)=>{const a=point.toAffine();return concatBytes(Uint8Array.from([4]),Fp.toBytes(a.x),Fp.toBytes(a.y))});const fromBytes=CURVE.fromBytes||(bytes=>{const tail=bytes.subarray(1);const x=Fp.fromBytes(tail.subarray(0,Fp.BYTES));const y=Fp.fromBytes(tail.subarray(Fp.BYTES,2*Fp.BYTES));return{x:x,y:y}});function weierstrassEquation(x){const{a:a,b:b}=CURVE;const x2=Fp.sqr(x);const x3=Fp.mul(x2,x);return Fp.add(Fp.add(x3,Fp.mul(x,a)),b)}if(!Fp.eql(Fp.sqr(CURVE.Gy),weierstrassEquation(CURVE.Gx)))throw new Error("bad generator point: equation left != right");function isWithinCurveOrder(num){return inRange(num,_1n$1,CURVE.n)}function normPrivateKeyToScalar(key){const{allowedPrivateKeyLengths:lengths,nByteLength:nByteLength,wrapPrivateKey:wrapPrivateKey,n:N}=CURVE;if(lengths&&typeof key!=="bigint"){if(isBytes$1(key))key=bytesToHex(key);if(typeof key!=="string"||!lengths.includes(key.length))throw new Error("invalid private key");key=key.padStart(nByteLength*2,"0")}let num;try{num=typeof key==="bigint"?key:bytesToNumberBE(ensureBytes("private key",key,nByteLength))}catch(error){throw new Error("invalid private key, expected hex or "+nByteLength+" bytes, got "+typeof key)}if(wrapPrivateKey)num=mod(num,N);aInRange("private key",num,_1n$1,N);return num}function assertPrjPoint(other){if(!(other instanceof Point))throw new Error("ProjectivePoint expected")}const toAffineMemo=memoized(((p,iz)=>{const{px:x,py:y,pz:z}=p;if(Fp.eql(z,Fp.ONE))return{x:x,y:y};const is0=p.is0();if(iz==null)iz=is0?Fp.ONE:Fp.inv(z);const ax=Fp.mul(x,iz);const ay=Fp.mul(y,iz);const zz=Fp.mul(z,iz);if(is0)return{x:Fp.ZERO,y:Fp.ZERO};if(!Fp.eql(zz,Fp.ONE))throw new Error("invZ was invalid");return{x:ax,y:ay}}));const assertValidMemo=memoized((p=>{if(p.is0()){if(CURVE.allowInfinityPoint&&!Fp.is0(p.py))return;throw new Error("bad point: ZERO")}const{x:x,y:y}=p.toAffine();if(!Fp.isValid(x)||!Fp.isValid(y))throw new Error("bad point: x or y not FE");const left=Fp.sqr(y);const right=weierstrassEquation(x);if(!Fp.eql(left,right))throw new Error("bad point: equation left != right");if(!p.isTorsionFree())throw new Error("bad point: not in prime-order subgroup");return true}));class Point{constructor(px,py,pz){this.px=px;this.py=py;this.pz=pz;if(px==null||!Fp.isValid(px))throw new Error("x required");if(py==null||!Fp.isValid(py))throw new Error("y required");if(pz==null||!Fp.isValid(pz))throw new Error("z required");Object.freeze(this)}static fromAffine(p){const{x:x,y:y}=p||{};if(!p||!Fp.isValid(x)||!Fp.isValid(y))throw new Error("invalid affine point");if(p instanceof Point)throw new Error("projective point not allowed");const is0=i=>Fp.eql(i,Fp.ZERO);if(is0(x)&&is0(y))return Point.ZERO;return new Point(x,y,Fp.ONE)}get x(){return this.toAffine().x}get y(){return this.toAffine().y}static normalizeZ(points){const toInv=Fp.invertBatch(points.map((p=>p.pz)));return points.map(((p,i)=>p.toAffine(toInv[i]))).map(Point.fromAffine)}static fromHex(hex){const P=Point.fromAffine(fromBytes(ensureBytes("pointHex",hex)));P.assertValidity();return P}static fromPrivateKey(privateKey){return Point.BASE.multiply(normPrivateKeyToScalar(privateKey))}static msm(points,scalars){return pippenger(Point,Fn,points,scalars)}_setWindowSize(windowSize){wnaf.setWindowSize(this,windowSize)}assertValidity(){assertValidMemo(this)}hasEvenY(){const{y:y}=this.toAffine();if(Fp.isOdd)return!Fp.isOdd(y);throw new Error("Field doesn't support isOdd")}equals(other){assertPrjPoint(other);const{px:X1,py:Y1,pz:Z1}=this;const{px:X2,py:Y2,pz:Z2}=other;const U1=Fp.eql(Fp.mul(X1,Z2),Fp.mul(X2,Z1));const U2=Fp.eql(Fp.mul(Y1,Z2),Fp.mul(Y2,Z1));return U1&&U2}negate(){return new Point(this.px,Fp.neg(this.py),this.pz)}double(){const{a:a,b:b}=CURVE;const b3=Fp.mul(b,_3n);const{px:X1,py:Y1,pz:Z1}=this;let X3=Fp.ZERO,Y3=Fp.ZERO,Z3=Fp.ZERO;let t0=Fp.mul(X1,X1);let t1=Fp.mul(Y1,Y1);let t2=Fp.mul(Z1,Z1);let t3=Fp.mul(X1,Y1);t3=Fp.add(t3,t3);Z3=Fp.mul(X1,Z1);Z3=Fp.add(Z3,Z3);X3=Fp.mul(a,Z3);Y3=Fp.mul(b3,t2);Y3=Fp.add(X3,Y3);X3=Fp.sub(t1,Y3);Y3=Fp.add(t1,Y3);Y3=Fp.mul(X3,Y3);X3=Fp.mul(t3,X3);Z3=Fp.mul(b3,Z3);t2=Fp.mul(a,t2);t3=Fp.sub(t0,t2);t3=Fp.mul(a,t3);t3=Fp.add(t3,Z3);Z3=Fp.add(t0,t0);t0=Fp.add(Z3,t0);t0=Fp.add(t0,t2);t0=Fp.mul(t0,t3);Y3=Fp.add(Y3,t0);t2=Fp.mul(Y1,Z1);t2=Fp.add(t2,t2);t0=Fp.mul(t2,t3);X3=Fp.sub(X3,t0);Z3=Fp.mul(t2,t1);Z3=Fp.add(Z3,Z3);Z3=Fp.add(Z3,Z3);return new Point(X3,Y3,Z3)}add(other){assertPrjPoint(other);const{px:X1,py:Y1,pz:Z1}=this;const{px:X2,py:Y2,pz:Z2}=other;let X3=Fp.ZERO,Y3=Fp.ZERO,Z3=Fp.ZERO;const a=CURVE.a;const b3=Fp.mul(CURVE.b,_3n);let t0=Fp.mul(X1,X2);let t1=Fp.mul(Y1,Y2);let t2=Fp.mul(Z1,Z2);let t3=Fp.add(X1,Y1);let t4=Fp.add(X2,Y2);t3=Fp.mul(t3,t4);t4=Fp.add(t0,t1);t3=Fp.sub(t3,t4);t4=Fp.add(X1,Z1);let t5=Fp.add(X2,Z2);t4=Fp.mul(t4,t5);t5=Fp.add(t0,t2);t4=Fp.sub(t4,t5);t5=Fp.add(Y1,Z1);X3=Fp.add(Y2,Z2);t5=Fp.mul(t5,X3);X3=Fp.add(t1,t2);t5=Fp.sub(t5,X3);Z3=Fp.mul(a,t4);X3=Fp.mul(b3,t2);Z3=Fp.add(X3,Z3);X3=Fp.sub(t1,Z3);Z3=Fp.add(t1,Z3);Y3=Fp.mul(X3,Z3);t1=Fp.add(t0,t0);t1=Fp.add(t1,t0);t2=Fp.mul(a,t2);t4=Fp.mul(b3,t4);t1=Fp.add(t1,t2);t2=Fp.sub(t0,t2);t2=Fp.mul(a,t2);t4=Fp.add(t4,t2);t0=Fp.mul(t1,t4);Y3=Fp.add(Y3,t0);t0=Fp.mul(t5,t4);X3=Fp.mul(t3,X3);X3=Fp.sub(X3,t0);t0=Fp.mul(t3,t1);Z3=Fp.mul(t5,Z3);Z3=Fp.add(Z3,t0);return new Point(X3,Y3,Z3)}subtract(other){return this.add(other.negate())}is0(){return this.equals(Point.ZERO)}wNAF(n){return wnaf.wNAFCached(this,n,Point.normalizeZ)}multiplyUnsafe(sc){const{endo:endo,n:N}=CURVE;aInRange("scalar",sc,_0n,N);const I=Point.ZERO;if(sc===_0n)return I;if(this.is0()||sc===_1n$1)return this;if(!endo||wnaf.hasPrecomputes(this))return wnaf.wNAFCachedUnsafe(this,sc,Point.normalizeZ);let{k1neg:k1neg,k1:k1,k2neg:k2neg,k2:k2}=endo.splitScalar(sc);let k1p=I;let k2p=I;let d=this;while(k1>_0n||k2>_0n){if(k1&_1n$1)k1p=k1p.add(d);if(k2&_1n$1)k2p=k2p.add(d);d=d.double();k1>>=_1n$1;k2>>=_1n$1}if(k1neg)k1p=k1p.negate();if(k2neg)k2p=k2p.negate();k2p=new Point(Fp.mul(k2p.px,endo.beta),k2p.py,k2p.pz);return k1p.add(k2p)}multiply(scalar){const{endo:endo,n:N}=CURVE;aInRange("scalar",scalar,_1n$1,N);let point,fake;if(endo){const{k1neg:k1neg,k1:k1,k2neg:k2neg,k2:k2}=endo.splitScalar(scalar);let{p:k1p,f:f1p}=this.wNAF(k1);let{p:k2p,f:f2p}=this.wNAF(k2);k1p=wnaf.constTimeNegate(k1neg,k1p);k2p=wnaf.constTimeNegate(k2neg,k2p);k2p=new Point(Fp.mul(k2p.px,endo.beta),k2p.py,k2p.pz);point=k1p.add(k2p);fake=f1p.add(f2p)}else{const{p:p,f:f}=this.wNAF(scalar);point=p;fake=f}return Point.normalizeZ([point,fake])[0]}multiplyAndAddUnsafe(Q,a,b){const G=Point.BASE;const mul=(P,a)=>a===_0n||a===_1n$1||!P.equals(G)?P.multiplyUnsafe(a):P.multiply(a);const sum=mul(this,a).add(mul(Q,b));return sum.is0()?undefined:sum}toAffine(iz){return toAffineMemo(this,iz)}isTorsionFree(){const{h:cofactor,isTorsionFree:isTorsionFree}=CURVE;if(cofactor===_1n$1)return true;if(isTorsionFree)return isTorsionFree(Point,this);throw new Error("isTorsionFree() has not been declared for the elliptic curve")}clearCofactor(){const{h:cofactor,clearCofactor:clearCofactor}=CURVE;if(cofactor===_1n$1)return this;if(clearCofactor)return clearCofactor(Point,this);return this.multiplyUnsafe(CURVE.h)}toRawBytes(isCompressed=true){abool("isCompressed",isCompressed);this.assertValidity();return toBytes(Point,this,isCompressed)}toHex(isCompressed=true){abool("isCompressed",isCompressed);return bytesToHex(this.toRawBytes(isCompressed))}}Point.BASE=new Point(CURVE.Gx,CURVE.Gy,Fp.ONE);Point.ZERO=new Point(Fp.ZERO,Fp.ONE,Fp.ZERO);const _bits=CURVE.nBitLength;const wnaf=wNAF(Point,CURVE.endo?Math.ceil(_bits/2):_bits);return{CURVE:CURVE,ProjectivePoint:Point,normPrivateKeyToScalar:normPrivateKeyToScalar,weierstrassEquation:weierstrassEquation,isWithinCurveOrder:isWithinCurveOrder}}function validateOpts(curve){const opts=validateBasic(curve);validateObject(opts,{hash:"hash",hmac:"function",randomBytes:"function"},{bits2int:"function",bits2int_modN:"function",lowS:"boolean"});return Object.freeze({lowS:true,...opts})}function weierstrass(curveDef){const CURVE=validateOpts(curveDef);const{Fp:Fp,n:CURVE_ORDER}=CURVE;const compressedLen=Fp.BYTES+1;const uncompressedLen=2*Fp.BYTES+1;function modN(a){return mod(a,CURVE_ORDER)}function invN(a){return invert(a,CURVE_ORDER)}const{ProjectivePoint:Point,normPrivateKeyToScalar:normPrivateKeyToScalar,weierstrassEquation:weierstrassEquation,isWithinCurveOrder:isWithinCurveOrder}=weierstrassPoints({...CURVE,toBytes(_c,point,isCompressed){const a=point.toAffine();const x=Fp.toBytes(a.x);const cat=concatBytes;abool("isCompressed",isCompressed);if(isCompressed){return cat(Uint8Array.from([point.hasEvenY()?2:3]),x)}else{return cat(Uint8Array.from([4]),x,Fp.toBytes(a.y))}},fromBytes(bytes){const len=bytes.length;const head=bytes[0];const tail=bytes.subarray(1);if(len===compressedLen&&(head===2||head===3)){const x=bytesToNumberBE(tail);if(!inRange(x,_1n$1,Fp.ORDER))throw new Error("Point is not on curve");const y2=weierstrassEquation(x);let y;try{y=Fp.sqrt(y2)}catch(sqrtError){const suffix=sqrtError instanceof Error?": "+sqrtError.message:"";throw new Error("Point is not on curve"+suffix)}const isYOdd=(y&_1n$1)===_1n$1;const isHeadOdd=(head&1)===1;if(isHeadOdd!==isYOdd)y=Fp.neg(y);return{x:x,y:y}}else if(len===uncompressedLen&&head===4){const x=Fp.fromBytes(tail.subarray(0,Fp.BYTES));const y=Fp.fromBytes(tail.subarray(Fp.BYTES,2*Fp.BYTES));return{x:x,y:y}}else{const cl=compressedLen;const ul=uncompressedLen;throw new Error("invalid Point, expected length of "+cl+", or uncompressed "+ul+", got "+len)}}});const numToNByteStr=num=>bytesToHex(numberToBytesBE(num,CURVE.nByteLength));function isBiggerThanHalfOrder(number){const HALF=CURVE_ORDER>>_1n$1;return number>HALF}function normalizeS(s){return isBiggerThanHalfOrder(s)?modN(-s):s}const slcNum=(b,from,to)=>bytesToNumberBE(b.slice(from,to));class Signature{constructor(r,s,recovery){this.r=r;this.s=s;this.recovery=recovery;this.assertValidity()}static fromCompact(hex){const l=CURVE.nByteLength;hex=ensureBytes("compactSignature",hex,l*2);return new Signature(slcNum(hex,0,l),slcNum(hex,l,2*l))}static fromDER(hex){const{r:r,s:s}=DER.toSig(ensureBytes("DER",hex));return new Signature(r,s)}assertValidity(){aInRange("r",this.r,_1n$1,CURVE_ORDER);aInRange("s",this.s,_1n$1,CURVE_ORDER)}addRecoveryBit(recovery){return new Signature(this.r,this.s,recovery)}recoverPublicKey(msgHash){const{r:r,s:s,recovery:rec}=this;const h=bits2int_modN(ensureBytes("msgHash",msgHash));if(rec==null||![0,1,2,3].includes(rec))throw new Error("recovery id invalid");const radj=rec===2||rec===3?r+CURVE.n:r;if(radj>=Fp.ORDER)throw new Error("recovery id 2 or 3 invalid");const prefix=(rec&1)===0?"02":"03";const R=Point.fromHex(prefix+numToNByteStr(radj));const ir=invN(radj);const u1=modN(-h*ir);const u2=modN(s*ir);const Q=Point.BASE.multiplyAndAddUnsafe(R,u1,u2);if(!Q)throw new Error("point at infinify");Q.assertValidity();return Q}hasHighS(){return isBiggerThanHalfOrder(this.s)}normalizeS(){return this.hasHighS()?new Signature(this.r,modN(-this.s),this.recovery):this}toDERRawBytes(){return hexToBytes(this.toDERHex())}toDERHex(){return DER.hexFromSig({r:this.r,s:this.s})}toCompactRawBytes(){return hexToBytes(this.toCompactHex())}toCompactHex(){return numToNByteStr(this.r)+numToNByteStr(this.s)}}const utils={isValidPrivateKey(privateKey){try{normPrivateKeyToScalar(privateKey);return true}catch(error){return false}},normPrivateKeyToScalar:normPrivateKeyToScalar,randomPrivateKey:()=>{const length=getMinHashLength(CURVE.n);return mapHashToField(CURVE.randomBytes(length),CURVE.n)},precompute(windowSize=8,point=Point.BASE){point._setWindowSize(windowSize);point.multiply(BigInt(3));return point}};function getPublicKey(privateKey,isCompressed=true){return Point.fromPrivateKey(privateKey).toRawBytes(isCompressed)}function isProbPub(item){const arr=isBytes$1(item);const str=typeof item==="string";const len=(arr||str)&&item.length;if(arr)return len===compressedLen||len===uncompressedLen;if(str)return len===2*compressedLen||len===2*uncompressedLen;if(item instanceof Point)return true;return false}function getSharedSecret(privateA,publicB,isCompressed=true){if(isProbPub(privateA))throw new Error("first arg must be private key");if(!isProbPub(publicB))throw new Error("second arg must be public key");const b=Point.fromHex(publicB);return b.multiply(normPrivateKeyToScalar(privateA)).toRawBytes(isCompressed)}const bits2int=CURVE.bits2int||function(bytes){if(bytes.length>8192)throw new Error("input is too large");const num=bytesToNumberBE(bytes);const delta=bytes.length*8-CURVE.nBitLength;return delta>0?num>>BigInt(delta):num};const bits2int_modN=CURVE.bits2int_modN||function(bytes){return modN(bits2int(bytes))};const ORDER_MASK=bitMask(CURVE.nBitLength);function int2octets(num){aInRange("num < 2^"+CURVE.nBitLength,num,_0n,ORDER_MASK);return numberToBytesBE(num,CURVE.nByteLength)}function prepSig(msgHash,privateKey,opts=defaultSigOpts){if(["recovered","canonical"].some((k=>k in opts)))throw new Error("sign() legacy options not supported");const{hash:hash,randomBytes:randomBytes}=CURVE;let{lowS:lowS,prehash:prehash,extraEntropy:ent}=opts;if(lowS==null)lowS=true;msgHash=ensureBytes("msgHash",msgHash);validateSigVerOpts(opts);if(prehash)msgHash=ensureBytes("prehashed msgHash",hash(msgHash));const h1int=bits2int_modN(msgHash);const d=normPrivateKeyToScalar(privateKey);const seedArgs=[int2octets(d),int2octets(h1int)];if(ent!=null&&ent!==false){const e=ent===true?randomBytes(Fp.BYTES):ent;seedArgs.push(ensureBytes("extraEntropy",e))}const seed=concatBytes(...seedArgs);const m=h1int;function k2sig(kBytes){const k=bits2int(kBytes);if(!isWithinCurveOrder(k))return;const ik=invN(k);const q=Point.BASE.multiply(k).toAffine();const r=modN(q.x);if(r===_0n)return;const s=modN(ik*modN(m+r*d));if(s===_0n)return;let recovery=(q.x===r?0:2)|Number(q.y&_1n$1);let normS=s;if(lowS&&isBiggerThanHalfOrder(s)){normS=normalizeS(s);recovery^=1}return new Signature(r,normS,recovery)}return{seed:seed,k2sig:k2sig}}const defaultSigOpts={lowS:CURVE.lowS,prehash:false};const defaultVerOpts={lowS:CURVE.lowS,prehash:false};function sign(msgHash,privKey,opts=defaultSigOpts){const{seed:seed,k2sig:k2sig}=prepSig(msgHash,privKey,opts);const C=CURVE;const drbg=createHmacDrbg(C.hash.outputLen,C.nByteLength,C.hmac);return drbg(seed,k2sig)}Point.BASE._setWindowSize(8);function verify(signature,msgHash,publicKey,opts=defaultVerOpts){const sg=signature;msgHash=ensureBytes("msgHash",msgHash);publicKey=ensureBytes("publicKey",publicKey);const{lowS:lowS,prehash:prehash,format:format}=opts;validateSigVerOpts(opts);if("strict"in opts)throw new Error("options.strict was renamed to lowS");if(format!==undefined&&format!=="compact"&&format!=="der")throw new Error("format must be compact or der");const isHex=typeof sg==="string"||isBytes$1(sg);const isObj=!isHex&&!format&&typeof sg==="object"&&sg!==null&&typeof sg.r==="bigint"&&typeof sg.s==="bigint";if(!isHex&&!isObj)throw new Error("invalid signature, expected Uint8Array, hex string or Signature instance");let _sig=undefined;let P;try{if(isObj)_sig=new Signature(sg.r,sg.s);if(isHex){try{if(format!=="compact")_sig=Signature.fromDER(sg)}catch(derError){if(!(derError instanceof DER.Err))throw derError}if(!_sig&&format!=="der")_sig=Signature.fromCompact(sg)}P=Point.fromHex(publicKey)}catch(error){return false}if(!_sig)return false;if(lowS&&_sig.hasHighS())return false;if(prehash)msgHash=CURVE.hash(msgHash);const{r:r,s:s}=_sig;const h=bits2int_modN(msgHash);const is=invN(s);const u1=modN(h*is);const u2=modN(r*is);const R=Point.BASE.multiplyAndAddUnsafe(P,u1,u2)?.toAffine();if(!R)return false;const v=modN(R.x);return v===r}return{CURVE:CURVE,getPublicKey:getPublicKey,getSharedSecret:getSharedSecret,sign:sign,verify:verify,ProjectivePoint:Point,Signature:Signature,utils:utils}}
./fincept-qt/resources/component_catalog.json:10:    { "id": "crypto_trading",    "title": "Crypto Trading",     "category": "Trading",     "description": "Order entry + real-time book for Kraken / HyperLiquid",    "tags": ["crypto","trading","order"] },
./fincept-qt/resources/component_catalog.json:13:    { "id": "backtesting",       "title": "Backtesting",        "category": "Trading",     "description": "Historical strategy simulation and reporting",             "tags": ["backtest","simulation"] },
./fincept-qt/resources/component_catalog.json:16:    { "id": "portfolio",         "title": "Portfolio",          "category": "Research",    "description": "Holdings, P&L, allocation and performance attribution",    "tags": ["portfolio","pnl","holdings"] },
./fincept-qt/resources/component_catalog.json:23:    { "id": "quantlib",          "title": "QuantLib Suite",     "category": "QuantLib",    "description": "18 quantitative analysis tools — curves, models, risk",    "tags": ["quantlib","curves","models"] },
./fincept-qt/resources/component_catalog.json:24:    { "id": "ai_quant_lab",      "title": "AI Quant Lab",       "category": "AI",          "description": "ML factor discovery, HFT, RL trading, vision quant",       "tags": ["ai","quant","ml"] },
./fincept-qt/resources/component_catalog.json:26:    { "id": "agent_config",      "title": "Agent Config",       "category": "AI",          "description": "LLM agent framework configuration (hedge fund, macro)",    "tags": ["agents","llm","config"] },
./fincept-qt/resources/component_catalog.json:27:    { "id": "mcp_servers",       "title": "MCP Servers",        "category": "AI",          "description": "Model Context Protocol server management",                 "tags": ["mcp","tools","servers"] },
./fincept-qt/resources/component_catalog.json:30:    { "id": "economics",         "title": "Economics",          "category": "Economics",   "description": "Macro dashboards — FRED, IMF, World Bank, OECD",          "tags": ["economics","macro","fred"] },
./fincept-qt/resources/component_catalog.json:32:    { "id": "akshare",           "title": "AkShare Data",       "category": "Economics",   "description": "China markets and alternative data",                      "tags": ["akshare","china","data"] },
./fincept-qt/resources/component_catalog.json:45:    { "id": "data_sources",      "title": "Data Sources",       "category": "Tools",       "description": "100+ connectors — APIs, DBs, websockets",                  "tags": ["data","sources","connectors"] },
./fincept-qt/resources/component_catalog.json:46:    { "id": "data_mapping",      "title": "Data Mapping",       "category": "Tools",       "description": "Transform and route between data sources",                "tags": ["mapping","etl","transform"] },
./fincept-qt/resources/component_catalog.json:52:    { "id": "settings",          "title": "Settings",           "category": "Community",   "description": "Preferences, keybindings, themes, voice, LLM",            "tags": ["settings","preferences"] },
./fincept-qt/tests/CMakeLists.txt:38:# ── MCP schema validator tests (Phase 3) ────────────────────────────────────
./fincept-qt/tests/CMakeLists.txt:40:# No dependency on the rest of the MCP system — McpProvider/McpService are not linked.
./fincept-qt/tests/CMakeLists.txt:63:# ── MCP async dispatch tests (Phase 4) ──────────────────────────────────────
./fincept-qt/tests/CMakeLists.txt:90:# ── MCP dispatcher tests (Phase 5) ──────────────────────────────────────────
./fincept-qt/tests/mcp/test_dispatcher.cpp:4:// pre-registered MCP tools. Confirms:
./fincept-qt/docs/MCP_TOOLS_GUIDE.md:1:# MCP Tools — Author & Maintainer Guide
./fincept-qt/docs/MCP_TOOLS_GUIDE.md:3:This guide documents how the Model Context Protocol (MCP) tool system works
./fincept-qt/docs/MCP_TOOLS_GUIDE.md:4:inside Fincept Terminal after the 6-phase refactor (see
./fincept-qt/docs/MCP_TOOLS_GUIDE.md:5:`fincept-qt/plans/mcp-refactor-INDEX.md`).
./fincept-qt/docs/MCP_TOOLS_GUIDE.md:8:debugging why an LLM call isn't hitting your tool, jump to **§6 Diagnosis**.
./fincept-qt/docs/MCP_TOOLS_GUIDE.md:124:| `Authenticated` | Authenticated reads (portfolios, settings reads) |
./fincept-qt/docs/MCP_TOOLS_GUIDE.md:145:   existing category (markets, news, portfolio, …), append to that file. If
./fincept-qt/docs/MCP_TOOLS_GUIDE.md:160:6. **Register the factory** in your module's `get_X_tools()` returning
./fincept-qt/docs/MCP_TOOLS_GUIDE.md:165:   (`MCP_SOURCES` and the `SKIP_UNITY_BUILD_INCLUSION` list in `CMakeLists.txt`).
./fincept-qt/docs/MCP_TOOLS_GUIDE.md:180:t.legacy_aliases = {"get_quote"};   // saved chats / Finagent workflows still resolve
./fincept-qt/docs/MCP_TOOLS_GUIDE.md:191:- Did your factory return it? `tools.push_back(std::move(t))` at the end.
./fincept-qt/docs/MCP_TOOLS_GUIDE.md:192:- Is your factory registered in `McpInit.cpp`?
./fincept-qt/docs/MCP_TOOLS_GUIDE.md:193:- Is your module's `.cpp` listed in `MCP_SOURCES`?
./fincept-qt/docs/MCP_TOOLS_GUIDE.md:206:- Check the LLM's argument shape — sometimes it nests args inside an
./fincept-qt/docs/MCP_TOOLS_GUIDE.md:224:- Refactor plans: `fincept-qt/plans/mcp-refactor-phase-{1..6}-*.md`
./fincept-qt/docs/MCP_TOOLS_GUIDE.md:225:- Refactor index: `fincept-qt/plans/mcp-refactor-INDEX.md`
./fincept-qt/docs/datahub-phases/phase-06-economics-dbnomics.md:13:(most FRED, World Bank, IMF series update daily at most; many
./fincept-qt/docs/datahub-phases/phase-06-economics-dbnomics.md:35:Memory: the economics tab was already refactored to per-source
./fincept-qt/docs/datahub-phases/phase-06-economics-dbnomics.md:43:  `src/screens/economics/panels/` (FRED, World Bank, IMF, OECD,
./fincept-qt/docs/datahub-phases/phase-06-economics-dbnomics.md:82:on refresh can't hammer FRED. This is a small, contained addition to
./fincept-qt/docs/datahub-phases/phase-06-economics-dbnomics.md:97:### FRED / long-TTL warm-start
./fincept-qt/docs/datahub-phases/phase-06-economics-dbnomics.md:140:- Open a FRED panel (GDP) and a World Bank panel (same metric) in
./fincept-qt/docs/datahub-phases/phase-06-economics-dbnomics.md:161:  refactor created a per-source panel architecture). Migrate the
./fincept-qt/docs/datahub-phases/phase-06-economics-dbnomics.md:173:- **FRED API key gating.** Users without a FRED key fall through to
./fincept-qt/docs/datahub-phases/phase-06-economics-dbnomics.md:186:  "loading" state on startup. No data-correctness risk.
./fincept-qt/docs/datahub-phases/phase-06-economics-dbnomics.md:197:- QuantLib Economics tab (different data flow — internal models,
./fincept-qt/docs/datahub-phases/phase-06-economics-dbnomics.md:200:- MCP `economics_tools` module — Phase 9.
./fincept-qt/docs/datahub-phases/phase-08-geopolitics-maritime-govdata.md:7:**Rough size:** Medium (5 services, cold data, low risk)
./fincept-qt/docs/datahub-phases/phase-08-geopolitics-maritime-govdata.md:61:  published when an agent produces analysis. TTL 6 h (effectively
./fincept-qt/docs/datahub-phases/phase-08-geopolitics-maritime-govdata.md:134:  established. The main risk is simple bugs from repetitive work —
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:1:# Phase 9 — AI / MCP / Agents Integration
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:4:**Depends on:** Phases 3, 4, 5 (and ideally 6, 7, 8 — agents benefit
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:8:**Rough size:** Medium (24 MCP modules lightly touched, 1 new MCP
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:9:module, agent helper added)
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:15:Let the AI surface — MCP tools, agent frameworks, LLM chat — read
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:17:that a visible screen already has streaming; LLM tool calls become
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:21:Critically: **agents are subscribers, not producers.** They don't
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:22:publish their own topics (except a narrow set of agent-output
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:24:reading from the hub, into the agent world.
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:30:### MCP tool modules — 24 modules
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:49:### New MCP module — `DataHubTools`
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:51:A generic introspection surface for LLMs:
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:54:  Lets the LLM "see" what data is currently flowing and reason
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:69:Under `src/services/agents/`. Add `AgentContext::peek(topic)` and
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:89:A small set of agent-produced topics, so the UI can subscribe to
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:90:agent analyses the same way it subscribes to market data:
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:92:- `agent:<agent_id>:status` — running / idle / error.
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:93:- `agent:<agent_id>:output:<run_id>` — final output of a run.
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:94:- `agent:<agent_id>:stream:<run_id>` — streamed intermediate tokens
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:101:### LLM chat integration
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:103:`LlmService` / AI Chat screen currently streams LLM responses via
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:106:screens that want to observe an ongoing LLM conversation (e.g.
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:107:AgentConfig showing an agent's internal reasoning in real time).
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:113:- `DataHubTools` MCP module implemented and registered in the MCP
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:115:- Existing MCP tool modules (the ~10 listed above) modified: their
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:117:  preserving the tool API surface as seen by the LLM.
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:119:- `AgentService` implements Producer for `agent:*` topics.
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:122:- `docs/agents/datahub-guide.md` (new short doc) — one page
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:123:  explaining how agents should use the hub, with a code example.
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:130:- An LLM tool-use: "What is the current price of AAPL?" — the
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:134:- Open AI Chat and run an agent; AgentConfig panel (separate
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:135:  screen) subscribes to `agent:<id>:stream:<run>` and shows the
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:137:- `datahub_list_topics` MCP call: LLM receives a JSON structure
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:139:  Useful for debug and for LLMs to reason about what "the
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:141:- An Agno Trading agent running in the background subscribes to
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:143:  viewing AAPL, the agent's data comes entirely from the hub's
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:166:- **LLM reasoning on stale cache.** `peek` returns whatever is
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:167:  cached; if the cache is 30 s old (within TTL), the LLM gets
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:169:  response includes `age_ms` alongside the value; LLM-facing tool
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:171:- **Agent output topic explosion.** If a trading agent publishes
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:172:  `agent:<id>:output:<run>` per trade and runs 1000 simulated
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:178:  to the Python bridge expands the public Python API for agent
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:186:- Revert per-MCP-module changes — tools fall back to direct
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:189:  LLM tool catalog shrinks, no caller breaks.
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:192:- Agent Python helpers are additive; no agent is forced to use
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:193:  them yet. Existing agents keep working.
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:199:- Rewriting the LLM chat stream engine — out of scope; only
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:201:- New agent frameworks beyond the existing ones.
./fincept-qt/docs/datahub-phases/phase-09-ai-mcp-agents.md:202:- Changing MCP tool schemas visible to external MCP clients —
./fincept-qt/docs/datahub-phases/phase-03-market-data-full-migration.md:28:(which backs four dashboard factories: Indices, Crypto, Forex,
./fincept-qt/docs/datahub-phases/phase-03-market-data-full-migration.md:60:| `PortfolioBlotter`      | `src/screens/portfolio/PortfolioBlotter.cpp`                             |
./fincept-qt/docs/datahub-phases/phase-03-market-data-full-migration.md:106:  entry point for market data, instead of the existing batched-calls
./fincept-qt/docs/datahub-phases/phase-03-market-data-full-migration.md:180:- WebSocket tick feeds (Kraken, HyperLiquid, broker streams) — Phase 4
./fincept-qt/docs/datahub-phases/phase-07-broker-account-streams.md:19:The payoff: a user with three brokers (Zerodha + IBKR + Kraken) and
./fincept-qt/docs/datahub-phases/phase-07-broker-account-streams.md:20:two screens open (dashboard portfolio summary + equity trading
./fincept-qt/docs/datahub-phases/phase-07-broker-account-streams.md:23:the largest wins in this refactor.
./fincept-qt/docs/datahub-phases/phase-07-broker-account-streams.md:48:  phase refactors to publish to the hub per-account.
./fincept-qt/docs/datahub-phases/phase-07-broker-account-streams.md:106:### `AccountDataStream` / `DataStreamManager` refactor
./fincept-qt/docs/datahub-phases/phase-07-broker-account-streams.md:143:  portfolio summary visible. Log shows one active Zerodha WS
./fincept-qt/docs/datahub-phases/phase-07-broker-account-streams.md:159:- Tick feed consolidation: open CryptoWidget (Kraken via
./fincept-qt/docs/datahub-phases/phase-07-broker-account-streams.md:191:  broker-refactor cadence from memory
./fincept-qt/docs/datahub-phases/phase-07-broker-account-streams.md:222:- Broker-specific screens beyond the generic equity/portfolio flow
./fincept-qt/docs/datahub-phases/phase-05-news.md:187:- MCP news tool modules — Phase 9.
./fincept-qt/docs/datahub-phases/phase-04-websocket-producers.md:14:producers. Today Kraken and HyperLiquid feeds go through
./fincept-qt/docs/datahub-phases/phase-04-websocket-producers.md:32:| `ExchangeService`          | `src/trading/ExchangeService.{h,cpp}`                   | Long-running WS subprocess for Kraken + HyperLiquid |
./fincept-qt/docs/datahub-phases/phase-04-websocket-producers.md:71:- On WS message: parse → publish. Example for Kraken ticker:
./fincept-qt/docs/datahub-phases/phase-04-websocket-producers.md:96:- MCP `CryptoTradingTools` module (`src/mcp/tools/`) — use
./fincept-qt/docs/datahub-phases/phase-04-websocket-producers.md:97:  `hub.peek()` when an LLM tool asks for "latest price". Lazy: no
./fincept-qt/docs/datahub-phases/phase-04-websocket-producers.md:111:  Kraken's 100+/sec ticker feed overwhelming a UI thread that can
./fincept-qt/docs/datahub-phases/phase-04-websocket-producers.md:122:  Python WS subprocess: **exactly one** connection to Kraken exists.
./fincept-qt/docs/datahub-phases/phase-04-websocket-producers.md:132:  observed on Kraken during volatile hours).
./fincept-qt/docs/datahub-phases/phase-04-websocket-producers.md:148:- **Backpressure on Kraken feed.** Without `coalesce_within_ms`, 100 Hz
./fincept-qt/docs/datahub-phases/phase-04-websocket-producers.md:178:  hub signal — additive, low-risk, kept regardless.
./fincept-qt/docs/datahub-phases/phase-02-market-data-pilot.md:56:This base class backs **four dashboard widgets** via factory functions
./fincept-qt/docs/datahub-phases/phase-02-market-data-pilot.md:137:- No user-facing regression risk if rollback is done within the same
./fincept-qt/docs/datahub-phases/phase-10-enforcement-cleanup.md:119:agent:<id>:stream:<run>                 AgentService          —        —       yes  coalesce 100 ms
./fincept-qt/docs/datahub-phases/phase-10-enforcement-cleanup.md:180:  the biggest risk. Mitigation:
./fincept-qt/docs/datahub-phases/phase-10-enforcement-cleanup.md:196:- **Agent / MCP regressions.** Phase 9 deletions may affect
./fincept-qt/docs/datahub-phases/phase-10-enforcement-cleanup.md:197:  third-party MCP consumers that call deprecated service APIs
./fincept-qt/docs/datahub-phases/phase-10-enforcement-cleanup.md:198:  directly. Mitigation: MCP tool surface doesn't expose service
./fincept-qt/docs/datahub-phases/phase-10-enforcement-cleanup.md:199:  APIs; external MCP clients call tool names, implementation is
./fincept-qt/docs/datahub-phases/phase-10-enforcement-cleanup.md:200:  internal. Low risk.
./fincept-qt/docs/datahub-phases/phase-10-enforcement-cleanup.md:214:If rollback is triggered by a subtle regression (e.g. an agent
./fincept-qt/docs/backtesting-provider-process.md:63:- Run one backtest end-to-end
./fincept-qt/docs/CRYPTO_CENTER_PHASE_2.md:5:- See **every token** your wallet holds (SOL + every SPL token), with USD prices and portfolio total.
./fincept-qt/docs/CRYPTO_CENTER_PHASE_2.md:25:The HOLDINGS BAR sits above every tab — your portfolio total never disappears even when you switch tabs. Stake / Markets / Roadmap are placeholders for Phases 3 / 4 / 5 respectively.
./fincept-qt/docs/CRYPTO_CENTER_PHASE_2.md:104:Every paid feature in Fincept Terminal — AI reports, deep backtests, premium screens — accepts $FNCPT at a **30% discount** when you hold **≥ 1,000 $FNCPT**.
./fincept-qt/docs/agents/datahub-guide.md:1:# DataHub guide for agents / LLM tool callers
./fincept-qt/docs/agents/datahub-guide.md:3:Phase 9 of the DataHub migration exposes the terminal's in-process pub/sub layer directly to LLM tool callers through four generic MCP tools. Everything streaming into any active widget — quotes, order books, news, vessel tracks, broker ticks, geopolitical events, agent outputs, LLM token streams — is observable from an agent via hub topic names.
./fincept-qt/docs/agents/datahub-guide.md:5:This guide explains what an agent can do and when to use which tool. The full topic catalogue lives in [`docs/DATAHUB_TOPICS.md`](../DATAHUB_TOPICS.md).
./fincept-qt/docs/agents/datahub-guide.md:33:`force: true` bypasses the topic's `min_interval_ms` rate gate. Per-producer `max_requests_per_sec` is still enforced — an agent can't hammer a rate-limited broker REST API by rage-calling this tool.
./fincept-qt/docs/agents/datahub-guide.md:68:- `agent:output:<run_id>`, `agent:stream:<run_id>`, `agent:status:<run_id>`
./fincept-qt/docs/agents/datahub-guide.md:75:**Cache trustworthiness.** Peeked values are the most recent publish. Check `age_ms`. Pull-through topics auto-refresh on access when stale; push-only topics (most `agent:*`, most `ma:*`, broker WebSocket tick channels) only update when their producer pushes.
./fincept-qt/docs/agents/datahub-guide.md:77:**Disposable topics.** Some topics (especially `agent:output:<run_id>` and `llm:session:<id>:stream`) are created per-run and retired on completion. Their cached state disappears after retire_topic; subsequent peeks return unknown. This is intentional — the terminal would otherwise grow unbounded memory over a long session with many agent runs.
./fincept-qt/docs/agents/datahub-guide.md:81:**Thread safety.** All tools are safe to call from the MCP handler thread. `datahub_subscribe_briefly` spins a local event loop bounded by `duration_ms`, so it never blocks the UI thread.
./fincept-qt/docs/agents/datahub-guide.md:100:### "Tail a running agent's output."
./fincept-qt/docs/agents/datahub-guide.md:102:If the user kicked off an agent run and returned a `request_id`:
./fincept-qt/docs/agents/datahub-guide.md:106:  "topic": "agent:stream:<run_id>",
./fincept-qt/docs/agents/datahub-guide.md:111:You'll receive every token published in that window. For the final result, peek `agent:output:<run_id>` *before* the run completes — after completion the topic is retired.
./fincept-qt/docs/agents/datahub-guide.md:123:## Relation to existing MCP tools
./fincept-qt/docs/agents/datahub-guide.md:125:The terminal exposes ~24 domain-specific MCP tool modules (markets, news, portfolio, forum, notes, etc.). Those still exist and are the right tool for write operations (`save_config`, `add_news_monitor`, `execute_trade`), for one-shot lookups that don't flow through the hub, and for actions that need to drive UI navigation.
./fincept-qt/docs/agents/datahub-guide.md:132:- Tailing agent runs and LLM streams.
./fincept-qt/docs/agents/datahub-guide.md:134:Use domain MCP tools for:
./fincept-qt/docs/polymarket_api_links.txt:64:- Negative Risk Markets: https://docs.polymarket.com/advanced/neg-risk.md
./fincept-qt/docs/CRYPTO_CENTER_PHASE_3.md:6:2. A **billing tier** (Bronze / Silver / Gold) that unlocks paid screens elsewhere in the terminal — AI Quant Lab, Alpha Arena, premium agents.
./fincept-qt/docs/CRYPTO_CENTER_PHASE_3.md:32:│  GOLD     10k+ veFNCPT       all agents + arena                     │
./fincept-qt/docs/CRYPTO_CENTER_PHASE_3.md:80:- **Gold** (10k+ veFNCPT) reveals Alpha Arena + every agent.
./fincept-qt/docs/CRYPTO_CENTER_PHASE_4.md:36:Until both are present, the MARKETS tab serves the curated three-market dataset baked into `FinceptInternalAdapter` so you can see what the screen will look like and verify the data shapes integrate cleanly with the unified `PredictionExchangeAdapter` (which also serves Polymarket and Kalshi).
./fincept-qt/docs/CRYPTO_CENTER_PHASE_4.md:42:The Fincept internal adapter is registered with `PredictionExchangeRegistry` alongside `PolymarketAdapter` and `KalshiAdapter`. Any code that already iterates the registry (Polymarket / Kalshi screen, command bar, MCP tools) can switch to `fincept` without special-casing.
./fincept-qt/docs/DATAHUB_TOPICS.md:17:Producer changed to `ExchangeSessionManager` with the multi-broker refactor
./fincept-qt/docs/DATAHUB_TOPICS.md:28:| `ws:hyperliquid:*` | `ExchangeSessionManager` | push-only | Same sub-families as Kraken |
./fincept-qt/docs/DATAHUB_TOPICS.md:29:| `prediction:polymarket:price:<asset_id>` | `PolymarketWebSocket` | push-only | Was `polymarket:price:*` before the prediction-markets refactor |
./fincept-qt/docs/DATAHUB_TOPICS.md:30:| `prediction:polymarket:orderbook:<asset_id>` | `PolymarketWebSocket` | push-only | Was `polymarket:orderbook:*` before the prediction-markets refactor |
./fincept-qt/docs/DATAHUB_TOPICS.md:70:plan's risk-mitigation cadence).
./fincept-qt/docs/DATAHUB_TOPICS.md:85:| `geopolitics:relationship_graph:<ticker>` | `RelationshipMapService` | 10 min | 2 min | yfinance-backed corporate relationship snapshot |
./fincept-qt/docs/DATAHUB_TOPICS.md:103:## AI / Agents / LLM (Phase 9)
./fincept-qt/docs/DATAHUB_TOPICS.md:111:| `agent:output:<run_id>` | `AgentService` | 10 min (push-only) | — | Final result payload for a run. Retired on completion. Shape: `{request_id, success, response, error, execution_time_ms, final}`. |
./fincept-qt/docs/DATAHUB_TOPICS.md:112:| `agent:stream:<run_id>` | `AgentService` | 5 min (push-only, coalesce 50 ms) | — | Token firehose from streaming runs. Shape: `{request_id, token}`. |
./fincept-qt/docs/DATAHUB_TOPICS.md:113:| `agent:status:<run_id>` | `AgentService` | 5 min (push-only, coalesce 100 ms) | — | Thinking/tool-call narration. Shape: `{request_id, status}`. |
./fincept-qt/docs/DATAHUB_TOPICS.md:114:| `agent:routing:<run_id>` | `AgentService` | 10 min (push-only) | — | One-shot routing decision. Shape: `{request_id, success, agent_id, intent, confidence}`. |
./fincept-qt/docs/DATAHUB_TOPICS.md:115:| `agent:error:<context>` | `AgentService` | 2 min (push-only) | — | Error stream keyed by context (discover_agents, create_plan, etc.). Shape: `{context, message}`. |
./fincept-qt/docs/DATAHUB_TOPICS.md:117:### LLM session stream
./fincept-qt/docs/DATAHUB_TOPICS.md:123:### Generic DataHub MCP tools
./fincept-qt/docs/DATAHUB_TOPICS.md:125:The MCP module `DataHubTools` exposes four generic introspection tools to any LLM tool caller (see `docs/agents/datahub-guide.md`):
./fincept-qt/docs/DATAHUB_TOPICS.md:159:| `billing:fncpt_discount:<pubkey>` | `FeeDiscountService` | derived from `wallet:balance:<pubkey>` (no separate fetch) | — | The service subscribes to the user's balance topic internally and republishes eligibility. Shape: `FncptDiscount{eligible, threshold_raw, threshold_decimals, applied_skus}`. Threshold + applied SKUs come from `services/billing/FeeDiscountConfig.h`; defaults to **1,000 $FNCPT → 30 % off** for AI reports, deep backtests, premium screens. |
./fincept-qt/docs/DATAHUB_TOPICS.md:191:Reserved topic family for the `FinceptInternalAdapter` matching engine. Topics are policy-registered at adapter startup, but **no producer publishes to them yet**: the adapter ships in **demo mode** (curated 3-market dataset emitted via Qt signals only) until `fincept.markets_endpoint` is configured *and* the `fincept_market` Anchor program (`solana/programs/fincept_market/`, separate repo) is deployed.
./fincept-qt/docs/ANGELONE_QT_CROSSCHECK.md:104:- Core auth + order + portfolio + quotes/history: **Completed**
./fincept-qt/DATAHUB_PHASES.md:24:| 9 | AI / MCP / Agents integration              | Subscribers, not producers            | Medium     | 3, 4, 5    |
./fincept-qt/DATAHUB_PHASES.md:105:  `CommoditiesWidget` factory functions, so migrating it in one place
./fincept-qt/DATAHUB_PHASES.md:135:Forex / Commodities factories). Remaining market-data consumers confirmed
./fincept-qt/DATAHUB_PHASES.md:152:`PortfolioBlotter` (`src/screens/portfolio/PortfolioBlotter.cpp`),
./fincept-qt/DATAHUB_PHASES.md:175:- Large diff surface — split into sub-PRs by screen group (dashboard widgets, markets, watchlist, portfolio, report builder).
./fincept-qt/DATAHUB_PHASES.md:185:- `trading/ExchangeService` — Kraken + HyperLiquid WebSocket feeds → `ws:kraken:*`, `ws:hyperliquid:*`.
./fincept-qt/DATAHUB_PHASES.md:195:- CryptoTradingScreen, CryptoWidget, MCP `CryptoTradingTools`, agents — all subscribe via hub.
./fincept-qt/DATAHUB_PHASES.md:197:- Kraken/HyperLiquid WS opens only when ≥1 subscriber exists.
./fincept-qt/DATAHUB_PHASES.md:205:- Backpressure on high-frequency feeds (Kraken can emit 100+/sec) — hub dispatcher must coalesce or drop stale updates. Add a `coalesce_within_ms` field to TopicPolicy if needed.
./fincept-qt/DATAHUB_PHASES.md:246:- Economics tab + per-source panels (already refactored, per memory) → subscribers only.
./fincept-qt/DATAHUB_PHASES.md:272:- `AccountDataStream` (per memory: multi-account architecture) refactored to publish to hub per-account.
./fincept-qt/DATAHUB_PHASES.md:273:- Equity trading screen, portfolio, multi-account selector → subscribers.
./fincept-qt/DATAHUB_PHASES.md:296:- Low — these are long-TTL, relatively cold data sources. Pattern is well-established by Phases 5–6.
./fincept-qt/DATAHUB_PHASES.md:300:## Phase 9 — AI / MCP / Agents Integration
./fincept-qt/DATAHUB_PHASES.md:302:**Goal:** the AI and agent surface can read hub topics the same way screens do.
./fincept-qt/DATAHUB_PHASES.md:305:- MCP tool modules in `src/mcp/tools/` (24 modules) — replace direct service calls with `DataHub::peek()` / `subscribe()` where appropriate.
./fincept-qt/DATAHUB_PHASES.md:306:- `AgentService` — agents can subscribe to market/news/broker topics to get context without bespoke service plumbing.
./fincept-qt/DATAHUB_PHASES.md:310:- MCP `datahub_peek`, `datahub_subscribe`, `datahub_list_topics` tool module (new).
./fincept-qt/DATAHUB_PHASES.md:315:- Agents running in background threads must use `peek()` or subscribe with queued connection — document in agent contributor guide.
./fincept-qt/DATAHUB_PHASES.md:328:- **docs/DATAHUB_TOPICS.md** — ✅ full topic registry for Phases 2–9 (markets, ws, news, econ, dbnomics, govdata, broker, geopolitics, maritime, M&A, agents, LLM sessions).
./fincept-qt/scripts/akshare_energy.py:13:    import akshare as ak
./fincept-qt/scripts/coinpaprika_data.py:101:    """Get price tickers for top coins with market data."""
./fincept-qt/scripts/nber_data.py:101:    "m08023": "Index of factory employment",
./fincept-qt/scripts/nber_data.py:273:    fred_key = os.environ.get("FRED_API_KEY", "")
./fincept-qt/scripts/nber_data.py:290:                "source": "BLS via FRED",
./fincept-qt/scripts/nber_data.py:305:        "note": "Set FRED_API_KEY for live data. Available via FRED API.",
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:5:strategy library. Supports multi-symbol backtesting with proper portfolio tracking.
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:8:    python python_backtest_engine.py \
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:14:        --data-provider yfinance \
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:35:    DEBUG_LOG.append(f"[py:python_backtest] {msg}")
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:146:                          provider: str = 'yfinance') -> Dict[str, pd.DataFrame]:
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:151:    if provider == 'yfinance':
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:153:            import yfinance as yf
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:154:            debug(f"yfinance version: {yf.__version__}")
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:172:            raise ImportError("yfinance not installed. Install with: pip install yfinance")
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:209:    """Represents a single time slice of market data."""
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:299:def run_backtest(
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:307:    """Execute the backtest."""
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:308:    debug(f"Starting backtest with {len(historical_data)} symbols")
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:355:    # This ensures the backtest uses the user-specified capital
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:357:    debug(f"Cash after re-apply: {algo.portfolio.cash}")
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:429:        # Update portfolio holdings' market prices so equity tracks correctly
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:432:            algo.portfolio.update_market_prices(price_updates)
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:451:        positions_before = {sym: algo.portfolio[sym].quantity for sym in historical_data.keys()}
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:463:            pos_after = algo.portfolio[symbol].quantity
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:511:        # Update portfolio market prices again after on_data (fills may have changed holdings)
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:513:            algo.portfolio.update_market_prices(price_updates)
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:516:        equity = algo.portfolio.total_portfolio_value
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:561:    """Calculate backtest performance metrics."""
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:573:            'profit_factor': 0,
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:609:            'profit_factor': 0,
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:620:    profit_factor = (gross_profit / gross_loss) if gross_loss > 0 else (999.99 if gross_profit > 0 else 0)
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:625:    # Sharpe ratio (simplified daily calculation)
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:653:        'profit_factor': round(min(profit_factor, 999.99), 2),
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:670:    parser.add_argument('--data-provider', default='yfinance', help='Data provider: yfinance')
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:741:    # Run backtest
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:743:        result = run_backtest(
./fincept-qt/scripts/algo_trading/backtest_engine.py:2:Backtest Engine — Walk-forward strategy backtester
./fincept-qt/scripts/algo_trading/backtest_engine.py:4:Fetches historical data via yfinance or from local candle_cache (Fyers),
./fincept-qt/scripts/algo_trading/backtest_engine.py:9:    python backtest_engine.py \
./fincept-qt/scripts/algo_trading/backtest_engine.py:38:    DEBUG_LOG.append(f"[py:backtest] {msg}")
./fincept-qt/scripts/algo_trading/backtest_engine.py:76:def fetch_from_yfinance(symbol: str, period: str, interval: str):
./fincept-qt/scripts/algo_trading/backtest_engine.py:77:    """Fetch OHLCV data via yfinance."""
./fincept-qt/scripts/algo_trading/backtest_engine.py:78:    debug(f"fetch_from_yfinance: symbol={symbol}, period={period}, interval={interval}")
./fincept-qt/scripts/algo_trading/backtest_engine.py:80:        import yfinance as yf
./fincept-qt/scripts/algo_trading/backtest_engine.py:81:        debug(f"yfinance version: {yf.__version__}")
./fincept-qt/scripts/algo_trading/backtest_engine.py:88:            return None, "No data returned from yfinance"
./fincept-qt/scripts/algo_trading/backtest_engine.py:101:        debug(f"yfinance ImportError: {e}")
./fincept-qt/scripts/algo_trading/backtest_engine.py:102:        return None, "yfinance not installed. Install with: pip install yfinance"
./fincept-qt/scripts/algo_trading/backtest_engine.py:104:        debug(f"yfinance Exception: {e}\n{traceback.format_exc()}")
./fincept-qt/scripts/algo_trading/backtest_engine.py:105:        return None, f"yfinance error: {e}"
./fincept-qt/scripts/algo_trading/backtest_engine.py:167:def fetch_historical_data(symbol: str, period: str, interval: str, provider: str = 'yfinance', db_path: str = None):
./fincept-qt/scripts/algo_trading/backtest_engine.py:192:        # Default to yfinance
./fincept-qt/scripts/algo_trading/backtest_engine.py:193:        debug("Using yfinance provider")
./fincept-qt/scripts/algo_trading/backtest_engine.py:194:        return fetch_from_yfinance(symbol, period, interval)
./fincept-qt/scripts/algo_trading/backtest_engine.py:197:def run_backtest(
./fincept-qt/scripts/algo_trading/backtest_engine.py:242:            # Check risk management first
./fincept-qt/scripts/algo_trading/backtest_engine.py:348:                'profit_factor': 0,
./fincept-qt/scripts/algo_trading/backtest_engine.py:365:    profit_factor = (gross_profit / gross_loss) if gross_loss > 0 else float('inf') if gross_profit > 0 else 0
./fincept-qt/scripts/algo_trading/backtest_engine.py:367:    # Annualization factor based on timeframe (bars per year)
./fincept-qt/scripts/algo_trading/backtest_engine.py:373:    ann_factor = BARS_PER_YEAR.get(timeframe, 252)
./fincept-qt/scripts/algo_trading/backtest_engine.py:375:    # Sharpe ratio (annualized using timeframe-aware factor)
./fincept-qt/scripts/algo_trading/backtest_engine.py:384:            sharpe = (mean_ret / std_ret) * (ann_factor ** 0.5) if std_ret > 0 else 0
./fincept-qt/scripts/algo_trading/backtest_engine.py:390:    # Cap profit_factor for JSON serialization
./fincept-qt/scripts/algo_trading/backtest_engine.py:391:    if math.isinf(profit_factor):
./fincept-qt/scripts/algo_trading/backtest_engine.py:392:        profit_factor = 999.99
./fincept-qt/scripts/algo_trading/backtest_engine.py:417:            'profit_factor': round(profit_factor, 2),
./fincept-qt/scripts/algo_trading/backtest_engine.py:437:    conn.row_factory = sqlite3.Row
./fincept-qt/scripts/algo_trading/backtest_engine.py:586:def cmd_run_backtest(params: dict, db_path: str):
./fincept-qt/scripts/algo_trading/backtest_engine.py:587:    """Run walk-forward backtest for a strategy loaded from DB."""
./fincept-qt/scripts/algo_trading/backtest_engine.py:588:    debug("cmd_run_backtest started")
./fincept-qt/scripts/algo_trading/backtest_engine.py:623:    # Determine period string from date range for yfinance
./fincept-qt/scripts/algo_trading/backtest_engine.py:644:        df, error = fetch_historical_data(symbol, period, timeframe, provider='yfinance', db_path=db_path)
./fincept-qt/scripts/algo_trading/backtest_engine.py:654:            'hint': 'Use .NS suffix for NSE stocks (e.g. RELIANCE.NS) for yfinance.',
./fincept-qt/scripts/algo_trading/backtest_engine.py:668:        result = run_backtest(
./fincept-qt/scripts/algo_trading/backtest_engine.py:678:        debug(f"Exception in run_backtest: {e}\n{traceback.format_exc()}")
./fincept-qt/scripts/algo_trading/backtest_engine.py:694:        'profit_factor': metrics.get('profit_factor', 0),
./fincept-qt/scripts/algo_trading/backtest_engine.py:705:    parser.add_argument('command', choices=['save_strategy', 'list_strategies', 'list_registry', 'delete_strategy', 'run_backtest'],
./fincept-qt/scripts/algo_trading/backtest_engine.py:742:    elif args.command == 'run_backtest':
./fincept-qt/scripts/algo_trading/backtest_engine.py:748:        cmd_run_backtest(params, db_path)
./fincept-qt/scripts/algo_trading/algo_manager.py:37:    conn.row_factory = sqlite3.Row
./fincept-qt/scripts/algo_trading/algo_live_runner.py:201:def check_risk_management(current_price: float, position: dict, strategy: dict) -> str:
./fincept-qt/scripts/algo_trading/algo_live_runner.py:338:            # Check risk management first
./fincept-qt/scripts/algo_trading/algo_live_runner.py:348:                risk_exit = check_risk_management(current_price, position, strategy)
./fincept-qt/scripts/algo_trading/algo_live_runner.py:349:                if risk_exit:
./fincept-qt/scripts/algo_trading/algo_live_runner.py:350:                    log.info(f"  RISK EXIT TRIGGERED: {risk_exit}")
./fincept-qt/scripts/algo_trading/algo_live_runner.py:358:                                     abs(position['qty']), current_price, pnl, risk_exit)
./fincept-qt/scripts/hdx_data.py:39:    # Create request with user agent
./fincept-qt/scripts/akshare_index.py:13:    import akshare as ak
./fincept-qt/scripts/alpha_arena/types/responses.py:5:Provides event-driven communication between agents and frontend.
./fincept-qt/scripts/alpha_arena/types/responses.py:20:    AGENT = "agent"
./fincept-qt/scripts/alpha_arena/types/responses.py:47:    PORTFOLIO_UPDATE = "portfolio_update"
./fincept-qt/scripts/alpha_arena/types/responses.py:51:    """Events specific to streaming agent responses."""
./fincept-qt/scripts/alpha_arena/types/responses.py:64:    """Events specific to notification agent responses."""
./fincept-qt/scripts/alpha_arena/types/responses.py:72:    """Response model for streaming agent responses.
./fincept-qt/scripts/alpha_arena/types/responses.py:74:    Used by agents that stream progress, decisions, reasoning, or
./fincept-qt/scripts/alpha_arena/types/responses.py:97:    """Response model for notification agent responses."""
./fincept-qt/scripts/alpha_arena/types/responses.py:161:    item_id: str = Field(default_factory=generate_item_id)
./fincept-qt/scripts/alpha_arena/types/responses.py:162:    timestamp: datetime = Field(default_factory=datetime.now)
./fincept-qt/scripts/alpha_arena/types/responses.py:195:    timestamp: datetime = Field(default_factory=datetime.now)
./fincept-qt/scripts/alpha_arena/types/responses.py:201:# Response factory functions
./fincept-qt/scripts/alpha_arena/types/responses.py:280:    """Create a market data response."""
./fincept-qt/scripts/alpha_arena/types/responses.py:323:def portfolio_update(
./fincept-qt/scripts/alpha_arena/types/responses.py:325:    portfolio_value: float,
./fincept-qt/scripts/alpha_arena/types/responses.py:332:    """Create a real-time portfolio update response after trade execution."""
./fincept-qt/scripts/alpha_arena/types/responses.py:334:        content=f"{model_name}: Portfolio ${portfolio_value:,.2f} (P&L: ${total_pnl:+,.2f})",
```

## 10. 入口文件 / Main / CLI / App 启动扫描

```text
./.github/scripts/update_readme_table.py:28:def main() -> int:
./.github/scripts/update_readme_table.py:71:if __name__ == "__main__":
./.github/scripts/update_readme_table.py:72:    sys.exit(main())
./.github/scripts/generate_updates_manifest.py:23:def main() -> int:
./.github/scripts/generate_updates_manifest.py:81:if __name__ == "__main__":
./.github/scripts/generate_updates_manifest.py:82:    sys.exit(main())
./fincept-qt/tests/datahub/test_datahub.cpp:9:#include <QCoreApplication>
./fincept-qt/tests/datahub/test_datahub.cpp:61:        QCoreApplication::processEvents();
./fincept-qt/tests/datahub/test_datahub.cpp:62:        QCoreApplication::sendPostedEvents();
./fincept-qt/tests/datahub/test_datahub.cpp:63:        QCoreApplication::processEvents();
./fincept-qt/tests/datahub/test_datahub.cpp:110:        QCoreApplication::sendPostedEvents();
./fincept-qt/tests/datahub/test_datahub.cpp:111:        QCoreApplication::processEvents();
./fincept-qt/tests/datahub/test_datahub.cpp:112:        QCoreApplication::processEvents();
./fincept-qt/tests/datahub/test_datahub.cpp:115:        QCoreApplication::processEvents();
./fincept-qt/tests/datahub/test_datahub.cpp:141:        QCoreApplication::processEvents();
./fincept-qt/tests/datahub/test_datahub.cpp:196:        QCoreApplication::processEvents();
./fincept-qt/tests/datahub/test_datahub.cpp:229:        QCoreApplication::processEvents();
./fincept-qt/tests/datahub/test_datahub.cpp:258:        QCoreApplication::processEvents();
./fincept-qt/tests/datahub/test_datahub.cpp:278:        QCoreApplication::processEvents();
./fincept-qt/tests/mcp/test_async.cpp:11:#include <QCoreApplication>
./fincept-qt/tests/mcp/test_dispatcher.cpp:17:#include <QCoreApplication>
./fincept-qt/tests/mcp/test_dispatcher.cpp:112:        auto out = dispatcher.run("hi", {}, adapter, send, {}, {});
./fincept-qt/tests/mcp/test_dispatcher.cpp:152:        auto out = dispatcher.run("hi", {}, adapter, send, {}, {});
./fincept-qt/tests/mcp/test_dispatcher.cpp:191:        auto out = dispatcher.run("hi", {}, adapter, send, {}, {});
./fincept-qt/tests/mcp/test_dispatcher.cpp:223:        auto out = dispatcher.run("hi", {}, adapter, send, {}, cancel_flag);
./fincept-qt/tests/mcp/test_dispatcher.cpp:255:        auto out = dispatcher.run("hi", {}, adapter, send, {}, {});
./fincept-qt/scripts/ons_data.py:84:def main(args=None):
./fincept-qt/scripts/ons_data.py:122:if __name__ == "__main__":
./fincept-qt/scripts/ons_data.py:123:    main()
./fincept-qt/scripts/grain_futures_data.py:69:def main(args=None):
./fincept-qt/scripts/grain_futures_data.py:99:if __name__ == "__main__":
./fincept-qt/scripts/grain_futures_data.py:100:    main()
./fincept-qt/scripts/akshare_energy.py:133:def main():
./fincept-qt/scripts/akshare_energy.py:160:if __name__ == "__main__":
./fincept-qt/scripts/akshare_energy.py:161:    main()
./fincept-qt/scripts/scb_data.py:639:def main():
./fincept-qt/scripts/scb_data.py:724:if __name__ == "__main__":
./fincept-qt/scripts/scb_data.py:725:    main()
./fincept-qt/scripts/coinpaprika_data.py:117:def main(args=None):
./fincept-qt/scripts/coinpaprika_data.py:177:if __name__ == "__main__":
./fincept-qt/scripts/coinpaprika_data.py:178:    main()
./fincept-qt/scripts/ebrd_data.py:78:def main(args=None):
./fincept-qt/scripts/ebrd_data.py:113:if __name__ == "__main__":
./fincept-qt/scripts/ebrd_data.py:114:    main()
./fincept-qt/scripts/adb_data.py:594:def main(args=None):
./fincept-qt/scripts/adb_data.py:728:if __name__ == "__main__":
./fincept-qt/scripts/adb_data.py:729:    main()
./fincept-qt/scripts/nber_data.py:310:def main(args=None):
./fincept-qt/scripts/nber_data.py:345:if __name__ == "__main__":
./fincept-qt/scripts/nber_data.py:346:    main()
./fincept-qt/scripts/un_sdg_data.py:137:def main(args=None):
./fincept-qt/scripts/un_sdg_data.py:186:if __name__ == "__main__":
./fincept-qt/scripts/un_sdg_data.py:187:    main()
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:23:import argparse
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:83:    # Must be a QCAlgorithm subclass (not just any class with initialize)
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:90:    # Fallback: check for both initialize and on_data (strategy signature)
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:91:    if hasattr(obj, 'initialize') and hasattr(obj, 'on_data'):
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:341:    debug("Calling initialize()...")
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:343:        algo.initialize()
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:345:        debug(f"initialize() error: {e}\n{traceback.format_exc()}")
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:354:    # Re-apply initial cash AFTER initialize() since strategies often override set_cash
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:659:def main():
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:660:    debug("main() started")
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:663:    parser = argparse.ArgumentParser(description='Python Strategy Backtest Engine')
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:764:if __name__ == '__main__':
./fincept-qt/scripts/algo_trading/python_backtest_engine.py:765:    main()
./fincept-qt/scripts/algo_trading/backtest_engine.py:27:import argparse
./fincept-qt/scripts/algo_trading/backtest_engine.py:700:def main():
./fincept-qt/scripts/algo_trading/backtest_engine.py:701:    debug("main() started")
./fincept-qt/scripts/algo_trading/backtest_engine.py:704:    parser = argparse.ArgumentParser(description='Backtest Engine')
./fincept-qt/scripts/algo_trading/backtest_engine.py:751:if __name__ == '__main__':
./fincept-qt/scripts/algo_trading/backtest_engine.py:752:    main()
./fincept-qt/scripts/algo_trading/scanner_engine.py:22:import argparse
./fincept-qt/scripts/algo_trading/scanner_engine.py:41:def main():
./fincept-qt/scripts/algo_trading/scanner_engine.py:42:    parser = argparse.ArgumentParser(description='Algo Scanner Engine')
./fincept-qt/scripts/algo_trading/scanner_engine.py:125:if __name__ == '__main__':
./fincept-qt/scripts/algo_trading/scanner_engine.py:126:    main()
./fincept-qt/scripts/algo_trading/condition_evaluator.py:28:import argparse
./fincept-qt/scripts/algo_trading/condition_evaluator.py:390:def main():
./fincept-qt/scripts/algo_trading/condition_evaluator.py:391:    parser = argparse.ArgumentParser(description='Condition Evaluator')
./fincept-qt/scripts/algo_trading/condition_evaluator.py:427:if __name__ == '__main__':
./fincept-qt/scripts/algo_trading/condition_evaluator.py:428:    main()
./fincept-qt/scripts/algo_trading/algo_manager.py:17:import argparse
./fincept-qt/scripts/algo_trading/algo_manager.py:111:def main():
./fincept-qt/scripts/algo_trading/algo_manager.py:112:    parser = argparse.ArgumentParser(description='Algo Deployment Manager')
./fincept-qt/scripts/algo_trading/algo_manager.py:132:if __name__ == '__main__':
./fincept-qt/scripts/algo_trading/algo_manager.py:133:    main()
./fincept-qt/scripts/algo_trading/algo_live_runner.py:14:import argparse
./fincept-qt/scripts/algo_trading/algo_live_runner.py:233:def main():
./fincept-qt/scripts/algo_trading/algo_live_runner.py:234:    parser = argparse.ArgumentParser(description='Algo Live Runner')
./fincept-qt/scripts/algo_trading/algo_live_runner.py:479:if __name__ == '__main__':
./fincept-qt/scripts/algo_trading/algo_live_runner.py:480:    main()
./fincept-qt/scripts/afdb_data.py:85:def main(args=None):
./fincept-qt/scripts/afdb_data.py:119:if __name__ == "__main__":
./fincept-qt/scripts/afdb_data.py:120:    main()
./fincept-qt/scripts/glassnode_data.py:75:def main(args=None):
./fincept-qt/scripts/glassnode_data.py:118:if __name__ == "__main__":
./fincept-qt/scripts/glassnode_data.py:119:    main()
./fincept-qt/scripts/hdx_data.py:193:def main(args: Optional[List[str]] = None) -> str:
./fincept-qt/scripts/hdx_data.py:545:if __name__ == "__main__":
./fincept-qt/scripts/hdx_data.py:546:    main()
./fincept-qt/scripts/opec_data.py:63:def main(args=None):
./fincept-qt/scripts/opec_data.py:96:if __name__ == "__main__":
./fincept-qt/scripts/opec_data.py:97:    main()
./fincept-qt/scripts/akshare_index.py:570:def main():
./fincept-qt/scripts/akshare_index.py:597:if __name__ == "__main__":
./fincept-qt/scripts/akshare_index.py:598:    main()
./fincept-qt/scripts/govtrack_data.py:65:def main(args=None):
./fincept-qt/scripts/govtrack_data.py:97:if __name__ == "__main__":
./fincept-qt/scripts/govtrack_data.py:98:    main()
./fincept-qt/scripts/coinglass_data.py:61:def main(args=None):
./fincept-qt/scripts/coinglass_data.py:94:if __name__ == "__main__":
./fincept-qt/scripts/coinglass_data.py:95:    main()
./fincept-qt/scripts/global_innovation_data.py:72:def main(args=None):
./fincept-qt/scripts/global_innovation_data.py:106:if __name__ == "__main__":
./fincept-qt/scripts/global_innovation_data.py:107:    main()
./fincept-qt/scripts/alpha_arena/core/competition.py:103:    async def initialize(self, api_keys: Dict[str, str]) -> bool:
./fincept-qt/scripts/alpha_arena/core/competition.py:113:        # Check if already initialized
./fincept-qt/scripts/alpha_arena/core/competition.py:115:            logger.info(f"Competition {self.competition_id} already initialized with {len(self._agents)} agents")
./fincept-qt/scripts/alpha_arena/core/competition.py:130:                    logger.info("Polymarket data provider initialized")
./fincept-qt/scripts/alpha_arena/core/competition.py:142:                    logger.info(f"Market data provider initialized for {self.config.exchange_id}")
./fincept-qt/scripts/alpha_arena/core/competition.py:225:                        agent.initialize(),
./fincept-qt/scripts/alpha_arena/core/competition.py:229:                        logger.info(f"Agent {model.name} initialized successfully with real LLM")
./fincept-qt/scripts/alpha_arena/core/competition.py:233:                        logger.error(f"Agent {model.name} failed to initialize: {init_error}")
./fincept-qt/scripts/alpha_arena/core/competition.py:252:            # Validate enough agents initialized with real LLMs
./fincept-qt/scripts/alpha_arena/core/competition.py:256:                    f"Only {len(self._agents)} agent(s) initialized successfully out of {len(self.config.models)}. "
./fincept-qt/scripts/alpha_arena/core/competition.py:263:            logger.info(f"Competition {self.competition_id} initialized with {len(self._agents)} agents")
./fincept-qt/scripts/alpha_arena/core/competition.py:267:            logger.exception(f"Failed to initialize competition: {e}")
./fincept-qt/scripts/alpha_arena/core/competition.py:318:            # Ensure market provider is initialized
./fincept-qt/scripts/alpha_arena/core/competition.py:320:                yield error("Market data provider not initialized. Cannot run cycle without live market data.")
./fincept-qt/scripts/alpha_arena/core/competition.py:518:        if not await self.initialize(api_keys):
./fincept-qt/scripts/alpha_arena/core/competition.py:614:        # Ensure Polymarket provider is initialized
./fincept-qt/scripts/alpha_arena/core/competition.py:616:            yield error("Polymarket data provider not initialized")
./fincept-qt/scripts/alpha_arena/core/base_agent.py:68:        self._initialized = False
./fincept-qt/scripts/alpha_arena/core/base_agent.py:113:    async def initialize(self) -> bool:
./fincept-qt/scripts/alpha_arena/core/base_agent.py:115:        self._initialized = True
./fincept-qt/scripts/alpha_arena/core/base_agent.py:116:        logger.info(f"Agent '{self.name}' initialized")
./fincept-qt/scripts/alpha_arena/core/base_agent.py:121:        self._initialized = False
./fincept-qt/scripts/alpha_arena/core/base_agent.py:125:    def is_initialized(self) -> bool:
./fincept-qt/scripts/alpha_arena/core/base_agent.py:126:        return self._initialized
./fincept-qt/scripts/alpha_arena/core/base_agent.py:180:    def initialize_metrics(self, initial_capital: float = 10000.0):
./fincept-qt/scripts/alpha_arena/core/base_agent.py:184:            logger.info(f"Portfolio metrics initialized for {self.name}")
./fincept-qt/scripts/alpha_arena/core/base_agent.py:430:    async def initialize(self) -> bool:
./fincept-qt/scripts/alpha_arena/core/base_agent.py:437:                logger.error(f"LLM agent '{self.name}' FAILED to initialize: {self._init_error}")
./fincept-qt/scripts/alpha_arena/core/base_agent.py:438:                self._initialized = False
./fincept-qt/scripts/alpha_arena/core/base_agent.py:440:            await super().initialize()
./fincept-qt/scripts/alpha_arena/core/base_agent.py:443:            logger.error(f"Failed to initialize LLM agent '{self.name}': {e}")
./fincept-qt/scripts/alpha_arena/core/base_agent.py:446:            self._initialized = False
./fincept-qt/scripts/alpha_arena/core/base_agent.py:691:            # Note: Agno's agent.run() is synchronous, so we run it in a thread pool
./fincept-qt/scripts/alpha_arena/core/base_agent.py:919:            # Handle Agno RunOutput object (main response type from agent.run())
./fincept-qt/scripts/alpha_arena/core/database.py:59:        self._initialize_db()
./fincept-qt/scripts/alpha_arena/core/database.py:75:    def _initialize_db(self):
./fincept-qt/scripts/alpha_arena/core/database.py:155:            logger.info(f"Database initialized at {self.db_path}")
./fincept-qt/scripts/alpha_arena/core/broker_adapter.py:333:        self._initialized = False
./fincept-qt/scripts/alpha_arena/core/broker_adapter.py:335:    async def initialize(self):
./fincept-qt/scripts/alpha_arena/core/broker_adapter.py:339:        self._initialized = True
./fincept-qt/scripts/alpha_arena/core/broker_adapter.py:340:        logger.info(f"Multi-exchange provider initialized (default: {self.default_exchange})")
./fincept-qt/scripts/alpha_arena/core/broker_adapter.py:411:            raise RuntimeError("HTTP client not initialized. Call initialize() first.")
./fincept-qt/scripts/alpha_arena/core/broker_adapter.py:445:            raise RuntimeError("HTTP client not initialized. Call initialize() first.")
./fincept-qt/scripts/alpha_arena/core/broker_adapter.py:470:            raise RuntimeError("HTTP client not initialized. Call initialize() first.")
./fincept-qt/scripts/alpha_arena/core/broker_adapter.py:497:            raise RuntimeError("HTTP client not initialized. Call initialize() first.")
./fincept-qt/scripts/alpha_arena/core/broker_adapter.py:526:            raise RuntimeError("HTTP client not initialized. Call initialize() first.")
./fincept-qt/scripts/alpha_arena/core/broker_adapter.py:553:            raise RuntimeError("HTTP client not initialized. Call initialize() first.")
./fincept-qt/scripts/alpha_arena/core/broker_adapter.py:580:            raise RuntimeError("HTTP client not initialized. Call initialize() first.")
./fincept-qt/scripts/alpha_arena/core/broker_adapter.py:608:            raise RuntimeError("HTTP client not initialized. Call initialize() first.")
./fincept-qt/scripts/alpha_arena/core/broker_adapter.py:663:        self._initialized = False
./fincept-qt/scripts/alpha_arena/core/broker_adapter.py:665:    async def initialize(self) -> bool:
./fincept-qt/scripts/alpha_arena/core/broker_adapter.py:668:        await self._data_provider.initialize()
./fincept-qt/scripts/alpha_arena/core/broker_adapter.py:669:        self._initialized = True
./fincept-qt/scripts/alpha_arena/core/broker_adapter.py:670:        logger.info(f"Broker adapter initialized: {self.broker_id} (paper={self.is_paper})")
./fincept-qt/scripts/alpha_arena/core/broker_adapter.py:681:            raise RuntimeError("Adapter not initialized")
./fincept-qt/scripts/alpha_arena/core/broker_adapter.py:784:    """Create and initialize a broker adapter."""
./fincept-qt/scripts/alpha_arena/core/broker_adapter.py:786:    await adapter.initialize()
./fincept-qt/scripts/alpha_arena/core/broker_adapter.py:805:        await _multi_provider.initialize()
./fincept-qt/scripts/alpha_arena/core/sentiment_agent.py:131:    async def initialize(self) -> bool:
./fincept-qt/scripts/alpha_arena/core/sentiment_agent.py:142:        self._initialized = True
./fincept-qt/scripts/alpha_arena/core/sentiment_agent.py:426:        await _sentiment_agent.initialize()
./fincept-qt/scripts/alpha_arena/core/memory_adapter.py:140:            logger.info(f"Session initialized for {self.agent_name}")
./fincept-qt/scripts/alpha_arena/core/memory_adapter.py:145:            logger.warning(f"Failed to initialize session: {e}")
./fincept-qt/scripts/alpha_arena/core/agent_manager.py:45:        self._initialized = False
./fincept-qt/scripts/alpha_arena/core/agent_manager.py:47:    async def initialize(self):
./fincept-qt/scripts/alpha_arena/core/agent_manager.py:49:        if self._initialized:
./fincept-qt/scripts/alpha_arena/core/agent_manager.py:60:        self._initialized = True
./fincept-qt/scripts/alpha_arena/core/agent_manager.py:61:        logger.info(f"Agent manager initialized with {len(self._contexts)} agents")
./fincept-qt/scripts/alpha_arena/core/agent_manager.py:63:    def _ensure_initialized(self):
./fincept-qt/scripts/alpha_arena/core/agent_manager.py:64:        """Ensure the manager is initialized."""
./fincept-qt/scripts/alpha_arena/core/agent_manager.py:65:        if not self._initialized:
./fincept-qt/scripts/alpha_arena/core/agent_manager.py:74:            self._initialized = True
./fincept-qt/scripts/alpha_arena/core/agent_manager.py:95:        self._ensure_initialized()
./fincept-qt/scripts/alpha_arena/core/agent_manager.py:126:            if await instance.initialize():
./fincept-qt/scripts/alpha_arena/core/agent_manager.py:132:                logger.error(f"Failed to initialize agent: {agent_name}")
./fincept-qt/scripts/alpha_arena/core/agent_manager.py:163:        self._ensure_initialized()
./fincept-qt/scripts/alpha_arena/core/agent_manager.py:184:        self._ensure_initialized()
./fincept-qt/scripts/alpha_arena/core/agent_manager.py:193:        self._ensure_initialized()
./fincept-qt/scripts/alpha_arena/core/agent_manager.py:198:        self._ensure_initialized()
./fincept-qt/scripts/alpha_arena/core/agent_manager.py:203:        self._ensure_initialized()
./fincept-qt/scripts/alpha_arena/core/agent_manager.py:209:        self._ensure_initialized()
./fincept-qt/scripts/alpha_arena/core/agent_manager.py:266:        await _manager.initialize()
./fincept-qt/scripts/alpha_arena/core/market_data.py:46:        await self.initialize()
./fincept-qt/scripts/alpha_arena/core/market_data.py:52:    async def initialize(self):
./fincept-qt/scripts/alpha_arena/core/market_data.py:56:        logger.info(f"Market data provider initialized for {self.exchange_id}")
./fincept-qt/scripts/alpha_arena/core/market_data.py:117:            raise RuntimeError("HTTP client not initialized. Call initialize() first.")
./fincept-qt/scripts/alpha_arena/core/market_data.py:158:            raise RuntimeError("HTTP client not initialized. Call initialize() first.")
./fincept-qt/scripts/alpha_arena/core/market_data.py:248:        await _provider.initialize()
./fincept-qt/scripts/alpha_arena/core/market_data.py:284:        await self.initialize()
./fincept-qt/scripts/alpha_arena/core/market_data.py:290:    async def initialize(self):
./fincept-qt/scripts/alpha_arena/core/market_data.py:294:        logger.info("Polymarket data provider initialized")
./fincept-qt/scripts/alpha_arena/core/market_data.py:321:            raise RuntimeError("HTTP client not initialized")
./fincept-qt/scripts/alpha_arena/core/market_data.py:436:        await _polymarket_provider.initialize()
./fincept-qt/scripts/alpha_arena/core/paper_trading_bridge.py:193:        self._initialize_portfolio()
./fincept-qt/scripts/alpha_arena/core/paper_trading_bridge.py:319:    def _initialize_portfolio(self):
./fincept-qt/scripts/alpha_arena/core/paper_trading_bridge.py:541:            logger.error("No portfolio initialized")
./fincept-qt/scripts/alpha_arena/core/paper_trading_bridge.py:969:                reason="Portfolio not initialized",
./fincept-qt/scripts/alpha_arena/core/paper_trading_bridge.py:1206:                reason="Portfolio not initialized",
./fincept-qt/scripts/alpha_arena/core/research_agent.py:188:    async def initialize(self) -> bool:
./fincept-qt/scripts/alpha_arena/core/research_agent.py:192:            edgar_base.initialize_edgar()
./fincept-qt/scripts/alpha_arena/core/research_agent.py:199:        self._initialized = True
./fincept-qt/scripts/alpha_arena/core/research_agent.py:404:        await _research_agent.initialize()
./fincept-qt/scripts/alpha_arena/core/grid_agent.py:105:        self._initialized = False
./fincept-qt/scripts/alpha_arena/core/grid_agent.py:107:    async def initialize(self) -> bool:
./fincept-qt/scripts/alpha_arena/core/grid_agent.py:109:        self._initialized = True
./fincept-qt/scripts/alpha_arena/core/grid_agent.py:110:        logger.info(f"Grid agent '{self.name}' initialized")
./fincept-qt/scripts/alpha_arena/core/grid_agent.py:195:    def _initialize_state(self, current_price: float):
./fincept-qt/scripts/alpha_arena/core/grid_agent.py:282:            self._initialize_state(price)
./fincept-qt/scripts/alpha_arena/core/grid_agent.py:398:            return {"status": "not_initialized"}
./fincept-qt/scripts/alpha_arena/main.py:289:                competition.initialize(api_keys),
./fincept-qt/scripts/alpha_arena/main.py:308:            # Report which agents initialized successfully
./fincept-qt/scripts/alpha_arena/main.py:309:            initialized_agents = list(competition._agents.keys())
./fincept-qt/scripts/alpha_arena/main.py:310:            failed_agents = [m.name for m in models if m.name not in initialized_agents]
./fincept-qt/scripts/alpha_arena/main.py:317:                "models_count": len(initialized_agents),
./fincept-qt/scripts/alpha_arena/main.py:318:                "initialized_agents": initialized_agents,
./fincept-qt/scripts/alpha_arena/main.py:322:                result["warnings"] = [f"{name}: failed to initialize LLM" for name in failed_agents]
./fincept-qt/scripts/alpha_arena/main.py:324:                logger.warning(f"{len(failed_agents)} agent(s) failed to initialize: {failed_agents}")
./fincept-qt/scripts/alpha_arena/main.py:329:            initialized_count = len(competition._agents)
./fincept-qt/scripts/alpha_arena/main.py:334:                    f"Competition initialization failed. Only {initialized_count}/{total_count} agents "
./fincept-qt/scripts/alpha_arena/main.py:335:                    f"initialized successfully. At least 2 agents with valid LLM connections are required. "
./fincept-qt/scripts/alpha_arena/main.py:414:                    competition.initialize(api_keys),
./fincept-qt/scripts/alpha_arena/main.py:419:                    return {"success": False, "error": "Failed to reinitialize competition from database"}
./fincept-qt/scripts/alpha_arena/main.py:1047:        await agent.initialize()
./fincept-qt/scripts/alpha_arena/main.py:1535:def main(args=None):
./fincept-qt/scripts/alpha_arena/main.py:1563:        result = asyncio.run(handle_action(action, params, api_keys))
./fincept-qt/scripts/alpha_arena/main.py:1573:if __name__ == "__main__":
./fincept-qt/scripts/alpha_arena/main.py:1574:    result = main()
./fincept-qt/scripts/cninfo_pdf_text_extractor.py:225:def main() -> None:
./fincept-qt/scripts/cninfo_pdf_text_extractor.py:281:if __name__ == "__main__":
./fincept-qt/scripts/cninfo_pdf_text_extractor.py:282:    main()
./fincept-qt/scripts/canada_gov_api.py:659:def main():
./fincept-qt/scripts/canada_gov_api.py:771:if __name__ == "__main__":
./fincept-qt/scripts/canada_gov_api.py:772:    main()
./fincept-qt/scripts/fmp_extra_data.py:53:def main(args=None):
./fincept-qt/scripts/fmp_extra_data.py:85:if __name__ == "__main__":
./fincept-qt/scripts/fmp_extra_data.py:86:    main()
./fincept-qt/scripts/unep_data.py:86:def main(args=None):
./fincept-qt/scripts/unep_data.py:120:if __name__ == "__main__":
./fincept-qt/scripts/unep_data.py:121:    main()
./fincept-qt/scripts/global_health_security_data.py:174:def main(args=None):
./fincept-qt/scripts/global_health_security_data.py:214:if __name__ == "__main__":
./fincept-qt/scripts/global_health_security_data.py:215:    main()
./fincept-qt/scripts/undp_data.py:84:def main(args=None):
./fincept-qt/scripts/undp_data.py:120:if __name__ == "__main__":
./fincept-qt/scripts/undp_data.py:121:    main()
./fincept-qt/scripts/rba_data.py:426:def main() -> None:
./fincept-qt/scripts/rba_data.py:491:if __name__ == "__main__":
./fincept-qt/scripts/rba_data.py:492:    main()
./fincept-qt/scripts/akshare_alternative.py:228:if __name__ == "__main__":
./fincept-qt/scripts/technicals/technical_analysis.py:223:def main():
./fincept-qt/scripts/technicals/technical_analysis.py:342:if __name__ == "__main__":
./fincept-qt/scripts/technicals/technical_analysis.py:343:    main()
./fincept-qt/scripts/fiscal_data.py:689:def main():
./fincept-qt/scripts/fiscal_data.py:794:if __name__ == "__main__":
./fincept-qt/scripts/fiscal_data.py:795:    main()
./fincept-qt/scripts/marketstack_data.py:78:def main(args=None):
./fincept-qt/scripts/marketstack_data.py:119:if __name__ == "__main__":
./fincept-qt/scripts/marketstack_data.py:120:    main()
./fincept-qt/scripts/baostock_daily_backfill.py:276:def main() -> None:
./fincept-qt/scripts/baostock_daily_backfill.py:341:if __name__ == "__main__":
./fincept-qt/scripts/baostock_daily_backfill.py:342:    main()
./fincept-qt/scripts/intrinio_data.py:60:def main(args=None):
./fincept-qt/scripts/intrinio_data.py:97:if __name__ == "__main__":
./fincept-qt/scripts/intrinio_data.py:98:    main()
./fincept-qt/scripts/coingecko.py:149:def main(args=None):
./fincept-qt/scripts/coingecko.py:183:if __name__ == "__main__":
./fincept-qt/scripts/coingecko.py:184:    main()
./fincept-qt/scripts/messari_data.py:143:def main(args=None):
./fincept-qt/scripts/messari_data.py:194:if __name__ == "__main__":
./fincept-qt/scripts/messari_data.py:195:    main()
./fincept-qt/scripts/akshare_crypto.py:104:def main():
./fincept-qt/scripts/akshare_crypto.py:131:if __name__ == "__main__":
./fincept-qt/scripts/akshare_crypto.py:132:    main()
./fincept-qt/scripts/open_secrets_data.py:92:def main(args=None):
./fincept-qt/scripts/open_secrets_data.py:129:if __name__ == "__main__":
./fincept-qt/scripts/open_secrets_data.py:130:    main()
./fincept-qt/scripts/spreadsheet.py:23:import argparse
./fincept-qt/scripts/spreadsheet.py:192:def main():
./fincept-qt/scripts/spreadsheet.py:193:    parser = argparse.ArgumentParser()
./fincept-qt/scripts/spreadsheet.py:259:if __name__ == "__main__":
./fincept-qt/scripts/spreadsheet.py:260:    main()
./fincept-qt/scripts/baostock_fundamentals_quarterly.py:275:def main() -> None:
./fincept-qt/scripts/baostock_fundamentals_quarterly.py:360:if __name__ == "__main__":
./fincept-qt/scripts/baostock_fundamentals_quarterly.py:361:    main()
./fincept-qt/scripts/waqi_data.py:122:def main(args=None):
./fincept-qt/scripts/waqi_data.py:170:if __name__ == "__main__":
./fincept-qt/scripts/waqi_data.py:171:    main()
./fincept-qt/scripts/translate_text.py:124:def main(args=None):
./fincept-qt/scripts/translate_text.py:151:if __name__ == "__main__":
./fincept-qt/scripts/translate_text.py:152:    main()
./fincept-qt/scripts/exchange/fetch_ticker.py:35:def main():
./fincept-qt/scripts/exchange/fetch_ticker.py:65:if __name__ == "__main__":
./fincept-qt/scripts/exchange/fetch_ticker.py:66:    main()
./fincept-qt/scripts/exchange/fetch_balance.py:29:def main():
./fincept-qt/scripts/exchange/fetch_balance.py:62:if __name__ == "__main__":
./fincept-qt/scripts/exchange/fetch_balance.py:63:    main()
./fincept-qt/scripts/exchange/exchange_daemon.py:503:def main():
./fincept-qt/scripts/exchange/exchange_daemon.py:536:if __name__ == "__main__":
./fincept-qt/scripts/exchange/exchange_daemon.py:543:        main()
./fincept-qt/scripts/exchange/fetch_ohlcv.py:27:def main():
./fincept-qt/scripts/exchange/fetch_ohlcv.py:57:if __name__ == "__main__":
./fincept-qt/scripts/exchange/fetch_ohlcv.py:58:    main()
./fincept-qt/scripts/exchange/fetch_orderbook.py:29:def main():
./fincept-qt/scripts/exchange/fetch_orderbook.py:57:if __name__ == "__main__":
./fincept-qt/scripts/exchange/fetch_orderbook.py:58:    main()
./fincept-qt/scripts/exchange/ws_stream.py:457:async def main():
./fincept-qt/scripts/exchange/ws_stream.py:603:if __name__ == "__main__":
./fincept-qt/scripts/exchange/ws_stream.py:609:        asyncio.run(main())
./fincept-qt/scripts/exchange/broker_ws_bridge.py:28:import argparse
./fincept-qt/scripts/exchange/broker_ws_bridge.py:198:    Import the openalgo adapter for `broker`, initialize it with credentials,
./fincept-qt/scripts/exchange/broker_ws_bridge.py:246:        result = adapter.initialize(broker, user_id, auth_data=auth_data)
./fincept-qt/scripts/exchange/broker_ws_bridge.py:247:        emit_status(broker, False, f"Adapter initialized: {result}")
./fincept-qt/scripts/exchange/broker_ws_bridge.py:385:    p = argparse.ArgumentParser()
./fincept-qt/scripts/exchange/broker_ws_bridge.py:397:def main():
./fincept-qt/scripts/exchange/broker_ws_bridge.py:436:if __name__ == "__main__":
./fincept-qt/scripts/exchange/broker_ws_bridge.py:437:    main()
./fincept-qt/scripts/exchange/fetch_trades.py:26:def main():
./fincept-qt/scripts/exchange/fetch_trades.py:54:if __name__ == "__main__":
./fincept-qt/scripts/exchange/fetch_trades.py:55:    main()
./fincept-qt/scripts/exchange/set_margin_mode.py:10:def main():
./fincept-qt/scripts/exchange/set_margin_mode.py:25:if __name__ == "__main__":
./fincept-qt/scripts/exchange/set_margin_mode.py:26:    main()
./fincept-qt/scripts/exchange/list_exchanges.py:36:def main():
./fincept-qt/scripts/exchange/list_exchanges.py:68:if __name__ == "__main__":
./fincept-qt/scripts/exchange/list_exchanges.py:69:    main()
./fincept-qt/scripts/exchange/list_exchange_ids.py:21:def main():
./fincept-qt/scripts/exchange/list_exchange_ids.py:29:if __name__ == "__main__":
./fincept-qt/scripts/exchange/list_exchange_ids.py:30:    main()
./fincept-qt/scripts/exchange/fetch_markets.py:43:def main():
./fincept-qt/scripts/exchange/fetch_markets.py:88:if __name__ == "__main__":
./fincept-qt/scripts/exchange/fetch_markets.py:89:    main()
./fincept-qt/scripts/exchange/resolve_kraken_symbols.py:67:def main() -> None:
./fincept-qt/scripts/exchange/resolve_kraken_symbols.py:94:if __name__ == "__main__":
./fincept-qt/scripts/exchange/resolve_kraken_symbols.py:95:    main()
./fincept-qt/scripts/exchange/set_leverage.py:10:def main():
./fincept-qt/scripts/exchange/set_leverage.py:25:if __name__ == "__main__":
./fincept-qt/scripts/exchange/set_leverage.py:26:    main()
./fincept-qt/scripts/exchange/totp_gen.py:7:def main():
./fincept-qt/scripts/exchange/totp_gen.py:32:if __name__ == "__main__":
./fincept-qt/scripts/exchange/totp_gen.py:33:    main()
./fincept-qt/scripts/exchange/fetch_funding_rate.py:23:def main():
./fincept-qt/scripts/exchange/fetch_funding_rate.py:75:if __name__ == "__main__":
./fincept-qt/scripts/exchange/fetch_funding_rate.py:76:    main()
./fincept-qt/scripts/exchange/fetch_my_trades.py:10:def main():
./fincept-qt/scripts/exchange/fetch_my_trades.py:41:if __name__ == "__main__":
./fincept-qt/scripts/exchange/fetch_my_trades.py:42:    main()
./fincept-qt/scripts/exchange/fetch_open_orders.py:10:def main():
./fincept-qt/scripts/exchange/fetch_open_orders.py:43:if __name__ == "__main__":
./fincept-qt/scripts/exchange/fetch_open_orders.py:44:    main()
./fincept-qt/scripts/exchange/fetch_mark_price.py:9:def main():
./fincept-qt/scripts/exchange/fetch_mark_price.py:30:if __name__ == "__main__":
./fincept-qt/scripts/exchange/fetch_mark_price.py:31:    main()
./fincept-qt/scripts/exchange/fetch_positions.py:10:def main():
./fincept-qt/scripts/exchange/fetch_positions.py:46:if __name__ == "__main__":
./fincept-qt/scripts/exchange/fetch_positions.py:47:    main()
./fincept-qt/scripts/exchange/fetch_trading_fees.py:9:def main():
./fincept-qt/scripts/exchange/fetch_trading_fees.py:38:if __name__ == "__main__":
./fincept-qt/scripts/exchange/fetch_trading_fees.py:39:    main()
./fincept-qt/scripts/exchange/fetch_open_interest.py:20:def main():
./fincept-qt/scripts/exchange/fetch_open_interest.py:56:if __name__ == "__main__":
./fincept-qt/scripts/exchange/fetch_open_interest.py:57:    main()
./fincept-qt/scripts/exchange/fetch_tickers.py:45:def main():
./fincept-qt/scripts/exchange/fetch_tickers.py:67:if __name__ == "__main__":
./fincept-qt/scripts/exchange/fetch_tickers.py:68:    main()
./fincept-qt/scripts/exchange/cancel_order.py:27:def main():
./fincept-qt/scripts/exchange/cancel_order.py:56:if __name__ == "__main__":
./fincept-qt/scripts/exchange/cancel_order.py:57:    main()
./fincept-qt/scripts/exchange/place_order.py:39:def main():
./fincept-qt/scripts/exchange/place_order.py:102:if __name__ == "__main__":
./fincept-qt/scripts/exchange/place_order.py:103:    main()
./fincept-qt/scripts/databento_provider.py:163:            raise ValueError(f"Failed to initialize Databento client: {e}")
./fincept-qt/scripts/databento_provider.py:3196:def main():
./fincept-qt/scripts/databento_provider.py:3588:if __name__ == "__main__":
./fincept-qt/scripts/databento_provider.py:3589:    main()
./fincept-qt/scripts/openCorporates_data.py:225:def main(args=None):
./fincept-qt/scripts/openCorporates_data.py:270:if __name__ == "__main__":
./fincept-qt/scripts/openCorporates_data.py:271:    main()
./fincept-qt/scripts/crossref_data.py:178:def main(args=None):
./fincept-qt/scripts/crossref_data.py:224:if __name__ == "__main__":
./fincept-qt/scripts/crossref_data.py:225:    main()
./fincept-qt/scripts/wto_data_extended.py:94:def main(args=None):
./fincept-qt/scripts/wto_data_extended.py:133:if __name__ == "__main__":
./fincept-qt/scripts/wto_data_extended.py:134:    main()
./fincept-qt/scripts/entso_e_data.py:68:def main(args=None):
```

## 11. 可能的核心源码文件预览

### fincept-qt/scripts/abs_data.py

```python
"""
Australian Bureau of Statistics Data Fetcher
ABS: Australian economic, demographic, social statistics — GDP, CPI, labour, trade.
"""
import sys
import json
import os
import requests
from typing import Dict, Any, Optional, List

BASE_URL = "https://api.data.abs.gov.au"

ABS_DATAFLOWS = {
    "gdp": "ANA_AGG",
    "cpi": "CPI",
    "labour": "LF",
    "trade": "MERCH_EXP",
    "population": "ERP_QUARTERLY"
}

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=3)
session.mount('https://', adapter)
session.mount('http://', adapter)


def _make_request(endpoint: str, params: Dict = None) -> Any:
    url = f"{BASE_URL}/{endpoint}" if not endpoint.startswith('http') else endpoint
    if params is None:
        params = {}
    params.setdefault("format", "jsondata")
    try:
        response = session.get(url, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except (json.JSONDecodeError, ValueError) as e:
        return {"error": f"JSON decode error: {str(e)}"}


def get_dataflow(dataflow_id: str) -> Any:
    return _make_request(f"dataflow/ABS/{dataflow_id}")


def get_data(dataflow_id: str, key: str = "all", start_period: str = None, end_period: str = None) -> Any:
    params = {}
    if start_period:
        params["startPeriod"] = start_period
    if end_period:
        params["endPeriod"] = end_period
    return _make_request(f"data/{dataflow_id}/{key}", params=params)


def get_gdp(state: str = "AUS", frequency: str = "Q", start: str = "2020-Q1", end: str = "2024-Q4") -> Any:
    dataflow = ABS_DATAFLOWS["gdp"]
    params = {"startPeriod": start, "endPeriod": end}
    return _make_request(f"data/{dataflow}/{state}..", params=params)


def get_cpi(product_group: str = "1", state: str = "50", start: str = "2020-Q1", end: str = "2024-Q4") -> Any:
    dataflow = ABS_DATAFLOWS["cpi"]
    params = {"startPeriod": start, "endPeriod": end}
    return _make_request(f"data/{dataflow}/{product_group}.{state}.", params=params)


def get_labour(state: str = "AUS", sex: str = "3", start: str = "2020-01", end: str = "2024-12") -> Any:
    dataflow = ABS_DATAFLOWS["labour"]
    params = {"startPeriod": start, "endPeriod": end}
    return _make_request(f"data/{dataflow}/{state}.{sex}.", params=params)


def get_trade(product: str = "all", partner: str = "all", start: str = "2020-01", end: str = "2024-12") -> Any:
    dataflow = ABS_DATAFLOWS["trade"]
    params = {"startPeriod": start, "endPeriod": end}
    key = f"{product}.{partner}" if product != "all" or partner != "all" else "all"
    return _make_request(f"data/{dataflow}/{key}", params=params)


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if not args:
        print(json.dumps({"error": "No command provided"}))
        return
    command = args[0]
    result = {"error": f"Unknown command: {command}"}
    if command == "dataflow":
        dataflow_id = args[1] if len(args) > 1 else "ANA_AGG"
        result = get_dataflow(dataflow_id)
    elif command == "data":
        dataflow_id = args[1] if len(args) > 1 else "ANA_AGG"
        key = args[2] if len(args) > 2 else "all"
        start_period = args[3] if len(args) > 3 else None
        end_period = args[4] if len(args) > 4 else None
        result = get_data(dataflow_id, key, start_period, end_period)
    elif command == "gdp":
        state = args[1] if len(args) > 1 else "AUS"
        frequency = args[2] if len(args) > 2 else "Q"
        start = args[3] if len(args) > 3 else "2020-Q1"
        end = args[4] if len(args) > 4 else "2024-Q4"
        result = get_gdp(state, frequency, start, end)
    elif command == "cpi":
        product_group = args[1] if len(args) > 1 else "1"
        state = args[2] if len(args) > 2 else "50"
        start = args[3] if len(args) > 3 else "2020-Q1"
        end = args[4] if len(args) > 4 else "2024-Q4"
        result = get_cpi(product_group, state, start, end)
    elif command == "labour":
        state = args[1] if len(args) > 1 else "AUS"
        sex = args[2] if len(args) > 2 else "3"
        start = args[3] if len(args) > 3 else "2020-01"
        end = args[4] if len(args) > 4 else "2024-12"
        result = get_labour(state, sex, start, end)
    elif command == "trade":
        product = args[1] if len(args) > 1 else "all"
        partner = args[2] if len(args) > 2 else "all"
        start = args[3] if len(args) > 3 else "2020-01"
        end = args[4] if len(args) > 4 else "2024-12"
        result = get_trade(product, partner, start, end)
    print(json.dumps(result))


if __name__ == "__main__":
    main()
```

### fincept-qt/scripts/acled_data.py

```python
"""
ACLED (Armed Conflict Location & Event Data) Fetcher
Provides political violence events, protest data, conflict fatalities,
actor information, and trend analysis for countries globally.
"""
import sys
import json
import os
import requests
from typing import Dict, Any, Optional, List

API_KEY = os.environ.get('ACLED_API_KEY', '')
ACLED_EMAIL = os.environ.get('ACLED_EMAIL', '')
BASE_URL = "https://api.acleddata.com/acled/read"

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=3)
session.mount('https://', adapter)
session.mount('http://', adapter)


def _make_request(endpoint: str, params: Dict = None) -> Any:
    url = f"{BASE_URL}/{endpoint}" if not endpoint.startswith('http') else endpoint
    try:
        response = session.get(url, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except (json.JSONDecodeError, ValueError) as e:
        return {"error": f"JSON decode error: {str(e)}"}


def _check_credentials() -> Optional[Dict]:
    if not API_KEY or not ACLED_EMAIL:
        return {"error": "ACLED_API_KEY and ACLED_EMAIL environment variables required"}
    return None


def _base_params() -> Dict:
    return {"key": API_KEY, "email": ACLED_EMAIL}


def get_events(country: str, event_type: str = None, start_date: str = None, end_date: str = None, limit: int = 100) -> Any:
    """Return conflict/protest events for a country within a date range."""
    err = _check_credentials()
    if err:
        return err
    params = _base_params()
    params["country"] = country
    params["limit"] = limit
    if event_type:
        params["event_type"] = event_type
    if start_date:
        params["event_date"] = start_date
        params["event_date_where"] = "BETWEEN"
    if end_date:
        params["event_date2"] = end_date
    data = _make_request(BASE_URL, params=params)
    if isinstance(data, dict) and "error" in data:
        return data
    return {"country": country, "event_type": event_type, "start_date": start_date,
            "end_date": end_date, "events": data.get("data", []), "count": data.get("count", 0)}


def get_fatalities(country: str, year: int) -> Any:
    """Return total fatalities from conflict events in a country for a given year."""
    err = _check_credentials()
    if err:
        return err
    params = _base_params()
    params["country"] = country
    params["year"] = year
    params["fields"] = "fatalities,event_date,event_type"
    params["limit"] = 500
    data = _make_request(BASE_URL, params=params)
    if isinstance(data, dict) and "error" in data:
        return data
    events = data.get("data", [])
    total_fatalities = sum(int(e.get("fatalities", 0)) for e in events if e.get("fatalities"))
    return {"country": country, "year": year, "total_fatalities": total_fatalities,
            "event_count": len(events), "events": events}


def get_trends(country: str, year: int) -> Any:
    """Return monthly event count and fatality trends for a country."""
    err = _check_credentials()
    if err:
        return err
    params = _base_params()
    params["country"] = country
    params["year"] = year
    params["fields"] = "event_date,event_type,fatalities"
    params["limit"] = 1000
    data = _make_request(BASE_URL, params=params)
    if isinstance(data, dict) and "error" in data:
        return data
    events = data.get("data", [])
    monthly: Dict[str, Dict] = {}
    for event in events:
        date_str = event.get("event_date", "")
        if date_str and len(date_str) >= 7:
            month_key = date_str[:7]
            if month_key not in monthly:
                monthly[month_key] = {"events": 0, "fatalities": 0}
            monthly[month_key]["events"] += 1
            monthly[month_key]["fatalities"] += int(event.get("fatalities", 0))
    return {"country": country, "year": year, "monthly_trends": monthly}


def get_event_types() -> Any:
    """Return all ACLED event type categories."""
    event_types = [
        "Battles", "Violence against civilians", "Explosions/Remote violence",
        "Protests", "Riots", "Strategic developments"
    ]
    return {"event_types": event_types, "count": len(event_types)}


def get_actors(country: str, year: int) -> Any:
    """Return conflict actors active in a country for a given year."""
    err = _check_credentials()
    if err:
        return err
    params = _base_params()
    params["country"] = country
    params["year"] = year
    params["fields"] = "actor1,actor2,inter1,inter2"
    params["limit"] = 500
    data = _make_request(BASE_URL, params=params)
    if isinstance(data, dict) and "error" in data:
        return data
    events = data.get("data", [])
    actors: set = set()
    for event in events:
        if event.get("actor1"):
            actors.add(event["actor1"])
        if event.get("actor2"):
            actors.add(event["actor2"])
    return {"country": country, "year": year, "actors": sorted(list(actors)), "count": len(actors)}


def get_regions() -> Any:
    """Return all geographic regions covered by ACLED."""
    regions = [
        "Western Africa", "Middle Africa", "Eastern Africa", "Southern Africa",
        "Northern Africa", "South Asia", "Southeast Asia", "East Asia",
        "Middle East", "Central Asia", "Caucasus and Central Asia",
        "Europe", "Central America", "South America", "North America",
        "Caribbean", "Oceania"
    ]
    return {"regions": regions, "count": len(regions)}


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if not args:
        print(json.dumps({"error": "No command provided"}))
        return
    command = args[0]
    result = {"error": f"Unknown command: {command}"}
    if command == "events":
        country = args[1] if len(args) > 1 else ""
        if not country:
            result = {"error": "country required"}
        else:
            event_type = args[2] if len(args) > 2 else None
            start_date = args[3] if len(args) > 3 else None
            end_date = args[4] if len(args) > 4 else None
            limit = int(args[5]) if len(args) > 5 else 100
            result = get_events(country, event_type, start_date, end_date, limit)
    elif command == "fatalities":
        if len(args) < 3:
            result = {"error": "country and year required"}
        else:
            result = get_fatalities(args[1], int(args[2]))
    elif command == "trends":

# ... 文件较长，已截断。总行数：198
```

### fincept-qt/scripts/adb_data.py

```python
"""
Asian Development Bank (ADB) Key Indicators Database (KIDB) Data Fetcher
Fetches macroeconomic and social indicators from Asia-Pacific region
Returns JSON output for Qt/C++ integration

API Documentation: https://kidb.adb.org/api
Rate Limit: 30 queries per minute
"""

import sys
import json
import os
import requests
from typing import Dict, List, Optional, Any, Union
from datetime import datetime
import urllib.parse

# --- CONFIGURATION ---
BASE_URL = "https://kidb.adb.org/api/v4/sdmx"
TIMEOUT = 30
RATE_LIMIT_DELAY = 2.1  # ~28 queries per minute to stay under limit

# Common SDMX components
FREQUENCIES = {
    'A': 'Annual',
    'Q': 'Quarterly',
    'M': 'Monthly'
}

# Major dataflow codes (can be expanded)
DATAFLOWS = {
    'EO_NA': 'National Accounts',
    'PPL_POP': 'Population',
    'EO_FI': 'Financial Indicators',
    'EO_TR': 'Trade',
    'EO_PM': 'Price Management',
    'EO_GOV': 'Government Finance',
    'EO_EL': 'External Sector'
}

# Common economy codes (ISO 3-letter country codes)
ECONOMIES = {
    'PHI': 'Philippines',
    'SGP': 'Singapore',
    'JPN': 'Japan',
    'CHN': 'China',
    'IND': 'India',
    'KOR': 'Korea',
    'THA': 'Thailand',
    'MYS': 'Malaysia',
    'IDN': 'Indonesia',
    'VNM': 'Vietnam',
    'HKG': 'Hong Kong',
    'TWN': 'Taiwan',
    'AUS': 'Australia',
    'NZL': 'New Zealand',
    'all': 'All Economies'
}

def _make_request(endpoint: str, params: Optional[Dict[str, Any]] = None, format_type: str = "sdmx-json") -> Dict[str, Any]:
    """
    Centralized request handler with comprehensive error handling

    Args:
        endpoint: API endpoint path
        params: Query parameters
        format_type: Response format (sdmx-json, sdmx-csv, or xml)

    Returns:
        Dict with consistent structure: {"data": [...], "metadata": {...}, "error": None/error_msg}
    """
    try:
        url = f"{BASE_URL}/{endpoint}"

        # Add format parameter if not already present
        if params is None:
            params = {}
        if 'format' not in params:
            params['format'] = format_type

        # Make request with timeout
        response = requests.get(url, params=params, timeout=TIMEOUT)
        response.raise_for_status()

        # Check if response is an XML error (ADB returns XML for errors even when JSON requested)
        if response.text.strip().startswith('<?xml') or response.text.strip().startswith('<'):
            # Extract error message from XML
            import re
            error_match = re.search(r'<com:Text>([^<]+)</com:Text>', response.text)
            error_msg = error_match.group(1) if error_match else "Unknown API error"
            return {
                "data": [],
                "metadata": {
                    "source": "Asian Development Bank (ADB) - Key Indicators Database",
                    "endpoint": endpoint,
                    "parameters": params
                },
                "error": f"ADB API Error: {error_msg}"
            }

        # Process response based on format
        if format_type == "sdmx-json":
            data = response.json()
        else:
            data = response.text

        # Return structured success response
        return {
            "data": data,
            "metadata": {
                "source": "Asian Development Bank (ADB) - Key Indicators Database",
                "endpoint": endpoint,
                "parameters": params,
                "last_updated": datetime.now().isoformat(),
                "url": response.url
            },
            "error": None
        }

    except requests.exceptions.HTTPError as e:
        return {
            "data": [],
            "metadata": {
                "source": "Asian Development Bank (ADB) - Key Indicators Database",
                "endpoint": endpoint,
                "parameters": params,
                "http_status": e.response.status_code
            },
            "error": f"HTTP Error: {e.response.status_code} - {e.response.text}"
        }
    except requests.exceptions.Timeout:
        return {
            "data": [],
            "metadata": {
                "source": "Asian Development Bank (ADB) - Key Indicators Database",
                "endpoint": endpoint,
                "parameters": params
            },
            "error": "Request timeout. The ADB API is taking too long to respond."
        }
    except requests.exceptions.ConnectionError:
        return {
            "data": [],
            "metadata": {
                "source": "Asian Development Bank (ADB) - Key Indicators Database",
                "endpoint": endpoint,
                "parameters": params
            },
            "error": "Connection error. Could not connect to ADB API."
        }
    except requests.exceptions.RequestException as e:
        return {
            "data": [],
            "metadata": {
                "source": "Asian Development Bank (ADB) - Key Indicators Database",
                "endpoint": endpoint,
                "parameters": params
            },
            "error": f"Request error: {str(e)}"
        }
    except json.JSONDecodeError:
        return {
            "data": [],
            "metadata": {
                "source": "Asian Development Bank (ADB) - Key Indicators Database",
                "endpoint": endpoint,
                "parameters": params
            },
            "error": "Invalid JSON response from ADB API."
        }
    except Exception as e:
        return {
            "data": [],
            "metadata": {
                "source": "Asian Development Bank (ADB) - Key Indicators Database",
                "endpoint": endpoint,
                "parameters": params
            },
            "error": f"An unexpected error occurred: {str(e)}"
        }

# ... 文件较长，已截断。总行数：729
```

### fincept-qt/scripts/adb_data_extended.py

```python
"""
Asian Development Bank (ADB) Extended Data Fetcher
Additional indicators covering poverty, gender, climate, and infrastructure
for Asia-Pacific countries via the ADB Key Indicators Database (KIDB).
"""
import sys
import json
import os
import requests
from typing import Dict, Any, Optional, List

API_KEY = os.environ.get('ADB_API_KEY', '')
BASE_URL = "https://kidb.adb.org/api"

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=3)
session.mount('https://', adapter)
session.mount('http://', adapter)


def _make_request(endpoint: str, params: Dict = None) -> Any:
    url = f"{BASE_URL}/{endpoint}" if not endpoint.startswith('http') else endpoint
    try:
        response = session.get(url, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except (json.JSONDecodeError, ValueError) as e:
        return {"error": f"JSON decode error: {str(e)}"}


def get_gdp_data(country: str = None, year: str = None) -> Any:
    params = {"indicator": "GDP", "category": "economy"}
    if country:
        params["country"] = country
    if year:
        params["year"] = year
    return _make_request("indicators/gdp", params)


def get_poverty_data(country: str = None, year: str = None) -> Any:
    params = {"category": "poverty"}
    if country:
        params["country"] = country
    if year:
        params["year"] = year
    return _make_request("indicators/poverty", params)


def get_gender_data(country: str = None, indicator: str = None, year: str = None) -> Any:
    params = {"category": "gender"}
    if country:
        params["country"] = country
    if indicator:
        params["indicator"] = indicator
    if year:
        params["year"] = year
    return _make_request("indicators/gender", params)


def get_climate_data(country: str = None, indicator: str = None, year: str = None) -> Any:
    params = {"category": "climate"}
    if country:
        params["country"] = country
    if indicator:
        params["indicator"] = indicator
    if year:
        params["year"] = year
    return _make_request("indicators/climate", params)


def get_infrastructure_data(country: str = None, sector: str = None, year: str = None) -> Any:
    params = {"category": "infrastructure"}
    if country:
        params["country"] = country
    if sector:
        params["sector"] = sector
    if year:
        params["year"] = year
    return _make_request("indicators/infrastructure", params)


def get_countries() -> Any:
    return _make_request("countries")


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if not args:
        print(json.dumps({"error": "No command provided"}))
        return
    command = args[0]
    result = {"error": f"Unknown command: {command}"}
    if command == "gdp":
        country = args[1] if len(args) > 1 else None
        year = args[2] if len(args) > 2 else None
        result = get_gdp_data(country, year)
    elif command == "poverty":
        country = args[1] if len(args) > 1 else None
        year = args[2] if len(args) > 2 else None
        result = get_poverty_data(country, year)
    elif command == "gender":
        country = args[1] if len(args) > 1 else None
        indicator = args[2] if len(args) > 2 else None
        year = args[3] if len(args) > 3 else None
        result = get_gender_data(country, indicator, year)
    elif command == "climate":
        country = args[1] if len(args) > 1 else None
        indicator = args[2] if len(args) > 2 else None
        year = args[3] if len(args) > 3 else None
        result = get_climate_data(country, indicator, year)
    elif command == "infrastructure":
        country = args[1] if len(args) > 1 else None
        sector = args[2] if len(args) > 2 else None
        year = args[3] if len(args) > 3 else None
        result = get_infrastructure_data(country, sector, year)
    elif command == "countries":
        result = get_countries()
    print(json.dumps(result))


if __name__ == "__main__":
    main()
```

### fincept-qt/scripts/afdb_data.py

```python
"""
African Development Bank (AfDB) Data Fetcher
African economic data, projects, infrastructure, and development indicators
from the AfDB Open Data for Africa portal.
"""
import sys
import json
import os
import requests
from typing import Dict, Any, Optional, List

API_KEY = os.environ.get('AFDB_API_KEY', '')
BASE_URL = "https://dataportal.opendataforafrica.org/api/1.0"

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=3)
session.mount('https://', adapter)
session.mount('http://', adapter)


def _make_request(endpoint: str, params: Dict = None) -> Any:
    url = f"{BASE_URL}/{endpoint}" if not endpoint.startswith('http') else endpoint
    try:
        response = session.get(url, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except (json.JSONDecodeError, ValueError) as e:
        return {"error": f"JSON decode error: {str(e)}"}


def get_datasets() -> Any:
    return _make_request("datasets")


def get_indicator_data(dataset_id: str = None, country: str = None, indicator: str = None, year: str = None) -> Any:
    params = {}
    if dataset_id:
        params["dataset"] = dataset_id
    if country:
        params["country"] = country
    if indicator:
        params["indicator"] = indicator
    if year:
        params["year"] = year
    return _make_request("data", params)


def get_countries() -> Any:
    return _make_request("countries")


def get_projects(country: str = None, sector: str = None, status: str = None) -> Any:
    params = {}
    if country:
        params["country"] = country
    if sector:
        params["sector"] = sector
    if status:
        params["status"] = status
    return _make_request("projects", params)


def get_economic_indicators(country: str = None, year: str = None) -> Any:
    params = {"category": "economic"}
    if country:
        params["country"] = country
    if year:
        params["year"] = year
    return _make_request("indicators", params)


def get_infrastructure_data(country: str = None, sector: str = None) -> Any:
    params = {"category": "infrastructure"}
    if country:
        params["country"] = country
    if sector:
        params["sector"] = sector
    return _make_request("infrastructure", params)


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if not args:
        print(json.dumps({"error": "No command provided"}))
        return
    command = args[0]
    result = {"error": f"Unknown command: {command}"}
    if command == "datasets":
        result = get_datasets()
    elif command == "data":
        dataset_id = args[1] if len(args) > 1 else None
        country = args[2] if len(args) > 2 else None
        indicator = args[3] if len(args) > 3 else None
        year = args[4] if len(args) > 4 else None
        result = get_indicator_data(dataset_id, country, indicator, year)
    elif command == "countries":
        result = get_countries()
    elif command == "projects":
        country = args[1] if len(args) > 1 else None
        sector = args[2] if len(args) > 2 else None
        status = args[3] if len(args) > 3 else None
        result = get_projects(country, sector, status)
    elif command == "economic":
        country = args[1] if len(args) > 1 else None
        year = args[2] if len(args) > 2 else None
        result = get_economic_indicators(country, year)
    elif command == "infrastructure":
        country = args[1] if len(args) > 1 else None
        sector = args[2] if len(args) > 2 else None
        result = get_infrastructure_data(country, sector)
    print(json.dumps(result))


if __name__ == "__main__":
    main()
```

### fincept-qt/scripts/aisstream_data.py

```python
"""
AISStream Data Fetcher
Global real-time AIS vessel positions, vessel info, port calls
via AISStream REST API (free key required).
"""
import sys
import json
import os
import requests
from typing import Dict, Any, Optional, List

API_KEY = os.environ.get('AISSTREAM_API_KEY', '')
BASE_URL = "https://api.aisstream.io/v0"

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=3)
session.mount('https://', adapter)
session.mount('http://', adapter)


def _make_request(endpoint: str, params: Dict = None) -> Any:
    url = f"{BASE_URL}/{endpoint}" if not endpoint.startswith('http') else endpoint
    headers = {}
    if API_KEY:
        headers["X-API-Key"] = API_KEY
    try:
        response = session.get(url, params=params, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except (json.JSONDecodeError, ValueError) as e:
        return {"error": f"JSON decode error: {str(e)}"}


def _make_post_request(endpoint: str, payload: Dict) -> Any:
    url = f"{BASE_URL}/{endpoint}" if not endpoint.startswith('http') else endpoint
    headers = {"Content-Type": "application/json"}
    if API_KEY:
        headers["X-API-Key"] = API_KEY
    try:
        response = session.post(url, json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except (json.JSONDecodeError, ValueError) as e:
        return {"error": f"JSON decode error: {str(e)}"}


def get_vessels_in_area(lat1: float, lon1: float, lat2: float, lon2: float) -> Any:
    payload = {
        "BoundingBoxes": [[[lat1, lon1], [lat2, lon2]]]
    }
    return _make_post_request("vessels/area", payload)


def get_vessel_by_mmsi(mmsi: str) -> Any:
    return _make_request(f"vessels/{mmsi}")


def get_vessel_track(mmsi: str, start_date: str = None, end_date: str = None) -> Any:
    params = {}
    if start_date:
        params["start_date"] = start_date
    if end_date:
        params["end_date"] = end_date
    return _make_request(f"vessels/{mmsi}/track", params)


def get_port_calls(port_name: str = None, start_date: str = None, end_date: str = None) -> Any:
    params = {}
    if port_name:
        params["port_name"] = port_name
    if start_date:
        params["start_date"] = start_date
    if end_date:
        params["end_date"] = end_date
    return _make_request("port-calls", params)


def get_fleet(vessel_type: str = None, limit: int = 50) -> Any:
    params = {"limit": limit}
    if vessel_type:
        params["vessel_type"] = vessel_type
    return _make_request("vessels", params)


def search_vessel(name: str) -> Any:
    params = {"name": name}
    return _make_request("vessels/search", params)


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if not args:
        print(json.dumps({"error": "No command provided"}))
        return
    command = args[0]
    result = {"error": f"Unknown command: {command}"}
    if command == "area":
        lat1 = float(args[1]) if len(args) > 1 else 51.0
        lon1 = float(args[2]) if len(args) > 2 else -1.0
        lat2 = float(args[3]) if len(args) > 3 else 52.0
        lon2 = float(args[4]) if len(args) > 4 else 1.0
        result = get_vessels_in_area(lat1, lon1, lat2, lon2)
    elif command == "vessel":
        mmsi = args[1] if len(args) > 1 else "123456789"
        result = get_vessel_by_mmsi(mmsi)
    elif command == "track":
        mmsi = args[1] if len(args) > 1 else "123456789"
        start_date = args[2] if len(args) > 2 else None
        end_date = args[3] if len(args) > 3 else None
        result = get_vessel_track(mmsi, start_date, end_date)
    elif command == "port_calls":
        port_name = args[1] if len(args) > 1 else None
        start_date = args[2] if len(args) > 2 else None
        end_date = args[3] if len(args) > 3 else None
        result = get_port_calls(port_name, start_date, end_date)
    elif command == "fleet":
        vessel_type = args[1] if len(args) > 1 else None
        limit = int(args[2]) if len(args) > 2 else 50
        result = get_fleet(vessel_type, limit)
    elif command == "search":
        name = args[1] if len(args) > 1 else "MSC"
        result = search_vessel(name)
    print(json.dumps(result))


if __name__ == "__main__":
    main()
```

### fincept-qt/scripts/akshare_data.py

```python
"""
AKShare Data Wrapper - COMPREHENSIVE VERSION
Most comprehensive Chinese financial data API with 1,200+ endpoints
Returns JSON output for Qt/C++ integration
Modular, fault-tolerant design with specialized wrappers
All endpoints are FREE - no API keys required

Coverage: 95%+ of available AKShare endpoints across all data categories
"""

import sys
import json
import pandas as pd
import akshare as ak
from typing import Dict, Any, List, Optional, Union
from datetime import datetime, timedelta, date
import traceback

# Custom JSON encoder for date objects
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return super().default(obj)

# Import specialized wrappers
try:
    from akshare_analysis import StockAnalysisWrapper
except ImportError:
    StockAnalysisWrapper = None

try:
    from akshare_economics_china import ChinaEconomicsWrapper
except ImportError:
    ChinaEconomicsWrapper = None

try:
    from akshare_economics_global import GlobalEconomicsWrapper
except ImportError:
    GlobalEconomicsWrapper = None

try:
    from akshare_derivatives import DerivativesWrapper
except ImportError:
    DerivativesWrapper = None

try:
    from akshare_bonds import BondsWrapper
except ImportError:
    BondsWrapper = None

try:
    from akshare_alternative import AlternativeDataWrapper
except ImportError:
    AlternativeDataWrapper = None

try:
    from akshare_funds_expanded import ExpandedFundsWrapper
except ImportError:
    ExpandedFundsWrapper = None


class AKShareError:
    """Custom error class for AKShare API errors"""
    def __init__(self, endpoint: str, error: str, data_source: Optional[str] = None):
        self.endpoint = endpoint
        self.error = error
        self.data_source = data_source
        self.timestamp = int(datetime.now().timestamp())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "endpoint": self.endpoint,
            "error": self.error,
            "data_source": self.data_source,
            "timestamp": self.timestamp,
            "type": "AKShareError"
        }


class AKShareDataWrapper:
    """Comprehensive AKShare data wrapper - Main orchestrator for all specialized modules"""

    def __init__(self):
        self.session = None
        self.default_timeout = 30

        # Common date parameters
        self.default_start_date = (datetime.now() - timedelta(days=365)).strftime('%Y%m%d')
        self.default_end_date = datetime.now().strftime('%Y%m%d')

        # Initialize specialized wrappers
        self.analysis = StockAnalysisWrapper() if StockAnalysisWrapper else None
        self.economics_china = ChinaEconomicsWrapper() if ChinaEconomicsWrapper else None
        self.economics_global = GlobalEconomicsWrapper() if GlobalEconomicsWrapper else None
        self.derivatives = DerivativesWrapper() if DerivativesWrapper else None
        self.bonds = BondsWrapper() if BondsWrapper else None
        self.alternative = AlternativeDataWrapper() if AlternativeDataWrapper else None
        self.funds_expanded = ExpandedFundsWrapper() if ExpandedFundsWrapper else None

        # Track available modules
        self.available_modules = {
            "Stock Analysis": self.analysis is not None,
            "China Economics": self.economics_china is not None,
            "Global Economics": self.economics_global is not None,
            "Derivatives": self.derivatives is not None,
            "Bonds": self.bonds is not None,
            "Alternative Data": self.alternative is not None,
            "Expanded Funds": self.funds_expanded is not None
        }

    def _safe_call(self, func, *args, **kwargs) -> Dict[str, Any]:
        """Safely call AKShare function with error handling"""
        try:
            result = func(*args, **kwargs)
            if result is not None and not result.empty:
                # Convert date/datetime columns to strings for JSON serialization
                df_copy = result.copy()
                for col in df_copy.columns:
                    if pd.api.types.is_datetime64_any_dtype(df_copy[col]):
                        df_copy[col] = df_copy[col].astype(str)
                return {
                    "success": True,
                    "data": df_copy.to_dict('records'),
                    "count": len(result),
                    "timestamp": int(datetime.now().timestamp())
                }
            else:
                return {
                    "success": False,
                    "error": "No data returned",
                    "data": [],
                    "count": 0,
                    "timestamp": int(datetime.now().timestamp())
                }
        except Exception as e:
            error_obj = AKShareError(
                endpoint=func.__name__,
                error=str(e),
                data_source=getattr(func, '__module__', 'unknown')
            )
            return {
                "success": False,
                "error": error_obj.to_dict(),
                "data": [],
                "count": 0,
                "timestamp": int(datetime.now().timestamp())
            }

    # ==================== STOCK MARKET DATA ====================

    def get_stock_zh_a_spot(self) -> Dict[str, Any]:
        """Get all Chinese A-shares real-time quotes"""
        return self._safe_call(ak.stock_zh_a_spot_em)

    def get_stock_zh_a_daily(self, symbol: str, start_date: str = None, end_date: str = None, adjust: str = "") -> Dict[str, Any]:
        """Get Chinese A-share historical daily data

        Args:
            symbol: Stock symbol (e.g., "sh600000", "sz000001")
            start_date: Start date in YYYYMMDD format
            end_date: End date in YYYYMMDD format
            adjust: Adjustment type ("", "qfq", "hfq")
        """
        start = start_date or self.default_start_date
        end = end_date or self.default_end_date
        return self._safe_call(ak.stock_zh_a_hist_em, symbol=symbol, period="daily", start_date=start, end_date=end, adjust=adjust)

    def get_stock_us_spot(self) -> Dict[str, Any]:
        """Get all US stocks real-time quotes (15-min delayed)"""
        return self._safe_call(ak.stock_us_spot)

    def get_stock_us_daily(self, symbol: str, start_date: str = None, end_date: str = None, adjust: str = "") -> Dict[str, Any]:
        """Get US stock historical daily data

        Args:
            symbol: US stock symbol (e.g., "AAPL", ".DJI")
            start_date: Start date in YYYYMMDD format
            end_date: End date in YYYYMMDD format
            adjust: Adjustment type ("", "qfq", "hfq")

# ... 文件较长，已截断。总行数：484
```

### fincept-qt/scripts/alpha_spread_data.py

```python
"""
AlphaSpread Data Fetcher
Intrinsic value, DCF, comparable company analysis for stocks — free tier.
"""
import sys
import json
import os
import requests
from typing import Dict, Any, Optional, List

API_KEY = os.environ.get('ALPHA_SPREAD_API_KEY', '')
BASE_URL = "https://alphaspread.com/api"

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=3)
session.mount('https://', adapter)
session.mount('http://', adapter)

def _make_request(endpoint: str, params: Dict = None) -> Any:
    url = f"{BASE_URL}/{endpoint}" if not endpoint.startswith('http') else endpoint
    try:
        headers = {"Authorization": f"Bearer {API_KEY}"}
        response = session.get(url, params=params, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except (json.JSONDecodeError, ValueError) as e:
        return {"error": f"JSON decode error: {str(e)}"}

def get_valuation(ticker: str) -> Any:
    return _make_request(f"v1/equity/{ticker}/valuation", {})

def get_dcf(ticker: str) -> Any:
    return _make_request(f"v1/equity/{ticker}/dcf", {})

def get_comparables(ticker: str) -> Any:
    return _make_request(f"v1/equity/{ticker}/comparables", {})

def get_watchlist_data(tickers: List[str]) -> Any:
    return _make_request("v1/equity/batch", {"tickers": ",".join(tickers)})

def get_score(ticker: str) -> Any:
    return _make_request(f"v1/equity/{ticker}/score", {})

def get_intrinsic_value_history(ticker: str) -> Any:
    return _make_request(f"v1/equity/{ticker}/intrinsic-value/history", {})

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if not args:
        print(json.dumps({"error": "No command provided"}))
        return
    command = args[0]
    result = {"error": f"Unknown command: {command}"}
    if command == "valuation":
        ticker = args[1] if len(args) > 1 else "AAPL"
        result = get_valuation(ticker)
    elif command == "dcf":
        ticker = args[1] if len(args) > 1 else "AAPL"
        result = get_dcf(ticker)
    elif command == "comparables":
        ticker = args[1] if len(args) > 1 else "AAPL"
        result = get_comparables(ticker)
    elif command == "watchlist":
        tickers = args[1].split(",") if len(args) > 1 else ["AAPL", "MSFT"]
        result = get_watchlist_data(tickers)
    elif command == "score":
        ticker = args[1] if len(args) > 1 else "AAPL"
        result = get_score(ticker)
    elif command == "history":
        ticker = args[1] if len(args) > 1 else "AAPL"
        result = get_intrinsic_value_history(ticker)
    print(json.dumps(result))

if __name__ == "__main__":
    main()
```

### fincept-qt/scripts/alpha_vantage_extra_data.py

```python
"""
Alpha Vantage Extended Data Fetcher
Forex, crypto, commodities, economic indicators, sector performance.
"""
import sys
import json
import os
import requests
from typing import Dict, Any, Optional, List

API_KEY = os.environ.get('ALPHA_VANTAGE_API_KEY', '')
BASE_URL = "https://www.alphavantage.co/query"

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=3)
session.mount('https://', adapter)
session.mount('http://', adapter)

def _make_request(endpoint: str, params: Dict = None) -> Any:
    url = f"{BASE_URL}/{endpoint}" if not endpoint.startswith('http') else endpoint
    try:
        response = session.get(url, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except (json.JSONDecodeError, ValueError) as e:
        return {"error": f"JSON decode error: {str(e)}"}

def get_forex_daily(from_symbol: str, to_symbol: str, outputsize: str = "compact") -> Any:
    params = {"function": "FX_DAILY", "from_symbol": from_symbol, "to_symbol": to_symbol, "outputsize": outputsize, "apikey": API_KEY}
    return _make_request(BASE_URL, params)

def get_crypto_daily(symbol: str, market: str = "USD") -> Any:
    params = {"function": "DIGITAL_CURRENCY_DAILY", "symbol": symbol, "market": market, "apikey": API_KEY}
    return _make_request(BASE_URL, params)

def get_commodity_daily(commodity: str = "WTI") -> Any:
    params = {"function": commodity, "interval": "monthly", "apikey": API_KEY}
    return _make_request(BASE_URL, params)

def get_sector_performance() -> Any:
    params = {"function": "SECTOR", "apikey": API_KEY}
    return _make_request(BASE_URL, params)

def get_economic_indicator(function: str = "REAL_GDP", interval: str = "annual") -> Any:
    params = {"function": function, "interval": interval, "apikey": API_KEY}
    return _make_request(BASE_URL, params)

def get_earnings_calendar(symbol: str = None, horizon: str = "3month") -> Any:
    params = {"function": "EARNINGS_CALENDAR", "horizon": horizon, "apikey": API_KEY}
    if symbol:
        params["symbol"] = symbol
    return _make_request(BASE_URL, params)

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if not args:
        print(json.dumps({"error": "No command provided"}))
        return
    command = args[0]
    result = {"error": f"Unknown command: {command}"}
    if command == "forex":
        from_symbol = args[1] if len(args) > 1 else "EUR"
        to_symbol = args[2] if len(args) > 2 else "USD"
        outputsize = args[3] if len(args) > 3 else "compact"
        result = get_forex_daily(from_symbol, to_symbol, outputsize)
    elif command == "crypto":
        symbol = args[1] if len(args) > 1 else "BTC"
        market = args[2] if len(args) > 2 else "USD"
        result = get_crypto_daily(symbol, market)
    elif command == "commodity":
        commodity = args[1] if len(args) > 1 else "WTI"
        result = get_commodity_daily(commodity)
    elif command == "sectors":
        result = get_sector_performance()
    elif command == "economic":
        function = args[1] if len(args) > 1 else "REAL_GDP"
        interval = args[2] if len(args) > 2 else "annual"
        result = get_economic_indicator(function, interval)
    elif command == "earnings":
        symbol = args[1] if len(args) > 1 else None
        horizon = args[2] if len(args) > 2 else "3month"
        result = get_earnings_calendar(symbol, horizon)
    print(json.dumps(result))

if __name__ == "__main__":
    main()
```

### fincept-qt/scripts/alphavantage_data.py

```python
"""
Alpha Vantage Data Fetcher
Fetches stock quotes and data from Alpha Vantage API
Returns JSON output for Qt/C++ integration
"""

import sys
import json
import os
import requests
from typing import Dict, Any

# API Configuration
API_KEY = os.environ.get('', '')
BASE_URL = "https://www.alphavantage.co/query"


def get_quote(symbol: str) -> Dict[str, Any]:
    """Fetch real-time quote for a stock symbol"""
    try:
        if not API_KEY:
            return {"error": "Alpha Vantage API key not configured"}

        params = {
            'function': 'GLOBAL_QUOTE',
            'symbol': symbol,
            'apikey': API_KEY
        }

        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        if 'Global Quote' not in data:
            return {"error": "No data returned for symbol", "symbol": symbol}

        quote = data['Global Quote']

        result = {
            "symbol": symbol,
            "price": float(quote.get('05. price', 0)),
            "change": float(quote.get('09. change', 0)),
            "change_percent": quote.get('10. change percent', '0'),
            "volume": int(quote.get('06. volume', 0)),
            "open": float(quote.get('02. open', 0)),
            "high": float(quote.get('03. high', 0)),
            "low": float(quote.get('04. low', 0)),
            "previous_close": float(quote.get('08. previous close', 0)),
            "trading_day": quote.get('07. latest trading day', '')
        }

        return result

    except requests.exceptions.RequestException as e:
        return {"error": f"Network error: {str(e)}", "symbol": symbol}
    except Exception as e:
        return {"error": str(e), "symbol": symbol}


def main(args=None):
    
    if args is None:
        args = sys.argv[1:]
    """Main CLI entry point"""
    if len(args) + 1 < 3:
        print(json.dumps({
            "error": "Usage: python alphavantage_data.py quote <symbol>"
        }))
        sys.exit(1)

    command = args[0]
    symbol = args[1]

    if command == "quote":
        result = get_quote(symbol)
        print(json.dumps(result, indent=2))
    else:
        print(json.dumps({"error": f"Unknown command: {command}"}))
        sys.exit(1)


if __name__ == "__main__":
    main()
```

### fincept-qt/scripts/alternative_me_data.py

```python
"""
Alternative.me Data Fetcher
Alternative.me: Fear & Greed Index, crypto fear gauge,
global market sentiment (no API key required).
"""
import sys
import json
import os
import requests
from typing import Dict, Any, Optional, List

BASE_URL = "https://api.alternative.me"

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=3)
session.mount('https://', adapter)
session.mount('http://', adapter)


def _make_request(endpoint: str, params: Dict = None) -> Any:
    url = f"{BASE_URL}/{endpoint}" if not endpoint.startswith('http') else endpoint
    try:
        response = session.get(url, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except (json.JSONDecodeError, ValueError) as e:
        return {"error": f"JSON decode error: {str(e)}"}


def get_fear_greed_index(limit: int = 10, date_format: str = "us") -> Any:
    params = {"limit": limit, "date_format": date_format}
    data = _make_request("fng/", params)
    if isinstance(data, dict) and "data" in data:
        result = data["data"]
        for item in result:
            val = int(item.get("value", 0))
            if val <= 24:
                item["sentiment"] = "Extreme Fear"
            elif val <= 44:
                item["sentiment"] = "Fear"
            elif val <= 55:
                item["sentiment"] = "Neutral"
            elif val <= 75:
                item["sentiment"] = "Greed"
            else:
                item["sentiment"] = "Extreme Greed"
        return {"count": len(result), "index": "Fear & Greed", "data": result}
    return data


def get_crypto_fear_greed(limit: int = 30) -> Any:
    params = {"limit": limit}
    data = _make_request("fng/", params)
    if isinstance(data, dict) and "data" in data:
        items = data["data"]
        values = [int(i.get("value", 0)) for i in items if i.get("value")]
        avg = sum(values) / len(values) if values else 0
        return {
            "current": items[0] if items else {},
            "30_day_average": round(avg, 1),
            "history": items,
            "metadata": data.get("metadata", {})
        }
    return data


def get_global_crypto_data() -> Any:
    return _make_request("v2/global/")


def get_portfolio_return(symbols: str = "BTC,ETH", amount: float = 1000.0,
                          currency: str = "USD") -> Any:
    syms = [s.strip() for s in symbols.split(',')]
    results = {}
    for sym in syms:
        data = _make_request(f"v2/ticker/{sym}/", {"convert": currency})
        if isinstance(data, dict) and not data.get("error"):
            results[sym] = data
    return {
        "symbols": syms,
        "amount": amount,
        "currency": currency,
        "prices": results
    }


def get_currencies() -> Any:
    data = _make_request("v2/listings/", {"start": 1, "limit": 100})
    return data


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if not args:
        print(json.dumps({"error": "No command provided"}))
        return
    command = args[0]
    result = {"error": f"Unknown command: {command}"}
    if command == "fear_greed":
        limit = int(args[1]) if len(args) > 1 else 10
        date_format = args[2] if len(args) > 2 else "us"
        result = get_fear_greed_index(limit, date_format)
    elif command == "crypto_fear":
        limit = int(args[1]) if len(args) > 1 else 30
        result = get_crypto_fear_greed(limit)
    elif command == "global":
        result = get_global_crypto_data()
    elif command == "portfolio":
        symbols = args[1] if len(args) > 1 else "BTC,ETH"
        amount = float(args[2]) if len(args) > 2 else 1000.0
        currency = args[3] if len(args) > 3 else "USD"
        result = get_portfolio_return(symbols, amount, currency)
    elif command == "currencies":
        result = get_currencies()
    print(json.dumps(result))


if __name__ == "__main__":
    main()
```

### fincept-qt/scripts/arxiv_data.py

```python
"""
ArXiv Data Fetcher
Fetches research papers in finance, economics, machine learning, and quantitative finance
from the ArXiv API — full metadata and abstracts.
"""
import sys
import json
import os
import requests
import xml.etree.ElementTree as ET
from typing import Dict, Any, Optional, List

API_KEY = os.environ.get('ARXIV_API_KEY', '')
BASE_URL = "http://export.arxiv.org/api"

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=3)
session.mount('https://', adapter)
session.mount('http://', adapter)

ARXIV_NS = "http://www.w3.org/2005/Atom"
OPENSEARCH_NS = "http://a9.com/-/spec/opensearch/1.1/"

QUANT_FINANCE_SUBCATEGORIES = {
    "portfolio": "q-fin.PM",
    "risk": "q-fin.RM",
    "pricing": "q-fin.PR",
    "trading": "q-fin.TR",
    "computational": "q-fin.CP",
    "economics": "q-fin.EC",
    "general_finance": "q-fin.GN",
    "statistics": "q-fin.ST",
    "mathematical_finance": "q-fin.MF",
}

ML_SUBCATEGORIES = {
    "learning": "cs.LG",
    "ai": "cs.AI",
    "neural_networks": "cs.NE",
    "cv": "cs.CV",
    "nlp": "cs.CL",
    "stats_ml": "stat.ML",
}


def _parse_atom_entry(entry) -> Dict:
    ns = ARXIV_NS
    arxiv_ns = "http://arxiv.org/schemas/atom"

    def tag(name, namespace=ns):
        return f"{{{namespace}}}{name}"

    paper = {}
    id_elem = entry.find(tag("id"))
    if id_elem is not None:
        full_id = id_elem.text.strip()
        paper["arxiv_id"] = full_id.split("/abs/")[-1]
        paper["url"] = full_id
    title_elem = entry.find(tag("title"))
    if title_elem is not None:
        paper["title"] = " ".join(title_elem.text.strip().split())
    summary_elem = entry.find(tag("summary"))
    if summary_elem is not None:
        paper["abstract"] = " ".join(summary_elem.text.strip().split())
    published_elem = entry.find(tag("published"))
    if published_elem is not None:
        paper["published"] = published_elem.text.strip()
    updated_elem = entry.find(tag("updated"))
    if updated_elem is not None:
        paper["updated"] = updated_elem.text.strip()
    authors = []
    for author_elem in entry.findall(tag("author")):
        name_elem = author_elem.find(tag("name"))
        if name_elem is not None:
            authors.append(name_elem.text.strip())
    paper["authors"] = authors
    categories = []
    for cat_elem in entry.findall(tag("category")):
        term = cat_elem.get("term", "")
        if term:
            categories.append(term)
    paper["categories"] = categories
    primary_elem = entry.find(f"{{{arxiv_ns}}}primary_category")
    if primary_elem is not None:
        paper["primary_category"] = primary_elem.get("term", "")
    doi_elem = entry.find(f"{{{arxiv_ns}}}doi")
    if doi_elem is not None:
        paper["doi"] = doi_elem.text.strip()
    comment_elem = entry.find(f"{{{arxiv_ns}}}comment")
    if comment_elem is not None:
        paper["comment"] = comment_elem.text.strip()
    for link_elem in entry.findall(tag("link")):
        if link_elem.get("type") == "application/pdf":
            paper["pdf_url"] = link_elem.get("href", "")
    return paper


def _make_request(endpoint: str, params: Dict = None) -> Any:
    url = f"{BASE_URL}/{endpoint}" if not endpoint.startswith('http') else endpoint
    try:
        response = session.get(url, params=params, timeout=30)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


def _parse_atom_response(xml_text: str) -> Dict:
    if isinstance(xml_text, dict):
        return xml_text
    try:
        root = ET.fromstring(xml_text)
        ns = ARXIV_NS
        opensearch_ns = OPENSEARCH_NS

        def tag(name, namespace=ns):
            return f"{{{namespace}}}{name}"

        total_elem = root.find(f"{{{opensearch_ns}}}totalResults")
        total = int(total_elem.text) if total_elem is not None else 0
        start_elem = root.find(f"{{{opensearch_ns}}}startIndex")
        start = int(start_elem.text) if start_elem is not None else 0
        per_page_elem = root.find(f"{{{opensearch_ns}}}itemsPerPage")
        per_page = int(per_page_elem.text) if per_page_elem is not None else 0
        papers = []
        for entry in root.findall(tag("entry")):
            papers.append(_parse_atom_entry(entry))
        return {
            "total_results": total,
            "start_index": start,
            "items_per_page": per_page,
            "papers": papers,
        }
    except ET.ParseError as e:
        return {"error": f"XML parse error: {str(e)}"}


def search_papers(query: str, category: str = "", max_results: int = 10, start: int = 0) -> Dict:
    search_query = query
    if category:
        search_query = f"({query}) AND cat:{category}"
    params = {
        "search_query": f"all:{search_query}",
        "start": start,
        "max_results": max_results,
        "sortBy": "relevance",
        "sortOrder": "descending",
    }
    raw = _make_request("query", params)
    return _parse_atom_response(raw)


def get_paper(arxiv_id: str) -> Dict:
    params = {"id_list": arxiv_id}
    raw = _make_request("query", params)
    result = _parse_atom_response(raw)
    if "papers" in result and result["papers"]:
        return result["papers"][0]
    return {"error": f"Paper not found: {arxiv_id}"}


def get_recent_papers(category: str = "q-fin", max_results: int = 20) -> Dict:
    params = {
        "search_query": f"cat:{category}",
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    raw = _make_request("query", params)
    return _parse_atom_response(raw)


def get_quant_finance_papers(subcategory: str = "", max_results: int = 20) -> Dict:
    if subcategory and subcategory in QUANT_FINANCE_SUBCATEGORIES:
        cat = QUANT_FINANCE_SUBCATEGORIES[subcategory]
    elif subcategory and subcategory.startswith("q-fin"):
        cat = subcategory

# ... 文件较长，已截断。总行数：275
```

### fincept-qt/scripts/baostock_data.py

```python
#!/usr/bin/env python3
"""
BaoStock Data Wrapper
Provides a CLI-style endpoint interface with JSON output for Fincept Terminal.
"""

import io
import json
import sys
import time
from datetime import datetime
from typing import Any, Dict, List

try:
    import baostock as bs
    import pandas as pd
except ImportError as e:
    print(
        json.dumps(
            {
                "success": False,
                "error": f"Missing dependency: {e}",
                "data": [],
            },
            ensure_ascii=True,
        )
    )
    sys.exit(1)


def _now_ts() -> int:
    return int(datetime.now().timestamp())


class BaoStockWrapper:
    """BaoStock endpoint wrapper with safe execution and retries."""

    def __init__(self) -> None:
        self._logged_in = False

    def _login(self) -> None:
        if self._logged_in:
            return
        lg = bs.login()
        if lg.error_code != "0":
            raise RuntimeError(f"BaoStock login failed: {lg.error_msg}")
        self._logged_in = True

    def _logout(self) -> None:
        if self._logged_in:
            try:
                bs.logout()
            finally:
                self._logged_in = False

    def _normalize_df(self, df: pd.DataFrame) -> List[Dict[str, Any]]:
        if df.empty:
            return []
        for col in df.columns:
            if pd.api.types.is_datetime64_any_dtype(df[col]):
                df[col] = df[col].astype(str)
        df = df.replace([float("inf"), float("-inf")], None)
        df = df.where(pd.notna(df), None)
        return df.to_dict(orient="records")

    def _query_to_df(self, rs) -> pd.DataFrame:
        if rs.error_code != "0":
            raise RuntimeError(rs.error_msg)
        rows: List[List[str]] = []
        while rs.next():
            rows.append(rs.get_row_data())
        return pd.DataFrame(rows, columns=rs.fields)

    def _safe_call(self, func, *args, **kwargs) -> Dict[str, Any]:
        max_retries = 2
        for attempt in range(max_retries):
            try:
                self._login()
                result = func(*args, **kwargs)
                if isinstance(result, pd.DataFrame):
                    data = self._normalize_df(result)
                    return {
                        "success": True,
                        "data": data,
                        "count": len(data),
                        "timestamp": _now_ts(),
                    }
                if isinstance(result, (list, dict)):
                    count = len(result) if isinstance(result, list) else 1
                    return {
                        "success": True,
                        "data": result,
                        "count": count,
                        "timestamp": _now_ts(),
                    }
                return {
                    "success": True,
                    "data": str(result),
                    "count": 1,
                    "timestamp": _now_ts(),
                }
            except Exception as e:  # pragma: no cover - defensive
                if attempt < max_retries - 1:
                    self._logout()
                    time.sleep(1)
                    continue
                return {
                    "success": False,
                    "error": str(e),
                    "data": [],
                    "timestamp": _now_ts(),
                }
        return {
            "success": False,
            "error": "Max retries exceeded",
            "data": [],
            "timestamp": _now_ts(),
        }

    def _query_safe(self, query_func, *args, **kwargs) -> Dict[str, Any]:
        def _inner():
            rs = query_func(*args, **kwargs)
            return self._query_to_df(rs)

        return self._safe_call(_inner)

    # -------- Endpoints --------

    def get_stock_basic(self, code: str = "", code_name: str = "") -> Dict[str, Any]:
        return self._query_safe(bs.query_stock_basic, code=code, code_name=code_name)

    def get_trade_dates(
        self, start_date: str = "2024-01-01", end_date: str = "2024-12-31"
    ) -> Dict[str, Any]:
        return self._query_safe(
            bs.query_trade_dates, start_date=start_date, end_date=end_date
        )

    def get_hs300_stocks(self, date: str = "") -> Dict[str, Any]:
        return self._query_safe(bs.query_hs300_stocks, date=date)

    def get_sz50_stocks(self, date: str = "") -> Dict[str, Any]:
        return self._query_safe(bs.query_sz50_stocks, date=date)

    def get_zz500_stocks(self, date: str = "") -> Dict[str, Any]:
        return self._query_safe(bs.query_zz500_stocks, date=date)

    def get_all_stock(self, day: str = "") -> Dict[str, Any]:
        return self._query_safe(bs.query_all_stock, day=day or None)

    def get_stock_industry(self, date: str = "") -> Dict[str, Any]:
        return self._query_safe(bs.query_stock_industry, code="", date=date)

    def get_stock_profit_data(
        self, code: str, year: str = "2024", quarter: str = "4"
    ) -> Dict[str, Any]:
        return self._query_safe(
            bs.query_profit_data, code=code, year=year, quarter=quarter
        )

    def get_stock_growth_data(
        self, code: str, year: str = "2024", quarter: str = "4"
    ) -> Dict[str, Any]:
        return self._query_safe(
            bs.query_growth_data, code=code, year=year, quarter=quarter
        )

    def get_stock_balance_data(
        self, code: str, year: str = "2024", quarter: str = "4"
    ) -> Dict[str, Any]:
        return self._query_safe(
            bs.query_balance_data, code=code, year=year, quarter=quarter
        )

    def get_stock_cash_flow_data(
        self, code: str, year: str = "2024", quarter: str = "4"
    ) -> Dict[str, Any]:
        return self._query_safe(
            bs.query_cash_flow_data, code=code, year=year, quarter=quarter
        )

# ... 文件较长，已截断。总行数：408
```

### fincept-qt/scripts/bcb_data.py

```python
"""
Banco Central do Brasil (BCB) Data Wrapper
Fetches data from the BCB SGS (Sistema Gerenciador de Series Temporais) API.

API Reference:
  Base URL:  https://api.bcb.gov.br/dados/serie/bcdata.sgs.{series_id}/dados
  Format:    JSON array [{data: "DD/MM/YYYY", valor: "N.NN"}, ...]
  Auth:      None required — fully public

Endpoint patterns:
  All data:       GET /dados/serie/bcdata.sgs.{id}/dados?formato=json
  Date range:     GET /dados/serie/bcdata.sgs.{id}/dados?formato=json&dataInicial=DD/MM/YYYY&dataFinal=DD/MM/YYYY
  Last N:         GET /dados/serie/bcdata.sgs.{id}/dados/ultimos/{n}?formato=json
  Multiple SGS:   GET /dados/conjuntos/dados?codigoseries={id1},{id2}&formato=json

Key series IDs (verified):
  432   — Selic target rate (% per year)
  11    — Selic daily rate
  433   — IPCA monthly inflation (%)
  189   — IGP-M monthly inflation (%)
  1     — USD/BRL exchange rate (PTAX selling)
  21619 — EUR/BRL exchange rate
  4192  — EUR/BRL (older series)
  7326  — GDP annual growth rate (%)
  27791 — M1 (currency + demand deposits, R$ thousands)
  28000 — M2 monetary aggregate
  29037 — M3 monetary aggregate
  24369 — Unemployment rate (PNAD) %
  20539 — Total credit outstanding (R$ millions)
  13621 — International reserves (USD millions)
  4189  — Primary fiscal surplus/deficit (R$ millions)
  7478  — Net public debt (% GDP)
  4390  — Trade balance (USD millions, monthly)
  22707 — Current account (USD millions)
  3541  — TJLP (long-term interest rate)
  226   — TR (referential rate)
  1178  — CDB 1-day rate
  7809  — Bovespa index (monthly avg)

Returns JSON output for C++ integration.
"""

import sys
import json
import requests
import traceback
from typing import Dict, Any, List, Optional
from datetime import datetime, timezone


BASE_URL        = "https://api.bcb.gov.br/dados/serie/bcdata.sgs"
MULTI_URL       = "https://api.bcb.gov.br/dados/conjuntos/dados"
DEFAULT_TIMEOUT = 30

# ---------------------------------------------------------------------------
# Series catalogue
# ---------------------------------------------------------------------------

SERIES = {
    # Monetary policy
    "selic_target":      {"id": 432,   "name": "Selic Target Rate",            "category": "monetary_policy", "unit": "% p.a.",      "freq": "daily"},
    "selic_daily":       {"id": 11,    "name": "Selic Daily Rate",              "category": "monetary_policy", "unit": "% p.a.",      "freq": "daily"},
    "tjlp":              {"id": 3541,  "name": "TJLP Long-Term Rate",           "category": "monetary_policy", "unit": "% p.a.",      "freq": "monthly"},
    "tr":                {"id": 226,   "name": "TR Referential Rate",           "category": "monetary_policy", "unit": "%",           "freq": "monthly"},
    # Inflation
    "ipca":              {"id": 433,   "name": "IPCA Monthly Inflation",        "category": "inflation",       "unit": "%",           "freq": "monthly"},
    "igpm":              {"id": 189,   "name": "IGP-M Monthly Inflation",       "category": "inflation",       "unit": "%",           "freq": "monthly"},
    # Exchange rates
    "usd_brl":           {"id": 1,     "name": "USD/BRL PTAX (selling)",        "category": "exchange_rates",  "unit": "BRL per USD", "freq": "daily"},
    "eur_brl":           {"id": 21619, "name": "EUR/BRL PTAX (selling)",        "category": "exchange_rates",  "unit": "BRL per EUR", "freq": "daily"},
    # Monetary aggregates
    "m1":                {"id": 27791, "name": "M1 Monetary Aggregate",         "category": "monetary",        "unit": "R$ thousands","freq": "monthly"},
    "m2":                {"id": 28000, "name": "M2 Monetary Aggregate",         "category": "monetary",        "unit": "R$ thousands","freq": "monthly"},
    "m3":                {"id": 29037, "name": "M3 Monetary Aggregate",         "category": "monetary",        "unit": "R$ thousands","freq": "monthly"},
    # GDP / real economy
    "gdp_growth":        {"id": 7326,  "name": "GDP Annual Growth Rate",        "category": "gdp",             "unit": "%",           "freq": "annual"},
    "unemployment":      {"id": 24369, "name": "Unemployment Rate (PNAD)",      "category": "labour",          "unit": "%",           "freq": "monthly"},
    # Credit
    "credit_total":      {"id": 20539, "name": "Total Credit Outstanding",      "category": "credit",          "unit": "R$ millions", "freq": "monthly"},
    # External sector
    "reserves":          {"id": 13621, "name": "International Reserves",        "category": "external",        "unit": "USD millions","freq": "daily"},
    "trade_balance":     {"id": 4390,  "name": "Trade Balance (monthly)",       "category": "external",        "unit": "USD millions","freq": "monthly"},
    "current_account":   {"id": 22707, "name": "Current Account Balance",       "category": "external",        "unit": "USD millions","freq": "monthly"},
    # Fiscal
    "primary_surplus":   {"id": 4189,  "name": "Primary Fiscal Surplus/Deficit","category": "fiscal",          "unit": "R$ millions", "freq": "monthly"},
    "net_public_debt":   {"id": 7478,  "name": "Net Public Debt (% GDP)",       "category": "fiscal",          "unit": "% GDP",       "freq": "monthly"},
    # Capital markets
    "bovespa":           {"id": 7809,  "name": "Bovespa Index Monthly Avg",     "category": "markets",         "unit": "index",       "freq": "monthly"},
    "cdb_1d":            {"id": 1178,  "name": "CDB 1-Day Rate",                "category": "interest_rates",  "unit": "% p.a.",      "freq": "daily"},
}

# Convenience groups
GROUPS = {
    "monetary_policy": ["selic_target", "selic_daily", "tjlp"],
    "inflation":       ["ipca", "igpm"],
    "exchange_rates":  ["usd_brl", "eur_brl"],
    "monetary":        ["m1", "m2", "m3"],
    "external":        ["reserves", "trade_balance", "current_account"],
    "fiscal":          ["primary_surplus", "net_public_debt"],
    "overview":        ["selic_target", "ipca", "usd_brl", "gdp_growth", "unemployment", "reserves"],
}


# ---------------------------------------------------------------------------
# Error container
# ---------------------------------------------------------------------------

class BCBError:
    def __init__(self, endpoint: str, error: str, status_code: Optional[int] = None):
        self.endpoint    = endpoint
        self.error       = error
        self.status_code = status_code
        self.timestamp   = int(datetime.now(timezone.utc).timestamp())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "success":     False,
            "endpoint":    self.endpoint,
            "error":       self.error,
            "status_code": self.status_code,
            "timestamp":   self.timestamp,
            "type":        "BCBError",
        }


# ---------------------------------------------------------------------------
# Main wrapper
# ---------------------------------------------------------------------------

class BCBWrapper:
    """
    Wrapper for Banco Central do Brasil SGS (Time Series Management System).

    The BCB SGS API returns JSON arrays: [{data: "DD/MM/YYYY", valor: "N.NN"}]
    All series are accessible without authentication.
    """

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Fincept-Terminal/4.0.2",
            "Accept":     "*/*",
        })

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _fetch_series(self, series_id: int, start_date: Optional[str] = None,
                      end_date: Optional[str] = None,
                      last_n: Optional[int] = None) -> List[Dict]:
        """
        Fetch a single SGS series.
        start_date/end_date: "DD/MM/YYYY" format
        last_n: fetch only last N observations
        """
        if last_n:
            url = f"{BASE_URL}.{series_id}/dados/ultimos/{last_n}"
        else:
            url = f"{BASE_URL}.{series_id}/dados"

        params: Dict[str, str] = {"formato": "json"}
        if start_date and not last_n:
            params["dataInicial"] = start_date
        if end_date and not last_n:
            params["dataFinal"] = end_date

        resp = self.session.get(url, params=params, timeout=DEFAULT_TIMEOUT)
        resp.raise_for_status()
        return resp.json()

    def _parse_rows(self, raw: List[Dict], series_name: str) -> List[Dict]:
        rows = []
        for item in raw:
            date_str = item.get("data", "")
            val_str  = item.get("valor", "")
            val      = None
            if val_str not in ("", None):
                try:
                    val = float(str(val_str).replace(",", "."))

# ... 文件较长，已截断。总行数：504
```

### fincept-qt/scripts/bea_data.py

```python
"""
BEA (Bureau of Economic Analysis) Data Fetcher
Comprehensive wrapper for BEA Data Retrieval API providing access to
National, Regional, Industry and International economic data

API Documentation:
- Base URL: https://apps.bea.gov/api/data/
- Authentication: API key required
- Rate limits: None specified but be reasonable with requests
- Registration: https://www.bea.gov/data/api/register

Supported Datasets:
- NIPA: National Income and Product Accounts
- NIUnderlyingDetail: NIPA Underlying Detail
- FixedAssets: Fixed Assets
- MNE: Multinational Enterprises
- GDPbyIndustry: GDP by Industry
- ITA: International Transactions
- IIP: International Investment Position
- InputOutput: Input-Output Accounts
- UnderlyingGDPbyIndustry: GDP by Industry - Underlying Detail
- IntlServTrade: International Services Trade
- Regional: Regional Economic Accounts
"""

import sys
import json
import os
import requests
from datetime import datetime, timedelta
from typing import Dict, Any, Optional, List, Union
from urllib.parse import urlencode


class BEAError:
    """Error handling wrapper for BEA API responses"""
    def __init__(self, endpoint: str, error: str, status_code: Optional[int] = None):
        self.endpoint = endpoint
        self.error = error
        self.status_code = status_code
        self.timestamp = int(datetime.now().timestamp())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "success": False,
            "error": self.error,
            "endpoint": self.endpoint,
            "status_code": self.status_code,
            "timestamp": self.timestamp
        }


class BEAWrapper:
    """Comprehensive BEA API wrapper with fault tolerance"""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get('BEA_API_KEY', '')
        self.base_url = "https://apps.bea.gov/api/data/"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Fincept-Terminal/1.0'
        })

    def _make_request(self, method: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Centralized request handler with comprehensive error handling"""
        try:
            # Add API key to all requests
            params['UserID'] = self.api_key
            params['method'] = method
            params['resultformat'] = 'JSON'

            # Add Year parameter if not specified (default to most recent)
            if 'Year' not in params and method.startswith('GetData'):
                current_year = datetime.now().year
                params['Year'] = str(current_year)

            url = f"{self.base_url}?{urlencode(params)}"

            response = self.session.get(url, timeout=30)
            response.raise_for_status()

            data = response.json()

            # Check for BEA API errors
            if 'BEAAPI' in data:
                if 'Error' in data['BEAAPI']:
                    error_desc = data['BEAAPI']['Error'].get('ErrorDesc', 'Unknown BEA API error')
                    return BEAError(method, error_desc).to_dict()

                # Extract actual data
                results = data['BEAAPI'].get('Results', {})

                # Handle different response structures
                if method == 'GetDatasetList':
                    return {
                        "success": True,
                        "endpoint": method,
                        "data": results.get('Dataset', []),
                        "timestamp": int(datetime.now().timestamp())
                    }

                elif method == 'GetParameterList':
                    return {
                        "success": True,
                        "endpoint": method,
                        "data": results.get('Parameter', []),
                        "dataset_name": params.get('DatasetName', ''),
                        "timestamp": int(datetime.now().timestamp())
                    }

                elif method in ['GetParameterValues', 'GetParameterValuesFiltered']:
                    return {
                        "success": True,
                        "endpoint": method,
                        "data": results.get('ParamValue', []),
                        "parameter": params.get('ParameterName', ''),
                        "dataset_name": params.get('DatasetName', ''),
                        "timestamp": int(datetime.now().timestamp())
                    }

                else:  # GetData methods
                    return {
                        "success": True,
                        "endpoint": method,
                        "data": results.get('Data', []),
                        "dataset_name": params.get('DatasetName', ''),
                        "parameters": {
                            k: v for k, v in params.items()
                            if k not in ['UserID', 'method', 'resultformat']
                        },
                        "notes": results.get('Notes', []),
                        "statistics": results.get('Stat', []),
                        "dimensions": results.get('Dimensions', []),
                        "timestamp": int(datetime.now().timestamp())
                    }

            return BEAError(method, "Unexpected response format").to_dict()

        except requests.exceptions.RequestException as e:
            return BEAError(method, f"Network error: {str(e)}").to_dict()
        except json.JSONDecodeError as e:
            return BEAError(method, f"JSON decode error: {str(e)}").to_dict()
        except Exception as e:
            return BEAError(method, f"Unexpected error: {str(e)}").to_dict()

    # ==================== METADATA ENDPOINTS ====================

    def get_dataset_list(self) -> Dict[str, Any]:
        """Get list of all available datasets"""
        try:
            result = self._make_request('GetDatasetList', {})

            if result.get("success"):
                # Add descriptions for major datasets
                dataset_descriptions = {
                    "NIPA": "National Income and Product Accounts",
                    "NIUnderlyingDetail": "NIPA Underlying Detail",
                    "FixedAssets": "Fixed Assets",
                    "MNE": "Multinational Enterprises",
                    "GDPbyIndustry": "GDP by Industry",
                    "ITA": "International Transactions",
                    "IIP": "International Investment Position",
                    "InputOutput": "Input-Output Accounts",
                    "UnderlyingGDPbyIndustry": "GDP by Industry - Underlying Detail",
                    "IntlServTrade": "International Services Trade",
                    "Regional": "Regional Economic Accounts"
                }

                # Enhance dataset information
                for dataset in result.get("data", []):
                    dataset_name = dataset.get("DatasetName", "")
                    if dataset_name in dataset_descriptions:
                        dataset["Description"] = dataset_descriptions[dataset_name]

            return result

        except Exception as e:
            return BEAError('GetDatasetList', str(e)).to_dict()

    def get_parameter_list(self, dataset_name: str) -> Dict[str, Any]:

# ... 文件较长，已截断。总行数：912
```

### fincept-qt/scripts/bis_data.py

```python
"""
BIS (Bank for International Settlements) SDMX API wrapper
Provides access to global economic and financial statistics data from BIS

API Documentation: https://www.bis.org/statistics/about_bis_stats_data_services.htm
Base URL: https://stats.bis.org/api/v1

Key Features:
- No API key required (public data)
- SDMX 2.1 format support
- Multiple response formats (XML, JSON, CSV)
- Comprehensive time series data
- Global economic and financial statistics
"""

import asyncio
import json
import sys
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from typing import Dict, Any, Optional, List, Union
from urllib.parse import urlencode, quote
import aiohttp
import html


class BISError(Exception):
    """Custom exception for BIS API errors"""
    def __init__(self, message: str, status_code: Optional[int] = None, endpoint: Optional[str] = None):
        super().__init__(message)
        self.status_code = status_code
        self.endpoint = endpoint


class BISAPI:
    """BIS SDMX API client with comprehensive coverage of all endpoints"""

    def __init__(self, base_url: str = "https://stats.bis.org/api/v1", timeout: int = 30):
        self.base_url = base_url.rstrip('/')
        self.timeout = aiohttp.ClientTimeout(total=timeout)
        self.session = None

        # Common BIS data flows (statistical domains)
        self.known_flows = {
            "WS_EER": "Effective exchange rates",
            "WS_CBPOL": "Central bank policy rates",
            "WS_DT1": "Debt securities",
            "WS_LTINT": "Long-term interest rates",
            "WS_STINT": "Short-term interest rates",
            "WS_MON": "Monetary aggregates",
            "WS_XRU": "Exchange rates",
            "WS_CRD": "Credit to the non-financial sector",
            "WS_HP": "House prices",
            "WS_REER": "Real effective exchange rates",
            "WS_CUST": "Customs and exchange controls",
            "WS_FDI": "Foreign direct investment",
            "WS_CUR": "Currency composition of official foreign exchange reserves"
        }

        # Random user agents for requests
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
        ]

    async def __aenter__(self):
        self.session = aiohttp.ClientSession(timeout=self.timeout)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    def _get_headers(self, endpoint_type: str = "data") -> Dict[str, str]:
        """Get request headers with random user agent"""
        import random

        # Set appropriate Accept header based on endpoint type
        if endpoint_type == "structure":
            accept_header = "application/vnd.sdmx.structure+json;version=1.0.0,application/vnd.sdmx.structure+xml;version=2.1,application/xml"
        else:
            accept_header = "application/vnd.sdmx.data+json;version=1.0.0,application/vnd.sdmx.genericdata+xml;version=2.1,application/xml"

        return {
            "User-Agent": random.choice(self.user_agents),
            "Accept": accept_header,
            "Accept-Encoding": "gzip, deflate"
        }

    async def _make_request(self, endpoint: str, params: Optional[Dict[str, Any]] = None, endpoint_type: str = "data") -> Dict[str, Any]:
        """Make HTTP request with error handling"""
        if not self.session:
            raise BISError("Session not initialized. Use async with BISAPI()...")

        url = f"{self.base_url}/{endpoint}"
        headers = self._get_headers(endpoint_type)

        try:
            async with self.session.get(url, params=params, headers=headers) as response:
                if response.status == 200:
                    content_type = response.headers.get('content-type', '')

                    if 'application/json' in content_type or 'application/vnd.sdmx.data+json' in content_type:
                        data = await response.json()
                        return self._format_response(data, endpoint)
                    elif 'application/xml' in content_type or 'text/xml' in content_type:
                        text_data = await response.text()
                        return self._parse_xml_response(text_data, endpoint)
                    elif 'text/csv' in content_type:
                        text_data = await response.text()
                        return self._parse_csv_response(text_data, endpoint)
                    else:
                        # Try to parse as JSON first, then as text
                        try:
                            data = await response.json()
                            return self._format_response(data, endpoint)
                        except:
                            text_data = await response.text()
                            return {
                                "success": True,
                                "data": text_data,
                                "content_type": content_type,
                                "endpoint": endpoint,
                                "params": params
                            }
                else:
                    error_text = await response.text()
                    raise BISError(f"HTTP {response.status}: {error_text}", response.status, endpoint)

        except asyncio.TimeoutError:
            raise BISError(f"Request timeout after {self.timeout.total} seconds", None, endpoint)
        except aiohttp.ClientError as e:
            raise BISError(f"Network error: {str(e)}", None, endpoint)
        except Exception as e:
            raise BISError(f"Unexpected error: {str(e)}", None, endpoint)

    def _format_response(self, data: Dict[str, Any], endpoint: str) -> Dict[str, Any]:
        """Format API response with metadata"""
        return {
            "success": True,
            "data": data,
            "endpoint": endpoint,
            "timestamp": datetime.now().isoformat()
        }

    def _parse_xml_response(self, xml_data: str, endpoint: str) -> Dict[str, Any]:
        """Parse XML SDMX response"""
        try:
            root = ET.fromstring(xml_data)

            # Extract basic information
            result = {
                "success": True,
                "data": {
                    "xml_raw": xml_data,
                    "root_tag": root.tag,
                    "namespaces": dict(root.attrib.items()) if hasattr(root, 'attrib') else {}
                },
                "endpoint": endpoint,
                "format": "xml"
            }

            # Try to extract series data if present
            series = root.findall('.//{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic}Series')
            if series:
                result["data"]["series_count"] = len(series)
                series_data = []
                for series_elem in series[:5]:  # Limit to first 5 for preview
                    series_info = {}
                    for child in series_elem:
                        if child.tag.endswith('SeriesKey'):
                            series_info["key"] = {v.attrib.get('id'): v.text for v in child}
                        elif child.tag.endswith('Obs'):
                            obs_info = {v.attrib.get('id'): v.text for v in child}
                            series_info.setdefault("observations", []).append(obs_info)
                    series_data.append(series_info)
                result["data"]["series_preview"] = series_data


# ... 文件较长，已截断。总行数：1446
```

### fincept-qt/scripts/bis_data_extended.py

```python
"""
BIS Stats Extended Data Fetcher
Bank for International Settlements extended statistics: global credit gap,
property prices, exchange rates, banking stats, and policy rates via SDMX API.
"""
import sys
import json
import os
import requests
from typing import Dict, Any, Optional, List

API_KEY = os.environ.get('BIS_API_KEY', '')
BASE_URL = "https://stats.bis.org/api/v1/data"

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=3)
session.mount('https://', adapter)
session.mount('http://', adapter)


def _make_request(endpoint: str, params: Dict = None) -> Any:
    url = f"{BASE_URL}/{endpoint}" if not endpoint.startswith('http') else endpoint
    if params is None:
        params = {}
    params["format"] = "jsondata"
    try:
        response = session.get(url, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except (json.JSONDecodeError, ValueError) as e:
        return {"error": f"JSON decode error: {str(e)}"}


def get_credit_gap(country: str = "US") -> Any:
    key = f"CREDIT_GAPS/{country.upper()}.."
    return _make_request(key)


def get_residential_property_prices(country: str = "US", freq: str = "Q") -> Any:
    key = f"RPPI/{freq}.{country.upper()}..N.."
    return _make_request(key)


def get_commercial_property_prices(country: str = "US") -> Any:
    key = f"CPPI/Q.{country.upper()}..."
    return _make_request(key)


def get_banking_stats(reporting_country: str = "US", counterparty: str = "5J") -> Any:
    key = f"BIS_LBS_DISS/{reporting_country.upper()}.{counterparty}.A.B.A.TO1.A"
    return _make_request(key)


def get_consumer_prices(country: str = "US") -> Any:
    key = f"CPI/M.{country.upper()}.N.H.000000..P1M"
    return _make_request(key)


def get_policy_rates(country: str = "US") -> Any:
    key = f"CBPOL/M.{country.upper()}"
    return _make_request(key)


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if not args:
        print(json.dumps({"error": "No command provided"}))
        return
    command = args[0]
    result = {"error": f"Unknown command: {command}"}

    if command == "credit_gap":
        country = args[1] if len(args) > 1 else "US"
        result = get_credit_gap(country)
    elif command == "residential_prices":
        country = args[1] if len(args) > 1 else "US"
        freq = args[2] if len(args) > 2 else "Q"
        result = get_residential_property_prices(country, freq)
    elif command == "commercial_prices":
        country = args[1] if len(args) > 1 else "US"
        result = get_commercial_property_prices(country)
    elif command == "banking":
        reporting_country = args[1] if len(args) > 1 else "US"
        counterparty = args[2] if len(args) > 2 else "5J"
        result = get_banking_stats(reporting_country, counterparty)
    elif command == "cpi":
        country = args[1] if len(args) > 1 else "US"
        result = get_consumer_prices(country)
    elif command == "policy_rates":
        country = args[1] if len(args) > 1 else "US"
        result = get_policy_rates(country)

    print(json.dumps(result))


if __name__ == "__main__":
    main()
```

### fincept-qt/scripts/bis_stats_data.py

```python
"""
BIS Data Portal SDMX Data Fetcher
Global credit, debt securities, banking stats, effective exchange rates, property prices.
No API key required.
"""
import sys
import json
import os
import requests
from typing import Dict, Any, Optional, List

BASE_URL = "https://stats.bis.org/api/v1"

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=3)
session.mount('https://', adapter)
session.mount('http://', adapter)
session.headers.update({"Accept": "application/json"})


def _make_request(endpoint: str, params: Dict = None) -> Any:
    """Make HTTP request with error handling."""
    url = f"{BASE_URL}/{endpoint}" if not endpoint.startswith('http') else endpoint
    try:
        response = session.get(url, params=params, timeout=60)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except (json.JSONDecodeError, ValueError) as e:
        return {"error": f"JSON decode error: {str(e)}"}


def _parse_sdmx_compact(data: Any, label: str = "data") -> Any:
    """Extract time-series from BIS SDMX-JSON compact format."""
    if isinstance(data, dict) and "error" in data:
        return data
    try:
        datasets = data.get("dataSets", [])
        if not datasets:
            return {"error": "No dataSets in response", "keys": list(data.keys())}
        dataset = datasets[0]
        structure = data.get("structure", {})
        dimensions = structure.get("dimensions", {})
        series_dims = dimensions.get("series", [])
        obs_dims = dimensions.get("observation", [])

        time_periods = []
        for dim in obs_dims:
            if "TIME" in dim.get("id", ""):
                time_periods = [v.get("id") for v in dim.get("values", [])]

        series_list = []
        for key, series_obj in dataset.get("series", {}).items():
            parts = key.split(":")
            dim_labels = {}
            for i, dim in enumerate(series_dims):
                if i < len(parts):
                    try:
                        idx = int(parts[i])
                        vals = dim.get("values", [])
                        if idx < len(vals):
                            dim_labels[dim["id"]] = vals[idx].get("id", "")
                    except ValueError:
                        pass
            obs_map = series_obj.get("observations", {})
            observations = []
            for obs_idx_str, obs_val in obs_map.items():
                idx = int(obs_idx_str)
                period = time_periods[idx] if idx < len(time_periods) else obs_idx_str
                value = obs_val[0] if obs_val else None
                observations.append({"period": period, "value": value})
            series_list.append({"dimensions": dim_labels, "observations": observations})

        return {label: series_list, "count": len(series_list)}
    except Exception as e:
        return {"error": f"Parse error: {str(e)}"}


def get_total_credit(country: str = "US", sector: str = "P") -> Any:
    """Get BIS total credit to private non-financial sector.
    country: US, GB, DE, FR, JP, CN, KR, AU, CA, etc.
    sector: P=private, C=corporations, H=households.
    """
    params = {"format": "jsondata", "lastNObservations": 80}
    key = f"data/total-credit/Q.{sector.upper()}.A.M.770.{country.upper()}.A"
    data = _make_request(key, params=params)
    result = _parse_sdmx_compact(data, "credit_series")
    result.update({"country": country.upper(), "sector": sector.upper(), "dataset": "Total Credit"})
    return result


def get_debt_securities(issuer_type: str = "C", currency: str = "USD") -> Any:
    """Get BIS international debt securities statistics.
    issuer_type: C=all, G=government, F=financial, N=non-financial.
    currency: USD, EUR, GBP, JPY, CHF, etc.
    """
    params = {"format": "jsondata", "lastNObservations": 40}
    key = f"data/debt-sec2/Q.N.{issuer_type.upper()}.A.{currency.upper()}.A.A.TO1.A"
    data = _make_request(key, params=params)
    result = _parse_sdmx_compact(data, "debt_securities")
    result.update({"issuer_type": issuer_type, "currency": currency.upper(), "dataset": "Debt Securities"})
    return result


def get_effective_exchange_rates(country: str = "US", type_: str = "R") -> Any:
    """Get BIS effective exchange rate indices (BIS EER).
    country: US, GB, DE, FR, JP, CN, KR, AU, CA, CH, SE, NO, etc.
    type_: R=real, N=nominal.
    """
    params = {"format": "jsondata", "lastNObservations": 120}
    eer_type = "N" if type_.upper() == "N" else "R"
    key = f"data/eer/M.{eer_type}.B.{country.upper()}"
    data = _make_request(key, params=params)
    result = _parse_sdmx_compact(data, "eer_series")
    result.update({"country": country.upper(), "type": eer_type, "dataset": "Effective Exchange Rates"})
    return result


def get_property_prices(country: str = "US") -> Any:
    """Get BIS residential property price statistics.
    country: US, GB, DE, FR, JP, KR, AU, CA, SE, NL, ES, IT, CH, etc.
    """
    params = {"format": "jsondata", "lastNObservations": 100}
    key = f"data/pp-selected/Q.{country.upper()}.N.628"
    data = _make_request(key, params=params)
    result = _parse_sdmx_compact(data, "property_prices")
    result.update({"country": country.upper(), "dataset": "Property Prices"})
    return result


def get_policy_rates(country: str = "US") -> Any:
    """Get BIS central bank policy/target interest rates.
    country: US, GB, DE, FR, JP, CN, AU, CA, SE, NO, CH, NZ, etc.
    """
    params = {"format": "jsondata", "lastNObservations": 120}
    key = f"data/cb-policy-rates/M.{country.upper()}"
    data = _make_request(key, params=params)
    result = _parse_sdmx_compact(data, "policy_rates")
    result.update({"country": country.upper(), "dataset": "Policy Rates"})
    return result


def get_datasets() -> Any:
    """Get list of available BIS statistical datasets."""
    url = f"{BASE_URL}/dataflow/BIS"
    params = {"detail": "allstubs", "format": "jsondata"}
    try:
        response = session.get(url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        flows = data.get("dataflows", data.get("Dataflows", []))
        if isinstance(flows, list):
            return {
                "datasets": [
                    {"id": df.get("id"), "name": df.get("name", {}).get("en", df.get("name", ""))}
                    for df in flows
                ],
                "count": len(flows)
            }
        return {"raw_keys": list(data.keys())}
    except Exception as e:
        # Return known datasets
        return {
            "datasets": [
                {"id": "total-credit", "name": "Total credit to the private non-financial sector"},
                {"id": "debt-sec2", "name": "International debt securities"},
                {"id": "eer", "name": "Effective exchange rates"},
                {"id": "pp-selected", "name": "Residential property prices"},
                {"id": "cb-policy-rates", "name": "Central bank policy rates"},
                {"id": "lbs-by-residence", "name": "Locational banking statistics"},
                {"id": "cbs-by-residence", "name": "Consolidated banking statistics"},
                {"id": "dsr", "name": "Debt service ratios"},
            ],
            "note": f"Dataset list endpoint failed: {str(e)}"
        }



# ... 文件较长，已截断。总行数：239
```

### fincept-qt/scripts/blockchain_com_data.py

```python
"""
Blockchain.com Data Fetcher
Bitcoin network stats, hashrate, mempool, tx volumes, address data.
No API key required.
"""
import sys
import json
import os
import requests
from typing import Dict, Any, Optional, List

BASE_URL = "https://api.blockchain.info"

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=3)
session.mount('https://', adapter)
session.mount('http://', adapter)
session.headers.update({"Accept": "application/json"})


def _make_request(endpoint: str, params: Dict = None) -> Any:
    """Make HTTP request with error handling."""
    url = f"{BASE_URL}/{endpoint}" if not endpoint.startswith('http') else endpoint
    try:
        response = session.get(url, params=params, timeout=30)
        response.raise_for_status()
        ct = response.headers.get("content-type", "")
        if "json" in ct:
            return response.json()
        # Some endpoints return plain text/numbers
        text = response.text.strip()
        try:
            return json.loads(text)
        except (json.JSONDecodeError, ValueError):
            return {"value": text}
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


def get_stats() -> Any:
    """Get comprehensive Bitcoin network statistics."""
    data = _make_request("stats")
    if isinstance(data, dict) and "error" not in data:
        return {
            "market_price_usd": data.get("market_price_usd"),
            "hash_rate": data.get("hash_rate"),
            "total_fees_btc": data.get("total_fees_btc"),
            "n_btc_mined": data.get("n_btc_mined"),
            "n_tx": data.get("n_tx"),
            "n_blocks_mined": data.get("n_blocks_mined"),
            "minutes_between_blocks": data.get("minutes_between_blocks"),
            "totalbc": data.get("totalbc"),
            "n_blocks_total": data.get("n_blocks_total"),
            "estimated_transaction_volume_usd": data.get("estimated_transaction_volume_usd"),
            "blocks_size": data.get("blocks_size"),
            "miners_revenue_usd": data.get("miners_revenue_usd"),
            "nextretarget": data.get("nextretarget"),
            "difficulty": data.get("difficulty"),
            "estimated_btc_sent": data.get("estimated_btc_sent"),
            "miners_revenue_btc": data.get("miners_revenue_btc"),
            "total_btc_sent": data.get("total_btc_sent"),
            "trade_volume_btc": data.get("trade_volume_btc"),
            "trade_volume_usd": data.get("trade_volume_usd"),
        }
    return data


def get_chart(chart_name: str, timespan: str = "1year") -> Any:
    """Get chart data for various Bitcoin metrics.
    Available charts: total-bitcoins, market-price, market-cap, trade-volume,
    blocks-size, avg-block-size, n-transactions, hash-rate, difficulty, etc.
    Timespans: 1week, 2weeks, 1month, 3months, 6months, 1year, 2year, all.
    """
    params = {"timespan": timespan, "format": "json", "cors": "true"}
    data = _make_request(f"charts/{chart_name}", params=params)
    if isinstance(data, dict) and "values" in data:
        return {
            "chart": chart_name,
            "timespan": timespan,
            "unit": data.get("unit"),
            "period": data.get("period"),
            "description": data.get("description"),
            "name": data.get("name"),
            "values": data["values"],
            "count": len(data["values"]),
        }
    return data


def get_pools(timespan: str = "4days") -> Any:
    """Get mining pool distribution by hashrate share.
    Timespans: 24hours, 48hours, 4days, 1week, 2week, 1month.
    """
    params = {"timespan": timespan}
    data = _make_request("pools", params=params)
    if isinstance(data, dict) and "error" not in data:
        pools = [{"pool": k, "blocks": v} for k, v in data.items()]
        pools.sort(key=lambda x: x["blocks"], reverse=True)
        return {"timespan": timespan, "pools": pools, "total_pools": len(pools)}
    return data


def get_address(address: str) -> Any:
    """Get address balance and transaction history."""
    params = {"format": "json"}
    data = _make_request(f"rawaddr/{address}", params=params)
    if isinstance(data, dict) and "error" not in data:
        txs = data.get("txs", [])
        return {
            "address": address,
            "final_balance": data.get("final_balance"),
            "n_tx": data.get("n_tx"),
            "total_received": data.get("total_received"),
            "total_sent": data.get("total_sent"),
            "recent_transactions": txs[:10],
        }
    return data


def get_transaction(tx_hash: str) -> Any:
    """Get details for a specific Bitcoin transaction."""
    data = _make_request(f"rawtx/{tx_hash}")
    if isinstance(data, dict) and "error" not in data:
        return {
            "hash": data.get("hash"),
            "time": data.get("time"),
            "block_height": data.get("block_height"),
            "fee": data.get("fee"),
            "size": data.get("size"),
            "inputs": data.get("inputs", [])[:5],
            "out": data.get("out", [])[:5],
            "input_count": len(data.get("inputs", [])),
            "output_count": len(data.get("out", [])),
        }
    return data


def get_ticker() -> Any:
    """Get Bitcoin ticker data in multiple currencies."""
    data = _make_request("ticker")
    if isinstance(data, dict) and "error" not in data:
        result = {}
        for currency, info in data.items():
            result[currency] = {
                "buy": info.get("buy"),
                "sell": info.get("sell"),
                "last": info.get("last"),
                "15m": info.get("15m"),
                "symbol": info.get("symbol"),
            }
        return {"ticker": result, "currencies": list(result.keys())}
    return data


def get_mempool() -> Any:
    """Get current mempool size and unconfirmed transaction count."""
    data = _make_request("q/unconfirmedcount")
    unconfirmed = data.get("value") if isinstance(data, dict) else data
    size_data = _make_request("q/getblockcount")
    block_count = size_data.get("value") if isinstance(size_data, dict) else size_data
    return {
        "unconfirmed_count": unconfirmed,
        "block_height": block_count,
    }


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if not args:
        print(json.dumps({"error": "No command provided. Available: stats, chart, pools, address, transaction, ticker, mempool"}))
        return

    command = args[0]

    if command == "stats":
        result = get_stats()
    elif command == "chart":

# ... 文件较长，已截断。总行数：210
```

### fincept-qt/scripts/bls_data.py

```python
# BLS (Bureau of Labor Statistics) Data Wrapper
# Based on OpenBB BLS provider - https://github.com/OpenBB-finance/OpenBB/tree/main/openbb_platform/providers/bls

import sys
import json
import requests
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Union, Any, Literal
from io import StringIO
import pandas as pd
import asyncio
import aiohttp

# BLS API Configuration
BLS_API_URL = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
BLS_FTP_BASE = "https://download.bls.gov/pub/time.series/"

# Survey Categories (from OpenBB constants)
SURVEY_CATEGORIES = {
    "cpi": ["ap", "cu", "cw", "li", "su", "ei"],
    "pce": ["cx"],
    "ppi": ["wp", "pc"],
    "ip": ["ip", "pr", "mp"],
    "jolts": ["jl", "jt"],
    "nfp": ["ce"],
    "cps": ["le", "lu"],
    "lfs": ["ln", "fm", "in", "ws"],
    "wages": ["ci", "wm"],
    "ec": ["cm", "cc"],
    "sla": ["la", "sm"],
    "bed": ["bd"],
    "tu": ["tu"]
}

SURVEY_CATEGORY_NAMES = {
    "cpi": "Consumer Price Index",
    "pce": "Personal Consumption Expenditure",
    "ppi": "Producer Price Index",
    "ip": "Industry Productivity",
    "jolts": "Job Openings and Labor Turnover Survey",
    "nfp": "Nonfarm Payrolls",
    "cps": "Current Population Survey",
    "lfs": "Labor Force Statistics",
    "wages": "Wages",
    "ec": "Employer Costs",
    "sla": "State and Local Area Employment",
    "bed": "Business Employment Dynamics",
    "tu": "Time Use",
}

# Popular Series IDs for quick access
POPULAR_SERIES = {
    "CPIAUCSL": "Consumer Price Index for All Urban Consumers: All Items",
    "UNRATE": "Unemployment Rate",
    "PAYEMS": "All Employees: Total Nonfarm Payrolls",
    "CPIAUCNS": "Consumer Price Index for All Urban Consumers: All Items (NSA)",
    "USPRIV": "All Employees: Private",
    "CES0000000001": "All Employees: Total Nonfarm",
    "LNS14000000": "Unemployment Rate",
    "LNS13000000": "Labor Force Participation Rate",
    "LNS11300000": "Employment-Population Ratio",
    "CIVPART": "Labor Force Participation Rate",
    "EMRATIO": "Employment-Population Ratio"
}


class BLSError:
    """Custom error class for BLS API errors"""
    def __init__(self, endpoint: str, error: str, status_code: Optional[int] = None):
        self.endpoint = endpoint
        self.error = error
        self.status_code = status_code
        self.timestamp = int(datetime.now().timestamp())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "error": True,
            "endpoint": self.endpoint,
            "message": self.error,
            "status_code": self.status_code,
            "timestamp": self.timestamp
        }


class BLSDataAPI:
    """BLS Data API wrapper for modular data fetching"""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("BLS_API_KEY")
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Fincept-Terminal/1.0',
            'Content-Type': 'application/json'
        })

        # Cache for series data (24-hour cache)
        self._cache_timeout = 24 * 60 * 60  # 24 hours
        self._cache = {}

    def _is_cache_valid(self, cache_key: str) -> bool:
        """Check if cached data is still valid"""
        if cache_key not in self._cache:
            return False

        cached_time = self._cache[cache_key].get("timestamp", 0)
        current_time = datetime.now().timestamp()
        return (current_time - cached_time) < self._cache_timeout

    def _get_cached_data(self, cache_key: str) -> Optional[pd.DataFrame]:
        """Get cached data if valid"""
        if self._is_cache_valid(cache_key):
            return self._cache[cache_key].get("data")
        return None

    def _set_cache_data(self, cache_key: str, data: pd.DataFrame) -> None:
        """Set cached data with timestamp"""
        self._cache[cache_key] = {
            "data": data,
            "timestamp": datetime.now().timestamp()
        }

    async def _make_async_request(self, url: str, method: str = "GET",
                                  headers: Optional[Dict] = None,
                                  data: Optional[str] = None) -> Dict[str, Any]:
        """Make async HTTP request with error handling"""
        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                if method.upper() == "GET":
                    async with session.get(url) as response:
                        if response.status == 200:
                            result = await response.json()
                            return {"success": True, "data": result}
                        else:
                            return BLSError(url, f"HTTP {response.status}: {await response.text()}", response.status).to_dict()
                elif method.upper() == "POST":
                    async with session.post(url, data=data) as response:
                        if response.status == 200:
                            result = await response.json()
                            return {"success": True, "data": result}
                        else:
                            return BLSError(url, f"HTTP {response.status}: {await response.text()}", response.status).to_dict()

        except aiohttp.ClientError as e:
            return BLSError(url, f"Network error: {str(e)}").to_dict()
        except json.JSONDecodeError as e:
            return BLSError(url, f"JSON decode error: {str(e)}").to_dict()
        except Exception as e:
            return BLSError(url, f"Unexpected error: {str(e)}").to_dict()

    def _make_request(self, url: str, method: str = "GET",
                     headers: Optional[Dict] = None,
                     data: Optional[str] = None) -> Dict[str, Any]:
        """Make HTTP request with error handling"""
        try:
            if method.upper() == "GET":
                response = self.session.get(url, headers=headers, timeout=30)
            elif method.upper() == "POST":
                response = self.session.post(url, headers=headers, data=data, timeout=30)
            else:
                return BLSError(url, f"Unsupported method: {method}").to_dict()

            if response.status_code == 200:
                try:
                    data = response.json()
                    return {"success": True, "data": data}
                except json.JSONDecodeError:
                    return BLSError(url, "Invalid JSON response", response.status_code).to_dict()
            else:
                return BLSError(url, f"HTTP {response.status_code}: {response.text}", response.status_code).to_dict()

        except requests.exceptions.RequestException as e:
            return BLSError(url, f"Network error: {str(e)}", getattr(e.response, 'status_code', None)).to_dict()
        except Exception as e:
            return BLSError(url, f"Unexpected error: {str(e)}").to_dict()

    def _parse_ftp_data(self, content: str) -> pd.DataFrame:
        """Parse tab-delimited FTP data"""
        try:
            df = pd.read_csv(StringIO(content), sep="\t", low_memory=False, dtype="object")

# ... 文件较长，已截断。总行数：803
```

### fincept-qt/scripts/bnm_data.py

```python
"""
Bank Negara Malaysia (BNM) Data Wrapper
Fetches data from the BNM Open API.

API Reference:
  Base URL:  https://api.bnm.gov.my/public
  Format:    JSON
  Auth:      None required — fully public
  Docs:      https://api.bnm.gov.my/

Accept header required: application/vnd.BNM.API.v1+json

Endpoints:
  GET /exchange-rate                    — All currency rates (current session)
    ?session=0900|1200|1130             — Rate session (0900=morning, 1200=noon, 1130=closing)
  GET /exchange-rate/{currency}         — Single currency rate
    ?session=0900|1200|1130
  GET /interest-rate                    — Base rate, BLR, OPR, KLIBOR
  GET /base-rate                        — Base rate and BLR
  GET /kijang-emas                      — Gold coin (Kijang Emas) prices
  GET /interbank-swap                   — Interbank FX swap
  GET /opr                             — OPR (overnight policy rate) latest

Exchange rates expressed as MYR per foreign currency unit.
Some currencies use unit=100 (AED, HKD, IDR, INR, JPY, KHR, KRW, MMK,
NPR, PHP, PKR, SAR, THB, TWD, VND); the wrapper normalises to MYR per 1 unit.

27 currencies: AED, AUD, BND, CAD, CHF, CNY, EGP, EUR, GBP, HKD, IDR,
               INR, JPY, KHR, KRW, MMK, NOK, NPR, NZD, PHP, PKR, SAR,
               SDR, SGD, THB, TWD, USD, VND

Returns JSON output for C++ integration.
"""

import sys
import json
import requests
import traceback
from typing import Dict, Any, List, Optional
from datetime import datetime, date, timedelta, timezone


BASE_URL        = "https://api.bnm.gov.my/public"
ACCEPT_HEADER   = "application/vnd.BNM.API.v1+json"
DEFAULT_TIMEOUT = 30

# Sessions: morning fixing, noon, 1130 closing
SESSIONS = ["0900", "1200", "1130"]

MAJOR_CURRENCIES = ["USD", "EUR", "GBP", "JPY", "CHF", "AUD", "CAD",
                    "SGD", "CNY", "HKD", "INR", "NZD"]
ASEAN_CURRENCIES = ["SGD", "IDR", "THB", "PHP", "VND", "KHR", "MMK",
                    "BND", "AUD", "NZD"]

# Unit multipliers per currency (unit=100 → divide by 100 to get MYR per 1 unit)
UNIT_MAP: Dict[str, int] = {
    "AED": 100, "HKD": 100, "IDR": 100, "INR": 100,
    "JPY": 100, "KHR": 100, "KRW": 100, "MMK": 100,
    "NPR": 100, "PHP": 100, "PKR": 100, "SAR": 100,
    "THB": 100, "TWD": 100, "VND": 100,
}


# ---------------------------------------------------------------------------
# Error container
# ---------------------------------------------------------------------------

class BNMError:
    def __init__(self, endpoint: str, error: str, status_code: Optional[int] = None):
        self.endpoint    = endpoint
        self.error       = error
        self.status_code = status_code
        self.timestamp   = int(datetime.now(timezone.utc).timestamp())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "success":     False,
            "endpoint":    self.endpoint,
            "error":       self.error,
            "status_code": self.status_code,
            "timestamp":   self.timestamp,
            "type":        "BNMError",
        }


# ---------------------------------------------------------------------------
# Main wrapper
# ---------------------------------------------------------------------------

class BNMWrapper:
    """
    Wrapper for the Bank Negara Malaysia (BNM) Open API.

    Exchange rates are MYR (Malaysian Ringgit) per 1 unit of foreign currency.
    Currencies with unit=100 are normalised by the wrapper.
    Three rate sessions per day: 0900 (morning fix), 1200 (noon), 1130 (closing).
    """

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Fincept-Terminal/4.0.2",
            "Accept":     ACCEPT_HEADER,
        })

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _get(self, path: str, params: Optional[Dict] = None) -> Any:
        url  = f"{BASE_URL}/{path.lstrip('/')}"
        resp = self.session.get(url, params=params or {}, timeout=DEFAULT_TIMEOUT)
        resp.raise_for_status()
        return resp.json()

    def _normalise_rate(self, value: Optional[float],
                        unit: int) -> Optional[float]:
        """Normalise rate: if unit=100, divide by 100 to get per-1-unit."""
        if value is None:
            return None
        return round(value / unit, 6) if unit > 1 else value

    def _parse_fx_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """Parse a single FX item from BNM API into clean dict."""
        code   = item.get("currency_code", "")
        raw    = item.get("unit", 1)
        unit   = int(raw) if raw else UNIT_MAP.get(code, 1)
        rate   = item.get("rate", {})
        return {
            "currency":   code,
            "date":       rate.get("date", ""),
            "buying":     self._normalise_rate(rate.get("buying_rate"),  unit),
            "selling":    self._normalise_rate(rate.get("selling_rate"), unit),
            "middle":     self._normalise_rate(rate.get("middle_rate"),  unit),
            "unit":       unit,
        }

    # ------------------------------------------------------------------
    # Public methods
    # ------------------------------------------------------------------

    def get_exchange_rates(self, session: str = "1130") -> Dict[str, Any]:
        """All currency rates vs MYR for the specified daily session."""
        session = session.strip()
        try:
            data    = self._get("exchange-rate", {"session": session})
            items   = data.get("data", [])
            meta    = data.get("meta", {})
            parsed  = [self._parse_fx_item(i) for i in items]
            # Build simple flat dict: {USD: middle_rate, ...}
            flat: Dict[str, Optional[float]] = {}
            for p in parsed:
                flat[p["currency"]] = p["middle"] or p["buying"]
            return {
                "success":    True,
                "session":    session,
                "date":       parsed[0]["date"] if parsed else "",
                "data":       flat,
                "full_data":  parsed,
                "count":      len(parsed),
                "note":       "MYR per 1 unit of foreign currency (normalised from unit=100 where applicable)",
                "source":     "Bank Negara Malaysia",
                "url":        f"{BASE_URL}/exchange-rate",
                "meta":       meta,
                "timestamp":  int(datetime.now(timezone.utc).timestamp()),
            }
        except requests.exceptions.HTTPError as e:
            sc = e.response.status_code if e.response is not None else None
            return BNMError("exchange-rate", str(e), sc).to_dict()
        except Exception as e:
            return BNMError("exchange-rate", str(e)).to_dict()

    def get_currency(self, currency: str, session: str = "1130") -> Dict[str, Any]:
        """Current rate for a single currency vs MYR."""
        currency = currency.upper()
        try:
            data   = self._get(f"exchange-rate/{currency}", {"session": session})
            item   = data.get("data", {})
            meta   = data.get("meta", {})
            parsed = self._parse_fx_item(item)

# ... 文件较长，已截断。总行数：437
```

### fincept-qt/scripts/bnr_data.py

```python
"""
National Bank of Romania (BNR) Data Wrapper
Fetches data from the BNR public XML API.

API Reference:
  Base URL:  https://www.bnr.ro
  Format:    XML (utf-8)
  Auth:      None required — fully public
  Docs:      https://www.bnr.ro/Cursuri-de-schimb-524.aspx

Endpoints:
  GET /nbrfxrates.xml                    — Latest reference rates (today)
  GET /nbrfxrates.xml?date=YYYYMMDD      — Rates for a specific date
  GET /files/xml/years/nbrfxrates{Y}.xml — All rates for a calendar year

Exchange rates expressed as RON per foreign currency unit.
Some currencies use a multiplier (e.g. JPY per 100, HUF per 100, KRW per 100).

Currencies published (36+):
  AED, AUD, BGN, BRL, CAD, CHF, CNY, CZK, DKK, EGP, EUR, GBP, HKD,
  HUF, IDR, ILS, INR, ISK, JPY, KRW, MDL, MXN, MYR, NOK, NZD, PHP,
  PLN, RON (1), RSD, RUB, SEK, SGD, THB, TRY, UAH, USD, XAU, XDR, ZAR

Returns JSON output for C++ integration.
"""

import sys
import json
import requests
import traceback
import xml.etree.ElementTree as ET
from typing import Dict, Any, List, Optional
from datetime import datetime, date, timedelta, timezone


BASE_URL        = "https://www.bnr.ro"
XML_NS          = "http://www.bnr.ro/xsd"
DEFAULT_TIMEOUT = 30

MAJOR_CURRENCIES = ["USD", "EUR", "GBP", "JPY", "CHF", "CAD", "AUD",
                    "NOK", "SEK", "DKK", "CNY", "PLN", "HUF", "CZK"]


# ---------------------------------------------------------------------------
# Error container
# ---------------------------------------------------------------------------

class BNRError:
    def __init__(self, endpoint: str, error: str, status_code: Optional[int] = None):
        self.endpoint    = endpoint
        self.error       = error
        self.status_code = status_code
        self.timestamp   = int(datetime.now(timezone.utc).timestamp())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "success":     False,
            "endpoint":    self.endpoint,
            "error":       self.error,
            "status_code": self.status_code,
            "timestamp":   self.timestamp,
            "type":        "BNRError",
        }


# ---------------------------------------------------------------------------
# Main wrapper
# ---------------------------------------------------------------------------

class BNRWrapper:
    """
    Wrapper for the National Bank of Romania XML data feed.

    All rates are RON per 1 unit of foreign currency.
    For currencies with multiplier > 1 (e.g. JPY, HUF, KRW, IDR, ISK):
      actual_rate = obs_value / multiplier
    The wrapper normalises all rates to RON per 1 unit.
    """

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Fincept-Terminal/4.0.2",
            "Accept":     "application/xml, text/xml, */*",
        })

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _fetch_xml(self, url: str) -> bytes:
        resp = self.session.get(url, timeout=DEFAULT_TIMEOUT)
        resp.raise_for_status()
        return resp.content

    def _parse_dataset(self, content: bytes) -> List[Dict[str, Any]]:
        """
        Parse a BNR XML DataSet (single date or full-year).
        Returns list of {date, CCY1: rate, CCY2: rate, ...} rows.
        RON rates are normalised: value / multiplier.
        """
        root = ET.fromstring(content)
        ns   = {"b": XML_NS}
        rows: List[Dict[str, Any]] = []

        for cube in root.findall(".//b:Cube", ns):
            d = cube.get("date", "")
            row: Dict[str, Any] = {"date": d}
            for rate_el in cube.findall("b:Rate", ns):
                ccy  = rate_el.get("currency", "")
                mult = int(rate_el.get("multiplier", "1"))
                try:
                    val = float(rate_el.text or "0")
                    row[ccy] = round(val / mult, 6)
                except (ValueError, TypeError):
                    pass
            if d:
                rows.append(row)

        return sorted(rows, key=lambda r: r["date"])

    def _parse_header(self, content: bytes) -> Dict[str, str]:
        """Extract header metadata (publisher, publish date, message type)."""
        root   = ET.fromstring(content)
        ns     = {"b": XML_NS}
        header = root.find("b:Header", ns)
        if header is None:
            return {}
        return {
            "publisher":      (header.findtext("b:Publisher",  namespaces=ns) or "").strip(),
            "publish_date":   (header.findtext("b:PublishingDate", namespaces=ns) or "").strip(),
            "orig_currency":  (header.findtext("b:Body/b:OrigCurrency", namespaces={"b": XML_NS}) or "RON").strip(),
        }

    def _today_url(self) -> str:
        return f"{BASE_URL}/nbrfxrates.xml"

    def _date_url(self, d: str) -> str:
        # BNR expects YYYYMMDD
        clean = d.replace("-", "")
        return f"{BASE_URL}/nbrfxrates.xml?date={clean}"

    def _year_url(self, year: int) -> str:
        return f"{BASE_URL}/files/xml/years/nbrfxrates{year}.xml"

    # ------------------------------------------------------------------
    # Public methods
    # ------------------------------------------------------------------

    def get_today(self) -> Dict[str, Any]:
        """Latest reference rates (today's publication)."""
        url = self._today_url()
        try:
            content = self._fetch_xml(url)
            rows    = self._parse_dataset(content)
            latest  = rows[-1] if rows else {}
            return {
                "success":   True,
                "date":      latest.get("date", ""),
                "data":      latest,
                "note":      "RON per 1 unit of foreign currency (normalised for multiplied currencies)",
                "source":    "National Bank of Romania",
                "url":       url,
                "timestamp": int(datetime.now(timezone.utc).timestamp()),
            }
        except requests.exceptions.HTTPError as e:
            sc = e.response.status_code if e.response is not None else None
            return BNRError("today", str(e), sc).to_dict()
        except Exception as e:
            return BNRError("today", str(e)).to_dict()

    def get_date(self, rate_date: str) -> Dict[str, Any]:
        """Reference rates for a specific date (YYYY-MM-DD)."""
        url = self._date_url(rate_date)
        try:
            content = self._fetch_xml(url)
            rows    = self._parse_dataset(content)
            entry   = rows[-1] if rows else {}
            return {
                "success":   True,

# ... 文件较长，已截断。总行数：434
```

### fincept-qt/scripts/boc_data.py

```python
"""
Bank of Canada (BoC) Data Wrapper
Fetches data from the Bank of Canada Valet API.

API Reference:
  Base URL:  https://www.bankofcanada.ca/valet
  Format:    JSON
  Auth:      None required — fully public
  Docs:      https://www.bankofcanada.ca/valet/docs

Endpoints:
  GET /lists/series/json              — Full catalogue of all 15,000+ series
  GET /lists/groups/json              — Groups/categories
  GET /observations/{series}/json     — Observation history
    ?recent=N                         — Last N observations
    ?start_date=YYYY-MM-DD            — From date
    ?end_date=YYYY-MM-DD              — To date
  GET /observations/group/{group}/json — All series in a group

Key series IDs:
  FXUSDCAD, FXEURCAD, FXGBPCAD, FXJPYCAD, FXCHFCAD, FXAUDCAD — Exchange rates
  STATIC_ATABLE_V39079  — Overnight rate target (policy rate, end of month)
  AVG.INTWO             — CORRA (Canadian Overnight Repo Rate Average)
  V80691342             — 1-month treasury bill yield
  V80691344             — 3-month treasury bill yield
  V80691346             — 6-month treasury bill yield
  V80691348             — 1-year treasury bill yield
  V122530               — Prime rate
  A.BCPI                — Bank of Canada commodity price index
  A.ENER                — Energy commodity price sub-index

Returns JSON output for C++ integration.
"""

import sys
import json
import requests
import traceback
from typing import Dict, Any, List, Optional
from datetime import datetime, date, timedelta, timezone


BASE_URL        = "https://www.bankofcanada.ca/valet"
DEFAULT_TIMEOUT = 30


# ---------------------------------------------------------------------------
# Key series catalogue
# ---------------------------------------------------------------------------

SERIES = {
    # Exchange rates (CAD per 1 foreign currency unit)
    "FXUSDCAD": {"label": "USD/CAD",  "category": "exchange_rates"},
    "FXEURCAD": {"label": "EUR/CAD",  "category": "exchange_rates"},
    "FXGBPCAD": {"label": "GBP/CAD",  "category": "exchange_rates"},
    "FXJPYCAD": {"label": "JPY/CAD",  "category": "exchange_rates"},
    "FXCHFCAD": {"label": "CHF/CAD",  "category": "exchange_rates"},
    "FXAUDCAD": {"label": "AUD/CAD",  "category": "exchange_rates"},
    "FXNZDCAD": {"label": "NZD/CAD",  "category": "exchange_rates"},
    "FXHKDCAD": {"label": "HKD/CAD",  "category": "exchange_rates"},
    "FXSEKCAD": {"label": "SEK/CAD",  "category": "exchange_rates"},
    "FXNOKCAD": {"label": "NOK/CAD",  "category": "exchange_rates"},
    "FXDKKCAD": {"label": "DKK/CAD",  "category": "exchange_rates"},
    "FXSGDCAD": {"label": "SGD/CAD",  "category": "exchange_rates"},
    "FXCNYCAD": {"label": "CNY/CAD",  "category": "exchange_rates"},
    "FXINRCAD": {"label": "INR/CAD",  "category": "exchange_rates"},
    "FXMXNCAD": {"label": "MXN/CAD",  "category": "exchange_rates"},
    # Interest rates / policy
    "STATIC_ATABLE_V39079": {"label": "Overnight rate target",    "category": "interest_rates"},
    "AVG.INTWO":            {"label": "CORRA overnight repo rate", "category": "interest_rates"},
    "V80691342":            {"label": "T-bill 1 month",           "category": "interest_rates"},
    "V80691344":            {"label": "T-bill 3 month",           "category": "interest_rates"},
    "V80691346":            {"label": "T-bill 6 month",           "category": "interest_rates"},
    "V80691348":            {"label": "T-bill 1 year",            "category": "interest_rates"},
    "V122530":              {"label": "Prime rate",                "category": "interest_rates"},
    # Commodity prices
    "A.BCPI":               {"label": "Commodity Price Index",     "category": "commodities"},
    "A.ENER":               {"label": "Energy sub-index",          "category": "commodities"},
    "A.MTLS":               {"label": "Metals sub-index",          "category": "commodities"},
    "A.AGRI":               {"label": "Agriculture sub-index",     "category": "commodities"},
}

FX_SERIES = [k for k, v in SERIES.items() if v["category"] == "exchange_rates"]
RATE_SERIES = [k for k, v in SERIES.items() if v["category"] == "interest_rates"]


# ---------------------------------------------------------------------------
# Error container
# ---------------------------------------------------------------------------

class BoCError:
    def __init__(self, endpoint: str, error: str, status_code: Optional[int] = None):
        self.endpoint    = endpoint
        self.error       = error
        self.status_code = status_code
        self.timestamp   = int(datetime.now(timezone.utc).timestamp())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "success":     False,
            "endpoint":    self.endpoint,
            "error":       self.error,
            "status_code": self.status_code,
            "timestamp":   self.timestamp,
            "type":        "BoCError",
        }


# ---------------------------------------------------------------------------
# Main wrapper
# ---------------------------------------------------------------------------

class BoCWrapper:
    """
    Wrapper for the Bank of Canada Valet REST API.

    All data is free, no authentication required.
    Exchange rates are expressed as CAD per 1 unit of foreign currency.
    """

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Fincept-Terminal/4.0.2",
            "Accept":     "application/json",
        })

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _get(self, path: str, params: Optional[Dict] = None) -> Any:
        url  = f"{BASE_URL}/{path.lstrip('/')}"
        resp = self.session.get(url, params=params or {}, timeout=DEFAULT_TIMEOUT)
        resp.raise_for_status()
        return resp.json()

    def _parse_observations(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Flatten Valet observations into wide-format list of {date, series: value}."""
        obs_raw  = data.get("observations", [])
        rows: List[Dict[str, Any]] = []
        for o in obs_raw:
            row: Dict[str, Any] = {"date": o.get("d", "")}
            for k, v in o.items():
                if k == "d":
                    continue
                val = v.get("v") if isinstance(v, dict) else v
                if val is not None:
                    try:
                        row[k] = float(val)
                    except (ValueError, TypeError):
                        row[k] = val
            rows.append(row)
        return rows

    def _obs(self, series_ids: str, recent: Optional[int] = None,
             start_date: Optional[str] = None,
             end_date: Optional[str] = None) -> Dict[str, Any]:
        """Fetch observations for one or more comma-joined series IDs."""
        params: Dict[str, Any] = {}
        if recent:
            params["recent"] = recent
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        try:
            data = self._get(f"observations/{series_ids}/json", params)
            rows = self._parse_observations(data)
            detail = data.get("seriesDetail", {})
            return {
                "success":    True,
                "series":     series_ids,
                "detail":     detail,
                "data":       rows,
                "count":      len(rows),
                "source":     "Bank of Canada",
                "url":        f"{BASE_URL}/observations/{series_ids}/json",
                "timestamp":  int(datetime.now(timezone.utc).timestamp()),
            }

# ... 文件较长，已截断。总行数：400
```

### fincept-qt/scripts/boe_data.py

```python
#!/usr/bin/env python3
"""
Bank of England (BoE) Statistical Interactive Database (IADB) Wrapper

Provides programmatic access to the Bank of England's IADB covering:
- Official Bank Rate (base rate)
- SONIA (Sterling Overnight Index Average)
- Spot exchange rates (GBP vs 26+ currencies)
- Sterling Exchange Rate Index (ERI / trade-weighted)
- Gilt yield curves (nominal, real, inflation, OIS)
- Quoted household interest rates (mortgages, deposits, consumer credit)
- Effective interest rates
- Monetary aggregates (M0, M4, M4Lx, notes & coin)
- Balance sheet / Bankstats data

API details:
- Base URL: https://www.bankofengland.co.uk/boeapps/database/_iadb-fromshowcolumns.asp
- No authentication required (completely free and open)
- Response formats: CSV (primary), XML, HTML, Excel
- Date format: DD/Mon/YYYY (e.g. 01/Jan/2000)
- Up to 300 series codes per CSV/XML/HTML request; 250 for Excel
- Missing values represented as ".." (two dots) -> converted to None/NaN

Usage:
    python boe_data.py available_categories
    python boe_data.py bank_rate [--start 01/Jan/2000] [--end now]
    python boe_data.py sonia [--start 01/Jan/2020] [--end now]
    python boe_data.py exchange_rates [--start 01/Jan/2020] [--end now]
    python boe_data.py exchange_rate_index [--start 01/Jan/2020] [--end now]
    python boe_data.py quoted_rates [--start 01/Jan/2012] [--end now]
    python boe_data.py effective_rates [--start 01/Jan/2012] [--end now]
    python boe_data.py monetary_aggregates [--start 01/Jan/2010] [--end now]
    python boe_data.py series --codes IUDBEDR,IUDSOIA [--start 01/Jan/2020] [--end now]
    python boe_data.py overview
"""

import sys
import json
import io
import csv
import requests
from datetime import datetime, date
from typing import Dict, List, Optional, Any, Union

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

BOE_BASE_URL = "https://www.bankofengland.co.uk/boeapps/database/_iadb-fromshowcolumns.asp"

# Reusable session with retry behaviour
_session = requests.Session()
_adapter = requests.adapters.HTTPAdapter(
    pool_connections=5,
    pool_maxsize=10,
    max_retries=requests.adapters.Retry(total=3, backoff_factor=1),
)
_session.mount("https://", _adapter)
_session.headers.update({
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
})

# ---------------------------------------------------------------------------
# Key series-code reference catalogue
# ---------------------------------------------------------------------------

SERIES_CATALOGUE: Dict[str, Dict[str, Any]] = {
    # --- Monetary Policy -------------------------------------------------------
    "IUDBEDR": {
        "name": "Official Bank Rate (Base Rate)",
        "category": "interest_rates",
        "subcategory": "monetary_policy",
        "frequency": "daily",
        "description": "Bank of England policy rate set by the Monetary Policy Committee (MPC).",
        "unit": "percent",
    },
    "IUDSOIA": {
        "name": "Daily SONIA Rate",
        "category": "interest_rates",
        "subcategory": "money_market",
        "frequency": "daily",
        "description": "Sterling Overnight Index Average – effective overnight interbank rate.",
        "unit": "percent",
    },
    "IUASOIA": {
        "name": "SONIA Compounded Index",
        "category": "interest_rates",
        "subcategory": "money_market",
        "frequency": "daily",
        "description": "SONIA Compounded Index published from 3 August 2020 for RFR transition.",
        "unit": "index",
    },

    # --- Government Gilt Yield Curves (nominal par yields) ---------------------
    "IUDSNPY": {
        "name": "Nominal Par Yield – 5Y",
        "category": "yield_curves",
        "subcategory": "gilt_nominal",
        "frequency": "daily",
        "description": "UK gilt nominal par yield, 5-year maturity.",
        "unit": "percent",
    },
    "IUDMNPY": {
        "name": "Nominal Par Yield – 10Y",
        "category": "yield_curves",
        "subcategory": "gilt_nominal",
        "frequency": "daily",
        "description": "UK gilt nominal par yield, 10-year maturity.",
        "unit": "percent",
    },
    "IUDLNPY": {
        "name": "Nominal Par Yield – 20Y",
        "category": "yield_curves",
        "subcategory": "gilt_nominal",
        "frequency": "daily",
        "description": "UK gilt nominal par yield, 20-year maturity.",
        "unit": "percent",
    },
    "IUDSIZC": {
        "name": "Implied Zero-Coupon Inflation Curve – 5Y",
        "category": "yield_curves",
        "subcategory": "gilt_inflation",
        "frequency": "daily",
        "description": "Implied zero-coupon inflation term structure, 5-year maturity.",
        "unit": "percent",
    },
    "IUDMIZC": {
        "name": "Implied Zero-Coupon Inflation Curve – 10Y",
        "category": "yield_curves",
        "subcategory": "gilt_inflation",
        "frequency": "daily",
        "description": "Implied zero-coupon inflation term structure, 10-year maturity.",
        "unit": "percent",
    },

    # --- OIS (Overnight Index Swap) Yield Curves ------------------------------
    "IUDZOS2": {
        "name": "OIS Zero-Coupon Spot Rate – 2Y",
        "category": "yield_curves",
        "subcategory": "ois",
        "frequency": "daily",
        "description": "SONIA-based OIS zero-coupon spot rate, 2-year maturity.",
        "unit": "percent",
    },
    "IUDZLT2": {
        "name": "OIS Zero-Coupon Spot Rate – 5Y",
        "category": "yield_curves",
        "subcategory": "ois",
        "frequency": "daily",
        "description": "SONIA-based OIS zero-coupon spot rate, 5-year maturity.",
        "unit": "percent",
    },
    "IUDZLS6": {
        "name": "OIS Zero-Coupon Spot Rate – 10Y",
        "category": "yield_curves",
        "subcategory": "ois",
        "frequency": "daily",
        "description": "SONIA-based OIS zero-coupon spot rate, 10-year maturity.",
        "unit": "percent",
    },
    "IUDZLS7": {
        "name": "OIS Zero-Coupon Spot Rate – 25Y",
        "category": "yield_curves",
        "subcategory": "ois",
        "frequency": "daily",
        "description": "SONIA-based OIS zero-coupon spot rate, 25-year maturity (extended in 2021).",
        "unit": "percent",
    },

    # --- GBP Spot Exchange Rates (XUDL prefix) --------------------------------
    "XUDLUSS": {
        "name": "GBP/USD Spot Rate",
        "category": "exchange_rates",
        "subcategory": "gbp_spot",
        "frequency": "daily",
        "description": "US dollar into sterling – indicative 4pm mid-market rate.",

# ... 文件较长，已截断。总行数：1454
```

### fincept-qt/scripts/boi_data.py

```python
"""
Bank of Israel (BOI) Data Wrapper
Fetches data from the Bank of Israel public APIs.

API References:
  SDMX REST API:
    Base URL: https://edge.boi.gov.il/FusionEdgeServer/sdmx/v2
    Format:   CSV (csvdata) or XML
    Auth:     None required — fully public
    Docs:     https://edge.boi.gov.il/FusionEdgeServer/sdmx/v2/swagger-ui/

  Public JSON API:
    Base URL: https://www.boi.org.il/PublicApi
    Auth:     None required

Dataflows (SDMX):
  EXR  — Exchange rates (ILS per foreign currency)
    Series pattern: RER_{CCY}_ILS  (e.g. RER_USD_ILS, RER_EUR_ILS)
    Special: NER_ILS_BSK_IDX — effective exchange rate index
             NER_ILS_BSK_PCT — percent change in effective rate
    Unit multiplier in column UNIT_MULT:
      0 → rate as-is  (e.g. USD/ILS = 3.12)
      1 → rate ÷ 10   (e.g. LBP)
      2 → rate ÷ 100  (e.g. JPY/ILS reported per 100 JPY)

  Public JSON /GetExchangeRates — latest spot rates with daily change

Key exchange rate series:
  RER_USD_ILS, RER_EUR_ILS, RER_GBP_ILS, RER_JPY_ILS,
  RER_CHF_ILS, RER_AUD_ILS, RER_CAD_ILS, RER_SEK_ILS,
  RER_NOK_ILS, RER_DKK_ILS, RER_ZAR_ILS, RER_JOD_ILS

Returns JSON output for C++ integration.
"""

import sys
import csv
import io
import json
import requests
import traceback
from typing import Dict, Any, List, Optional
from datetime import datetime, date, timedelta, timezone


SDMX_URL        = "https://edge.boi.gov.il/FusionEdgeServer/sdmx/v2"
PUBLIC_URL      = "https://www.boi.org.il/PublicApi"
DEFAULT_TIMEOUT = 30

# All known EXR series codes with their base currency and unit multiplier
EXR_SERIES: Dict[str, Dict[str, Any]] = {
    "RER_USD_ILS": {"base": "USD", "label": "USD/ILS", "multiplier": 1},
    "RER_EUR_ILS": {"base": "EUR", "label": "EUR/ILS", "multiplier": 1},
    "RER_GBP_ILS": {"base": "GBP", "label": "GBP/ILS", "multiplier": 1},
    "RER_JPY_ILS": {"base": "JPY", "label": "JPY/ILS (per 100)", "multiplier": 100},
    "RER_CHF_ILS": {"base": "CHF", "label": "CHF/ILS", "multiplier": 1},
    "RER_AUD_ILS": {"base": "AUD", "label": "AUD/ILS", "multiplier": 1},
    "RER_CAD_ILS": {"base": "CAD", "label": "CAD/ILS", "multiplier": 1},
    "RER_SEK_ILS": {"base": "SEK", "label": "SEK/ILS", "multiplier": 1},
    "RER_NOK_ILS": {"base": "NOK", "label": "NOK/ILS", "multiplier": 1},
    "RER_DKK_ILS": {"base": "DKK", "label": "DKK/ILS", "multiplier": 1},
    "RER_ZAR_ILS": {"base": "ZAR", "label": "ZAR/ILS", "multiplier": 1},
    "RER_JOD_ILS": {"base": "JOD", "label": "JOD/ILS", "multiplier": 1},
    "RER_EGP_ILS": {"base": "EGP", "label": "EGP/ILS", "multiplier": 1},
    "NER_ILS_BSK_IDX": {"base": "BASKET", "label": "Nominal effective exchange rate index", "multiplier": 1},
    "NER_ILS_BSK_PCT":  {"base": "BASKET", "label": "Nominal effective exchange rate % change", "multiplier": 1},
}

MAJOR_SERIES = ["RER_USD_ILS", "RER_EUR_ILS", "RER_GBP_ILS", "RER_JPY_ILS",
                "RER_CHF_ILS", "RER_AUD_ILS", "RER_CAD_ILS"]


# ---------------------------------------------------------------------------
# Error container
# ---------------------------------------------------------------------------

class BOIError:
    def __init__(self, endpoint: str, error: str, status_code: Optional[int] = None):
        self.endpoint    = endpoint
        self.error       = error
        self.status_code = status_code
        self.timestamp   = int(datetime.now(timezone.utc).timestamp())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "success":     False,
            "endpoint":    self.endpoint,
            "error":       self.error,
            "status_code": self.status_code,
            "timestamp":   self.timestamp,
            "type":        "BOIError",
        }


# ---------------------------------------------------------------------------
# Main wrapper
# ---------------------------------------------------------------------------

class BOIWrapper:
    """
    Wrapper for the Bank of Israel public data APIs.

    Exchange rates are ILS (New Israeli Shekel) per 1 unit of foreign currency,
    except JPY which is per 100 JPY (multiplier=100).
    Data is published on Israeli business days (Sun–Thu).
    """

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Fincept-Terminal/4.0.2",
            "Accept":     "text/csv, application/json, */*",
        })

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _sdmx_csv(self, dataflow: str, series_key: str = "",
                  start: Optional[str] = None,
                  end: Optional[str] = None) -> str:
        """Fetch SDMX CSV data from the BOI FusionEdge server."""
        path = f"{SDMX_URL}/data/dataflow/BOI.STATISTICS/{dataflow}/1.0"
        if series_key:
            path = f"{path}/{series_key}"
        params: Dict[str, str] = {"format": "csvdata"}
        if start:
            params["startperiod"] = start
        if end:
            params["endperiod"] = end
        resp = self.session.get(path, params=params, timeout=DEFAULT_TIMEOUT)
        resp.raise_for_status()
        return resp.text

    def _parse_exr_csv(self, text: str) -> List[Dict[str, Any]]:
        """
        Parse BOI EXR CSV into wide-format rows keyed by date.
        Handles UNIT_MULT: obs value is already in ILS per currency unit,
        but for series with multiplier>1 (e.g. JPY), we note it in label.
        """
        reader = csv.DictReader(io.StringIO(text))
        wide: Dict[str, Dict[str, Any]] = {}
        for row in reader:
            series = row.get("SERIES_CODE", "").strip()
            d      = row.get("TIME_PERIOD", "").strip()
            val    = row.get("OBS_VALUE",  "").strip()
            if not d or not series:
                continue
            if d not in wide:
                wide[d] = {"date": d}
            if val not in ("", "..", "N/A"):
                try:
                    wide[d][series] = float(val)
                except ValueError:
                    wide[d][series] = val
        return sorted(wide.values(), key=lambda r: r["date"])

    def _public_json(self, path: str, params: Optional[Dict] = None) -> Any:
        """Fetch from the BOI PublicApi JSON endpoint."""
        url  = f"{PUBLIC_URL}/{path}"
        resp = self.session.get(url, params=params or {}, timeout=DEFAULT_TIMEOUT)
        resp.raise_for_status()
        return resp.json()

    # ------------------------------------------------------------------
    # Public methods
    # ------------------------------------------------------------------

    def get_exchange_rates_today(self) -> Dict[str, Any]:
        """Latest ILS exchange rates from the PublicApi (with daily change %)."""
        try:
            data  = self._public_json("GetExchangeRates")
            rates = data.get("exchangeRates", [])
            result_rows = []
            for r in rates:
                result_rows.append({
                    "currency":    r.get("key"),
                    "rate":        r.get("currentExchangeRate"),
                    "change_pct":  round(r.get("currentChange", 0), 6),
                    "unit":        r.get("unit", 1),

# ... 文件较长，已截断。总行数：378
```

### fincept-qt/scripts/carbon_price_data.py

```python
"""
Carbon Price Data Fetcher
Carbon pricing data: EU ETS prices, California CCA, RGGI allowances, global carbon markets.
"""
import sys
import json
import os
import requests
from typing import Dict, Any, Optional, List

API_KEY = os.environ.get('ICE_API_KEY', '')
BASE_URL = "https://www.theice.com/marketdata/reports"

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=3)
session.mount('https://', adapter)
session.mount('http://', adapter)


def _make_request(endpoint: str, params: Dict = None) -> Any:
    url = f"{BASE_URL}/{endpoint}" if not endpoint.startswith('http') else endpoint
    try:
        response = session.get(url, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except (json.JSONDecodeError, ValueError) as e:
        return {"error": f"JSON decode error: {str(e)}"}


def get_eu_ets_price(start_date: str, end_date: str) -> Any:
    params = {"market": "EU_ETS", "product": "EUA", "startDate": start_date, "endDate": end_date}
    return _make_request("carbon/eu_ets", params)


def get_california_cca(start_date: str, end_date: str) -> Any:
    params = {"market": "CALIFORNIA_CCA", "startDate": start_date, "endDate": end_date}
    return _make_request("carbon/california", params)


def get_rggi_price(start_date: str, end_date: str) -> Any:
    params = {"market": "RGGI", "startDate": start_date, "endDate": end_date}
    return _make_request("carbon/rggi", params)


def get_uk_ets_price(start_date: str, end_date: str) -> Any:
    params = {"market": "UK_ETS", "product": "UKA", "startDate": start_date, "endDate": end_date}
    return _make_request("carbon/uk_ets", params)


def get_voluntary_market_prices(standard: str, start_date: str, end_date: str) -> Any:
    params = {"standard": standard, "startDate": start_date, "endDate": end_date}
    return _make_request("carbon/voluntary", params)


def get_carbon_futures(contract: str, start_date: str, end_date: str) -> Any:
    params = {"contract": contract, "startDate": start_date, "endDate": end_date}
    return _make_request("carbon/futures", params)


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if not args:
        print(json.dumps({"error": "No command provided"}))
        return
    command = args[0]
    result = {"error": f"Unknown command: {command}"}
    if command == "eu_ets":
        start_date = args[1] if len(args) > 1 else "2024-01-01"
        end_date = args[2] if len(args) > 2 else "2024-03-31"
        result = get_eu_ets_price(start_date, end_date)
    elif command == "california":
        start_date = args[1] if len(args) > 1 else "2024-01-01"
        end_date = args[2] if len(args) > 2 else "2024-03-31"
        result = get_california_cca(start_date, end_date)
    elif command == "rggi":
        start_date = args[1] if len(args) > 1 else "2024-01-01"
        end_date = args[2] if len(args) > 2 else "2024-03-31"
        result = get_rggi_price(start_date, end_date)
    elif command == "uk_ets":
        start_date = args[1] if len(args) > 1 else "2024-01-01"
        end_date = args[2] if len(args) > 2 else "2024-03-31"
        result = get_uk_ets_price(start_date, end_date)
    elif command == "voluntary":
        standard = args[1] if len(args) > 1 else "VCS"
        start_date = args[2] if len(args) > 2 else "2024-01-01"
        end_date = args[3] if len(args) > 3 else "2024-03-31"
        result = get_voluntary_market_prices(standard, start_date, end_date)
    elif command == "futures":
        contract = args[1] if len(args) > 1 else "EUA"
        start_date = args[2] if len(args) > 2 else "2024-01-01"
        end_date = args[3] if len(args) > 3 else "2024-03-31"
        result = get_carbon_futures(contract, start_date, end_date)
    print(json.dumps(result))


if __name__ == "__main__":
    main()
```

### fincept-qt/scripts/cboe_data.py

```python
# CBOE (Chicago Board Options Exchange) Data Wrapper
# Based on OpenBB CBOE provider - https://github.com/OpenBB-finance/OpenBB/tree/main/openbb_platform/providers/cboe

import sys
import json
import requests
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Union, Any, Literal
from io import StringIO
import pandas as pd

# CBOE API URLs
BASE_URL = "https://cdn.cboe.com/api/global/delayed_quotes"
EU_BASE_URL = "https://cdn.cboe.com/api/global/european_indices"
US_INDICES_URL = "https://cdn.cboe.com/api/global/delayed_quotes/quotes/all_us_indices.json"
EU_INDICES_URL = "https://cdn.cboe.com/api/global/european_indices/index_quotes/all-indices.json"

# CBOE European Index Constituents (from OpenBB constants)
EU_INDEX_CONSTITUENTS = [
    "BAT20P", "BBE20P", "BCH20P", "BCHM30P", "BDE40P", "BDEM50P", "BDES50P", "BDK25P",
    "BEP50P", "BEPACP", "BEPBUS", "BEPCNC", "BEPCONC", "BEPCONS", "BEPENGY", "BEPFIN",
    "BEPHLTH", "BEPIND", "BEPNEM", "BEPTEC", "BEPTEL", "BEPUTL", "BEPXUKP", "BES35P",
    "BEZ50P", "BEZACP", "BFI25P", "BFR40P", "BFRM20P", "BIE20P", "BIT40P", "BNL25P",
    "BNLM25P", "BNO25G", "BNORD40P", "BPT20P", "BSE30P", "BUK100P", "BUK250P", "BUK350P",
    "BUKAC", "BUKBISP", "BUKBUS", "BUKCNC", "BUKCONC", "BUKCONS", "BUKENGY", "BUKFIN",
    "BUKHI50P", "BUKHLTH", "BUKIND", "BUKLO50P", "BUKMINP", "BUKNEM", "BUKSC", "BUKTEC",
    "BUKTEL", "BUKUTL"
]

# VIX Futures Symbols (from OpenBB)
VIX_SYMBOLS = ["VX_AM", "VX_EOD"]

# Ticker Exceptions (from OpenBB)
TICKER_EXCEPTIONS = ["VIX", "VX", "SPX", "SPEU", "NDX", "NDXE", "RUT", "RUTE"]


class CBOEError:
    """Custom error class for CBOE API errors"""
    def __init__(self, endpoint: str, error: str, status_code: Optional[int] = None):
        self.endpoint = endpoint
        self.error = error
        self.status_code = status_code
        self.timestamp = int(datetime.now().timestamp())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "error": True,
            "endpoint": self.endpoint,
            "message": self.error,
            "status_code": self.status_code,
            "timestamp": self.timestamp
        }


class CBOEDataAPI:
    """CBOE Data API wrapper for modular data fetching"""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Fincept-Terminal/1.0',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        })

        # Cache for directories (24-hour cache like OpenBB)
        self._cache_timeout = 24 * 60 * 60  # 24 hours
        self._cache = {}

    def _is_cache_valid(self, cache_key: str) -> bool:
        """Check if cached data is still valid"""
        if cache_key not in self._cache:
            return False

        cached_time = self._cache[cache_key].get("timestamp", 0)
        current_time = datetime.now().timestamp()
        return (current_time - cached_time) < self._cache_timeout

    def _get_cached_data(self, cache_key: str) -> Optional[pd.DataFrame]:
        """Get cached data if valid"""
        if self._is_cache_valid(cache_key):
            return self._cache[cache_key].get("data")
        return None

    def _set_cache_data(self, cache_key: str, data: pd.DataFrame) -> None:
        """Set cached data with timestamp"""
        self._cache[cache_key] = {
            "data": data,
            "timestamp": datetime.now().timestamp()
        }

    def _make_request(self, url: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """Make HTTP request with error handling"""
        try:
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()

            data = response.json()

            if "error" in data:
                return CBOEError(url, data["error"], response.status_code).to_dict()

            return {"success": True, "data": data}

        except requests.exceptions.RequestException as e:
            return CBOEError(url, str(e), getattr(e.response, 'status_code', None)).to_dict()
        except json.JSONDecodeError as e:
            return CBOEError(url, f"JSON decode error: {str(e)}").to_dict()
        except Exception as e:
            return CBOEError(url, f"Unexpected error: {str(e)}").to_dict()

    def _parse_dataframe_response(self, data: Dict) -> pd.DataFrame:
        """Parse response into DataFrame"""
        if "data" not in data or not isinstance(data["data"], list):
            return pd.DataFrame()

        return pd.DataFrame(data["data"])

    def get_equity_quote(self, symbol: str) -> Dict[str, Any]:
        """Get real-time equity quote with implied volatility data

        Args:
            symbol: Stock symbol (e.g., "AAPL", "MSFT")

        Returns:
            Dict containing equity quote data
        """
        try:
            symbol_clean = symbol.replace("^", "").upper()

            # Determine URL pattern based on ticker exceptions
            if symbol_clean in TICKER_EXCEPTIONS:
                url = f"{BASE_URL}/quotes/_{symbol_clean}.json"
            else:
                url = f"{BASE_URL}/quotes/{symbol_clean}.json"

            result = self._make_request(url)

            if "error" in result:
                return result

            # Extract the quote data from response
            quote_data = result.get("data", {})
            if not quote_data:
                return CBOEError("equity_quote", "No data found for symbol").to_dict()

            return {
                "success": True,
                "data": {
                    "symbol": quote_data.get("symbol"),
                    "current_price": quote_data.get("current_price"),
                    "open": quote_data.get("open"),
                    "high": quote_data.get("high"),
                    "low": quote_data.get("low"),
                    "close": quote_data.get("close"),
                    "volume": quote_data.get("volume"),
                    "bid": quote_data.get("bid"),
                    "ask": quote_data.get("ask"),
                    "bid_size": quote_data.get("bid_size"),
                    "ask_size": quote_data.get("ask_size"),
                    "prev_day_close": quote_data.get("prev_day_close"),
                    "price_change": quote_data.get("price_change"),
                    "price_change_percent": quote_data.get("price_change_percent"),
                    "iv30": quote_data.get("iv30"),
                    "iv30_change": quote_data.get("iv30_change"),
                    "iv30_change_percent": quote_data.get("iv30_change_percent"),
                    "last_trade_time": quote_data.get("last_trade_time"),
                    "security_type": quote_data.get("security_type"),
                    "tick": quote_data.get("tick"),
                    "mkt_data_delay": quote_data.get("mkt_data_delay")
                }
            }

        except Exception as e:
            return CBOEError("equity_quote", str(e)).to_dict()

    def get_equity_historical(self, symbol: str, interval: str = "1d",
                            start_date: Optional[str] = None,
                            end_date: Optional[str] = None,
                            use_cache: bool = True) -> Dict[str, Any]:

# ... 文件较长，已截断。总行数：843
```

### fincept-qt/scripts/cboe_vix_data.py

```python
"""
CBOE VIX Data Fetcher
CBOE VIX historical data and CBOE indices: VIX, VIX3M, VVIX, SKEW directly
from the CBOE CDN CSV endpoint. Parses CSV and converts to JSON.
"""
import sys
import json
import os
import io
import csv
import requests
from typing import Dict, Any, Optional, List

API_KEY = os.environ.get('CBOE_API_KEY', '')
BASE_URL = "https://cdn.cboe.com/api/global/us_indices/daily_prices"

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=3)
session.mount('https://', adapter)
session.mount('http://', adapter)

CBOE_INDICES = {
    "VIX": "VIX_History.csv",
    "VIX3M": "VIX3M_History.csv",
    "VVIX": "VVIX_History.csv",
    "SKEW": "SKEW_History.csv",
    "VXN": "VXN_History.csv",
    "VXO": "VXO_History.csv",
    "GVZ": "GVZ_History.csv",
    "OVX": "OVX_History.csv",
    "TYVIX": "TYVIX_History.csv",
    "SHORTVOL": "ShortTermVol_History.csv",
}


def _make_request(endpoint: str, params: Dict = None) -> Any:
    url = f"{BASE_URL}/{endpoint}" if not endpoint.startswith('http') else endpoint
    try:
        response = session.get(url, params=params, timeout=30)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


def _parse_csv(csv_text: str, start_date: str = None, end_date: str = None) -> Any:
    if isinstance(csv_text, dict):
        return csv_text
    try:
        reader = csv.DictReader(io.StringIO(csv_text))
        rows = []
        for row in reader:
            clean = {k.strip(): v.strip() for k, v in row.items() if k}
            if not any(clean.values()):
                continue
            date_val = clean.get("DATE", clean.get("Date", ""))
            if start_date and date_val and date_val < start_date:
                continue
            if end_date and date_val and date_val > end_date:
                continue
            rows.append(clean)
        return {"data": rows, "count": len(rows)}
    except Exception as e:
        return {"error": f"CSV parse error: {str(e)}"}


def get_vix_history(index_name: str = "VIX") -> Any:
    name = index_name.upper()
    filename = CBOE_INDICES.get(name)
    if not filename:
        return {"error": f"Unknown index: {index_name}. Available: {list(CBOE_INDICES.keys())}"}
    raw = _make_request(filename)
    return _parse_csv(raw)


def get_vix_current() -> Any:
    raw = _make_request("VIX_History.csv")
    parsed = _parse_csv(raw)
    if "data" in parsed and parsed["data"]:
        return {"current": parsed["data"][-1]}
    return parsed


def get_available_indices() -> Any:
    return {"indices": list(CBOE_INDICES.keys()), "count": len(CBOE_INDICES)}


def get_vix_futures_term_structure() -> Any:
    vix_raw = _make_request("VIX_History.csv")
    vix3m_raw = _make_request("VIX3M_History.csv")
    vvix_raw = _make_request("VVIX_History.csv")
    vix_parsed = _parse_csv(vix_raw)
    vix3m_parsed = _parse_csv(vix3m_raw)
    vvix_parsed = _parse_csv(vvix_raw)
    latest_vix = vix_parsed["data"][-1] if "data" in vix_parsed and vix_parsed["data"] else {}
    latest_vix3m = vix3m_parsed["data"][-1] if "data" in vix3m_parsed and vix3m_parsed["data"] else {}
    latest_vvix = vvix_parsed["data"][-1] if "data" in vvix_parsed and vvix_parsed["data"] else {}
    return {
        "term_structure": {
            "VIX_spot": latest_vix,
            "VIX3M_3month": latest_vix3m,
            "VVIX_vol_of_vol": latest_vvix,
        }
    }


def get_index_data(index_name: str, start_date: str = None, end_date: str = None) -> Any:
    name = index_name.upper()
    filename = CBOE_INDICES.get(name)
    if not filename:
        return {"error": f"Unknown index: {index_name}. Available: {list(CBOE_INDICES.keys())}"}
    raw = _make_request(filename)
    return _parse_csv(raw, start_date, end_date)


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if not args:
        print(json.dumps({"error": "No command provided"}))
        return
    command = args[0]
    result = {"error": f"Unknown command: {command}"}

    if command == "history":
        index_name = args[1] if len(args) > 1 else "VIX"
        result = get_vix_history(index_name)
    elif command == "current":
        result = get_vix_current()
    elif command == "indices":
        result = get_available_indices()
    elif command == "term_structure":
        result = get_vix_futures_term_structure()
    elif command == "data":
        index_name = args[1] if len(args) > 1 else "VIX"
        start_date = args[2] if len(args) > 2 else None
        end_date = args[3] if len(args) > 3 else None
        result = get_index_data(index_name, start_date, end_date)

    print(json.dumps(result))


if __name__ == "__main__":
    main()
```

### fincept-qt/scripts/census_data.py

```python
"""
US Census Bureau Data Fetcher
US Census Bureau API: ACS demographics, trade statistics, economic census,
and population estimates.
"""
import sys
import json
import os
import requests
from typing import Dict, Any, Optional, List

API_KEY = os.environ.get('CENSUS_API_KEY', '')
BASE_URL = "https://api.census.gov/data"

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=3)
session.mount('https://', adapter)
session.mount('http://', adapter)


def _make_request(endpoint: str, params: Dict = None) -> Any:
    url = f"{BASE_URL}/{endpoint}" if not endpoint.startswith('http') else endpoint
    if params is None:
        params = {}
    if API_KEY:
        params["key"] = API_KEY
    try:
        response = session.get(url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        if isinstance(data, list) and len(data) > 1:
            headers = data[0]
            rows = data[1:]
            return {"headers": headers, "data": [dict(zip(headers, row)) for row in rows], "count": len(rows)}
        return data
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except (json.JSONDecodeError, ValueError) as e:
        return {"error": f"JSON decode error: {str(e)}"}


def get_acs_data(variables: str = "NAME,B01003_001E", geography: str = "state:*", year: str = "2022") -> Any:
    params = {"get": variables, "for": geography}
    return _make_request(f"{year}/acs/acs5", params)


def get_trade_data(commodity: str = "0101", country: str = "1220", year: str = "2023") -> Any:
    params = {
        "get": "CTY_CODE,CTY_NAME,ALL_VAL_MO,VES_WGT_MO,AIR_WGT_MO",
        "COMM_LVL": "HS10",
        "I_COMMODITY": commodity,
        "CTY_CODE": country,
    }
    return _make_request(f"timeseries/intltrade/imports/hs", params)


def get_population(state: str = "*", year: str = "2023") -> Any:
    params = {
        "get": "NAME,POP,DENSITY",
        "for": f"state:{state}" if state != "*" else "state:*",
    }
    return _make_request(f"{year}/pep/population", params)


def get_housing_data(geography: str = "state:*", year: str = "2022") -> Any:
    params = {
        "get": "NAME,B25001_001E,B25002_002E,B25002_003E,B25003_002E,B25003_003E",
        "for": geography,
    }
    return _make_request(f"{year}/acs/acs5", params)


def get_business_patterns(naics: str = "52", state: str = "*", year: str = "2021") -> Any:
    params = {
        "get": "NAME,NAICS2017,NAICS2017_TTL,EMP,PAYANN,ESTAB",
        "for": f"state:{state}",
        "NAICS2017": naics,
    }
    return _make_request(f"{year}/cbp", params)


def get_datasets() -> Any:
    return _make_request("", {"vintage": "2023"})


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if not args:
        print(json.dumps({"error": "No command provided"}))
        return
    command = args[0]
    result = {"error": f"Unknown command: {command}"}

    if command == "acs":
        variables = args[1] if len(args) > 1 else "NAME,B01003_001E"
        geography = args[2] if len(args) > 2 else "state:*"
        year = args[3] if len(args) > 3 else "2022"
        result = get_acs_data(variables, geography, year)
    elif command == "trade":
        commodity = args[1] if len(args) > 1 else "0101"
        country = args[2] if len(args) > 2 else "1220"
        year = args[3] if len(args) > 3 else "2023"
        result = get_trade_data(commodity, country, year)
    elif command == "population":
        state = args[1] if len(args) > 1 else "*"
        year = args[2] if len(args) > 2 else "2023"
        result = get_population(state, year)
    elif command == "housing":
        geography = args[1] if len(args) > 1 else "state:*"
        year = args[2] if len(args) > 2 else "2022"
        result = get_housing_data(geography, year)
    elif command == "business":
        naics = args[1] if len(args) > 1 else "52"
        state = args[2] if len(args) > 2 else "*"
        year = args[3] if len(args) > 3 else "2021"
        result = get_business_patterns(naics, state, year)
    elif command == "datasets":
        result = get_datasets()

    print(json.dumps(result))


if __name__ == "__main__":
    main()
```

### fincept-qt/scripts/census_international_data.py

```python
"""
Census International Data Fetcher
US Census International Data: population, demographics, economic development indicators for all countries (IDB).
"""
import sys
import json
import os
import requests
from typing import Dict, Any, Optional, List

API_KEY = os.environ.get('CENSUS_API_KEY', '')
BASE_URL = "https://api.census.gov/data/timeseries/idb"

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=3)
session.mount('https://', adapter)
session.mount('http://', adapter)


def _make_request(endpoint: str, params: Dict = None) -> Any:
    url = f"{BASE_URL}/{endpoint}" if not endpoint.startswith('http') else endpoint
    if params is None:
        params = {}
    if API_KEY:
        params["key"] = API_KEY
    try:
        response = session.get(url, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except (json.JSONDecodeError, ValueError) as e:
        return {"error": f"JSON decode error: {str(e)}"}


def get_countries() -> Any:
    return _make_request("1yr", params={"get": "GENC,NAME", "FIPS": "*", "time": "2023"})


def get_population_projection(country: str, year: int = 2023, sex: str = "0") -> Any:
    params = {
        "get": "POP,NAME,GENC",
        "FIPS": country,
        "time": str(year),
        "SEX": sex
    }
    return _make_request("1yr", params=params)


def get_age_structure(country: str, year: int = 2023) -> Any:
    params = {
        "get": "AGE,POP,NAME",
        "FIPS": country,
        "time": str(year),
        "SEX": "0"
    }
    return _make_request("5yr", params=params)


def get_birth_death_rates(country: str, year: int = 2023) -> Any:
    params = {
        "get": "CBR,CDR,NAME,GENC",
        "FIPS": country,
        "time": str(year)
    }
    return _make_request("1yr", params=params)


def get_infant_mortality(country: str, year: int = 2023) -> Any:
    params = {
        "get": "IMR,NAME,GENC",
        "FIPS": country,
        "time": str(year)
    }
    return _make_request("1yr", params=params)


def get_life_expectancy(country: str, year: int = 2023, sex: str = "0") -> Any:
    params = {
        "get": "E0,NAME,GENC",
        "FIPS": country,
        "time": str(year),
        "SEX": sex
    }
    return _make_request("1yr", params=params)


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if not args:
        print(json.dumps({"error": "No command provided"}))
        return
    command = args[0]
    result = {"error": f"Unknown command: {command}"}
    if command == "countries":
        result = get_countries()
    elif command == "projection":
        country = args[1] if len(args) > 1 else "IN"
        year = int(args[2]) if len(args) > 2 else 2023
        sex = args[3] if len(args) > 3 else "0"
        result = get_population_projection(country, year, sex)
    elif command == "age_structure":
        country = args[1] if len(args) > 1 else "IN"
        year = int(args[2]) if len(args) > 2 else 2023
        result = get_age_structure(country, year)
    elif command == "birth_death":
        country = args[1] if len(args) > 1 else "IN"
        year = int(args[2]) if len(args) > 2 else 2023
        result = get_birth_death_rates(country, year)
    elif command == "infant_mortality":
        country = args[1] if len(args) > 1 else "IN"
        year = int(args[2]) if len(args) > 2 else 2023
        result = get_infant_mortality(country, year)
    elif command == "life_expectancy":
        country = args[1] if len(args) > 1 else "IN"
        year = int(args[2]) if len(args) > 2 else 2023
        sex = args[3] if len(args) > 3 else "0"
        result = get_life_expectancy(country, year, sex)
    print(json.dumps(result))


if __name__ == "__main__":
    main()
```

### fincept-qt/scripts/cftc_data.py

```python
# CFTC (Commodity Futures Trading Commission) Data Wrapper
# Modular, fault-tolerant design - each endpoint works independently
# Focus on Commitment of Traders (COT) reports for market sentiment analysis

import sys
import json
import requests
import pandas as pd
from typing import Dict, Any, List, Optional, Union
from datetime import datetime, timedelta
import traceback
import os


class CFTCError:
    """Custom error class for CFTC API errors"""
    def __init__(self, endpoint: str, error: str, status_code: Optional[int] = None):
        self.endpoint = endpoint
        self.error = error
        self.status_code = status_code
        self.timestamp = int(datetime.now().timestamp())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "endpoint": self.endpoint,
            "error": self.error,
            "status_code": self.status_code,
            "timestamp": self.timestamp,
            "type": "CFTCError"
        }


class CFTCDataWrapper:
    """Modular CFTC data wrapper with fault-tolerant endpoints"""

    def __init__(self, app_token: Optional[str] = None):
        self.base_url = "https://publicreporting.cftc.gov"
        self.app_token = app_token or os.environ.get('CFTC_APP_TOKEN', '')
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Fincept Terminal - financial analysis tool (contact@fincept.com)',
            'Accept': 'application/json'
        })

        # Report type mappings
        self.reports_dict = {
            "legacy_futures_only": "6dca-aqww",
            "legacy_combined": "jun7-fc8e",
            "disaggregated_futures_only": "72hh-3qpy",
            "disaggregated_combined": "kh3c-gbw2",
            "tff_futures_only": "gpe5-46if",
            "tff_combined": "yw9f-hn96",
            "supplemental": "4zgm-a668",
        }

        # Report type descriptions
        self.report_descriptions = {
            "legacy": "Legacy reports with commercial, non-commercial and non-reportable classifications",
            "disaggregated": "Disaggregated reports with Producer/Merchant, Swap Dealers, Managed Money classifications",
            "financial": "Traders in Financial Futures (TFF) reports for financial contracts",
            "supplemental": "Supplemental reports for additional market information"
        }

        # Sample COT contract codes (curated from the full list)
        self.cot_codes = {
            # Agricultural
            "corn": "002602",
            "wheat": "001602",
            "soybeans": "005602",
            "cotton": "033661",
            "cocoa": "073732",
            "coffee": "083731",
            "sugar": "080732",
            "live_cattle": "057642",
            "lean_hogs": "054642",

            # Energy
            "crude_oil": "067651",
            "natural_gas": "02365B",
            "gasoline": "111659",
            "heating_oil": "022651",

            # Metals
            "gold": "088691",
            "silver": "084691",
            "copper": "085692",
            "platinum": "076651",
            "palladium": "075651",

            # Financial
            "euro": "099741",
            "jpy": "097741",
            "british_pound": "096742",
            "swiss_franc": "092741",
            "canadian_dollar": "090741",
            "australian_dollar": "232741",

            # Index Futures
            "s&p_500": "13874A",
            "nasdaq_100": "209742",
            "dow_jones": "124603",
            "nikkei": "240741",
            "vix": "1170E1",

            # Interest Rates
            "treasury_bonds": "020601",
            "treasury_notes_2y": "042601",
            "treasury_notes_5y": "044601",
            "treasury_notes_10y": "043602",
            "fed_funds": "045601",

            # Crypto
            "bitcoin": "133741",
            "ether": "146021",

            # Other
            "us_dollar_index": "098662"
        }

        # Common market codes and names for search
        self.market_mappings = {
            "gold": ["GOLD", "088691"],
            "silver": ["SILVER", "084691"],
            "crude": ["CRUDE OIL", "067651"],
            "wti": ["WTI-PHYSICAL", "067651"],
            "brent": ["BRENT LAST DAY", "06765T"],
            "natural_gas": ["HENRY HUB", "02365B"],
            "corn": ["CORN", "002602"],
            "wheat": ["WHEAT-SRW", "001602"],
            "s&p": ["E-MINI S&P 500", "13874A"],
            "sp500": ["E-MINI S&P 500", "13874A"],
            "nasdaq": ["NASDAQ MINI", "209742"],
            "bitcoin": ["BITCOIN", "133741"],
            "btc": ["BITCOIN", "133741"],
            "ether": ["ETHER CASH SETTLED", "146021"],
            "eth": ["ETHER CASH SETTLED", "146021"],
            "euro": ["EURO FX", "099741"],
            "yen": ["JAPANESE YEN", "097741"],
            "pound": ["BRITISH POUND", "096742"],
            "vix": ["VIX FUTURES", "1170E1"],
            "treasury": ["UST BOND", "020601"],
            "dollar": ["USD INDEX", "098662"]
        }

    def _make_request(self, url: str) -> Dict[str, Any]:
        """Make HTTP request with proper error handling"""
        try:
            # Add app token if available
            if self.app_token:
                separator = "&" if "?" in url else "?"
                url = f"{url}{separator}$$app_token={self.app_token}"

            response = self.session.get(url, timeout=30)
            response.raise_for_status()

            data = response.json()

            # Check for API errors
            if isinstance(data, dict) and "error" in data:
                raise Exception(f"CFTC API error: {data['error']}")

            return data

        except requests.exceptions.RequestException as e:
            raise Exception(f"HTTP request failed: {str(e)}")
        except json.JSONDecodeError as e:
            raise Exception(f"JSON decode error: {str(e)}")

    def _format_date(self, date_str: str) -> str:
        """Format date string to CFTC format (YYYY-MM-DD)"""
        try:
            if not date_str:
                return ""

            # Handle different date formats
            if '-' in date_str:
                # Already in YYYY-MM-DD format
                return date_str
            elif len(date_str) == 8 and date_str.isdigit():
                # Convert YYYYMMDD to YYYY-MM-DD

# ... 文件较长，已截断。总行数：727
```

### fincept-qt/scripts/china_data_quality_checks.py

```python
#!/usr/bin/env python3
"""
China Data Quality Checks
Runs integrity/coverage checks on unified China data store.
"""

import io
import json
import sqlite3
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List


UNIFIED_DB = Path(__file__).resolve().parent / "data" / "china" / "unified_store" / "china_data.db"
QUALITY_DIR = Path(__file__).resolve().parent / "data" / "china" / "quality_checks"
REPORT_LATEST = QUALITY_DIR / "report_latest.json"


def _now_ts() -> int:
    return int(datetime.now().timestamp())


def _json(data: Dict[str, Any]) -> None:
    print(json.dumps(data, ensure_ascii=True, default=str))


class ChinaDataQualityChecks:
    def __init__(self) -> None:
        QUALITY_DIR.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def _connect() -> sqlite3.Connection:
        conn = sqlite3.connect(UNIFIED_DB)
        conn.row_factory = sqlite3.Row
        return conn

    def _table_count(self, conn: sqlite3.Connection, table: str) -> int:
        return int(conn.execute(f"SELECT COUNT(1) AS c FROM {table}").fetchone()["c"])

    def _check_market_nulls(self, conn: sqlite3.Connection) -> Dict[str, Any]:
        row = conn.execute(
            """
            SELECT
                SUM(CASE WHEN close IS NULL OR TRIM(close) = '' THEN 1 ELSE 0 END) AS null_close,
                SUM(CASE WHEN volume IS NULL OR TRIM(volume) = '' THEN 1 ELSE 0 END) AS null_volume,
                COUNT(1) AS total
            FROM market_daily
            """
        ).fetchone()
        return {
            "total": int(row["total"] or 0),
            "null_close": int(row["null_close"] or 0),
            "null_volume": int(row["null_volume"] or 0),
        }

    def _check_announcement_fields(self, conn: sqlite3.Connection) -> Dict[str, Any]:
        row = conn.execute(
            """
            SELECT
                SUM(CASE WHEN pdf_url IS NULL OR TRIM(pdf_url) = '' THEN 1 ELSE 0 END) AS missing_pdf_url,
                SUM(CASE WHEN title IS NULL OR TRIM(title) = '' THEN 1 ELSE 0 END) AS missing_title,
                COUNT(1) AS total
            FROM announcements
            """
        ).fetchone()
        return {
            "total": int(row["total"] or 0),
            "missing_pdf_url": int(row["missing_pdf_url"] or 0),
            "missing_title": int(row["missing_title"] or 0),
        }

    def _check_entity_market(self, conn: sqlite3.Connection) -> Dict[str, Any]:
        rows = conn.execute(
            """
            SELECT stock_code, market
            FROM entities
            """
        ).fetchall()
        mismatches: List[Dict[str, str]] = []
        for row in rows:
            code = str(row["stock_code"] or "")
            market = str(row["market"] or "")
            expected = "sse" if code.startswith(("5", "6", "9")) else "szse"
            if market and market != expected:
                mismatches.append({"stock_code": code, "market": market, "expected": expected})
        return {
            "total_entities": len(rows),
            "market_mismatches": len(mismatches),
            "examples": mismatches[:20],
        }

    def _check_pdf_files(self, conn: sqlite3.Connection) -> Dict[str, Any]:
        rows = conn.execute("SELECT entry_key, file_path, sha256 FROM pdf_index").fetchall()
        missing = 0
        bad_hash = 0
        checked = 0
        examples = []
        import hashlib

        for row in rows:
            checked += 1
            file_path = Path(str(row["file_path"] or ""))
            expected_sha = str(row["sha256"] or "")
            if not file_path.exists():
                missing += 1
                if len(examples) < 20:
                    examples.append({"entry_key": row["entry_key"], "issue": "missing_file"})
                continue
            if expected_sha:
                h = hashlib.sha256()
                with file_path.open("rb") as fh:
                    while True:
                        chunk = fh.read(1024 * 1024)
                        if not chunk:
                            break
                        h.update(chunk)
                actual = h.hexdigest()
                if actual != expected_sha:
                    bad_hash += 1
                    if len(examples) < 20:
                        examples.append({"entry_key": row["entry_key"], "issue": "sha256_mismatch"})
        return {
            "checked": checked,
            "missing_files": missing,
            "sha256_mismatch": bad_hash,
            "examples": examples,
        }

    def _check_pdf_text_coverage(self, conn: sqlite3.Connection) -> Dict[str, Any]:
        pdf_count = self._table_count(conn, "pdf_index")
        txt_count = self._table_count(conn, "pdf_texts")
        coverage = 0.0 if pdf_count == 0 else round((txt_count * 100.0) / pdf_count, 2)
        return {"pdf_index_count": pdf_count, "pdf_text_count": txt_count, "coverage_pct": coverage}

    def _check_fundamentals_coverage(self, conn: sqlite3.Connection) -> Dict[str, Any]:
        rows = conn.execute(
            """
            SELECT dataset, fiscal_year, fiscal_quarter, COUNT(1) AS n
            FROM fundamentals_quarterly
            GROUP BY dataset, fiscal_year, fiscal_quarter
            ORDER BY fiscal_year DESC, fiscal_quarter DESC, dataset
            """
        ).fetchall()
        details = [
            {
                "dataset": row["dataset"],
                "fiscal_year": int(row["fiscal_year"]),
                "fiscal_quarter": int(row["fiscal_quarter"]),
                "rows": int(row["n"]),
            }
            for row in rows[:60]
        ]
        return {"group_count": len(rows), "latest_groups": details}

    def run_checks(self) -> Dict[str, Any]:
        if not UNIFIED_DB.exists():
            return {
                "success": False,
                "error": f"Unified DB not found: {UNIFIED_DB}",
                "data": [],
                "timestamp": _now_ts(),
            }

        with self._connect() as conn:
            table_counts = {
                "market_daily": self._table_count(conn, "market_daily"),
                "fundamentals_quarterly": self._table_count(conn, "fundamentals_quarterly"),
                "corporate_actions_adjust": self._table_count(conn, "corporate_actions_adjust"),
                "corporate_actions_dividend": self._table_count(conn, "corporate_actions_dividend"),
                "announcements": self._table_count(conn, "announcements"),
                "entities": self._table_count(conn, "entities"),
                "pdf_index": self._table_count(conn, "pdf_index"),
                "pdf_texts": self._table_count(conn, "pdf_texts"),
            }
            checks = {
                "market_nulls": self._check_market_nulls(conn),
                "announcement_fields": self._check_announcement_fields(conn),
                "entity_market": self._check_entity_market(conn),

# ... 文件较长，已截断。总行数：280
```

### fincept-qt/scripts/china_data_unified_store.py

```python
#!/usr/bin/env python3
"""
China Data Unified Store
Normalizes BaoStock + CNINFO outputs into one SQLite store.
"""

import csv
import io
import json
import sqlite3
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List


DATA_ROOT = Path(__file__).resolve().parent / "data" / "china" / "unified_store"
DB_FILE = DATA_ROOT / "china_data.db"

BAO_DAILY_DIR = Path(__file__).resolve().parent / "data" / "baostock" / "daily_backfill"
BAO_FUND_DIR = Path(__file__).resolve().parent / "data" / "baostock" / "fundamentals_quarterly"
BAO_CA_ADJUST_DIR = (
    Path(__file__).resolve().parent / "data" / "baostock" / "corporate_actions" / "adjust_factor"
)
BAO_CA_DIV_DIR = (
    Path(__file__).resolve().parent / "data" / "baostock" / "corporate_actions" / "dividend"
)

CN_ANN_DIR = (
    Path(__file__).resolve().parent / "data" / "cninfo" / "announcements_incremental" / "records"
)
CN_ENTITIES_JSONL = (
    Path(__file__).resolve().parent / "data" / "cninfo" / "entity_resolver" / "entities.jsonl"
)
CN_PDF_INDEX = Path(__file__).resolve().parent / "data" / "cninfo" / "pdf_downloader" / "index.json"
CN_PDF_TEXT_STATE = (
    Path(__file__).resolve().parent / "data" / "cninfo" / "pdf_text_extractor" / "state.json"
)


def _now_ts() -> int:
    return int(datetime.now().timestamp())


def _json(data: Dict[str, Any]) -> None:
    print(json.dumps(data, ensure_ascii=True, default=str))


class ChinaDataUnifiedStore:
    def __init__(self) -> None:
        DATA_ROOT.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS market_daily (
                    date TEXT NOT NULL,
                    code TEXT NOT NULL,
                    adjustflag TEXT NOT NULL DEFAULT '',
                    open TEXT,
                    high TEXT,
                    low TEXT,
                    close TEXT,
                    volume TEXT,
                    amount TEXT,
                    turn TEXT,
                    pctChg TEXT,
                    raw_json TEXT NOT NULL,
                    PRIMARY KEY (date, code, adjustflag)
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS fundamentals_quarterly (
                    dataset TEXT NOT NULL,
                    source_code TEXT NOT NULL,
                    fiscal_year INTEGER NOT NULL,
                    fiscal_quarter INTEGER NOT NULL,
                    raw_json TEXT NOT NULL,
                    PRIMARY KEY (dataset, source_code, fiscal_year, fiscal_quarter)
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS corporate_actions_adjust (
                    source_code TEXT NOT NULL,
                    dividOperateDate TEXT NOT NULL,
                    raw_json TEXT NOT NULL,
                    PRIMARY KEY (source_code, dividOperateDate)
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS corporate_actions_dividend (
                    source_code TEXT NOT NULL,
                    dividend_year INTEGER NOT NULL,
                    dividOperateDate TEXT NOT NULL,
                    raw_json TEXT NOT NULL,
                    PRIMARY KEY (source_code, dividend_year, dividOperateDate)
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS announcements (
                    announcement_id TEXT PRIMARY KEY,
                    sec_code TEXT,
                    sec_name TEXT,
                    org_id TEXT,
                    category TEXT,
                    announcement_time INTEGER,
                    title TEXT,
                    pdf_url TEXT,
                    raw_json TEXT NOT NULL
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS entities (
                    stock_code TEXT PRIMARY KEY,
                    org_id TEXT,
                    sec_code TEXT,
                    sec_name TEXT,
                    market TEXT,
                    raw_json TEXT NOT NULL
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS pdf_index (
                    entry_key TEXT PRIMARY KEY,
                    announcement_id TEXT,
                    stock_code TEXT,
                    url TEXT,
                    file_path TEXT,
                    sha256 TEXT,
                    size INTEGER,
                    downloaded_at INTEGER,
                    raw_json TEXT NOT NULL
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS pdf_texts (
                    pdf_path TEXT PRIMARY KEY,
                    sha256 TEXT,
                    text_file TEXT,
                    page_count INTEGER,
                    char_count INTEGER,
                    parser TEXT,
                    extracted_at INTEGER,
                    raw_json TEXT NOT NULL
                )
                """
            )
            conn.commit()

    @staticmethod
    def _list_files(directory: Path, pattern: str, max_files: int = 0) -> List[Path]:
        if not directory.exists():
            return []
        files = sorted(directory.glob(pattern))
        if max_files > 0:
            return files[:max_files]
        return files

    def ingest_baostock_daily(self, max_files: int = 0) -> Dict[str, Any]:

# ... 文件较长，已截断。总行数：563
```

### fincept-qt/scripts/climate_trace_data.py

```python
"""
Climate TRACE Data Fetcher
GHG emissions for 350M+ assets globally, country/sector level, 2015-2025.
No API key required (beta).
"""
import sys
import json
import os
import requests
from typing import Dict, Any, Optional, List

BASE_URL = "https://api.climatetrace.org/v4"

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=3)
session.mount('https://', adapter)
session.mount('http://', adapter)
session.headers.update({"Accept": "application/json"})


def _make_request(endpoint: str, params: Dict = None) -> Any:
    """Make HTTP request with error handling."""
    url = f"{BASE_URL}/{endpoint}" if not endpoint.startswith('http') else endpoint
    try:
        response = session.get(url, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except (json.JSONDecodeError, ValueError) as e:
        return {"error": f"JSON decode error: {str(e)}"}


def get_country_emissions(country: str, year: int = 2022) -> Any:
    """Get GHG emissions by country and year.
    country: ISO 3166-1 alpha-3 code (e.g. USA, CHN, DEU, IND, GBR).
    year: 2015-2023.
    """
    params = {"countries": country.upper(), "since": year, "to": year}
    data = _make_request("country/emissions", params=params)
    if isinstance(data, dict) and "error" not in data:
        return {"country": country.upper(), "year": year, "emissions": data}
    return data


def get_sector_emissions(sector: str, year: int = 2022) -> Any:
    """Get GHG emissions by sector and year.
    sector: agriculture, buildings, electricity-generation, fossil-fuel-operations,
            forestry-and-land-use, manufacturing, mineral-extraction, shipping,
            transportation, waste, oil-and-gas-production, etc.
    """
    params = {"sector": sector, "since": year, "to": year}
    data = _make_request("sector/emissions", params=params)
    if isinstance(data, dict) and "error" not in data:
        return {"sector": sector, "year": year, "emissions": data}
    return data


def get_asset_emissions(asset_id: str) -> Any:
    """Get detailed emissions data for a specific tracked asset by ID."""
    data = _make_request(f"asset/{asset_id}/emissions")
    if isinstance(data, dict) and "error" not in data:
        return {"asset_id": asset_id, "data": data}
    return data


def search_assets(name: str = None, country: str = None, sector: str = None, limit: int = 50) -> Any:
    """Search for emissions assets by name, country, and/or sector."""
    params = {"limit": min(limit, 100)}
    if name:
        params["name"] = name
    if country:
        params["countries"] = country.upper()
    if sector:
        params["sector"] = sector
    data = _make_request("assets", params=params)
    if isinstance(data, list):
        return {"assets": data, "count": len(data)}
    elif isinstance(data, dict) and "assets" in data:
        return {"assets": data["assets"], "count": len(data["assets"]), "total": data.get("total")}
    return data


def get_sectors() -> Any:
    """Get list of all available emission sectors."""
    data = _make_request("definitions/sectors")
    if isinstance(data, list):
        return {"sectors": data, "count": len(data)}
    elif isinstance(data, dict) and "sectors" in data:
        return {"sectors": data["sectors"], "count": len(data["sectors"])}
    return data


def get_summary(year: int = 2022) -> Any:
    """Get global emissions summary for a given year across all countries."""
    params = {"since": year, "to": year}
    data = _make_request("country/emissions", params=params)
    if isinstance(data, dict) and "error" not in data:
        return {"year": year, "summary": data}
    return data


def get_country_list() -> Any:
    """Get list of all countries tracked with emissions data."""
    data = _make_request("definitions/countries")
    if isinstance(data, list):
        return {"countries": data, "count": len(data)}
    elif isinstance(data, dict) and "countries" in data:
        return {"countries": data["countries"], "count": len(data["countries"])}
    return data


def get_asset_types() -> Any:
    """Get all asset/sub-sector types tracked in Climate TRACE."""
    data = _make_request("definitions/subsectors")
    if isinstance(data, list):
        return {"asset_types": data, "count": len(data)}
    return data


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if not args:
        print(json.dumps({"error": "No command provided. Available: country, sector, asset, search, sectors, summary, countries, asset_types"}))
        return

    command = args[0]

    if command == "country":
        if len(args) < 2:
            result = {"error": "Usage: country <iso3_code> [year] (e.g. country USA 2022)"}
        else:
            year = int(args[2]) if len(args) > 2 else 2022
            result = get_country_emissions(args[1], year)
    elif command == "sector":
        if len(args) < 2:
            result = {"error": "Usage: sector <sector_name> [year]"}
        else:
            year = int(args[2]) if len(args) > 2 else 2022
            result = get_sector_emissions(args[1], year)
    elif command == "asset":
        if len(args) < 2:
            result = {"error": "Usage: asset <asset_id>"}
        else:
            result = get_asset_emissions(args[1])
    elif command == "search":
        name = args[1] if len(args) > 1 else None
        country = args[2] if len(args) > 2 else None
        sector = args[3] if len(args) > 3 else None
        result = search_assets(name, country, sector)
    elif command == "sectors":
        result = get_sectors()
    elif command == "summary":
        year = int(args[1]) if len(args) > 1 else 2022
        result = get_summary(year)
    elif command == "countries":
        result = get_country_list()
    elif command == "asset_types":
        result = get_asset_types()
    else:
        result = {"error": f"Unknown command: {command}. Available: country, sector, asset, search, sectors, summary, countries, asset_types"}

    print(json.dumps(result))


if __name__ == "__main__":
    main()
```

### fincept-qt/scripts/cme_data.py

```python
"""
CME Data Fetcher
CME Group public market data: futures prices, volumes, open interest, settlement prices.
"""
import sys
import json
import os
import requests
from typing import Dict, Any, Optional, List

API_KEY = os.environ.get('CME_API_KEY', '')
BASE_URL = "https://www.cmegroup.com/api/v1"

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=3)
session.mount('https://', adapter)
session.mount('http://', adapter)


def _make_request(endpoint: str, params: Dict = None) -> Any:
    url = f"{BASE_URL}/{endpoint}" if not endpoint.startswith('http') else endpoint
    try:
        response = session.get(url, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except (json.JSONDecodeError, ValueError) as e:
        return {"error": f"JSON decode error: {str(e)}"}


def get_settlement_prices(product_code: str, date: str) -> Any:
    params = {"productCode": product_code, "date": date}
    return _make_request("settlements/futures", params)


def get_volume(product_code: str, date: str) -> Any:
    params = {"productCode": product_code, "date": date}
    return _make_request("volume/futures", params)


def get_open_interest(product_code: str, date: str) -> Any:
    params = {"productCode": product_code, "date": date}
    return _make_request("openinterest/futures", params)


def get_delayed_quotes(product_code: str) -> Any:
    params = {"productCode": product_code}
    return _make_request("quotes/delayed", params)


def get_product_info(product_code: str) -> Any:
    params = {"productCode": product_code}
    return _make_request("products/futures", params)


def get_calendar(product_code: str, year: str) -> Any:
    params = {"productCode": product_code, "year": year}
    return _make_request("calendar/futures", params)


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if not args:
        print(json.dumps({"error": "No command provided"}))
        return
    command = args[0]
    result = {"error": f"Unknown command: {command}"}
    if command == "settlement":
        product_code = args[1] if len(args) > 1 else "ES"
        date = args[2] if len(args) > 2 else "2024-01-15"
        result = get_settlement_prices(product_code, date)
    elif command == "volume":
        product_code = args[1] if len(args) > 1 else "ES"
        date = args[2] if len(args) > 2 else "2024-01-15"
        result = get_volume(product_code, date)
    elif command == "open_interest":
        product_code = args[1] if len(args) > 1 else "ES"
        date = args[2] if len(args) > 2 else "2024-01-15"
        result = get_open_interest(product_code, date)
    elif command == "quotes":
        product_code = args[1] if len(args) > 1 else "ES"
        result = get_delayed_quotes(product_code)
    elif command == "product":
        product_code = args[1] if len(args) > 1 else "ES"
        result = get_product_info(product_code)
    elif command == "calendar":
        product_code = args[1] if len(args) > 1 else "ES"
        year = args[2] if len(args) > 2 else "2024"
        result = get_calendar(product_code, year)
    print(json.dumps(result))


if __name__ == "__main__":
    main()
```

### fincept-qt/scripts/cnb_data.py

```python
"""
Czech National Bank (CNB) Data Wrapper
Fetches data from the CNB public REST API.

API Reference:
  Base URL:  https://api.cnb.cz/cnbapi
  Format:    JSON
  Auth:      None required — fully public
  Docs:      https://api.cnb.cz/cnbapi/swagger-ui.html

Verified Endpoints:
  GET /exrates/daily?[date=YYYY-MM-DD]&lang=EN
      Daily CZK exchange rate fixing (33 currencies)
  GET /exrates/daily-year?year=YYYY&lang=EN
      All daily fixings for a year
  GET /exrates/daily-currency-month?year=YYYY&month=MM&currencyCode=USD&lang=EN
      Single currency by month
  GET /exrates/monthly-averages-year?year=YYYY&lang=EN
      Monthly average rates for a year
  GET /czeonia/daily?[date=YYYY-MM-DD]&lang=EN
      CZEONIA overnight rate (Czech equivalent of EONIA)
  GET /czeonia/daily-year?year=YYYY&lang=EN
      CZEONIA for a full year
  GET /pribor/daily?[date=YYYY-MM-DD]&lang=EN
      PRIBOR fixing (1D, 1W, 2W, 1M, 2M, 3M, 6M, 9M, 12M)
  GET /pribor/daily-year?year=YYYY&lang=EN
      PRIBOR for a full year
  GET /pribor/daily-year-term?year=YYYY&term=THREE_MONTH&lang=EN
      PRIBOR for a term and year
  GET /omo/daily?[date=YYYY-MM-DD]&lang=EN
      Open market operations (repo, deposit facility)
  GET /forward/daily?[date=YYYY-MM-DD]&lang=EN
      Forward exchange rates (EUR/CZK, USD/CZK)
  GET /fxrates/daily-year?year=YYYY&lang=EN
      FX rates for currencies not in fixing table
  GET /skd/daily?[date=YYYY-MM-DD]&lang=EN
      Short-term government debt (SKD) rates

Returns JSON output for C++ integration.
"""

import sys
import json
import requests
import traceback
from typing import Dict, Any, List, Optional
from datetime import datetime, date, timedelta, timezone


BASE_URL        = "https://api.cnb.cz/cnbapi"
DEFAULT_TIMEOUT = 30
DEFAULT_LANG    = "EN"

# PRIBOR tenor codes
PRIBOR_TERMS = ["ONE_DAY", "ONE_WEEK", "TWO_WEEKS", "ONE_MONTH",
                "TWO_MONTHS", "THREE_MONTHS", "SIX_MONTHS", "NINE_MONTHS", "TWELVE_MONTHS"]

# Main fixing currencies (Table A equivalent)
FIXING_CURRENCIES = [
    "AUD", "BGN", "BRL", "CAD", "CHF", "CNY", "DKK", "EUR", "GBP",
    "HKD", "HRK", "HUF", "IDR", "ILS", "INR", "ISK", "JPY", "KRW",
    "MXN", "MYR", "NOK", "NZD", "PHP", "PLN", "RON", "RSD", "RUB",
    "SEK", "SGD", "THB", "TRY", "USD", "ZAR",
]


# ---------------------------------------------------------------------------
# Error container
# ---------------------------------------------------------------------------

class CNBError:
    def __init__(self, endpoint: str, error: str, status_code: Optional[int] = None):
        self.endpoint    = endpoint
        self.error       = error
        self.status_code = status_code
        self.timestamp   = int(datetime.now(timezone.utc).timestamp())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "success":     False,
            "endpoint":    self.endpoint,
            "error":       self.error,
            "status_code": self.status_code,
            "timestamp":   self.timestamp,
            "type":        "CNBError",
        }


# ---------------------------------------------------------------------------
# Main wrapper
# ---------------------------------------------------------------------------

class CNBWrapper:
    """
    Wrapper for the Czech National Bank (CNB) public REST API.

    Provides exchange rates, PRIBOR, CZEONIA, OMO, and forward rates.
    All rates are expressed as CZK per foreign currency (or per amount).
    No authentication required.
    """

    def __init__(self, lang: str = DEFAULT_LANG):
        self.lang    = lang
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Fincept-Terminal/4.0.2",
            "Accept":     "application/json",
        })

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _get(self, path: str, params: Optional[Dict] = None) -> Any:
        url = f"{BASE_URL}/{path.lstrip('/')}"
        p   = {"lang": self.lang, **(params or {})}
        resp = self.session.get(url, params=p, timeout=DEFAULT_TIMEOUT)
        resp.raise_for_status()
        return resp.json()

    def _safe(self, path: str, label: str,
              params: Optional[Dict] = None) -> Dict[str, Any]:
        try:
            data = self._get(path, params)
            return {
                "success":   True,
                "data":      data,
                "source":    "Czech National Bank",
                "url":       f"{BASE_URL}/{path}",
                "timestamp": int(datetime.now(timezone.utc).timestamp()),
            }
        except requests.exceptions.HTTPError as e:
            sc = e.response.status_code if e.response is not None else None
            return CNBError(label, str(e), sc).to_dict()
        except Exception as e:
            return CNBError(label, str(e)).to_dict()

    def _flatten_rates(self, raw_rates: List[Dict],
                       amount_key: str = "amount") -> List[Dict]:
        """Normalize a rates list to {date, currencyCode: rate_per_unit}."""
        by_date: Dict[str, Dict] = {}
        for r in raw_rates:
            d    = r.get("validFor", "")
            code = r.get("currencyCode", "")
            rate = r.get("rate")
            amt  = r.get(amount_key, 1)
            if not d or not code:
                continue
            by_date.setdefault(d, {"date": d})
            if rate is not None and amt:
                by_date[d][code] = round(rate / amt, 6) if amt != 1 else rate
        return sorted(by_date.values(), key=lambda x: x["date"])

    # ------------------------------------------------------------------
    # Public methods
    # ------------------------------------------------------------------

    def get_exchange_rates(self, rate_date: Optional[str] = None) -> Dict[str, Any]:
        """Daily CZK exchange rate fixing. rate_date: YYYY-MM-DD (default=latest)."""
        params = {}
        if rate_date:
            params["date"] = rate_date
        try:
            raw   = self._get("exrates/daily", params)
            rates = raw.get("rates", [])
            rows  = self._flatten_rates(rates)
            return {
                "success":   True,
                "date":      rates[0].get("validFor", rate_date) if rates else rate_date,
                "data":      rows[0] if rows else {},
                "all_rates": rates,
                "count":     len(rates),
                "note":      "CZK per 1 unit of foreign currency (adjusted for amount)",
                "source":    "Czech National Bank",
                "timestamp": int(datetime.now(timezone.utc).timestamp()),
            }
        except requests.exceptions.HTTPError as e:
            sc = e.response.status_code if e.response is not None else None
            return CNBError("exrates/daily", str(e), sc).to_dict()
        except Exception as e:

# ... 文件较长，已截断。总行数：477
```

### fincept-qt/scripts/cninfo_data.py

```python
#!/usr/bin/env python3
"""
CNINFO Data Wrapper
Provides disclosure search endpoints for Chinese listed companies.
"""

import io
import json
import re
import sys
import time
import warnings
from datetime import datetime
from typing import Any, Dict, Optional

warnings.filterwarnings(
    "ignore",
    message=r"urllib3 .* doesn't match a supported version!",
)

try:
    import pandas as pd
    import requests
    from cninfo import hq as cninfo_hq
    from cninfo import hq_info as cninfo_hq_info
    from cninfo import stock_structure as cninfo_stock_structure
except ImportError as e:
    print(
        json.dumps(
            {
                "success": False,
                "error": f"Missing dependency: {e}",
                "data": [],
            },
            ensure_ascii=True,
        )
    )
    sys.exit(1)


CNINFO_BASE = "http://www.cninfo.com.cn"
TOP_SEARCH_URL = f"{CNINFO_BASE}/new/information/topSearch/query"
ANNOUNCE_URL = f"{CNINFO_BASE}/new/hisAnnouncement/query"
DETAIL_URL = f"{CNINFO_BASE}/new/announcement/bulletin_detail"
STATIC_BASE = "http://static.cninfo.com.cn"


def _now_ts() -> int:
    return int(datetime.now().timestamp())


def _norm_stock_code(code: str) -> str:
    digits = re.sub(r"[^\d]", "", code or "")
    return digits[:6].zfill(6)


def _guess_market(code: str, raw_type: Optional[str]) -> str:
    t = (raw_type or "").lower()
    if "sz" in t:
        return "szse"
    if "sh" in t:
        return "sse"
    if code.startswith("6") or code.startswith("9"):
        return "sse"
    return "szse"


def _to_bool(value: Any) -> bool:
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def _headers() -> Dict[str, str]:
    return {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        ),
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": CNINFO_BASE,
        "Referer": (
            f"{CNINFO_BASE}/new/commonUrl/pageOfSearch?"
            "url=disclosure/list/search&lastPage=index"
        ),
    }


class CNInfoWrapper:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.session.headers.update(_headers())

    @staticmethod
    def _normalize_df(df: pd.DataFrame) -> list:
        if df.empty:
            return []
        for col in df.columns:
            if pd.api.types.is_datetime64_any_dtype(df[col]):
                df[col] = df[col].astype(str)
        df = df.replace([float("inf"), float("-inf")], None)
        df = df.where(pd.notna(df), None)
        return df.to_dict(orient="records")

    def _post(
        self, url: str, data: Dict[str, Any], max_retries: int = 2
    ) -> Dict[str, Any]:
        for attempt in range(max_retries):
            try:
                resp = self.session.post(url, data=data, timeout=20)
                resp.raise_for_status()
                parsed = resp.json()
                return {
                    "success": True,
                    "data": parsed,
                    "timestamp": _now_ts(),
                }
            except Exception as e:  # pragma: no cover - defensive
                if attempt < max_retries - 1:
                    time.sleep(1)
                    continue
                return {
                    "success": False,
                    "error": str(e),
                    "data": [],
                    "timestamp": _now_ts(),
                }
        return {
            "success": False,
            "error": "Max retries exceeded",
            "data": [],
            "timestamp": _now_ts(),
        }

    def _safe_lib_call(self, func, *args, **kwargs) -> Dict[str, Any]:
        try:
            result = func(*args, **kwargs)
            if isinstance(result, pd.DataFrame):
                data = self._normalize_df(result)
                return {
                    "success": True,
                    "data": data,
                    "count": len(data),
                    "timestamp": _now_ts(),
                }
            if isinstance(result, list):
                return {
                    "success": True,
                    "data": result,
                    "count": len(result),
                    "timestamp": _now_ts(),
                }
            if isinstance(result, dict):
                return {
                    "success": True,
                    "data": result,
                    "count": 1,
                    "timestamp": _now_ts(),
                }
            return {
                "success": True,
                "data": result,
                "count": 1,
                "timestamp": _now_ts(),
            }
        except Exception as e:  # pragma: no cover - defensive
            return {
                "success": False,
                "error": str(e),
                "data": [],
                "timestamp": _now_ts(),
            }

    @staticmethod
    def _extract_search_items(raw: Any) -> list:
        if isinstance(raw, list):
            return raw
        if isinstance(raw, dict):
            maybe = raw.get("keyBoardList")
            if isinstance(maybe, list):
                return maybe

# ... 文件较长，已截断。总行数：488
```

### fincept-qt/scripts/cnstats_data.py

```python
#!/usr/bin/env python3
"""
China National Statistics API Wrapper
A COMPLETE wrapper for accessing China's National Bureau of Statistics data.
Provides access to ALL Chinese economic indicators, price indices, industrial data, and more.

This wrapper covers ALL functionality available in the cnstats library:
- Main stats function for querying statistical data
- Hierarchical indicator tree browsing
- Region code listing (provincial and city)
- Complete database code support
- Full API parameter handling

Usage Examples:
    # Get macro economic data (exact cnstats behavior)
    python cnstats_data.py stats A0D01 202201

    # Get provincial data with automatic dbcode detection
    python cnstats_data.py stats A010101 202201 110000

    # Get city data with automatic dbcode detection
    python cnstats_data.py stats A010101 202201 370200

    # List hierarchical indicator tree (exact cnstats behavior)
    python cnstats_data.py --tree --dbcode hgyd

    # List province region codes (exact cnstats behavior)
    python cnstats_data.py --list-regcode

    # List city region codes (exact cnstats behavior)
    python cnstats_data.py --list-regcode --dbcode csnd

Database Codes (COMPLETE):
    - hgyd: 宏观月度数据 (Macro monthly data - default)
    - hgjd: 宏观季度数据 (Macro quarterly data)
    - hgnd: 宏观年度数据 (Macro annual data)
    - fsyd: 分省月度数据 (Provincial monthly data)
    - fsjd: 分省季度数据 (Provincial quarterly data)
    - fsnd: 分省年度数据 (Provincial annual data)
    - csyd: 城市月度数据 (City monthly data)
    - csjd: 城市季度数据 (City quarterly data)
    - csnd: 城市年度数据 (City annual data)

Data Source: China National Bureau of Statistics (http://www.stats.gov.cn/)
Library: cnstats (https://github.com/songjian/cnstats)
"""

import sys
import json
import os
import requests
import time
from datetime import datetime
from typing import Dict, List, Any, Optional, Union

# --- 1. CONFIGURATION ---

# API Configuration
BASE_URL = "https://data.stats.gov.cn/easyquery.htm"
API_HEADERS = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://data.stats.gov.cn/easyquery.htm?cn=A01',
    'Host': 'data.stats.gov.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': '_trs_uv=l0krufmy_6_30qm; JSESSIONID=JkGLaObMfWG3_P3_bNKa59cUydvE_nJDUpJOsskem4S-E-wgJeA7!-2135294552; u=1'
}

# Request configuration
TIMEOUT = 30
MAX_RETRIES = 3

# Database codes mapping
DATABASE_CODES = {
    'hgyd': {'name': '宏观月度数据', 'type': 'macro', 'period': 'monthly'},
    'hgjd': {'name': '宏观季度数据', 'type': 'macro', 'period': 'quarterly'},
    'hgnd': {'name': '宏观年度数据', 'type': 'macro', 'period': 'annual'},
    'fsyd': {'name': '分省月度数据', 'type': 'provincial', 'period': 'monthly'},
    'fsjd': {'name': '分省季度数据', 'type': 'provincial', 'period': 'quarterly'},
    'fsnd': {'name': '分省年度数据', 'type': 'provincial', 'period': 'annual'},
    'csyd': {'name': '城市月度数据', 'type': 'city', 'period': 'monthly'},
    'csjd': {'name': '城市季度数据', 'type': 'city', 'period': 'quarterly'},
    'csnd': {'name': '城市年度数据', 'type': 'city', 'period': 'annual'}
}

# Common indicator codes
COMMON_INDICATORS = {
    'A0D01': '货币供应量',
    'A0101': '价格指数',
    'A010101': '居民消费价格指数',
    'A0201': '工业增加值增长速度',
    'A0301': '能源主要产品产量',
    'A0401': '固定资产投资概况',
    'A0501': '服务业生产指数',
    'A0601': '房地产开发投资情况',
    'A0701': '社会消费品零售总额',
    'A0801': '进出口总额'
}

# --- 2. PRIVATE HELPER FUNCTIONS ---

def _generate_timestamp() -> str:
    """Generate random timestamp for API requests"""
    return str(int(round(time.time() * 1000)))

def easyquery(m: str = 'QueryData', dbcode: str = 'hgyd', rowcode: str = 'zb',
               colcode: str = 'sj', wds: List[Dict] = None, dfwds: List[Dict] = None,
               id: str = None, wdcode: str = None) -> Dict[str, Any]:
    """
    EXACT replica of cnstats easyquery function
    Centralized request handler for China Statistics API

    Args:
        m: API method name (exact parameter name from cnstats)
        dbcode: Database code
        rowcode: Row code
        colcode: Column code
        wds: WDS parameters
        dfwds: DFWDS parameters
        id: ID parameter
        wdcode: WD code parameter

    Returns:
        Raw API response (exact format from cnstats)
    """
    if wds is None:
        wds = []
    if dfwds is None:
        dfwds = []

    try:
        # Exact URL and parameters from cnstats
        url = 'https://data.stats.gov.cn/easyquery.htm'
        obj = {
            'm': m,
            'dbcode': dbcode,
            'rowcode': rowcode,
            'colcode': colcode,
            'wds': json.dumps(wds),
            'dfwds': json.dumps(dfwds),
            'k1': _generate_timestamp(),
            'h': '1',
        }

        if id:
            obj['id'] = id
        if wdcode:
            obj['wdcode'] = wdcode

        # Exact request handling from cnstats
        requests.packages.urllib3.disable_warnings()
        response = requests.post(url, data=obj, headers=API_HEADERS, verify=False, timeout=TIMEOUT)
        response.raise_for_status()

        return response.json()

    except Exception as e:
        return {"returncode": 500, "returndata": {}, "error": str(e)}

# --- 3. EXACT CNSTATS CORE FUNCTIONS ---

def stats(zbcode: str, datestr: str, regcode: str = None, dbcode: str = 'hgyd') -> List[str]:
    """
    EXACT replica of cnstats stats function
    Main function for retrieving statistical data

    Args:
        zbcode: Statistical indicator code
        datestr: Date string (YYYYMM format, supports comma-separated multiple dates)
        regcode: Optional region code for provincial/city data
        dbcode: Database code (default: 'hgyd')

    Returns:
        List of strings in exact cnstats format (for CLI compatibility)
        Each element is space-separated values: [name, code, date/region, value]
    """
    try:
        wds = []
        dfwds = []

# ... 文件较长，已截断。总行数：791
```

### fincept-qt/scripts/coincap_data.py

```python
"""
CoinCap v2 Data Fetcher
1000+ crypto prices, market caps, volumes, exchange data, candles.
No API key required (rate limited). Optional key via COINCAP_API_KEY.
"""
import sys
import json
import os
import requests
from typing import Dict, Any, Optional, List

API_KEY = os.environ.get('COINCAP_API_KEY', '')
BASE_URL = "https://api.coincap.io/v2"

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=3)
session.mount('https://', adapter)
session.mount('http://', adapter)

if API_KEY:
    session.headers.update({"Authorization": f"Bearer {API_KEY}"})


def _make_request(endpoint: str, params: Dict = None) -> Any:
    """Make HTTP request with error handling."""
    url = f"{BASE_URL}/{endpoint}" if not endpoint.startswith('http') else endpoint
    try:
        response = session.get(url, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except (json.JSONDecodeError, ValueError) as e:
        return {"error": f"JSON decode error: {str(e)}"}


def get_assets(limit: int = 100, offset: int = 0) -> Any:
    """Get paginated list of crypto assets with market data."""
    params = {"limit": limit, "offset": offset}
    data = _make_request("assets", params=params)
    if isinstance(data, dict) and "data" in data:
        return {"assets": data["data"], "timestamp": data.get("timestamp"), "count": len(data["data"])}
    return data


def get_asset(asset_id: str) -> Any:
    """Get detailed data for a specific asset by ID (e.g. bitcoin, ethereum)."""
    data = _make_request(f"assets/{asset_id}")
    if isinstance(data, dict) and "data" in data:
        return data["data"]
    return data


def get_asset_history(asset_id: str, interval: str = "d1") -> Any:
    """Get price history for an asset. Intervals: m1,m5,m15,m30,h1,h2,h6,h12,d1."""
    params = {"interval": interval}
    data = _make_request(f"assets/{asset_id}/history", params=params)
    if isinstance(data, dict) and "data" in data:
        history = data["data"]
        return {"asset_id": asset_id, "interval": interval, "history": history, "count": len(history)}
    return data


def get_markets(asset_id: str) -> Any:
    """Get exchange markets for a specific asset."""
    params = {"limit": 100}
    data = _make_request(f"assets/{asset_id}/markets", params=params)
    if isinstance(data, dict) and "data" in data:
        return {"asset_id": asset_id, "markets": data["data"], "count": len(data["data"])}
    return data


def get_exchanges() -> Any:
    """Get list of exchanges with volume data."""
    params = {"limit": 100}
    data = _make_request("exchanges", params=params)
    if isinstance(data, dict) and "data" in data:
        return {"exchanges": data["data"], "count": len(data["data"])}
    return data


def get_rates() -> Any:
    """Get current conversion rates against USD for all supported currencies."""
    data = _make_request("rates")
    if isinstance(data, dict) and "data" in data:
        return {"rates": data["data"], "timestamp": data.get("timestamp"), "count": len(data["data"])}
    return data


def get_candles(exchange_id: str, base_id: str, quote_id: str, interval: str = "d1") -> Any:
    """Get OHLCV candles for a trading pair on an exchange."""
    params = {
        "exchange": exchange_id,
        "interval": interval,
        "baseId": base_id,
        "quoteId": quote_id,
        "limit": 200
    }
    data = _make_request("candles", params=params)
    if isinstance(data, dict) and "data" in data:
        return {"exchange": exchange_id, "base": base_id, "quote": quote_id, "interval": interval, "candles": data["data"]}
    return data


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if not args:
        print(json.dumps({"error": "No command provided. Available: assets, asset, history, markets, exchanges, rates, candles"}))
        return

    command = args[0]

    if command == "assets":
        limit = int(args[1]) if len(args) > 1 else 100
        offset = int(args[2]) if len(args) > 2 else 0
        result = get_assets(limit, offset)
    elif command == "asset":
        if len(args) < 2:
            result = {"error": "Usage: asset <asset_id> (e.g. bitcoin, ethereum)"}
        else:
            result = get_asset(args[1])
    elif command == "history":
        if len(args) < 2:
            result = {"error": "Usage: history <asset_id> [interval] (intervals: m1,m5,m15,m30,h1,h2,h6,h12,d1)"}
        else:
            interval = args[2] if len(args) > 2 else "d1"
            result = get_asset_history(args[1], interval)
    elif command == "markets":
        if len(args) < 2:
            result = {"error": "Usage: markets <asset_id>"}
        else:
            result = get_markets(args[1])
    elif command == "exchanges":
        result = get_exchanges()
    elif command == "rates":
        result = get_rates()
    elif command == "candles":
        if len(args) < 4:
            result = {"error": "Usage: candles <exchange_id> <base_id> <quote_id> [interval]"}
        else:
            interval = args[4] if len(args) > 4 else "d1"
            result = get_candles(args[1], args[2], args[3], interval)
    else:
        result = {"error": f"Unknown command: {command}. Available: assets, asset, history, markets, exchanges, rates, candles"}

    print(json.dumps(result))


if __name__ == "__main__":
    main()
```

### fincept-qt/scripts/coinglass_data.py

```python
"""
CoinGlass Data Fetcher
Crypto futures open interest, funding rates, liquidations, long/short ratios across 30+ exchanges.
"""
import sys
import json
import os
import requests
from typing import Dict, Any, Optional, List

API_KEY = os.environ.get('COINGLASS_API_KEY', '')
BASE_URL = "https://open-api.coinglass.com/public/v2"

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=3)
session.mount('https://', adapter)
session.mount('http://', adapter)

def _make_request(endpoint: str, params: Dict = None) -> Any:
    url = f"{BASE_URL}/{endpoint}" if not endpoint.startswith('http') else endpoint
    try:
        headers = {"coinglassSecret": API_KEY}
        response = session.get(url, params=params, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except (json.JSONDecodeError, ValueError) as e:
        return {"error": f"JSON decode error: {str(e)}"}

def get_open_interest(symbol: str = "BTC", exchange: str = None) -> Any:
    params = {"symbol": symbol}
    if exchange:
        params["exchange"] = exchange
    return _make_request("openInterest", params)

def get_funding_rate(symbol: str = "BTC", exchange: str = None) -> Any:
    params = {"symbol": symbol}
    if exchange:
        params["exchange"] = exchange
    return _make_request("funding", params)

def get_liquidations(symbol: str = "BTC", exchange: str = None, time_range: str = "h4") -> Any:
    params = {"symbol": symbol, "timeType": time_range}
    if exchange:
        params["exchange"] = exchange
    return _make_request("liquidation/detail/chart", params)

def get_long_short_ratio(symbol: str = "BTC", exchange: str = "Binance", period: str = "h4") -> Any:
    params = {"symbol": symbol, "exchangeName": exchange, "period": period}
    return _make_request("longShort", params)

def get_aggregated_oi(symbol: str = "BTC") -> Any:
    return _make_request("openInterest/aggregated-history", {"symbol": symbol})

def get_futures_markets() -> Any:
    return _make_request("exchange/info", {})

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if not args:
        print(json.dumps({"error": "No command provided"}))
        return
    command = args[0]
    result = {"error": f"Unknown command: {command}"}
    if command == "open_interest":
        symbol = args[1] if len(args) > 1 else "BTC"
        exchange = args[2] if len(args) > 2 else None
        result = get_open_interest(symbol, exchange)
    elif command == "funding":
        symbol = args[1] if len(args) > 1 else "BTC"
        exchange = args[2] if len(args) > 2 else None
        result = get_funding_rate(symbol, exchange)
    elif command == "liquidations":
        symbol = args[1] if len(args) > 1 else "BTC"
        exchange = args[2] if len(args) > 2 else None
        time_range = args[3] if len(args) > 3 else "h4"
        result = get_liquidations(symbol, exchange, time_range)
    elif command == "long_short":
        symbol = args[1] if len(args) > 1 else "BTC"
        exchange = args[2] if len(args) > 2 else "Binance"
        period = args[3] if len(args) > 3 else "h4"
        result = get_long_short_ratio(symbol, exchange, period)
    elif command == "aggregated_oi":
        symbol = args[1] if len(args) > 1 else "BTC"
        result = get_aggregated_oi(symbol)
    elif command == "markets":
        result = get_futures_markets()
    print(json.dumps(result))

if __name__ == "__main__":
    main()
```

### fincept-qt/scripts/coinmarketcap_data.py

```python
"""
CoinMarketCap Data Fetcher
CoinMarketCap Basic tier: top crypto listings, prices, market caps, categories,
and global metrics via the CoinMarketCap Pro API.
"""
import sys
import json
import os
import requests
from typing import Dict, Any, Optional, List

API_KEY = os.environ.get('CMC_API_KEY', '')
BASE_URL = "https://pro-api.coinmarketcap.com/v1"

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=3)
session.mount('https://', adapter)
session.mount('http://', adapter)


def _make_request(endpoint: str, params: Dict = None) -> Any:
    url = f"{BASE_URL}/{endpoint}" if not endpoint.startswith('http') else endpoint
    if params is None:
        params = {}
    headers = {"X-CMC_PRO_API_KEY": API_KEY, "Accept": "application/json"}
    try:
        response = session.get(url, params=params, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except (json.JSONDecodeError, ValueError) as e:
        return {"error": f"JSON decode error: {str(e)}"}


def get_listings_latest(limit: str = "100", convert: str = "USD") -> Any:
    params = {
        "start": "1",
        "limit": limit,
        "convert": convert.upper(),
        "sort": "market_cap",
        "sort_dir": "desc",
    }
    return _make_request("cryptocurrency/listings/latest", params)


def get_quotes_latest(symbols: str, convert: str = "USD") -> Any:
    params = {"symbol": symbols.upper(), "convert": convert.upper()}
    return _make_request("cryptocurrency/quotes/latest", params)


def get_global_metrics(convert: str = "USD") -> Any:
    params = {"convert": convert.upper()}
    return _make_request("global-metrics/quotes/latest", params)


def get_categories(limit: str = "100") -> Any:
    params = {"start": "1", "limit": limit}
    return _make_request("cryptocurrency/categories", params)


def get_ohlcv_historical(symbol: str, time_start: str = None, time_end: str = None, convert: str = "USD") -> Any:
    params = {"symbol": symbol.upper(), "convert": convert.upper()}
    if time_start:
        params["time_start"] = time_start
    if time_end:
        params["time_end"] = time_end
    return _make_request("cryptocurrency/ohlcv/historical", params)


def get_trending(limit: str = "10") -> Any:
    params = {"start": "1", "limit": limit}
    return _make_request("cryptocurrency/trending/latest", params)


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if not args:
        print(json.dumps({"error": "No command provided"}))
        return
    command = args[0]
    result = {"error": f"Unknown command: {command}"}

    if command == "listings":
        limit = args[1] if len(args) > 1 else "100"
        convert = args[2] if len(args) > 2 else "USD"
        result = get_listings_latest(limit, convert)
    elif command == "quotes":
        symbols = args[1] if len(args) > 1 else "BTC,ETH"
        convert = args[2] if len(args) > 2 else "USD"
        result = get_quotes_latest(symbols, convert)
    elif command == "global":
        convert = args[1] if len(args) > 1 else "USD"
        result = get_global_metrics(convert)
    elif command == "categories":
        limit = args[1] if len(args) > 1 else "100"
        result = get_categories(limit)
    elif command == "ohlcv":
        symbol = args[1] if len(args) > 1 else "BTC"
        time_start = args[2] if len(args) > 2 else None
        time_end = args[3] if len(args) > 3 else None
        convert = args[4] if len(args) > 4 else "USD"
        result = get_ohlcv_historical(symbol, time_start, time_end, convert)
    elif command == "trending":
        limit = args[1] if len(args) > 1 else "10"
        result = get_trending(limit)

    print(json.dumps(result))


if __name__ == "__main__":
    main()
```

### fincept-qt/scripts/coinpaprika_data.py

```python
"""
CoinPaprika Data Fetcher
71000+ assets, market caps, OHLCV, exchanges, events.
No API key required for public endpoints.
"""
import sys
import json
import os
import requests
from typing import Dict, Any, Optional, List

BASE_URL = "https://api.coinpaprika.com/v1"

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=3)
session.mount('https://', adapter)
session.mount('http://', adapter)


def _make_request(endpoint: str, params: Dict = None) -> Any:
    """Make HTTP request with error handling."""
    url = f"{BASE_URL}/{endpoint}" if not endpoint.startswith('http') else endpoint
    try:
        response = session.get(url, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except (json.JSONDecodeError, ValueError) as e:
        return {"error": f"JSON decode error: {str(e)}"}


def get_global() -> Any:
    """Get global cryptocurrency market overview."""
    data = _make_request("global")
    return data


def get_coins(limit: int = 100) -> Any:
    """Get list of all coins with basic info."""
    data = _make_request("coins")
    if isinstance(data, list):
        return {"coins": data[:limit], "total_count": len(data)}
    return data


def get_coin(coin_id: str) -> Any:
    """Get detailed info for a specific coin (e.g. btc-bitcoin, eth-ethereum)."""
    return _make_request(f"coins/{coin_id}")


def get_coin_ohlcv(coin_id: str, start: str = None, end: str = None, limit: int = 365) -> Any:
    """Get OHLCV daily data for a coin.
    start/end format: YYYY-MM-DD. Default: last 365 days.
    """
    params = {"limit": min(limit, 366)}
    if start:
        params["start"] = start
    if end:
        params["end"] = end
    data = _make_request(f"coins/{coin_id}/ohlcv/historical", params=params)
    if isinstance(data, list):
        return {"coin_id": coin_id, "ohlcv": data, "count": len(data)}
    return data


def get_coin_today_ohlcv(coin_id: str, quote: str = "usd") -> Any:
    """Get today's OHLCV for a coin."""
    params = {"quote": quote}
    data = _make_request(f"coins/{coin_id}/ohlcv/today", params=params)
    if isinstance(data, list):
        return {"coin_id": coin_id, "quote": quote, "today": data}
    return data


def get_exchanges() -> Any:
    """Get list of all exchanges with volume data."""
    data = _make_request("exchanges")
    if isinstance(data, list):
        return {"exchanges": data[:100], "total_count": len(data)}
    return data


def get_exchange(exchange_id: str) -> Any:
    """Get detailed data for a specific exchange (e.g. binance, coinbase-pro)."""
    return _make_request(f"exchanges/{exchange_id}")


def get_markets(coin_id: str) -> Any:
    """Get markets (trading pairs) for a specific coin."""
    params = {"quotes": "USD,BTC"}
    data = _make_request(f"coins/{coin_id}/markets", params=params)
    if isinstance(data, list):
        return {"coin_id": coin_id, "markets": data[:50], "count": len(data)}
    return data


def get_tickers(limit: int = 100, quotes: str = "USD") -> Any:
    """Get price tickers for top coins with market data."""
    params = {"limit": min(limit, 250), "quotes": quotes}
    data = _make_request("tickers", params=params)
    if isinstance(data, list):
        return {"tickers": data, "count": len(data)}
    return data


def get_coin_events(coin_id: str) -> Any:
    """Get upcoming and past events for a coin."""
    data = _make_request(f"coins/{coin_id}/events")
    if isinstance(data, list):
        return {"coin_id": coin_id, "events": data, "count": len(data)}
    return data


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if not args:
        print(json.dumps({"error": "No command provided. Available: global, coins, coin, ohlcv, today_ohlcv, exchanges, exchange, markets, tickers, events"}))
        return

    command = args[0]

    if command == "global":
        result = get_global()
    elif command == "coins":
        limit = int(args[1]) if len(args) > 1 else 100
        result = get_coins(limit)
    elif command == "coin":
        if len(args) < 2:
            result = {"error": "Usage: coin <coin_id> (e.g. btc-bitcoin, eth-ethereum)"}
        else:
            result = get_coin(args[1])
    elif command == "ohlcv":
        if len(args) < 2:
            result = {"error": "Usage: ohlcv <coin_id> [start_date] [end_date] [limit]"}
        else:
            start = args[2] if len(args) > 2 else None
            end = args[3] if len(args) > 3 else None
            limit = int(args[4]) if len(args) > 4 else 365
            result = get_coin_ohlcv(args[1], start, end, limit)
    elif command == "today_ohlcv":
        if len(args) < 2:
            result = {"error": "Usage: today_ohlcv <coin_id> [quote]"}
        else:
            quote = args[2] if len(args) > 2 else "usd"
            result = get_coin_today_ohlcv(args[1], quote)
    elif command == "exchanges":
        result = get_exchanges()
    elif command == "exchange":
        if len(args) < 2:
            result = {"error": "Usage: exchange <exchange_id> (e.g. binance, coinbase-pro)"}
        else:
            result = get_exchange(args[1])
    elif command == "markets":
        if len(args) < 2:
            result = {"error": "Usage: markets <coin_id>"}
        else:
            result = get_markets(args[1])
    elif command == "tickers":
        limit = int(args[1]) if len(args) > 1 else 100
        quotes = args[2] if len(args) > 2 else "USD"
        result = get_tickers(limit, quotes)
    elif command == "events":
        if len(args) < 2:
            result = {"error": "Usage: events <coin_id>"}
        else:
            result = get_coin_events(args[1])
    else:
        result = {"error": f"Unknown command: {command}. Available: global, coins, coin, ohlcv, today_ohlcv, exchanges, exchange, markets, tickers, events"}

    print(json.dumps(result))


if __name__ == "__main__":
    main()
```

### fincept-qt/scripts/comex_data.py

```python
"""
COMEX Data Fetcher
COMEX metals futures (Gold, Silver, Copper) via public CME/COMEX data: settlement prices, volume, open interest.
"""
import sys
import json
import os
import requests
from typing import Dict, Any, Optional, List

API_KEY = os.environ.get('CME_API_KEY', '')
BASE_URL = "https://www.cmegroup.com/CmeWS/mvc/Settlements/futures/settlements"

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=3)
session.mount('https://', adapter)
session.mount('http://', adapter)


def _make_request(endpoint: str, params: Dict = None) -> Any:
    url = f"{BASE_URL}/{endpoint}" if not endpoint.startswith('http') else endpoint
    try:
        response = session.get(url, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except (json.JSONDecodeError, ValueError) as e:
        return {"error": f"JSON decode error: {str(e)}"}


def get_gold_futures(date: str) -> Any:
    params = {"productCode": "GC", "date": date, "exchange": "COMEX"}
    return _make_request("GC/P", params)


def get_silver_futures(date: str) -> Any:
    params = {"productCode": "SI", "date": date, "exchange": "COMEX"}
    return _make_request("SI/P", params)


def get_copper_futures(date: str) -> Any:
    params = {"productCode": "HG", "date": date, "exchange": "COMEX"}
    return _make_request("HG/P", params)


def get_platinum_futures(date: str) -> Any:
    params = {"productCode": "PL", "date": date, "exchange": "NYMEX"}
    return _make_request("PL/P", params)


def get_palladium_futures(date: str) -> Any:
    params = {"productCode": "PA", "date": date, "exchange": "NYMEX"}
    return _make_request("PA/P", params)


def get_metals_settlement(metal: str, date: str) -> Any:
    metal_map = {
        "gold": "GC", "silver": "SI", "copper": "HG",
        "platinum": "PL", "palladium": "PA"
    }
    product_code = metal_map.get(metal.lower(), metal.upper())
    params = {"productCode": product_code, "date": date, "exchange": "COMEX"}
    return _make_request(f"{product_code}/P", params)


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if not args:
        print(json.dumps({"error": "No command provided"}))
        return
    command = args[0]
    result = {"error": f"Unknown command: {command}"}
    if command == "gold":
        date = args[1] if len(args) > 1 else "2024-01-15"
        result = get_gold_futures(date)
    elif command == "silver":
        date = args[1] if len(args) > 1 else "2024-01-15"
        result = get_silver_futures(date)
    elif command == "copper":
        date = args[1] if len(args) > 1 else "2024-01-15"
        result = get_copper_futures(date)
    elif command == "platinum":
        date = args[1] if len(args) > 1 else "2024-01-15"
        result = get_platinum_futures(date)
    elif command == "palladium":
        date = args[1] if len(args) > 1 else "2024-01-15"
        result = get_palladium_futures(date)
    elif command == "settlement":
        metal = args[1] if len(args) > 1 else "gold"
        date = args[2] if len(args) > 2 else "2024-01-15"
        result = get_metals_settlement(metal, date)
    print(json.dumps(result))


if __name__ == "__main__":
    main()
```

### fincept-qt/scripts/congress_gov_data.py

```python
"""
Congress.gov Data Fetcher
Modular, fault-tolerant wrapper for US Congressional data based on OpenBB congress_gov provider
Sources: Congress.gov API
Each endpoint works independently with isolated error handling
"""

import sys
import json
import requests
import asyncio
import base64
from datetime import datetime, timedelta, date
from typing import Dict, Any, Optional, List, Union
from io import BytesIO
import re
import math

# Congress.gov API Constants
BASE_URL = "https://api.congress.gov/v3/"
BILL_TYPES = ["hr", "s", "hjres", "sjres", "hconres", "sconres", "hres", "sres"]

BILL_TYPE_OPTIONS = [
    {"label": "House Bill", "value": "hr"},
    {"label": "Senate Bill", "value": "s"},
    {"label": "House Joint Resolution", "value": "hjres"},
    {"label": "Senate Joint Resolution", "value": "sjres"},
    {"label": "House Concurrent Resolution", "value": "hconres"},
    {"label": "Senate Concurrent Resolution", "value": "sconres"},
    {"label": "House Simple Resolution", "value": "hres"},
    {"label": "Senate Simple Resolution", "value": "sres"},
]

class CongressGovError:
    """Error handling wrapper for Congress.gov API responses"""
    def __init__(self, endpoint: str, error: str, status_code: Optional[int] = None):
        self.endpoint = endpoint
        self.error = error
        self.status_code = status_code
        self.timestamp = int(datetime.now().timestamp())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "success": False,
            "error": self.error,
            "endpoint": self.endpoint,
            "status_code": self.status_code,
            "timestamp": self.timestamp
        }

class CongressGovWrapper:
    """Modular Congress.gov API wrapper with fault tolerance"""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get('CONGRESS_GOV_API_KEY', '')
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Fincept-Terminal/1.0',
            'Accept': 'application/json'
        })

    def _make_request(self, url: str, method: str = 'GET', params: Optional[Dict] = None) -> Dict[str, Any]:
        """Make HTTP request with comprehensive error handling"""
        try:
            if not self.api_key:
                return {"error": "Congress.gov API key not configured. Please set CONGRESS_GOV_API_KEY environment variable.", "api_key_required": True}

            # Add API key to URL
            if '?' in url:
                url += f"&api_key={self.api_key}"
            else:
                url += f"?api_key={self.api_key}"

            response = self.session.request(method=method, url=url, params=params, timeout=30)
            response.raise_for_status()

            try:
                data = response.json()
                return {"success": True, "data": data}
            except json.JSONDecodeError:
                return {"error": "Invalid JSON response", "json_error": True}

        except requests.exceptions.Timeout:
            return {"error": "Request timeout", "timeout": True, "status_code": None}
        except requests.exceptions.ConnectionError:
            return {"error": "Connection error", "connection_error": True, "status_code": None}
        except requests.exceptions.HTTPError as e:
            if response.status_code == 401:
                return {"error": "Invalid API key", "auth_error": True, "status_code": response.status_code}
            elif response.status_code == 403:
                return {"error": "Rate limit exceeded", "rate_limit_error": True, "status_code": response.status_code}
            elif response.status_code == 404:
                return {"error": "Resource not found", "not_found": True, "status_code": response.status_code}
            else:
                return {"error": f"HTTP error: {e}", "http_error": True, "status_code": response.status_code}
        except requests.exceptions.RequestException as e:
            return {"error": f"Request error: {e}", "request_error": True, "status_code": None}
        except Exception as e:
            return {"error": f"Unexpected error: {e}", "general_error": True, "status_code": None}

    def _year_to_congress(self, year: int) -> int:
        """Map a year (1935-present) to the corresponding U.S. Congress number."""
        if year < 1935:
            raise ValueError("Year must be 1935 or later.")
        # 74th Congress started in 1935
        congress_number = 74 + ((year - 1935) // 2)
        return congress_number

    def _get_congress_from_params(self, start_date: Optional[str] = None,
                                end_date: Optional[str] = None,
                                congress: Optional[int] = None) -> int:
        """Determine congress number from various parameters"""
        if congress:
            return congress

        current_year = datetime.now().year
        current_congress = self._year_to_congress(current_year)

        if start_date and not end_date:
            try:
                start_year = datetime.fromisoformat(start_date).year
                return self._year_to_congress(start_year)
            except:
                return current_congress
        elif end_date and not start_date:
            try:
                end_year = datetime.fromisoformat(end_date).year
                return self._year_to_congress(end_year)
            except:
                return current_congress
        else:
            return current_congress

    # ===== CONGRESS BILLS ENDPOINT =====

    def get_congress_bills(self, congress: Optional[int] = None,
                          bill_type: Optional[str] = None,
                          start_date: Optional[str] = None,
                          end_date: Optional[str] = None,
                          limit: Optional[int] = None,
                          offset: Optional[int] = 0,
                          sort_by: str = "desc",
                          get_all: bool = False) -> Dict[str, Any]:
        """
        Get US Congressional bills

        Args:
            congress: Congress number (e.g., 118 for 118th Congress)
            bill_type: Bill type (hr, s, hjres, sjres, hconres, sconres, hres, sres)
            start_date: Start date in ISO format (YYYY-MM-DD)
            end_date: End date in ISO format (YYYY-MM-DD)
            limit: Maximum number of bills to return (default 100, max 250)
            offset: Number of results to skip
            sort_by: Sort order (asc/desc)
            get_all: If True, fetch all bills (ignores limit)
        """
        try:
            if bill_type and bill_type not in BILL_TYPES:
                return CongressGovError('congress_bills', f'Invalid bill_type: {bill_type}. Must be one of: {", ".join(BILL_TYPES)}').to_dict()

            # Determine congress number
            congress_num = self._get_congress_from_params(start_date, end_date, congress)

            # Build URL
            if bill_type:
                url = f"{BASE_URL}bill/{congress_num}/{bill_type}"
            else:
                url = f"{BASE_URL}bill/{congress_num}"

            # Build query parameters
            params = []

            if start_date:
                params.append(f"fromDateTime={start_date}T00:00:00Z")
            if end_date:
                params.append(f"toDateTime={end_date}T23:59:59Z")

            if get_all and bill_type and congress_num:
                # Fetch all bills for this type and congress
                return self._get_all_bills_by_type(congress_num, bill_type, start_date, end_date)

# ... 文件较长，已截断。总行数：850
```

### fincept-qt/scripts/copernicus_data.py

```python
"""
Copernicus Climate Change Service (C3S) Data Fetcher
Provides ERA5 reanalysis data, seasonal forecasts, climate indicators,
sea level data, and temperature anomalies via the CDS API.
"""
import sys
import json
import os
import requests
from typing import Dict, Any, Optional, List

API_KEY = os.environ.get('COPERNICUS_API_KEY', '')
BASE_URL = "https://cds.climate.copernicus.eu/api/v2"

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=3)
session.mount('https://', adapter)
session.mount('http://', adapter)


def _make_request(endpoint: str, params: Dict = None) -> Any:
    url = f"{BASE_URL}/{endpoint}" if not endpoint.startswith('http') else endpoint
    headers = {}
    if API_KEY:
        headers["Authorization"] = f"Bearer {API_KEY}"
    try:
        response = session.get(url, params=params, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except (json.JSONDecodeError, ValueError) as e:
        return {"error": f"JSON decode error: {str(e)}"}


def _check_api_key() -> Optional[Dict]:
    if not API_KEY:
        return {"error": "COPERNICUS_API_KEY environment variable not set"}
    return None


def get_datasets() -> Any:
    """Return all publicly available datasets in the Copernicus CDS catalogue."""
    err = _check_api_key()
    if err:
        return err
    data = _make_request("resources")
    if isinstance(data, dict) and "error" in data:
        return data
    return {"datasets": data}


def get_era5_monthly(variable: str, year: int, month: int, area: List[float] = None) -> Any:
    """Return ERA5 monthly averaged reanalysis data for a variable, year, and month."""
    err = _check_api_key()
    if err:
        return err
    params = {
        "variable": variable,
        "year": str(year),
        "month": str(month).zfill(2),
        "product_type": "monthly_averaged_reanalysis",
        "format": "json"
    }
    if area:
        params["area"] = area
    data = _make_request("resources/reanalysis-era5-single-levels-monthly-means", params=params)
    if isinstance(data, dict) and "error" in data:
        return data
    return {"variable": variable, "year": year, "month": month, "data": data}


def get_temperature_anomaly(year: int, month: int) -> Any:
    """Return global mean surface temperature anomaly for a given year and month."""
    err = _check_api_key()
    if err:
        return err
    params = {
        "variable": "2m_temperature",
        "year": str(year),
        "month": str(month).zfill(2),
        "product_type": "monthly_averaged_reanalysis_by_hour_of_day",
        "format": "json"
    }
    data = _make_request("resources/reanalysis-era5-single-levels-monthly-means", params=params)
    if isinstance(data, dict) and "error" in data:
        return data
    return {"year": year, "month": month, "anomaly_data": data}


def get_sea_level_indicators(year: int) -> Any:
    """Return global mean sea level indicators for a given year."""
    err = _check_api_key()
    if err:
        return err
    params = {"year": str(year), "format": "json"}
    data = _make_request("resources/sea-level-gridded-data-from-satellite-observations", params=params)
    if isinstance(data, dict) and "error" in data:
        return data
    return {"year": year, "sea_level_data": data}


def get_climate_indices(index: str, year: int) -> Any:
    """Return a climate index (e.g., ENSO, NAO, PDO) for a given year."""
    err = _check_api_key()
    if err:
        return err
    params = {"climate_index": index, "year": str(year), "format": "json"}
    data = _make_request("resources/climate-indices", params=params)
    if isinstance(data, dict) and "error" in data:
        return data
    return {"index": index, "year": year, "data": data}


def get_dataset_info(dataset_name: str) -> Any:
    """Return metadata and available variables for a specific CDS dataset."""
    err = _check_api_key()
    if err:
        return err
    data = _make_request(f"resources/{dataset_name}")
    if isinstance(data, dict) and "error" in data:
        return data
    return {"dataset": dataset_name, "info": data}


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if not args:
        print(json.dumps({"error": "No command provided"}))
        return
    command = args[0]
    result = {"error": f"Unknown command: {command}"}
    if command == "datasets":
        result = get_datasets()
    elif command == "era5":
        if len(args) < 4:
            result = {"error": "variable, year, month required"}
        else:
            variable = args[1]
            year = int(args[2])
            month = int(args[3])
            result = get_era5_monthly(variable, year, month)
    elif command == "temperature":
        if len(args) < 3:
            result = {"error": "year and month required"}
        else:
            result = get_temperature_anomaly(int(args[1]), int(args[2]))
    elif command == "sea_level":
        year = int(args[1]) if len(args) > 1 else 2023
        result = get_sea_level_indicators(year)
    elif command == "indices":
        if len(args) < 3:
            result = {"error": "index and year required"}
        else:
            result = get_climate_indices(args[1], int(args[2]))
    elif command == "info":
        dataset_name = args[1] if len(args) > 1 else ""
        if not dataset_name:
            result = {"error": "dataset_name required"}
        else:
            result = get_dataset_info(dataset_name)
    print(json.dumps(result))


if __name__ == "__main__":
    main()
```
