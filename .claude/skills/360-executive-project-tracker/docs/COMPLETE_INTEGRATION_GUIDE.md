# 360 Project Tracker: Complete Integration Guide

## Quick Start: 3-Step Workflow

### Step 1: Collect Data → Generate XLSX
```python
from tracker_orchestrator import TrackerOrchestrator

orchestrator = TrackerOrchestrator(mode='on_demand')
xlsx_path = orchestrator.run(days_back=7, use_sample_data=False)
```
**Result:** `/mnt/user-data/outputs/360_project_tracker.xlsx`

### Step 2: Enhance XLSX Schema (One-time)
```python
from xlsx_enhancer import enhance_xlsx_schema

enhance_xlsx_schema(
    xlsx_path='/mnt/user-data/outputs/360_project_tracker.xlsx',
    output_path='/mnt/user-data/outputs/360_project_tracker_enhanced.xlsx'
)
```
**Result:** XLSX with Category and Source Details columns added

### Step 3: Export to HTML Dashboard
```python
from xlsx_to_html_export import export_xlsx_to_html

export_xlsx_to_html(
    xlsx_path='/mnt/user-data/outputs/360_project_tracker_enhanced.xlsx',
    html_template_path='/path/to/dashboard_template.html',
    output_path='/mnt/user-data/outputs/dashboard.html'
)
```
**Result:** Live HTML dashboard with current data

## What Each Component Does

### 📊 XLSX File (Source of Truth)
**File:** `360_project_tracker.xlsx`

**Purpose:**
- Stores all task data
- Supports manual edits and overrides
- Provides Excel formulas for calculations
- Includes Dashboard sheet with metrics

**Key Sheets:**
- **Dashboard** - Summary metrics and KPIs
- **Project Status** - Task details (14 → 16 columns)
- **Instructions** - User guide

**Who Uses It:**
- Team members for manual updates
- Project managers for review and editing
- Automated scripts for data storage

### 🌐 HTML Dashboard (Visualization Layer)
**File:** `360_project_tracker_final.html`

**Purpose:**
- Professional executive presentation
- Interactive filtering and sorting
- Real-time client-side calculations
- Shareable read-only view

**Features:**
- Executive summary with key metrics
- Search across all fields
- Filter by status, priority, owner, category
- Visual indicators (progress bars, status badges, blocker alerts)
- Responsive design

**Who Uses It:**
- Executives for high-level overview
- Team for status visibility
- Stakeholders for progress tracking

### 🐍 Python Scripts (Automation Engine)

#### tracker_orchestrator.py
Coordinates the entire collection process

```python
orchestrator = TrackerOrchestrator(mode='on_demand')
orchestrator.run(days_back=7, create_new=False)
```

#### data_collector.py
Parses and deduplicates task information

- Extracts tasks from raw data
- Infers status and priority
- Detects blockers
- Deduplicates across sources

#### tool_integrator.py
Integrates with external tools

- Gmail search
- Google Calendar
- Google Drive (2 folders)
- Asana Command Center

#### project_tracker_builder.py
Builds and formats Excel file

- Creates worksheet structure
- Applies conditional formatting
- Adds data validation
- Inserts formulas

#### xlsx_enhancer.py (NEW)
Adds Category and Source Details columns

```python
enhance_xlsx_schema(xlsx_path, output_path)
```

#### xlsx_to_html_export.py (NEW)
Exports XLSX data to HTML format

```python
export_xlsx_to_html(xlsx_path, html_template, output_path)
```

### ⚙️ Configuration
**File:** `config.json`

**Configures:**
- Data sources (Gmail, Calendar, Drive, Asana)
- Team members
- Project keywords
- Classification rules (status, priority)
- Visual settings
- Blocker thresholds

## Complete Workflows

### Workflow A: Daily Update (Automated)

```python
from tracker_orchestrator import TrackerOrchestrator
from xlsx_to_html_export import export_xlsx_to_html

# 1. Collect latest data
orchestrator = TrackerOrchestrator(mode='on_demand')
xlsx_path = orchestrator.run(days_back=3)

# 2. Export to dashboard
html_path = export_xlsx_to_html(
    xlsx_path=xlsx_path,
    html_template_path='dashboard_template.html',
    output_path='/mnt/user-data/outputs/daily_dashboard.html'
)

print(f"Dashboard updated: {html_path}")
```

### Workflow B: Weekly Review (Manual + Auto)

```python
# 1. Auto-collect from sources
orchestrator = TrackerOrchestrator(mode='on_demand')
xlsx_path = orchestrator.run(days_back=7)

# 2. Manual review and edits in Excel
# (Open XLSX, review tasks, add categories, override status, etc.)

# 3. Generate executive dashboard
html_path = export_xlsx_to_html(
    xlsx_path=xlsx_path,
    html_template_path='dashboard_template.html',
    output_path='/mnt/user-data/outputs/weekly_dashboard.html'
)

# 4. Share HTML with stakeholders
```

