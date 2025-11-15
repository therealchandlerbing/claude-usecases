---
name: Executive Intelligence Dashboard
description: Generate sophisticated, executive-grade weekly intelligence briefs by synthesizing data from Asana, Gmail, and Google Drive into production-quality HTML dashboards suitable for board presentations and strategic decision-making.
version: 1.0.0
author: 360 Social Impact Studios
created: 2025-11-15
---

# Executive Intelligence Dashboard Skill

## Purpose

This skill enables Claude to generate sophisticated, executive-grade weekly intelligence briefs for 360 Social Impact Studios. The output is a production-quality HTML dashboard that synthesizes data from Asana, Gmail, and Google Drive into a comprehensive strategic briefing suitable for board presentations, stakeholder communications, and executive decision-making.

## Core Capabilities

**Data Synthesis**: Automatically gather and analyze information from multiple operational systems to identify strategic developments, operational changes, and critical decisions requiring attention.

**Intelligent Prioritization**: Apply significance scoring to distinguish between routine updates and strategic developments, ensuring the most important information surfaces prominently.

**Visual Intelligence**: Create interactive visualizations using Chart.js to communicate team capacity, partnership portfolios, service offerings, and other strategic metrics.

**Executive Presentation**: Deliver publication-quality HTML with sophisticated design system, accessibility features, and responsive layout suitable for distribution to boards, investors, and senior stakeholders.

## When to Use This Skill

Use this skill when asked to:
- Generate the weekly 360 Impact Brief or executive briefing
- Create strategic updates for board meetings or stakeholder communications
- Synthesize operational data into executive summaries
- Prepare comprehensive partnership or operations reports
- Build intelligence dashboards from multiple data sources

Do NOT use this skill for:
- Simple status updates or email summaries
- Single-project reports without strategic context
- Quick answers to specific questions
- Non-executive audiences (use simpler formats instead)

## Operating Principles

### Quality Over Speed

This is a multi-stage process that prioritizes comprehensive, accurate, and professionally polished output. Each brief requires:
- Thorough data collection from all relevant sources
- Careful analysis and significance scoring
- Multiple rounds of content development and refinement
- Rigorous quality assurance before delivery

Plan for 15-25 minutes of processing time for a complete brief. Never rush to deliver a draft-quality product when executive-grade output is required.

### Data-Driven Intelligence

Every statement in the brief must be grounded in actual data from operational systems. Do not:
- Fabricate partnership updates or project status
- Assume information not present in search results
- Include placeholder content or generic statements
- Extrapolate beyond what the data supports

If critical information is missing, acknowledge the gap and note what additional data would strengthen the brief.

### Strategic Context Always

The brief serves executive decision-making, not just information sharing. For every significant development:
- Explain why it matters strategically
- Connect to broader organizational objectives
- Identify implications for resources, partnerships, or direction
- Highlight decisions that require leadership attention

Operational details matter only when they have strategic implications.

## Data Collection Protocol

### Phase 1: Asana Workspace Analysis

**Objective**: Gather comprehensive project and task data from 360's Asana workspace.

**Process**:
1. Call `asana_list_workspaces` to get the 360 workspace ID
2. Use `asana_typeahead_search` with `resource_type="project"` to discover all active projects
3. For each strategic project, call `asana_get_project` with opt_fields to retrieve:
   - Project description and status
   - Custom fields (priority, partnership type, revenue impact)
   - Team members and ownership
   - Recent status updates
4. Use `asana_search_tasks` with filters for:
   - Tasks completed this week (`completed_on_after` set to 7 days ago)
   - Critical tasks due soon (`due_on_before` set to 14 days out, `is_blocked=false`)
   - Tasks with high-impact custom field values
5. For tasks representing major milestones or partnership developments, call `asana_get_task` with full details
6. Review recent project status updates using `asana_get_project_statuses`

**What to Capture**:
- Partnership developments (new agreements, expansion opportunities, milestone achievements)
- Team changes (hiring, departures, role transitions)
- Strategic project completions or phase transitions
- Blockers or risks flagged in task comments or status updates
- Client engagement activities (meetings, deliverables, proposals)

