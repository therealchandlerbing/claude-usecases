# Templates Directory

Model templates and configurations for the Financial Modeling Suite.

---

## Template Types

### Excel Model Templates

Templates are generated dynamically based on the analysis type:

| Template | Worksheets | Use Case |
|----------|------------|----------|
| Investment Model | 9 sheets | Growth equity, venture, buyout |
| Portfolio Dashboard | 6 sheets | Quarterly reporting |
| Comps Analysis | 4 sheets | Valuation benchmarking |
| Sensitivity Tables | 2 sheets | Variable testing |

### Output Configurations

Templates for generated outputs:

| Format | Contents |
|--------|----------|
| IC Memo | 10-15 page investment memo |
| Executive Summary | 1-page deal overview |
| LP Report | Quarterly portfolio report |
| Dashboard | Interactive HTML analytics |

---

## Excel Model Structure

### Standard Worksheets

**1. Cover/TOC**
- Deal name and date
- Table of contents with hyperlinks
- Version history

**2. Assumptions**
- All inputs in blue cells
- Clearly labeled sections
- Source documentation

**3. Revenue Build**
- Customer/segment detail
- Growth assumptions
- Seasonality factors

**4. P&L Projection**
- 5-year monthly/annual
- Key metrics calculated
- Margin analysis

**5. Balance Sheet**
- Working capital
- CapEx and D&A
- Debt schedule

**6. Cash Flow**
- Operating cash flow
- Investing activities
- Financing activities

**7. Scenarios**
- Base, upside, downside
- Toggle for easy switching
- Key driver differences

**8. Returns**
- IRR, MOIC, DPI
- By scenario
- Sensitivity tables

**9. Comps**
- Public comparables
- Transaction comps
- Valuation summary

---

## Formatting Standards

### Cell Formatting

```
Inputs: Blue text (#0066CC), light blue fill (#E8F4FD)
Calculations: Black text, white fill
Links: Green text (#008000)
Headers: Bold, dark blue (#003D7A), 12pt
Totals: Double top border
Negatives: Red text (#CC0000), parentheses
```

### Number Formatting

```
Currency: $#,##0;($#,##0)
Percentage: 0.0%
Multiples: 0.0x
Large numbers: $0.0M or $0.0B
```

### Named Ranges

```
Assumptions: a_[name]
Calculations: c_[name]
Outputs: o_[name]

Examples:
- a_revenue_growth
- a_exit_multiple
- o_irr_base
- o_moic_upside
```

---

## IC Memo Template

### Structure

```
1. Executive Summary (1 page)
   - Investment thesis
   - Key terms and returns
   - Recommendation

2. Investment Thesis (2-3 pages)
   - Market opportunity
   - Competitive position
   - Value creation plan
   - Exit strategy

3. Business Overview (3-4 pages)
   - Company history
   - Products/services
   - Customers
   - Team

4. Financial Analysis (3-4 pages)
   - Historical performance
   - Projections
   - Scenarios
   - Returns analysis

5. Risk Assessment (2 pages)
   - Key risks
   - Mitigations
   - Deal protections

6. Transaction (1 page)
   - Structure
   - Terms
   - Governance

7. Appendices
   - Detailed financials
   - Comps detail
   - DD items
```

---

## Dashboard Template

### Sections

**Portfolio Overview:**
- KPIs: NAV, IRR, TVPI, DPI
- Charts: Performance trend, vintage comparison

**Attribution:**
- Waterfall chart
- Sector/stage breakdown

**Risk:**
- Correlation matrix
- Concentration alerts

**Companies:**
- Top performers
- Action items

### Chart.js Configuration

```javascript
const chartConfig = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      position: 'bottom',
      labels: {
        font: { family: 'Inter', size: 12 }
      }
    }
  }
};

const colors = [
  '#1a1a1a',
  '#4a4a4a',
  '#7a7a7a',
  '#aaaaaa',
  '#d4d4d4'
];
```

---

## Usage Notes

Templates are generated dynamically during analysis. The skill automatically:

1. Selects appropriate template based on request
2. Populates with gathered data
3. Applies institutional formatting
4. Generates documentation

**For customization:**
- Specify format preferences in request
- Request specific worksheets or sections
- Indicate output format (Excel, memo, dashboard)

---

*For operational protocols, see [../SKILL.md](../SKILL.md)*