### Workflow C: First-Time Setup

```python
# 1. Create initial tracker with sample data
orchestrator = TrackerOrchestrator(mode='on_demand')
xlsx_path = orchestrator.run(days_back=7, create_new=True, use_sample_data=True)

# 2. Enhance schema with new columns
from xlsx_enhancer import enhance_xlsx_schema
enhanced_path = enhance_xlsx_schema(xlsx_path)

# 3. Verify schema
from xlsx_enhancer import verify_schema
verify_schema(enhanced_path)

# 4. Generate first dashboard
html_path = export_xlsx_to_html(
    xlsx_path=enhanced_path,
    html_template_path='dashboard_template.html',
    output_path='/mnt/user-data/outputs/dashboard.html'
)
```

### Workflow D: On-Demand Status Check

```python
from xlsx_to_html_export import generate_task_summary

# Quick text summary without full dashboard
summary = generate_task_summary('/mnt/user-data/outputs/360_project_tracker.xlsx')
print(summary)
```

**Output:**
```
================================================================================
360 PROJECT TRACKER - TASK SUMMARY
================================================================================
Generated: 2025-11-15 14:30:00
Total Tasks: 15

BLOCKED (3 tasks)
--------------------------------------------------------------------------------
  [T002] GenIP integration testing
       Owner: Team Member | Priority: High | Progress: 40%
       🚫 BLOCKER: Waiting on API credentials from GenIP
          Blocked for 7 days
       → Next: Escalate with GenIP technical contact
...
```

## Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│  EXTERNAL SOURCES                                            │
│  • Gmail (status emails, blockers)                           │
│  • Calendar (meeting action items)                           │
│  • Drive Folder 1: "A - Processed Meeting Deliverables"     │
│  • Drive Folder 2: "Fathom meeting deliverables"            │
│  • Asana: "🎯 Chandler's Command Center"                    │
└────────────┬────────────────────────────────────────────────┘
             │
             │ tool_integrator.py
             │ (search, fetch, parse)
             │
             ▼
┌─────────────────────────────────────────────────────────────┐
│  RAW DATA EXTRACTION                                         │
│  • Email threads                                             │
│  • Calendar events                                           │
│  • Document sections                                         │
│  • Asana tasks                                               │
└────────────┬────────────────────────────────────────────────┘
             │
             │ data_collector.py
             │ (parse, deduplicate, classify)
             │
             ▼
┌─────────────────────────────────────────────────────────────┐
│  PROCESSED TASKS                                             │
│  • Extracted descriptions                                    │
│  • Inferred status & priority                                │
│  • Detected blockers                                         │
│  • Assigned owners                                           │
└────────────┬────────────────────────────────────────────────┘
             │
             │ project_tracker_builder.py
             │ (build Excel, apply formatting)
             │
             ▼
┌─────────────────────────────────────────────────────────────┐
│  XLSX FILE                                                   │
│  360_project_tracker.xlsx                                    │
│  • Project Status sheet (task data)                          │
│  • Dashboard sheet (metrics)                                 │
│  • Instructions sheet                                        │
└────────────┬────────────────────────────────────────────────┘
             │
             │ Manual edits, category assignment,
             │ manual overrides (Excel UI)
             │
             ▼
┌─────────────────────────────────────────────────────────────┐
│  ENHANCED XLSX                                               │
│  • All 16 columns including Category & Source Details       │
│  • Manual overrides preserved                                │
│  • Validated data                                            │
└────────────┬────────────────────────────────────────────────┘
             │
             │ xlsx_to_html_export.py
             │ (extract tasks, format JSON, inject into HTML)
             │
             ▼
