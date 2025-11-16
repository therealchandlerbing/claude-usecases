# 360 Project Tracker: XLSX ↔ HTML Dashboard Integration Map

## System Architecture Overview

```
┌───────────────────────────────────────────────────────────────────┐
│                    DATA COLLECTION LAYER                           │
│  Gmail + Calendar + Drive (2 folders) + Asana Command Center     │
└───────────────────────────────┬───────────────────────────────────┘
                                │
                                ▼
┌────────────────────────────────────────────────────────────────────┐
│                   PYTHON ORCHESTRATOR                              │
│  • tracker_orchestrator.py   (coordinates collection)             │
│  • data_collector.py          (parses & deduplicates)             │
│  • tool_integrator.py         (integrates data sources)           │
│  • project_tracker_builder.py (builds Excel file)                 │
└───────────────────────────────┬────────────────────────────────────┘
                                │
                                ▼
┌────────────────────────────────────────────────────────────────────┐
│              XLSX FILE (Source of Truth)                           │
│  360_project_tracker.xlsx                                          │
│  • Dashboard sheet (metrics & formulas)                            │
│  • Project Status sheet (task data)                                │
│  • Instructions sheet (user guide)                                 │
└───────────────────────────────┬────────────────────────────────────┘
                                │
                                ▼
┌────────────────────────────────────────────────────────────────────┐
│           HTML DASHBOARD (Visualization Layer)                     │
│  360_project_tracker_final.html                                    │
│  • Executive summary                                               │
│  • Interactive filters                                             │
│  • Real-time calculations                                          │
│  • Visual status indicators                                        │
└────────────────────────────────────────────────────────────────────┘
```

## Data Schema Mapping

### XLSX → HTML Field Mapping

| XLSX Column (Project Status) | HTML Field | Notes |
|------------------------------|------------|-------|
| Task ID | id | Direct match |
| Task Owner | owner | Direct match |
| Task Description | description | Direct match |
| Status | status | Values: "Blocked", "In Progress", "Done", "Not Started" |
| Priority | priority | Values: "Critical", "High", "Medium", "Low" |
| Progress % | progress | Integer 0-100 |
| Blocker Details | blocker | Direct match (can be empty string) |
| Days Blocked | daysBlocked | Integer, 0 if not blocked |
| Last Update Date | lastUpdate | Format: YYYY-MM-DD |
| Source Context | source | Short label (e.g., "Gmail: Thread with...") |
| Next Steps | nextSteps | Direct match |
| First Detected | firstDetected | Format: YYYY-MM-DD |
| **Category** | category | Workstream classification |
| **Source Details** | sourceDetails | Extended context |
| Last Auto-Update | N/A | XLSX tracking field (not used in HTML) |
| Manual Override | N/A | XLSX tracking field (not used in HTML) |

### Field Details

#### 1. Category Field (Column O)
**Purpose:** Organize tasks by workstream/area

**Values:**
- "Partnership & Legal"
- "Technical & Product"
- "Pilot & Implementation"
- "Business Development"
- "Operations"
- "Strategy & Planning"

**Implementation:**
- Added as Column O in "Project Status" sheet
- Data validation dropdown
- Can be auto-inferred from task description keywords or manually set

#### 2. Source Details Field (Column P)
**Purpose:** Extended context about where information came from

**Format:** Longer text description expanding on Source Context

**Examples:**
- Source Context: "Gmail: Thread with SpacePlan legal team"
- Source Details: "Ongoing thread to finalize joint venture term sheet and cap table scenarios for SpacePlan. Legal comments consolidated in shared document."

## HTML Dashboard Data Structure

The HTML expects a JavaScript array of objects:

```javascript
const tasks = [
  {
    id: "T001",
    owner: "Chandler Lewis",
    description: "SpacePlan JV legal documentation",
    status: "In Progress",
    priority: "Critical",
    progress: 75,
    blocker: "",
    daysBlocked: 0,
    lastUpdate: "2025-11-10",
    source: "Gmail: Thread with SpacePlan legal team",
    sourceDetails: "Ongoing thread to finalize joint venture term sheet...",
    nextSteps: "Finalize term sheet and route for signatures",
    firstDetected: "2025-11-05",
    category: "Partnership & Legal"
  }
  // ... more tasks
]
```

## Integration Workflow

### 1. Data Collection → XLSX Generation

```python
from tracker_orchestrator import TrackerOrchestrator

# Initialize orchestrator
orchestrator = TrackerOrchestrator(mode='on_demand')

# Collect from all sources and build XLSX
tracker_path = orchestrator.run(
    days_back=7,
    create_new=False,  # Update existing
    use_sample_data=False  # Use live data
)
```

