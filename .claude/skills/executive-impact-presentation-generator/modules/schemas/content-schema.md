# Content Schema

## Complete Data Structure

This is the complete YAML schema for all six sections of the executive impact report.

```yaml
organization:
  name: "Organization Name"
  report_title: "Executive Impact Report FY 2025"
  brand_color: "#FF6B35"  # Hex code
  fiscal_year: "2025"
  report_date: "November 2025"
  audience: "Board & Executives"

impact_overview:
  reach_metrics:
    - label: "Lives Impacted"
      value: "1.8M"
      description: "Brief description of this metric"
    - label: "Countries Engaged"
      value: "14"
      description: "Geographic reach and focus areas"
    - label: "Capital Mobilized"
      value: "$42M"
      description: "Capital deployed and aligned to outcomes"

  momentum:
    - title: "34% increase in high-intensity interventions"
      badge: "Higher depth of support"
      badge_type: "success"  # success, info, warning, or null
      description: "Detailed explanation of this achievement"
    - title: "22% reduction in cost per outcome"
      badge: "Operational efficiency"
      badge_type: "info"
      description: "How efficiency was achieved"
    - title: "3x growth in cross-border partnerships"
      badge: null
      badge_type: null
      description: "Partnership expansion details"

regional_portfolio:
  regions:
    - name: "Latin America"
      percentage: "36%"
      description: "Regional focus and strategic priorities"
    - name: "Africa"
      percentage: "26%"
      description: "Key initiatives and partners"
    - name: "South Asia"
      percentage: "18%"
      description: "Program areas and outcomes"
    - name: "North America"
      percentage: "12%"
      description: "Domestic programs and innovation"
    - name: "Europe"
      percentage: "5%"
      description: "Strategic partnerships and learning"
    - name: "Other Regions"
      percentage: "3%"
      description: "Emerging opportunities"

  strategic_priorities:
    - title: "Brazil as a regional hub"
      description: "Establish durable presence connecting health, universities, industry"
    - title: "Health and climate intersections"
      description: "Grow work where climate, health, livelihoods overlap"
    - title: "Digital public goods"
      description: "Support reusable tools and open standards"

financial_performance:
  capital_overview:
    - metric: "Capital mobilized"
      value: "$42M"
      commentary: "Total capital under active management"
    - metric: "Percent deployed to Global South"
      value: "78%"
      commentary: "Majority directed to LMIC contexts"
    - metric: "Cost per outcome"
      value: "$23"
      commentary: "22% reduction from prior year"
    - metric: "Operating efficiency ratio"
      value: "12%"
      commentary: "Admin and overhead costs"

  capital_mix:
    - category: "Grants and Philanthropy"
      percentage: "34%"
      description: "Early-stage pilots and community engagement"
    - category: "Catalytic and Blended"
      percentage: "41%"
      description: "Ventures on path to commercial viability"
    - category: "Commercial Capital"
      percentage: "25%"
      description: "Scalable solutions with revenue models"

  safeguards:
    - title: "Guardrails on mission drift"
      description: "All commercial instruments evaluated against impact criteria"
    - title: "Risk sharing with partners"
      description: "Blended structures designed for proportional risk"

program_outcomes:
  pillars:
    - name: "Health Access"
      label: "Primary Pillar"
      metric_label: "Patients Served"
      metric_value: "847K"
      metric_change: "+41% from FY 2024"
      outcomes:
        - title: "Maternal health"
          description: "92% of mothers received prenatal care within recommended windows"
        - title: "Chronic disease management"
          description: "68% reduction in emergency visits for diabetes/hypertension"
        - title: "Telemedicine expansion"
          description: "Reached 127 remote communities without consistent access"

    - name: "Skills Development"
      label: "Secondary Pillar"
      metric_label: "Trainees"
      metric_value: "124K"
      metric_change: "+28% from FY 2024"
      outcomes:
        - title: "Digital skills"
          description: "76% employment or income increase within 6 months"
        - title: "Youth workforce readiness"
          description: "Partnerships with 34 employers for direct placement"
        - title: "Entrepreneurship training"
          description: "892 new businesses launched by graduates"

    - name: "Income Generation"
      label: "Tertiary Pillar"
      metric_label: "Microenterprises Supported"
      metric_value: "38K"
      metric_change: "+19% from FY 2024"
      outcomes:
        - title: "Access to capital"
          description: "$4.2M in microloans disbursed, 97% repayment rate"
        - title: "Market linkages"
          description: "Connected 1,200 producers to regional buyers"
        - title: "Cooperative formation"
          description: "127 new cooperatives formed, averaging 32 members"

  evaluation_approach:
    - title: "Common outcome framework"
      description: "Shared indicators enable meaningful comparison across programs"
    - title: "Mixed methods evaluation"
      description: "Quantitative data paired with qualitative community insight"
    - title: "Learning loops"
      description: "Insights from pilots feed into portfolio decisions"

partnerships:
  statistics:
    - label: "Active Partnerships"
      value: "142"
      description: "Across 38 countries"
    - label: "New in FY 2025"
      value: "37"
      description: "Strategic collaborations launched"
    - label: "Multi-Year Agreements"
      value: "89"
      description: "Committed partnerships (63%)"

  partner_categories:
    - name: "Foundation partners"
      count: 42
      description: "Global and regional foundations providing core funding"
    - name: "Corporate partners"
      count: 28
      description: "Multi-sector companies contributing expertise and resources"
    - name: "Government agencies"
      count: 18
      description: "Federal and regional government collaborators"
    - name: "Academic institutions"
      count: 24
      description: "Universities and research centers"
    - name: "NGO and civil society"
      count: 30
      description: "Implementation partners and community organizations"

  flagship_partnerships:
    - name: "Global Health Alliance"
      status_badge: "EXPANDED"
      status_type: "success"
      description: "5-year, $12M commitment supporting maternal and child health across 8 countries"
    - name: "Tech for Good Initiative"
      status_badge: "NEW"
      status_type: "info"
      description: "Partnership with 4 major tech companies providing AI tools and infrastructure"
    - name: "Regional Innovation Fund"
      status_badge: "ONGOING"
      status_type: null
      description: "Joint fund with development banks supporting social enterprises"
    - name: "University Consortium"
      status_badge: "EXPANDED"
      status_type: "success"
      description: "Research collaboration with 12 universities across 3 continents"

strategic_outlook:
  roadmap:
    - horizon: "Horizon 1 · Next 6 months"
      description: "Consolidate early wins in Brazil and anchor geographies, finalize lab and hub structures"
    - horizon: "Horizon 2 · 6 to 18 months"
      description: "Scale proven models with priority partners, expand digital public goods"
    - horizon: "Horizon 3 · 18 to 36 months"
      description: "Position organization as leading innovation partner with scalable ventures"

  leadership_asks:
    - title: "Confirm investment envelope and risk appetite"
      description: "Clarify capital deployment capacity and acceptable risk tolerance levels"
    - title: "Endorse priority partnerships"
      description: "Confirm which strategic partnerships are most important to advance"
    - title: "Invest in internal capacity"
      description: "Strengthen core team in innovation management, partnership stewardship, data systems"
```

## Required Fields by Section

### Impact Overview
- 3 reach metrics (label, value, description)
- 3-4 momentum highlights (title, badge optional, description)

### Regional Portfolio
- 6 regions (name, percentage, description)
- 3 strategic priorities (title, description)

### Financial Performance
- 4-6 capital metrics (metric, value, commentary)
- Capital mix breakdown (category, percentage, description)
- 2-3 safeguards (title, description)

### Program Outcomes
- 3 impact pillars (name, metric label, metric value, 3-4 outcomes each)
- Evaluation approach (3 principles with descriptions)

### Partnership Ecosystem
- 3 partnership statistics
- 4-6 partner categories with counts
- 4-6 flagship partnerships with status badges

### Strategic Outlook
- 3-horizon roadmap (6-18-36 month view with descriptions)
- 3-4 leadership asks (title, description)
