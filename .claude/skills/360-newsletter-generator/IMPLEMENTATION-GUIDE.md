# Implementation Guide: 360 Newsletter Generator

**Deep Knowledge Base for Executive Intelligence Production**

This guide provides comprehensive guidance on data collection, content analysis, writing standards, chart specifications, and troubleshooting for the 360 Newsletter Generator.

---

## Table of Contents

1. [Data Collection Protocols](#data-collection-protocols)
2. [Content Analysis Framework](#content-analysis-framework)
3. [Writing Style Guide](#writing-style-guide)
4. [Chart Specifications](#chart-specifications)
5. [Template Customization](#template-customization)
6. [Troubleshooting Guide](#troubleshooting-guide)
7. [Configuration Management](#configuration-management)

---

## Data Collection Protocols

### Asana Integration

**Connection Setup:**
```
1. Call asana_list_workspaces
2. Identify workspace: 360socialventures.com
3. Extract workspace_gid: 1210382795871981
4. Confirm successful connection
```

**Project Discovery:**
```
1. Call asana_search_projects with workspace_gid
2. Filter for priority projects
3. For each project:
   - Get project details
   - Get sections
   - Get custom fields
```

**Task Queries:**

For completed tasks in date range:
```
asana_search_tasks:
  workspace_gid: [gid]
  completed_since: [start_date]T00:00:00Z
  completed_before: [end_date]T23:59:59Z
  opt_fields: name,completed_at,assignee,projects,custom_fields
```

For modified/active tasks:
```
asana_search_tasks:
  workspace_gid: [gid]
  modified_since: [start_date]T00:00:00Z
  opt_fields: name,modified_at,assignee,projects,custom_fields
```

**Custom Fields to Extract:**

| Field Name | Type | Use |
|------------|------|-----|
| Pipeline Stage | Enum | Partnership status |
| Market Fit Score | Number | Opportunity ranking |
| Priority | Enum | Task importance |
| Region | Enum | Geographic distribution |
| Partner | Text | Partnership association |

### Gmail Integration

**Connection Setup:**
```
1. Call read_gmail_profile
2. Confirm email: chandler@360social.org
3. Verify search access
```

**Search Query Patterns:**

**Partnership Communications:**
```
from:(spaceplan.com OR genip.com OR sciencelink OR nanobioplus OR cnen.gov.br)
after:[YYYY/MM/DD] before:[YYYY/MM/DD]
```

**Sent Strategic Emails:**
```
from:me (agreement OR proposal OR contract OR partnership OR MOU)
after:[YYYY/MM/DD] before:[YYYY/MM/DD]
```

**Impact and Feedback:**
```
(testimonial OR feedback OR "thank you" OR impact OR outcome)
after:[YYYY/MM/DD] before:[YYYY/MM/DD]
```

**Board and Governance:**
```
(board OR governance OR fiduciary OR "board meeting")
after:[YYYY/MM/DD] before:[YYYY/MM/DD]
```

**Financial Communications:**
```
(invoice OR payment OR budget OR financial OR funding)
after:[YYYY/MM/DD] before:[YYYY/MM/DD]
```

### Google Drive Integration

**Search Query Patterns:**

**Recently Modified Strategic Docs:**
```
modifiedTime > '[YYYY-MM-DD]' and
(name contains 'strategy' or name contains 'plan' or name contains 'roadmap')
```

**Partner-Specific Documents:**
```
modifiedTime > '[YYYY-MM-DD]' and
(name contains 'SpacePlan' or fullText contains 'SpacePlan')
```

**Impact Documentation:**
```
modifiedTime > '[YYYY-MM-DD]' and
(name contains 'impact' or name contains 'metrics' or name contains 'outcomes')
```

**Financial Documents:**
```
modifiedTime > '[YYYY-MM-DD]' and
(name contains 'budget' or name contains 'financial' or name contains 'revenue')
```

**Reports and Deliverables:**
```
modifiedTime > '[YYYY-MM-DD]' and
(name contains 'report' or name contains 'deliverable')
```

### Data Quality Verification

**Checklist after collection:**
- [ ] All three sources responded successfully
- [ ] Date ranges correctly applied
- [ ] Expected project count returned
- [ ] Key partners represented
- [ ] No API errors in responses

---

## Content Analysis Framework

### Significance Scoring Algorithm

**Base Score Components:**

| Factor | Weight | Scoring Criteria |
|--------|--------|-----------------|
| Strategic Importance | 40% | Partnership stage, funding amount, board relevance |
| Stakeholder Impact | 25% | Who is affected (board, investors, partners, team) |
| Timeliness | 20% | Deadlines, windows of opportunity |
| Outcome Magnitude | 15% | Reach, financial impact, systemic change |

**Scoring Matrix:**

**95-100 Critical:**
- Partnership signatures or major agreements
- Funding milestones ($100K+)
- Board-level decisions
- Major strategic pivots
- Critical deadlines

**85-94 High:**
- Project completions with significant impact
- Partnership stage advancement
- Key hire completions
- Strategic milestone achievements
- Important client deliverables

**70-84 Medium:**
- Partnership pipeline progress
- Program updates and improvements
- Team capacity enhancements
- Process implementations
- Regular client work

**40-69 Low:**
- Routine operations updates
- Administrative completions
- Process improvements
- Internal tooling
- Documentation updates

### Section Assignment Logic

**Decision Tree:**

```
Is it about external relationships or ecosystem?
├─ Yes → Partnerships & Ecosystem
└─ No → Is it about project work or deliverables?
        ├─ Yes → Programs & Innovation
        └─ No → Is it about impact metrics or outcomes?
                ├─ Yes → Impact & Outcomes
                └─ No → Is it about team, systems, or infrastructure?
                        ├─ Yes → Operations & Capacity
                        └─ No → Strategic Horizon
```

**Content Type Mapping:**

| Content Type | Primary Section | Secondary Section |
|-------------|-----------------|-------------------|
| Partnership updates | Partnerships | Strategic Horizon |
| Client deliverables | Programs | Impact |
| Impact metrics | Impact | Executive Summary |
| Hiring updates | Operations | Executive Summary |
| Financial metrics | Operations | Executive Summary |
| Events/deadlines | Strategic Horizon | - |
| Board items | Strategic Horizon | Executive Summary |

### Lead Story Selection

**Selection Criteria (in priority order):**

1. **Highest significance score** - Typically 95+ for lead
2. **Strategic alignment** - Advances organizational mission
3. **Stakeholder relevance** - Matters to the audience
4. **Outcome magnitude** - Size of impact
5. **Timeliness** - Recent or time-sensitive

**Lead Story Format:**
- Bold headline statement
- 1-2 supporting sentences
- Key metric or outcome
- Strategic implication

### Action Item Extraction

**Identify action items when:**
- Task has future due date
- Email requests response or action
- Document is marked for review
- Meeting notes contain decisions requiring follow-up

**Action Item Format:**
- Clear action description
- Responsible owner
- Due date
- Priority level (Critical, High, Normal)

---

## Writing Style Guide

### Voice and Tone

**Grounded + Visionary:**
Balance realism with possibility. Lead with facts, connect to strategy.

**DO:**
- "The partnership positions 360 to influence technology transfer across Latin America."
- "Three enterprise opportunities advanced to negotiation, validating our cross-border approach."
- "Runway solid through Q2. Hiring increases burn but unlocks capacity for 2-3 additional client projects."

**DON'T:**
- "We're excited to announce..." (too promotional)
- "It appears that perhaps..." (too hedging)
- "Revolutionary breakthrough..." (too hyperbolic)

### Critical Formatting Rules

**NEVER use em dashes (—)**

Instead:
- Use commas for brief pauses
- Use periods for separate thoughts
- Use parentheses for clarification
- Use colons for lists or elaboration

**Wrong:** The partnership—which includes both companies—will launch in Q1.
**Right:** The partnership, which includes both companies, will launch in Q1.

### Executive Writing Principles

**Lead with impact:**
```
Good: "$150K contract signed with SpacePlan. Annual revenue increases 40%."
Bad: "After several months of negotiation, we are pleased to say that the SpacePlan deal has closed."
```

**Quantify whenever possible:**
```
Good: "Pipeline grew to $2.1M across 8 opportunities."
Bad: "Pipeline continues to show strong growth."
```

**Connect to strategy:**
```
Good: "Nadia hire enables Latin America expansion, directly supporting 2026 revenue targets."
Bad: "Nadia Rodriguez has joined the team."
```

**Use active voice:**
```
Good: "Board approved Q1 budget."
Bad: "The Q1 budget was approved by the board."
```

### Section-Specific Guidelines

**Executive Summary:**
- Maximum 4 cards
- Each card: label, value, 2-sentence detail
- Most critical information only
- No detailed explanations

**Anchor Cards ("This Week in..."):**
- Exactly 3 bullets
- Each bullet: bold label + 1 short sentence
- Lead with action or outcome

**Supporting Cards:**
- Maximum 3 per section
- Maximum 5 bullets per card
- Short, declarative sentences
- Include relevant metrics

**Chart Insights:**
- 1-2 sentences maximum
- Interpret the data (what it means)
- Connect to strategy (why it matters)

### International Awareness

**Time Zones:**
- Always note time zone for events (PT, BRT, UTC)
- Consider São Paulo time for Brazil-related items

**Cultural Context:**
- Don't assume US-centric norms
- Note Portuguese language context when relevant
- Acknowledge different business practices

---

## Chart Specifications

### Chart Type Selection Guide

| Data Story | Chart Type | When to Use |
|------------|-----------|-------------|
| Composition | Doughnut/Pie | Showing parts of whole (revenue sources, geographic split) |
| Comparison | Bar | Ranking items (pipeline stages, market fit scores) |
| Multi-dimensional | Radar | Comparing across multiple attributes (team capabilities) |
| Trend | Line | Showing change over time (revenue trajectory) |
| Part-to-whole over categories | Stacked Bar | Resource allocation across areas |

### Chart.js Configuration

**Standard Options (all charts):**
```javascript
{
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      position: 'bottom',
      labels: {
        font: { family: 'Inter', size: 12 },
        color: '#4a4a4a'
      }
    }
  }
}
```

**Monochromatic Palette:**
```javascript
colors: [
  '#1a1a1a',  // Primary black
  '#4a4a4a',  // Dark gray
  '#7a7a7a',  // Medium gray
  '#aaaaaa',  // Light gray
  '#d4d4d4',  // Lightest gray
  '#2563eb'   // Accent blue (for highlights)
]
```

### Chart Specifications by Type

**Bar Chart (Pipeline, Market Fit):**
```javascript
{
  type: 'bar',
  options: {
    indexAxis: 'y',  // Horizontal bars
    scales: {
      x: {
        beginAtZero: true,
        max: 100,
        grid: { display: false }
      }
    }
  }
}
```

**Doughnut Chart (Distribution):**
```javascript
{
  type: 'doughnut',
  options: {
    cutout: '60%',
    plugins: {
      legend: { position: 'right' }
    }
  }
}
```

**Radar Chart (Capabilities):**
```javascript
{
  type: 'radar',
  options: {
    scales: {
      r: {
        beginAtZero: true,
        max: 100,
        ticks: { stepSize: 20 }
      }
    }
  }
}
```

**Line Chart (Trends):**
```javascript
{
  type: 'line',
  options: {
    scales: {
      y: { beginAtZero: true }
    },
    elements: {
      line: { tension: 0.3 }
    }
  }
}
```

### Chart Insight Requirements

Every chart must have an insight box containing:

1. **Data interpretation**: What does this show?
2. **Strategic connection**: Why does it matter?
3. **Action implication**: What should we consider?

**Example:**
```
Innovation Compass shows highest market fit at 100%, indicating strong
product-market alignment for full-service engagements. Consider prioritizing
enterprise prospects for Q1 pipeline development.
```

---

## Template Customization

### Section Color Codes

| Section | Color | Hex Code |
|---------|-------|----------|
| Executive Summary | Gradient Blue | #667eea → #764ba2 |
| Partnerships | Blue | #3b82f6 |
| Programs | Teal | #14b8a6 |
| Impact | Purple | #8b5cf6 |
| Operations | Green | #22c55e |
| Strategy | Orange | #f97316 |

### Status Badge Classes

```css
.badge-critical {
  border-left: 4px solid #dc2626;
  background: #fef2f2;
}

.badge-action {
  border-left: 4px solid #f59e0b;
  background: #fffbeb;
}

.badge-monitoring {
  border-left: 4px solid #6b7280;
  background: #f9fafb;
}

.badge-success {
  border-left: 4px solid #22c55e;
  background: #f0fdf4;
}
```

### Timeline Configuration

```javascript
const timelineConfig = {
  week: {
    label: 'Week Ahead: Nov 15-22',
    data: [
      {
        date: 'Monday, Nov 18',
        events: [
          { text: 'Team standup 9am PT', priority: '' },
          { text: 'SpacePlan call 2pm PT', priority: 'high' }
        ]
      }
    ]
  },
  twoweeks: {
    label: 'Next Two Weeks: Nov 17-30',
    data: [/* similar structure */]
  }
};
```

---

## Troubleshooting Guide

### Data Collection Issues

**Asana returns empty results:**
- Verify workspace_gid is correct (1210382795871981)
- Check date range format (RFC3339)
- Confirm project names haven't changed
- Verify API permissions

**Gmail search fails:**
- Check date format (YYYY/MM/DD for Gmail)
- Verify search syntax (no typos in operators)
- Confirm email domains are current
- Check for special characters needing escaping

**Drive returns no documents:**
- Verify date format (YYYY-MM-DD for Drive)
- Check folder permissions
- Confirm file naming patterns
- Verify document types included

### Content Issues

**Lead story seems wrong:**
- Review significance scoring for all items
- Check for newer high-priority items missed
- Verify date filtering includes relevant period
- Manual override if scoring doesn't reflect reality

**Section appears empty:**
- Expand date range
- Check section assignment logic
- Verify content exists in data sources
- Add manual entries if data sources incomplete

**Metrics seem inaccurate:**
- Verify custom field names in Asana
- Check calculation formulas
- Confirm data extraction queries
- Cross-reference with source systems

### Technical Issues

**Charts not rendering:**
- Verify Chart.js CDN loaded
- Check canvas element IDs match
- Confirm data arrays contain valid numbers
- Check browser console for errors

**Navigation not scrolling:**
- Verify section IDs match nav href values
- Check scroll-behavior CSS
- Confirm initialization called
- Test in different browsers

**Timeline not updating:**
- Check data-view attributes on buttons
- Verify timelineConfig object structure
- Confirm toggle event handlers
- Check for JavaScript errors

**Print layout broken:**
- Verify @media print CSS
- Check page break settings
- Confirm colors print correctly
- Test with different browsers

### Performance Issues

**Generation too slow:**
- Reduce date range
- Limit number of projects scanned
- Optimize search queries
- Cache repeated lookups

**HTML file too large:**
- Compress images
- Minimize inline CSS
- Remove unused components
- Optimize chart data

---

## Configuration Management

### data-sources.json Structure

```json
{
  "workspace": {
    "asana_workspace_gid": "1210382795871981",
    "asana_workspace_name": "360socialventures.com",
    "gmail_user": "chandler@360social.org",
    "time_zone": "America/Los_Angeles"
  },
  "priority_projects": [
    "Weekly Meeting Tracker",
    "Partnership Development",
    "Client Engagements",
    "SpacePlan Joint Venture",
    "GenIP Integration",
    "CNEN Partnership"
  ],
  "key_partners": [
    {
      "name": "SpacePlan",
      "domains": ["spaceplan.com"],
      "category": "Joint Venture"
    },
    {
      "name": "GenIP",
      "domains": ["genip.com"],
      "category": "Technology Partner"
    }
  ],
  "significance_weights": {
    "strategic_importance": 0.40,
    "stakeholder_impact": 0.25,
    "timeliness": 0.20,
    "outcome_magnitude": 0.15
  },
  "section_keywords": {
    "partnerships": ["partner", "agreement", "MOU", "joint venture"],
    "programs": ["project", "deliverable", "assessment", "client"],
    "impact": ["outcome", "metric", "beneficiary", "community"],
    "operations": ["hire", "team", "system", "process"],
    "strategy": ["board", "goal", "initiative", "planning"]
  }
}
```

### Maintenance Schedule

**Weekly:**
- Review generated content for accuracy
- Note missed items for query refinement
- Flag scoring discrepancies
- Check for new priorities

**Monthly:**
- Update partner list if new partnerships
- Review priority projects
- Verify email domains current
- Check custom fields unchanged

**Quarterly:**
- Comprehensive configuration review
- Update scoring weights if priorities change
- Refine search patterns
- Archive completed partnerships/projects
- Add new chart types if useful

---

*For operational protocols, see [SKILL.md](./SKILL.md)*
*For worked examples, see [EXAMPLES.md](./EXAMPLES.md)*