**Output:** Updated `360_project_tracker.xlsx` with latest task data

### 2. XLSX → HTML Dashboard Export

#### Approach A: Manual Data Transfer (Not Recommended)
1. Open XLSX file
2. Copy task data from "Project Status" sheet
3. Manually format as JavaScript array in HTML
4. Update the `const tasks = [...]` section

#### Approach B: Automated Export Script (Recommended)

**Create `xlsx_to_html.py`:**

```python
import openpyxl
import json
from datetime import datetime

def export_xlsx_to_html_data(xlsx_path, html_template_path, output_path):
    """
    Read XLSX Project Status sheet and inject into HTML dashboard
    """
    # Load workbook
    wb = openpyxl.load_workbook(xlsx_path)
    ws = wb['Project Status']

    # Extract tasks
    tasks = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        if row[0]:  # Has Task ID
            task = {
                'id': row[0],
                'owner': row[1],
                'description': row[2],
                'status': row[3],
                'priority': row[4],
                'progress': row[5] or 0,
                'blocker': row[6] or '',
                'daysBlocked': row[7] or 0,
                'lastUpdate': row[8].strftime('%Y-%m-%d') if row[8] else '',
                'source': row[9] or '',
                'nextSteps': row[10] or '',
                'firstDetected': row[11].strftime('%Y-%m-%d') if row[11] else '',
                'category': row[14] or 'Uncategorized',  # Column O
                'sourceDetails': row[15] or ''  # Column P
            }
            tasks.append(task)

    # Read HTML template
    with open(html_template_path, 'r') as f:
        html = f.read()

    # Replace tasks data in HTML
    tasks_json = json.dumps(tasks, indent=8)
    html = html.replace(
        'const tasks = [',
        f'const tasks = {tasks_json};\n        const tasks_backup = ['
    )

    # Write output
    with open(output_path, 'w') as f:
        f.write(html)

    return output_path
```

**Usage:**
```python
export_xlsx_to_html_data(
    xlsx_path='360_project_tracker.xlsx',
    html_template_path='360_project_tracker_template.html',
    output_path='360_project_tracker_dashboard.html'
)
```

### 3. Complete Workflow (Recommended)

```python
# Step 1: Collect data from sources → Update XLSX
orchestrator = TrackerOrchestrator(mode='on_demand')
xlsx_path = orchestrator.run(days_back=7, use_sample_data=False)

# Step 2: Export XLSX data → HTML dashboard
from xlsx_to_html import export_xlsx_to_html_data
html_path = export_xlsx_to_html_data(
    xlsx_path=xlsx_path,
    html_template_path='dashboard_template.html',
    output_path='live_dashboard.html'
)

print(f"Dashboard ready: {html_path}")
```

## Enhanced XLSX Schema

### Updated "Project Status" Sheet Columns

| Col | Field | Type | Source | Notes |
|-----|-------|------|--------|-------|
| A | Task ID | Text | Auto | T001, T002, etc. |
| B | Task Owner | Text | Auto/Manual | From assignee fields |
| C | Task Description | Text | Auto | Extracted from sources |
| D | Status | Dropdown | Auto/Manual | Blocked/In Progress/Done/Not Started |
| E | Priority | Dropdown | Auto/Manual | Critical/High/Medium/Low |
| F | Progress % | Number | Manual | 0-100 |
| G | Blocker Details | Text | Auto/Manual | Empty if not blocked |
| H | Days Blocked | Number | Auto | Calculated from dates |
| I | Last Update Date | Date | Auto | Most recent update |
| J | Source Context | Text | Auto | Short label |
| K | Next Steps | Text | Auto | Action items |
| L | First Detected | Date | Auto | When task first appeared |
| M | Last Auto-Update | DateTime | Auto | System tracking |
| N | Manual Override | Dropdown | Manual | Yes/No |
| **O** | **Category** | Dropdown | Manual | **NEW: Workstream classification** |
| **P** | **Source Details** | Text | Auto | **NEW: Extended context** |

### Data Validation Rules

**Column O (Category):**
```
List: Partnership & Legal, Technical & Product, Pilot & Implementation,
      Business Development, Operations, Strategy & Planning
```

**Column N (Manual Override):**
```
List: Yes, No
```

## Dashboard Features Using XLSX Data

### Executive Summary Calculations

HTML calculates from task array:
- Total tasks
- Completion rate
- Blocked tasks count
- Critical blockers (>7 days)
- Status distribution
- Priority distribution

### Interactive Filters

