---
name: Financial Modeling Skills
description: Comprehensive financial analysis suite including investment evaluation, portfolio intelligence, SROI calculation, technology transfer valuation, and cross-border analysis. Use for investment decisions, portfolio management, impact measurement, and financial modeling requiring institutional-grade outputs.
version: 1.0.0
author: 360 Social Impact Studios
created: 2025-11-15
updated: 2025-11-22
category: financial-analysis
complexity: high
tags: [investment-analysis, portfolio-management, impact-measurement, financial-modeling, excel, valuations]
dependencies:
  - Python (for data gathering scripts)
  - Excel (for financial models)
  - Web search (for market data)
outputs:
  - Excel models with working formulas
  - Investment committee memos
  - Portfolio dashboards (HTML/Excel)
  - Valuation reports
  - SROI analyses
---

# Financial Modeling Skills - Master Skill

## Purpose

This is a comprehensive financial modeling suite containing multiple specialized skills for investment analysis, portfolio management, and impact measurement. This master skill routes requests to the appropriate sub-skill based on the user's needs.

## Sub-Skill Catalog

### 1. Investment Analysis (`investment-analysis/SKILL.md`)
**Use when:** Evaluating equity investments, growth capital opportunities, acquisition targets, portfolio companies

**Capabilities:**
- Multi-scenario financial modeling (base, upside, downside)
- Returns analysis (IRR, MOIC, DPI, TVPI)
- Comparable company benchmarking
- Risk assessment frameworks
- Sensitivity analysis and stress testing
- Exit strategy evaluation
- Investment committee documentation

**Typical outputs:** Excel financial model, IC memo, executive summary
**Time investment:** 50-70 minutes comprehensive analysis

---

### 2. Portfolio Intelligence (`portfolio-intelligence/SKILL.md`)
**Use when:** Analyzing portfolio performance, creating LP reports, optimizing allocation, assessing risk correlations

**Capabilities:**
- Cross-portfolio performance analytics
- Strategic allocation optimization
- Risk correlation analysis
- Impact measurement aggregation
- Quarterly reporting automation
- Interactive dashboard generation
- LP communication packages

**Typical outputs:** Portfolio dashboard (Excel/HTML), quarterly reports, performance attribution
**Time investment:** 40-60 minutes

---

### 3. Impact Modeling (`impact-modeling/SKILL.md`)
**Use when:** Quantifying social impact, calculating SROI, structuring blended finance, measuring SDG contributions

**Capabilities:**
- Social Return on Investment (SROI) calculation
- Blended finance structuring
- Impact-weighted accounting
- Sustainability metrics integration
- Theory of change financial modeling
- SDG contribution mapping
- Impact attribution analysis

**Typical outputs:** SROI report, impact dashboard, blended finance structure model
**Time investment:** 60-90 minutes

---

### 4. Deal Sourcing (Planned - Not Yet Implemented)
**Use when:** Assessing market opportunities, analyzing comparables, prioritizing pipeline

**Planned capabilities:**
- Market opportunity assessment
- Comparable company analysis
- Valuation benchmarking
- Pipeline prioritization frameworks
- Partnership evaluation protocols

---

### 5. International Markets (Planned - Not Yet Implemented)
**Use when:** Evaluating cross-border investments, analyzing currency risk, assessing regional markets

**Planned capabilities:**
- Cross-border valuation adjustments
- Currency risk modeling
- Regional comparables analysis
- Regulatory impact assessment
- Market entry financial models

---

### 6. Innovation Portfolio Valuation (Planned - Not Yet Implemented)
**Use when:** Valuing technology transfer, IP portfolios, research commercialization, university spin-outs

**Planned capabilities:**
- Technology transfer valuation
- IP portfolio assessment
- Research commercialization models
- University spin-out structuring
- Grant funding optimization

---

## Routing Logic

When user request is received, determine which sub-skill to use:

### Investment Analysis Triggers:
- "evaluate [company] as an investment"
- "build a financial model for [company]"
- "analyze this acquisition opportunity"
- "create IC memo for [deal]"
- "perform due diligence on [investment]"
- Keywords: IRR, MOIC, returns, valuation, investment, equity, growth capital

