# Financial Dashboard Workflow
## Specialized Reference for Board Packet Financial Section

This file is loaded just-in-time when generating the Financial Dashboard component of the board packet.

---

## Purpose

Transform raw financial data from QuickBooks and Asana into an executive-grade financial dashboard that tells the story of 360's financial health, identifies risks, and projects future performance.

---

## Data Inputs

### From QuickBooks (via MCP or CSV)

**Revenue Data**:
- Total revenue YTD
- Revenue by source/category:
  - Consulting services
  - Licensing fees
  - Grant income
  - Other income
- Revenue by client (if available)
- Budget vs. actual (if budget exists in QB)

**Expense Data**:
- Total expenses YTD
- Expenses by category:
  - Personnel/contractor costs
  - Professional services
  - Software/technology
  - Travel
  - Office/administrative
  - Other
- Budget vs. actual

**Cash Flow Data**:
- Current cash position
- Accounts receivable total
- AR aging report (0-30, 31-60, 61-90, 90+ days)
- Accounts payable (if needed)

**Historical Data** (if available):
- Prior year same period comparison
- Prior quarter comparison

### From Asana Client Delivery Hub

**Pipeline Data**:
- All projects with contract_value and probability fields
- Filter by stage:
  - Proposal (probability × value)
  - Negotiation (probability × value)
  - Signed (100% × value, if not yet in QB revenue)
  - Delivered (should be in QB, verify)
  - Invoiced (should be in QB AR)
  - Paid (should be in QB revenue)

**Cross-Validation**:
- Compare Asana "Paid" stage contract values with QB revenue
- Flag discrepancies >$1,000

---

## Dashboard Structure

### 1. Executive Summary (1 Paragraph)

Synthesize the full financial picture in 3-5 sentences:

**Template**:
"As of [date], 360 has generated $[X] in revenue against an annual target of $40,000, representing [X]% achievement. The organization maintains [X] months of cash runway with $[X] in current assets and $[X] in outstanding receivables. The weighted pipeline totals $[X] across [Y] opportunities, with $[Z] projected to close this quarter. [Major risk or opportunity, e.g., 'A concentration of $[X] in receivables >60 days requires collection attention.']"

**Key elements**:
- Revenue achievement vs. target
- Cash position and runway
- Pipeline value and timing
- One critical flag or opportunity

**Tone**: Direct, factual, action-oriented. No fluff.

---

### 2. Revenue Analysis

#### 2.1 Year-to-Date Performance

**Table Format**:

| Category | YTD Actual | Annual Budget | % of Budget | Variance |
|----------|-----------|---------------|-------------|----------|
| Consulting Services | $[X] | $[Y] | [X]% | $[±Z] |
| Licensing Fees | $[X] | $[Y] | [X]% | $[±Z] |
| Grant Income | $[X] | $[Y] | [X]% | $[±Z] |
| Other Income | $[X] | $[Y] | [X]% | $[±Z] |
| **Total Revenue** | **$[X]** | **$40,000** | **[X]%** | **$[±Z]** |

**Narrative** (2-3 sentences):
"Consulting services represent [X]% of revenue, primarily from [top 2-3 clients]. Licensing fees from [partnership name] contributed $[X]. [Any notable variance explanation, e.g., 'Grant income is below budget due to timing delays in the Brazil partnership launch.']"

#### 2.2 Revenue by Client (Top 5)

**Table Format**:

| Client | Contract Value | Revenue Recognized | % of Total Revenue |
|--------|---------------|-------------------|-------------------|
| [Client 1] | $[X] | $[Y] | [Z]% |
| [Client 2] | $[X] | $[Y] | [Z]% |
| [Client 3] | $[X] | $[Y] | [Z]% |
| [Client 4] | $[X] | $[Y] | [Z]% |
| [Client 5] | $[X] | $[Y] | [Z]% |
| **Top 5 Total** | **$[X]** | **$[Y]** | **[Z]%** |
| All Others | $[X] | $[Y] | [Z]% |
| **Grand Total** | **$[X]** | **$[Y]** | **100%** |

**Flag**: If top client >40% of revenue, note: "⚠️ Revenue concentration: [Client name] represents [X]% of total revenue, indicating concentration risk."

