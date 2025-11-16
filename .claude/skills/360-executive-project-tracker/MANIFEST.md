# 360 Project Tracker - Package Manifest

**Version:** 1.2.0
**Package Date:** November 15, 2025

## Package Contents

### 📖 Documentation (Read in This Order)

1. **skill.md** - Quick reference skill definition
2. **DELIVERABLES_SUMMARY.md** - What's included and how to use it (START HERE)
3. **docs/INTEGRATION_SUMMARY.md** - Executive overview of the system
4. **docs/COMPLETE_INTEGRATION_GUIDE.md** - Complete step-by-step usage guide
5. **docs/INTEGRATION_MAPPING.md** - Technical XLSX ↔ HTML field mapping
6. **docs/README.md** - Technical documentation (original)
7. **docs/QUICK_START.md** - Basic setup and first run

### 🐍 Core Python Scripts

**Main Workflow:**
- **scripts/tracker_orchestrator.py** - Main controller that coordinates everything
- **scripts/data_collector.py** - Data extraction and parsing engine
- **scripts/tool_integrator.py** - API integrations (Gmail, Calendar, Drive, Asana)
- **scripts/project_tracker_builder.py** - Excel template builder

**Integration Scripts (v1.2.0):**
- **scripts/xlsx_enhancer.py** - Adds Category and Source Details columns
- **scripts/xlsx_to_html_export.py** - Exports XLSX data to HTML dashboard

### ⚙️ Configuration

- **config/config.json** - System configuration (customize for your team/projects)

### 📊 Templates

- **templates/360_project_tracker_template.html** - Interactive HTML dashboard template
- **Note:** Excel sample files referenced but not included in repository (generate with scripts)

## File Sizes

- Python Scripts: ~92 KB total
- Documentation: ~88 KB total
- Configuration: ~6 KB
- HTML Template: ~85 KB
- **Total Package:** ~271 KB

## What's New in v1.2.0

✨ **Enhanced Schema:** 16 columns (was 14)
- Added Column O: **Category** (workstream organization)
- Added Column P: **Source Details** (extended context)

✨ **HTML Dashboard Integration:**
- Interactive visualization layer
- Export automation from XLSX
- Stakeholder-ready presentations

✨ **Asana Integration:**
- Fully integrated and live
- "🎯 Chandler's Command Center" project support

✨ **Category Auto-Assignment:**
- 6 preset categories
- Keyword-based classification
- Customizable taxonomy

## Dependencies

**Required:**
- Python 3.8+
- openpyxl (Excel file handling)
- Claude tools access (Gmail, Calendar, Drive, Asana)

**Optional:**
- Excel or Google Sheets (for viewing/editing XLSX)
- Modern web browser (for HTML dashboard)

## Quick Validation

After installation, verify package integrity:

```bash
# Check all core files present
ls -l scripts/*.py config/*.json docs/*.md

# Should see:
# - 6 Python files
# - 1 JSON file
# - 5+ MD files
```

## Next Steps

1. Extract this package
2. Read **DELIVERABLES_SUMMARY.md**
3. Edit **config/config.json** with your settings
4. Run Quick Start workflow from **docs/QUICK_START.md**
5. Generate your first tracker

## Support

For questions or issues:
1. Check **docs/COMPLETE_INTEGRATION_GUIDE.md**
2. Review **docs/INTEGRATION_MAPPING.md**
3. Consult **skill.md** for triggers and workflows

---

**Package created:** November 15, 2025
**By:** Claude (Anthropic)
**For:** 360 Social Impact Studios