**Action:** Load and execute `investment-analysis/SKILL.md`

---

### Portfolio Intelligence Triggers:
- "portfolio performance analysis"
- "quarterly portfolio report"
- "LP update"
- "portfolio risk analysis"
- "allocation optimization"
- Keywords: portfolio, LP, fund performance, risk correlation, allocation

**Action:** Load and execute `portfolio-intelligence/SKILL.md`

---

### Impact Modeling Triggers:
- "calculate SROI for [program/investment]"
- "measure social impact"
- "blended finance structure"
- "SDG contribution"
- "theory of change financial model"
- Keywords: SROI, impact, social return, blended finance, SDG, sustainability

**Action:** Load and execute `impact-modeling/SKILL.md`

---

### Technology Transfer / IP Valuation Triggers:
- "value our [technology] portfolio"
- "technology transfer valuation"
- "IP portfolio assessment"
- "commercialization potential"
- "university spin-out"
- Keywords: technology transfer, IP, patent, licensing, commercialization

**Action:** Inform user that innovation-valuation sub-skill is planned but not yet implemented. Suggest using investment-analysis skill as interim solution.

---

### Multiple Sub-Skills Needed:
If request requires multiple sub-skills (e.g., "evaluate this impact investment"):
1. Start with investment-analysis for financial modeling
2. Then use impact-modeling for SROI calculation
3. Integrate outputs into comprehensive report

---

## Quality Standards

All sub-skills adhere to institutional investment standards:

**Accuracy:**
- Validated calculations with sourced assumptions
- Cross-checked market data
- Documented methodology

**Clarity:**
- Clear logic flow throughout models
- Color-coded inputs, calculations, outputs
- Executive summaries for non-technical stakeholders

**Flexibility:**
- Scenario testing (base, upside, downside)
- Sensitivity analysis on key variables
- Adjustable assumptions for different contexts

**Professionalism:**
- Consistent formatting across all outputs
- Publication-ready quality
- Board and IC presentation standards

**Auditability:**
- Transparent formulas (no hidden calculations)
- Traceable inputs with sources
- Documented assumptions and logic

---

## Data Integration

### Supported Data Sources:
- **Financial Platforms**: S&P Capital IQ, Daloopa, PitchBook, FactSet
- **Internal Systems**: Asana (pipeline), Google Drive (documents), Box (templates)
- **Market Data**: Web search for real-time metrics, SEC filings, regulatory documents
- **Portfolio Tools**: GenIP (IP valuation), Vianeo (business validation)

### Data Gathering Protocol:
1. Use Python scripts in `scripts/` directory for automated collection
2. Fallback to manual web search for missing data
3. Document all sources in model assumptions tab
4. Flag low-confidence data for user verification

---

## Output Formats

### Excel Models (Investment Analysis, Impact Modeling):
- Working formulas throughout
- Multiple worksheets (assumptions, model, scenarios, sensitivity, returns)
- Institutional formatting standards
- Print-optimized layouts

### Dashboards (Portfolio Intelligence):
- Interactive HTML with charts
- Excel pivot tables and charts
- Real-time data connections (if available)
- Mobile-responsive layouts

### Documents (All Skills):
- Investment committee memos
- Executive summaries
- Board presentations
- LP reports

---

## Usage Examples

### Example 1: Growth Equity Investment Evaluation
```
User: "Evaluate MediTech Solutions as a $75M Series C investment.
      They're a healthcare SaaS company with $15M ARR growing 80% YoY."

System: Routes to investment-analysis/SKILL.md
Output: Complete Excel model + IC memo (50-70 minutes)
```

### Example 2: Quarterly Portfolio Review
```
User: "Generate Q4 2024 portfolio performance report with risk analysis"

System: Routes to portfolio-intelligence/SKILL.md
Output: Portfolio dashboard (Excel/HTML) + quarterly report (40-60 minutes)
```

### Example 3: Impact Measurement
```
User: "Calculate SROI for our education program that served 10,000 students
      with $2M budget over 3 years"

System: Routes to impact-modeling/SKILL.md
Output: SROI report with impact dashboard (60-90 minutes)
```

