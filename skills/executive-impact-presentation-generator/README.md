# Executive Impact Presentation Generator

A Claude skill that generates professional board-ready impact reports in two formats (Presentation and Executive) from a single content input.

## Overview

This skill transforms your organizational impact data into polished, print-ready reports suitable for board meetings, stakeholder communications, and annual reporting.

**Two output formats:**
1. **Presentation Format**: Fixed-slide deck optimized for live presentations (landscape slides)
2. **Executive Format**: Continuous-scroll document for comprehensive review (portrait pages)

**Six core sections:**
1. Impact Overview (reach metrics + momentum)
2. Regional Portfolio (geographic allocation + priorities)
3. Financial Performance (capital structure + efficiency)
4. Program Outcomes (three impact pillars + evaluation)
5. Partnership Ecosystem (collaborations + flagship partnerships)
6. Strategic Outlook (roadmap + leadership asks)

## Quick Start

### 1. Trigger the Skill
```
"Create an executive impact report for [your organization]"
```

### 2. Provide Content
Use the CONTENT_SCHEMA_TEMPLATE.md to organize your data, then share:
- Organization name and brand color
- Impact metrics for all 6 sections
- Descriptions and context

### 3. Receive Outputs
Two HTML files ready for download:
- `[Organization]-Impact-Report-Presentation-[Year].html`
- `[Organization]-Impact-Report-Executive-[Year].html`

### 4. Export to PDF
Open in Chrome, press Cmd+P (Mac) or Ctrl+P (Windows):
- Presentation: Set to **Landscape**
- Executive: Set to **Portrait**
- Enable background graphics, save as PDF

## Documentation Files

### INDEX.md (Start Here)
**Navigation hub for the skill**
- Quick start guide
- File guide with descriptions
- Six sections overview
- Format comparison
- Export instructions

**Read this for:** First-time orientation and quick navigation

### SKILL.md (Complete Documentation)
**Comprehensive reference guide**
- When and how to use the skill
- Complete content requirements for all sections
- Format comparison and selection guidance
- Branding customization options
- Quality assurance standards
- Troubleshooting guide
- Example interactions

**Read this for:** Understanding what the skill does, learning how to use it effectively, troubleshooting issues

### CONTENT_SCHEMA_TEMPLATE.md (Content Input Guide)
**Fill-in-the-blank template for providing your organization's data**

**Includes:**
- Complete content structure for all 6 sections
- Field-by-field guidance
- Examples and formatting tips
- Quality checklist

**Use this for:** Organizing your content before generation, ensuring completeness, providing structured input

### QUICK_REFERENCE.md (Fast Lookup)
**One-page reference card for quick lookups**

**Contains:**
- 5-minute start guide
- Content requirements summary
- Format comparison table
- Brand color suggestions
- Export instructions
- Navigation reference
- Common troubleshooting

**Use this for:** Quick answers, reminders, frequent tasks

## File Structure

```
executive-impact-presentation-generator/
├── INDEX.md                      # START HERE - Navigation hub
├── README.md                     # This file - Skill overview
├── SKILL.md                      # Complete documentation
├── CONTENT_SCHEMA_TEMPLATE.md    # Content input guide
├── QUICK_REFERENCE.md            # Fast lookup reference
│
├── templates/                    # HTML templates
│   ├── presentation-template.html    # Landscape slide deck
│   └── executive-template.html       # Portrait continuous document
│
├── references/                   # Reference materials (future)
│   └── (future: branding guide, examples, etc.)
│
└── examples/                     # Sample outputs (future)
    └── (future: sample reports)
```

## Key Features

**Dual-format generation**
- Presentation: Fixed slides for meetings
- Executive: Continuous scroll for sharing
- Same content, optimized layouts

**Brand customization**
- Custom colors (any hex code)
- Organization name throughout
- Consistent visual identity

**Print-optimized**
- Presentation: One slide per page (landscape)
- Executive: Multi-page document (portrait)
- High-quality PDF export

**Accessibility**
- Keyboard navigation
- Screen reader support
- WCAG 2.1 AA compliant
- Reduced motion support

**Responsive**
- Desktop, tablet, mobile
- All browsers supported
- Works offline

## When to Use Each Format

### Presentation Format
**Best for:**
- Board meeting presentations
- Live deck display
- PDF slide decks
- One-page-per-topic layout
- PowerPoint alternative

**Constraints:**
- Content must fit within slide (height limit ~700px)
- Linear progression expected
- Landscape orientation

### Executive Format
**Best for:**
- Email distribution
- Comprehensive stakeholder review
- Detailed reading
- Multi-page sections
- Document sharing

**Advantages:**
- No height limits (content expands)
- Sections can be any length
- Better for dense information
- Portrait orientation

### Generate Both When:
- You have different audiences (meeting attendees vs email recipients)
- You want flexibility in distribution
- You're creating a complete documentation package
- You're archiving annual results

## Content Requirements

**Minimum required per section:**

