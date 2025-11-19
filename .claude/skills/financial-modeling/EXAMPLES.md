# Examples: Financial Modeling Suite

**Worked Examples Across Investment Types**

---

## Table of Contents

1. [Growth Equity Investment](#example-1-growth-equity-investment)
2. [Venture Series B](#example-2-venture-series-b)
3. [Portfolio Quarterly Report](#example-3-portfolio-quarterly-report)
4. [Impact Investment with SROI](#example-4-impact-investment-with-sroi)
5. [Comparable Company Analysis](#example-5-comparable-company-analysis)
6. [Platform Investment](#example-6-platform-investment)

---

## Example 1: Growth Equity Investment

### User Request

```
Evaluate DataCloud as a $75M growth equity investment at 6x ARR

Context:
- Enterprise data platform, $12.5M ARR
- 35% YoY growth, 80% gross margin
- EBITDA breakeven, 50 enterprise customers
- 130% NRR, 8% gross churn

Terms:
- 30% ownership for $75M
- 5-year hold, targeting 2.5x MOIC
```

### Response

---

**Phase 1: Data Gathering**

Collecting company and market data:
- Company financials and customer metrics
- Enterprise software market sizing
- Comparable transactions (Snowflake, Databricks valuations)
- Public comps (Datadog, MongoDB, Confluent)

**Phase 2: Model Construction**

Building 9-worksheet Excel model:

**Scenario Summary:**

| Metric | Downside | Base | Upside |
|--------|----------|------|--------|
| Year 5 ARR | $45M | $60M | $85M |
| Exit Multiple | 5x | 7x | 9x |
| Exit Value | $225M | $420M | $765M |
| MOIC | 0.9x | 1.7x | 3.1x |
| IRR | -2% | 11% | 26% |

**Key Assumptions:**
- Revenue CAGR: 25% (base), 20% (down), 35% (up)
- EBITDA margin improvement: 15% by Year 5
- NRR maintained at 130%

**Phase 3: Risk Assessment**

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Competition from hyperscalers | High | Severe | Differentiation, vertical focus |
| Slower enterprise adoption | Medium | Moderate | SMB expansion option |
| Key engineer departures | Low | Severe | Retention packages, equity |

**Deliverables:**
- Excel model with full scenarios
- 12-page IC memo
- 1-page executive summary

**Recommendation:** Base case returns below target (11% IRR vs. 20% target). Consider negotiating to 5x ARR ($62.5M) to achieve acceptable risk-adjusted returns.

---

## Example 2: Venture Series B

### User Request

```
Analyze HealthBot as a $25M Series B at $100M pre-money

Context:
- AI-powered clinical decision support
- $2M ARR, 150% YoY growth
- FDA breakthrough device designation
- 15 health system pilots, 5 paying
```

### Response

---

**Venture Investment Analysis**

**Market Opportunity:**
- Clinical decision support TAM: $15B by 2030
- AI healthcare CAGR: 45%
- HealthBot addressable: $3B

**Financial Projections (Base Case):**

| Year | ARR | Growth | Burn |
|------|-----|--------|------|
| 2025 | $2M | 150% | $6M |
| 2026 | $5M | 150% | $8M |
| 2027 | $12M | 140% | $5M |
| 2028 | $30M | 150% | $0 |
| 2029 | $70M | 133% | +$15M |

**Returns Analysis:**

| Scenario | Exit | Ownership | Value | MOIC | IRR |
|----------|------|-----------|-------|------|-----|
| Downside | $300M | 15% | $45M | 1.8x | 13% |
| Base | $700M | 18% | $126M | 5.0x | 38% |
| Upside | $1.5B | 20% | $300M | 12x | 65% |

*Ownership assumes follow-on rounds with pro-rata*

**Key Risks:**
- FDA clearance timeline (18-24 months)
- Health system sales cycle (12-18 months)
- Reimbursement uncertainty
- Clinical validation requirements

**Recommendation:** Attractive risk/reward for venture portfolio. Protect downside with milestone-based funding.

---

## Example 3: Portfolio Quarterly Report

### User Request

```
Generate Q4 2025 portfolio performance report

Portfolio:
- 15 active investments
- Fund I (2020): $100M, 60% deployed
- Fund II (2023): $150M, 25% deployed
```

### Response

---

**Q4 2025 Portfolio Performance Report**

**Executive Summary:**
- Total portfolio value: $285M
- Net IRR: 22.4%
- TVPI: 1.65x
- DPI: 0.32x

**Performance by Fund:**

| Fund | Vintage | Invested | Value | IRR | TVPI |
|------|---------|----------|-------|-----|------|
| Fund I | 2020 | $60M | $165M | 28% | 2.75x |
| Fund II | 2023 | $38M | $50M | 15% | 1.32x |

**Attribution Analysis:**

By Sector:
- Technology: +850 bps (45% of portfolio)
- Healthcare: +320 bps (30% of portfolio)
- Consumer: -180 bps (15% of portfolio)
- Industrial: +120 bps (10% of portfolio)

By Vintage:
- 2020: 35% gross IRR
- 2021: 28% gross IRR
- 2022: 18% gross IRR
- 2023-24: 15% gross IRR

**Risk Dashboard:**

Concentration:
- Top 5 positions: 62% of value (flag: >50%)
- Largest position: 18% (flag: >15%)
- Technology sector: 45% (OK: <50%)

Correlations:
- Highest pair correlation: 0.72 (TechA-TechB)
- Average sector correlation: 0.45

**Key Events:**
- DataCloud exit: $120M (3.2x MOIC)
- HealthBot Series C: 2.5x markup
- CleanEnergy impairment: -40%

**Action Items:**
- Consider partial realization of TechA (concentration)
- Support HealthBot commercialization
- Monitor CleanEnergy turnaround

---

## Example 4: Impact Investment with SROI

### User Request

```
Evaluate CleanGrid as a $20M impact investment

Context:
- Distributed solar for underserved communities
- 50MW deployed, 10,000 households served
- $8M revenue, 25% EBITDA margin
- SDG 7 (Clean Energy), SDG 13 (Climate)
```

### Response

---

**Impact Investment Analysis**

**Financial Returns:**

| Scenario | Exit Value | MOIC | IRR |
|----------|-----------|------|-----|
| Downside | $40M | 2.0x | 15% |
| Base | $65M | 3.3x | 27% |
| Upside | $100M | 5.0x | 38% |

**Impact Metrics:**

Annual Outcomes:
- CO2 avoided: 75,000 tons
- Households served: 10,000
- Jobs created: 150
- Energy cost savings: $2M to households

**SROI Calculation:**

| Outcome | Quantity | Value | Annual Value |
|---------|----------|-------|--------------|
| CO2 avoided | 75,000 tons | $50/ton | $3.75M |
| Energy savings | 10,000 HH | $200/yr | $2.0M |
| Jobs | 150 | $45,000 | $6.75M |
| Total Social Value | | | $12.5M |

**5-Year SROI:**
```
Financial Return: $65M - $20M = $45M
Social Value (PV): $45M (5 years discounted)
Total Value: $90M
SROI = $90M / $20M = 4.5:1
```

**SDG Alignment Scorecard:**

| SDG | Contribution | KPIs |
|-----|-------------|------|
| SDG 7 | Primary | MWh generated, households served |
| SDG 13 | Primary | tCO2e avoided |
| SDG 8 | Secondary | Jobs created |
| SDG 1 | Secondary | Energy cost savings |

**Recommendation:** Strong blended returns (3.3x financial + 4.5:1 SROI). Aligns with impact thesis and provides diversification from technology portfolio.

---

## Example 5: Comparable Company Analysis

### User Request

```
Find comparable companies and transactions for a $15M ARR vertical SaaS company in construction tech
```

### Response

---

**Comparable Company Analysis**

**Public Trading Comps:**

| Company | Revenue | Growth | EV/Rev | Margin |
|---------|---------|--------|--------|--------|
| Procore | $950M | 30% | 12x | 5% |
| Autodesk | $5.5B | 15% | 8x | 30% |
| Trimble | $3.8B | 12% | 5x | 22% |
| Bentley | $1.1B | 10% | 10x | 28% |

**Median:** 9x EV/Revenue

**Adjustment for Target:**
- Size discount: -25% (smaller than comps)
- Growth premium: +15% (higher growth)
- Margin discount: -10% (lower margins)
- Net adjustment: -20%

**Implied Multiple:** 7.2x Revenue

**Precedent Transactions:**

| Target | Acquirer | Date | Revenue | Multiple |
|--------|----------|------|---------|----------|
| PlanGrid | Autodesk | 2018 | $100M | 8.7x |
| BuildingConnected | Autodesk | 2019 | $50M | 6.0x |
| Fieldwire | Hilti | 2021 | $40M | 10x |
| Ryvit | Trimble | 2022 | $25M | 8x |

**Median:** 8.4x Revenue

**Valuation Summary:**

| Method | Multiple | Value |
|--------|----------|-------|
| Trading comps (adj) | 7.2x | $108M |
| Transaction comps | 8.4x | $126M |
| Weighted Average | 7.8x | $117M |

**Recommendation:** Fair value range $105-125M based on 7-8.5x revenue multiple.

---

## Example 6: Platform Investment

### User Request

```
Model a platform investment strategy for ServiceTech

Initial platform: $100M at 8x EBITDA
Add-on targets: 3 acquisitions at 5x EBITDA
```

### Response

---

**Platform Investment Model**

**Entry Investment:**
- Platform EBITDA: $12.5M
- Purchase price: $100M (8x)
- Equity: $50M (50% LTV)
- Debt: $50M (4x EBITDA)

**Add-On Strategy:**

| Target | EBITDA | Multiple | Price | Synergies |
|--------|--------|----------|-------|-----------|
| Add-on 1 | $3M | 5x | $15M | $1M |
| Add-on 2 | $4M | 5x | $20M | $1.5M |
| Add-on 3 | $5M | 5x | $25M | $2M |
| Total | $12M | 5x | $60M | $4.5M |

**Pro Forma Platform:**
- Combined EBITDA: $29M ($12.5M + $12M + $4.5M)
- Total invested: $110M equity
- Exit multiple: 8x (maintain platform multiple)
- Exit value: $232M

**Returns Analysis:**

| Scenario | Exit Multiple | Value | MOIC | IRR |
|----------|-------------|-------|------|-----|
| Downside | 6x | $174M | 1.6x | 10% |
| Base | 8x | $232M | 2.1x | 16% |
| Upside | 10x | $290M | 2.6x | 22% |

**Multiple Arbitrage:**
- Buy add-ons: 5x
- Sell consolidated: 8x
- Arbitrage value: $36M (3x × $12M)

**Value Creation Waterfall:**

| Source | Value | % of Total |
|--------|-------|------------|
| Entry multiple | $100M | 43% |
| EBITDA growth | $32M | 14% |
| Add-on arbitrage | $36M | 15% |
| Synergies | $36M | 15% |
| Multiple expansion | $28M | 12% |
| Total | $232M | 100% |

**Key Risks:**
- Integration execution
- Add-on sourcing/pricing
- Debt refinancing
- Multiple compression

---

## Customization Patterns

### Adding Analysis

```
Add Monte Carlo simulation for returns distribution
```

### Changing Assumptions

```
Change exit multiple to 10x and show sensitivity
```

### Expanding Sections

```
Expand competitive analysis with detailed positioning
```

### Different Formats

```
Generate one-page investment summary instead of full memo
```

---

*For operational protocols, see [SKILL.md](./SKILL.md)*
*For implementation details, see [IMPLEMENTATION-GUIDE.md](./IMPLEMENTATION-GUIDE.md)*