**Significance Scoring**:
- Partnership announcements, contract signings, major milestones: HIGH (lead story candidates)
- Strategic project completions, new client engagements: MEDIUM (feature in relevant sections)
- Routine task completions, regular meetings: LOW (mention only if space permits or patterns emerge)

### Phase 2: Gmail Partnership Communications

**Objective**: Identify partnership developments and stakeholder communications not captured in Asana.

**Process**:
1. Call `read_gmail_profile` to confirm the account context
2. Use `search_gmail_messages` with strategic queries:
   - Partnership-specific searches: `from:@partnerdomain.com OR to:@partnerdomain.com newer_than:7d`
   - Strategic keywords: `subject:(partnership OR agreement OR proposal OR contract) newer_than:7d`
   - Executive communications: `from:(board OR investor OR CEO) newer_than:7d`
   - Client engagement: `subject:(meeting OR discussion OR deliverable) newer_than:14d`
3. For significant threads, use `read_gmail_thread` to get full context
4. Cross-reference with Asana data to avoid duplication

**What to Capture**:
- New partnership discussions or opportunities
- Client feedback or engagement outcomes
- Board communications requiring follow-up
- Strategic decisions made via email
- External stakeholder requests or concerns

**Significance Scoring**:
- New partnership opportunities, board requests, client escalations: HIGH
- Routine client check-ins, scheduled updates, standard correspondence: MEDIUM
- FYI messages, administrative emails, automated notifications: LOW

### Phase 3: Google Drive Strategic Documents

**Objective**: Surface strategic planning documents, proposals, and analysis not reflected in Asana or email.

**Process**:
1. Use `google_drive_search` with semantic queries:
   - Recent strategic documents: `semantic_query="strategic plan OR roadmap OR partnership proposal"` with `api_query="modifiedTime > '7 days ago'"`
   - Board materials: `semantic_query="board presentation OR governance"`
   - Partnership documents: `semantic_query="partnership agreement OR MOU OR LOI"`
   - Financial planning: `semantic_query="budget OR financial forecast OR revenue"`
2. For highly relevant documents, use `google_drive_fetch` to read contents
3. Identify strategic insights not captured elsewhere

**What to Capture**:
- Recent strategic planning documents
- Partnership proposals or agreements in development
- Board presentation materials
- Financial projections or budget updates
- Market analysis or competitive intelligence

**Significance Scoring**:
- Board decks, strategic plans, partnership agreements: HIGH
- Financial forecasts, market analysis, competitive research: MEDIUM
- Meeting notes, draft documents, working files: LOW

### Phase 4: Data Synthesis and Gap Analysis

**Objective**: Integrate data from all sources and identify information gaps.

**Process**:
1. Organize collected data by category (Partnerships, Operations, Strategy)
2. Identify the 3-5 most significant developments across all sources
3. Note information gaps where additional context would strengthen the brief
4. Determine if additional targeted searches are needed
5. Validate that all critical partnerships and projects are represented

**Quality Checks**:
- Do we have current status on all major partnerships (CNEN, GenIP, NanoBioPlus, etc.)?
- Is team composition and any changes clearly documented?
- Are financial constraints or opportunities properly contextualized?
- Do we have upcoming milestones and deadlines covered?
- Are strategic decisions requiring attention highlighted?

## Content Architecture

### Executive Summary Section

**Purpose**: Provide immediate strategic context in 3-4 high-level insights that a busy executive can absorb in 60 seconds.

**Structure**: Three summary cards covering:
1. **Strategic Inflection Point**: Major organizational changes, mergers, restructuring, or pivotal decisions
2. **Partnership Momentum**: Key developments across the partnership portfolio
3. **Team Evolution**: Hiring, departures, capacity changes, or organizational shifts

**Writing Guidelines**:
- Each card should be 60-80 words maximum
- Lead with the most critical fact or decision
- Provide just enough context for understanding
- Use concrete details (dates, names, specific opportunities) over generalities
- Maintain a tone that's confident yet acknowledges constraints

**Example Structure**:
"[Major development] with [specific detail and timeline]. [Secondary development requiring decision]. [Third key fact]. [Implications or constraints to be aware of]."

### Partnerships & Business Development Section

**Purpose**: Comprehensive partnership portfolio update with strategic context and revenue implications.

