# Content Schema Template

Use this template to provide your impact report content. Fill in all sections with your organization's data.

## Organization Information

```yaml
organization:
  name: "[Your Organization Name]"
  report_title: "Executive Impact Report FY [Year]"
  brand_color: "#FF6B35"  # Hex color code
  fiscal_year: "[Year]"
  report_date: "[Month Year]"
  audience: "Board & Executives"
```

## Section 1: Impact Overview

```yaml
impact_overview:
  # Top-line reach metrics (3 metrics)
  reach_metrics:
    - label: "Lives Impacted"
      value: "[Number]"  # e.g., "1.8M"
      description: "[How you reached them and what programs]"

    - label: "Countries Engaged"
      value: "[Number]"
      description: "[Geographic focus areas]"

    - label: "Capital Mobilized"
      value: "$[Number]"  # e.g., "$42M"
      description: "[Types of capital and alignment]"

  # Year-over-year momentum (3-5 highlights)
  momentum:
    - title: "[Percentage/multiple] increase/growth in [what]"
      badge: "[Short label]"  # e.g., "Higher depth"
      badge_type: "success"  # success (green), info (blue), warning (yellow), or null
      description: "[What this means and why it matters]"

    - title: "[Percentage] reduction in [what]"
      badge: "[Short label]"
      badge_type: "info"
      description: "[Impact of this improvement]"

    - title: "[Multiple]x growth in [what]"
      badge: null
      badge_type: null
      description: "[Scale and significance]"
```

## Section 2: Regional Portfolio

```yaml
regional_portfolio:
  # Geographic allocation (6 regions)
  regions:
    - name: "[Region Name]"  # e.g., "Latin America"
      percentage: "[XX]%"
      description: "[Focus areas and approach in this region]"

    - name: "[Region Name]"
      percentage: "[XX]%"
      description: "[What you're doing here]"

    # ... Add 4 more regions (total of 6)

  # Strategic priorities (3-5 items)
  strategic_priorities:
    - title: "[Priority name]"
      description: "[What you plan to do and why]"

    - title: "[Priority name]"
      description: "[Strategic approach and expected outcome]"

    # ... Add more priorities
```

## Section 3: Financial Performance

```yaml
financial_performance:
  # Capital overview table (4-5 key metrics)
  capital_overview:
    - metric: "Capital mobilized"
      value: "$[Number]"
      commentary: "[What this represents and timeframe]"

    - metric: "Percent deployed to [region/focus]"
      value: "[XX]%"
      commentary: "[Alignment with mission]"

    - metric: "Cost per verified outcome"
      value: "↓ [XX]% vs prior year"
      commentary: "[Efficiency improvements and drivers]"

    - metric: "Runway on committed capital"
      value: "[XX] months"
      commentary: "[Assumptions and context]"

  # Capital mix breakdown (3 categories)
  capital_mix:
    - category: "Grants and Philanthropy"
      percentage: "[XX]%"
      description: "[How this capital is used]"

    - category: "Catalytic and Blended"
      percentage: "[XX]%"
      description: "[Stage and approach]"

    - category: "Commercial Capital"
      percentage: "[XX]%"
      description: "[Revenue models and impact standards]"

  # Safeguard principles (2-3 items)
  safeguards:
    - title: "[Safeguard name]"
      description: "[How you protect mission and values]"

    - title: "[Safeguard name]"
      description: "[Risk management approach]"
```

## Section 4: Program Outcomes

```yaml
program_outcomes:
  # Three impact pillars
  pillars:
    - name: "[Pillar 1 Name]"  # e.g., "Health Access"
      label: "[Category]"  # e.g., "Primary Pillar"
      metric_label: "[What you measure]"  # e.g., "Patients Served"
      metric_value: "[Number]"  # e.g., "847K"
      metric_change: "+[XX]% from FY [Year]"
      outcomes:
        - title: "[Outcome area]"
          description: "[Specific result with metric]"

        - title: "[Outcome area]"
          description: "[Achievement and impact]"

        - title: "[Outcome area]"
          description: "[Scale and reach]"

    - name: "[Pillar 2 Name]"
      label: "[Category]"
      metric_label: "[What you measure]"
      metric_value: "[Number]"
      metric_change: "+[XX]% from FY [Year]"
      outcomes:
        - title: "[Outcome area]"
          description: "[Result]"
        # ... 2-3 more outcomes

    - name: "[Pillar 3 Name]"
      label: "[Category]"
      metric_label: "[What you measure]"
      metric_value: "[Number]"
      metric_change: "+[XX]% from FY [Year]"
      outcomes:
        - title: "[Outcome area]"
          description: "[Result]"
        # ... 2-3 more outcomes

  # Evaluation approach (3 principles)
  evaluation_approach:
    - title: "[Approach name]"
      description: "[How you ensure quality and rigor]"

    - title: "[Approach name]"
      description: "[Methodology and standards]"

    - title: "[Approach name]"
      description: "[Learning and adaptation process]"
```

