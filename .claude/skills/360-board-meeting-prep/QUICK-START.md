# 360 Board Meeting Prep - Quick Start

## One-Line Summary
Transform scattered organizational data into polished, governance-ready board meeting packets with 5 professional documents from Asana, QuickBooks, Gmail, and Google Drive.

---

## When to Use

**Trigger phrases:**
- "Help me prep for the [date] board meeting"
- "Create a board packet for [date]"
- "Build board meeting materials"
- "Generate board documents"
- "I need to prepare for the board meeting"

**Proactive triggers:**
- 10 days before scheduled board meetings
- When "board meeting" mentioned in planning context

---

## 3-Step Quick Use

### Step 1: Request Board Packet

Simply state:
```
"Help me prep for the December 15th board meeting"
"Create board packet for Q4 annual meeting"
"Build materials for next board meeting"
```

**System will ask:**
- Meeting date?
- Meeting type (Annual / Quarterly / Special)?
- Key agenda topics?
- Need motion tracking? (usually yes)
- Any special appendices needed?

### Step 2: System Pulls Data Automatically

Auto-collects from:
- ✅ **Asana** - Client pipeline, strategic partnerships, action items
- ✅ **QuickBooks** - Revenue, expenses, AR aging, cash position
- ✅ **Gmail** - Communication patterns with strategic partners
- ✅ **Google Drive** - Prior board packets, historical context

**Validates data:**
- Flags stale projects (>14 days no update)
- Identifies missing custom fields
- Highlights incomplete financial data
- Notes low-interaction partnerships

### Step 3: Receive 5 Professional Documents

1. **Financial Dashboard** - Revenue, expenses, cash, pipeline
2. **Client Portfolio Health** - Relationship status, capacity analysis
3. **Strategic Initiatives** - Progress on 4 priorities, partnerships
4. **Governance & Compliance** - Action items, filings, board composition
5. **Motion Tracking Sheet** - Pre-drafted motions for voting

**Format:** DOCX with exact 360 formatting standards
**Time:** 45-60 minutes (vs. 8-12 hours manual)

---

## The 5 Documents Explained

### 1. 📊 Financial Dashboard
**Purpose:** Comprehensive financial health snapshot

**Key Sections:**
- Executive Summary (1-paragraph overall financial health)
- Revenue Analysis (YTD vs. $40K target, by source)
- Expense Analysis (by category, variance from budget)
- Cash Flow & Receivables (AR aging, cash runway)
- Pipeline Valuation (weighted by probability)
- Risk Assessment (flags for >60 day AR, <6 month runway, >20% variance)

**Data Sources:** QuickBooks + Asana pipeline

---

### 2. 🤝 Client Portfolio Health Report
**Purpose:** Relationship and capacity assessment

**Key Sections:**
- Executive Summary
- Tier 1 Strategic Partner Deep Dives (5 partners):
  - SpacePlan, GenIP, ScienceLink, NanoBioPlus, CNEN
  - For each: Relationship status, revenue, communication frequency, current projects, risks
- Major Clients Summary Table
- Portfolio Analytics (concentration, retention, acquisition)
- Capacity Analysis (team utilization, pipeline constraints)

**Data Sources:** Asana + Gmail + past conversations

---

### 3. 🎯 Strategic Initiatives Update
**Purpose:** Progress tracking on strategic priorities

**Key Sections:**
- 4 Strategic Priorities (with progress metrics):
  1. Global technology transfer
  2. Brazilian joint ventures
  3. GenIP commercialization
  4. University partnerships
- Major Partnership Updates:
  - SpacePlan JV status
  - GenIP product development
  - NanoBioPlus partnership
  - CNEN technology transfer
- Strategic Risks & Opportunities

**Data Sources:** Asana + Gmail + Drive documents

---

### 4. ⚖️ Governance & Compliance Report
**Purpose:** Board oversight and legal compliance

**Key Sections:**
- Outstanding Action Items (from prior meetings)
- Upcoming Compliance Calendar:
  - 990-EZ filing (May 15)
  - DE Annual Report (March 1)
  - Business licenses renewals
- Board Composition & Terms
- Policy Updates Required
- Legal/Contract Updates

**Data Sources:** Asana governance project + Drive compliance folder

---

### 5. 🗳️ Motion Tracking Sheet
**Purpose:** Board voting record and resolutions

**Typical Motions:**
- Approve financial statements
- Authorize partnership agreements
- Approve budget amendments
- Elect/re-elect board members
- Approve strategic initiatives

**Format:** Motion text, voting record, implementation tracking

**Data Sources:** Agenda items + prior motion sheets

---

## 6-Phase Workflow

