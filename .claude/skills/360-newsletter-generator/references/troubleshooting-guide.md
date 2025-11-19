# Troubleshooting Guide

Common issues and solutions for newsletter generation.

## Overview

This guide covers:
1. Data collection problems
2. Content quality issues
3. Chart rendering problems
4. Format and design issues
5. Performance optimization

## Data Collection Issues

### Issue: No Data Returned from Asana

**Symptoms:**
- Empty or very sparse newsletter
- Missing expected projects
- No tasks found

**Possible Causes:**
1. Workspace GID incorrect
2. Project names changed
3. Date range too narrow
4. API permissions issue
5. Network connectivity problem

**Solutions:**

**Verify workspace access:**
```javascript
// Test workspace connection
Tool: asana_list_workspaces()
Expected: Should return 360socialventures.com with GID

// If wrong workspace:
Update workspace_gid in data-sources.json
```

**Find renamed projects:**
```javascript
// Use typeahead to find current name
Tool: asana_typeahead_search
Parameters:
  workspace_gid: [correct_gid]
  resource_type: "project"
  query: "Partner"  // Try partial name

// Update priority projects list with new names
```

**Expand date range:**
```
If "Generate newsletter for last week" returns no data:
Try: "Generate newsletter for last 2 weeks"
Or: "Generate newsletter for last month"
```

**Check API permissions:**
- Verify Asana integration is authorized
- Check that user has access to projects
- Confirm API key/token is valid

### Issue: No Data Returned from Gmail

**Symptoms:**
- Missing partnership communications
- No email content in newsletter
- Empty Gmail sections

**Possible Causes:**
1. Partner email domains changed
2. Search syntax errors
3. Date format incorrect
4. Too restrictive search
5. API permissions issue

**Solutions:**

**Update partner domains:**
```javascript
// If partner changed email domain
// Update in data-sources.json:
"key_partners": [
  {
    "name": "SpacePlan",
    "domain": "spaceplan.com",  // Update if changed
    ...
  }
]
```

**Verify search syntax:**
```javascript
// Gmail date format must be YYYY/MM/DD
Correct: after:2025/11/01
Wrong: after:2025-11-01

// Verify parentheses are balanced
Correct: from:(*@spaceplan.com OR *@genip.com)
Wrong: from:(*@spaceplan.com OR *@genip.com
```

**Broaden search:**
```javascript
// If too few results, remove some restrictions
Instead of: from:me (partnership AND agreement)
Try: from:me (partnership OR agreement)

// Or expand keyword list
Add: MOU, LOI, collaboration, alliance
```

**Check API permissions:**
- Verify Gmail API is enabled
- Confirm OAuth scopes include Gmail read
- Test with simple query to confirm access

### Issue: No Data Returned from Google Drive

**Symptoms:**
- Missing documents in newsletter
- No Drive-sourced metrics
- Empty document references

**Possible Causes:**
1. Date range too narrow (Drive modifiedTime filter)
2. Document naming conventions changed
3. Semantic search not finding relevant docs
4. API permissions issue
5. Documents not modified in period

**Solutions:**

**Expand date range:**
```javascript
// Drive searches are very date-sensitive
// Expand backward if needed
Instead of: modifiedTime > '2025-11-01T00:00:00Z'
Try: modifiedTime > '2025-10-01T00:00:00Z'
```

**Broaden search criteria:**
```javascript
// Add more name patterns
api_query: "name contains 'partnership' or
            name contains 'partner' or
            name contains 'agreement' or
            name contains 'collab'"

// Expand semantic query
semantic_query: "partnership agreements collaboration
                 deliverables reports updates meetings"
```

**Use fullText search:**
```javascript
// Search content, not just names
api_query: "fullText contains 'SpacePlan' and
            modifiedTime > '[date]'"
```

**Verify permissions:**
- Check Drive API is enabled
- Confirm user has access to documents
- Test with simple search to confirm connection

## Content Quality Issues

### Issue: Newsletter Seems Incomplete

**Symptoms:**
- Sections with very few stories
- Missing expected content
- Feels thin or sparse

**Diagnosis:**

**Check data collection results:**
```
How many items were found from each source?
- Asana: X completed tasks, Y modified tasks
- Gmail: X threads
- Drive: X documents

If any source returned 0-2 items, investigate that source.
```

**Review significance scoring:**
```
Are items being filtered out due to low scores?
Request: "Show all items regardless of score"
Or manually specify: "Include [specific project/partnership]"
```

**Verify date range:**
```
Is the date range appropriate?
- Holiday weeks may have less activity
- Vacation periods may be sparse
- Check if period is actually empty or data collection failed
```

**Solutions:**

**Expand date range:**
```
"Generate newsletter for last 2 weeks instead"
```

**Lower significance threshold:**
```
"Include medium-significance items (70+) in this newsletter"
```

**Manually add content:**
```
"Also include updates from [specific project]"
"Add information about [specific partnership]"
```

**Be transparent about sparse periods:**
```html
<div class="section-intro">
Light activity during Thanksgiving week. Focus this period on strategic
planning and relationship maintenance.
</div>
```