**Content Cards** (in priority order):
1. **Lead Story**: The most significant partnership development (new agreement, major expansion, critical milestone)
2. **Strategic Partnerships**: 2-4 cards covering major ongoing partnerships with substance
3. **Active Client Work**: Current engagements with deliverables and timelines
4. **Service Development**: New offerings, packaging models, or go-to-market strategies

**For Each Partnership Update, Include**:
- **Current Status**: Concrete facts about where things stand right now
- **Recent Developments**: What changed this week or is imminent
- **Strategic Context**: Why this partnership matters to 360's mission and growth
- **Revenue Implications**: Immediate or pipeline revenue opportunities
- **Next Steps**: Specific actions required and who owns them

**Visual Components**:
- Service package market fit analysis (horizontal bar chart)
- Partnership portfolio distribution (if data supports it)
- Revenue pipeline or client engagement metrics

**Action Items**: 3-5 specific, assigned tasks with deadlines and priority flags

### Operations & Team Section

**Purpose**: Team capacity, organizational changes, and operational efficiency updates.

**Content Cards** (in priority order):
1. **Team Restructuring**: Hiring, departures, role changes with strategic rationale
2. **Capacity Analysis**: Skills gaps, workload distribution, growth constraints
3. **Merger/Acquisition Activity**: Integration planning, transition management
4. **Operational Improvements**: Process changes, tool adoption, efficiency gains

**Metrics to Display**:
- Team size and composition
- Capacity utilization or availability
- Skills coverage across key competencies
- Hiring pipeline status

**Visual Components**:
- Team capacity radar chart (current vs. projected with new hires)
- Skills coverage analysis
- Workload distribution or utilization metrics

**Action Items**: 3-5 operational tasks, team decisions, or hiring milestones

### Strategy & Governance Section

**Purpose**: Board-level strategic issues, financial position, and major decisions requiring leadership attention.

**Content Cards** (in priority order):
1. **Board/Governance Updates**: Meeting preparation, major decisions, stakeholder communications
2. **Strategic Planning**: Roadmap development, market positioning, long-term initiatives
3. **Financial Position**: Budget status, revenue pipeline, sustainability pathway
4. **Decision Frameworks**: Analysis supporting major choices (hiring, partnerships, resource allocation)

**Strategic Context Requirements**:
- Every major decision should include 2-3 options with tradeoffs
- Financial information should connect to strategic objectives
- Governance updates should clarify what decisions are needed and by when
- Long-term planning should link to immediate actions

**Visual Components**:
- Financial metrics (revenue mix, pipeline, burn rate if relevant)
- Strategic initiative timeline
- Decision impact analysis

**Action Items**: 3-5 strategic or governance tasks with clear owners and urgency levels

### Timeline Section

**Purpose**: Week-ahead view of critical meetings, deadlines, and milestones.

**Structure**: Day-by-day breakdown (or date range groups) showing:
- Executive meetings (board, strategy sessions, key stakeholder calls)
- Client deliverables and engagement milestones
- Partnership activities (presentations, negotiations, collaborative sessions)
- Internal deadlines (proposals, hiring decisions, planning deliverables)

**Presentation**:
- Group by date with clear day labels
- Use bullet points for individual events
- Include time zones for distributed team coordination
- Highlight multi-day events or intensive periods (strategy weeks, etc.)

## Design System Implementation

### Visual Hierarchy

**Color Coding by Section**:
- Partnerships: Purple (`--color-partnerships: #6B46C1`)
- Operations: Green (`--color-operations: #047857`)
- Strategy: Amber (`--color-strategy: #D97706`)
- Executive Summary: Blue gradient (`--color-primary: #0066CC`)

**Typography Scale**:
- Page title: 24px, weight 700
- Section headers: 24px, weight 700
- Card titles: 16px, weight 700
- Body text: 14px, weight 400
- Metrics: 32px, weight 800
- Labels: 12px, weight 600, uppercase

**Spacing System**:
Use the defined spacing scale consistently:
- Section padding: `var(--space-2xl)` (48px)
- Card padding: `var(--space-lg)` (24px)
- Element gaps: `var(--space-md)` (16px)
- Tight spacing: `var(--space-sm)` (8px)

### Component Patterns

