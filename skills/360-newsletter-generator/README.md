# 360 Newsletter Generator

**Category:** Executive Communication & Strategic Briefing
**Purpose:** Generate publication-style newsletters for 360 Social Impact Studios synthesizing updates from Asana, Google Drive, and Gmail into professionally designed digests.

## Overview

The 360 Newsletter Generator automatically creates sophisticated, publication-style newsletters by aggregating data from multiple sources and presenting strategic updates in a dense but readable format inspired by British newspaper design, with interactive data visualizations showing trends and metrics.

## Key Features

### Multi-Source Data Integration
- **Asana Integration** (70% weight) - Project progress, task velocity, milestone tracking
- **Gmail Integration** (20% weight) - Partnership communications, client interactions, announcements
- **Google Drive Integration** (10% weight) - Reports, deliverables, impact documentation

### Professional Newsletter Design
- Modern executive dashboard aesthetic
- Fixed sidebar navigation
- Color-coded sections (partnerships blue, operations green, strategy orange)
- Interactive Chart.js visualizations
- Print-friendly PDF export

### Content Analysis & Prioritization
- Automatic significance scoring (0-100 scale)
- Lead story selection based on strategic importance
- Section assignment by content type
- Action item flagging and tracking

### Quality Assurance
- Data integrity verification
- Content completeness checks
- Design and formatting validation
- Tone and voice consistency

## When to Use

Trigger this skill when the user requests:
- "Generate newsletter" or "create newsletter"
- "Weekly digest", "monthly update", or "company summary"
- "What happened this week/month"
- "Create board update" or "prep investor update"
- Any comprehensive summary of 360 activities

## Quick Start

### 1. Generate Your First Newsletter

**Simple command:**
```
Generate newsletter for last week
```

**With specifics:**
```
Create newsletter for November 4-10 focused on partnerships
```

**For board meeting:**
```
Generate November newsletter for board meeting
```

### 2. What Happens Next

1. Date range confirmation (5 seconds)
2. Data collection from Asana, Gmail, Drive (30-40 seconds)
3. Content analysis and scoring (10 seconds)
4. HTML generation with charts (10 seconds)
5. Interactive artifact delivered (~60 seconds total)

### 3. Customize & Iterate

After seeing the first newsletter:
- "Expand the partnerships section"
- "Add a chart showing team capacity"
- "Change the lead story to [different item]"
- "Focus more on operations, less on strategy"

## Context: 360 Social Impact Studios

**Organization Overview:**
- 501(c)(3) nonprofit innovation consultancy
- Global operations: Seattle (HQ), São Paulo Brazil, international partnerships
- Focus areas: Innovation consulting, technology transfer, social impact ventures
- Cross-border market expansion (US-Brazil corridor emphasis)

**Key Partnerships Monitored:**
- SpacePlan (360 Space Innovation Studios joint venture)
- GenIP (Invention Evaluator integration)
- ScienceLink (technology transfer)
- NanoBioPlus (biomaterials platforms)
- CNEN (National Nuclear Energy Commission, Brazil)
- Carnegie Mellon, Life Science Washington, various universities

**Strategic Focus Areas:**
- Partnership development and ecosystem building
- Innovation portfolio assessment and validation
- International business development (especially Brazil)
- Social impact measurement and systems change
- Technology commercialization and transfer

## Newsletter Structure

### Sections

1. **Executive Summary**
   - Gradient blue banner
   - 3-4 key highlight cards
   - Most critical information at a glance

2. **Partnerships & Ecosystem**
   - Partnership pipeline status
   - New agreements or renewals
   - Relationship health indicators
   - Cross-border developments

3. **Programs & Innovation**
   - Active project updates
   - Technology assessments completed
   - Client deliverables
   - Methodology applications

4. **Impact & Outcomes**
   - Social impact metrics
   - Community outcomes
   - Systems change indicators
   - Testimonials and feedback

5. **Operations & Capacity**
   - Team updates and hiring
   - Infrastructure improvements
   - Financial sustainability
   - System implementations

6. **Strategic Horizon**
   - Upcoming meetings and events
   - Decision deadlines
   - Strategic initiatives launching
   - Board priorities

### Visual Components

**Charts (minimum 4 per newsletter):**
- Partnership pipeline by stage (bar chart)
- Project distribution by region (pie chart)
- Impact metrics trend (line chart)
- Revenue/sustainability trajectory (line chart)

**Metric Cards:**
- Partnership value/count
- Active projects
- Social impact numbers
- Team capacity
- Financial runway

**Status Badges:**
- CRITICAL: Urgent action needed (red border)
- ACTION REQUIRED: Response needed (yellow border)
- MONITORING: Watching closely (gray border)

## Data Collection Protocol

### Phase 1: Connect to Data Sources

