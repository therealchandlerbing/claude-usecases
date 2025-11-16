# 360 Project Tracker - Package Manifest

**Version:** 1.2.0
**Package Date:** November 15, 2025

## Package Contents

### 📖 Documentation (Read in This Order)

1. **skill.md** - Quick reference skill definition
2. **docs/DELIVERABLES_SUMMARY.md** - What's included and how to use it (START HERE)
3. **docs/INTEGRATION_SUMMARY.md** - Executive overview of the system
4. **docs/COMPLETE_INTEGRATION_GUIDE.md** - Complete step-by-step usage guide
5. **docs/INTEGRATION_MAPPING.md** - Technical XLSX ↔ HTML field mapping
6. **docs/SKILL_ALIGNMENT_ANALYSIS.md** - Gap analysis and version tracking
7. **docs/README.md** - Technical documentation (original)
8. **docs/QUICK_START.md** - Basic setup and first run

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

- **templates/README.md** - HTML dashboard template documentation and usage guide
- **Note:** The HTML dashboard template is embedded in `xlsx_to_html_export.py` and does not need to be stored as a separate file. The export script contains the full template and generates dashboards automatically. Excel sample files are also not included in repository (generate with scripts).

## File Sizes

- Python Scripts: ~92 KB total
- Documentation: ~120 KB total (8 markdown files)
- Configuration: ~6 KB
- Templates: README.md documenting HTML template integration
- **Total Package:** ~218 KB (core files, excluding generated outputs)

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
# - 6 Python files (tracker_orchestrator, data_collector, tool_integrator, project_tracker_builder, xlsx_enhancer, xlsx_to_html_export)
# - 1 JSON file (config.json)
# - 7 MD files in docs/ (README, QUICK_START, DELIVERABLES_SUMMARY, INTEGRATION_SUMMARY, INTEGRATION_MAPPING, COMPLETE_INTEGRATION_GUIDE, SKILL_ALIGNMENT_ANALYSIS)
# - 2 MD files in root (skill.md, MANIFEST.md)
# - 1 MD file in templates/ (README.md)
```

## Next Steps

1. Extract this package
2. Read **docs/DELIVERABLES_SUMMARY.md** (start here)
3. Review **docs/INTEGRATION_SUMMARY.md** for executive overview
4. Follow **docs/COMPLETE_INTEGRATION_GUIDE.md** for step-by-step workflows
5. Edit **config/config.json** with your settings
6. Run Quick Start workflow from **docs/QUICK_START.md**
7. Generate your first tracker

## Support

For questions or issues:
1. Start with **docs/COMPLETE_INTEGRATION_GUIDE.md** - comprehensive step-by-step guide
2. Check **docs/SKILL_ALIGNMENT_ANALYSIS.md** - gap analysis and version tracking
3. Review **docs/INTEGRATION_MAPPING.md** - technical field mapping reference
4. Consult **skill.md** for triggers and workflows
5. See **docs/README.md** for technical architecture details

---

**Package created:** November 15, 2025
**By:** Claude (Anthropic)
**For:** 360 Social Impact Studios
