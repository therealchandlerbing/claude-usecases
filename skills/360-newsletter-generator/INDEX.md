# 360 Newsletter Generator - File Index

Complete index of all files in the 360 Newsletter Generator skill.

## Core Documentation

| File | Purpose | Start Here? |
|------|---------|-------------|
| [README.md](README.md) | Main documentation and overview | ✅ YES |
| [INDEX.md](INDEX.md) | This file - complete file listing | For reference |

## Reference Documentation

| File | Purpose |
|------|---------|
| [data-collection-guide.md](references/data-collection-guide.md) | Detailed protocols for collecting data from Asana, Gmail, and Drive |
| [content-analysis-framework.md](references/content-analysis-framework.md) | Significance scoring rules and section assignment logic |
| [writing-style-guide.md](references/writing-style-guide.md) | Tone, voice, formatting rules, and critical writing guidelines |
| [chart-specifications.md](references/chart-specifications.md) | Chart types, data requirements, and visual design specifications |
| [troubleshooting-guide.md](references/troubleshooting-guide.md) | Common issues and solutions |
| [workflow-examples.md](references/workflow-examples.md) | Step-by-step workflow walkthroughs |

## Templates

| File | Purpose |
|------|---------|
| [newsletter-template.html](templates/newsletter-template.html) | Complete HTML template with sidebar navigation, sections, and Chart.js integration |
| [data-sources.json](templates/data-sources.json) | Configuration file for priority projects, partners, search queries, and metrics |

## Examples

| File | Demonstrates |
|------|-------------|
| [weekly-newsletter-example.html](examples/weekly-newsletter-example.html) | Sample weekly newsletter output |
| [monthly-board-brief-example.html](examples/monthly-board-brief-example.html) | Sample monthly board brief with expanded metrics |

## Quick Navigation

### For First-Time Users
1. Read [README.md](README.md) - Overview and key features
2. Try generating a newsletter: "Generate newsletter for last week"
3. Review output and iterate
4. Check [Workflow Examples](references/workflow-examples.md) for detailed walkthroughs

### For Regular Users
1. Request newsletter generation with specific date range
2. Review [Data Collection Guide](references/data-collection-guide.md) for query optimization
3. Check [Chart Specifications](references/chart-specifications.md) for visualization options
4. Use [Troubleshooting Guide](references/troubleshooting-guide.md) when issues arise

### For Administrators
1. Update [data-sources.json](templates/data-sources.json) as partnerships change
2. Review [Content Analysis Framework](references/content-analysis-framework.md) for scoring adjustments
3. Maintain priority projects list in configuration
4. Monitor newsletter quality using checklist

### For Developers
1. Review [newsletter-template.html](templates/newsletter-template.html) for structure
2. Check [data-sources.json](templates/data-sources.json) for configuration schema
3. See [Data Collection Guide](references/data-collection-guide.md) for API usage
4. Reference [Chart Specifications](references/chart-specifications.md) for Chart.js implementation

## File Organization

```
360-newsletter-generator/
├── README.md                           # Main documentation
├── INDEX.md                            # This file
│
├── references/                         # Reference documentation
│   ├── data-collection-guide.md        # Data collection protocols
│   ├── content-analysis-framework.md   # Scoring and prioritization
│   ├── writing-style-guide.md          # Tone and formatting
│   ├── chart-specifications.md         # Visual specifications
│   ├── troubleshooting-guide.md        # Issue resolution
│   └── workflow-examples.md            # Step-by-step examples
│
├── templates/                          # Templates and configuration
│   ├── newsletter-template.html        # Complete HTML template
│   └── data-sources.json               # Data source configuration
│
└── examples/                           # Sample outputs
    ├── weekly-newsletter-example.html  # Weekly sample
    └── monthly-board-brief-example.html # Monthly sample
```

## Configuration Files

### data-sources.json Structure

```json
{
  "workspace": {
    "asana_workspace_gid": "1210382795871981",
    "asana_workspace_name": "360socialventures.com",
    "gmail_user": "chandler@360social.org",
    "time_zone": "America/Los_Angeles"
  },
  "priority_projects": [...],
  "key_partners": [...],
  "asana_queries": {...},
  "gmail_queries": {...},
  "drive_queries": {...},
  "section_mapping": {...},
  "metric_calculations": {...},
  "chart_data_sources": {...},
  "significance_scoring": {...}
}
```

See [data-sources.json](templates/data-sources.json) for complete configuration.

## Newsletter Sections

Each newsletter includes these sections:

1. **Executive Summary** - 3-4 key highlights in gradient banner
2. **Partnerships & Ecosystem** - Partnership pipeline and developments
3. **Programs & Innovation** - Project updates and deliverables
4. **Impact & Outcomes** - Social impact metrics and testimonials
5. **Operations & Capacity** - Team updates and infrastructure
6. **Strategic Horizon** - Upcoming events and decision deadlines

## Data Sources Priority

| Source | Weight | Content Type |
|--------|--------|--------------|
| Asana | 70% | Project progress, tasks, milestones |
| Gmail | 20% | Communications, announcements, feedback |
| Google Drive | 10% | Reports, deliverables, documentation |

