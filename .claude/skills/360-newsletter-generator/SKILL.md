---
name: 360 Newsletter Generator
description: Generate publication-style newsletters and executive briefs for 360 Social Impact Studios by synthesizing updates from Asana, Gmail, and Google Drive into professionally designed, interactive HTML dashboards with data visualizations. Supports both confidential executive briefs and public-facing newsletters.
version: 1.0.0
author: 360 Social Impact Studios
created: 2024-10-15
updated: 2025-11-22
category: executive-communication
complexity: high
tags: [newsletter, executive-brief, dashboard, asana-integration, gmail-integration, drive-integration, data-visualization, chart-js]
dependencies:
  - Asana API (project and task data)
  - Gmail API (communications and updates)
  - Google Drive API (documents and reports)
  - Chart.js (interactive visualizations)
outputs:
  - Interactive HTML newsletter dashboard
  - Executive brief HTML (confidential)
  - Print-friendly PDF export
---

# 360 Newsletter Generator

## Purpose

Automatically generate sophisticated, publication-style newsletters and executive briefs by aggregating data from Asana, Gmail, and Google Drive and presenting strategic updates in a dense but readable format inspired by British newspaper design, with interactive Chart.js visualizations showing trends and metrics.

**Output Quality Standard:** Executive dashboard aesthetic with professional design, interactive components, and print-ready formatting.

---

## When to Use This Skill

### Trigger Phrases

**For Executive Brief (Confidential):**
- "Generate executive brief" or "create executive brief"
- "Create board update" or "prep investor update"
- "Weekly leadership brief" or "confidential update"
- "Executive intelligence dashboard"

**For General Newsletter (Public/Stakeholder):**
- "Generate newsletter" or "create newsletter"
- "Weekly digest", "monthly update", or "company summary"
- "What happened this week/month"

### When NOT to Use

- Real-time dashboards (this is retrospective summary generation)
- Email marketing campaigns (use email marketing tools)
- Press releases (different format and tone)
- Social media content (use 360-content-converter)

---

## Two Output Formats

### 1. 360 Executive Brief (Primary Use Case)

**Audience:** Leadership team, board members, investors
**Content:** Confidential intelligence, financial data, HR updates, strategic decisions
**Sensitivity:** Executive-level confidential information
**Template:** `executive-brief-template.html`

### 2. 360 Newsletter (Secondary Use Case)

**Audience:** General stakeholders, partners, public-facing
**Content:** High-level updates, shareable insights, impact stories
**Sensitivity:** Public or stakeholder-appropriate information
**Template:** `newsletter-template.html`

**Key Difference:** Both use identical professional dashboard design, navigation structure, and interactive components. The distinction is purely content-based.

---

## Core Capabilities

### 1. Multi-Source Data Integration

**Asana Integration (70% weight)**
- Project progress and task velocity
- Milestone tracking
- Completion metrics
- Workstream status

**Gmail Integration (20% weight)**
- Partnership communications
- Client interactions
- Strategic announcements
- Impact feedback

**Google Drive Integration (10% weight)**
- Reports and deliverables
- Impact documentation
- Strategic documents

### 2. Professional Newsletter Design

- Modern executive dashboard aesthetic
- Fixed sidebar navigation
- Color-coded sections (partnerships blue, operations green, strategy orange)
- Interactive Chart.js visualizations
- Print-friendly PDF export
- Mobile-responsive layout

### 3. Content Analysis & Prioritization

- Automatic significance scoring (0-100 scale)
- Lead story selection based on strategic importance
- Section assignment by content type
- Action item flagging and tracking

### 4. Quality Assurance

- Data integrity verification
- Content completeness checks
- Design and formatting validation
- Tone and voice consistency

---

## Newsletter Structure

### Sections

1. **Executive Summary**
   - Gradient blue banner
   - 3-4 key highlight cards
   - Most critical information at a glance

2. **Partnerships & Ecosystem**
   - Partnership pipeline status
   - New agreements or renewals
   - Relationship health indicators
   - Cross-border developments

