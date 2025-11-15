# Data Collection Guide

Comprehensive protocols for collecting data from Asana, Gmail, and Google Drive for newsletter generation.

## Overview

Data collection follows a five-phase protocol:
1. Connect to data sources
2. Define date range
3. Collect Asana data (70% weight)
4. Collect Gmail data (20% weight)
5. Collect Google Drive data (10% weight)

**Total time:** 30-40 seconds for standard weekly newsletter

## Phase 1: Connect to Data Sources

### Asana Connection

```javascript
// Step 1: Get workspace GID
Tool: asana_list_workspaces()
Expected: 360socialventures.com
GID: 1210382795871981

// Step 2: Confirm connection
Verify workspace accessible
Check user permissions
```

### Gmail Connection

```javascript
// Step 1: Get user profile
Tool: read_gmail_profile()
Expected: chandler@360social.org
Verify: Gmail API access enabled

// Step 2: Test search
Simple query to confirm search access
```

### Google Drive Connection

```javascript
// Step 1: Verify search access
Tool: google_drive_search (test query)
Expected: Results returned
Verify: Drive API permissions
```

## Phase 2: Define Date Range

### Standard Periods

**Weekly (default):**
```
Start: Previous Monday at 00:00:00
End: Previous Sunday at 23:59:59
Format: YYYY-MM-DD
```

**Monthly:**
```
Start: First day of previous month at 00:00:00
End: Last day of previous month at 23:59:59
Format: YYYY-MM-DD
```

**Custom:**
```
Start: User-specified date
End: User-specified date
Format: YYYY-MM-DD
```

### Date Format Reference

| Tool | Format | Example |
|------|--------|---------|
| Asana (date) | YYYY-MM-DD | 2025-11-04 |
| Asana (datetime) | YYYY-MM-DDTHH:MM:SSZ | 2025-11-04T00:00:00Z |
| Gmail | YYYY/MM/DD | 2025/11/04 |
| Drive (RFC3339) | YYYY-MM-DDTHH:MM:SSZ | 2025-11-04T00:00:00Z |

## Phase 3: Collect Asana Data

### Priority Projects List

Always scan these projects:
1. Weekly Meeting Tracker
2. Partnership Development
3. Client Engagements
4. SpacePlan Joint Venture
5. GenIP Integration
6. CNEN Partnership
7. Any project with "Board" in name
8. Any project with partner organization names

### Step 3.1: Get Active Projects

```javascript
Tool: asana_get_projects
Parameters:
  workspace: [workspace_gid]
  archived: false

Output: List of all active project names and IDs
```

### Step 3.2: Identify Key Projects

Use typeahead search for each priority project:

```javascript
Tool: asana_typeahead_search
Parameters:
  workspace_gid: [workspace_gid]
  resource_type: "project"
  query: "Partnership Development"

Repeat for each priority project
Store project GIDs for next steps
```

### Step 3.3: Scan Each Project

**For each priority project, run these queries in sequence:**

#### 1. Get Project Details

```javascript
Tool: asana_get_project
Parameters:
  project_id: [project_gid]
  opt_fields: "name,owner,members,custom_fields,notes,due_date,current_status"

Captures:
- Project metadata
- Custom field definitions
- Current status
- Owner and team members
```

#### 2. Get Project Sections

```javascript
Tool: asana_get_project_sections
Parameters:
  project_id: [project_gid]

Captures:
- Section organization
- Workflow stages
- Pipeline structure
```

#### 3. Search Completed Tasks

```javascript
Tool: asana_search_tasks
Parameters:
  workspace: [workspace_gid]
  projects_any: [project_gid]
  completed: true
  completed_on_after: [start_date]
  completed_on_before: [end_date]
  opt_fields: "name,notes,completed_at,assignee,custom_fields,tags"

Captures:
- Deliverables completed
- Milestones hit
- Tasks finished in period
```

#### 4. Search Modified/Active Tasks

```javascript
Tool: asana_search_tasks
Parameters:
  workspace: [workspace_gid]
  projects_any: [project_gid]
  modified_on_after: [start_date]
  modified_on_before: [end_date]
  opt_fields: "name,notes,due_date,assignee,custom_fields,tags"

Captures:
- Work in progress
- Tasks updated
- Upcoming deadlines
```

#### 5. Get Task Counts

```javascript
Tool: asana_get_project_task_counts
Parameters:
  project_id: [project_gid]

Captures:
- Total tasks
- Completed vs incomplete
- Project health metrics
```

### Step 3.4: Aggregate Asana Metrics

Calculate from collected data:

**Task Metrics:**
- Total tasks completed in period
- Tasks by project/partnership
- Tasks by status (complete, in-progress, blocked)
- Task velocity (completions per day/week)

