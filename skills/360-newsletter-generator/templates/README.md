# Templates Directory

This directory contains the newsletter template and configuration files.

## Files

### data-sources.json
Complete configuration for newsletter generation including:
- Workspace settings (Asana GID, Gmail user, timezone)
- Priority projects list
- Key partner organizations
- Search query templates for Asana, Gmail, Drive
- Section mapping rules
- Metric calculation definitions
- Chart data source specifications
- Significance scoring parameters
- Date format requirements

**Usage:** This file is referenced during newsletter generation to determine which projects to scan, which partners to monitor, how to score content, and how to organize sections.

**Maintenance:** Update quarterly or when partnerships/projects change.

### Newsletter HTML Template

The complete newsletter template includes:

#### Structure
- Fixed sidebar navigation (8 sections)
- Main content area with responsive grid
- Executive summary banner (gradient blue)
- Section-based organization with color coding:
  - Partnerships: Blue (#3b82f6)
  - Operations: Green (#10b981)
  - Strategy: Orange (#f59e0b)
- Interactive Chart.js visualizations
- Timeline section for upcoming events
- Action items section with urgency indicators

#### Key Features
- **Sidebar Navigation:** Fixed left sidebar with smooth scroll to sections
- **Executive Summary:** Gradient banner with 3-4 highlight cards
- **Insight Cards:** Color-coded cards for different section types
- **Chart Containers:** Styled containers for Chart.js visualizations
- **Status Chips:** Color-coded urgency indicators (Critical, Action Required, Success)
- **Timeline:** Horizontal scroll timeline for week/month ahead
- **Action Items:** Yellow-highlighted section for items requiring decisions
- **Responsive Design:** Mobile-friendly layout with breakpoints
- **Print-Friendly:** Optimized for PDF export

#### CSS Variables
```css
--color-primary: #1e3a8a (dark blue)
--color-partnerships: #3b82f6 (blue)
--color-operations: #10b981 (green)
--color-strategy: #f59e0b (orange)
--color-critical: #dc2626 (red)
--color-warning: #f59e0b (yellow)
```

#### External Dependencies
- **Chart.js:** CDN for interactive charts
- **Font Awesome:** CDN for icons
- System fonts (no custom font loading)

#### Sections Generated
1. **Executive Summary** - Key highlights in gradient banner
2. **Lead Story** - Most significant development (if score 95-100)
3. **Partnerships & Ecosystem** - Partnership updates and developments
4. **Programs & Innovation** - Project work and deliverables
5. **Impact & Outcomes** - Social impact metrics and testimonials
6. **Operations & Capacity** - Team and infrastructure updates
7. **Strategic Horizon** - Upcoming events and decision deadlines
8. **Action Items** - (Optional) Items requiring decisions

#### Chart Types Implemented
- **Doughnut/Pie:** Partnership portfolio, regional distribution
- **Bar (horizontal):** Service packages, market fit scores
- **Bar (vertical):** Pipeline stages, completion velocity
- **Radar:** Team capabilities, partnership health
- **Line:** Revenue trends, impact metrics over time

#### Typography & Spacing
- **Fonts:** System font stack (-apple-system, BlinkMacSystemFont, etc.)
- **Hierarchy:**
  - Lead headline: 38px
  - Section titles: 28px
  - Card titles: 18px
  - Body text: 14-15px
  - Metadata: 12px
- **Spacing:**
  - Container: max-width 1400px
  - Section padding: 40px
  - Card gaps: 24px

#### Color Palette
- **Background:** #fafafa (off-white), containers #ffffff (white)
- **Text:** #1a1a1a (near-black), secondary #6b7280 (gray)
- **Borders:** #e5e7eb (light gray)
- **Chart colors:** Monochromatic blues, grays, with section-specific accents

## Template Usage

When generating a newsletter:

1. **Load configuration** from `data-sources.json`
2. **Collect data** following protocols in reference guides
3. **Score and analyze** content using significance scoring rules
4. **Generate HTML** using the template structure
5. **Populate sections** with analyzed content
6. **Create charts** using Chart.js with data from collection
7. **Apply styling** using CSS variables and responsive design
8. **Deliver artifact** as interactive HTML

## Customization

### Updating Priority Projects
Edit `data-sources.json`:
```json
{
  "priority_projects": {
    "projects": [
      {
        "name": "Your Project Name",
        "category": "partnerships|programs|impact|operations",
        "priority": "high|medium|low",
        "search_method": "typeahead|partial_match"
      }
    ]
  }
}
```

### Updating Key Partners
Edit `data-sources.json`:
```json
{
  "key_partners": {
    "partners": [
      {
        "name": "Partner Name",
        "domain": "partnerdomain.com",
        "category": "partnerships",
        "importance": "critical|high|medium|low"
      }
    ]
  }
}
```

### Adjusting Section Colors
Modify CSS variables in template:
```css
:root {
  --color-partnerships: #your-color;
  --color-operations: #your-color;
  --color-strategy: #your-color;
}
```

### Adding New Chart Types
1. Add chart specification to `data-sources.json`
2. Create Chart.js configuration in template
3. Ensure data collection provides necessary metrics

## Template Sections Detail

### Executive Summary
- **Purpose:** At-a-glance highlights for executives
- **Content:** 3-4 most significant developments
- **Format:** Gradient blue banner with white summary cards
- **Criteria:** Only items scoring 85+

### Lead Story (Optional)
- **Purpose:** Feature most significant single development
- **Content:** Detailed story with context and implications
- **Format:** Large headline, context paragraph, bullet points
- **Criteria:** Only if item scores 95-100

### Partnership Cards
- **Title:** Bold partner name + development
- **Status chip:** Critical/Action/Success indicator
- **Context:** 1-2 sentence overview
- **Bullets:** 3-5 specific details with bold labels
- **Chart:** Optional partnership-specific chart

### Operation Cards
- **Title:** Team/infrastructure development
- **Status chip:** As appropriate
- **Context:** Why this matters
- **Bullets:** Specific updates
- **Chart:** Often capacity or velocity charts

### Timeline Section
- **Purpose:** Show upcoming week/month
- **Format:** Horizontal scrolling day cards
- **Content:** Events, deadlines, meetings
- **Criteria:** Items with specific dates in next 7-30 days

### Action Items Section
- **Purpose:** Flag items requiring decisions
- **Format:** Yellow-highlighted cards with metadata
- **Content:** Specific action + context + responsible party + deadline
- **Criteria:** Flagged during content analysis

## Quality Assurance

Before using template, verify:
- [ ] All Chart.js chart IDs match canvas elements
- [ ] CSS variables are defined
- [ ] Font Awesome CDN loads correctly
- [ ] Chart.js CDN loads correctly
- [ ] Responsive breakpoints work
- [ ] Print styles are appropriate
- [ ] All sections have proper IDs for navigation
- [ ] Sidebar navigation links match section IDs

## Examples

See `examples/` directory for:
- `weekly-newsletter-example.html` - Sample weekly output
- `monthly-board-brief-example.html` - Sample monthly output

## Maintenance

**Weekly:** No maintenance required

**Monthly:** Verify external CDN links still work

**Quarterly:**
- Update priority projects as needed
- Update partner organizations as partnerships change
- Review section color schemes
- Check responsive design on new devices

**Annually:**
- Review complete template structure
- Consider design refresh if needed
- Update Chart.js version if major update available
- Audit all configuration settings

---

For complete implementation details, see:
- [Data Collection Guide](../references/data-collection-guide.md)
- [Content Analysis Framework](../references/content-analysis-framework.md)
- [Chart Specifications](../references/chart-specifications.md)
- [Writing Style Guide](../references/writing-style-guide.md)
