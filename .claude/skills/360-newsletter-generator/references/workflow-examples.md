# Workflow Examples

Step-by-step walkthroughs of complete newsletter generation workflows.

## Example 1: Standard Weekly Newsletter

### User Request
```
Generate newsletter for last week
```

### Step 1: Confirmation & Setup (5 seconds)

**Claude Response:**
```
Generating 360 Newsletter for November 4-10, 2025.
Collecting data from Asana, Gmail, and Google Drive...
```

**Internal Planning:**
- Date range: 2025-11-04 to 2025-11-10
- Scope: All priority areas
- Data sources: Asana (70%), Gmail (20%), Drive (10%)
- Output: Full interactive newsletter with charts

### Step 2: Data Collection (30-40 seconds)

**Asana Collection (15-20 seconds, 5-6 API calls):**

```javascript
// Call 1: Get workspace
asana_list_workspaces()
→ workspace_gid: 1210382795871981

// Call 2: Find Partnership Development project
asana_typeahead_search(
  workspace_gid: "1210382795871981",
  resource_type: "project",
  query: "Partnership"
)
→ project_gid: 1234567890

// Call 3: Get project details
asana_get_project(
  project_id: "1234567890",
  opt_fields: "name,custom_fields,current_status"
)
→ Project details including custom field definitions

// Call 4: Get completed tasks in period
asana_search_tasks(
  workspace: "1210382795871981",
  projects_any: "1234567890",
  completed: true,
  completed_on_after: "2025-11-04",
  completed_on_before: "2025-11-10"
)
→ 12 completed tasks

// Call 5: Get modified/active tasks
asana_search_tasks(
  workspace: "1210382795871981",
  projects_any: "1234567890",
  modified_on_after: "2025-11-04",
  completed: false
)
→ 23 active tasks

// Call 6: Get task counts for project health
asana_get_project_task_counts(
  project_id: "1234567890"
)
→ Total: 45, Complete: 28, Incomplete: 17

// Repeat calls 2-6 for other priority projects
// (SpacePlan, GenIP, CNEN, Operations, etc.)
```

**Gmail Collection (8-12 seconds, 3-4 API calls):**

```javascript
// Call 1: Partnership communications
search_gmail_messages(
  q: "from:(*@spaceplan.com OR *@genip.com OR *@sciencelink.org OR
      *@nanobioplus.com OR *@cnen.gov.br) after:2025/11/04 before:2025/11/11"
)
→ 8 threads found

// Call 2: Read high-priority thread
read_gmail_thread(thread_id: "abc123xyz")
→ Full thread content about SpacePlan MOU

// Call 3: Sent strategic emails
search_gmail_messages(
  q: "from:me (partnership OR agreement OR MOU) after:2025/11/04"
)
→ 3 sent emails

// Call 4: Impact/testimonials
search_gmail_messages(
  q: "(testimonial OR feedback OR impact) after:2025/11/04"
)
→ 2 feedback emails
```

**Google Drive Collection (6-8 seconds, 2-3 API calls):**

```javascript
// Call 1: Recent strategic documents
google_drive_search(
  api_query: "modifiedTime > '2025-11-04T00:00:00Z' and
              (name contains 'partnership' or name contains 'deliverable')",
  semantic_query: "partnership agreements deliverables reports",
  order_by: "modifiedTime desc",
  page_size: 20
)
→ 6 documents found

// Call 2: SpacePlan-specific documents
google_drive_search(
  api_query: "modifiedTime > '2025-11-04T00:00:00Z' and
              fullText contains 'SpacePlan'",
  semantic_query: "SpacePlan partnership joint venture"
)
→ 3 documents found

// Call 3: Fetch high-priority document
google_drive_fetch(
  document_ids: ["doc_id_1", "doc_id_2"]
)
→ Content from SpacePlan MOU and financial report
```

### Step 3: Content Analysis & Scoring (10 seconds)

**Content Inventory:**
- Asana: 23 completed tasks, 45 active tasks across 6 projects
- Gmail: 8 partner communications, 3 strategic sent emails, 2 testimonials
- Drive: 6 strategic documents, key MOU text extracted

**Scoring Process:**

| Item | Source | Base | Mods | Final | Section |
|------|--------|------|------|-------|---------|
| SpacePlan MOU signed | Gmail + Drive | 95 | +10 int'l, +15 revenue | 100 | Partnership (LEAD) |
| GenIP integration complete | Asana | 85 | +10 strategic | 95 | Partnership |
| Brazil team onboarding | Asana | 70 | +10 int'l, +10 capacity | 90 | Operations |
| CNEN quarterly report | Drive | 80 | +10 stakeholder | 90 | Partnership |
| Service package design | Asana | 75 | +10 strategic | 85 | Strategy |
| UW consulting debrief | Asana | 65 | +10 stakeholder | 75 | Operations |
| Board meeting prep | Asana | 70 | - | 70 | Strategy |
| Limus case study progress | Asana | 60 | - | 60 | Programs |
| Weekly team meeting | Asana | 40 | -20 routine | 20 | (Omit) |

