# Workflow Example: Generating an Executive Brief

**Complete walkthrough of creating a weekly executive brief from start to finish.**

## User Request

```
Generate this week's 360 Impact Brief
```

## Phase 1: Data Collection (12 minutes)

### Step 1.1: Asana Workspace Discovery
```javascript
asana_list_workspaces()
→ Get workspace GID "1206587815959876" for "360socialventures.com"
```

### Step 1.2: Project Discovery
```javascript
asana_typeahead_search(resource_type="project", workspace_gid="...", query="")
→ Returns 15 projects: CNEN, GenIP, NanoBioPlus, Limis, BIG NCP, etc.
```

### Step 1.3: CNEN Partnership Deep Dive
```javascript
// Get project details
asana_get_project(project_id="...", opt_fields="...")
→ Status: Green, Phase: IRDose Session 3, Priority: High

// Recent tasks
asana_search_tasks(projects_any="...", completed_on_after="2025-11-08")
→ 3 completed tasks, 2 upcoming

// Significance Score: 8/10 (Strategic: 3, Revenue: 3, Urgency: 2, Visibility: 1)
→ Decision: Lead story for Partnerships section
```

### Step 1.4: Team Restructuring Discovery
```javascript
asana_search_tasks(text="hiring OR candidate", completed=false)
→ "Finalize Nadia vs. Leo decision" (Due: Nov 17, Priority: Critical)

asana_get_task(task_id="...", opt_fields="...")
→ Candidate profiles: Nadia (corp BD/AI), Leo (multilingual/agritech)

// Significance Score: 9/10 (Strategic: 4, Revenue: 2, Urgency: 2, Visibility: 1)
→ Decision: Lead story for Operations section
```

### Step 1.5: Gmail Partnership Communications
```javascript
search_gmail_messages(q="from:@cnen.gov.br OR to:@cnen.gov.br newer_than:14d")
→ 8 threads found

read_gmail_thread(thread_id="...", include_full_messages=true)
→ Email chain about medical physics consulting, nuclear medicine programs
→ CNEN interested in scope beyond IRDose
```

### Step 1.6: Google Drive Strategic Documents
```javascript
google_drive_search(
    api_query="modifiedTime > '7 days ago'",
    semantic_query="strategic plan roadmap partnership board"
)
→ 7 documents: "Board Meeting Prep Nov 17", "NanoBioPlus Market Entry"

google_drive_fetch(document_ids=["..."])
→ Slide deck with merger update, team restructuring, Q1 2026 objectives
```

## Phase 2: Analysis & Prioritization (3 minutes)

### Organize by Section

**Partnerships** (5 items):
1. CNEN Expansion - 8/10
2. NanoBioPlus Strategy Week - 7/10
3. GenIP Integration - 6/10
4. Active Client Work - 5/10
5. Service Packaging - 6/10

**Operations** (4 items):
1. Team Restructuring (Nadia vs. Leo) - 9/10
2. Claude Transition - 7/10
3. Merger Integration - 8/10
4. Team Capacity Analysis - 6/10

**Strategy** (3 items):
1. Board Meeting Prep - 9/10
2. Strategy Week Planning - 7/10
3. Financial Position - 7/10

### Identify Lead Stories

**Top 4 Developments** (score 8+):
1. Team Restructuring (9/10) - Urgent board decision
2. Board Meeting (9/10) - Critical governance moment
3. Merger Integration (8/10) - Major organizational change
4. CNEN Expansion (8/10) - Revenue opportunity

## Phase 3: Content Generation (6 minutes)

### Executive Summary (3 cards, 60-80 words each)

**Card 1 - Strategic Inflection Point**:
"Space Innovation Studios merger LOI signed with transition timeline established. Board meeting Sunday (Nov 17) to review merger roadmap, team restructuring, and Q1 2026 objectives. Guilherme (NanoBioPlus CEO) and Daniel (Carnegie Mellon) arriving for strategy week. Financial constraints from lost federal funding require careful capacity management during expansion."

**Card 2 - Partnership Momentum**:
"CNEN partnership advancing with IRDose Session 3 scheduled and new consulting opportunities emerging around medical physics and nuclear medicine. GenIP platform integration progressing with biweekly syncs. Active client work across Limis, BIG NCP, and University of Minnesota..."

**Card 3 - Team Evolution**:
"Claude transitioning to Space Innovation Studios requires immediate replacement strategy. Nadia and Leo advancing as strong candidates with complementary profiles..."

### Partnerships Section

**Lead Story - CNEN Strategic Partnership Expansion** (400 words):
- Current Status: IRDose Session 3 scheduled Monday
- Expansion Opportunities: Medical physics, nuclear medicine
- Relationship Context: Cornerstone for Brazil operations
- Strategic Implications: Template for Latin America partnerships
- Revenue: Multi-service relationship