**Asana Workspace:**
1. Use `asana_list_workspaces` to get workspace gid
2. Expected workspace: 360socialventures.com (gid: 1210382795871981)
3. Confirm connection successful

**Gmail Profile:**
1. Use `read_gmail_profile` to get user email
2. Confirm access to Gmail search

**Google Drive:**
1. Verify `google_drive_search` access
2. Test with simple query

### Phase 2: Define Date Range

**Determine newsletter period:**
- Default: Previous 7 days (Monday to Sunday)
- Monthly: Previous calendar month
- Custom: User-specified date range

**Calculate dates:**
- Start date: [YYYY-MM-DD]
- End date: [YYYY-MM-DD]
- RFC3339 format for tools: YYYY-MM-DDTHH:MM:SSZ

### Phase 3: Collect Asana Data

**Priority Projects to Scan:**
- Weekly Meeting Tracker
- Partnership Development
- Client Engagements
- SpacePlan Joint Venture
- GenIP Integration
- CNEN Partnership
- Any project with "Board" in name

**For Each Project:**
1. Get project details with custom fields
2. Get project sections
3. Search completed tasks (with date filter)
4. Search modified/active tasks
5. Get project task counts

### Phase 4: Collect Gmail Data

**Search Patterns:**
1. Partnership communications from key domains
2. Sent strategic emails (agreements, proposals, contracts)
3. Impact/client feedback (testimonials, outcomes)
4. Board-related correspondence

### Phase 5: Collect Google Drive Data

**Search Patterns:**
1. Strategic documents modified in period
2. Partner-specific documents
3. Impact metrics documentation
4. Financial and budget documents

## Content Analysis & Prioritization

### Significance Scoring (0-100 Scale)

**95-100: Critical**
- Partnership announcements/signatures
- Major funding milestones
- Board-level decisions

**85-94: High**
- Project completions with impact
- Partnership stage advancement
- Strategic milestone achievements

**70-84: Medium**
- Partnership pipeline progress
- Program updates and deliverables
- Team capacity enhancements

**40-69: Low**
- Operations updates
- Process improvements
- Routine completions

### Lead Story Selection

Select based on:
1. Highest significance score (95-100 preferred)
2. Strategic importance to mission
3. Stakeholder relevance
4. Impact magnitude
5. Timeliness

## Writing Guidelines

### Tone: Grounded + Visionary

Balance realism with possibility. Write clearly and professionally while leaving room for aspiration.

**Examples:**
- "The partnership positions 360 to influence technology transfer across Latin America."
- "Three enterprise opportunities advanced to negotiation, validating our cross-border approach."

### Critical Rules

**NEVER use em dashes (—)**
- Use commas instead
- Use periods for separate thoughts
- Use parentheses for clarification

**Apply purpose-driven lens appropriately:**
- Partnership strategy → Consider mutual benefit, ecosystem impact
- Program design → Consider access, inclusion, systems change
- Organizational decisions → Consider community outcomes
- Impact metrics → Show human outcomes, not just numbers

**Maintain international awareness:**
- Don't assume US-centric norms
- Acknowledge time zones (PT, BRT)
- Note cultural considerations
- Portuguese language context when relevant

## Chart Specifications

### Chart Types

**Doughnut/Pie Charts:**
- Partnership portfolio distribution
- Project distribution by region
- Revenue sources breakdown

**Bar Charts:**
- Partnership pipeline by stage
- Service package market fit
- Project completion velocity

**Radar Charts:**
- Team capability assessment
- Service offering maturity
- Market positioning analysis

**Line Charts:**
- Revenue trajectory
- Partnership pipeline growth
- Task completion trends

### Chart Styling (All Charts)

- Monochromatic palette (grays, blacks, charcoals)
- No gradients or shadows
- Minimal grid lines
- Clean sans-serif fonts
- Professional spacing

## Customization Options

### Scope Adjustments

**Partnership-focused:**
```
Generate newsletter for last month focused on partnerships only
```

**Operations-only:**
```
Create operations brief for Q4
```

**Board-ready:**
```
Generate November brief for board meeting, include financial metrics
```

### Date Range Variations

- Weekly: `Generate newsletter for last week`
- Monthly: `Create newsletter for October`
- Custom: `Generate brief for November 1-15`
- Quarter: `Create Q4 newsletter`

### Audience Adjustments

- Internal team: More operational detail
- Investors: Emphasis on traction and metrics
- Partners: Focus on collaborative opportunities

## Quality Assurance Checklist

### Data Integrity
- [ ] Connected to all three data sources
- [ ] Correct date range applied
- [ ] Metrics from actual data, not estimates
- [ ] Charts display real numbers
- [ ] Geographic spread accurate

### Content Quality
- [ ] Lead story is most significant
- [ ] Minimum 2 substantive stories per section
- [ ] Context beyond task names
- [ ] Action items specific and attributed
- [ ] Strategic implications explained