**Lead Story Selection:**
- Highest score: SpacePlan MOU (100)
- Validates significance: Partnership agreement formalized
- Strategic implication: Revenue model pivot
- Multiple stakeholders: Board, team, partners

**Section Assignment:**
- **Partnerships:** SpacePlan MOU (100), GenIP (95), CNEN (90) = 3 stories
- **Operations:** Brazil team (90), UW debrief (75) = 2 stories
- **Strategy:** Service package (85), Board prep (70) = 2 stories
- **Programs:** Limus case study (60) = 1 story
- **Impact:** (No high-scoring items this period)

### Step 4: Chart Data Preparation (5 seconds)

**Chart 1: Partnership Portfolio Distribution (Doughnut)**
```javascript
{
  labels: ['Nuclear Tech', 'Biomaterials', 'Innovation Services',
           'Space/Arch', 'Healthcare', 'Investment DD'],
  data: [2, 2, 5, 2, 1, 1]  // Count from Asana project categorization
}
```

**Chart 2: Project Distribution by Region (Pie)**
```javascript
{
  labels: ['North America', 'Latin America', 'Europe', 'Other'],
  data: [45, 35, 15, 5]  // Percentage from task geographic keywords
}
```

**Chart 3: Task Completion Velocity (Line)**
```javascript
{
  labels: ['Week -3', 'Week -2', 'Week -1', 'Current'],
  data: [18, 22, 19, 23]  // Completed tasks per week
}
```

**Chart 4: Team Capacity Assessment (Radar)**
```javascript
{
  labels: ['Corp BD', 'AI/Tech', 'Multilingual', 'Strategic', 'Financial', 'Agritech'],
  datasets: [
    { label: 'Current', data: [50, 75, 60, 70, 50, 30] },
    { label: 'With Hires', data: [90, 85, 95, 90, 90, 85] }
  ]
}
```

### Step 5: HTML Generation (10 seconds)

**Structure:**
1. Executive Summary (3 highlight cards)
2. Lead Story (SpacePlan MOU)
3. Partnerships Section (3 cards + pipeline chart)
4. Operations Section (2 cards + capacity chart)
5. Strategy Section (2 cards + service fit chart)
6. Programs Section (1 card)
7. Timeline (upcoming week events)
8. Action Items (4 flagged items)

**Key Components Generated:**
- Sidebar navigation with 8 sections
- Executive summary with SpacePlan, Brazil team, Service package highlights
- Lead story with 6 bullet points on MOU details
- 8 insight cards across sections
- 4 Chart.js visualizations
- 12 timeline day cards
- 4 action items with owners and deadlines

### Step 6: Delivery (1 second)

**Claude Response:**
```
[Interactive HTML artifact delivered]

360 Newsletter for November 4-10, 2025

Key highlights this week:

• SpacePlan joint venture formalized (MOU signed, $1.2M initial pipeline)
• Brazil team capacity expansion underway (2 new hires in process)
• Service package design nearing completion (3-tier model ready)

Critical actions flagged:
• Finalize service pricing model (due Nov 20)
• Schedule strategic planning session (due Nov 17)
• Consult on team transition strategy (due Nov 20)

The newsletter includes 4 charts showing partnership portfolio, regional
distribution, task velocity, and team capacity.

Would you like me to:
- Expand any section with more detail?
- Add additional charts?
- Adjust the timeline?
- Export for board meeting?
```

---

## Example 2: Monthly Board Brief

### User Request
```
Create October newsletter for board meeting
```

### Step 1: Confirmation & Setup (5 seconds)

**Claude Response:**
```
Generating comprehensive October board brief for 360 Social Impact Studios...
Expanded data collection for monthly view with strategic framing.
```

**Internal Planning:**
- Date range: 2025-10-01 to 2025-10-31 (full month)
- Scope: All areas, board-level framing
- Data sources: All three (comprehensive)
- Output: Board-ready brief with 6-8 charts
- Emphasis: Strategic implications, financial metrics, forward-looking

### Step 2: Data Collection (60-90 seconds)

**Asana Collection (30-40 seconds, 10-12 API calls):**

Scan all priority projects (not just recent activity):
- Weekly Meeting Tracker
- Partnership Development
- SpacePlan Joint Venture
- GenIP Integration
- CNEN Partnership
- Board Materials
- Strategic Planning 2025-2027
- Client Engagements
- Operations
- Impact Tracking

