# 360 Executive Project Tracker

**Version:** 1.2.0
**Type:** Project Management & Executive Intelligence
**Owner:** 360 Social Impact Studios

## Description

Build professionally designed, multi-source project status trackers that consolidate information from Gmail, Google Calendar, Google Drive, and Asana into Excel dashboards and interactive HTML visualizations. This skill creates executive-ready status tracking systems with automated updates, intelligent blocker detection, and category-based organization.

## When to Use This Skill

Use this skill when you need to:
- Create comprehensive project status trackers or dashboards
- Consolidate status from multiple sources (email, calendar, documents, Asana)
- Generate automated project tracking systems
- Build executive dashboards for project visibility
- Track blockers and escalation systems
- Monitor team workload and capacity
- Create weekly status reporting automation
- Track multi-project portfolios
- Generate interactive HTML dashboards for stakeholder sharing

## Trigger Phrases

Activate this skill with phrases like:
- "Create a project tracker"
- "Build a status dashboard"
- "Track project status from my email/calendar/Drive/Asana"
- "Generate weekly project updates"
- "Set up automated project tracking"
- "Show me all blocked tasks"
- "Consolidate project status"
- "Create an executive dashboard"
- "Export tracker to HTML"
- "Pull project status from my sources"

## Core Capabilities

### 1. Multi-Source Data Collection
- **Gmail**: Status updates, blocker mentions, task assignments
- **Google Calendar**: Meeting notes, action items, follow-ups
- **Google Drive**: Meeting deliverables from multiple folders
- **Asana**: Direct project and task integration

### 2. Excel Tracker (Source of Truth)
- Professional 16-column structure with formulas and validation
- Conditional formatting for visual status recognition
- Dashboard sheet with real-time metrics and KPIs
- Manual editing capability with override protection
- Category-based workstream organization
- Blocker alerts (warning at 3 days, critical at 7+ days)

### 3. HTML Dashboard (Executive Presentation)
- Interactive filtering by status, priority, owner, category
- Real-time search across all fields
- Visual indicators (progress bars, status badges, blocker severity)
- Responsive mobile-friendly design
- Shareable read-only view for stakeholders
- Client-side calculations (no server required)

### 4. Intelligence Layer
- Smart task deduplication across sources
- Auto-categorization by workstream
- Status and priority inference from text
- Blocker detection and tracking
- Owner assignment from @mentions and context
- Conflict resolution when sources disagree

## Quick Start Workflow

### First-Time Setup

**Step 1: Discovery**
When a user requests a tracker, ask:
1. "What team members should I track?"
2. "What are your key projects or initiatives?"
3. "Where does your team communicate status?" (Gmail/Calendar/Drive/Asana)
4. "How far back should I look?" (typically 7-14 days)
5. "Do you want on-demand only or recurring updates?"
6. "Do you need an HTML dashboard for stakeholder sharing?"
7. "What workstreams or categories do you use?"

**Step 2: Generate Configuration**
Create a customized `config.json` with:
- Team member names
- Project keywords
- Data source settings
- Drive folder IDs
- Asana project IDs
- Category keywords
- Visual preferences

**Step 3: Create Initial Tracker**
```python
from tracker_orchestrator import TrackerOrchestrator

orchestrator = TrackerOrchestrator(mode='on_demand')
xlsx_path = orchestrator.run(days_back=7, create_new=True, use_sample_data=True)
```

**Step 4: Enhance Schema**
```python
from xlsx_enhancer import enhance_xlsx_schema

enhanced_path = enhance_xlsx_schema(xlsx_path)
```

**Step 5: Generate HTML Dashboard**
```python
from xlsx_to_html_export import export_xlsx_to_html

dashboard_path = export_xlsx_to_html(
    xlsx_path=enhanced_path,
    html_template_path='dashboard_template.html',
    output_path='live_dashboard.html'
)
```

### Daily/Weekly Updates

**On-Demand Collection:**
```python
orchestrator = TrackerOrchestrator(mode='on_demand')
xlsx_path = orchestrator.run(days_back=7, use_sample_data=False)
```

**Export to Dashboard:**
```python
from xlsx_to_html_export import export_xlsx_to_html

dashboard = export_xlsx_to_html(xlsx_path, 'template.html', 'dashboard.html')
```