#### 2.3 Revenue Trends (if historical data available)

**Comparison Format**:
- This quarter vs. prior quarter
- This YTD vs. same period last year

"Revenue has [increased/decreased] by $[X] ([Y]%) compared to [prior period], driven primarily by [explanation]."

---

### 3. Expense Analysis

#### 3.1 Expense Breakdown

**Table Format**:

| Category | YTD Actual | Annual Budget | % of Budget | Variance |
|----------|-----------|---------------|-------------|----------|
| Personnel/Contractors | $[X] | $[Y] | [X]% | $[±Z] |
| Professional Services | $[X] | $[Y] | [X]% | $[±Z] |
| Software/Technology | $[X] | $[Y] | [X]% | $[±Z] |
| Travel | $[X] | $[Y] | [X]% | $[±Z] |
| Office/Administrative | $[X] | $[Y] | [X]% | $[±Z] |
| Other | $[X] | $[Y] | [X]% | $[±Z] |
| **Total Expenses** | **$[X]** | **$[Y]** | **[X]%** | **$[±Z]** |

**Narrative** (2-3 sentences):
"Personnel and contractor costs account for [X]% of total expenses, reflecting [context, e.g., 'the lean operational model']. Professional services include [breakdown if significant]. [Any variance >20% requires explanation]."

#### 3.2 Expense Efficiency Metrics

**Operating Margin**:
- Revenue: $[X]
- Expenses: $[Y]
- Net: $[Z]
- Margin: [X]%

"360 is operating at a [positive/negative] margin of [X]%, [improving/declining] from [prior period comparison if available]."

---

### 4. Cash Flow & Receivables

#### 4.1 Cash Position

**Current State**:
- Cash on hand: $[X]
- Monthly burn rate: $[Y] (average expenses ÷ months)
- Cash runway: [Z] months

**Flag Thresholds**:
- <6 months runway: ⚠️ Yellow flag
- <3 months runway: 🚨 Red flag - immediate attention needed

#### 4.2 Accounts Receivable Aging

**Table Format**:

| Aging Period | Amount | % of Total AR | Key Clients |
|-------------|--------|--------------|-------------|
| Current (0-30 days) | $[X] | [Y]% | [List if >$5K each] |
| 31-60 days | $[X] | [Y]% | [List] |
| 61-90 days | $[X] | [Y]% | [List] |
| 90+ days | $[X] | [Y]% | [List] |
| **Total AR** | **$[X]** | **100%** | |

**Flags**:
- Any amount in 61-90 days: ⚠️ "Requires follow-up: [Client name], $[X], invoice dated [date]"
- Any amount in 90+ days: 🚨 "Urgent collection needed: [Client name], $[X], invoice dated [date]"

**Narrative**:
"Outstanding receivables total $[X], with [X]% current. [If flags exist: 'Collection efforts are needed on $[X] in receivables >60 days, primarily from [client names].' If clean: 'Receivables are healthy with [X]% collected within 30 days.']"

#### 4.3 Collection Assumptions

If significant AR exists, note expected collection timing:
"Based on client payment patterns:
- $[X] expected to collect in [month]
- $[X] expected to collect in [month]
- $[X] requires collection action (>90 days)"

---

### 5. Pipeline Valuation

#### 5.1 Weighted Pipeline

From Asana Client Delivery Hub, calculate weighted pipeline:

**Formula**: Contract Value × Probability

**Table Format**:

| Stage | # of Opportunities | Total Value | Weighted Value | Expected Close |
|-------|-------------------|-------------|---------------|----------------|
| Proposal | [X] | $[Y] | $[Z] | [Quarter] |
| Negotiation | [X] | $[Y] | $[Z] | [Quarter] |
| Signed (not invoiced) | [X] | $[Y] | $[Y] | [Quarter] |
| **Total Pipeline** | **[X]** | **$[Y]** | **$[Z]** | |

**Narrative**:
"The current pipeline contains $[total value] in opportunities with a weighted value of $[weighted]. [X]% of the weighted pipeline is expected to close in [current quarter]. Major opportunities include:
- [Client 1]: $[X] at [Y]% probability, [stage]
- [Client 2]: $[X] at [Y]% probability, [stage]"

