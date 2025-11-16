---
name: investment-analysis
description: Complete investment evaluation with financial modeling, scenario planning, and risk assessment. Use when evaluating equity investments, growth capital opportunities, acquisition targets, or portfolio companies. Supports venture, growth equity, and buyout analyses with multi-scenario modeling, returns analysis, comparable company benchmarking, and IC memo generation. Automatically pulls data from financial platforms and generates institutional-grade Excel models with working formulas.
---

# Investment Analysis Skill

Transform investment evaluation from manual model building into systematic analysis with institutional-grade outputs.

## Core Capabilities

This skill provides comprehensive investment analysis workflows including:
- Multi-scenario financial modeling (base, upside, downside)
- Returns analysis (IRR, MOIC, DPI, TVPI)
- Comparable company benchmarking
- Risk assessment frameworks
- Sensitivity analysis and stress testing
- Exit strategy evaluation
- Investment committee documentation

## Workflow Architecture

### Phase 1: Data Gathering (15-20 minutes)
Systematic collection from multiple sources to build complete investment picture.

### Phase 2: Model Construction (20-30 minutes)
Build comprehensive Excel model with scenarios, sensitivities, and working formulas.

### Phase 3: Analysis & Documentation (15-20 minutes)
Generate IC memo, executive summary, and decision framework.

## Data Collection Protocol

### Company Information
```python
# Use scripts/gather_company_data.py for systematic collection
# Pulls from: Daloopa, S&P Capital IQ, SEC filings, company websites

Required data points:
- Historical financials (3-5 years)
- Current metrics (ARR, growth rate, margins)
- Customer metrics (concentration, churn, CAC/LTV)
- Market position and competition
- Management team and ownership
```

### Market Intelligence
Search for:
- Industry growth rates and TAM
- Recent comparable transactions
- Public company trading multiples
- Regulatory environment and risks
- Technology or market disruptions

### Investment Parameters
Gather from user or documents:
- Deal structure (equity %, debt terms)
- Entry valuation and multiples
- Target returns (IRR, MOIC)
- Investment horizon
- Exit assumptions

## Model Construction Standards

### Structure Requirements
Every model includes these worksheets:
1. **Executive Summary** - Deal overview, returns, investment thesis
2. **Assumptions** - All inputs clearly marked in blue
3. **Financial Model** - P&L, cash flow, balance sheet projections
4. **Scenarios** - Base, upside, downside with probability weighting
5. **Sensitivity** - Tables testing key variables
6. **Valuation** - Entry, exit, and interim valuations
7. **Returns** - IRR, MOIC, DPI by scenario
8. **Comps** - Trading and transaction comparables
9. **Risks** - Categorized risk assessment with mitigations

### Formatting Standards
Apply institutional formatting consistently:
```
Input cells: Blue text, light blue background (#E8F4FD)
Calculations: Black text, white background
References: Green text for cross-sheet links
Headers: Bold, dark blue (#003D7A), larger font
Subtotals: Bold with top border
Totals: Bold with double top border
Negative values: Red text with parentheses
```

### Formula Best Practices
- Use named ranges for key assumptions
- Build dynamic models that update automatically
- Include error checks and validation
- Document complex calculations with comments
- Maintain formula consistency across rows/columns

## Scenario Development Framework

### Base Case Construction
Start with management projections then apply:
- Historical growth rate analysis
- Market growth constraints
- Competitive dynamics assessment
- Margin improvement reality check
- Working capital normalization

### Upside Case Triggers
Model specific value drivers:
- Market expansion acceleration
- Product innovation success
- M&A or consolidation opportunity
- Operational improvement execution
- Multiple expansion scenarios

### Downside Protection
Stress test for:
- Revenue growth deceleration
- Margin compression
- Customer concentration loss
- Competitive disruption
- Regulatory changes
- Recession scenarios

## Risk Assessment Matrix

Evaluate each risk across dimensions:

### Probability Scoring
- **High (>60%)**: Likely to occur based on precedent
- **Medium (30-60%)**: Reasonable possibility
- **Low (<30%)**: Unlikely but possible

### Impact Assessment
- **Severe**: >20% impact on returns
- **Moderate**: 10-20% impact on returns
- **Minor**: <10% impact on returns

### Mitigation Strategies
For each high probability or severe impact risk:
1. Identify early warning indicators
2. Develop contingency plans
3. Structure protective provisions
4. Price risk into valuation

## Comparable Company Analysis

### Public Comparables
When gathering public comps via S&P Capital IQ or web search:
```
Key metrics to collect:
- EV/Revenue (current and forward)
- EV/EBITDA multiples
- P/E ratios (if profitable)
- Growth rates (historical and projected)
- Gross and EBITDA margins
- Rule of 40 score (for SaaS)
- Customer metrics where available
```

### Transaction Comparables
Search for recent transactions including:
- Purchase price and structure
- Revenue and EBITDA at transaction
- Growth rate at time of deal
- Strategic vs. financial buyer
- Market conditions at transaction

### Benchmarking Framework
Position target company against comps:
1. Create scatter plots (growth vs. multiple)
2. Calculate premium/discount to median
3. Identify closest comparables (size, growth, market)
4. Adjust for company-specific factors

## Investment Thesis Development

### Strategic Rationale
Articulate why this investment makes sense:
- Market opportunity and timing
- Competitive advantages and moats
- Management capability and alignment
- Value creation levers
- Exit strategy clarity

### Value Creation Plan
Define specific initiatives with timelines:
- Revenue acceleration tactics
- Margin improvement programs
- M&A or consolidation plays
- Technology or product investments
- International expansion

