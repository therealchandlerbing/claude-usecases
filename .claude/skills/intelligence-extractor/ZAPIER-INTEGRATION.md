# Zapier Integration Guide
## Automated Intelligence Extraction from Meeting Transcripts

This guide shows how to automate intelligence extraction using Zapier to connect Fathom transcripts → Claude → Asana intelligence databases.

---

## Overview

**Manual Workflow:**
Meeting → Transcript → You read it → Extract intelligence → Create Asana tasks

**Automated Workflow:**
Meeting → Transcript → Zapier detects → Claude extracts → Asana tasks created → You review

**Time saved:** 15-20 minutes per meeting
**Quality:** Consistent, comprehensive, no missed intelligence

---

## Prerequisites

- Zapier account (Professional plan recommended for multi-step workflows)
- Claude API key (anthropic.com)
- Google Drive (where Fathom saves transcripts)
- Asana account with projects set up (see ASANA-SETUP.md)

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    1. TRIGGER SOURCE                             │
│                                                                  │
│  Fathom saves transcript → Google Drive folder                  │
│  "A - Meeting Transcript Processing"                            │
└───────────────────────────┬──────────────────────────────────────┘
                            │
                            v
┌─────────────────────────────────────────────────────────────────┐
│                 2. ZAPIER DETECTS NEW FILE                       │
│                                                                  │
│  Trigger: New File in Folder                                    │
│  Action: Read file contents                                     │
└───────────────────────────┬──────────────────────────────────────┘
                            │
                            v
┌─────────────────────────────────────────────────────────────────┐
│                3. ROUTE TO CLAUDE API                            │
│                                                                  │
│  Determine meeting type (from filename or calendar)             │
│  Select appropriate extraction template                         │
│  Send transcript + template to Claude                           │
└───────────────────────────┬──────────────────────────────────────┘
                            │
                            v
┌─────────────────────────────────────────────────────────────────┐
│                 4. PARSE CLAUDE RESPONSE                         │
│                                                                  │
│  Extract JSON from Claude's output                              │
│  Validate JSON structure                                        │
│  Route by intelligence type (partnership/funding/stakeholder)   │
└───────────────────────────┬──────────────────────────────────────┘
                            │
                            v
┌─────────────────────────────────────────────────────────────────┐
│              5. CREATE/UPDATE ASANA TASKS                        │
│                                                                  │
│  Search for existing tasks (avoid duplicates)                   │
│  Create new tasks OR update existing with new intelligence      │
│  Set custom fields from extracted data                          │
│  Add subtasks for next actions                                  │
└───────────────────────────┬──────────────────────────────────────┘
                            │
                            v
┌─────────────────────────────────────────────────────────────────┐
│                    6. LOG QUALITY DATA                           │
│                                                                  │
│  Create quality tracking entry                                  │
│  Log extraction metadata for feedback loop                      │
└─────────────────────────────────────────────────────────────────┘
```

---

## Zap 1: Meeting Transcript Intelligence Extraction

### Step 1: Trigger - New File in Google Drive

**App:** Google Drive
**Event:** New File in Folder
**Folder:** `A - Meeting Transcript Processing`
**File Type:** `.txt` or `.docx`

**Test:** Upload a sample transcript and verify Zapier detects it

---

### Step 2: Read File Contents

**App:** Google Drive
**Action:** Get File Content
**File:** Use file from Step 1

**Output:** File text content

---

### Step 3: Determine Meeting Type (Optional Intelligence)

**App:** Code by Zapier (JavaScript)

**Purpose:** Automatically detect meeting type from filename or calendar metadata to select the right extraction template.

**Code:**
```javascript
// Input from previous steps
const fileName = inputData.fileName; // e.g., "2025-03-10 - InovaEduK Partnership Exploration.txt"
const fileContent = inputData.fileContent;

// Simple keyword-based meeting type detection
function detectMeetingType(fileName, content) {
  const lowerName = fileName.toLowerCase();
  const lowerContent = content.toLowerCase().substring(0, 500); // First 500 chars

  // Check filename first
  if (lowerName.includes('partnership') || lowerName.includes('partner exploration')) {
    if (lowerName.includes('check-in') || lowerName.includes('follow-up')) {
      return 'partnership-existing';
    }
    return 'partnership-new';
  }

  if (lowerName.includes('funder') || lowerName.includes('foundation') || lowerName.includes('grant')) {
    if (lowerName.includes('application') || lowerName.includes('proposal')) {
      return 'funder-application';
    }
    return 'funder-initial';
  }

  if (lowerName.includes('board') || lowerName.includes('governance')) {
    return 'board-meeting';
  }

  if (lowerName.includes('client') || lowerName.includes('sprint')) {
    return 'client-sprint';
  }

  // Check content if filename unclear
  if (lowerContent.includes('first meeting') || lowerContent.includes('initial conversation')) {
    if (lowerContent.includes('fund') || lowerContent.includes('grant')) {
      return 'funder-initial';
    }
    return 'partnership-new';
  }

  // Default
  return 'general';
}