3. **Programs & Innovation**
   - Active project updates
   - Technology assessments completed
   - Client deliverables
   - Methodology applications

4. **Impact & Outcomes**
   - Social impact metrics
   - Community outcomes
   - Systems change indicators
   - Testimonials and feedback

5. **Operations & Capacity**
   - Team updates and hiring
   - Infrastructure improvements
   - Financial sustainability
   - System implementations

6. **Strategic Horizon**
   - Upcoming meetings and events
   - Decision deadlines
   - Strategic initiatives launching
   - Board priorities

### Visual Components

**Charts (minimum 4 per newsletter):**
- Partnership pipeline by stage (bar chart)
- Project distribution by region (pie chart)
- Impact metrics trend (line chart)
- Revenue/sustainability trajectory (line chart)

**Metric Cards:**
- Partnership value/count
- Active projects
- Social impact numbers
- Team capacity
- Financial runway

**Status Badges:**
- CRITICAL: Urgent action needed (red border)
- ACTION REQUIRED: Response needed (yellow border)
- MONITORING: Watching closely (gray border)

---

## 6-Phase Generation Workflow

### Phase 1: Define Scope

**Ask clarifying questions:**
- Newsletter type (Executive Brief vs. General Newsletter)?
- Date range (last week, last month, custom)?
- Special focus areas (partnerships, operations, strategy)?
- Target audience (board, investors, stakeholders)?
- Output format preference (HTML dashboard, PDF, both)?

**Default settings:**
- Type: Executive Brief (confidential)
- Range: Previous 7 days (Monday to Sunday)
- Focus: Balanced across all sections
- Audience: Leadership team
- Format: Interactive HTML dashboard

### Phase 2: Connect to Data Sources

**Asana Workspace:**
1. Use `asana_list_workspaces` to get workspace gid
2. Expected workspace: 360socialventures.com (gid: 1210382795871981)
3. Confirm connection successful

**Gmail Profile:**
1. Use `read_gmail_profile` to get user email
2. Confirm access to Gmail search

**Google Drive:**
1. Verify `google_drive_search` access
2. Test with simple query

**Calculate dates:**
- Start date: [YYYY-MM-DD]
- End date: [YYYY-MM-DD]
- RFC3339 format for tools: YYYY-MM-DDTHH:MM:SSZ

### Phase 3: Collect Data

**Asana Data Collection:**
- Scan priority projects (Weekly Meeting Tracker, Partnership Development, Client Engagements, SpacePlan, GenIP, CNEN)
- Get project details with custom fields
- Get project sections
- Search completed tasks (with date filter)
- Search modified/active tasks
- Get project task counts

**Gmail Data Collection:**
- Partnership communications from key domains
- Sent strategic emails (agreements, proposals, contracts)
- Impact/client feedback (testimonials, outcomes)
- Board-related correspondence

**Google Drive Data Collection:**
- Strategic documents modified in period
- Partner-specific documents
- Impact metrics documentation
- Financial and budget documents

### Phase 4: Analyze & Score Content

**Significance Scoring (0-100):**
- Strategic importance (40 points)
- Stakeholder impact (30 points)
- Urgency/timeliness (20 points)
- Completeness of information (10 points)

**Lead Story Selection:**
- Highest significance score
- Passes completeness threshold
- Has actionable context

**Section Assignment:**
- Partnerships: Partnership-related items
- Programs: Project/client work
- Impact: Outcomes and metrics
- Operations: Team/infrastructure
- Strategy: Board/investor items

### Phase 5: Generate HTML Dashboard

**Template Selection:**
- Executive Brief: `executive-brief-template.html`
- General Newsletter: `newsletter-template.html`

**Content Insertion:**
- Executive summary cards (top 3-4 items)
- Section-specific content (organized by type)
- Charts with data from analysis
- Metric cards with current values
- Action items and deadlines

