# Financial Modeling Skills Repository
## 360 Social Impact Studios

Strategic toolkit for transforming financial analysis from manual effort into systematic intelligence generation.

## Repository Philosophy

This repository contains modular financial skills designed to elevate 360's investment analysis, portfolio management, and strategic decision-making capabilities. Each skill transforms Claude from a general assistant into a specialized financial analyst equipped with institutional-grade workflows, proven frameworks, and reusable components.

## Core Skills Catalog

### 1. Investment Analysis Suite
**[investment-analysis](./investment-analysis/)**
- Complete investment evaluation workflows
- Multi-scenario financial modeling
- Risk assessment frameworks
- Returns analysis and sensitivity testing
- Exit strategy evaluation

### 2. Portfolio Intelligence
**[portfolio-intelligence](./portfolio-intelligence/)**
- Cross-portfolio performance analytics
- Strategic allocation optimization
- Risk correlation analysis
- Impact measurement frameworks
- Quarterly reporting automation

### 3. Deal Sourcing Engine
**[deal-sourcing](./deal-sourcing/)**
- Market opportunity assessment
- Comparable company analysis
- Valuation benchmarking
- Pipeline prioritization frameworks
- Partnership evaluation protocols

### 4. Impact Financial Modeling
**[impact-modeling](./impact-modeling/)**
- Social return on investment (SROI)
- Blended finance structuring
- Impact-weighted accounting
- Sustainability metrics integration
- Theory of change financial modeling

### 5. International Markets Analysis
**[international-markets](./international-markets/)**
- Cross-border valuation adjustments
- Currency risk modeling
- Regional comparables analysis
- Regulatory impact assessment
- Market entry financial models

### 6. Innovation Portfolio Valuation
**[innovation-valuation](./innovation-valuation/)**
- Technology transfer valuation
- IP portfolio assessment
- Research commercialization models
- University spin-out structuring
- Grant funding optimization

## Architecture Principles

### Progressive Disclosure
- **Level 1**: Skill metadata triggers appropriate financial analysis
- **Level 2**: Core workflows load when skill activates
- **Level 3**: Detailed models and references load as needed

### Reusability First
- Standardized financial model templates
- Consistent formatting protocols
- Modular calculation components
- Shareable validation frameworks

### Executive Readiness
- Publication-quality outputs by default
- Board-ready visualizations
- Strategic context integration
- Decision-focused narratives

## Usage Patterns

### For Executives
```
"Evaluate MediTech Solutions as a $75M growth equity opportunity"
→ Triggers investment-analysis skill
→ Delivers complete IC memo with model
```

### For Analysts
```
"Build quarterly portfolio performance report with risk correlations"
→ Triggers portfolio-intelligence skill
→ Generates interactive dashboard with drill-downs
```

### For Innovation Teams
```
"Value our nuclear technology portfolio for CNEN partnership"
→ Triggers innovation-valuation skill
→ Creates technology transfer valuation framework
```

## Integration Points

### Data Sources
- **Financial Platforms**: S&P Capital IQ, Daloopa, PitchBook
- **Internal Systems**: Asana (pipeline), Google Drive (documents), Box (templates)
- **Market Data**: Web search for real-time metrics, regulatory filings
- **Portfolio Tools**: GenIP (IP valuation), Vianeo (business validation)

### Output Formats
- Excel models with working formulas
- Interactive HTML dashboards
- Board presentation decks
- Investment committee memos
- Partnership term sheets

## Quality Standards

Every skill output meets institutional investment standards:
- **Accuracy**: Validated calculations, sourced assumptions
- **Clarity**: Clear logic flow, documented methodology
- **Flexibility**: Scenario testing, sensitivity analysis
- **Professionalism**: Consistent formatting, publication-ready
- **Auditability**: Transparent formulas, traceable inputs

## Getting Started

1. **Browse Skills**: Review individual skill documentation in `/skills/`
2. **Install Skills**: Upload .skill files to your Claude instance
3. **Connect Data**: Configure integrations with financial platforms
4. **Test Workflows**: Run example analyses to validate setup
5. **Customize**: Adapt templates to your investment thesis

## Development Workflow

### Creating New Skills
```bash
python scripts/init_skill.py <skill-name> --path skills/
# Edit SKILL.md and add resources
python scripts/package_skill.py skills/<skill-name>
```

### Testing Skills
```bash
python scripts/validate_skill.py skills/<skill-name>
python scripts/test_workflows.py skills/<skill-name>
```

## Repository Structure

```
financial-skills-repo/
├── skills/                    # Individual financial skills
│   ├── investment-analysis/
│   ├── portfolio-intelligence/
│   ├── deal-sourcing/
│   ├── impact-modeling/
│   ├── international-markets/
│   └── innovation-valuation/
├── scripts/                   # Utility scripts
│   ├── init_skill.py
│   ├── package_skill.py
│   ├── validate_skill.py
│   └── test_workflows.py
├── templates/                 # Shared model templates
│   ├── dcf_model.xlsx
│   ├── comps_analysis.xlsx
│   └── sensitivity_table.xlsx
└── docs/                      # Additional documentation
    ├── integration-guide.md
    ├── best-practices.md
    └── troubleshooting.md
```

## Support & Contribution

**Maintainer**: 360 Social Impact Studios
**Contact**: innovation@360socialimpact.com
**Version**: 1.0.0
**License**: Proprietary - 360 Social Impact Studios

---

*Building systematic infrastructure for high-stakes innovation finance.*
