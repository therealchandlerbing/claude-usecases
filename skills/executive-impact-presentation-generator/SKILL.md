---
name: Executive Impact Presentation Generator
description: Generate professional, board-ready impact reports in dual formats (presentation deck and executive document) from a single content input, with brand customization, accessibility compliance, and print optimization. Transforms organizational impact data into polished HTML outputs for board meetings and stakeholder communication.
version: 1.0.0
author: 360 Social Impact Studios
created: 2024-11-18
updated: 2025-11-22
category: reporting
complexity: medium
tags: [impact-reports, board-presentations, executive-documents, dual-format, brand-customization, accessibility, wcag, html-generation]
dependencies:
  - HTML/CSS templates
  - Impact data (metrics, outcomes, partnerships)
outputs:
  - Presentation Format HTML (landscape slides, board meetings)
  - Executive Format HTML (portrait pages, comprehensive review)
  - Print-optimized PDFs (both formats)
---

# Executive Impact Presentation Generator

Generate professional executive impact reports in two distinct formats from a single content input: **Presentation format** (fixed-slide deck) and **Executive format** (continuous scroll document).

## When to Use This Skill

Use this skill when you need to create board-ready impact reports that showcase organizational performance, outcomes, and strategy.

**Trigger phrases:**
- "Create an executive impact report for [organization]"
- "Generate a board presentation about our FY [year] impact"
- "Build an impact report showing [metrics/outcomes/partnerships]"
- "I need both presentation and executive versions of our impact report"
- "Generate our annual impact report with [data]"

## What This Skill Does

**Inputs:** Organization details, impact metrics, program outcomes, financial data, partnership information, strategic priorities

**Outputs:**
- **Presentation Format**: Fixed-slide HTML deck optimized for board presentations and PDF export (landscape slides)
- **Executive Format**: Continuous-scroll HTML document for comprehensive review and sharing (portrait pages)

**Key capabilities:**
- Dual-format generation from single content source
- Brand customization (colors, organization name, styling)
- Six core sections covering the full impact story
- Print-optimized for both formats
- Accessibility-compliant markup (WCAG 2.1 AA)
- Responsive design for all devices

## Content Structure

Both formats include these six sections:

1. **Impact Overview** (Slide 1)
   - Top-level reach metrics (lives impacted, countries, capital)
   - Year-over-year momentum highlights

2. **Regional Portfolio** (Slide 2)
   - Geographic allocation breakdown
   - Strategic priorities by region

3. **Financial Performance** (Slide 3)
   - Capital overview and efficiency metrics
   - Capital mix (grants, catalytic, commercial)
   - Safeguard principles

4. **Program Outcomes** (Slide 4)
   - Three impact pillars with metrics
   - Outcome highlights per pillar
   - Evaluation approach

5. **Partnership Ecosystem** (Slide 5)
   - Partnership statistics
   - Partner categories and flagship relationships

6. **Strategic Outlook** (Slide 6)
   - Three-horizon roadmap
   - Leadership asks and priorities

## Format Comparison

| Feature | Presentation Format | Executive Format |
|---------|-------------------|------------------|
| **Layout** | Fixed slides (1050px × 700px) | Continuous scroll sections |
| **Navigation** | Slide-based (arrows, dots, keyboard) | Section navigation + smooth scroll |
| **Content Height** | Must fit within slide boundaries | Unlimited, expands as needed |
| **Best For** | Board meetings, live presentations | Email distribution, detailed review |
| **Print Output** | Landscape slides (deck style) | Portrait pages (report style) |
| **Use Case** | PowerPoint alternative, deck format | Comprehensive document sharing |

## Usage Workflow

### Step 1: Provide Content

Share your impact data in any format:
- Structured JSON or YAML
- Spreadsheet or CSV
- Plain text description
- Previous report to update
- Bullet points by section

