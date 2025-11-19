# Templates Directory

Ready-to-use templates for 360 Newsletter generation.

---

## Available Templates

| Template | Purpose | Size |
|----------|---------|------|
| **executive-brief-template.html** | Interactive HTML dashboard for executive briefs and newsletters | 42KB |
| **data-sources.json** | Configuration for data sources, priorities, and scoring | 16KB |

---

## executive-brief-template.html

Complete HTML template for generating 360 Executive Briefs and Newsletters.

### Features

- **Fixed sidebar navigation** with section links
- **Executive snapshot** with 4 metric cards
- **6 color-coded sections** with collapsible content
- **Interactive Chart.js visualizations**
- **Timeline component** with week/two-week views
- **Print-friendly styles**
- **Mobile responsive design**

### Sections

1. Executive Snapshot (gradient hero)
2. Partnerships & Ecosystem (blue)
3. Programs & Innovation (teal)
4. Impact & Outcomes (purple)
5. Operations & Capacity (green)
6. Strategic Horizon (orange)

### Chart Placeholders

The template includes canvas elements for:
- Service Package Market Fit (bar)
- Team Capability Analysis (radar)
- Revenue Distribution (doughnut)
- Pipeline/Trend charts (line)

### Customization Points

**Content areas to update:**
- `<h1 class="snapshot-title">` - Week label
- `.snapshot-card` elements - Executive snapshot data
- `.anchor-bullets` - Section highlights
- `.info-card` elements - Detailed content
- `.metric-card` elements - Key metrics
- Timeline configuration JavaScript

**Chart data in JavaScript:**
- `initializeCharts()` function contains all chart configurations
- Update `labels` and `data` arrays for each chart
- Modify colors and options as needed

---

## data-sources.json

Configuration file for data collection, priorities, and analysis.

### Structure

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

### Configuration Sections

**workspace**: API connection details
**priority_projects**: Projects to scan for content
**key_partners**: Organizations to monitor
**asana_queries**: Search patterns for Asana
**gmail_queries**: Search patterns for Gmail
**drive_queries**: Search patterns for Google Drive
**section_mapping**: Content-to-section assignment rules
**metric_calculations**: Formulas for dashboard metrics
**chart_data_sources**: Data sources for each chart
**significance_scoring**: Weights for prioritization algorithm

### Maintenance

**Weekly:**
- Check for new priority projects
- Verify partner list current

**Monthly:**
- Review search patterns
- Update email domains if needed

**Quarterly:**
- Comprehensive configuration review
- Update scoring weights

---

## Usage

The newsletter generator uses these templates automatically when generating output. You don't need to manually edit templates for normal use.

**For customization:**
1. Copy the template
2. Modify as needed
3. Reference the custom version in your request

**For configuration changes:**
1. Update data-sources.json
2. Changes apply to next generation

---

*For implementation details, see [../IMPLEMENTATION-GUIDE.md](../IMPLEMENTATION-GUIDE.md)*