```
Phase 1: Initial Consultation & Data Collection (T-10 days)
├─ Gather meeting parameters (date, type, agenda)
├─ Confirm data source access
├─ Pull base data (Asana, QuickBooks, Gmail, Drive)
└─ Validate data and identify gaps

Phase 2: Draft Document Generation (T-7 days)
├─ Generate Financial Dashboard (references/financial-dashboard.md)
├─ Generate Client Portfolio Health (references/client-portfolio-health.md)
├─ Generate Strategic Initiatives (references/strategic-initiatives.md)
├─ Generate Governance & Compliance (references/governance-compliance.md)
└─ Generate Motion Tracking Sheet (references/motion-preparation.md)

Phase 3: Quality Assurance & Review (T-5 days)
├─ Cross-document consistency checks
├─ Data validation
├─ Financial calculations verification
└─ Present drafts for user approval

Phase 4: Final Generation & Distribution (T-3 days)
├─ Generate DOCX files with exact formatting
├─ Create board packet cover page
├─ Upload to Google Drive
├─ Send to board members
└─ Create meeting agenda

Phase 5: Meeting Support (T-0 days)
├─ Present documents during meeting
├─ Track motions and votes
├─ Capture action items
└─ Document key decisions

Phase 6: Post-Meeting Follow-Up (T+2 days)
├─ Create Asana tasks for action items
├─ Assign owners and due dates
├─ Archive board packet
└─ Update compliance calendar
```

---

## Data Source Setup

### Asana Integration
**Required Access:**
- Client Delivery Hub Portfolio: `1211712180134240`
- Board/Governance Project: `1211794887178220`

**Custom Fields Needed:**
- `contract_value` (Number)
- `probability` (Single-select: 10%, 25%, 50%, 75%, 90%)
- `stage` (Single-select: Prospect, Proposal, Contract, Delivery, Complete)
- `client_tier` (Single-select: Tier 1 Strategic, Major, Standard)

### QuickBooks Integration
**Preferred:** MCP server for automatic queries
**Fallback:** Manual CSV export

**Required Reports:**
- Revenue YTD (by source)
- Expenses YTD (by category)
- AR Aging Summary
- Cash Position

**If MCP unavailable:** System will prompt for CSV exports

### Gmail Integration
**Purpose:** Communication pattern analysis with strategic partners

**Searched Partners:**
- SpacePlan
- GenIP
- ScienceLink
- NanoBioPlus
- CNEN

**Metrics:** Email count last 60 days (relationship health indicator)

### Google Drive Integration
**Purpose:** Historical context and prior board packets

**Searches:** "Board Packet" in "Board Materials" folder

---

## Strategic Partners Tracked

| Partner | Type | Key Metrics |
|---------|------|-------------|
| **SpacePlan** | JV Partner | JV status, equity %, integration progress |
| **GenIP** | Product Dev | Revenue share, product milestones, market traction |
| **ScienceLink** | Client + Partner | Project status, revenue, relationship health |
| **NanoBioPlus** | Strategic Client | Contract value, delivery timeline, expansion opportunities |
| **CNEN** | Tech Transfer | Technology pipeline, licensing status, regulatory progress |

---

## 360's 4 Strategic Priorities

### Priority 1: Global Technology Transfer
**Goal:** Establish 360 as leading tech transfer intermediary
**Metrics:** # technologies evaluated, # licensing deals closed, revenue from tech transfer

### Priority 2: Brazilian Joint Ventures
**Goal:** Build sustainable partnership ecosystem in Brazil
**Metrics:** # active JVs, revenue from Brazilian partnerships, cross-border deals

### Priority 3: GenIP Commercialization
**Goal:** Scale GenIP platform and generate recurring revenue
**Metrics:** GenIP ARR, # active users, product milestones achieved

### Priority 4: University Partnerships
**Goal:** Create university innovation pipeline
**Metrics:** # university partnerships, # technologies sourced, # spin-outs supported

---

## Quality Assurance Checks

**Cross-Document Consistency:**
- Financial figures match across all documents
- Client names and tiers consistent
- Strategic priority progress aligned with project statuses

**Data Validation:**
- Revenue + Expenses = Net Income calculations correct
- Pipeline valuation = (Contract Value × Probability) sums correctly
- AR Aging totals match QuickBooks
- Cash runway calculations accurate

**Formatting Compliance:**
- Headers use 360 brand colors
- Tables formatted consistently
- Page breaks logical
- Motion numbering sequential

**Gap Flagging:**
- Projects not updated >14 days highlighted
- Strategic partners with <2 email interactions flagged
- Missing custom fields noted
- Incomplete financial data identified