**Minimum required:**
- Organization name
- Brand color (hex code)
- Key metrics for each section
- Descriptions and context

### Step 2: Skill Processes Content

The skill will:
1. Parse your content into the six-section structure
2. Apply your branding (colors, organization name)
3. Populate both template formats
4. Validate completeness and structure
5. Generate two ready-to-use HTML files

### Step 3: Review & Refine

Both outputs are delivered as:
- `[Organization]-Impact-Report-Presentation-[Year].html`
- `[Organization]-Impact-Report-Executive-[Year].html`

Review in browser, test navigation and print, then share or export to PDF.

## Content Input Schema

Here's the full content structure the skill expects:

```yaml
organization:
  name: "360 Social Impact Studios"
  report_title: "Executive Impact Report FY 2025"
  brand_color: "#FF6B35"
  fiscal_year: "2025"
  report_date: "November 2025"
  audience: "Board & Executives"

impact_overview:
  reach_metrics:
    - label: "Lives Impacted"
      value: "1.8M"
      description: "Individuals reached across programs in health, skills, and income generation."
    - label: "Countries Engaged"
      value: "14"
      description: "Growing footprint with focus on Latin America, Africa, and South Asia."
    - label: "Capital Mobilized"
      value: "$42M"
      description: "Blend of grant, catalytic, and commercial capital aligned to social outcomes."

  momentum:
    - title: "34% increase in high-intensity interventions"
      badge: "Higher depth of support"
      badge_type: "success"  # success, info, warning
      description: "More participants are receiving integrated services across health, skills, and income."
    - title: "22% reduction in cost per outcome"
      badge: "Operational efficiency"
      badge_type: "info"
      description: "Process redesign, digital tools, and better partner alignment reducing costs."
    - title: "3x growth in cross-border partnerships"
      badge: null
      badge_type: null
      description: "New alliances across government, industry, and civil society unlocking scale."

regional_portfolio:
  regions:
    - name: "Latin America"
      percentage: "36%"
      description: "Deepening work in Brazil and the region, combining innovation management, workforce development, and digital health."
    - name: "Africa"
      percentage: "26%"
      description: "Focus on climate resilience, digital public goods, and inclusive finance with local partners."
    # ... 4 more regions

  strategic_priorities:
    - title: "Brazil as a regional hub"
      description: "Establish a durable presence that connects health systems, universities, and industry."
    - title: "Health and climate intersections"
      description: "Grow work where climate, health, and livelihoods overlap."
    - title: "Digital public goods"
      description: "Support reusable tools and open standards for workforce training, telehealth, and data access."

financial_performance:
  capital_overview:
    - metric: "Capital mobilized"
      value: "$42M"
      commentary: "Total capital under active management this year, including multi-year commitments."
    - metric: "Percent deployed to Global South"
      value: "78%"
      commentary: "Majority of capital directed to low and middle-income contexts."
    # ... more metrics

  capital_mix:
    - category: "Grants and Philanthropy"
      percentage: "34%"
      description: "Funds early-stage pilots, learning, and community engagement that de-risk later investment."
    - category: "Catalytic and Blended"
      percentage: "41%"
      description: "Supports ventures and programs on a path to commercial viability."
    - category: "Commercial Capital"
      percentage: "25%"
      description: "Targets scalable solutions with clear revenue models and strong impact integrity."

  safeguards:
    - title: "Guardrails on mission drift"
      description: "All commercial instruments evaluated against explicit impact criteria and equity standards."
    - title: "Risk sharing with partners"
      description: "Blended structures designed so partners share risk in proportion to role and benefit."

program_outcomes:
  pillars:
    - name: "Health Access"
      label: "Primary Pillar"
      metric_label: "Patients Served"
      metric_value: "847K"
      metric_change: "+41% from FY 2024"
      outcomes:
        - title: "Maternal health"
          description: "92% of mothers received prenatal care within recommended windows."
        - title: "Chronic disease management"
          description: "68% reduction in emergency visits for diabetes and hypertension patients."
        - title: "Telemedicine expansion"
          description: "Reached 127 remote communities previously without consistent access."
    # ... 2 more pillars

  evaluation_approach:
    - title: "Common outcome framework"
      description: "Shared indicators and definitions across programs enable meaningful comparison."
    - title: "Mixed methods evaluation"
      description: "Quantitative data paired with qualitative insight from communities and partners."
    - title: "Learning loops"
      description: "Insights from pilots feed into portfolio decisions and future program designs."

partnerships:
  statistics:
    - label: "Active Partnerships"
      value: "142"
      description: "Across 38 countries"
    - label: "New in FY 2025"
      value: "37"
      description: "Strategic collaborations launched"
    - label: "Multi-Year Agreements"
      value: "89"
      description: "Committed partnerships (63%)"

  partner_categories:
    - name: "Foundation partners"
      count: 42
      description: "Global and regional foundations providing core funding and strategic guidance."
    - name: "Corporate partners"
      count: 28
      description: "Multi-sector companies contributing expertise, technology, and resources."
    # ... more categories

  flagship_partnerships:
    - name: "Global Health Alliance"
      status_badge: "EXPANDED"
      status_type: "success"  # success, info, null
      description: "5-year, $12M commitment supporting maternal and child health across 8 countries."
    - name: "Tech for Good Initiative"
      status_badge: "NEW"
      status_type: "info"
      description: "Partnership with 4 major tech companies providing AI tools and cloud infrastructure."
    # ... more partnerships

strategic_outlook:
  roadmap:
    - horizon: "Horizon 1 · Next 6 months"
      description: "Consolidate early wins in Brazil and other anchor geographies, finalize lab and hub structures."
    - horizon: "Horizon 2 · 6 to 18 months"
      description: "Scale proven models with priority partners, expand digital public goods."
    - horizon: "Horizon 3 · 18 to 36 months"
      description: "Position organization as a leading innovation partner with scalable ventures."

  leadership_asks:
    - title: "Confirm investment envelope and risk appetite"
      description: "Clarify how much capital, and at what level of risk tolerance, can be deployed."
    - title: "Endorse priority partnerships"
      description: "Confirm which strategic partnerships are most important to advance."
    - title: "Invest in internal capacity"
      description: "Strengthen core team capacity in innovation management, partnership stewardship, and data."
```

