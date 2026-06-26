# Super SP v1.0.5 - 亚马逊广告全景分析系统

> Geist Design System edition. AI-powered classification for Amazon SP ad reports.

## Overview

Super SP reads Amazon Sponsored Products ad reports (Excel), classifies each search term
into one of 14 categories, generates actionable strategies, and outputs a visual dashboard,
Excel report, and JSON data.

## Features

- **14-dimension classification**: Super/High Potential/Secondary/Invalid/Low Efficiency/
  Uncompetitive/High Competition keywords and ASINs
- **Trend analysis**: 7-day vs 23-day comparison with deviation scoring
- **Strategy mapping**: Bid, placement, targeting, and match type recommendations
- **Spend structure analysis**: ASIN vs keyword spend breakdown by order attribution
- **Negative keyword mining**: Manual extraction + auto-detection
- **Geist UI**: Vercel's design system — minimal, high-contrast, developer-focused

## Quick Start

```bash
# Install dependencies
pip install pandas openpyxl

# Run analysis
python generate.py

# Or on Windows
run.bat
```

## Project Structure

```
super_sp_v1.0.5/
├── DESIGN.md              # Geist design system tokens
├── generate.py            # Entry point (7-step pipeline)
├── report_loader.py       # Excel report loader
├── trend_engine.py        # 30-day trend calculator
├── classifier.py          # 14-dimension classifier
├── strategy_mapper.py     # Strategy generator
├── status_auditor.py      # Status checker (paused/archived)
├── writer.py              # JSON + Excel + HTML output
├── negative_keywords.py   # Negative keyword miner
├── template.html          # Geist-styled dashboard template
├── run.bat                # Windows launcher
├── data/                  # Input: ad reports
└── output/                # Output: dashboard.html, report.xlsx, analysis.json
```

## Design System

This project uses **Vercel Geist** (Light theme). Full design tokens are documented
in `DESIGN.md`. Key principles:

- Gray-scale surfaces with accent color reserved for interaction
- 4px spacing scale, 6px/12px border radii
- Geist Sans typography, tabular figures in data cells
- WCAG AA contrast (4.5:1) for all body text

## License
MIT