For each: Get details, sections, completed tasks, modified tasks, task counts

**Gmail Collection (15-20 seconds, 6-8 API calls):**

Comprehensive searches:
- All partner communications (full month)
- Strategic sent emails
- Impact/testimonial emails
- Board-related correspondence
- Financial discussions
- International partner emails

Read high-priority threads (more than weekly)

**Google Drive Collection (15-20 seconds, 5-6 API calls):**

Comprehensive document search:
- Strategic documents (full month)
- Partner-specific documents (all partners)
- Financial/budget documents
- Impact reports
- Board materials
- Deliverables

Fetch more documents than weekly brief

### Step 3: Content Analysis & Scoring (15 seconds)

**Expanded Content Inventory:**
- Asana: 87 completed tasks, 120 active tasks
- Gmail: 34 relevant threads
- Drive: 18 strategic documents

**Comprehensive Scoring:**
More items analyzed, higher threshold for inclusion
Focus on strategic milestones over routine completions

**Section Assignment:**
All sections well-populated
Emphasis on strategic implications
Financial metrics highlighted
Forward-looking content emphasized

### Step 4: Chart Data Preparation (10 seconds)

**6-8 Charts Generated:**

1. **Partnership Portfolio Distribution** (Doughnut)
2. **Regional Distribution** (Pie)
3. **Monthly Task Velocity Trend** (Line - 4 weeks)
4. **Team Capacity** (Radar)
5. **Revenue Trajectory** (Line - quarterly with projection)
6. **Impact Metrics Trend** (Line - quarterly)
7. **Partnership Pipeline Health** (Radar - multi-dimensional)
8. **Strategic Priority Progress** (Horizontal bar)

### Step 5: HTML Generation (15 seconds)

**Enhanced Board Format:**

- **Executive Summary**: 4 cards (vs 3 for weekly)
- **Lead Story**: Expanded with strategic context
- **All Sections**: Populated with substantive content
- **Financial Metrics**: Dedicated subsection in Operations
- **Strategic Horizon**: Expanded to 30-60 days out
- **Charts**: 6-8 visualizations (vs 4 for weekly)
- **Action Items**: Board-level decisions highlighted

### Step 6: Delivery

**Claude Response:**
```
[Board-ready HTML artifact]

360 Social Impact Studios - October 2025 Board Brief

Executive Summary:
• SpacePlan joint venture formalized (5% royalty structure)
• Partnership pipeline grew 34% to $890K across 13 active relationships
• Team restructuring initiated (2 departures, 2 strategic hires)
• Q4 revenue trajectory stable at $89K (on pace for $110K projected)

The brief includes 8 charts analyzing partnership portfolio, regional
expansion, revenue trends, team capacity, and strategic progress.

Recommended for board review before Sunday meeting.
```

---

## Example 3: Partnership-Focused Brief

### User Request
```
Generate newsletter focused on SpacePlan partnership only, last 30 days
```

### Step 1: Confirmation & Setup (5 seconds)

**Claude Response:**
```
Generating SpacePlan-focused newsletter for October 15 - November 15...
All data collection filtered for SpacePlan mentions.
```

**Internal Planning:**
- Date range: 2025-10-15 to 2025-11-15
- Scope: SpacePlan partnership only
- Filter: All queries include SpacePlan filter
- Output: Deep-dive on single partnership

### Step 2: Filtered Data Collection (20-30 seconds)

**Asana: SpacePlan-specific**
```javascript
asana_search_tasks(
  workspace: "1210382795871981",
  projects_any: [spaceplan_project_gid],
  modified_on_after: "2025-10-15"
)

// Also search other projects for SpacePlan mentions
asana_search_tasks(
  workspace: "1210382795871981",
  text: "SpacePlan",
  modified_on_after: "2025-10-15"
)
```

**Gmail: SpacePlan communications only**
```javascript
search_gmail_messages(
  q: "(from:*@spaceplan.com OR to:*@spaceplan.com OR
      subject:SpacePlan OR SpacePlan) after:2025/10/15"
)
```

**Drive: SpacePlan documents only**
```javascript
google_drive_search(
  api_query: "modifiedTime > '2025-10-15T00:00:00Z' and
              fullText contains 'SpacePlan'",
  semantic_query: "SpacePlan joint venture partnership architecture innovation"
)
```

### Step 3: Partnership-Specific Analysis

**All content relates to SpacePlan:**
- MOU signing and terms
- Joint venture structure
- Initial pipeline development
- Team assignments
- Timeline and milestones
- Strategic implications

### Step 4: SpacePlan-Specific Charts