## Branding Customization

The skill applies your brand color to:
- Accent elements (bullets, highlights, section labels)
- Interactive states (hover effects, active navigation)
- Status badges and indicators
- Navigation elements (dots, buttons)
- Logo backgrounds and gradients
- Border highlights on cards

**Recommended colors by sector:**
- **Nonprofit/Social Impact**: `#FF6B35` (vibrant orange, default)
- **Corporate/Professional**: `#0052CC` (professional blue)
- **Healthcare**: `#22C55E` (medical green)
- **Environment**: `#10B981` (earth green)
- **Education**: `#8B5CF6` (academic purple)
- **Technology**: `#06B6D4` (tech cyan)
- **Finance**: `#DC2626` (corporate red)
- **Arts/Culture**: `#EC4899` (creative pink)

**Color accessibility:** The skill automatically validates your brand color for sufficient contrast (4.5:1 ratio) against dark backgrounds.

## Key Components

Both formats use these shared components:

### Metric Displays
Large numbers with labels, descriptions, and change indicators
```
LABEL
1.8M
Description text below
```

### Content Cards
Elevated containers with headers, borders, and flexible content areas

### Bulleted Lists
Orange dot markers with title + description format

### Regional Cards
Percentage-based displays with region names and allocation details

### Data Tables
Three-column format (Metric, Value, Commentary) styled for dark theme

### Status Badges
Color-coded indicators (✓ EXPANDED, ✓ NEW) for highlighting initiatives

## Quality Assurance