**Geographic Distribution:**
- North America (keywords: US, USA, Seattle, Washington, Canada)
- Latin America (keywords: Brazil, São Paulo, LATAM, Argentina)
- Europe (keywords: UK, Europe, EU, Germany, France)
- Asia-Pacific (keywords: China, Australia, Japan, APAC)
- Other (all remaining)

**Partnership Pipeline:**
- By custom field "Stage" if available
- Otherwise categorize by section or task name
- Stages: Discovery, Scoping, Active, Renewal

**Team Capacity:**
- Tasks per assignee
- Workload distribution
- Team velocity

## Phase 4: Collect Gmail Data

### Step 4.1: Search Partnership Communications

Search for emails from key partner domains:

```javascript
Tool: search_gmail_messages
Parameters:
  q: "from:(*@spaceplan.com OR *@genip.com OR *@sciencelink.org OR
      *@nanobioplus.com OR *@cnen.gov.br OR *@cmu.edu OR
      *@lifesciencewa.org) after:[start_date] before:[end_date]"

Then for each high-priority thread:
Tool: read_gmail_thread
Parameters:
  thread_id: [thread_id]

Captures:
- Partnership developments
- Strategic discussions
- Decision points
- Relationship evolution
```

### Step 4.2: Search Sent Strategic Emails

Check for significant outbound communications:

```javascript
Tool: search_gmail_messages
Parameters:
  q: "from:me (partnership OR agreement OR proposal OR contract OR
      MOU OR deliverable OR LOI) after:[start_date] before:[end_date]"

Captures:
- Proposals sent
- Agreements executed
- Deliverables shared
- Strategic outreach
```

### Step 4.3: Search for Impact/Client Feedback

Look for testimonials and impact reports:

```javascript
Tool: search_gmail_messages
Parameters:
  q: "(testimonial OR feedback OR impact OR outcome OR thank OR
      success OR results) after:[start_date] before:[end_date]"

Captures:
- Client testimonials
- Impact stories
- Success metrics
- Positive feedback
```

### Step 4.4: Search Board-Related Communications

```javascript
Tool: search_gmail_messages
Parameters:
  q: "(board OR director OR governance) after:[start_date] before:[end_date]"

Captures:
- Board communications
- Governance updates
- Strategic decisions
- Director correspondence
```

### Step 4.5: Categorize Email Content

For each email thread analyzed:
- **Determine relevance** - Which section does it belong in?
  - Partnerships: Partnership developments, agreements
  - Programs: Project updates, deliverables
  - Impact: Testimonials, outcomes, feedback
  - Operations: Team updates, financial discussions

- **Extract key information**
  - Decisions made
  - Announcements
  - Developments
  - Action items

- **Note action items or follow-ups**
  - Who needs to do what
  - By when
  - Dependencies

- **Identify metrics or outcomes**
  - Numbers mentioned (revenue, impact, growth)
  - Milestones hit
  - Goals achieved

## Phase 5: Collect Google Drive Data

### Step 5.1: Search Recent Strategic Documents

```javascript
Tool: google_drive_search
Parameters:
  api_query: "modifiedTime > '[start_date_RFC3339]' and
              (name contains 'partnership' or
               name contains 'agreement' or
               name contains 'report' or
               name contains 'deliverable' or
               name contains 'impact' or
               name contains 'board')"
  semantic_query: "partnership agreements reports deliverables
                   impact metrics board updates"
  order_by: "modifiedTime desc"
  page_size: 20

Captures:
- Recent strategic documents
- Partnership materials
- Reports and deliverables
- Board materials
```

### Step 5.2: Search by Partner Name

For each key partner:

```javascript
Tool: google_drive_search
Parameters:
  api_query: "modifiedTime > '[start_date_RFC3339]' and
              fullText contains '[partner_name]'"
  semantic_query: "[partner_name] partnership updates agreements"
  order_by: "modifiedTime desc"

Iterate through:
- SpacePlan
- GenIP
- ScienceLink
- NanoBioPlus
- CNEN

Captures:
- Partner-specific documents
- Collaboration materials
- Agreement drafts
- Project documentation
```

### Step 5.3: Search Impact Documentation

```javascript
Tool: google_drive_search
Parameters:
  api_query: "modifiedTime > '[start_date_RFC3339]' and
              (name contains 'impact' or
               name contains 'metrics' or
               name contains 'outcomes')"
  semantic_query: "social impact metrics community outcomes
                   systems change measurement"
  order_by: "modifiedTime desc"

Captures:
- Impact metrics
- Outcome reports
- Community data
- Systems change evidence
```

### Step 5.4: Search Financial Documents

```javascript
Tool: google_drive_search
Parameters:
  api_query: "modifiedTime > '[start_date_RFC3339]' and
              (name contains 'financial' or
               name contains 'revenue' or
               name contains 'budget')"
  semantic_query: "financial revenue budget forecast sustainability"
  order_by: "modifiedTime desc"

Captures:
- Financial reports
- Budget documents
- Revenue projections
- Sustainability metrics
```

### Step 5.5: Fetch Key Documents