### Design & Formatting
- [ ] No em dashes anywhere
- [ ] Inline stats properly formatted
- [ ] Status badges applied appropriately
- [ ] Charts render correctly
- [ ] Typography hierarchy consistent

## Directory Structure

```
360-newsletter-generator/
├── README.md                           # This file
├── INDEX.md                            # Complete file index
├── references/
│   ├── data-collection-guide.md        # Detailed data collection protocols
│   ├── content-analysis-framework.md   # Scoring and prioritization rules
│   ├── writing-style-guide.md          # Tone, voice, and formatting rules
│   ├── chart-specifications.md         # Visual design specifications
│   ├── troubleshooting-guide.md        # Common issues and solutions
│   └── workflow-examples.md            # Step-by-step workflow examples
├── templates/
│   ├── newsletter-template.html        # Complete HTML template
│   └── data-sources.json               # Configuration for data sources
└── examples/
    ├── weekly-newsletter-example.html  # Sample weekly output
    └── monthly-board-brief-example.html # Sample monthly output
```

## Usage Examples

### Example 1: Weekly Team Newsletter

```
User: Generate newsletter for last week
Assistant: Generating 360 Newsletter for November 4-10, 2025...
[Collects data, analyzes, generates HTML artifact]
Result: Interactive newsletter with 4 charts, executive summary,
        all sections populated, action items flagged
```

### Example 2: Monthly Board Brief

```
User: Create October newsletter for board meeting
Assistant: Creating comprehensive October board brief...
[Expanded data collection, deeper analysis, strategic framing]
Result: Board-ready newsletter with 6-8 charts, financial metrics,
        strategic horizon section emphasized
```

### Example 3: Partnership-Focused Update

```
User: Newsletter for SpacePlan partnership only, last 30 days
Assistant: Generating SpacePlan-focused newsletter...
[Filters all searches for SpacePlan mentions]
Result: Deep-dive newsletter on single partnership with all
        relevant context and metrics
```

## Best Practices

### Template Selection
1. Match newsletter type to audience needs
2. Weekly for team updates
3. Monthly for board/investors
4. Custom for specific partnerships or focus areas

### Data Quality
1. Verify all data sources accessible
2. Confirm date ranges are correct
3. Review significance scoring for accuracy
4. Check chart data for completeness

### Content Review
1. Lead story truly most significant
2. Each section has substantive content
3. Action items are specific
4. Strategic implications clear

## Advanced Features

### Multi-Period Comparison
Generate newsletters for multiple periods and show trends:
```
Generate newsletters for October and November, then show comparison
```

### Stakeholder-Specific Briefs
Focus on specific partnerships or stakeholders:
```
Generate brief focused on SpacePlan partnership, last 90 days
```

### Pre-Meeting Briefs
Enhanced format with talking points:
```
Generate brief for tomorrow's board meeting, include talking points
```

## Integration Workflow

```
Asana Projects ──┐
                 │
Gmail Threads ───┼──→ Claude Analysis ──→ HTML Newsletter
                 │         ↓
Drive Documents ─┘    Significance      Interactive Artifact
                      Scoring              (with charts)
                         ↓
                    Section
                    Assignment
```

## Troubleshooting

### Brief Seems Incomplete

**Possible causes:**
- Data source temporarily unavailable
- Date range too narrow
- Project names changed
- Partner domains changed

**Solutions:**
- Check which sources returned results
- Expand date range
- Manually specify projects
- Update partner configuration

### Charts Not Displaying

**Possible causes:**
- Insufficient data points
- Custom fields not found
- Metric extraction failed

**Solutions:**
- Verify data exists
- Check custom field names
- Use manual metrics
- Replace with text summary

## Support

- **Newsletter generation issues**: Review workflow examples
- **Data collection problems**: See data collection guide
- **Content quality concerns**: Check content analysis framework
- **Design questions**: See chart specifications

## Version History

- **v1.0** (2025-11-15) - Initial release
  - Multi-source data integration (Asana, Gmail, Drive)
  - Professional dashboard-style newsletter template
  - Automatic significance scoring and lead story selection
  - Interactive Chart.js visualizations
  - Quality assurance framework
  - Comprehensive reference documentation

## Quick Links

- [Complete File Index](INDEX.md)
- [Data Collection Guide](references/data-collection-guide.md)
- [Content Analysis Framework](references/content-analysis-framework.md)
- [Writing Style Guide](references/writing-style-guide.md)
- [Chart Specifications](references/chart-specifications.md)
- [Newsletter Template](templates/newsletter-template.html)
- [Configuration](templates/data-sources.json)

---

**Ready to generate your first newsletter?** Just say:
```
Generate newsletter for last week
```