### Issue: Lead Story Doesn't Feel Right

**Symptoms:**
- Lead story is operational/routine
- More significant items buried in sections
- Lead doesn't reflect most important development

**Diagnosis:**

**Review significance scores:**
```
What scored highest? Why?
Is the scoring reflecting actual strategic importance?
```

**Check for modifiers:**
```
Did modifiers inflate a routine item's score?
Example: Routine task + international modifier = high score
But is it actually lead-worthy?
```

**Solutions:**

**Manual override:**
```
"Make [different item] the lead story instead"
"The lead story should be [specific development]"
```

**Adjust scoring for future:**
```
"In future newsletters, weight [category] higher/lower"
```

**Create composite lead:**
```
"Combine the SpacePlan and team updates into a single lead story"
```

### Issue: Wrong Section Assignment

**Symptoms:**
- Partnership update in Operations
- Impact story in Programs
- Strategic item in routine section

**Diagnosis:**

**Review content emphasis:**
```
What is the PRIMARY focus of this item?
- The partnership itself → Partnerships section
- The operational impact → Operations section
- The strategic implication → Strategy section
```

**Solutions:**

**Manually reassign:**
```
"Move the SpacePlan update to Partnerships section"
"This should be in Strategic Horizon, not Operations"
```

**Update section mapping:**
```
For future newsletters, adjust section_mapping in data-sources.json
to better categorize similar items
```

## Chart Rendering Problems

### Issue: Charts Not Displaying

**Symptoms:**
- Blank space where chart should be
- Canvas element present but no visualization
- Console errors about Chart.js

**Possible Causes:**
1. Chart.js CDN not loaded
2. JavaScript errors preventing execution
3. Canvas ID mismatch
4. Data format incorrect

**Solutions:**

**Verify Chart.js CDN:**
```html
<!-- Should be in <head> -->
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<!-- Check browser console for load errors -->
```

**Check canvas ID:**
```html
<!-- Canvas element -->
<canvas id="pipelineChart"></canvas>

<!-- JavaScript must match -->
<script>
  const ctx = document.getElementById('pipelineChart').getContext('2d');
  // ID must match exactly
</script>
```

**Validate data format:**
```javascript
// Data must be array of numbers
data: [15, 25, 30, 20]  // ✓ Correct

data: ['15', '25', '30', '20']  // ✗ Wrong (strings)
data: [null, 25, 30, 20]  // ✗ Wrong (null)
```

**Check for JavaScript errors:**
```
Open browser console (F12)
Look for red error messages
Fix syntax errors or undefined variables
```

### Issue: Chart Data Incorrect

**Symptoms:**
- Chart shows wrong numbers
- Data doesn't match text in newsletter
- Placeholder values instead of real data

**Diagnosis:**

**Verify data source:**
```
Are chart values calculated from actual collected data?
Or are they example/placeholder values?
```

**Check calculation logic:**
```javascript
// Example: Partnership pipeline
// Should count actual tasks per stage
// Not use hardcoded example values

// Wrong:
data: [10, 20, 30, 15]  // Example values

// Right:
data: [
  discoveryCount,    // From actual Asana data
  scopingCount,      // From actual Asana data
  activeCount,       // From actual Asana data
  renewalCount       // From actual Asana data
]
```

**Solutions:**

**Recalculate from source data:**
```
"Regenerate charts with actual data from Asana/Gmail/Drive"
```

**Show calculation:**
```
"Show me how the partnership pipeline chart data was calculated"
```

**Use fallback if data insufficient:**
```
Replace chart with stat card or text summary if real data unavailable
```

### Issue: Too Many/Few Data Points

**Symptoms:**
- Chart overcrowded with segments
- Chart too sparse (only 1-2 points)
- Labels overlapping and unreadable

**Solutions:**

**Too many segments (>8):**
```javascript
// Group smaller segments into "Other"
const topSegments = data.sort().slice(0, 7);
const otherSum = data.slice(7).reduce((a, b) => a + b, 0);
const finalData = [...topSegments, otherSum];
const finalLabels = [...topLabels, 'Other'];
```

**Too few segments (<2):**
```
Replace chart with stat card or text description
Don't force a chart when data is insufficient
```

**Overlapping labels:**
```javascript
// Rotate labels
options: {
  scales: {
    x: {
      ticks: {
        maxRotation: 45,
        minRotation: 45
      }
    }
  }
}

// Or use shorter labels
labels: ['NA', 'LATAM', 'EU', 'APAC', 'Other']
// Instead of: ['North America', 'Latin America', ...]
```

## Format and Design Issues

### Issue: Em Dashes Appearing (—)

**Symptoms:**
- Em dashes in content
- Formatting issues in text
- Print/export problems

**Solution:**

**Find and replace all em dashes:**
```
Search for: —
Replace with: , (comma) or . (period) or ( ) (parentheses)

Examples:
"The deal — structured as..." → "The deal, structured as..."
"Revenue — $1.2M — exceeds..." → "Revenue ($1.2M) exceeds..."
```

**Prevention:**
```
During writing, never use em dash
Always use alternatives from style guide
```

### Issue: Inline Stats Not Styled

