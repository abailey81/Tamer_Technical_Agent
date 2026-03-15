"""
Technical Analysis Agent source package.

Modules:
    config          - Configuration constants and enums
    data_collector  - Phase 1: Market data pipeline with quality scoring
    technical_indicators - Phase 2: 20+ indicators across 5 families
    regime_detector - Phase 3: HMM regime detection, GARCH, Hurst exponent
    backtest_engine - Phase 4: Walk-forward backtesting and Monte Carlo
    risk_analytics  - Phase 4B: Risk attribution (52 fields)
    llm_agent       - Phase 5: Claude-powered trade note generation
    report_generator - JSON/HTML/Markdown output
    trade_note_reports - Professional PDF generation
"""
