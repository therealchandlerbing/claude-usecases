# Implementation Guide: Financial Modeling Suite

**Deep Knowledge Base for Investment Analysis and Portfolio Intelligence**

---

## Table of Contents

1. [Data Collection](#data-collection)
2. [Valuation Methodologies](#valuation-methodologies)
3. [Returns Analysis](#returns-analysis)
4. [Risk Assessment](#risk-assessment)
5. [Excel Best Practices](#excel-best-practices)
6. [Portfolio Analytics](#portfolio-analytics)
7. [Impact Measurement](#impact-measurement)
8. [Troubleshooting](#troubleshooting)

---

## Data Collection

### Financial Data Sources

| Source | Best For | Access Method |
|--------|----------|---------------|
| Daloopa | Historical financials | API/Web |
| S&P Capital IQ | Public comps | Terminal |
| PitchBook | Private transactions | Portal |
| SEC EDGAR | Public filings | Web search |
| Company | Management presentations | Direct request |

### Key Metrics to Collect

**Revenue Metrics:**
- Historical revenue (3-5 years)
- Revenue breakdown by segment
- Growth rates (YoY, CAGR)
- Recurring vs. non-recurring

**Profitability:**
- Gross margin and trend
- EBITDA and EBITDA margin
- Operating expenses by category
- Net income and EPS

**SaaS-Specific:**
- ARR/MRR
- Net revenue retention
- Gross and net churn
- CAC and LTV
- CAC payback period

**Working Capital:**
- Receivables and DSO
- Inventory and DIO
- Payables and DPO
- Working capital cycle

---

## Valuation Methodologies

### DCF Analysis

**Steps:**
1. Project free cash flows (5-10 years)
2. Calculate terminal value
3. Determine WACC
4. Discount to present value

**Terminal Value Methods:**
- Gordon Growth: FCF × (1 + g) / (WACC - g)
- Exit Multiple: EBITDA × multiple

**WACC Components:**
```
WACC = (E/V × Re) + (D/V × Rd × (1-T))

Where:
Re = Risk-free + Beta × Market premium
Rd = Cost of debt
T = Tax rate
```

### Comparable Companies

**Selection Criteria:**
- Same industry/sector
- Similar size (revenue, market cap)
- Comparable growth profile
- Geographic similarity

**Key Multiples:**
- EV/Revenue (growth companies)
- EV/EBITDA (profitable companies)
- P/E (mature companies)

**Adjustments:**
- Size premium/discount
- Growth differential
- Margin differential
- Geographic risk

### Precedent Transactions

**Search Criteria:**
- Same sector
- Similar size range
- Recent (ideally <3 years)
- Comparable deal type

**Control Premium:**
Typically 20-40% over trading multiples

---

## Returns Analysis

### IRR Calculation

```
NPV = Σ [CFt / (1 + IRR)^t] = 0

Where:
CFt = Cash flow at time t
IRR = Internal rate of return
```

**IRR Considerations:**
- Sensitive to timing
- Assumes reinvestment at IRR
- Multiple IRRs possible with sign changes

### MOIC Calculation

```
MOIC = (Total Distributions + Current Value) / Total Invested

Example:
Invested: $50M
Distributions: $20M
Current Value: $100M
MOIC = ($20M + $100M) / $50M = 2.4x
```

### J-Curve Analysis

**Typical Pattern:**
- Years 1-2: Negative returns (fees, deployment)
- Years 3-4: NAV appreciation
- Years 5+: Realizations and DPI

**Key Inflection Points:**
- First distribution
- First markup >2x
- DPI > 0.5x
- NAV peak

---

## Risk Assessment

### Risk Categories

**Market Risk:**
- Economic cycle sensitivity
- Interest rate exposure
- Currency fluctuation
- Commodity prices

**Business Risk:**
- Competitive dynamics
- Technology disruption
- Regulatory changes
- Customer concentration

**Execution Risk:**
- Management capability
- Integration challenges
- Operational complexity
- Capital requirements

**Financial Risk:**
- Leverage levels
- Liquidity constraints
- Refinancing risk
- Covenant compliance

### Mitigation Strategies

**Structural Protections:**
- Board seats
- Veto rights
- Anti-dilution
- Liquidation preference

**Operational:**
- Milestone-based funding
- Management incentives
- Reporting requirements
- Strategic support

**Financial:**
- Debt covenants
- Cash reserves
- Insurance coverage
- Hedging instruments

---

## Excel Best Practices

### Model Architecture

**Sheet Organization:**
1. Cover/TOC
2. Assumptions
3. Revenue build
4. P&L
5. Balance sheet
6. Cash flow
7. Scenarios
8. Returns
9. Sensitivity
10. Comps

### Naming Conventions

```
Assumptions: a_[name] (e.g., a_revenue_growth)
Calculations: c_[name] (e.g., c_ebitda_margin)
Outputs: o_[name] (e.g., o_irr_base)
```

### Error Prevention

**Input Validation:**
```excel
=IF(AND(a_growth>0, a_growth<1), a_growth, "Error: Growth should be 0-100%")
```

**Circular Reference Check:**
```excel
=IFERROR(formula, "Circular Ref")
```

**Cross-Check:**
```excel
=IF(ABS(BS_Assets-BS_Liabilities)<0.01, "OK", "BS doesn't balance")
```

### Sensitivity Tables

**Two-Variable Table:**
- Row: Revenue growth (5%, 10%, 15%, 20%, 25%)
- Column: Exit multiple (6x, 8x, 10x, 12x, 14x)
- Cell: IRR

**Tornado Chart Data:**
```
Variable | Low | Base | High | Swing
Growth   | 15% | 20%  | 25%  | 8%
Multiple | 6x  | 8x   | 10x  | 12%
Margin   | 20% | 25%  | 30%  | 5%
```

---

## Portfolio Analytics

### Performance Attribution

**Brinson Attribution:**
```
Allocation Effect = (Wp - Wb) × (Rb - Rtotal)
Selection Effect = Wb × (Rp - Rb)
Interaction Effect = (Wp - Wb) × (Rp - Rb)
```

### Risk Metrics

**Value at Risk (VaR):**
```
VaR95 = Portfolio Value × σ × 1.645

Where σ = portfolio standard deviation
```

**Sharpe Ratio:**
```
Sharpe = (Rp - Rf) / σp

Where:
Rp = Portfolio return
Rf = Risk-free rate
σp = Portfolio std dev
```

### Correlation Analysis

**Key Correlations to Monitor:**
- Intra-sector correlation
- Geographic correlation
- Factor correlation (growth, value)
- Macroeconomic sensitivity

**Warning Thresholds:**
- Correlation > 0.7: High concentration risk
- Correlation > 0.5: Moderate concern
- Correlation < 0.3: Good diversification

---

## Impact Measurement

### SROI Framework

**Steps:**
1. Define scope and stakeholders
2. Map outcomes (theory of change)
3. Assign values to outcomes
4. Establish impact duration
5. Calculate present value
6. Compute ratio

**Monetization Examples:**
- Job created: $45,000 (avg annual salary)
- Ton CO2 avoided: $50 (social cost of carbon)
- QALY gained: $100,000 (health economics)

### SDG Alignment

**Mapping Process:**
1. Identify primary SDG (>50% relevance)
2. List secondary SDGs
3. Define KPIs per SDG
4. Set targets and track progress

**Common Impact KPIs:**
- SDG 1 (Poverty): Income increase
- SDG 4 (Education): Completion rates
- SDG 7 (Energy): MWh clean energy
- SDG 8 (Work): Jobs created
- SDG 13 (Climate): tCO2e avoided

---

## Troubleshooting

### Common Issues

**Conflicting data:**
Priority order: Audited → Management → Estimates
Document reconciliations in assumptions.

**Limited comparables:**
Expand search to adjacent sectors. Use regression to adjust for differences.

**Complex deal structure:**
Build separate returns for each security. Model waterfalls explicitly.

**Exit uncertainty:**
Model multiple scenarios (IPO, strategic, sponsor). Use probability weighting.

### Model Debugging

**Formula errors:**
- Check cell references
- Verify named ranges
- Test with simple inputs
- Use IFERROR for debugging

**Circular references:**
- Enable iterative calculation
- Add manual override input
- Document circular logic

**Performance issues:**
- Reduce unnecessary calculations
- Use values instead of formulas where possible
- Limit volatile functions (INDIRECT, OFFSET)

---

## Quality Checklist

### Before Delivery

**Data:**
- [ ] Sources documented
- [ ] Cross-checked across sources
- [ ] Date stamps current

**Model:**
- [ ] Formulas correct
- [ ] Scenarios work
- [ ] Sensitivities update
- [ ] No errors (#REF, #DIV/0)

**Document:**
- [ ] Thesis clear
- [ ] Risks addressed
- [ ] Formatting consistent
- [ ] Executive summary complete

---

*For operational protocols, see [SKILL.md](./SKILL.md)*
*For worked examples, see [EXAMPLES.md](./EXAMPLES.md)*
