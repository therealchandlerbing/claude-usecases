# Quick Start Guide - 360 Executive Project Tracker

## 3-Step Quickstart

### Step 1: Create Your First Tracker (2 minutes)

Say to Claude:
```
"Create a project tracker with sample data"
```

Or run manually:
```python
from tracker_orchestrator import TrackerOrchestrator

orchestrator = TrackerOrchestrator(mode='on_demand')
xlsx_path = orchestrator.run(days_back=7, create_new=True, use_sample_data=True)
```

**Result:** `/mnt/user-data/outputs/360_project_tracker.xlsx`

### Step 2: Enhance the Schema (1 minute)

```python
from xlsx_enhancer import enhance_xlsx_schema

enhance_xlsx_schema(
    xlsx_path='/mnt/user-data/outputs/360_project_tracker.xlsx',
    output_path='/mnt/user-data/outputs/360_project_tracker_enhanced.xlsx'
)
```

**Result:** XLSX with Category and Source Details columns added

### Step 3: Generate HTML Dashboard (1 minute)

```python
from xlsx_to_html_export import export_xlsx_to_html

export_xlsx_to_html(
    xlsx_path='/mnt/user-data/outputs/360_project_tracker_enhanced.xlsx',
    html_template_path='/path/to/dashboard_template.html',
    output_path='/mnt/user-data/outputs/dashboard.html'
)
```

**Result:** Interactive HTML dashboard ready to share

## Common Commands

### Pull Project Status from Your Sources

Say to Claude:
```
"Pull project status from my Gmail, calendar, and Drive from the last 7 days"
```

This will:
- Search Gmail for status updates, blockers
- Extract action items from calendar meetings
- Scan Drive folders for meeting deliverables
- Pull tasks from Asana projects
- Generate tracker with all consolidated data

### Update Existing Tracker

Say to Claude:
```
"Update my project tracker with the latest status"
```

### Export to Dashboard

Say to Claude:
```
"Export my tracker to an HTML dashboard"
```

### Generate Quick Summary

Say to Claude:
```
"Show me all blocked tasks"
```

Or:
```
"Summarize my project status"
```

## Customization Checklist

Before first live run:

1. **Edit config.json:**
   - [ ] Add your team member names
   - [ ] Add your project keywords
   - [ ] Add your Drive folder IDs
   - [ ] Add your Asana project IDs

2. **Test data collection:**
   - [ ] Run with `use_sample_data=True` first
   - [ ] Verify data sources are accessible
   - [ ] Check folder IDs are correct

3. **Review output:**
   - [ ] Open XLSX file in Excel
   - [ ] Check sample tasks loaded correctly
   - [ ] Verify formulas and formatting work

## Configuration Examples

### Add Team Members
```json
// In config.json
"team": {
  "members": [
    "Chandler Lewis",
    "Your Name",
    "Team Member 1",
    "Team Member 2"
  ]
}
```

### Add Drive Folders
```json
// In config.json
"drive": {
  "enabled": true,
  "folders": [
    {"name": "Your Folder Name"},
    {
      "name": "Another Folder",
      "folder_id": "1ABC123XYZ456"
    }
  ]
}
```

**Pro tip:** Using folder_id is faster and more reliable than folder name.

**Get folder ID:**
1. Open folder in Google Drive
2. Copy ID from URL: `https://drive.google.com/drive/folders/{FOLDER_ID}`

### Add Asana Projects
```json
// In config.json
"asana": {
  "enabled": true,
  "projects": [
    {
      "name": "Your Project Name",
      "project_id": "1234567890"
    }
  ]
}
```

## Typical Workflows

### Morning Standup
```
"Pull project status from the last 3 days"
→ Review tracker in Excel
→ Update team on blockers
```

### Weekly Review
```
"Update project tracker for the week"
→ Review and categorize in Excel
→ Export to HTML dashboard
→ Share with stakeholders
```

### Board Meeting Prep
```
"Generate project status for the last 2 weeks"
→ Deep review in Excel
→ Assign categories
→ Export polished dashboard
→ Present to board
```

## Trigger Phrases

Use these phrases to activate the skill:

- "Create a project tracker"
- "Pull project status from my sources"
- "Update my project tracker"
- "Generate weekly project updates"
- "Show me all blocked tasks"
- "Export tracker to HTML"
- "Create an executive dashboard"

## What Gets Collected

### From Gmail
- Status update emails
- Blocker mentions
- Task assignments
- Completion notices

### From Calendar
- Meeting action items
- TODO items in event descriptions
- Checkboxes in notes
- Assigned tasks from attendees

### From Drive Documents
- ## Action Items sections
- ## Tasks sections
- ## Next Steps sections
- Bullet points and checkboxes
- @mentions for owners

### From Asana
- Task names and descriptions
- Assignees
- Completion status
- Due dates
- Task notes
- Subtasks (if enabled)

## Troubleshooting Quick Fixes

### No tasks collected?
1. Check date range (increase days_back)
2. Verify folder IDs in config.json
3. Confirm you have access to sources

### Missing columns in XLSX?
```python
enhance_xlsx_schema('360_project_tracker.xlsx')
```

### Dashboard shows old data?
```python
export_xlsx_to_html(xlsx_path, 'template.html', 'output.html')
```

### Categories not auto-assigning?
- Check keywords in config.json
- Manually assign in Excel
- Customize keywords in xlsx_enhancer.py

## Next Steps

After your first tracker:

1. **Customize categories**
   - Edit category keywords in config.json
   - Align with your organization's workstreams

2. **Set up recurring mode** (optional)
   - Edit config.json recurring settings
   - Schedule weekly automated updates

3. **Create HTML template** (optional)
   - Customize dashboard design
   - Add company branding

4. **Integrate with workflows**
   - Add to daily standup routine
   - Use for weekly status reports
   - Generate for board meetings

## Getting Help

1. Check docs/README.md for detailed info
2. Review skill.md for all capabilities
3. Examine config.json for all settings
4. Look at sample tracker for format examples

---

**Ready to start?** Say: "Create a project tracker with sample data"
