# 360 Executive Project Tracker - Documentation

## Overview

The 360 Executive Project Tracker is a comprehensive project management skill that consolidates task information from multiple sources (Gmail, Calendar, Drive, Asana) into professional Excel trackers and interactive HTML dashboards.

## System Components

### 1. Data Collection Layer
- **Gmail**: Status updates, blockers, task assignments
- **Google Calendar**: Meeting notes, action items
- **Google Drive**: Meeting deliverables from multiple folders
- **Asana**: Direct project and task integration

### 2. Processing Engine
- Smart task extraction and deduplication
- Auto-categorization by workstream
- Status and priority inference
- Blocker detection and tracking
- Owner assignment from @mentions

### 3. Excel Tracker (Source of Truth)
- Professional 16-column structure
- Conditional formatting and data validation
- Dashboard sheet with real-time metrics
- Manual editing capability with override protection
- Category-based organization

### 4. HTML Dashboard (Executive Presentation)
- Interactive filtering and search
- Visual status indicators
- Shareable read-only view
- Responsive mobile design
- Real-time calculations

## Quick Start

### 1. First-Time Setup

```python
from tracker_orchestrator import TrackerOrchestrator

# Create tracker with sample data
orchestrator = TrackerOrchestrator(mode='on_demand')
xlsx_path = orchestrator.run(days_back=7, create_new=True, use_sample_data=True)
```

### 2. Enhance Schema

```python
from xlsx_enhancer import enhance_xlsx_schema

# Add Category and Source Details columns
enhanced_path = enhance_xlsx_schema(xlsx_path)
```

### 3. Generate Dashboard

```python
from xlsx_to_html_export import export_xlsx_to_html

# Export to HTML
dashboard = export_xlsx_to_html(
    xlsx_path=enhanced_path,
    html_template_path='dashboard_template.html',
    output_path='dashboard.html'
)
```

## Data Schema (16 Columns)

1. **Task ID** - Auto-generated unique identifier
2. **Task Owner** - From @mentions or assignments
3. **Task Description** - Task summary
4. **Status** - Not Started | In Progress | Blocked | Done
5. **Priority** - Critical | High | Medium | Low
6. **Progress %** - 0-100 completion percentage
7. **Blocker Details** - What's blocking the task
8. **Days Blocked** - Auto-calculated from status change
9. **Last Update Date** - Last modification timestamp
10. **Source Context** - Where task was found
11. **Next Steps** - Planned actions
12. **First Detected** - When first captured
13. **Last Auto-Update** - System timestamp
14. **Manual Override** - Protection flag (Yes/No)
15. **Category** - Workstream classification
16. **Source Details** - Extended context from original source

## Category Organization

Tasks are automatically organized into six workstream categories:

1. **Partnership & Legal** - Contracts, agreements, joint ventures
2. **Technical & Product** - API integration, development, testing
3. **Pilot & Implementation** - Deployments, rollouts, clinic pilots
4. **Business Development** - Proposals, pricing, client engagement
5. **Operations** - Internal processes, workflow optimization
6. **Strategy & Planning** - Roadmaps, assessments, vision work

## Configuration

Edit `config/config.json` to customize:

- **Team members**: Add your team member names
- **Project keywords**: Define project names to track
- **Data sources**: Enable/disable Gmail, Calendar, Drive, Asana
- **Drive folders**: Add folder IDs for your meeting deliverables
- **Asana projects**: Add your Asana project IDs
- **Categories**: Customize workstream keywords
- **Visual settings**: Adjust colors and formatting

## Common Workflows

### Daily Update
```python
# Collect latest data
orchestrator = TrackerOrchestrator(mode='on_demand')
xlsx_path = orchestrator.run(days_back=3)

# Export to dashboard
dashboard = export_xlsx_to_html(xlsx_path, 'template.html', 'daily_dashboard.html')
```

### Weekly Review
```python
# Collect full week
xlsx_path = orchestrator.run(days_back=7)

# Manual review in Excel (edit categories, override status)

# Export polished dashboard
dashboard = export_xlsx_to_html(xlsx_path, 'template.html', 'weekly_dashboard.html')
```

### Board Meeting Prep
```python
# Collect comprehensive data
xlsx_path = orchestrator.run(days_back=14)

# Review and categorize in Excel

# Generate executive dashboard
dashboard = export_xlsx_to_html(xlsx_path, 'template.html', 'board_dashboard.html')

# Share HTML with board members
```

## Troubleshooting

### Missing Category or Source Details Columns
```python
from xlsx_enhancer import verify_schema, enhance_xlsx_schema

# Check schema
verify_schema('360_project_tracker.xlsx')

# Fix if needed
enhance_xlsx_schema('360_project_tracker.xlsx')
```

### HTML Dashboard Not Updating
```python
# Re-export with latest data
export_xlsx_to_html(xlsx_path, 'template.html', 'dashboard.html')
```

### Categories Not Auto-Assigning
- Check category keywords in `config.json`
- Customize keywords in `xlsx_enhancer.py`
- Manually assign categories in Excel

### Asana Tasks Not Appearing
- Verify Asana project ID in `config.json`
- Check Asana integration is enabled
- Confirm date range includes recent activity

## Best Practices

### For Daily Use
1. Run data collection each morning
2. Review XLSX for accuracy
3. Make manual adjustments as needed
4. Export to HTML for team viewing

### For Weekly Reviews
1. Collect data for full week (7 days)
2. Deep review in XLSX
3. Add categories and context
4. Generate polished HTML dashboard
5. Share with stakeholders

### For Executive Reporting
1. Filter HTML dashboard by priority
2. Focus on Critical/High items
3. Highlight blockers >7 days
4. Use executive summary metrics

## Files and Structure

```
.claude/skills/360-executive-project-tracker/
├── skill.md                    # Main skill definition
├── scripts/
│   ├── tracker_orchestrator.py  # Main controller
│   ├── data_collector.py        # Data extraction
│   ├── tool_integrator.py       # API integrations
│   ├── project_tracker_builder.py  # Excel generation
│   ├── xlsx_enhancer.py         # Schema enhancement
│   └── xlsx_to_html_export.py   # HTML export
├── config/
│   └── config.json              # System configuration
├── templates/
│   └── (HTML dashboard templates)
└── docs/
    └── README.md                # This file
```

## Support

For questions or issues:
1. Check this README first
2. Review skill.md for usage patterns
3. Examine config.json for settings
4. Check collection logs for debugging

## Version

**Current Version:** 1.2.0
**Last Updated:** November 2025

## Features

✅ Multi-source data collection (Gmail, Calendar, Drive, Asana)
✅ Professional Excel tracking (16-column structure)
✅ Interactive HTML dashboards
✅ Category-based workstream organization
✅ Auto-categorization by keywords
✅ Manual override protection
✅ Blocker detection and alerts
✅ Export automation (XLSX → HTML)

---

**Maintained by:** 360 Social Impact Studios
**Powered by:** Claude (Anthropic)
