---
name: portfolio-intelligence
description: Cross-portfolio performance analytics, strategic allocation optimization, and risk correlation analysis. Use for quarterly portfolio reviews, LP reporting, fund performance analysis, strategic allocation decisions, and impact measurement across investments. Generates interactive dashboards, performance attribution analysis, and strategic recommendations for portfolio construction and rebalancing.
---

# Portfolio Intelligence Skill

Transform portfolio management from spreadsheet aggregation into strategic intelligence generation.

## Core Capabilities

This skill provides institutional-grade portfolio analytics including:
- Cross-portfolio performance measurement and attribution
- Risk correlation and concentration analysis
- Strategic allocation optimization
- Impact and ESG integration
- Scenario stress testing across portfolio
- Interactive dashboard generation
- LP reporting automation

## Workflow Architecture

### Phase 1: Portfolio Data Aggregation
Systematically gather data across all portfolio companies and funds.

### Phase 2: Performance Analytics
Calculate returns, attribution, and comparative benchmarks.

### Phase 3: Risk Analysis
Assess correlations, concentrations, and scenario impacts.

### Phase 4: Strategic Insights
Generate allocation recommendations and rebalancing strategies.

## Data Collection Protocol

### Portfolio Structure Mapping
```python
# Map the complete portfolio hierarchy
portfolio_structure = {
    'funds': {
        'fund_1': {
            'vintage': 2021,
            'size': 250000000,
            'strategy': 'growth_equity',
            'investments': []
        },
        'fund_2': {
            'vintage': 2023,
            'size': 350000000,
            'strategy': 'venture',
            'investments': []
        }
    },
    'direct_investments': [],
    'co_investments': []
}
```

### Company-Level Data Requirements
For each portfolio company, gather:
- Current valuation and ownership percentage
- Revenue, EBITDA, and growth metrics
- Recent round details and valuation changes
- Operating KPIs and milestones
- Exit timeline and strategy
- Impact metrics (if applicable)

### Market Data Integration
Pull relevant indices and benchmarks:
- Public market equivalents (S&P 500, Russell 2000)
- Sector-specific indices
- Private market benchmarks (Cambridge Associates)
- Currency rates for international portfolios
- Risk-free rates for Sharpe calculations

## Performance Measurement Framework

### Returns Calculation Methodology

#### Time-Weighted Returns (TWR)
For period performance reporting:
```python
def calculate_twr(portfolio_values, cash_flows):
    """
    Calculate time-weighted returns removing cash flow impacts.
    Used for performance comparison across portfolios.
    """
    periods = []
    for i in range(1, len(portfolio_values)):
        period_return = (portfolio_values[i] - cash_flows[i]) / portfolio_values[i-1] - 1
        periods.append(1 + period_return)

    twr = np.prod(periods) - 1
    return twr
```

#### Money-Weighted Returns (IRR)
For actual investor returns:
```python
def calculate_irr(cash_flows, dates):
    """
    Calculate internal rate of return including all cash flows.
    Reflects actual investor experience.
    """
    # Implementation using scipy.optimize
    pass
```

### Performance Attribution Analysis

Break down returns by multiple dimensions:

#### Sector Attribution
- Technology: +450 bps
- Healthcare: +230 bps
- Consumer: -120 bps
- Industrial: +80 bps

#### Vintage Attribution
- 2020 vintage: 35% IRR
- 2021 vintage: 28% IRR
- 2022 vintage: 18% IRR
- 2023 vintage: 22% IRR

#### Stage Attribution
- Seed: 45% gross IRR
- Series A: 32% gross IRR
- Series B+: 25% gross IRR
- Growth: 20% gross IRR

#### Geography Attribution
- North America: 60% of value creation
- Europe: 25% of value creation
- Asia-Pacific: 10% of value creation
- Latin America: 5% of value creation

## Risk Analytics Framework

### Correlation Matrix Construction

Build comprehensive correlation analysis:
```python
correlation_dimensions = [
    'sector_correlation',      # Technology, Healthcare, Consumer, etc.
    'stage_correlation',        # Seed, A, B, Growth
    'geography_correlation',    # Regional exposure
    'currency_correlation',     # FX risk
    'economic_correlation'      # GDP sensitivity
]
```

### Concentration Risk Assessment

#### Single Position Limits
Flag when any position exceeds:
- 15% of total portfolio value
- 20% of committed capital
- 25% of a single fund

#### Sector Concentration
Monitor sector exposure:
- Warning: >40% in single sector
- Critical: >50% in single sector