## Significance Scoring Ranges

| Score | Category | Examples |
|-------|----------|----------|
| 95-100 | Critical | Partnership signatures, major funding |
| 85-94 | High | Project completions, strategic milestones |
| 70-84 | Medium | Pipeline progress, program updates |
| 40-69 | Low | Operations updates, routine completions |

## Newsletter Types

### Weekly Newsletter
- Default date range: Previous 7 days
- Focus: Tactical updates and action items
- Charts: 4 minimum
- Audience: Internal team

### Monthly Board Brief
- Date range: Previous calendar month
- Focus: Strategic overview and trends
- Charts: 6-8 recommended
- Audience: Board, investors

### Custom Focus Brief
- Date range: User-specified
- Focus: Specific partnership, program, or area
- Charts: As relevant
- Audience: Stakeholder-specific

## Key Partnerships Monitored

- **SpacePlan** - 360 Space Innovation Studios joint venture
- **GenIP** - Invention Evaluator integration
- **ScienceLink** - Technology transfer partnerships
- **NanoBioPlus** - Biomaterials platforms
- **CNEN** - National Nuclear Energy Commission (Brazil)
- **Carnegie Mellon** - University collaboration
- **Life Science Washington** - Regional ecosystem

## Chart Types Available

| Chart Type | Use Case | Data Source |
|------------|----------|-------------|
| Doughnut/Pie | Portfolio distribution, regional breakdown | Asana tasks |
| Bar | Pipeline stages, market fit scores | Asana custom fields |
| Radar | Team capabilities, service maturity | Mixed sources |
| Line | Revenue trends, completion velocity | Drive + Asana |

## Version Information

- **Current Version:** 1.0.0
- **Last Updated:** 2025-11-15
- **Data Sources:** Asana, Gmail, Google Drive
- **Template Engine:** Custom HTML + Chart.js
- **Output Format:** Interactive HTML artifact

## External Dependencies

- **Asana API** - For project and task data
- **Gmail API** - For email communications
- **Google Drive API** - For document search and retrieval
- **Chart.js** - For interactive visualizations (CDN)
- **Font Awesome** - For icons (CDN)

## Common Workflows

### Generate Weekly Newsletter
```
User: Generate newsletter for last week
→ Confirm date range
→ Collect Asana data (5-6 calls)
→ Collect Gmail data (3-4 calls)
→ Collect Drive data (2-3 calls)
→ Analyze and score content
→ Generate HTML with charts
→ Deliver artifact (~60 seconds)
```

### Generate Monthly Board Brief
```
User: Create October newsletter for board
→ Expand date range (full month)
→ Comprehensive data collection (15-20 calls)
→ Deeper trend analysis
→ More charts (6-8)
→ Strategic framing
→ Financial metrics included
→ Deliver artifact (~90 seconds)
```

### Focus on Specific Partnership
```
User: Newsletter for SpacePlan partnership only, last 30 days
→ Filter all searches for SpacePlan
→ All sections focus on this partnership
→ SpacePlan-specific metrics
→ Deeper detail on single relationship
→ Deliver artifact (~60 seconds)
```

## Customization Points

### Adjustable Configuration
- Priority projects list (add/remove projects)
- Key partners (add/remove organizations)
- Search query patterns (refine for better results)
- Significance scoring weights (adjust priorities)
- Section mappings (customize content organization)

### Template Modifications
- Color schemes (change section colors)
- Chart types (swap visualization styles)
- Section order (reorder newsletter sections)
- Badge styles (modify status indicators)

## Quality Metrics

### Data Integrity
- All three sources successfully queried
- Date ranges correctly applied
- Metrics from actual data
- Geographic distribution accurate

### Content Quality
- Lead story is most significant
- Minimum 2 stories per section
- Context beyond task names
- Action items specific

### Design Quality
- Charts render correctly
- Typography hierarchy consistent
- Print-friendly layout
- Mobile-responsive design

## Support Resources

- **Newsletter generation**: See [README.md](README.md)
- **Data collection**: See [data-collection-guide.md](references/data-collection-guide.md)
- **Content issues**: See [content-analysis-framework.md](references/content-analysis-framework.md)
- **Design questions**: See [chart-specifications.md](references/chart-specifications.md)
- **Troubleshooting**: See [troubleshooting-guide.md](references/troubleshooting-guide.md)

## Update Schedule

### Weekly
- Review generated content for accuracy
- Note any missed items
- Flag scoring discrepancies

### Monthly
- Update partner list if new partnerships added
- Review priority projects
- Verify email domains accurate
- Check custom fields unchanged

### Quarterly
- Comprehensive configuration review
- Update scoring weights if needed
- Refine search patterns
- Add new chart types if useful
- Archive completed partnerships/projects

---

**Quick Links:**
- [Main README](README.md) ← Start here
- [Data Collection Guide](references/data-collection-guide.md)
- [Content Analysis Framework](references/content-analysis-framework.md)
- [Writing Style Guide](references/writing-style-guide.md)
- [Newsletter Template](templates/newsletter-template.html)
- [Configuration File](templates/data-sources.json)