**Interactive Components:**
- Chart.js visualizations (bar, pie, line charts)
- Expandable sections
- Fixed sidebar navigation
- Print-friendly CSS

### Phase 6: Quality Assurance & Delivery

**Quality Checks:**
- Data integrity verification (all sources represented)
- Content completeness (all sections populated)
- Design validation (responsive, accessible)
- Tone consistency (executive voice)

**Deliverables:**
- Interactive HTML file (self-contained)
- Optional PDF export
- Content governance compliance report

**Time estimate:** 60-90 seconds total

---

## Data Collection Protocol Details

### Asana Priority Projects

- Weekly Meeting Tracker
- Partnership Development
- Client Engagements
- SpacePlan Joint Venture
- GenIP Integration
- CNEN Partnership
- Any project with "Board" in name

### Gmail Search Patterns

1. Partnership communications from key domains
2. Sent strategic emails (agreements, proposals, contracts)
3. Impact/client feedback (testimonials, outcomes)
4. Board-related correspondence

### Google Drive Search Patterns

1. Strategic documents modified in period
2. Partner-specific documents
3. Impact metrics documentation
4. Financial and budget documents

---

## Context: 360 Social Impact Studios

**Organization Overview:**
- 501(c)(3) nonprofit innovation consultancy
- Global operations: Seattle (HQ), São Paulo Brazil, international partnerships
- Focus areas: Innovation consulting, technology transfer, social impact ventures
- Cross-border market expansion (US-Brazil corridor emphasis)

**Key Partnerships Monitored:**
- SpacePlan (360 Space Innovation Studios joint venture)
- GenIP (Invention Evaluator integration)
- ScienceLink (technology transfer)
- NanoBioPlus (biomaterials platforms)
- CNEN (National Nuclear Energy Commission, Brazil)
- Carnegie Mellon, Life Science Washington, various universities

**Strategic Focus Areas:**
- Partnership development and ecosystem building
- Innovation portfolio assessment and validation
- International business development (especially Brazil)
- Social impact measurement and systems change
- Technology commercialization and transfer

---

## Supporting Files

**Core Documentation:**
- `README.md` - Overview and quick start
- `INDEX.md` - File navigation
- This file: `SKILL.md` - Complete operational specification

**References:**
- `references/chart-specifications.md` - Chart.js configuration
- `references/content-analysis-framework.md` - Scoring methodology
- `references/data-collection-guide.md` - API integration details
- `references/troubleshooting-guide.md` - Common issues
- `references/workflow-examples.md` - Real usage scenarios
- `references/writing-style-guide.md` - Tone and voice guidelines

**Templates:**
- `templates/executive-brief-template.html` - Confidential dashboard
- `templates/newsletter-template.html` - Public-facing format
- `templates/data-sources.json` - Data source configuration

**Executive Brief Docs:**
- `executive-brief-docs/360-impact-brief-weekly-template.md` - Content template
- `executive-brief-docs/SKILL.md` - Weekly production workflow
- `executive-brief-docs/DOCUMENTATION-INDEX.md` - Navigation guide

---

## Troubleshooting

**"Can't connect to Asana/Gmail/Drive"**
→ Verify API integrations are configured
→ Check authentication tokens are valid
→ Confirm workspace/account access

**"Newsletter feels too dense"**
→ Adjust content threshold (reduce items included)
→ Use executive brief format (more concise)
→ Focus on specific sections only

**"Charts not rendering"**
→ Verify Chart.js library loaded
→ Check data format matches chart type
→ Review browser console for errors

**"Content sensitivity concerns"**
→ Use General Newsletter template for public content
→ Review content governance rules
→ Mark sensitive items as Executive Brief only

---

## Version History

- **v1.0.0** (2025-11-22) - Created root-level SKILL.md for validation compliance
  - Comprehensive operational specification
  - 6-phase generation workflow
  - Data collection protocol documented
  - Supporting files catalog

---

**Ready to generate professional newsletters and executive briefs! 📰**