### Example 4: Combined Analysis
```
User: "Evaluate this $50M impact investment in affordable housing.
      Need both financial returns and social impact analysis."

System:
  Step 1: Routes to investment-analysis/SKILL.md (financial model + IC memo)
  Step 2: Routes to impact-modeling/SKILL.md (SROI calculation)
  Step 3: Integrates outputs into comprehensive impact investment analysis
Output: Integrated financial + impact report (110-160 minutes total)
```

---

## Getting Started

### First-Time Setup:
1. Review README.md for repository overview
2. Check FILE_INVENTORY.md for complete file listing
3. Read docs/integration-guide.md for implementation roadmap
4. Test with a simple investment analysis to validate setup

### Quick Start:
- For investment evaluation → Use investment-analysis sub-skill
- For portfolio reporting → Use portfolio-intelligence sub-skill
- For impact measurement → Use impact-modeling sub-skill

### Advanced Usage:
- Combine multiple sub-skills for comprehensive analyses
- Customize templates in each sub-skill's assets/ directory
- Extend with custom scripts in scripts/ directory

---

## Architecture Principles

### Progressive Disclosure:
- **Level 1**: Master skill routes to appropriate sub-skill
- **Level 2**: Sub-skill loads core workflow
- **Level 3**: Detailed models and references load as needed

### Reusability First:
- Standardized model templates across sub-skills
- Consistent formatting protocols
- Modular calculation components
- Shareable validation frameworks

### Executive Readiness:
- Publication-quality outputs by default
- Board-ready visualizations
- Strategic context integration
- Decision-focused narratives

---

## Time Investment Guidelines

| Sub-Skill | Complexity | Time Estimate |
|-----------|------------|---------------|
| Investment Analysis | High | 50-70 minutes |
| Portfolio Intelligence | Medium | 40-60 minutes |
| Impact Modeling | High | 60-90 minutes |
| Combined Analyses | Very High | 110-160 minutes |

**Note:** Times assume data is readily available. Add 15-30 minutes if extensive data gathering required.

---

## Supporting Files

**Core Documentation:**
- `README.md` - Repository overview and catalog
- `FILE_INVENTORY.md` - Complete file listing
- `docs/integration-guide.md` - Implementation roadmap

**Sub-Skills:**
- `investment-analysis/SKILL.md` - Investment evaluation workflows
- `portfolio-intelligence/SKILL.md` - Portfolio analytics workflows
- `impact-modeling/SKILL.md` - SROI and impact measurement

**Scripts:**
- `scripts/init_skill.py` - Create new sub-skills
- `scripts/package_skill.py` - Package skills for distribution

**References:**
- Each sub-skill has `references/` directory with detailed guides
- Each sub-skill has `assets/` directory with templates

---

## Troubleshooting

**"Which sub-skill should I use?"**
→ See routing logic section above
→ When in doubt, start with investment-analysis (most general)

**"Can I combine multiple sub-skills?"**
→ Yes! For complex analyses, use multiple sub-skills sequentially
→ Example: Investment analysis + impact modeling for impact investments

**"Data sources not accessible"**
→ Use web search as fallback
→ Document data limitations in assumptions
→ Flag for user verification

**"Need a sub-skill that doesn't exist yet"**
→ Check "Planned" section for upcoming capabilities
→ Use closest existing sub-skill as interim solution
→ Contact 360 team to prioritize development

---

## Version History

### v1.0.0 (2025-11-22)
- Initial master skill with routing logic
- Three implemented sub-skills: investment-analysis, portfolio-intelligence, impact-modeling
- Three planned sub-skills: deal-sourcing, international-markets, innovation-valuation
- Complete quality standards and architecture principles

---

## Next Steps

1. **Start simple**: Try investment-analysis on a known company
2. **Explore sub-skills**: Read individual SKILL.md files for detailed capabilities
3. **Customize**: Adapt templates to your investment thesis and portfolio needs
4. **Scale**: Use portfolio-intelligence for ongoing monitoring

**Ready to start?** Provide an investment opportunity, portfolio update request, or impact measurement need.