## Section 5: Partnership Ecosystem

```yaml
partnerships:
  # Overall statistics (3 metrics)
  statistics:
    - label: "Active Partnerships"
      value: "[Number]"
      description: "Across [X] countries"

    - label: "New in FY [Year]"
      value: "[Number]"
      description: "Strategic collaborations launched"

    - label: "Multi-Year Agreements"
      value: "[Number]"
      description: "Committed partnerships ([XX]%)"

  # Partner categories (4 types)
  partner_categories:
    - name: "[Category name]"  # e.g., "Foundation partners"
      count: [Number]
      description: "[Role and value]"

    - name: "[Category name]"
      count: [Number]
      description: "[Contribution type]"

    - name: "[Category name]"
      count: [Number]
      description: "[Strategic importance]"

    - name: "[Category name]"
      count: [Number]
      description: "[Partnership approach]"

  # Flagship partnerships (4 highlighted)
  flagship_partnerships:
    - name: "[Partnership Name]"
      status_badge: "EXPANDED"  # or "NEW" or null
      status_type: "success"  # success (green), info (blue), or null
      description: "[Scope, commitment, and impact]"

    - name: "[Partnership Name]"
      status_badge: "NEW"
      status_type: "info"
      description: "[What this partnership enables]"

    - name: "[Partnership Name]"
      status_badge: null
      status_type: null
      description: "[Scale and significance]"

    # ... Add more flagship partnerships
```

## Section 6: Strategic Outlook

```yaml
strategic_outlook:
  # Three-horizon roadmap
  roadmap:
    - horizon: "Horizon 1 · Next 6 months"
      description: "[Immediate priorities and consolidation focus]"

    - horizon: "Horizon 2 · 6 to 18 months"
      description: "[Scaling and expansion plans]"

    - horizon: "Horizon 3 · 18 to 36 months"
      description: "[Long-term vision and positioning]"

  # Leadership asks (3-4 items)
  leadership_asks:
    - title: "[Ask title]"
      description: "[Specific request and rationale]"

    - title: "[Ask title]"
      description: "[Decision needed and impact]"

    - title: "[Ask title]"
      description: "[Investment or approval required]"

    # ... Add more asks if needed
```

---

## Quick Tips for Filling Out This Template

**Metrics and numbers:**
- Use K for thousands (e.g., "847K")
- Use M for millions (e.g., "$42M")
- Round to whole numbers or one decimal for clarity
- Always include comparison (vs FY [Year], +XX%, etc.)

**Descriptions:**
- Keep under 20 words per description for readability
- Use active voice and present tense
- Front-load key information
- Be specific with numbers and dates

**Status badges:**
- Use "EXPANDED" for partnerships/programs that grew
- Use "NEW" for initiatives launched this year
- Leave null for established ongoing work
- badge_type: "success" = green, "info" = blue, "warning" = yellow

**Regional percentages:**
- Must total 100% across all 6 regions
- Can include "Global Initiatives" as a region
- Allocate by effort/resources, not just geography

**Capital mix percentages:**
- Must total 100% across 3 categories
- Reflect actual capital deployment, not just commitments

**Completeness check:**
- All 6 sections filled out
- No [brackets] or placeholder text remaining
- Metrics include units (%, $, M, K)
- Descriptions are complete sentences
- Brand color is valid hex code (#RRGGBB)

---

## Example Filled Section

Here's what Section 1 might look like when completed:

```yaml
impact_overview:
  reach_metrics:
    - label: "Lives Impacted"
      value: "1.8M"
      description: "Individuals reached across programs in health, skills, and income generation."

    - label: "Countries Engaged"
      value: "14"
      description: "Growing footprint with focus on Latin America, Africa, and South Asia."

    - label: "Capital Mobilized"
      value: "$42M"
      description: "Blend of grant, catalytic, and commercial capital aligned to social outcomes."

  momentum:
    - title: "34% increase in high-intensity interventions"
      badge: "Higher depth of support"
      badge_type: "success"
      description: "More participants are receiving integrated services across health, skills, and income."

    - title: "22% reduction in cost per outcome"
      badge: "Operational efficiency"
      badge_type: "info"
      description: "Process redesign, digital tools, and better partner alignment reducing costs."

    - title: "3x growth in cross-border partnerships"
      badge: null
      badge_type: null
      description: "New alliances across government, industry, and civil society unlocking scale."
```

---

**Ready to generate?** Once you've filled out this template, provide it to Claude and request generation of either or both the Presentation and Executive formats.

**Questions?** Ask Claude to:
- "Help me fill out the [section name] section"
- "Show me more examples for [specific part]"
- "What should I put for [field name]?"
- "Review my content for completeness"