Before delivery, the skill validates:

**Content completeness:**
- All 6 sections present and populated
- Required metrics included
- No placeholder text (e.g., "[Organization Name]")

**Technical accuracy:**
- Valid HTML5 structure
- All navigation functional (arrows, dots, dropdown, keyboard)
- Print styles configured correctly
- Accessibility attributes present (ARIA labels, semantic HTML)

**Visual consistency:**
- Brand color applied throughout
- Typography hierarchy maintained
- Spacing and alignment uniform
- Responsive breakpoints working (desktop, tablet, mobile)

## Export & Sharing

**To create PDFs:**

1. **Presentation format:**
   - Open HTML in Chrome
   - Press Cmd+P (Mac) or Ctrl+P (Windows)
   - Select "Save as PDF"
   - Set to **Landscape** orientation
   - Adjust margins to "None"
   - Enable "Background graphics"
   - Result: One slide per page

2. **Executive format:**
   - Open HTML in Chrome
   - Press Cmd+P (Mac) or Ctrl+P (Windows)
   - Select "Save as PDF"
   - Set to **Portrait** orientation
   - Enable "Background graphics"
   - Result: Multi-page document with section breaks

**File naming convention:**
- `[Organization]-Impact-Report-Presentation-[Year].html`
- `[Organization]-Impact-Report-Executive-[Year].html`
- `[Organization]-Impact-Report-Presentation-[Year].pdf`
- `[Organization]-Impact-Report-Executive-[Year].pdf`

## Common Use Cases

**Board presentations:** Use Presentation format for in-meeting display, advance to board via email using Executive format

**Quarterly updates:** Update metrics and momentum section, regenerate both formats quickly

**Annual reports:** Full six-section report with comprehensive data across all areas

**Partnership pitches:** Customize content to highlight relevant geography, sector, or partnership type

**Grant reporting:** Adapt content to funder requirements while maintaining professional design

**Stakeholder communications:** Executive format for email distribution, Presentation format for appendix

## Pro Tips

**Content writing best practices:**
- Keep metric descriptions under 20 words for readability
- Use active voice and present tense consistently
- Quantify impact wherever possible (numbers, percentages, change)
- Include year-over-year comparisons to show trajectory
- Front-load key information in descriptions

**Format selection:**
- **Presentation format** when: Live meeting presentation, PDF deck needed, one-page-per-topic layout preferred
- **Executive format** when: Comprehensive email sharing, detailed reading expected, multi-page sections acceptable
- **Generate both** when: Different audiences (meeting vs email), want flexibility in distribution

**Branding:**
- Test brand color for contrast before finalizing
- Stick to one primary color for consistency
- Use secondary teal accent sparingly for special callouts

**Navigation:**
- Presentation: Design for linear progression (cover → slide 1 → 6)
- Executive: Assume readers may jump between sections
- Both: Test all navigation methods (arrows, dots, dropdown, keyboard)

**Print optimization:**
- Always use Chrome for most consistent PDF rendering
- Preview before exporting to check page breaks
- Enable background graphics to preserve design
- Presentation: Landscape, one slide per page
- Executive: Portrait, continuous flow

## Limitations

**This skill does not:**
- Create original content or write descriptions (requires user-provided data)
- Generate charts, graphs, or data visualizations beyond template structure
- Translate content to other languages
- Integrate with external data sources automatically
- Support embedded video or interactive media
- Connect to live data feeds or APIs

**Content constraints:**
- Presentation format: Content must fit within slide boundaries (height limit ~700px)
- Executive format: No height limits, but very long sections may impact readability
- Maximum ~1500 words per section recommended for both formats
- Tables limited to 5-6 rows for optimal layout
- Regional cards support exactly 6 regions (can be adapted for fewer)
- Metric groups work best with 3 items per row

## Troubleshooting