const meetingType = detectMeetingType(fileName, fileContent);

return {
  meetingType: meetingType,
  fileName: fileName
};
```

**Output:** `meetingType` (partnership-new, funder-initial, etc.)

---

### Step 4: Call Claude API - Intelligence Extraction

**App:** Webhooks by Zapier (or Code by Zapier)
**Method:** POST
**URL:** `https://api.anthropic.com/v1/messages`

**Headers:**
```
Content-Type: application/json
x-api-key: YOUR_CLAUDE_API_KEY
anthropic-version: 2023-06-01
```

**Body (JSON):**
```json
{
  "model": "claude-sonnet-4-20250514",
  "max_tokens": 4000,
  "messages": [
    {
      "role": "user",
      "content": "You are using the intelligence-extractor skill.\n\nMeeting Type: {{meetingType from Step 3}}\n\nExtract partnership, funding, and stakeholder intelligence from this meeting transcript. Use the appropriate template for the meeting type.\n\nTranscript:\n{{fileContent from Step 2}}\n\nOutput valid JSON only."
    }
  ]
}
```

**Alternative (if using Code by Zapier for more control):**
```javascript
const axios = require('axios');

const meetingType = inputData.meetingType;
const transcript = inputData.fileContent;
const fileName = inputData.fileName;

// Build context-aware prompt
let prompt = `You are using the intelligence-extractor skill.\n\n`;
prompt += `Meeting Type: ${meetingType}\n`;
prompt += `Source: ${fileName}\n\n`;
prompt += `Extract partnership, funding, and stakeholder intelligence from this meeting transcript.\n\n`;

// Add template-specific guidance based on meeting type
if (meetingType === 'partnership-new') {
  prompt += `This is a NEW partnership exploration meeting. Focus on:\n`;
  prompt += `- Opening opportunities and pain points\n`;
  prompt += `- Cultural communication patterns\n`;
  prompt += `- Decision process intelligence\n`;
  prompt += `- Relationship-building pace\n\n`;
} else if (meetingType === 'funder-initial') {
  prompt += `This is an INITIAL funder conversation. Focus on:\n`;
  prompt += `- Program fit assessment\n`;
  prompt += `- Decision process intelligence\n`;
  prompt += `- Application strategy\n`;
  prompt += `- Relationship building with program officer\n\n`;
}

prompt += `Transcript:\n${transcript}\n\n`;
prompt += `Output valid JSON using the intelligence extraction schemas.`;

const response = await axios.post(
  'https://api.anthropic.com/v1/messages',
  {
    model: 'claude-sonnet-4-20250514',
    max_tokens: 4000,
    messages: [{ role: 'user', content: prompt }]
  },
  {
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': process.env.CLAUDE_API_KEY, // Set in Zapier environment
      'anthropic-version': '2023-06-01'
    }
  }
);

return {
  claude_response: response.data.content[0].text
};
```

**Output:** Claude's response with JSON extraction

---

### Step 5: Parse JSON Response

**App:** Code by Zapier