#### Correlation Clustering
Identify hidden concentrations:
- Companies with correlated revenue drivers
- Geographic cluster risk
- Supply chain dependencies

### Value at Risk (VaR) Calculation

Calculate portfolio VaR at 95% and 99% confidence:
```python
def calculate_portfolio_var(returns, confidence_level=0.95):
    """
    Calculate Value at Risk using historical simulation.
    """
    sorted_returns = np.sort(returns)
    index = int((1 - confidence_level) * len(sorted_returns))
    var = sorted_returns[index]

    # Also calculate CVaR (Conditional VaR)
    cvar = sorted_returns[:index].mean()

    return var, cvar
```

## Strategic Allocation Framework

### Modern Portfolio Theory Application

Optimize allocation using Markowitz framework:
```python
def optimize_portfolio(expected_returns, covariance_matrix, constraints):
    """
    Find efficient frontier and optimal allocations.
    """
    # Maximize Sharpe ratio
    # Subject to constraints (min/max positions, sector limits)
    pass
```

### Allocation Constraints

Apply institutional constraints:
- Minimum position size: $5M or 2% of fund
- Maximum position size: $50M or 15% of fund
- Sector limits: Max 40% in any sector
- Stage diversification: At least 3 stages
- Geographic diversification: Max 70% in single region

### Rebalancing Triggers

Monitor for rebalancing signals:
- Position exceeds target allocation by >5%
- Correlation increases above threshold
- Risk metrics exceed limits
- Strategic priorities shift
- Exit opportunities arise

## Scenario Analysis Engine

### Macro Scenario Testing

Test portfolio under conditions:

#### Recession Scenario
- Revenue growth: -20% to -40%
- Valuations: -30% to -50%
- Exit timeline: +2-3 years
- Default rate: 15-20%

#### High Inflation Scenario
- Margin compression: -500 to -1000 bps
- Discount rate increase: +300 bps
- Asset revaluation: Mixed
- FX volatility: High

#### Tech Correction Scenario
- Tech multiples: -40%
- Non-tech: -10%
- Flight to quality dynamics
- Dry powder advantage

### Company-Specific Stress Tests

Model individual company shocks:
- Loss of major customer (concentration risk)
- Regulatory change impact
- Competitive disruption
- Key person departure
- Technology obsolescence

## Dashboard Generation

### Executive Dashboard Structure

Create interactive HTML dashboard with:

#### Portfolio Overview Section
- Total portfolio value and IRR
- Quarterly performance vs. benchmarks
- Key metrics summary (DPI, TVPI, MOIC)
- Capital deployment and distribution pace

#### Performance Analytics Section
- Returns attribution waterfall chart
- Vintage year performance comparison
- J-curve visualization by fund
- Rolling IRR trends

#### Risk Monitoring Section
- Correlation heat map
- Concentration warnings
- VaR and stress test results
- Early warning indicators

#### Company Spotlight Section
- Top performers and detractors
- Recent valuation changes
- Upcoming exit opportunities
- Companies requiring attention

#### Strategic Allocation Section
- Current vs. target allocation
- Rebalancing recommendations
- Efficient frontier visualization
- Scenario impact analysis

### Interactive Features

Implement using Chart.js and JavaScript:
```javascript
// Enable drill-down capabilities
chart.options.onClick = function(event, elements) {
    if (elements.length > 0) {
        const dataIndex = elements[0].index;
        showCompanyDetails(dataIndex);
    }
};

// Add filtering controls
document.getElementById('sectorFilter').addEventListener('change', function(e) {
    updateDashboard({sector: e.target.value});
});

// Implement date range selection
const dateRangePicker = new DateRangePicker({
    onChange: function(start, end) {
        refreshAnalytics(start, end);
    }
});
```

## Impact Measurement Integration

### Impact Metrics Framework

Track portfolio impact across dimensions:

#### Social Impact
- Jobs created/sustained
- Beneficiaries served
- Access improvement metrics
- Community investment

#### Environmental Impact
- Carbon reduction (tCO2e)
- Resource efficiency gains
- Renewable energy capacity
- Circular economy metrics

#### Governance Impact
- Board diversity improvement
- Ethics policy implementation
- Stakeholder engagement scores
- Transparency indices

### SROI Calculation

Calculate Social Return on Investment:
```python
def calculate_sroi(financial_return, impact_metrics):
    """
    Blend financial and impact returns.
    """
    # Monetize impact outcomes
    social_value = sum([
        metric['value'] * metric['monetization_factor']
        for metric in impact_metrics
    ])

    # Calculate blended return
    total_value = financial_return + social_value
    sroi = total_value / investment_amount

    return sroi
```

