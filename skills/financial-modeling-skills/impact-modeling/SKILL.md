---
name: impact-modeling
description: Social return on investment (SROI) modeling, blended finance structuring, and impact-weighted accounting. Use for evaluating social enterprises, impact investments, ESG integration, sustainability metrics, and theory of change financial modeling. Generates comprehensive impact assessments that blend financial returns with social and environmental outcomes, suitable for impact investors, foundations, and mission-driven organizations.
---

# Impact Financial Modeling Skill

Transform impact measurement from qualitative narratives into quantitative financial models that capture true value creation.

## Core Capabilities

This skill provides comprehensive impact modeling workflows including:
- Social Return on Investment (SROI) calculations
- Blended finance deal structuring
- Impact-weighted accounting frameworks
- Theory of Change financial integration
- SDG contribution mapping and valuation
- Environmental and social cost accounting
- Impact risk assessment and mitigation
- Stakeholder value distribution analysis

## Philosophical Foundation

Traditional financial models capture only monetary flows, missing the broader value creation that defines impact investments. This skill bridges that gap by:

1. **Monetizing Social Value**: Converting social outcomes into financial equivalents
2. **Risk-Adjusting for Impact**: Incorporating impact risk into return calculations
3. **Stakeholder Inclusivity**: Modeling value for all stakeholders, not just investors
4. **Systems Thinking**: Capturing ripple effects and long-term systemic change
5. **Evidence-Based Valuation**: Grounding impact claims in verifiable data

## Workflow Architecture

### Phase 1: Impact Mapping (20-25 minutes)
Map theory of change to identify all impact pathways and stakeholders.

### Phase 2: Value Quantification (25-30 minutes)
Convert impact outcomes into monetary equivalents using established methodologies.

### Phase 3: Integrated Modeling (20-25 minutes)
Build unified model combining financial and impact returns.

### Phase 4: Reporting Generation (15-20 minutes)
Create impact investment memoranda and stakeholder reports.

## Theory of Change Integration

### Mapping Impact Pathways

```python
theory_of_change = {
    'inputs': {
        'financial_capital': 10000000,
        'human_capital': 50,  # FTEs
        'intellectual_capital': ['methodology', 'training'],
        'social_capital': ['partnerships', 'networks']
    },
    'activities': [
        'provide_training',
        'deliver_services',
        'build_infrastructure',
        'develop_capacity'
    ],
    'outputs': {
        'people_trained': 5000,
        'services_delivered': 100000,
        'infrastructure_built': 10,
        'organizations_strengthened': 50
    },
    'outcomes': {
        'short_term': {
            'employment_gained': 3000,
            'income_increased': 15000000,
            'access_improved': 50000
        },
        'medium_term': {
            'poverty_reduced': 10000,
            'health_improved': 25000,
            'education_completed': 5000
        },
        'long_term': {
            'systemic_change': 'market_transformation',
            'policy_influence': 'regulation_adopted',
            'ecosystem_strengthened': True
        }
    },
    'impact': {
        'lives_transformed': 100000,
        'co2_avoided': 500000,  # tons
        'inequality_reduced': 0.02  # Gini coefficient change
    }
}
```

### Outcome Valuation Framework

For each outcome, establish monetary value using:

#### Direct Valuation Methods
- **Market Prices**: Use actual market rates where available
- **Replacement Cost**: Cost to achieve outcome through alternatives
- **Opportunity Cost**: Value of next best alternative foregone

#### Revealed Preference Methods
- **Travel Cost Method**: For environmental/recreational benefits
- **Hedonic Pricing**: Extract value from related market goods
- **Defensive Expenditure**: Amount spent to avoid negative outcome

#### Stated Preference Methods
- **Contingent Valuation**: Survey-based willingness to pay
- **Choice Experiments**: Trade-off analysis for value extraction

#### Well-being Valuation
- **WELLBY**: Well-being adjusted life years
- **Life Satisfaction Approach**: Changes in reported well-being
- **QALY/DALY**: Health-related quality of life measures