1. **SpacePlan Pipeline by Client Sector** (Doughnut)
2. **SpacePlan Revenue Projection** (Line)
3. **SpacePlan Milestone Timeline** (Horizontal bar)
4. **SpacePlan vs Other Partnerships** (Radar comparison)

### Step 5: Focused Newsletter Structure

**Sections:**
1. Executive Summary (SpacePlan highlights)
2. Partnership Overview (deep context)
3. Recent Developments (MOU, structure, team)
4. Pipeline & Opportunities (12 prospective clients)
5. Timeline & Milestones (90-day view)
6. Strategic Implications (for 360 overall)

### Step 6: Delivery

**Claude Response:**
```
[SpacePlan-focused HTML artifact]

SpacePlan Partnership Update - October 15 - November 15, 2025

This deep-dive covers the formation and early development of the
360 Space Innovation Studios joint venture:

• MOU signed November 8 with 5% royalty structure
• Initial pipeline: $1.2M across 12 architectural innovation clients
• 90-day transition period launched
• Walter as Managing Partner, Chandler as Strategic Partner

4 SpacePlan-specific charts included showing pipeline, projections,
milestones, and comparative partnership health.
```

---

## Example 4: Quick Weekly Digest (Team-Focused)

### User Request
```
Generate team update for last week
```

### Step 1: Adjusted Framing (5 seconds)

**Claude Response:**
```
Generating team-focused weekly update for November 4-10...
Emphasis on operational details and action items.
```

**Internal Planning:**
- Same data collection as standard weekly
- Different framing: Team operations focus
- More detail on tactical items
- Less executive/strategic framing

### Step 2-4: Same as Standard Weekly

Data collection, analysis, charts all similar to Example 1

### Step 5: Team-Focused Generation

**Adjusted Structure:**
- Executive Summary → "Week at a Glance"
- Less strategic context, more "what we did"
- Operations section emphasized
- Action items front and center
- Timeline more detailed (daily vs weekly view)

**Tone Adjustments:**
- More conversational
- Direct address ("We completed...", "Team achieved...")
- Focus on who did what
- Celebrate completions

### Step 6: Delivery

**Claude Response:**
```
[Team-focused HTML artifact]

360 Team Update - Week of November 4-10

What We Accomplished:
• SpacePlan MOU finalized (Chandler & Walter)
• GenIP integration completed (Felipe)
• Brazil team interviews finished (2 strong candidates)
• UW consulting presentation delivered

Action Items for Next Week:
• [12 specific team tasks with owners]

Great week, team! 23 tasks completed, several major milestones hit.
```

---

## Common Workflow Patterns

### Pattern 1: Sparse Period Handling

```
User: Generate newsletter for Thanksgiving week
Claude: [Detects low activity]
Result: Newsletter with transparent note about holiday,
        focus on strategic planning and upcoming priorities,
        forward-looking timeline emphasized
```

### Pattern 2: Multi-Period Comparison

```
User: Generate newsletters for October and November, then compare
Claude: [Generates both, then creates comparison section]
Result: Two newsletters + comparison showing trends, changes, acceleration/deceleration
```

### Pattern 3: Pre-Meeting Brief

```
User: Generate brief for tomorrow's board meeting, include talking points
Claude: [Standard generation + enhanced format]
Result: Newsletter + "Key Talking Points" section +
        "Anticipated Questions" section +
        "Decisions Needed" section
```

### Pattern 4: Iteration

```
User: Generate newsletter for last week
Claude: [Delivers initial version]
User: Expand the partnerships section
Claude: [Regenerates with deeper partnership content]
User: Add a chart showing team capacity
Claude: [Adds requested chart]
Result: Iteratively refined newsletter
```

---

## Time Expectations

| Newsletter Type | Data Collection | Analysis | Generation | Total |
|-----------------|----------------|----------|------------|-------|
| Weekly (standard) | 30-40s | 10s | 10s | ~60s |
| Monthly (board) | 60-90s | 15s | 15s | ~120s |
| Focused (single topic) | 20-30s | 10s | 10s | ~50s |
| Team update | 30-40s | 10s | 10s | ~60s |

**Factors that increase time:**
- More projects to scan
- Longer date range
- More comprehensive Gmail search
- More documents to fetch
- More charts to generate

**Factors that decrease time:**
- Narrower scope (focused brief)
- Shorter date range
- Fewer data sources
- Minimal charts

---

**Related Guides:**
- [Data Collection Guide](data-collection-guide.md) - For detailed data protocols
- [Content Analysis Framework](content-analysis-framework.md) - For scoring logic
- [Chart Specifications](chart-specifications.md) - For chart generation
- [Writing Style Guide](writing-style-guide.md) - For content writing