## LP Reporting Automation

### Quarterly Report Generation

Automate standard LP reporting package:

#### Performance Summary
- Fund and portfolio company performance
- Capital account statements
- Benchmark comparisons
- Fee and carry calculations

#### Portfolio Review
- New investments and exits
- Valuation changes and rationale
- Portfolio company highlights
- Strategic initiatives update

#### Market Commentary
- Sector trends and opportunities
- Competitive dynamics
- Regulatory developments
- Economic outlook

#### Appendices
- Detailed financials by company
- Legal and compliance updates
- Team and organizational changes
- Upcoming capital calls schedule

### Custom Report Builder

Enable dynamic report generation:
```python
def build_custom_report(template, data_filters, sections):
    """
    Generate tailored reports for specific LP requests.
    """
    report = ReportBuilder(template)

    # Apply LP-specific filters
    filtered_data = apply_filters(portfolio_data, data_filters)

    # Build requested sections
    for section in sections:
        if section == 'geographic_analysis':
            report.add_geographic_breakdown(filtered_data)
        elif section == 'esg_metrics':
            report.add_esg_scorecard(filtered_data)
        # ... additional sections

    return report.generate()
```

## Quality Assurance Protocol

### Data Validation Checks
- [ ] Valuations sum to reported NAV
- [ ] Cash flows reconcile to capital accounts
- [ ] Performance calculations match across methods
- [ ] All portfolio companies accounted for
- [ ] Benchmark data is current

### Analytics Validation
- [ ] Correlation matrices are positive definite
- [ ] VaR calculations pass backtesting
- [ ] Attribution sums to total return
- [ ] Stress test scenarios are realistic
- [ ] Optimization constraints are satisfied

### Report Quality Review
- [ ] Numbers tie across all sections
- [ ] Visualizations accurately represent data
- [ ] Text narrative matches quantitative analysis
- [ ] Formatting is consistent throughout
- [ ] Interactive features function properly

## Using Bundled Resources

### Scripts
- `scripts/portfolio_aggregator.py` - Consolidate data across sources
- `scripts/performance_calculator.py` - TWR, IRR, and attribution
- `scripts/risk_analyzer.py` - Correlation and VaR calculations
- `scripts/allocation_optimizer.py` - Portfolio optimization
- `scripts/dashboard_generator.py` - Interactive HTML creation

### References
- `references/benchmark_definitions.md` - Standard benchmark descriptions
- `references/risk_metrics.md` - Risk calculation methodologies
- `references/impact_frameworks.md` - Impact measurement standards
- `references/lp_requirements.md` - Common LP reporting needs

### Assets
- `assets/dashboard_template.html` - Base dashboard structure
- `assets/charts_config.js` - Chart.js configurations
- `assets/report_template.docx` - LP report formatting
- `assets/styles.css` - Dashboard styling

## Advanced Techniques

### Machine Learning Applications

#### Exit Prediction Model
Use ML to predict exit timing and multiples:
- Features: Revenue growth, market conditions, comparables
- Output: Probability of exit by year, expected multiple

#### Pattern Recognition
Identify success patterns across portfolio:
- Cluster analysis of winning investments
- Feature importance for returns
- Early warning signal detection

### Real-Time Monitoring

Implement alerting system:
```python
def monitor_portfolio_triggers(portfolio, thresholds):
    """
    Real-time monitoring for critical events.
    """
    alerts = []

    # Check each trigger condition
    if portfolio.concentration_risk > thresholds['concentration']:
        alerts.append(('HIGH', 'Concentration risk exceeded'))

    if portfolio.correlation > thresholds['correlation']:
        alerts.append(('MEDIUM', 'Correlation increasing'))

    # Send notifications
    if alerts:
        send_alert_notifications(alerts)
```

## Integration with 360 Ecosystem

### Asana Portfolio Tracking
- Sync portfolio companies as Asana projects
- Track milestones and board meetings
- Monitor action items and follow-ups

### Document Management
- Link to deal documents in Google Drive
- Access board decks and financials
- Maintain investment memos archive

### Executive Briefing Integration
- Feed into weekly intelligence brief
- Highlight material changes
- Surface strategic decisions needed

Remember: Portfolio intelligence is about pattern recognition and strategic insight, not just performance reporting. Every analysis should inform better allocation decisions and risk management.