#### 5.2 Pipeline Health Indicators

**Velocity**:
- Average time from Proposal → Signed: [X] days
- Average time from Signed → Paid: [Y] days

**Conversion Rates** (if historical data available):
- Proposal → Negotiation: [X]%
- Negotiation → Signed: [Y]%
- Overall Proposal → Signed: [Z]%

**Pipeline Coverage**:
- Remaining revenue target for year: $[X]
- Weighted pipeline: $[Y]
- Coverage ratio: [Z]x

"To meet the annual target of $40,000, 360 needs to close $[remaining amount]. The weighted pipeline provides [X]x coverage, [indicating adequate/insufficient] pipeline health."

---

### 6. Risk Assessment & Recommendations

#### 6.1 Identified Risks

**Financial Risks** (flag any that apply):
- ⚠️ Revenue concentration: [X]% from single client
- ⚠️ Cash runway <6 months: [X] months remaining
- ⚠️ Receivables >60 days: $[X] outstanding
- ⚠️ Budget variance >20%: [Category] is [over/under] by [X]%
- ⚠️ Pipeline gap: Weighted pipeline only [X]x of remaining target

**Operational Risks**:
- ⚠️ Expense category trending above budget: [Category]
- ⚠️ Irregular cash flow patterns
- ⚠️ Dependency on single revenue source

#### 6.2 Board Action Recommendations

Based on identified risks, provide specific recommended actions:

**If cash runway <6 months**:
"**Recommended Action**: Board should approve accelerated collection efforts and consider short-term credit facility to bridge cash flow gaps."

**If revenue concentration >40%**:
"**Recommended Action**: Prioritize pipeline diversification efforts. Strategic priority: Convert [X] smaller opportunities to reduce dependency on [major client]."

**If receivables >60 days**:
"**Recommended Action**: Authorize executive-level outreach to [client names] for receivables collection. Consider payment plan negotiations if needed."

**If pipeline gap exists**:
"**Recommended Action**: Board should discuss resource allocation for business development. Current pipeline insufficient to meet annual targets without additional effort."

---

## Data Collection Logic

### QuickBooks MCP Available

```python
def collect_quickbooks_data():
    """Collect financial data via QuickBooks MCP integration"""

    # Revenue data
    revenue_ytd = quickbooks_query("revenue", period="YTD", year=2025)
    revenue_by_category = quickbooks_query("revenue", group_by="category", period="YTD")
    revenue_by_client = quickbooks_query("revenue", group_by="customer", period="YTD")

    # Expense data
    expenses_ytd = quickbooks_query("expenses", period="YTD", year=2025)
    expenses_by_category = quickbooks_query("expenses", group_by="category", period="YTD")

    # Cash flow
    cash_position = quickbooks_query("cash", as_of="today")
    ar_aging = quickbooks_query("ar_aging")

    # Budget (if available)
    try:
        budget_data = quickbooks_query("budget", year=2025)
    except:
        budget_data = None  # Will use manual target of $40K

    return {
        'revenue_ytd': revenue_ytd,
        'revenue_by_category': revenue_by_category,
        'revenue_by_client': revenue_by_client,
        'expenses_ytd': expenses_ytd,
        'expenses_by_category': expenses_by_category,
        'cash_position': cash_position,
        'ar_aging': ar_aging,
        'budget': budget_data,
        'data_source': 'QuickBooks MCP',
        'as_of_date': datetime.now()
    }
```

### QuickBooks CSV Export (Fallback)

```python
def collect_quickbooks_csv(csv_path):
    """Process QuickBooks CSV export"""
    import csv

    # User should provide CSVs for:
    # - ProfitLoss.csv (revenue and expenses)
    # - ARAgingDetail.csv (receivables)
    # - BalanceSheet.csv (cash position)

    # Parse and structure data similar to MCP format
    # Flag data source and date

    return {
        'data_source': f'QuickBooks CSV Export',
        'as_of_date': '[User-provided date]',
        'note': 'Manual export - may not reflect real-time data'
    }
```

### Asana Pipeline Data