## System Architecture

```
Data Sources → Collection Engine → Processing → Excel Tracker → HTML Dashboard
     ↓              ↓                  ↓              ↓              ↓
  Gmail          Extract          Deduplicate    Dashboard    Interactive
  Calendar       Detect           Resolve        Metrics      Filters
  Drive (2x)     Assign           Conflicts      Alerts       Search
  Asana          Categorize       Track          Formulas     Visuals
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
15. **Category** - Workstream classification (6 preset categories)
16. **Source Details** - Extended context from original source

## Category Organization

Tasks are automatically organized into workstream categories:

1. **Partnership & Legal** - Contracts, agreements, joint ventures
2. **Technical & Product** - API integration, development, testing
3. **Pilot & Implementation** - Deployments, rollouts, clinic pilots
4. **Business Development** - Proposals, pricing, client engagement
5. **Operations** - Internal processes, workflow optimization
6. **Strategy & Planning** - Roadmaps, assessments, vision work

## Configuration Example

```json
{
  "data_collection": {
    "days_back": 7,
    "sources": {
      "gmail": { "enabled": true },
      "calendar": { "enabled": true },
      "drive": {
        "enabled": true,
        "folders": [
          { "name": "A - Processed Meeting Deliverables" },
          {
            "name": "Fathom meeting deliverables",
            "folder_id": "1P8gGXnNvCjvejFosFqTE7qjDVS3uOrmL"
          }
        ]
      },
      "asana": {
        "enabled": true,
        "projects": [
          {
            "name": "🎯 Chandler's Command Center",
            "project_id": "1211488271541302"
          }
        ]
      }
    }
  },
  "team": {
    "members": ["Chandler Lewis", "Team Member", "Unassigned"]
  },
  "projects": {
    "keywords": ["SpacePlan", "GenIP", "CNEN", "NanoBioPlus"]
  }
}
```

## Key Features

### Automated Data Collection
- Pull from 4 sources automatically
- Smart pattern matching for task identification
- Status inference from language patterns
- Priority detection from urgency indicators
- Auto-categorization by workstream

### Smart Processing
- Cross-source deduplication
- Conflict resolution when sources disagree
- Owner assignment from @mentions and context
- Blocker history tracking
- Missing information flagging

### Professional Presentation
- Excel-based source of truth with formulas
- Interactive HTML dashboard with filters
- Visual status indicators and progress bars
- Blocker severity badges
- Category-based strategic views

### Manual Control
- Excel-based editing capability
- Manual override protection
- Category assignment
- Progress tracking
- Status and priority adjustments

## Common Use Cases

### Board Meeting Preparation
1. Run full collection (7-14 days)
2. Review and categorize in Excel
3. Export to polished HTML dashboard
4. Share dashboard with board members

### Weekly Team Status
1. Daily automated collection
2. Team reviews Excel for accuracy
3. Export to HTML for stakeholder viewing
4. Use filters to focus on specific priorities

### Blocker Escalation
1. Filter dashboard for critical blockers (7+ days)
2. Review blocker details and source context
3. Identify escalation paths
4. Track resolution progress

### Portfolio Management
1. Collect across all projects
2. Use category filters for strategic view
3. Monitor completion rates by workstream
3. Identify resource allocation gaps

## Best Practices

### When Building Trackers

**Do:**
- Start with discovery conversation to understand workflow
- Use sample data to demonstrate before running live
- Explain what each column means and why it matters
- Demonstrate HTML dashboard alongside Excel
- Test formulas and formatting before delivery
- Provide clear next steps for updates and customization

**Don't:**
- Build without understanding user's workflow
- Use generic configurations (personalize names, projects, categories)
- Overwhelm with all advanced features upfront
- Deliver without testing in both Excel and browser
- Skip documentation (users need to maintain it)
- Force categories that don't match user's mental model

### Communication Style

**For Executives:**
- Focus on value (time saved, visibility gained)
- Lead with HTML dashboard (more impressive visually)
- Show visual dashboards first, mechanics second
- Use business language (risks, priorities, completion)
- Demonstrate with real examples
- Show category-based strategic views

**For Technical Users:**
- Share architecture and data flow
- Explain extraction patterns and logic
- Walk through export automation scripts
- Provide config.json for customization
- Show debugging approaches
- Explain category auto-assignment logic

## Troubleshooting

### Missing Category or Source Details Columns
**Solution:**
```python
from xlsx_enhancer import enhance_xlsx_schema, verify_schema