**Code:**
```javascript
const claudeResponse = inputData.claude_response;

// Extract JSON from markdown code blocks if present
let jsonText = claudeResponse;

// Remove markdown code blocks
jsonText = jsonText.replace(/```json\n?/g, '');
jsonText = jsonText.replace(/```\n?/g, '');
jsonText = jsonText.trim();

try {
  const intelligence = JSON.parse(jsonText);

  // Validate structure
  if (!intelligence.intelligence_items || !Array.isArray(intelligence.intelligence_items)) {
    throw new Error('Invalid intelligence structure - missing intelligence_items array');
  }

  return {
    success: true,
    intelligence: intelligence,
    itemCount: intelligence.intelligence_items.length,
    flaggedCount: intelligence.flagged_for_review ? intelligence.flagged_for_review.length : 0
  };

} catch (error) {
  return {
    success: false,
    error: error.message,
    rawResponse: claudeResponse.substring(0, 500) // First 500 chars for debugging
  };
}
```

**Output:** Parsed intelligence object

---

### Step 6: Filter - Check Parse Success

**App:** Filter by Zapier

**Condition:** `success` (from Step 5) is `true`

**Purpose:** Only continue if JSON parsed successfully. Failed parses should be logged and alerted.

---

### Step 7: Loop Through Intelligence Items

**App:** Looping by Zapier (or multiple Paths)

**Loop Over:** `intelligence.intelligence_items` from Step 5

**For Each Item:**
- Extract item type (partnership/funding/stakeholder)
- Route to appropriate Asana project
- Search for existing or create new

---

### Step 8a: Partnership Intelligence → Asana

**Condition:** Intelligence item type = "partnership"

#### Action 8a.1: Search for Existing Partnership Task

**App:** Asana
**Action:** Find Task
**Project:** Partnership Intelligence Hub
**Search:** Task name contains `{{organization_name}}`

**Output:** Existing task ID or null

#### Action 8a.2: Path Split

**Path A:** Existing task found → Update it
**Path B:** No existing task → Create new

#### Path A: Update Existing Partnership

**App:** Asana
**Action:** Add Comment to Task
**Task:** From search result
**Comment:**
```
🤖 Intelligence Update from {{source_date}}

**Interaction Notes:**
{{interaction_notes}}

**Opening Opportunities (new insights):**
{{opening_opportunities joined with newlines}}

**Next Actions:**
{{next_actions joined with newlines}}

**Suggested Custom Field Updates:**
- Relationship Temperature: {{relationship_temperature}}
- Stage Health: On Track
- Last Interaction: {{today}}

Review and update task as needed.
```

#### Path B: Create New Partnership Task

**App:** Asana
**Action:** Create Task
**Project:** Partnership Intelligence Hub
**Section:** Active Exploration
**Task Name:** `{{organization_name}} - {{partnership_type}} - {{primary_contact}}`

**Description:** (Use partnership template populated with extracted data)

**Custom Fields:**
- Partnership Type: `{{partnership_type}}`
- Relationship Temperature: `{{relationship_temperature}}`
- Cultural Approach: `{{cultural_approach}}`
- Decision Timeline: `{{decision_timeline}}`
- Primary Owner: `{{relationship_owner}}`
- Last Interaction: `{{today}}`
- Auto-Created: `true`

**Assignee:** `{{relationship_owner}}`

#### Action 8a.3: Create Subtasks for Next Actions

**App:** Asana
**Action:** Create Subtask (loop through next_actions array)
**Parent Task:** From Step 8a.2
**Subtask Name:** `{{next_action}}`
**Assignee:** `{{relationship_owner}}`

---

### Step 8b: Funding Intelligence → Asana

**Condition:** Intelligence item type = "funding"

#### Action 8b.1: Search for Existing Funding Task

**App:** Asana
**Action:** Find Task
**Project:** Funding Opportunity Intelligence
**Search:** Task name contains `{{funder_name}}`

#### Action 8b.2: Path Split (Update vs. Create)

Similar logic to partnership...

#### Path A: Update Existing Funding Task
(Add comment with new intelligence)

#### Path B: Create New Funding Task
**Task Name:** `{{funder_name}} - {{program_name}} - {{year}}`
**Section:** Research Stage
**Custom Fields:** Populate from extraction
**Description:** Use funding template

---

### Step 8c: Stakeholder Intelligence → Asana

**Condition:** Intelligence item type = "stakeholder"

#### Action 8c.1: Search for Existing Stakeholder Profile

**App:** Asana
**Action:** Find Task
**Project:** Stakeholder Intelligence Database
**Search:** Task name contains `{{full_name}}`

#### Action 8c.2: Update or Create

Similar pattern...

**Create New:**
**Task Name:** `{{full_name}} - {{title_role, organization}} - {{stakeholder_type}}`
**Section:** Based on stakeholder_type
**Custom Fields:** Populate from extraction

---

### Step 9: Log Quality Data

**App:** Google Sheets (or Asana task in Quality Tracking project)

**Action:** Create Spreadsheet Row
**Spreadsheet:** "Intelligence Extraction Quality Log"

**Data:**
- Extraction ID: `{{zap_run_id}}`
- Date: `{{today}}`
- Source File: `{{fileName}}`
- Meeting Type: `{{meetingType}}`
- Entities Created: `{{itemCount}}`
- Entities Flagged: `{{flaggedCount}}`
- Confidence Levels: `{{array of confidence values}}`
- Processing Time: `{{timestamp difference}}`

---

### Step 10: Notification (Optional)

**App:** Slack (or Email)

**Condition:** Only if `flaggedCount > 0` or `confidence contains "low"`

**Message:**
```
🤖 Intelligence Extracted from: {{fileName}}

✅ Created/Updated: {{itemCount}} entities
⚠️ Flagged for review: {{flaggedCount}} items

{{#if flaggedCount > 0}}
Items needing review:
{{flagged_for_review items with reasons}}
{{/if}}

View in Asana:
[Links to created tasks]
```

---

## Zap 2: Email Thread Intelligence Extraction (Optional)

### Trigger: New Email Label

**App:** Gmail
**Event:** New Labeled Email
**Label:** "Intelligence Worthy" (you manually label important threads)

### Similar Steps:
1. Get email thread
2. Format for Claude
3. Extract intelligence
4. Create/update Asana tasks

---

## Error Handling

### Failed JSON Parse

**Zap Path:**
```
If parse fails →
  Log to "Failed Extractions" Google Sheet →
  Notify via Slack →
  Attach raw Claude response for manual review
```

### Asana API Errors

**Retry Logic:**
```
Try Create Task →
  If fails (rate limit, network) →
    Wait 2 seconds →
    Retry (up to 3 times) →
      If still fails →
        Log to error sheet →
        Notify
```

### Claude API Errors

```
If Claude API fails →
  Check error type:
    - Rate limit → Delay 10 seconds, retry
    - Invalid request → Log and notify
    - Timeout → Retry with shorter prompt
```

---

## Testing Your Zap

### Test with Sample Transcript

1. Create a simple test transcript:
```
Meeting with John Smith from TestOrg
Date: March 15, 2025

First conversation about potential partnership. They work on education in Brazil.
John is CEO, very collaborative communication style. They're interested in our
systems-change approach. Next step: John will send their strategic plan.
```

2. Upload to trigger folder
3. Watch Zap run
4. Verify:
   - Claude extracts intelligence
   - JSON parses correctly
   - Asana task created
   - Custom fields populated
   - Quality data logged

### Iterate and Refine

- Check Asana task quality
- Adjust prompt if needed
- Refine field mappings
- Test edge cases (multiple entities, low confidence, etc.)

---

## Cost Estimation

**Per Meeting:**
- Claude API: ~5,000 input tokens + ~1,500 output tokens ≈ $0.10
- Zapier: ~10 tasks per meeting ≈ included in plan

**Monthly (40 meetings):**
- Claude API: ~$4
- Zapier: Professional plan supports this volume

**ROI:**
- Time saved: 40 meetings × 15 minutes = 10 hours/month
- Cost: $4/month
- Value: $4 for 10 hours of time = excellent ROI

---

## Optimization Tips

### Batch Processing

Instead of processing one transcript at a time, batch several:
- Trigger: Daily at 6am
- Check for all new transcripts from yesterday
- Process in batch
- Reduces Zap complexity

### Confidence-Based Routing

```
If confidence = "high":
  → Auto-create tasks

If confidence = "medium":
  → Auto-create but tag "Needs Verification"

If confidence = "low":
  → Don't auto-create
  → Send to review queue
```

### Smart Duplicate Detection

Use fuzzy matching for organization names:
```javascript
function similarity(s1, s2) {
  // Levenshtein distance or similar
  // Return similarity score 0-1
}

const existingTasks = await searchAsana(projectId);
const bestMatch = existingTasks.find(task =>
  similarity(task.name, newOrgName) > 0.85
);
```

---

## Maintenance

### Weekly
- Check "Failed Extractions" log
- Review quality metrics
- Adjust prompts if patterns emerge

### Monthly
- Analyze extraction quality trends
- Update templates based on feedback
- Optimize Zap performance

---

## Troubleshooting

### "No intelligence extracted"

**Cause:** Transcript too short or off-topic
**Fix:** Add filter step to check transcript length and keywords before sending to Claude

### "Duplicate tasks created"

**Cause:** Search not finding existing tasks
**Fix:** Improve search query (search by multiple fields, fuzzy matching)

### "Custom fields not populating"

**Cause:** Field name mismatch between Zapier and Asana
**Fix:** Verify exact custom field names in Asana, update Zap mappings

### "Claude response is not JSON"

**Cause:** Prompt ambiguity or model creativity
**Fix:** Make prompt more explicit: "Output ONLY valid JSON, no explanatory text"

---

## Advanced: Quality Feedback Loop

See separate documentation (quality-feedback-loop.md) for:
- Automated quality scoring
- User feedback capture
- Template improvement system
- A/B testing framework

---

## Getting Help

**Resources:**
- Zapier Community Forums
- Claude API Documentation
- Asana API Reference
- This repository's Issues

**Support:**
- Create task in "Intelligence System Improvements" Asana project
- Tag relevant team members

---

*Automation amplifies intelligence capture. Invest setup time once, benefit continuously.*