1. **Impact Overview**: 3 reach metrics, 3 momentum highlights
2. **Regional Portfolio**: 6 regions with allocations, 3 strategic priorities
3. **Financial Performance**: 4 capital metrics, 3-part capital mix, 2 safeguards
4. **Program Outcomes**: 3 impact pillars (each with metric + 3 outcomes), 3 evaluation principles
5. **Partnership Ecosystem**: 3 overall stats, 4 partner categories, 4 flagship partnerships
6. **Strategic Outlook**: 3-horizon roadmap, 3 leadership asks

**See CONTENT_SCHEMA_TEMPLATE.md for complete details**

## Branding Options

**Default colors by sector:**
- Nonprofit/Social Impact: `#FF6B35` (vibrant orange)
- Corporate/Professional: `#0052CC` (professional blue)
- Healthcare: `#22C55E` (medical green)
- Environment: `#10B981` (earth green)
- Education: `#8B5CF6` (academic purple)
- Technology: `#06B6D4` (tech cyan)

**Custom branding:**
- Any hex color supported
- Organization logo integration (optional)
- Custom fonts (advanced)
- Modified spacing (advanced)

## Quality Standards

Before delivery, the skill ensures:
- All 6 sections complete
- No placeholder text
- Valid HTML structure
- Functional navigation (all methods)
- Print styles configured
- Accessibility features present
- Responsive breakpoints working
- Brand color applied consistently

## Common Use Cases

**Board presentations**
→ Generate presentation format for quarterly/annual board meetings

**Stakeholder communications**
→ Generate executive format for email distribution to funders, partners

**Annual reports**
→ Generate both formats, use presentation for meetings and executive for archival

**Grant reporting**
→ Customize content for specific funder, maintain professional format

**Partnership pitches**
→ Adapt content to emphasize relevant geography/sector for prospects

**Quarterly updates**
→ Update metrics, regenerate both formats quickly

## Example Interactions

### Quick Generation
```
You: "Create an executive impact report for Acme Foundation's FY 2024.
We reached 2.3M people, mobilized $58M, work in 22 countries.
Use blue (#0052CC) as our brand color."

Claude: [Requests details for the 6 sections, then generates both formats]
```

### Update Existing
```
You: "Update our Q3 report with these new partnership numbers:
142 active partnerships, 37 new this quarter, 89 multi-year agreements."

Claude: [Updates partnership section, regenerates both formats]
```

### Full Content Input
```
You: "Here's our complete FY 2025 data [provides structured content].
Generate both formats using our orange brand color."

Claude: [Parses content, populates templates, delivers both HTML files]
```

## Support

**For questions or help:**
- Ask Claude to explain any section of the documentation
- Request guided content gathering (step-by-step)
- Get examples for specific sections
- Troubleshoot generation or display issues
- Customize beyond default formats

**Common requests:**
- "Show me an example of the Impact Overview section"
- "Help me gather content for the Financial Performance section"
- "Can I add a seventh section about [topic]?"
- "How do I update last quarter's report with new numbers?"
- "What if my content doesn't fit in the presentation slides?"

## Integration

**Works with other skills:**
- **360-newsletter-generator**: Create pre-board meeting briefs
- **workflow-process-generator**: Visualize program workflows
- **design-director**: Apply additional design polish
- **intelligence-extractor**: Extract partnership data for reports

**Export options:**
- PDF (via Chrome print)
- Embed in website (HTML)
- Import to Google Slides (manual)
- Archive in document management systems

## Technical Specifications

**Browser support:**
- Chrome/Edge (recommended)
- Firefox
- Safari
- Mobile browsers

**File specifications:**
- Size: < 200KB per file
- Dependencies: Google Fonts only
- Load time: < 1 second
- Format: Self-contained HTML + embedded CSS
- Offline: Works fully offline after loading

**Accessibility:**
- WCAG 2.1 AA compliant
- Keyboard navigation
- Screen reader support
- Focus indicators
- Reduced motion support

## Limitations

**What this skill does NOT do:**
- Create original content (requires your data)
- Generate charts/graphs beyond template structure
- Translate to other languages automatically
- Connect to live data sources/APIs
- Support video or interactive media

**Content constraints:**
- Presentation slides have height limits (~700px)
- Executive format recommended max ~1500 words per section
- Tables work best with 5-6 rows
- Regional allocation requires exactly 6 regions

## Next Steps

1. **Read INDEX.md** for quick orientation and navigation
2. **Fill out CONTENT_SCHEMA_TEMPLATE.md** with your data
3. **Request generation** from Claude
4. **Review outputs** in browser
5. **Export to PDF** using Chrome
6. **Distribute** to appropriate audiences

---

## Version History

**v1.0 - November 2025**
- Initial release
- Dual-format generation (Presentation + Executive)
- Six core sections
- Brand customization
- Print optimization
- Accessibility compliance
- Responsive design

---

**Questions?** Ask Claude for help with any aspect of using this skill.

**Ready to start?** Say: *"Create an executive impact report for [your organization]"*