## SROI Calculation Framework

### Step 1: Establish Scope and Stakeholders

```python
stakeholder_map = {
    'primary_beneficiaries': {
        'count': 10000,
        'outcomes': ['employment', 'income', 'skills'],
        'value_per_outcome': {}
    },
    'secondary_beneficiaries': {
        'families': {
            'count': 30000,
            'outcomes': ['household_income', 'stability'],
            'value_per_outcome': {}
        },
        'communities': {
            'count': 50,
            'outcomes': ['economic_development', 'social_cohesion'],
            'value_per_outcome': {}
        }
    },
    'society': {
        'outcomes': ['reduced_public_costs', 'tax_revenue', 'environmental_benefit'],
        'value_per_outcome': {}
    },
    'investors': {
        'outcomes': ['financial_return', 'impact_return', 'reputation'],
        'value_per_outcome': {}
    }
}
```

### Step 2: Map Outcomes and Evidence

For each stakeholder-outcome pair:
1. Define change indicators
2. Collect baseline and endline data
3. Calculate net change
4. Apply deadweight (what would happen anyway)
5. Apply attribution (contribution of others)
6. Apply displacement (negative elsewhere)
7. Apply drop-off (deterioration over time)

### Step 3: Value Outcomes

```python
def value_employment_outcome(jobs_created, average_wage, duration_years):
    """
    Calculate value of employment creation.
    """
    # Direct income value
    income_value = jobs_created * average_wage * duration_years

    # Multiplier effects
    local_spending_multiplier = 1.5  # Economic multiplier
    income_with_multiplier = income_value * local_spending_multiplier

    # Avoided social costs
    unemployment_benefit_saved = jobs_created * 15000 * duration_years
    healthcare_cost_saved = jobs_created * 3000 * duration_years
    crime_reduction_value = jobs_created * 2000 * duration_years

    # Well-being improvements
    wellbeing_value = jobs_created * 10000 * duration_years  # Based on life satisfaction research

    total_value = (income_with_multiplier +
                  unemployment_benefit_saved +
                  healthcare_cost_saved +
                  crime_reduction_value +
                  wellbeing_value)

    return {
        'direct_value': income_value,
        'total_value': total_value,
        'multiplier': total_value / income_value
    }
```

### Step 4: Calculate SROI

```python
def calculate_sroi(impact_values, investment, discount_rate=0.035):
    """
    Calculate Social Return on Investment.
    """
    # Sum all stakeholder values
    total_impact_value = sum(impact_values.values())

    # Apply time value (NPV calculation)
    npv_impact = calculate_npv(impact_values, discount_rate)

    # Calculate SROI ratio
    sroi_ratio = npv_impact / investment

    # Calculate blended return
    financial_return = 0.15  # 15% financial IRR
    impact_return = (sroi_ratio - 1) / investment_period
    blended_return = financial_return + impact_return

    return {
        'sroi_ratio': sroi_ratio,
        'impact_value': npv_impact,
        'financial_return': financial_return,
        'impact_return': impact_return,
        'blended_return': blended_return,
        'value_distribution': impact_values
    }
```

## Blended Finance Structuring

### Capital Stack Design

```python
blended_finance_structure = {
    'catalytic_first_loss': {
        'amount': 5000000,
        'provider': 'foundation',
        'return_expectation': -1.0,  # Grant
        'risk_coverage': 'first_20_percent_losses'
    },
    'subordinated_debt': {
        'amount': 15000000,
        'provider': 'dfi',
        'return_expectation': 0.02,  # 2%
        'risk_position': 'mezzanine'
    },
    'senior_debt': {
        'amount': 50000000,
        'provider': 'commercial_bank',
        'return_expectation': 0.06,  # 6%
        'risk_position': 'senior'
    },
    'equity': {
        'amount': 30000000,
        'provider': 'impact_investor',
        'return_expectation': 0.12,  # 12%
        'risk_position': 'equity'
    }
}
```