For high-priority documents identified:

```javascript
Tool: google_drive_fetch
Parameters:
  document_ids: [array of doc IDs from searches]

Extract from fetched documents:
- Key metrics (revenue, impact numbers, growth)
- Decisions documented
- Impact data (beneficiaries, outcomes, systems change)
- Partnership status updates
- Financial milestones
```

## Data Quality Checks

### Asana Data Quality

**Verify:**
- [ ] All priority projects found
- [ ] Custom fields accessible
- [ ] Task counts seem reasonable
- [ ] Date filters working correctly
- [ ] Geographic distribution looks accurate

**Common issues:**
- Project renamed → Use typeahead to find new name
- Custom field changed → Update field name in queries
- No tasks in period → Confirm date range is correct
- Missing project → Add to priority list

### Gmail Data Quality

**Verify:**
- [ ] Partner domains returning results
- [ ] Sent emails captured
- [ ] Date range filter working
- [ ] Thread reading successful
- [ ] Relevant conversations identified

**Common issues:**
- Partner changed domain → Update domain list
- Low email volume → Expand search keywords
- Too many results → Refine search criteria
- Missing key thread → Check for typos in search

### Drive Data Quality

**Verify:**
- [ ] Recent documents found
- [ ] Partner documents identified
- [ ] Impact docs located
- [ ] Financial docs accessible
- [ ] Fetch successful for priority items

**Common issues:**
- No documents found → Check date range
- Partner docs missing → Verify naming conventions
- Fetch failed → Check document permissions
- Wrong documents returned → Refine semantic query

## Performance Optimization

### Parallel Queries

Run these in parallel when possible:
- Multiple Asana project searches
- Multiple Gmail searches (different keywords)
- Multiple Drive searches (different criteria)

### Sequential Requirements

Must run sequentially:
1. Get workspace → Then search projects
2. Find project GID → Then search tasks in project
3. Search emails → Then read high-priority threads
4. Search documents → Then fetch high-priority docs

### Query Batching

**Batch similar queries:**
```javascript
// Instead of 5 separate partner searches
google_drive_search for all partners at once with OR

// Instead of 3 separate Asana project queries
asana_search_tasks across multiple projects_any
```

## Data Retention

### What to Store

**For next newsletter generation:**
- Project GIDs (for faster lookup)
- Partner email domains (for consistent searches)
- Custom field names (for metrics)
- Common search patterns (for optimization)

**For trend analysis:**
- Previous period metrics (for comparison)
- Historical chart data (for trends)
- Significance scores (for calibration)

### What Not to Store

- Raw email content (privacy)
- Complete task details (data volume)
- Full document text (storage)
- Individual assignee data (privacy)

## Troubleshooting

### No Data Returned

**Check:**
1. Data source connection successful?
2. Date range correctly formatted?
3. Search queries syntactically correct?
4. Permissions allow access?
5. Data actually exists for period?

### Incomplete Data

**Check:**
1. All priority projects scanned?
2. All partner domains included?
3. Search keywords comprehensive enough?
4. Date range appropriate for content type?
5. API rate limits hit?

### Wrong Data Returned

**Check:**
1. Date filters applied correctly?
2. Search keywords too broad?
3. Project IDs correct?
4. Email domains accurate?
5. Document queries refined enough?

## Best Practices

### Query Construction

1. **Start broad, then refine**
   - Initial query captures wide net
   - Review results
   - Narrow search if too many irrelevant items

2. **Use multiple search methods**
   - Asana: Project search + task search + typeahead
   - Gmail: From domain + keywords + sent items
   - Drive: Name search + semantic search + full text

3. **Verify critical items**
   - High-significance items deserve confirmation
   - Read full thread/document if needed
   - Cross-check across sources

### Data Validation

1. **Sanity check metrics**
   - Does task count seem reasonable?
   - Do completion rates make sense?
   - Are geographic distributions plausible?

2. **Cross-reference sources**
   - Asana task mentions partnership
   - Gmail confirms partnership communication
   - Drive has partnership documentation
   - All three align = high confidence

3. **Flag anomalies**
   - Unusually high/low activity
   - Missing expected content
   - Contradictory information across sources

### Time Management

**Standard weekly newsletter:** 30-40 seconds total
- Asana: 15-20 seconds (5-6 API calls)
- Gmail: 8-12 seconds (3-4 API calls)
- Drive: 6-8 seconds (2-3 API calls)

**Monthly board brief:** 60-90 seconds total
- Asana: 30-40 seconds (10-12 API calls)
- Gmail: 15-20 seconds (6-8 API calls)
- Drive: 15-20 seconds (5-6 API calls)

**Optimize for:**
- Parallel queries when possible
- Minimal sequential dependencies
- Efficient query construction
- Appropriate page sizes

---

**Next:** See [Content Analysis Framework](content-analysis-framework.md) for how collected data is analyzed and scored.