┌─────────────────────────────────────────────────────────────┐
│  HTML DASHBOARD                                              │
│  360_project_tracker_dashboard.html                          │
│  • Executive summary                                         │
│  • Interactive filters                                       │
│  • Visual indicators                                         │
│  • Read-only shareable view                                  │
└─────────────────────────────────────────────────────────────┘
```

## Field Mapping Reference

### XLSX Columns → HTML Fields

| # | XLSX Column | HTML Field | Type | Notes |
|---|-------------|------------|------|-------|
| A | Task ID | id | String | T001, T002, etc. |
| B | Task Owner | owner | String | Team member name |
| C | Task Description | description | String | Task summary |
| D | Status | status | Enum | Blocked/In Progress/Done/Not Started |
| E | Priority | priority | Enum | Critical/High/Medium/Low |
| F | Progress % | progress | Integer | 0-100 |
| G | Blocker Details | blocker | String | Empty if not blocked |
| H | Days Blocked | daysBlocked | Integer | Auto-calculated |
| I | Last Update Date | lastUpdate | Date | YYYY-MM-DD |
| J | Source Context | source | String | Short label |
| K | Next Steps | nextSteps | String | Action items |
| L | First Detected | firstDetected | Date | YYYY-MM-DD |
| M | Last Auto-Update | - | DateTime | Internal tracking |
| N | Manual Override | - | Enum | Yes/No (internal) |
| **O** | **Category** | category | Enum | Workstream |
| **P** | **Source Details** | sourceDetails | String | Extended context |

## Configuration Customization

### Add New Team Members

```json
// config.json
"team": {
  "members": [
    "Chandler Lewis",
    "Team Member",
    "New Person",
    "Unassigned"
  ]
}
```

### Add New Project Keywords

```json
// config.json
"projects": {
  "keywords": [
    "SpacePlan",
    "GenIP",
    "CNEN",
    "NewProject"
  ]
}
```

### Customize Categories

```python
# In xlsx_enhancer.py
category_keywords = {
    'Custom Category': ['keyword1', 'keyword2'],
    'Another Category': ['keyword3', 'keyword4']
}
```

### Adjust Blocker Thresholds

```json
// config.json
"tracker_settings": {
  "blocker_alerts": {
    "warning_days": 3,
    "critical_days": 7
  }
}
```

## Maintenance & Updates

### Update Python Dependencies

```bash
pip install openpyxl --upgrade
```

### Backup Before Changes

```python
import shutil
from datetime import datetime

timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
backup_path = f'360_project_tracker_backup_{timestamp}.xlsx'
shutil.copy('360_project_tracker.xlsx', backup_path)
```

### Reset to Clean State

```python
orchestrator = TrackerOrchestrator(mode='on_demand')
orchestrator.run(days_back=7, create_new=True, use_sample_data=True)
```

## Troubleshooting

### Issue: XLSX missing Category/Source Details columns

**Solution:**
```python
from xlsx_enhancer import enhance_xlsx_schema
enhance_xlsx_schema('/path/to/file.xlsx')
```

### Issue: HTML dashboard shows old data

**Solution:**
```python
from xlsx_to_html_export import export_xlsx_to_html
export_xlsx_to_html(xlsx_path, html_template, output_path)
```

### Issue: Tasks not being collected from Asana

**Check:**
- Asana project ID is correct: `1211488271541302`
- Asana integration is enabled in config.json
- Tool has access to Asana

### Issue: Export script fails

**Check:**
- XLSX file exists and is not open in Excel
- HTML template path is correct
- Output directory exists and is writable

### Issue: Categories not auto-assigning

**Solution:** Manually update category keywords in `xlsx_enhancer.py` or assign manually in Excel

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

### Data Quality

- Review auto-categorized tasks
- Add source details where helpful
- Mark manual overrides when needed
- Keep Next Steps current

## Performance Tips

### For Large Datasets (100+ tasks)

- Limit date range in collection
- Archive completed tasks
- Use pagination in dashboard

### For Faster Exports

- Keep HTML template optimized
- Minimize unnecessary columns
- Use efficient data structures

## Version Compatibility Matrix

| Component | Current Version | Required Updates |
|-----------|----------------|------------------|
| tracker_orchestrator.py | v1.0.1 | None |
| data_collector.py | v1.0.1 | Add sourceDetails extraction |
| project_tracker_builder.py | v1.0.1 | Add columns O & P |
| XLSX Schema | v1.1 → v1.2 | Add Category & Source Details |
| HTML Dashboard | v1.1 | None |
| config.json | v1.0.1 | Add category keywords |
| xlsx_enhancer.py | v1.0 | NEW |
| xlsx_to_html_export.py | v1.0 | NEW |

## Next Steps

### Immediate Actions

✅ Run `xlsx_enhancer.py` on existing XLSX
✅ Verify schema with `verify_schema()`
✅ Test export with `xlsx_to_html_export.py`
✅ Review generated HTML dashboard

### Short-term Enhancements

- Update `project_tracker_builder.py` to include new columns by default
- Enhance `data_collector.py` to populate `sourceDetails`
- Add category auto-classification to main orchestrator
- Create scheduled automation script

### Long-term Vision

- Real-time sync between XLSX and HTML
- Web-based editing interface
- Mobile-friendly dashboard
- Historical trend analysis
- Predictive blocker detection

## Support & Documentation

- **Technical Docs**: README.md
- **Skill Definition**: SKILL.md
- **Integration Map**: INTEGRATION_MAPPING.md
- **This Guide**: COMPLETE_INTEGRATION_GUIDE.md
- **Quick Start**: QUICK_START.md

---

## Summary

This integrated toolkit provides:

✅ Automated data collection from 4 sources
✅ Professional Excel tracking with formulas and validation
✅ Interactive HTML dashboards for stakeholder visibility
✅ Flexible workflows for daily, weekly, or ad-hoc reporting
✅ Manual override capability for human judgment
✅ Scalable architecture for future enhancements

**The XLSX is your source of truth, the Python scripts keep it current, and the HTML dashboard makes it beautiful and shareable.**