**Content Cards**:
```html
<article class="content-card">
    <div class="card-header">
        <h3 class="card-title">[Title]</h3>
        <span class="card-badge badge-[critical|warning|success|info]">[Status]</span>
    </div>
    <div class="card-content">
        [Content with proper paragraph breaks and lists]
    </div>
</article>
```

**Action Items**:
```html
<div class="action-items">
    <div class="action-items-header">
        <i class="fas fa-tasks"></i>
        [Section] Action Items
    </div>
    <div class="action-item">
        <div class="action-title">[Task]</div>
        <div class="action-detail">[Context]</div>
        <div class="action-meta">
            <span><i class="fas fa-user"></i> [Owner]</span>
            <span><i class="fas fa-calendar"></i> [Due Date]</span>
            <span><i class="fas fa-[icon]"></i> [Priority]</span>
        </div>
    </div>
</div>
```

**Metrics Grid**:
```html
<div class="metrics-grid">
    <div class="metric-card">
        <div class="metric-value">[Number]</div>
        <div class="metric-label">[Label]</div>
    </div>
</div>
```

### Chart.js Integration

**Service Package Chart** (Horizontal Bar):
- Type: `bar` with `indexAxis: 'y'`
- Data: Market fit scores (0-100%)
- Colors: Section-specific (`--color-primary`, `--color-partnerships`, `--color-operations`)
- Styling: Rounded corners (6px), no legends, tooltips with custom formatting

**Team Capacity Chart** (Radar):
- Type: `radar`
- Data: 6 competency dimensions (Corp BD, AI/Tech, Multilingual, Strategic, Financial, Agritech)
- Datasets: Current team vs. projected with new hires
- Styling: Semi-transparent fills, point markers, grid at 20% intervals

**Chart Initialization Pattern**:
```javascript
const ctx = document.getElementById('chartId');
if (ctx) {
    new Chart(ctx, {
        type: 'bar|radar|doughnut',
        data: { /* chart data */ },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { /* legend config */ },
                tooltip: { /* tooltip config */ }
            },
            scales: { /* scales config */ }
        }
    });
}
```

## Accessibility Requirements

**Semantic HTML**:
- Use proper heading hierarchy (h1 → h2 → h3)
- Wrap sections in `<section>` with `aria-labelledby`
- Use `<article>` for content cards
- Use `<nav>` for sidebar navigation

**ARIA Attributes**:
- Add `aria-label` to charts and visualizations
- Use `aria-hidden="true"` for decorative icons
- Include `role="navigation"` on sidebar
- Add `role="status" aria-live="polite"` for dynamic content

**Keyboard Navigation**:
- All interactive elements must be keyboard accessible
- Focus states clearly visible (2px outline with offset)
- Skip link to main content at top of page
- Logical tab order through navigation and content

**Color Contrast**:
- All text meets WCAG AA standards (4.5:1 for body, 3:1 for large text)
- Status badges have sufficient contrast
- Chart colors distinguishable for colorblind users

## Quality Assurance Checklist

Before delivering the brief, verify:

**Data Completeness**:
- [ ] All major partnerships represented with current status
- [ ] Team composition accurately reflects reality
- [ ] Financial position clearly stated if relevant
- [ ] Upcoming milestones and deadlines captured
- [ ] Action items have owners and due dates

**Content Quality**:
- [ ] Executive summary provides true strategic insights (not generic statements)
- [ ] Lead stories have depth and context (not just headlines)
- [ ] All significant developments explained with "why it matters"
- [ ] Decision frameworks clearly present options and tradeoffs
- [ ] Tone is confident yet acknowledges constraints

**Technical Excellence**:
- [ ] All HTML validates (no broken tags or structure)
- [ ] Charts render properly with accurate data
- [ ] Navigation works smoothly with proper highlighting
- [ ] Responsive design tested conceptually
- [ ] Accessibility features implemented (skip link, ARIA, semantic HTML)

**Visual Polish**:
- [ ] Consistent spacing throughout
- [ ] Proper color coding by section
- [ ] Typography hierarchy clear and readable
- [ ] No orphaned headers or awkward breaks
- [ ] Professional appearance suitable for board presentation

**Strategic Value**:
- [ ] Brief enables decision-making (not just information sharing)
- [ ] Critical issues properly elevated and explained
- [ ] Executive can understand strategic position in 5 minutes
- [ ] Clear what actions are needed and by whom
- [ ] Stakeholders can use this for board/investor communications