```python
def collect_pipeline_data():
    """Collect pipeline data from Asana Client Delivery Hub"""

    portfolio_gid = "1211712180134240"
    projects = asana_get_items_for_portfolio(portfolio_gid)

    pipeline = []
    for project in projects:
        # Get project details
        project_data = asana_get_project(project['gid'])

        # Extract custom fields
        contract_value = get_custom_field(project_data, 'contract_value')
        probability = get_custom_field(project_data, 'probability')
        stage = get_custom_field(project_data, 'stage')
        client_tier = get_custom_field(project_data, 'client_tier')
        expected_close = get_custom_field(project_data, 'expected_close_date')

        # Calculate weighted value
        weighted_value = contract_value * (probability / 100) if contract_value and probability else 0

        pipeline.append({
            'client_name': project_data['name'],
            'contract_value': contract_value,
            'probability': probability,
            'stage': stage,
            'client_tier': client_tier,
            'expected_close': expected_close,
            'weighted_value': weighted_value,
            'last_updated': project_data['modified_at']
        })

    return pipeline
```

---

## Cross-Validation Logic

```python
def validate_financial_consistency(qb_data, asana_pipeline):
    """Cross-check financial data between systems"""

    issues = []

    # Check 1: Revenue in QB should match Asana "Paid" stage
    qb_revenue_total = qb_data['revenue_ytd']
    asana_paid_total = sum([p['contract_value'] for p in asana_pipeline if p['stage'] == 'Paid'])

    if abs(qb_revenue_total - asana_paid_total) > 1000:
        issues.append({
            'type': 'Revenue Mismatch',
            'severity': 'Warning',
            'detail': f'QB Revenue ({qb_revenue_total}) differs from Asana Paid stage ({asana_paid_total}) by ${abs(qb_revenue_total - asana_paid_total)}'
        })

    # Check 2: AR in QB should roughly match Asana "Invoiced" stage
    qb_ar_total = qb_data['ar_aging']['total']
    asana_invoiced_total = sum([p['contract_value'] for p in asana_pipeline if p['stage'] == 'Invoiced'])

    if abs(qb_ar_total - asana_invoiced_total) > 1000:
        issues.append({
            'type': 'AR Mismatch',
            'severity': 'Warning',
            'detail': f'QB AR ({qb_ar_total}) differs from Asana Invoiced stage ({asana_invoiced_total})'
        })

    # Check 3: Flag any Asana "Paid" projects not reflected in QB revenue
    for project in asana_pipeline:
        if project['stage'] == 'Paid':
            # Check if client appears in QB revenue by customer
            if project['client_name'] not in qb_data['revenue_by_client']:
                issues.append({
                    'type': 'Missing Revenue',
                    'severity': 'Error',
                    'detail': f'{project["client_name"]} marked Paid in Asana but not in QB revenue'
                })

    return issues
```

---

## Flag Generation Logic

