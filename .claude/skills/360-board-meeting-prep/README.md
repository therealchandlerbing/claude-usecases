# 360 Board Meeting Prep

**Transform scattered organizational data into polished, governance-ready board meeting packets with multi-format outputs and professional design elevation.**

---

## Overview

The 360 Board Meeting Prep skill automatically synthesizes financial, operational, strategic, and governance intelligence from Asana, QuickBooks, Gmail, and Google Drive into professionally formatted board materials across multiple output formats.

**Key differentiator**: All outputs are automatically routed through the design-director skill for professional visual polish, ensuring board-ready, publication-quality materials every time.

---

## Quick Start

### Trigger the Skill

Say any of these:
- "Help me prep for the [date] board meeting"
- "Create a board packet for [date]"
- "Build board meeting materials"
- "Generate board documents"

### What You'll Get

**Multi-format outputs**:
1. **DOCX Board Packet** - Complete master document with all sections
2. **HTML Dashboards** - Interactive visualizations for review
3. **PDF Exports** - Print-ready distribution copies

**Five core documents**:
1. Financial Dashboard
2. Client Portfolio Health Report
3. Strategic Initiatives Update
4. Governance & Compliance Report
5. Motion Tracking Sheet

---

## Features

### Multi-Source Data Intelligence

Automatically pulls and cross-validates data from:
- **Asana** - Pipeline projects, action items, governance tasks
- **QuickBooks** - Revenue, expenses, receivables, cash position
- **Gmail** - Partner communication patterns
- **Google Drive** - Historical context and archival

### Professional Design Elevation

Every output receives design-director polish:
- **Stripe exemplar** for financial dashboards (trust, clarity)
- **Swiss design** for systematic layouts
- **Linear exemplar** for strategic visualizations
- Typography hierarchy and spacing scale
- Accessibility compliance

### Interactive Dashboards

HTML dashboards with:
- Real-time data visualizations
- Chart.js powered charts
- Responsive design (desktop/tablet/mobile)
- Dark theme aesthetic
- Self-contained, shareable files

### Governance Compliance

- Pre-drafted motions for common agenda items
- Action item tracking with Asana integration
- Compliance calendar monitoring
- Board composition records
- Vote result documentation

---

## Workflow

### Timeline

| Phase | Timing | Activities |
|-------|--------|------------|
| 1. Data Collection | T-10 days | Gather meeting parameters, pull data, identify gaps |
| 2. Draft Generation | T-7 days | Create all 5 documents, cross-validate, generate dashboards |
| 3. Review & Refinement | T-7 to T-2 | User feedback, iterative updates, approval |
| 4. Final Generation | T-2 days | DOCX formatting, HTML dashboards, design elevation, storage |
| 5. Meeting Support | Meeting day | Real-time assistance, motion tracking |
| 6. Post-Meeting Follow-up | T+2 days | Action items to Asana, archival, minutes |

### User Interaction

The skill guides you through:
1. **Meeting parameters** - Date, type, agenda topics
2. **Data gaps** - Items needing clarification
3. **Draft review** - Approve or revise each section
4. **Final confirmation** - Output format selection
5. **Delivery** - Download links and distribution guidance

---

## Output Formats

### DOCX Documents

**Master Board Packet includes**:
- Cover page with meeting information
- Meeting info table (gray labels, professional formatting)
- Motion tracking sheet with checkboxes
- Section dividers between reports
- All five report sections

**Formatting specifications**:
- Typography: Arial/Calibri hierarchy
- Tables: Proper borders, shading, alignment
- Spacing: Consistent 8-point scale
- Print-ready: Works in Word and Google Docs

### HTML Dashboards

**Financial Intelligence Dashboard**:
- Revenue vs target gauge
- Expense breakdown pie chart
- Cash runway indicator
- AR aging visualization
- Pipeline waterfall chart

**Portfolio Health Dashboard**:
- Client tier distribution
- Relationship health indicators
- Engagement metrics
- Capacity utilization

**Strategic Progress Dashboard**:
- Initiative timeline/roadmap
- Priority progress bars
- Partnership status grid
- Risk indicators

### PDF Exports

- Portrait document PDF (complete packet)
- Landscape slide PDF (dashboards)
- Print-optimized with background graphics
- Proper page breaks and margins

---

## Data Requirements

### Required Data Sources

| Source | Data Points | Access Method |
|--------|-------------|---------------|
| Asana | Pipeline projects, governance tasks | MCP integration |
| QuickBooks | Revenue, expenses, AR, cash | MCP or CSV export |
| Gmail | Partner communication patterns | MCP integration |
| Google Drive | Historical board packets | MCP integration |

### Expected Asana Custom Fields

For pipeline projects:
- `contract_value` - Dollar amount
- `probability` - Percentage (0-100)
- `stage` - Proposal/Negotiation/Signed/Delivered/Invoiced/Paid
- `client_tier` - Tier 1/2/3

### QuickBooks CSV Fallback

