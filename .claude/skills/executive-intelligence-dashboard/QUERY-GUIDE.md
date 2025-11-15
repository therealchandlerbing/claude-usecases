# Query Guide: Data Source Strategies

**Reference for querying Asana, Gmail, and Google Drive effectively.**

## Query Philosophy

### Three Principles

**1. Start Broad, Then Narrow**
Begin with general searches to understand the landscape, then refine for specific information.

**2. Cross-Reference for Completeness**
Information often exists in multiple places. Check all sources to build the full picture.

**3. Validate Before Using**
Confirm that search results actually contain the information you need before including in the brief.

## Asana Query Strategies

### Workspace Discovery
```javascript
asana_list_workspaces()
→ Returns workspace list, find 360socialventures.com
```

### Project Discovery
```javascript
// Recent/relevant projects
asana_typeahead_search(
    resource_type="project",
    workspace_gid="...",
    query=""
)

// Specific project
asana_typeahead_search(
    resource_type="project",
    workspace_gid="...",
    query="CNEN"
)
```

### Project Details
```javascript
asana_get_project(
    project_id="...",
    opt_fields="name,notes,owner,members,custom_fields,current_status_update"
)
```

### Task Searches
```javascript
// Recent completions
asana_search_tasks(
    workspace="...",
    completed_on_after="2025-11-08",
    sort_by="completed_at",
    sort_ascending=false
)

// High-priority upcoming
asana_search_tasks(
    workspace="...",
    completed=false,
    due_on_before="2025-11-29",
    sort_by="due_on"
)
```

### Common Patterns

**Pattern 1: Partnership Deep Dive**
1. Find project: `asana_typeahead_search`
2. Get details: `asana_get_project`
3. Get status: `asana_get_project_statuses`
4. Get tasks: `asana_search_tasks` (active + completed)

**Pattern 2: Team Workload**
1. Get team members: `asana_get_team_users`
2. For each member: `asana_search_tasks` (assigned, incomplete)
3. Count and categorize by due date

## Gmail Query Strategies

### Profile Context
```javascript
read_gmail_profile()
→ Get user's email address
```

### Search Operators

**Time-Based**:
```
newer_than:7d
after:2025/11/08 before:2025/11/15
newer_than:1m
```

**Sender/Recipient**:
```
from:@partnerdomain.com
to:user@email.com
from:@domain1.com OR to:@domain2.com
-from:noreply@
```

**Content**:
```
subject:(partnership OR agreement)
fullText contains 'strategic planning'
has:attachment
```

**Status**:
```
is:unread
is:important
is:starred
```

### Common Patterns

**Pattern 1: Partnership Communications**
1. Search by domain: `from:@cnen.gov.br OR to:@cnen.gov.br newer_than:14d`
2. Read threads: `read_gmail_thread` for significant discussions
3. Extract key developments

**Pattern 2: Strategic Discussions**
1. Keyword search: `subject:(board OR strategy) newer_than:7d`
2. Executive search: `from:boardmember@email.com newer_than:14d`
3. Identify decisions and action items

## Google Drive Query Strategies

### Semantic Search
```javascript
google_drive_search(
    api_query="modifiedTime > '7 days ago'",
    semantic_query="strategic planning roadmap partnership"
)
```

### API Query Filters

**Time-Based**:
```
modifiedTime > '2025-11-08T00:00:00Z'
modifiedTime > '7 days ago'
createdTime > '2025-11-01T00:00:00Z'
```

**Content Type**:
```
mimeType = 'application/vnd.google-apps.document'
mimeType = 'application/pdf'
mimeType = 'application/vnd.google-apps.presentation'
```

**Name Matching**:
```
name contains 'Board'
name contains 'CNEN' and modifiedTime > '7 days ago'
```

### Combined Searches
```javascript
google_drive_search(
    api_query="modifiedTime > '7 days ago' and mimeType = 'application/vnd.google-apps.document'",
    semantic_query="partnership agreement proposal"
)
```

### Document Retrieval
```javascript
google_drive_fetch(
    document_ids=["DOC_ID_1", "DOC_ID_2"]
)
```

### Common Patterns

**Pattern 1: Recent Strategic Documents**
1. Broad search: semantic + recent modification
2. Fetch top results: `google_drive_fetch`
3. Extract strategic insights

**Pattern 2: Partnership Documents**
1. Search by name: `name contains 'CNEN'`
2. Semantic search: `partnership agreement contract`
3. Review most relevant

## Cross-Source Validation

### Pattern: Partnership Development

**Step 1 - Asana**: Find partnership project and status
**Step 2 - Gmail**: Find recent communications
**Step 3 - Google Drive**: Find formal documents
**Step 4 - Cross-Reference**: Build complete picture

Example:
- Asana shows project status (green/yellow/red)
- Gmail reveals recent discussions and decisions
- Drive contains formal agreements or proposals
- Combined = comprehensive partnership update

## Query Optimization

### Efficiency Tips

1. **Use Typeahead First**: Faster than full searches
2. **Limit Result Sets**: Don't retrieve more than needed (limit=50)
3. **Use Specific Date Ranges**: Narrow time windows
4. **Paginate When Necessary**: For large result sets

### Quality Over Quantity

Better to:
- Get full details on 5 critical partnerships
- Read 10 important Gmail threads completely
- Fetch 3 strategic Drive documents

Than to:
- List 50 projects without context
- Show 100 email subject lines
- Return 30 Drive file names

### When to Stop Searching

Stop additional searches when:
- You have clear picture of strategic position
- Major partnerships are covered with context
- Team composition is understood
- Critical decisions are identified
- Timeline of upcoming events is complete

## Troubleshooting

**Issue: No Results**
- Check workspace/account ID is correct
- Verify date filters aren't too restrictive
- Try broader search terms

**Issue: Too Many Results**
- Add time filters (newer_than:7d)
- Combine multiple conditions (AND)
- Exclude noise (-from:noreply)

**Issue: Results Not Relevant**
- Refine semantic query
- Add API query filters
- Try different keyword combinations

**Issue: Missing Expected Information**
- Check all three sources (might be in different location)
- Expand time window
- Search by person involved
- Check archived projects

## Summary: Query Best Practices

1. **Start Broad**: General searches first, then refine
2. **Cross-Reference**: Check all three sources for complete picture
3. **Validate Results**: Confirm relevance before using
4. **Depth Over Breadth**: Better to deeply understand 5 items than superficially know 50
5. **Combine Strategies**: Use multiple search approaches
6. **Time-Box Searches**: Don't search endlessly; focus on synthesis
7. **Document Gaps**: Note what's missing rather than fabricating

Remember: The goal is strategic intelligence, not comprehensive data collection. Query efficiently to support executive decision-making.