**Additional Cards**:
- GenIP Platform Integration (250 words)
- NanoBioPlus U.S. Market Entry (280 words)
- Active Client Work (grouped, 200 words)

**Service Package Chart Data**:
- Venture IQ: 85%
- Intelligence Audit: 60%
- Innovation Compass: 100%

**Action Items** (3 tasks):
1. CNEN expansion proposal (Chandler & Walter, Nov 22, High)
2. NanoBioPlus roadmap (Chandler & Guilherme, Nov 19-24, In Progress)
3. Service packaging framework (Chandler & Walter, Nov 20, In Progress)

### Operations Section

**Lead Story - Team Restructuring** (350 words):
- Claude's Transition: Departure creates gap
- Replacement Strategy: Timing, skills, cultural fit
- Board Context: Expected transition, Sunday decision

**Candidate Analysis Card** (450 words):
- Nadia's Profile: Corporate BD, AI proficiency
- Leo's Profile: Multilingual, agritech expertise
- Decision Framework: Immediate needs vs. strategic priorities

**Team Capacity Chart Data**:
- Current: [50, 75, 60, 70, 50, 30]
- With Both Hires: [90, 85, 95, 90, 90, 85]

### Strategy Section

**Board Meeting Strategic Agenda** (400 words):
- Meeting Context: Annual board during transition
- Key Agenda Items: Partnerships, merger, team, financial
- Board Decisions: Hiring, merger plan, Q1 priorities
- Presentation Materials: Visualizations, timeline, metrics

### Timeline Section

Day-by-day breakdown:
- Sunday Nov 17: Board meeting, merger review
- Monday Nov 18: CNEN Session 3, Limis standup, strategy week begins
- Tuesday Nov 19: GenIP sync, Guilherme arrives
- Nov 18-24: Strategy week sessions

## Phase 4: Visual Rendering (3 minutes)

### HTML Structure
- Semantic markup with accessibility features
- Sidebar navigation
- Color-coded sections (purple/green/amber)
- Responsive design system

### Chart Configuration
- Service Package Chart (horizontal bar)
- Team Capacity Chart (radar)

### JavaScript Initialization
- Navigation handlers
- Intersection observer
- Chart initialization

## Phase 5: Quality Assurance (2 minutes)

**Checklist**:
- ✅ All major partnerships represented
- ✅ Team composition accurate
- ✅ Financial position stated
- ✅ Upcoming milestones captured
- ✅ Action items have owners/dates
- ✅ Executive summary provides strategic insights
- ✅ Lead stories have depth
- ✅ HTML valid, charts working
- ✅ Professional appearance

## Phase 6: Delivery (30 seconds)

**File**: `360-impact-brief-2025-11-15.html`

**Summary**:
"This week's executive brief highlights three critical developments:
- CNEN partnership expanding with new consulting opportunities
- Team restructuring decision required (Nadia vs. Leo) ahead of board meeting
- Strategy week with Guilherme (NanoBioPlus) and Daniel (Carnegie Mellon)

[View your executive brief](computer:///mnt/user-data/outputs/360-impact-brief-2025-11-15.html)"

## Total Time: 26.5 minutes

- Data Collection: 12 min
- Analysis & Prioritization: 3 min
- Content Generation: 6 min
- Visual Rendering: 3 min
- Quality Assurance: 2 min
- Delivery: 0.5 min

## Key Decisions Made

**Prioritization**:
- Led with highest-scored items (team 9/10, board 9/10)
- Elevated CNEN due to revenue expansion
- Included all major partnerships with varying depth

**Content Depth**:
- Deep coverage on CNEN, team, board (lead stories)
- Moderate coverage on GenIP, NanoBioPlus, client work
- Brief mentions on service packaging, operational details

**Visual Design**:
- Production design system
- Two charts (service packages, team capacity)
- Color-coded sections

**Strategic Framing**:
- Emphasized inflection point (merger, hiring, board)
- Connected partnership momentum to revenue sustainability
- Explained team investment during constraints

## What Made This Brief Effective

**Strategic Signal**:
- Executive summary truly highlights strategic position
- Lead stories explain why they matter, not just what happened
- Decision frameworks help board make informed choices

**Operational Grounding**:
- Every statement backed by actual data
- Action items specific with owners and deadlines
- Timeline provides clear week-ahead visibility

**Professional Quality**:
- Visual polish suitable for board distribution
- Accessible design (WCAG AA)
- Interactive features

**Decision Support**:
- Hiring decision framed with options and tradeoffs
- Financial constraints explained with sustainability pathway
- Partnership opportunities sized for revenue impact

---

**Outcome**: A production-quality executive intelligence brief that enables strategic decision-making, board communication, and stakeholder engagement. The 26-minute investment delivers a comprehensive briefing that would take hours to compile manually.