---

## Common Use Cases

### Use Case 1: Q4 Annual Meeting Prep
```
Request: "Help me prep for the December 15th annual board meeting"

Process:
1. Pulls YTD financials from QuickBooks
2. Analyzes 12-month client pipeline from Asana
3. Reviews strategic partner communications (full year)
4. Generates 5 documents with annual perspective
5. Includes budget vs. actual analysis
6. Prepares motions for next year's budget approval

Output: Complete annual board packet (5 docs, 25-30 pages)
Time: 55 minutes
```

### Use Case 2: Q2 Quarterly Update
```
Request: "Create board packet for June quarterly meeting"

Process:
1. Pulls Q2 financials and Q3 pipeline
2. Focuses on quarterly strategic priorities
3. Highlights quarterly partnership milestones
4. Reviews Q2 action items from last meeting
5. Prepares mid-year checkpoint motions

Output: Quarterly board packet (5 docs, 18-22 pages)
Time: 45 minutes
```

### Use Case 3: Special Meeting (Partnership Decision)
```
Request: "Build materials for special board meeting about SpacePlan JV"

Process:
1. Deep-dive on SpacePlan relationship (emails, projects, revenue)
2. Financial analysis focused on JV economics
3. Strategic initiative focused on JV integration
4. Governance section on partnership approval requirements
5. Motion prepared for JV authorization

Output: Special topic board packet (focused, 12-15 pages)
Time: 35 minutes
```

---

## Post-Meeting Follow-Up

**Automatic Action Items:**
1. Extract decisions and action items from meeting
2. Create Asana tasks in Board/Governance project
3. Assign owners based on discussion
4. Set due dates (typically next board meeting date)
5. Add task descriptions with context

**Motion Tracking:**
1. Record votes for each motion
2. Update motion status (Passed / Failed / Tabled)
3. Create implementation tasks for passed motions
4. Archive motion sheet in Google Drive

**Compliance Calendar Update:**
1. Add newly identified compliance items
2. Update completion status for existing items
3. Flag items approaching deadlines
4. Create reminders for upcoming filings

---

## Troubleshooting

**"QuickBooks data not loading"**
→ Check MCP server connection
→ Fallback: Request CSV exports (Revenue, Expenses, AR Aging, Cash)
→ Manual data entry if needed

**"Asana projects not updating"**
→ Verify portfolio and project GIDs in config
→ Check Asana API permissions
→ Refresh Asana connection

**"Strategic partner data incomplete"**
→ Check Gmail integration for partner domains
→ Verify partner names match exactly
→ Manually supplement with recent interaction notes

**"Documents formatting incorrectly"**
→ Verify DOCX utilities are installed (python-docx)
→ Check template files in assets/templates/
→ Review formatting specification in references/

---

## Quick Commands

| Task | Command |
|------|---------|
| Full board packet | "Prep for [date] board meeting" |
| Single document | "Generate just the financial dashboard" |
| Strategic update | "Pull SpacePlan JV update for board" |
| Post-meeting follow-up | "Extract action items from meeting transcript" |
| Motion tracking | "Create motion tracking sheet" |
| Compliance calendar | "Review upcoming compliance deadlines" |

---

## Supporting Files

**Core Documentation:**
- `SKILL.md` - Complete 6-phase workflow orchestrator
- `README.md` - Overview and installation
- This file (QUICK-START.md) - Fast reference

**References (Specialized Workflows):**
- `references/financial-dashboard.md` - Revenue, expenses, pipeline logic
- `references/client-portfolio-health.md` - Relationship assessment, capacity
- `references/strategic-initiatives.md` - Partnership tracking, priorities
- `references/governance-compliance.md` - Action items, filings, board composition
- `references/motion-preparation.md` - Motion drafting and tracking

**Templates:**
- `assets/templates/board_packet_cover.md` - Cover page structure
- `assets/templates/financial_dashboard_template.md` - Financial report layout
- `assets/templates/motion_sheet_template.md` - Voting record format

**Utilities:**
- `assets/docx_utilities.py` - Python DOCX generation scripts

---

## Next Steps

1. ✅ **Test data connections** - Asana, QuickBooks, Gmail, Drive
2. ✅ **Run first packet** - Generate for upcoming/past meeting to validate
3. ✅ **Review outputs** - Check accuracy and formatting
4. ✅ **Customize** - Adjust templates to match board preferences
5. ✅ **Schedule** - Set up proactive reminders for future meetings

---

**Ready to prep? Request a board packet for your next meeting! 📋**

Version 1.0.0 | Updated: 2025-11-22 | 360 Social Impact Studios