### Risk-Return Optimization

Balance financial returns with impact achievement:

```python
def optimize_blended_structure(total_needed, impact_target, return_requirement):
    """
    Optimize capital structure for impact and return.
    """
    # Define constraints
    constraints = {
        'min_catalytic': 0.05,  # Minimum 5% catalytic capital
        'max_catalytic': 0.20,  # Maximum 20% grants
        'min_commercial': 0.40,  # Minimum 40% commercial capital
        'debt_equity_ratio': 2.5,  # Maximum leverage
        'impact_threshold': impact_target
    }

    # Optimize for minimum blended cost of capital
    # while achieving impact targets
    # Implementation uses linear programming

    return optimal_structure
```

## Impact-Weighted Accounting

### Framework Implementation

Based on Harvard Business School Impact-Weighted Accounts:

```python
def calculate_impact_weighted_accounts(financial_statements, impact_data):
    """
    Adjust financial statements for impact.
    """

    # Environmental impacts
    environmental_costs = {
        'carbon_emissions': emissions_tons * social_cost_carbon,
        'water_usage': water_gallons * water_scarcity_cost,
        'waste_generated': waste_tons * disposal_externality,
        'pollution': pollution_units * health_cost
    }

    # Social impacts
    social_value = {
        'employment_quality': calculate_employment_value(jobs_data),
        'wage_equity': calculate_wage_premium(wage_data),
        'diversity_inclusion': calculate_diversity_value(diversity_data),
        'community_investment': community_spending * multiplier
    }

    # Product impacts
    product_impact = {
        'customer_benefit': calculate_consumer_surplus(product_data),
        'accessibility': calculate_access_value(reach_data),
        'health_safety': calculate_health_value(safety_data)
    }

    # Adjust financial statements
    adjusted_revenue = revenue + product_impact['customer_benefit']
    adjusted_opex = opex + environmental_costs['total']
    adjusted_ebitda = adjusted_revenue - adjusted_opex
    adjusted_net_income = net_income + sum(social_value.values())

    # Calculate impact-adjusted metrics
    impact_roe = adjusted_net_income / equity
    impact_multiple = enterprise_value / adjusted_ebitda

    return {
        'traditional_financials': financial_statements,
        'impact_adjustments': {
            'environmental': environmental_costs,
            'social': social_value,
            'product': product_impact
        },
        'adjusted_financials': {
            'revenue': adjusted_revenue,
            'ebitda': adjusted_ebitda,
            'net_income': adjusted_net_income
        },
        'impact_metrics': {
            'impact_roe': impact_roe,
            'impact_multiple': impact_multiple
        }
    }
```

## SDG Integration Framework

### SDG Contribution Mapping

```python
sdg_contributions = {
    'SDG_1_no_poverty': {
        'indicators': ['people_lifted_from_poverty', 'income_increased'],
        'targets': ['1.1', '1.2', '1.4'],
        'value': 5000000,
        'beneficiaries': 10000
    },
    'SDG_3_health': {
        'indicators': ['healthcare_access', 'mortality_reduced'],
        'targets': ['3.8', '3.9'],
        'value': 3000000,
        'beneficiaries': 25000
    },
    'SDG_5_gender': {
        'indicators': ['women_employed', 'wage_gap_reduced'],
        'targets': ['5.1', '5.5'],
        'value': 2000000,
        'beneficiaries': 5000
    },
    'SDG_8_decent_work': {
        'indicators': ['jobs_created', 'productivity_increased'],
        'targets': ['8.2', '8.3', '8.5'],
        'value': 8000000,
        'beneficiaries': 3000
    },
    'SDG_13_climate': {
        'indicators': ['emissions_reduced', 'resilience_built'],
        'targets': ['13.1', '13.2'],
        'value': 4000000,
        'beneficiaries': 100000
    }
}
```

### SDG Premium Calculation

Investors increasingly pay premiums for SDG-aligned investments:

```python
def calculate_sdg_premium(sdg_contributions, market_data):
    """
    Calculate valuation premium for SDG alignment.
    """
    # Base premium for any SDG contribution
    base_premium = 0.05  # 5%

    # Additional premiums for high-priority SDGs
    priority_premiums = {
        'SDG_13_climate': 0.03,  # Additional 3% for climate
        'SDG_5_gender': 0.02,    # Additional 2% for gender
        'SDG_10_inequality': 0.02  # Additional 2% for inequality
    }

    # Scale premium by contribution magnitude
    contribution_score = sum(sdg_contributions.values()) / 1000000
    magnitude_multiplier = min(contribution_score / 10, 2.0)

    # Calculate total premium
    total_premium = base_premium
    for sdg, contribution in sdg_contributions.items():
        if sdg in priority_premiums and contribution > 0:
            total_premium += priority_premiums[sdg]

    total_premium *= magnitude_multiplier

    return {
        'sdg_premium': total_premium,
        'adjusted_valuation': base_valuation * (1 + total_premium)
    }
```

## Environmental Value Accounting

### Carbon Accounting Framework

```python
def calculate_carbon_value(emissions_data):
    """
    Calculate financial value of carbon impact.
    """
    # Use multiple carbon price sources
    carbon_prices = {
        'social_cost': 51,  # US EPA social cost of carbon
        'eu_ets': 85,       # EU Emissions Trading System
        'voluntary': 30,    # Voluntary carbon market
        'internal': 100     # Internal carbon price
    }

    # Calculate avoided emissions value
    baseline_emissions = calculate_baseline(sector, size)
    actual_emissions = emissions_data['scope1'] + emissions_data['scope2']
    avoided_emissions = baseline_emissions - actual_emissions

    # Calculate sequestration value
    sequestration = emissions_data.get('sequestration', 0)

    # Total carbon value
    carbon_value = {
        'avoided_value': avoided_emissions * carbon_prices['social_cost'],
        'sequestration_value': sequestration * carbon_prices['voluntary'],
        'total_value': (avoided_emissions + sequestration) * carbon_prices['social_cost']
    }

    return carbon_value
```

### Natural Capital Valuation

```python
def value_natural_capital(ecosystem_services):
    """
    Value ecosystem services provided or protected.
    """
    # Based on TEEB methodology
    values = {
        'provisioning': {  # Food, water, materials
            'water_provision': water_gallons * 0.002,
            'food_production': food_pounds * 0.5,
            'materials': materials_tons * 50
        },
        'regulating': {  # Climate, water, pollution
            'carbon_sequestration': co2_tons * 51,
            'water_purification': water_treated * 0.1,
            'air_quality': pollution_reduced * 100
        },
        'supporting': {  # Soil, nutrients, habitat
            'soil_formation': acres * 20,
            'biodiversity': species_protected * 10000,
            'habitat': habitat_acres * 500
        },
        'cultural': {  # Recreation, aesthetic, spiritual
            'recreation_value': visitor_days * 30,
            'aesthetic_value': viewshed_acres * 10,
            'education_value': students_educated * 100
        }
    }

    total_value = sum(sum(category.values()) for category in values.values())

    return {
        'ecosystem_services': values,
        'total_natural_capital': total_value
    }
```

## Risk-Adjusted Impact Modeling

### Impact Risk Framework

Based on Impact Management Project's five dimensions:

```python
impact_risks = {
    'evidence_risk': {  # Risk that impact doesn't occur
        'probability': 0.20,
        'mitigation': 'rigorous_measurement',
        'adjustment_factor': 0.80
    },
    'external_risk': {  # Risk from external factors
        'probability': 0.15,
        'mitigation': 'scenario_planning',
        'adjustment_factor': 0.85
    },
    'stakeholder_risk': {  # Risk of stakeholder participation
        'probability': 0.10,
        'mitigation': 'engagement_strategy',
        'adjustment_factor': 0.90
    },
    'drop_off_risk': {  # Risk impact diminishes over time
        'probability': 0.30,
        'mitigation': 'sustainability_planning',
        'adjustment_factor': 0.70
    },
    'efficiency_risk': {  # Risk of inefficient delivery
        'probability': 0.25,
        'mitigation': 'operational_excellence',
        'adjustment_factor': 0.75
    }
}

def risk_adjust_impact(gross_impact, risk_profile):
    """
    Adjust impact projections for risk.
    """
    # Calculate composite risk factor
    composite_risk = 1.0
    for risk_type, risk_data in risk_profile.items():
        composite_risk *= risk_data['adjustment_factor']

    # Apply to gross impact
    risk_adjusted_impact = gross_impact * composite_risk

    # Calculate confidence intervals
    confidence_intervals = {
        'optimistic': gross_impact * min(composite_risk * 1.2, 1.0),
        'base': risk_adjusted_impact,
        'pessimistic': gross_impact * composite_risk * 0.7
    }

    return {
        'gross_impact': gross_impact,
        'risk_adjusted_impact': risk_adjusted_impact,
        'risk_discount': 1 - composite_risk,
        'confidence_intervals': confidence_intervals
    }
```

## Output Generation

### Impact Investment Memorandum

Generate comprehensive investment memo including:

1. **Executive Summary**
   - Investment thesis with impact lens
   - Blended return projections
   - Key impact metrics

2. **Theory of Change**
   - Visual logic model
   - Evidence base
   - Assumptions and risks

3. **Impact Projections**
   - Outcome forecasts by stakeholder
   - SROI calculations
   - SDG contributions

4. **Financial Analysis**
   - Traditional financial model
   - Impact-weighted accounts
   - Blended finance structure

5. **Risk Assessment**
   - Impact risk matrix
   - Mitigation strategies
   - Scenario analysis

6. **Monitoring Plan**
   - KPI framework
   - Data collection methods
   - Reporting schedule

### Interactive Impact Dashboard

Create HTML dashboard with:
- Impact vs. financial return scatter plot
- Stakeholder value distribution chart
- SDG contribution radar chart
- Theory of change flow diagram
- Real-time SROI calculator
- Scenario sensitivity analysis

## Quality Assurance Checklist

### Methodological Rigor
- [ ] Theory of change is evidence-based
- [ ] Outcome valuations use accepted methods
- [ ] Deadweight and attribution properly calculated
- [ ] Stakeholder engagement documented
- [ ] Data sources are credible and current

### Calculation Accuracy
- [ ] SROI formula correctly applied
- [ ] Discount rates are justified
- [ ] Time horizons are appropriate
- [ ] All stakeholder groups included
- [ ] Double-counting avoided

### Transparency
- [ ] Assumptions clearly stated
- [ ] Methodology documented
- [ ] Limitations acknowledged
- [ ] Sensitivity analysis included
- [ ] Alternative scenarios presented

## Using Bundled Resources

### Scripts
- `scripts/sroi_calculator.py` - Complete SROI calculation engine
- `scripts/theory_of_change_mapper.py` - ToC visualization and analysis
- `scripts/impact_valuator.py` - Outcome monetization tools
- `scripts/blended_finance_optimizer.py` - Capital structure optimization
- `scripts/sdg_mapper.py` - SDG contribution analysis

### References
- `references/valuation_methods.md` - Comprehensive outcome valuation guide
- `references/impact_frameworks.md` - IMP, IRIS+, GRI standards
- `references/proxy_database.md` - Financial proxy values database
- `references/evidence_library.md` - Impact evidence and research

### Assets
- `assets/sroi_model_template.xlsx` - Excel SROI model
- `assets/impact_dashboard.html` - Interactive dashboard template
- `assets/toc_template.pptx` - Theory of change visualization
- `assets/impact_report_template.docx` - Impact report formatting

Remember: Impact modeling is about making the invisible visible. Every model should illuminate value creation that traditional finance ignores, enabling better decisions for people and planet.