**Symptoms:**
- Numbers don't stand out
- Metrics look like regular text
- Visual hierarchy unclear

**Solution:**

**Wrap all metrics in span:**
```html
<!-- Wrong -->
The partnership represents $1.2M in pipeline.

<!-- Right -->
The partnership represents <span class="inline-stat">$1.2M</span> in pipeline.

<!-- Multiple stats -->
We served <span class="inline-stat">280 founders</span> across
<span class="inline-stat">16 countries</span>.
```

### Issue: Status Badges Missing

**Symptoms:**
- No visual urgency indicators
- Action items don't stand out
- Critical items overlooked

**Solution:**

**Add appropriate badges:**
```html
<div class="card-header">
  <div class="card-title">Important Partnership Update</div>
  <span class="status-chip status-action">
    <i class="fas fa-clock"></i> Action Required
  </span>
</div>
```

**Badge criteria:**
- Critical: Red, deadline ≤3 days
- Action Required: Yellow, deadline ≤2 weeks
- Monitoring: Gray, watching situation
```

## Performance Issues

### Issue: Newsletter Generation Too Slow

**Symptoms:**
- Takes >2 minutes to generate
- User waiting too long
- Timeout errors

**Diagnosis:**

**Check number of API calls:**
```
Standard weekly should be ~10-12 calls total
If significantly more, optimize:
```

**Solutions:**

**Run queries in parallel:**
```javascript
// Instead of sequential:
await asanaProject1();
await asanaProject2();
await asanaProject3();

// Do parallel:
await Promise.all([
  asanaProject1(),
  asanaProject2(),
  asanaProject3()
]);
```

**Reduce data collection scope:**
```
Focus on fewer projects for faster generation
Prioritize highest-priority data sources
Skip optional searches if time-constrained
```

**Use appropriate page sizes:**
```javascript
// Don't request more than needed
page_size: 20  // Usually sufficient

// Not:
page_size: 100  // Slower, rarely necessary
```

### Issue: Rate Limiting Errors

**Symptoms:**
- API errors about too many requests
- Some queries failing
- Incomplete data collection

**Solutions:**

**Add delays between calls:**
```javascript
// Wait between sequential calls
await apiCall1();
await sleep(100);  // 100ms delay
await apiCall2();
```

**Reduce query volume:**
```
Prioritize essential projects
Skip optional searches
Cache results where appropriate
```

**Batch queries:**
```javascript
// One search across multiple projects
projects_any: [proj1_gid, proj2_gid, proj3_gid]

// Instead of 3 separate searches
```

## Edge Cases

### Issue: Holiday/Vacation Period

**Situation:**
- Very little activity in period
- Sparse data across all sources
- Newsletter feels empty

**Solution:**

**Be transparent:**
```html
<div class="executive-summary">
  <p><strong>Note:</strong> Light activity during holiday week.
  Focus on strategic planning and upcoming priorities.</p>
</div>
```

**Focus on forward-looking:**
```
Emphasize Strategic Horizon section
Show what's coming up
Preview next period's priorities
```

**Combine with longer period:**
```
"Generate newsletter covering last 2 weeks to include pre-holiday activity"
```

### Issue: Sensitive Information

**Situation:**
- Partnership information is confidential
- Financial data not ready to share
- Team changes not yet announced

**Solution:**

**Discretion levels:**
```
Confidential: Omit entirely or use vague reference
  "Advanced discussions with international partner"

Private: Include with limited details
  "Partnership scoping completed, pending board approval"

Public: Full details appropriate
  "SpacePlan joint venture formalized with signed MOU"
```

**Manual redaction:**
```
"Generate newsletter but keep SpacePlan partnership details vague"
"Don't include specific financial numbers, just trends"
```

### Issue: Multiple Newsletters Requested

**Situation:**
- Need both weekly team newsletter and monthly board brief
- Different audiences, different emphasis
- Want to compare periods

**Solution:**

**Generate sequentially with clear parameters:**
```
1. "Generate weekly newsletter for Nov 4-10 for team"
2. "Generate monthly newsletter for October for board meeting"
3. "Compare the two and highlight key differences"
```

**Maintain separate contexts:**
```
Each newsletter is independent
Don't mix data between them unless explicitly comparing
```

## Getting Help

If issue persists:

1. **Describe specifically:**
   - What you requested
   - What you expected
   - What you got instead
   - Any error messages

2. **Share context:**
   - Date range used
   - Newsletter type (weekly/monthly/custom)
   - Which sections are affected
   - What data sources returned results

3. **Try simplest case first:**
   - Generate with minimal date range
   - Focus on single section
   - Test each data source independently
   - Isolate the problem

4. **Check configuration:**
   - Review data-sources.json for accuracy
   - Verify priority projects list is current
   - Confirm partner domains are correct
   - Check custom field names haven't changed

---

**Related Guides:**
- [Data Collection Guide](data-collection-guide.md) - For data source issues
- [Content Analysis Framework](content-analysis-framework.md) - For scoring/section issues
- [Chart Specifications](chart-specifications.md) - For chart problems
- [Writing Style Guide](writing-style-guide.md) - For formatting issues