- Search across all fields
- Filter by status
- Filter by priority
- Filter by owner
- Filter by category (NEW)
- Quick filters (All/Blocked/Critical/My Tasks)

### Visual Indicators

- Status badges (color-coded)
- Progress bars
- Blocker severity badges
- Priority tags
- Days blocked counters

## Configuration Updates Needed

### config.json Additions

Add category classification:

```json
"classification": {
  "categories": {
    "partnership_legal": ["partnership", "legal", "contract", "agreement"],
    "technical_product": ["api", "integration", "development", "technical"],
    "pilot_implementation": ["pilot", "deployment", "rollout", "implementation"],
    "business_development": ["proposal", "pricing", "sales", "revenue"],
    "operations": ["operations", "process", "workflow", "internal"],
    "strategy_planning": ["strategy", "planning", "roadmap", "vision"]
  },
  "auto_categorize": true
}
```

### Enhanced Data Collector

Update `data_collector.py` to extract source details:

```python
def extract_source_details(source_type, raw_data):
    """
    Extract detailed context from source
    """
    if source_type == 'gmail':
        # Return email body excerpt or summary
        return raw_data.get('snippet', '')[:500]

    elif source_type == 'drive':
        # Return relevant section from doc
        return extract_relevant_section(raw_data)

    elif source_type == 'asana':
        # Return task notes/description
        return raw_data.get('notes', '')

    # ... etc
```

## Usage Patterns

### For Daily Updates

1. Run Python orchestrator to pull latest from sources
2. Review and adjust in XLSX (manual overrides, category assignments)
3. Export to HTML dashboard for team viewing

### For Executive Reporting

1. Filter HTML dashboard by priority/status
2. Use executive summary metrics
3. Export specific views or take screenshots

### For Team Collaboration

1. Share live HTML dashboard (read-only view)
2. Team updates through normal channels (Gmail, Asana, etc.)
3. Automated collection picks up changes

## File Structure

```
360-project-tracker/
├── config.json                          # System configuration
├── tracker_orchestrator.py              # Main orchestrator
├── data_collector.py                    # Data extraction
├── tool_integrator.py                   # Tool integrations
├── project_tracker_builder.py           # XLSX generation
├── xlsx_to_html.py                      # Export script (NEW)
├── README.md                            # Technical docs
├── SKILL.md                             # Skill definition
├── INTEGRATION_MAPPING.md               # This file
├── 360_project_tracker.xlsx             # Source of truth
├── 360_project_tracker_template.html    # HTML template
└── outputs/
    ├── 360_project_tracker.xlsx         # Latest XLSX
    └── 360_project_tracker_dashboard.html  # Generated dashboard
```

## Next Steps for Full Integration

### Immediate (Required for compatibility)

✅ Add Category column (O) to XLSX "Project Status" sheet
✅ Add Source Details column (P) to XLSX "Project Status" sheet
✅ Update `project_tracker_builder.py` to include new columns
✅ Add data validation for Category dropdown

### Short-term (Enables automation)

- Create `xlsx_to_html.py` export script
- Test end-to-end workflow
- Update config.json with category keywords
- Enhance `data_collector` to populate `sourceDetails`

### Long-term (Advanced features)

- Real-time sync between XLSX and HTML
- Web-based interface for manual edits
- Automated dashboard publishing
- Historical trend tracking

## Key Design Decisions

### Why XLSX as Source of Truth?

- Familiar to team members
- Supports manual overrides
- Excel formulas for calculations
- Conditional formatting
- Easy backup and version control

### Why Separate HTML Dashboard?

- Professional presentation layer
- Interactive filtering without Excel knowledge
- Shareable read-only views
- Mobile-friendly interface
- Fast, client-side performance

### Why Python Orchestrator?

- Automated data collection
- Complex parsing logic
- Multi-source integration
- Error handling
- Scheduled execution capability

## Troubleshooting

### Issue: HTML shows old data
**Solution:** Re-export XLSX to HTML using updated script

### Issue: Missing categories in HTML
**Solution:** Ensure Column O exists in XLSX and has valid values

### Issue: Source details empty
**Solution:** Update `data_collector` to populate `sourceDetails` field

### Issue: Dashboard won't load
**Solution:** Validate JavaScript task array syntax in HTML

## Version Compatibility

- **XLSX Schema:** v1.2 (adds Category + Source Details)
- **HTML Dashboard:** v1.1 (expects all 14 fields)
- **Python Scripts:** v1.0.1 (needs update for new fields)
- **Config:** v1.0.1 (needs category classification)

---

**Complete mapping documentation for the 360 Project Tracker integration system.**
