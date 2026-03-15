<div align="center">

# Technical Analysis Agent

### Institutional-Grade Quantitative Analysis Pipeline

*5-phase architecture · 20+ indicators · HMM regime detection · GARCH volatility · Claude-powered trade notes*

<br>

[![Python 3.10-3.12](https://img.shields.io/badge/python-3.10--3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Claude](https://img.shields.io/badge/Claude-Sonnet-CC785C?style=for-the-badge&logo=anthropic&logoColor=white)](https://anthropic.com/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![License](https://img.shields.io/badge/MIT-green?style=for-the-badge)](LICENSE)

<br>

[![GitHub stars](https://img.shields.io/github/stars/abailey81/Tamer_Technical_Agent?style=social)](https://github.com/abailey81/Tamer_Technical_Agent/stargazers)

---

**A 5-phase quantitative analysis pipeline** that generates institutional-quality trade recommendations through technical indicator analysis, regime detection, walk-forward backtesting, and LLM-powered narrative generation. Outputs a 247-field structured JSON with professional PDF/HTML/Markdown reports.

<br>

[Pipeline](#pipeline) · [Indicators](#technical-indicators) · [Regime Detection](#regime-detection) · [Backtesting](#backtesting) · [Getting Started](#getting-started)

</div>

<br>

## Highlights

<table>
<tr>
<td width="50%">

**5-Phase Pipeline**
- Phase 1: Data collection + 7 volatility estimators + quality scoring
- Phase 2: 20+ indicators across 5 families with confidence scoring
- Phase 3: HMM regime detection + GARCH + Hurst exponent
- Phase 4: Walk-forward backtesting + Monte Carlo + risk attribution
- Phase 5: Claude Sonnet trade note generation

</td>
<td width="50%">

**Structured Output**
- 247-field JSON for orchestration and decision support
- Professional PDF reports via ReportLab (8-10 pages)
- Interactive HTML reports with SVG visualizations
- Markdown reports for documentation
- CAPM alpha/beta, VaR/CVaR, factor attribution

</td>
</tr>
</table>

---

## Pipeline

```
Phase 1: Data Collection          Phase 2: Indicators           Phase 3: Regime
├─ yfinance OHLCV               ├─ Momentum (25%)              ├─ 3-state HMM
├─ 4-dimension quality scoring   ├─ Trend (25%)                 ├─ GARCH(1,1)
├─ 7 volatility estimators       ├─ Volatility (15%)            ├─ Hurst exponent
├─ 5 hypothesis tests            ├─ Volume (15%)                └─ CUSUM breaks
└─ VIX regime classification     └─ Ichimoku (20%)

Phase 4: Backtesting             Phase 5: Trade Notes
├─ Walk-forward (5 periods)      ├─ Claude Sonnet 4.5
├─ Monte Carlo (500 paths)       ├─ Investment thesis
├─ Transaction cost modeling     ├─ Bull/base/bear scenarios
├─ Kelly / vol-target sizing     ├─ Risk analysis
└─ Risk attribution (52 fields)  └─ Catalysts & risks
```

---

## Technical Indicators

| Family | Weight | Indicators |
|:-------|:------:|:-----------|
| **Momentum** | 25% | RSI (14), Stochastic %K/%D, Williams %R, ROC |
| **Trend** | 25% | MACD (12/26/9), ADX/DMI, Aroon, Supertrend |
| **Volatility** | 15% | Bollinger Bands, Keltner Channels, Donchian Channels |
| **Volume** | 15% | OBV, Chaikin Money Flow, MFI, VWMA |
| **Ichimoku** | 20% | Tenkan, Kijun, Senkou A/B, Chikou |

<details>
<summary><b>7 Volatility Estimators</b></summary>

| Estimator | Method |
|:----------|:-------|
| Close-to-Close | Baseline standard deviation |
| Parkinson (1980) | High-Low range based |
| Garman-Klass (1980) | Full OHLC utilization |
| Rogers-Satchell (1991) | Drift-adjusted |
| Yang-Zhang (2000) | Gap-adjusted (overnight returns) |
| GKYZ | Hybrid Garman-Klass / Yang-Zhang |
| Hodges-Tompkins | Bias-corrected finite sample |

</details>

<details>
<summary><b>Risk Attribution (52 fields)</b></summary>

- CAPM alpha/beta decomposition with t-stats and p-values
- Factor attribution analysis and information ratio
- Regime-conditional performance (Bull/Bear/Sideways)
- Historical stress testing (COVID crash, 2022 bear, 2018 Q4)
- VaR/CVaR at 95% and 99% confidence levels
- Drawdown analysis and recovery time estimation

</details>

---

## Getting Started

```bash
git clone https://github.com/abailey81/Tamer_Technical_Agent.git
cd Tamer_Technical_Agent

python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Set API key
echo "ANTHROPIC_API_KEY=sk-ant-..." > .env

# Run analysis
python run_demo.py                        # Default: AAPL
python run_demo.py --symbol MSFT          # Custom ticker
python run_demo.py --years 10             # 10 years of data
python run_demo.py --skip-llm             # Skip LLM (faster)
```

---

## Project Structure

```
Tamer_Technical_Agent/
├── run_demo.py                     # Main orchestrator (2,497 lines)
├── src/
│   ├── config.py                   # Configuration & enums
│   ├── data_collector.py           # Phase 1: Data pipeline + quality scoring
│   ├── technical_indicators.py     # Phase 2: 20+ indicators
│   ├── regime_detector.py          # Phase 3: HMM + GARCH + Hurst
│   ├── backtest_engine.py          # Phase 4: Walk-forward + Monte Carlo
│   ├── risk_analytics.py           # Phase 4B: Risk attribution (52 fields)
│   ├── llm_agent.py                # Phase 5: Claude trade notes
│   ├── report_generator.py         # JSON/HTML/Markdown output
│   └── trade_note_reports.py       # Professional PDF generation
├── requirements.txt
└── outputs/                        # Generated reports
```

---

<div align="center">

**[MIT License](LICENSE)**

Built with Claude, vectorbt, hmmlearn, arch, and ReportLab

</div>