# Verify current schema
verify_schema('360_project_tracker.xlsx')

# Enhance if needed
enhanced = enhance_xlsx_schema('360_project_tracker.xlsx')
```

### HTML Dashboard Not Updating
**Solution:**
```python
# Re-export with latest data
from xlsx_to_html_export import export_xlsx_to_html

export_xlsx_to_html(
    xlsx_path='360_project_tracker_enhanced.xlsx',
    html_template_path='template.html',
    output_path='dashboard.html'
)
```

### Categories Not Auto-Assigning
**Solution:**
- Check category keywords match your task descriptions
- Customize keywords in `xlsx_enhancer.py`
- Manually assign categories in Excel
- Re-run enhancement with updated keywords

### Asana Tasks Not Appearing
**Solution:**
- Verify Asana project ID is correct
- Check Asana integration enabled in config.json
- Confirm tool has Asana access
- Check date range includes recent Asana activity

## Success Metrics

Track these metrics to measure tracker value:

**Efficiency Gains:**
- Time saved per week on status compilation (target: 3-5 hours)
- Reduction in "what's the status?" meeting time
- Faster blocker identification (hours vs. days)

**Visibility Improvements:**
- % of projects with current status (target: >90%)
- % of tasks with clear owners (target: >95%)
- Average age of unresolved blockers (target: <5 days)
- % of tasks properly categorized (target: >85%)

**Team Adoption:**
- % of team regularly viewing tracker (target: >80%)
- % of status updates sourced from tracker
- Frequency of manual override usage
- Stakeholder engagement with HTML dashboards

## Deliverables Checklist

Before marking tracker as complete, ensure:

**Files Delivered:**
- [ ] `360_project_tracker_enhanced.xlsx` - Working Excel file with 16 columns
- [ ] `config.json` - User-specific configuration
- [ ] `dashboard.html` - Interactive HTML dashboard
- [ ] `README.md` - Setup and usage guide
- [ ] All 6 Python scripts (orchestrator, collector, integrator, builder, enhancer, exporter)

**Documentation Provided:**
- [ ] Quick start guide (3 steps to first tracker)
- [ ] Column definitions (all 16 fields explained)
- [ ] Export workflow guide (XLSX → HTML process)
- [ ] Configuration guide (how to customize)
- [ ] Category customization guide
- [ ] Troubleshooting section

**User Enablement:**
- [ ] Demonstrated how to open and use tracker
- [ ] Demonstrated HTML dashboard features
- [ ] Explained how to trigger updates
- [ ] Showed how to export to HTML
- [ ] Explained category auto-assignment
- [ ] Clarified manual override protection

## Version History

**v1.2.0** (Current)
- Multi-source data collection (Gmail, Calendar, Drive [2 folders], Asana)
- Professional Excel template with 16-column structure
- Interactive HTML dashboard with export automation
- Category-based workstream organization
- Dual-mode operation (on-demand, recurring)
- Auto-categorization by keywords
- Extended source context details

**v1.1.0**
- Added multiple Drive folder support
- Enhanced data collection patterns
- Improved deduplication logic

**v1.0.0**
- Basic Gmail, Calendar, single Drive folder
- 14-column tracker structure
- Excel-only output

## Integration with Other Skills

This skill works well with:
- **Executive Intelligence Dashboard**: Use tracker as data source for weekly briefs
- **Contract Redlining Tool**: Track contract review tasks and legal milestones
- **Intelligence Extractor**: Extract task information from various document types

## Support Files

This skill includes:
- **scripts/**: All 6 Python automation scripts
- **config/**: Sample configuration file
- **templates/**: HTML dashboard template
- **docs/**: Comprehensive documentation (README, Quick Start, Integration Guide)

---

**Created:** November 2025
**Maintained by:** Chandler Lewis / 360 Social Impact Studios
**Powered by:** Claude (Anthropic)

*This skill enables rapid deployment of professional project tracking systems with dual visualization layers (Excel + HTML) that save hours per week and provide executive-grade visibility into project status, blockers, team capacity, and workstream organization.*