**Issue: Content overflows presentation slide**
**Solution:** Reduce text length, use bullet points instead of paragraphs, move detailed content to Executive format only, or split into two slides

**Issue: Brand color not displaying**
**Solution:** Verify hex code format (#RRGGBB), check CSS variable was updated in both templates, clear browser cache

**Issue: Navigation broken or skipping slides**
**Solution:** Verify slide data-slide attributes are sequential (0, 1, 2, 3, 4, 5, 6), check JavaScript console for errors

**Issue: Print layout incorrect**
**Solution:** Use Chrome browser, select correct orientation (landscape for presentation, portrait for executive), enable background graphics, check print preview first

**Issue: Content not aligned across formats**
**Solution:** Ensure content structure matches expected schema, verify all required fields populated

**Issue: Mobile display problems**
**Solution:** Test responsive breakpoints, consider simplifying complex tables for mobile, verify viewport meta tag present

## Example Interactions

### Example 1: Quick Generation
```
User: "Create an executive impact report for Acme Foundation's FY 2024. We reached 2.3M people, mobilized $58M, work in 22 countries. Use blue (#0052CC) as our brand color."
Claude: "I'll gather the remaining details for all six sections. Let me start with your Impact Overview momentum highlights. What were your top 3-4 year-over-year achievements?"

[After gathering content, generates both formats and provides download links]
```

### Example 2: Full Content Upload
```
User: "Here's our complete FY 2025 data in this spreadsheet. Generate both presentation and executive versions using orange (#FF6B35)."

Claude: [Parses spreadsheet, maps to content schema, populates both templates, validates, delivers HTML files with download links]
```

### Example 3: Update Existing
```
User: "Update last quarter's report with these new numbers: 142 active partnerships (was 128), 37 new partnerships this quarter, 89 multi-year agreements (was 76)."

Claude: [Updates partnership section data, regenerates both formats with new metrics]
```

### Example 4: Custom Section Focus
```
User: "I need to emphasize our Brazil work in the regional portfolio section. Can you create a report that highlights Brazil's 40% allocation and our three strategic priorities there?"

Claude: [Adjusts regional breakdown to feature Brazil prominently, generates customized versions]
```

## Advanced Usage

### Customizing Beyond Defaults

While the skill provides two standard formats, you can request:

**Content variations:**
- Emphasis on specific sections (e.g., "Focus on financial performance")
- Custom section ordering (e.g., "Put partnerships before outcomes")
- Additional subsections (e.g., "Add a risk mitigation section under financials")

**Design variations:**
- Alternative brand color schemes
- Custom badge text or colors
- Modified spacing or typography
- Organization logo integration (if provided)

**Format adaptations:**
- Presentation with more slides (split content differently)
- Executive with table of contents
- Hybrid format (continuous scroll but fixed-width sections)

### Integration with Other Tools

**After generation, you can:**
- Import into Google Slides (presentation format serves as reference)
- Convert to PowerPoint (use PDF as base, rebuild with content)
- Embed in websites (both formats work as standalone pages)
- Include in email campaigns (executive format works well)
- Archive in document management systems

**Pair with other skills:**
- Use 360-newsletter-generator for pre-board meeting briefs
- Use workflow-process-generator for program workflow visualizations
- Use design-director for additional visual polish

## Version Control & Updates

**Managing multiple versions:**

The skill supports generating reports for different time periods while maintaining consistency:

```
User: "Generate our FY 2024 report"
[Delivers: Organization-Impact-Report-Presentation-2024.html + Executive version]

User: "Now generate FY 2025 with updated metrics"
[Delivers: Organization-Impact-Report-Presentation-2025.html + Executive version]
```

**Quarterly vs annual:**
- Quarterly: Focus on momentum and recent outcomes, lighter on strategic outlook
- Annual: Full six-section treatment with comprehensive data

**Update workflow:**
1. Start with previous report content
2. Update changed metrics and descriptions
3. Regenerate both formats
4. Compare to identify changes
5. Distribute updated versions

## Accessibility Features

Both formats include:

**Keyboard navigation:**
- Arrow keys move between slides/sections
- Tab key navigates interactive elements
- Enter/Space activates buttons
- Home/End jump to first/last slide

**Screen reader support:**
- Semantic HTML structure (header, main, nav, article)
- ARIA labels for all interactive elements
- Skip-to-content link
- Alt text for decorative elements marked appropriately

**Visual accessibility:**
- Sufficient color contrast (4.5:1 minimum)
- Focus indicators on interactive elements
- Reduced motion support (for users with motion sensitivity)
- Scalable text (no absolute font sizes)

**Print accessibility:**
- High-contrast mode for better readability
- Print-optimized layouts
- Page breaks at logical sections

## Performance & Compatibility

**Browser support:**
- Chrome/Edge (recommended for PDF export)
- Firefox
- Safari
- Mobile browsers (iOS Safari, Chrome Mobile)

**Performance:**
- Lightweight (< 200KB per file including all styles)
- No external dependencies except Google Fonts
- Fast load times (< 1 second on broadband)
- Smooth animations and transitions
- Works offline (fully self-contained)

**Device support:**
- Desktop (1440px and wider)
- Laptop (1024px - 1440px)
- Tablet (768px - 1024px)
- Mobile (< 768px)

## File Delivery

When the skill completes, you'll receive:

**Files:**
1. `[Organization]-Impact-Report-Presentation-[Year].html`
2. `[Organization]-Impact-Report-Executive-[Year].html`

**Each file includes:**
- Complete self-contained HTML with embedded CSS
- All content populated from your input
- Brand customization applied
- Navigation fully functional
- Print styles configured
- Accessibility features enabled

**File locations:**
- Files delivered as downloadable artifacts
- Direct download links provided
- Ready to open in any browser
- No additional setup required

## Next Steps After Generation

**Immediate actions:**
1. Open both HTML files in Chrome
2. Click through all navigation (arrows, dots, dropdown, keyboard)
3. Verify content accuracy in all sections
4. Test print/PDF export for both formats
5. Check mobile responsiveness (resize browser window)

**Before distribution:**
1. Review brand color application
2. Spell-check all content
3. Verify metrics and numbers
4. Test download links with colleagues
5. Create PDFs for archival

**Distribution:**
1. **Presentation format**: Send to meeting participants, use in live board sessions
2. **Executive format**: Email to full stakeholder list, post to board portal
3. **PDFs**: Archive in document management system

**Maintenance:**
1. Save source data/spreadsheet for future updates
2. Archive generated HTML files by fiscal year
3. Note any customizations made for next report cycle
4. Collect feedback for improvements

## Related Skills

**Pair this skill with:**

- **360-newsletter-generator**: Create pre-board meeting briefs with context on specific report sections
- **workflow-process-generator**: Visualize program workflows referenced in outcomes section
- **design-director**: Apply additional design polish beyond templates
- **intelligence-extractor**: Extract partnership and funding data for report sections

---

## Quick Reference Card

**To generate a report:**
1. Provide organization name and brand color
2. Share content for all six sections (or upload structured data)
3. Skill generates both HTML formats
4. Download, review, export to PDF, distribute

**When to use Presentation format:**
Board meetings, live presentations, PDF decks, one-slide-per-topic

**When to use Executive format:**
Email sharing, comprehensive review, multi-page sections, detailed reading

**Required inputs:**
Organization name, brand color, metrics for all six sections

**Outputs:**
Two HTML files ready for browser viewing and PDF export

**Time to generate:**
5-10 minutes after content provided

---

**Need help?** Ask Claude to:
- Explain any section in detail
- Guide you through content gathering
- Show example content for a specific section
- Help customize beyond default formats
- Troubleshoot issues with generation or display
- Adapt the report for specific audiences or use cases