```python
def generate_financial_flags(qb_data, pipeline_data):
    """Generate risk flags based on financial data"""

    flags = []

    # Cash runway flag
    cash = qb_data['cash_position']
    monthly_burn = qb_data['expenses_ytd'] / get_months_ytd()
    runway_months = cash / monthly_burn if monthly_burn > 0 else float('inf')

    if runway_months < 3:
        flags.append({
            'severity': 'Critical',
            'category': 'Cash Flow',
            'message': f'🚨 Critical: Only {runway_months:.1f} months cash runway remaining',
            'recommendation': 'Immediate board action needed on cash management and collection'
        })
    elif runway_months < 6:
        flags.append({
            'severity': 'Warning',
            'category': 'Cash Flow',
            'message': f'⚠️ Warning: {runway_months:.1f} months cash runway',
            'recommendation': 'Monitor cash closely, accelerate collection efforts'
        })

    # Receivables aging flag
    ar_aging = qb_data['ar_aging']
    if ar_aging['61_90_days'] > 0 or ar_aging['90_plus_days'] > 0:
        overdue_total = ar_aging['61_90_days'] + ar_aging['90_plus_days']
        flags.append({
            'severity': 'Warning',
            'category': 'Collections',
            'message': f'⚠️ ${overdue_total:,.0f} in receivables >60 days old',
            'recommendation': 'Prioritize collection efforts on aged receivables'
        })

    # Revenue concentration flag
    if qb_data['revenue_by_client']:
        top_client_revenue = max(qb_data['revenue_by_client'].values())
        total_revenue = qb_data['revenue_ytd']
        concentration_pct = (top_client_revenue / total_revenue * 100) if total_revenue > 0 else 0

        if concentration_pct > 40:
            flags.append({
                'severity': 'Info',
                'category': 'Revenue Concentration',
                'message': f'ℹ️ {concentration_pct:.0f}% of revenue from single client',
                'recommendation': 'Continue pipeline diversification efforts'
            })

    # Budget variance flags
    for category, actual in qb_data['expenses_by_category'].items():
        if 'budget' in qb_data and category in qb_data['budget']['expenses']:
            budget = qb_data['budget']['expenses'][category]
            variance_pct = ((actual - budget) / budget * 100) if budget > 0 else 0

            if abs(variance_pct) > 20:
                flags.append({
                    'severity': 'Info',
                    'category': 'Budget Variance',
                    'message': f'ℹ️ {category} expenses {variance_pct:+.0f}% vs budget',
                    'recommendation': f'Review {category} spending patterns'
                })

    # Pipeline coverage flag
    revenue_target = 40000
    revenue_achieved = qb_data['revenue_ytd']
    revenue_remaining = revenue_target - revenue_achieved
    weighted_pipeline = sum([p['weighted_value'] for p in pipeline_data])
    coverage_ratio = weighted_pipeline / revenue_remaining if revenue_remaining > 0 else 0

    if coverage_ratio < 1.0:
        flags.append({
            'severity': 'Warning',
            'category': 'Pipeline',
            'message': f'⚠️ Pipeline coverage only {coverage_ratio:.1f}x of remaining revenue target',
            'recommendation': 'Increase business development efforts to meet annual target'
        })

    return flags
```

---

## Output Format (Markdown for Draft)

```markdown
# FINANCIAL DASHBOARD

## Executive Summary

[Generated summary paragraph]

---

## Revenue Analysis

### Year-to-Date Performance

[Table: Revenue by category]

[Narrative paragraph]

### Revenue by Client

[Table: Top 5 clients]

[Narrative + concentration flag if applicable]

### Revenue Trends

[Comparison to prior periods if data available]

---

## Expense Analysis

### Expense Breakdown

[Table: Expenses by category]

[Narrative paragraph]

### Operating Margin

[Margin calculation and context]

---

## Cash Flow & Receivables

### Cash Position

- **Cash on hand**: $[X]
- **Monthly burn rate**: $[Y]
- **Cash runway**: [Z] months

[Flag if <6 months]

### Accounts Receivable Aging

[Table: AR aging]

[Narrative + flags for >60 day AR]

---

## Pipeline Valuation

### Weighted Pipeline

[Table: Pipeline by stage]

[Narrative on major opportunities]

### Pipeline Health

[Velocity metrics, conversion rates, coverage ratio]

---

## Risk Assessment & Recommendations

### Identified Risks

[Bulleted list of all flagged risks]

### Board Action Recommendations

[Specific recommended actions based on risks]

---

*Financial data as of [date] from [QuickBooks MCP/CSV Export]*
*Pipeline data from Asana Client Delivery Hub as of [date]*
```

---

## Final Conversion to DOCX

When main SKILL.md calls for DOCX generation, apply formatting:

- **Section headers**: Heading 1 (Arial 14pt Bold)
- **Subsection headers**: Heading 2 (Arial 12pt Bold)
- **Tables**: Calibri 11pt, borders, gray header row
- **Flags**: Keep emoji/symbols (⚠️, 🚨, ℹ️) for visual clarity
- **Spacing**: 18pt before H1, 12pt before H2

---

## User Interaction Points

**During data collection**:
- If QuickBooks unavailable: "I'll need a QuickBooks export. Can you provide Revenue, Expenses, AR Aging, and Cash Position reports?"
- If Asana custom fields missing: "I don't see contract_value or probability fields in Asana. Can you provide this data manually for [list of projects]?"

**During draft review**:
- "Here's the draft Financial Dashboard. Key flags:
  - [List all flags]

  What corrections or additions do you need?"

**After user review**:
- "Updated Financial Dashboard with your feedback. [Summary of changes]. Ready to proceed to next document?"

---

*End of Financial Dashboard Workflow*