If QuickBooks MCP unavailable, provide exports for:
- Profit & Loss (revenue and expenses)
- AR Aging Detail (receivables)
- Balance Sheet (cash position)

---

## Design-Director Integration

### Automatic Elevation

All outputs automatically receive design-director polish:

**DOCX Documents**:
- Typography hierarchy (Stripe exemplar)
- Consistent spacing scale
- Professional table formatting
- Print readiness verification

**HTML Dashboards**:
- Color palette (360 brand + professional accents)
- Data visualization clarity
- Responsive design
- Accessibility compliance

**PDF Exports**:
- Print optimization
- Background graphics
- Page break placement
- Header/footer formatting

### Quality Standards

Design-director ensures:
- Would fit in Stripe/Linear/Apple design system
- No template-based appearance
- Hand-crafted visual quality
- Portfolio-ready polish

---

## Quality Assurance

### Automated Validation

**Data integrity checks**:
- Cross-document consistency
- Revenue alignment across sources
- Capacity calculation accuracy
- Pipeline math verification

**Completeness checks**:
- All strategic priorities addressed
- All Tier 1 partners covered
- All prior action items accounted for
- All agenda items have motions

### Flag System

Automatic flags for:
- Cash runway <6 months
- Receivables >60 days
- Budget variance >20%
- Partner engagement gaps
- Stale project data

---

## Example Usage

### Basic Board Meeting Prep

```
User: Help me prep for the November 15 board meeting

Agent: I'll help you prepare for the November 15 board meeting. Let me gather some information:

1. What type of meeting is this? (Annual, Quarterly, Special)
2. What are the key agenda topics?
3. Do you need motion tracking?
4. Which output formats do you need?
   - DOCX board packet (recommended)
   - HTML dashboards (for interactive review)
   - PDF exports (for distribution)

User: It's a quarterly meeting. Key topics are financial review, SpacePlan partnership update, and Brazil expansion approval. Yes to motion tracking. I need all formats.

Agent: I'm pulling data from Asana, QuickBooks, Gmail, and Drive. This will take about 2 minutes...

[Data collection completes]

I found 3 items needing clarification:
- GenIP project hasn't been updated in 18 days
- SpacePlan contract value is missing probability
- Cash position shows <4 months runway

Can you provide updates on these before I generate drafts?
```

### With HTML Dashboards

```
User: I want to review the financial data interactively before the meeting

Agent: I'll generate an interactive Financial Intelligence Dashboard along with your board packet. The dashboard will include:

- Revenue vs Target gauge chart
- Expense breakdown pie chart
- Cash runway indicator
- AR aging stacked bar
- Pipeline waterfall chart

These visualizations are design-elevated using Stripe's dashboard exemplar for clarity and trust.
```

---

## Troubleshooting

### Common Issues

**QuickBooks data unavailable**
- Provide CSV exports (Profit & Loss, AR Aging, Balance Sheet)
- Skill will flag: "Using QuickBooks export from [date]"

**Asana custom fields missing**
- Skill will request manual data entry
- Provide contract value and probability for each project

**Design elevation not applied**
- Ensure design-director skill is available
- Check for any blocking errors
- Basic formatting will be applied as fallback

**HTML dashboard not rendering**
- Check browser compatibility (Chrome recommended)
- Ensure JavaScript is enabled
- Try clearing browser cache

### Data Gap Handling

The skill handles missing data gracefully:
- Flags gaps clearly with "Warning:" markers
- Requests user clarification
- Proceeds with available data when possible
- Notes data source limitations in output

---

## Related Skills

### Required Integration

- **design-director** - Professional visual polish for all outputs

### Recommended Companions

- **skill-orchestrator** - Complex workflow coordination
- **executive-intelligence-dashboard** - Weekly intelligence context
- **ceo-advisor** - Strategic decision support

---

## File Locations

### Generated Outputs

```
/mnt/user-data/outputs/
  360_Board_Packet_[Month]_[Year]_Professional.docx
  360_Financial_Dashboard_[Month]_[Year].html
  360_Portfolio_Dashboard_[Month]_[Year].html
  360_Strategic_Dashboard_[Month]_[Year].html
```

### Google Drive Storage

```
/Board Materials/[YYYY-MM]/
  [All generated files]
  Board_Meeting_[Date]_Summary.md
```

---

## Success Criteria

A successful board packet:
- Generated in <15 minutes
- Requires no manual cleanup
- Passes design-director quality gates
- Board members find information in <30 seconds
- Recording secretary uses without confusion
- Action items flow to Asana automatically

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0.0 | Nov 2025 | Managed skill with multi-format outputs, design-director integration, HTML dashboards |
| 1.0 | Nov 2025 | Initial user-skill with 5 core DOCX documents |

---

## Support

For issues or feedback:
- Check SKILL.md for detailed operational specifications
- Review references/ for document-specific logic
- Contact 360 Social Impact Studios

---

*Built for 360 Social Impact Studios*
*Skill version 2.0.0 | November 2025*