### Success Metrics
Establish clear KPIs for tracking:
- Quarterly milestones
- Annual targets
- Value creation proof points
- Exit readiness indicators

## Output Generation

### Excel Model Delivery
Create professional model with:
- Table of contents with hyperlinks
- Executive dashboard with key metrics
- Dynamic charts and visualizations
- Scenario selector dropdown
- Sensitivity heat maps
- Print-ready formatting

### IC Memo Structure
Generate comprehensive memo including:
1. **Executive Summary** (1 page)
2. **Investment Thesis** (2-3 pages)
3. **Business Overview** (3-4 pages)
4. **Financial Analysis** (3-4 pages)
5. **Risk Assessment** (2 pages)
6. **Transaction Structure** (1 page)
7. **Appendices** (supporting data)

### Presentation Materials
If requested, create deck with:
- Investment highlights
- Business model overview
- Financial performance and projections
- Competitive positioning
- Value creation roadmap
- Risk and mitigation summary
- Transaction terms and returns

## Quality Assurance Checklist

Before delivering any investment analysis:

### Data Validation
- [ ] Cross-check financial data across sources
- [ ] Verify growth rates and margins are realistic
- [ ] Confirm multiples align with market
- [ ] Validate customer metrics and assumptions

### Model Testing
- [ ] Check all formulas calculate correctly
- [ ] Test scenario toggles work properly
- [ ] Verify sensitivities update dynamically
- [ ] Ensure no circular references
- [ ] Confirm returns calculations are accurate

### Document Review
- [ ] Investment thesis is clear and compelling
- [ ] Risks are comprehensively addressed
- [ ] Assumptions are documented and justified
- [ ] Formatting is consistent throughout
- [ ] Executive summary captures key points

## Using Bundled Resources

### Scripts
- `scripts/gather_company_data.py` - Automated data collection from multiple sources
- `scripts/build_model_structure.py` - Generate standard model framework
- `scripts/calculate_returns.py` - IRR, MOIC, DPI calculations
- `scripts/generate_sensitivities.py` - Create sensitivity tables
- `scripts/format_excel.py` - Apply institutional formatting

### References
- `references/valuation_methods.md` - DCF, comps, precedent transaction methodologies
- `references/industry_frameworks.md` - Sector-specific analysis frameworks
- `references/risk_taxonomy.md` - Comprehensive risk categorization
- `references/ic_templates.md` - Investment committee documentation standards

### Assets
- `assets/model_template.xlsx` - Base financial model structure
- `assets/sensitivity_template.xlsx` - Sensitivity analysis frameworks
- `assets/ic_memo_template.docx` - IC memo formatting
- `assets/charts_library.xlsx` - Visualization templates

## Advanced Techniques

### Monte Carlo Simulation
For complex investments with multiple uncertainties:
1. Define probability distributions for key variables
2. Run 10,000+ scenarios
3. Generate probability-weighted returns distribution
4. Calculate confidence intervals for IRR/MOIC

### Real Options Valuation
For investments with embedded optionality:
1. Identify expansion, abandonment, timing options
2. Model using Black-Scholes or binomial trees
3. Calculate option value addition to base case
4. Incorporate into total valuation

### Portfolio Construction Analysis
When evaluating within portfolio context:
1. Assess correlation with existing investments
2. Calculate portfolio-level risk metrics
3. Optimize for risk-adjusted returns
4. Consider fund construction constraints

## Integration with 360 Ecosystem

### Vianeo Framework Integration
Apply business validation scoring:
- Commercial readiness assessment
- Market validation evidence
- Team capability scoring
- Scalability evaluation

### GenIP Valuation Integration
For technology or IP-heavy investments:
- Patent portfolio valuation
- Technology competitiveness scoring
- Innovation pipeline assessment
- IP risk evaluation

### Impact Measurement Integration
For impact investments:
- Theory of change alignment
- Impact metrics definition
- SROI calculations
- SDG contribution mapping

## Common Patterns and Solutions

### Pattern: High-Growth SaaS Investment
1. Focus on Rule of 40 and magic number
2. Model cohort-based revenue build
3. Emphasize CAC payback and LTV/CAC
4. Stress test churn and growth deceleration

### Pattern: Turnaround Investment
1. Separate core from non-core performance
2. Model operational improvements explicitly
3. Include restructuring costs and timeline
4. Focus on downside protection

### Pattern: Platform Investment
1. Model initial platform and add-ons separately
2. Include multiple arbitrage analysis
3. Factor integration costs and synergies
4. Build consolidated returns model

### Pattern: International Expansion
1. Incorporate FX risk and hedging
2. Model country-specific growth rates
3. Include regulatory and political risk
4. Adjust WACC for country risk premium

## Troubleshooting Guide

### Issue: Conflicting Financial Data
Solution: Prioritize audited financials > management reports > estimates. Document all reconciliations and note discrepancies in assumptions.

### Issue: Limited Comparable Companies
Solution: Expand search to adjacent sectors, use regression analysis to adjust for differences, consider precedent transactions even if dated.

### Issue: Uncertain Exit Timing/Multiple
Solution: Model multiple exit scenarios (IPO, strategic, sponsor), use probability weighting, show returns sensitivity to exit assumptions.

### Issue: Complex Deal Structure
Solution: Build separate returns models for each security type, model waterfalls explicitly, include all fees and carried interest.

Remember: The goal is not just to build a model, but to provide strategic intelligence that drives better investment decisions. Every analysis should tell a clear story about value creation potential and risk-adjusted returns.