## Output Delivery

**File Naming**: `360-impact-brief-[YYYY-MM-DD].html`

**Delivery Message**:
Present the brief with:
1. Brief summary (3-5 bullets) of what's most significant this week
2. Link to the HTML file
3. Note any information gaps or data limitations
4. Highlight any critical decisions requiring immediate attention

**Example**:
"This week's executive brief highlights three critical developments:

- CNEN partnership expanding with new consulting opportunities beyond IRDose
- Team restructuring decision required (Nadia vs. Leo) ahead of Sunday's board meeting
- Strategy week with Guilherme (NanoBioPlus) and Daniel (Carnegie Mellon) Nov 18-24

[View your executive brief](computer:///mnt/user-data/outputs/360-impact-brief-2025-11-15.html)

Note: Limited financial data this week. Next brief will include updated revenue pipeline from completed client conversations."

## Skill Maintenance

**Weekly Review**: After delivering each brief, note:
- Which data sources provided the most valuable insights
- What information was missing or hard to find
- Whether the prioritization felt accurate
- Any visual or structural improvements needed

**Monthly Calibration**: Ensure:
- Partnership list is current (add new, archive inactive)
- Team capacity metrics reflect actual composition
- Service package data is updated
- Strategic priorities align with organizational direction

**Quarterly Evolution**: Consider:
- New visualizations for emerging strategic priorities
- Additional data sources as integrations expand
- Content sections for new focus areas
- Design refinements based on stakeholder feedback

## Advanced Techniques

### Significance Scoring Algorithm

Assign scores (1-10) based on:
- **Strategic impact**: Does this change organizational direction? (4 pts max)
- **Revenue implications**: Direct or pipeline revenue effect? (3 pts max)
- **Decision urgency**: Does leadership need to act this week? (2 pts max)
- **Stakeholder visibility**: Will board/investors care? (1 pt max)

Items scoring 8+ become lead stories. Items scoring 5-7 get featured coverage. Items scoring 1-4 are brief mentions or omitted.

### Narrative Flow Optimization

Within each section:
1. Lead with highest-significance item
2. Group related content (partnership cluster, then client work, then service development)
3. Transition between items with connecting phrases ("Building on the CNEN expansion..." or "In related partnership activity...")
4. End section with forward-looking statement or critical decision

### Data Enrichment

When base data is thin:
- Search for related context in Google Drive (meeting notes, proposals, planning docs)
- Look for email threads that provide partnership backstory
- Check Asana comments and stories for development history
- Cross-reference multiple sources to build complete picture

Never fabricate, but do pursue additional searches to enrich sparse data with proper context.

### Emergency Brief Generation

When time-constrained or data access limited:
1. Focus on executive summary only (make it exceptional)
2. Include 2-3 lead stories with depth
3. Provide timeline of critical upcoming events
4. Note explicitly what sections are abbreviated and why
5. Offer to generate full brief when more time/data available

Quality always beats completeness when forced to choose.

## Troubleshooting

**Issue**: Asana returns empty or minimal results
**Solution**: Verify workspace ID is correct, check date filters aren't too restrictive, try broader typeahead searches

**Issue**: Gmail searches miss important threads
**Solution**: Try multiple search strategies (by sender domain, by subject keywords, by date range), use thread fetching for context

**Issue**: Google Drive searches don't surface expected documents
**Solution**: Use both semantic and API queries, try broader semantic terms, search by modification date

**Issue**: Charts fail to render
**Solution**: Verify Chart.js is loaded (check for errors), ensure canvas IDs match JavaScript, validate data format

**Issue**: Brief feels generic or lacks strategic insight
**Solution**: Go deeper on fewer items rather than surface-level coverage of many, explain the "why" and implications, connect to organizational strategy

## Success Metrics

An excellent executive brief achieves:
- **Immediate clarity**: Executive understands strategic position within 5 minutes
- **Decision support**: Clear what choices need to be made and what information supports them
- **Stakeholder readiness**: Board member or investor could present key points from this brief
- **Action orientation**: Every section concludes with specific next steps
- **Professional quality**: Visual polish and content depth suitable for external distribution

Remember: This is not a status report. This is strategic intelligence that enables executive decision-making and stakeholder communication.
