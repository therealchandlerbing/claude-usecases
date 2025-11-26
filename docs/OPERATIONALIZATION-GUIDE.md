# Operationalization Guide

**Making Your Intelligence System Live and Useful**

This guide walks you through the complete setup to make your claude-usecases repository operational with live data flowing from meetings to your dashboard.

---

## Quick Overview

```
Meeting (Fathom)
    ↓
Google Drive (A - Meeting Transcript Processing)
    ↓
Zapier (detects new file)
    ↓
Claude API (intelligence-extractor skill)
    ↓
Zapier (parses response)
    ↓
Supabase (stores extraction metrics)     →     Dashboard (displays metrics)
    ↓
Asana (stores actual intelligence)
```

---

## Your Configuration

| Component | Value |
|-----------|-------|
| **Google Drive Folder** | `A - Meeting Transcript Processing` |
| **Folder ID** | `1asWprM3W64cjz8HEoI7NA55mtAegFQWI` |
| **Supabase URL** | `https://pblxazslxcotbdxtvnlb.supabase.co` |
| **Supabase Anon Key** | `sb_publishable_mCH6Oiq63NdZAeOct2c80w_v8hHwsuS` |
| **Fathom Webhook** | `whsec_fMhJjCKZKrrw459/lsgdeswf5VeoWqGt` |

---

## Step 1: Deploy Supabase Schema (5 minutes)

### 1.1 Open Supabase SQL Editor

1. Go to https://supabase.com/dashboard
2. Select your project (`pblxazslxcotbdxtvnlb`)
3. Click **SQL Editor** in the left sidebar
4. Click **New query**

### 1.2 Run the Schema

Copy the entire contents of this file and paste into the SQL editor:

```
intelligence-dashboard/supabase-schema.sql
```

Click **Run** to execute.

### 1.3 Verify Tables Created

Go to **Table Editor** and confirm these tables exist:
- [ ] `extractions`
- [ ] `experiments`
- [ ] `edits`
- [ ] `weekly_analyses`

### 1.4 Enable Realtime

1. Go to **Database** > **Replication**
2. Ensure `extractions` table has realtime enabled
3. Or run this SQL:
   ```sql
   ALTER PUBLICATION supabase_realtime ADD TABLE extractions;
   ```

---

## Step 2: Set Up Zapier Workflow (20 minutes)

### 2.1 Create New Zap

1. Go to https://zapier.com
2. Click **Create** > **New Zap**
3. Name it: "Meeting Transcript → Intelligence Extraction → Supabase"

### 2.2 Step 1: Trigger - Google Drive

**App:** Google Drive
**Event:** New File in Folder
**Folder:** `A - Meeting Transcript Processing`
**File Types:** `.txt`, `.docx`

Test this step - it should find a file in your folder.

### 2.3 Step 2: Get File Contents

**App:** Google Drive
**Event:** Get File Contents
**File:** Use file from Step 1

### 2.4 Step 3: Detect Meeting Type (Code by Zapier)

**App:** Code by Zapier
**Event:** Run JavaScript

**Input Data:**
- `fileName`: File Name from Step 1
- `fileContent`: File Contents from Step 2

**Code:**
```javascript
const fileName = inputData.fileName || '';
const fileContent = inputData.fileContent || '';

function detectMeetingType(fileName, content) {
  const lowerName = fileName.toLowerCase();
  const lowerContent = content.toLowerCase().substring(0, 500);

  if (lowerName.includes('partnership') || lowerName.includes('partner')) {
    if (lowerName.includes('check-in') || lowerName.includes('follow-up')) {
      return 'partnership-existing';
    }
    return 'partnership-new';
  }

  if (lowerName.includes('funder') || lowerName.includes('foundation') || lowerName.includes('grant')) {
    return 'funder-initial';
  }

  if (lowerName.includes('board') || lowerName.includes('governance')) {
    return 'board-meeting';
  }

  if (lowerName.includes('client') || lowerName.includes('sprint')) {
    return 'client-sprint';
  }

  if (lowerContent.includes('fund') || lowerContent.includes('grant')) {
    return 'funder-initial';
  }

  return 'general';
}

return {
  meetingType: detectMeetingType(fileName, fileContent),
  fileName: fileName,
  extractionId: 'ext_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9)
};
```

### 2.5 Step 4: Call Claude API (Webhooks)

**App:** Webhooks by Zapier
**Event:** POST

**URL:** `https://api.anthropic.com/v1/messages`

**Headers:**
```
Content-Type: application/json
x-api-key: YOUR_CLAUDE_API_KEY
anthropic-version: 2023-06-01
```

**Data (Raw JSON):**
```json
{
  "model": "claude-sonnet-4-20250514",
  "max_tokens": 4000,
  "messages": [
    {
      "role": "user",
      "content": "You are using the intelligence-extractor skill from 360 Social Impact Studios.\n\nMeeting Type: {{Step 3 meetingType}}\nSource File: {{Step 1 File Name}}\nExtraction ID: {{Step 3 extractionId}}\n\nExtract partnership, funding, and stakeholder intelligence from this meeting transcript.\n\nIMPORTANT: Output ONLY valid JSON with this structure:\n{\n  \"extraction_summary\": \"Brief summary\",\n  \"intelligence_items\": [...],\n  \"flagged_for_review\": [...],\n  \"extraction_metadata\": {\n    \"completeness_score\": 0-100,\n    \"confidence_level\": \"high|medium|low\",\n    \"entities_created\": number,\n    \"auto_quality_rating\": \"excellent|good|fair|poor\"\n  }\n}\n\nTranscript:\n{{Step 2 File Contents}}"
    }
  ]
}
```

### 2.6 Step 5: Parse Claude Response (Code by Zapier)

**App:** Code by Zapier
**Event:** Run JavaScript

**Input Data:**
- `claudeResponse`: Content from Step 4
- `extractionId`: extractionId from Step 3
- `fileName`: fileName from Step 3
- `meetingType`: meetingType from Step 3

**Code:**
```javascript
const claudeResponse = inputData.claudeResponse || '';
const startTime = Date.now();

// Extract JSON from markdown code blocks if present
let jsonText = claudeResponse;
jsonText = jsonText.replace(/```json\n?/g, '');
jsonText = jsonText.replace(/```\n?/g, '');
jsonText = jsonText.trim();

try {
  const parsed = JSON.parse(jsonText);
  const metadata = parsed.extraction_metadata || {};
  const items = parsed.intelligence_items || [];

  // Count by type
  let partnerships = 0, funders = 0, stakeholders = 0;
  let highConf = 0, medConf = 0, lowConf = 0;

  items.forEach(item => {
    if (item.type === 'partnership') partnerships++;
    if (item.type === 'funding') funders++;
    if (item.type === 'stakeholder') stakeholders++;
    if (item.confidence === 'high') highConf++;
    if (item.confidence === 'medium') medConf++;
    if (item.confidence === 'low') lowConf++;
  });

  return {
    success: true,
    extraction_id: inputData.extractionId,
    source_file_name: inputData.fileName,
    meeting_type: inputData.meetingType,

    entities_created: items.length,
    partnerships_count: partnerships,
    funders_count: funders,
    stakeholders_count: stakeholders,

    completeness_score: metadata.completeness_score || 75,
    confidence_level: metadata.confidence_level || 'medium',
    confidence_high_count: highConf,
    confidence_medium_count: medConf,
    confidence_low_count: lowConf,

    auto_quality_rating: metadata.auto_quality_rating || 'good',
    flagged_for_review: (parsed.flagged_for_review || []).length > 0,
    flagged_count: (parsed.flagged_for_review || []).length,

    extraction_summary: parsed.extraction_summary || '',
    intelligence_data: JSON.stringify(parsed),

    processing_time: (Date.now() - startTime) / 1000,
    parsing_valid: true
  };

} catch (error) {
  return {
    success: false,
    extraction_id: inputData.extractionId,
    source_file_name: inputData.fileName,
    meeting_type: inputData.meetingType,
    error: error.message,
    raw_response: claudeResponse.substring(0, 500),
    parsing_valid: false
  };
}
```

### 2.7 Step 6: Filter - Only Continue on Success

**App:** Filter by Zapier

**Condition:** `success` from Step 5 equals `true`

### 2.8 Step 7: Send to Supabase (Code by Zapier)

**App:** Code by Zapier
**Event:** Run JavaScript

**Input Data:** (map all fields from Step 5)
- `extraction_id`
- `source_file_name`
- `meeting_type`
- `entities_created`
- `completeness_score`
- `confidence_level`
- `confidence_high_count`
- `confidence_medium_count`
- `confidence_low_count`
- `auto_quality_rating`
- `flagged_for_review`
- `extraction_summary`
- `intelligence_data`
- `processing_time`
- `parsing_valid`

**Code:**
```javascript
const SUPABASE_URL = 'https://pblxazslxcotbdxtvnlb.supabase.co';
// Use service role key for server-side Zapier operations (bypasses RLS)
const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBibHhhenNseGNvdGJkeHR2bmxiIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2NDEwMjIxOCwiZXhwIjoyMDc5Njc4MjE4fQ.YRi8Uut8X1je7cmEDgcxffrsDNG-BHQyZWYa1W14sUU';

const extractionData = {
  extraction_id: inputData.extraction_id,
  source_file_name: inputData.source_file_name,
  meeting_type: inputData.meeting_type,
  template_name: 'intelligence-extractor',
  template_version: '1.0.0',
  entities_created: parseInt(inputData.entities_created) || 0,
  items_extracted: parseInt(inputData.entities_created) || 0,
  completeness_score: parseInt(inputData.completeness_score) || null,
  confidence_level: inputData.confidence_level,
  confidence_high_count: parseInt(inputData.confidence_high_count) || 0,
  confidence_medium_count: parseInt(inputData.confidence_medium_count) || 0,
  confidence_low_count: parseInt(inputData.confidence_low_count) || 0,
  auto_quality_rating: inputData.auto_quality_rating,
  flagged_for_review: inputData.flagged_for_review === 'true',
  extraction_summary: inputData.extraction_summary,
  intelligence_data: inputData.intelligence_data ? JSON.parse(inputData.intelligence_data) : null,
  processing_time_seconds: parseFloat(inputData.processing_time) || null,
  parsing_valid: inputData.parsing_valid === 'true'
};

try {
  const response = await fetch(`${SUPABASE_URL}/rest/v1/extractions`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'apikey': SUPABASE_KEY,
      'Authorization': `Bearer ${SUPABASE_KEY}`,
      'Prefer': 'return=representation'
    },
    body: JSON.stringify(extractionData)
  });

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`Supabase error: ${response.status} - ${errorText}`);
  }

  const result = await response.json();

  return {
    success: true,
    supabase_id: result[0].id,
    created_at: result[0].created_at,
    message: 'Saved to Supabase successfully'
  };

} catch (error) {
  return {
    success: false,
    error: error.message,
    extraction_id: inputData.extraction_id
  };
}
```

### 2.9 Step 8 (Optional): Slack Notification

**App:** Slack
**Event:** Send Channel Message

**Condition:** Only if `flagged_for_review` is true or you want all notifications

**Message:**
```
Intelligence extracted from: {{Step 5 source_file_name}}

Entities: {{Step 5 entities_created}}
Quality: {{Step 5 auto_quality_rating}}
Completeness: {{Step 5 completeness_score}}%

{{#if Step 5 flagged_for_review}}Review needed for flagged items{{/if}}
```

---

## Step 3: Test the Pipeline (10 minutes)

### 3.1 Create Test Transcript

Create a file named `2025-11-26 - Test Partnership Exploration.txt`:

```
Meeting with John Smith from TestOrg
Date: November 26, 2025
Participants: Chandler Lewis (360), John Smith (TestOrg CEO)

First conversation about potential partnership. TestOrg works on education technology in Brazil.

John mentioned they're looking for strategic partners who understand systems-change approaches.
They have a 6-month decision timeline. Very collaborative communication style.

Their main pain point is scaling impact measurement.

Next steps:
1. John will send their strategic plan by December 5
2. Schedule follow-up call for mid-December
3. Chandler to send 360 case studies

John seemed warm to partnership - relationship temperature: warming.
```

### 3.2 Upload to Google Drive

1. Go to your Google Drive
2. Navigate to `A - Meeting Transcript Processing` folder
3. Upload the test file

### 3.3 Watch Zapier Execute

1. Go to Zapier > Zap History
2. Watch the zap run through all steps
3. Check for any errors

### 3.4 Verify in Supabase

1. Go to Supabase > Table Editor > `extractions`
2. Confirm new row was created
3. Check the data looks correct

### 3.5 Check Your Dashboard

1. Visit your deployed dashboard (Vercel URL)
2. The metrics should now show:
   - 1 extraction in 7d
   - Completeness score
   - Quality rating

---

## Step 4: Go Live

### 4.1 Fathom Configuration

Configure Fathom to save transcripts to your Google Drive folder:

1. In Fathom settings, find **Integrations** > **Google Drive**
2. Set save location to: `A - Meeting Transcript Processing`
3. Enable auto-save after meetings

### 4.2 Turn On the Zap

1. Go to Zapier
2. Find your zap
3. Toggle it **ON**

### 4.3 Monitor First Few Meetings

- Check Zap history after your next few meetings
- Verify extractions in Supabase
- Adjust prompts if needed

---

## Troubleshooting

### "No data in dashboard"

1. Check Supabase table has rows
2. Verify `.env.local` has correct credentials
3. Check browser console for errors
4. Verify Supabase RLS policies allow read access

### "Zapier fails at Claude step"

1. Check Claude API key is valid
2. Verify key has sufficient credits
3. Check request format matches API spec

### "Parsing fails"

1. Check Claude response format
2. Adjust prompt to emphasize "output ONLY valid JSON"
3. Add retry logic in Zapier

### "Supabase insert fails"

1. Check table schema matches data structure
2. Verify API key has insert permissions
3. Check RLS policies

---

## Maintenance

### Weekly
- [ ] Review Zap error history
- [ ] Check dashboard metrics for anomalies
- [ ] Review flagged extractions

### Monthly
- [ ] Analyze extraction quality trends
- [ ] Update Claude prompts if needed
- [ ] Review and clean up test data

---

## Files Modified in This Setup

| File | Purpose |
|------|---------|
| `.mcp.json` | Updated Supabase project reference |
| `intelligence-dashboard/.env.local` | Created with your credentials |
| `intelligence-dashboard/zapier-supabase-integration.js` | Updated with your Supabase URL |

---

## Next Steps

Once operational, consider:

1. **Add more extraction templates** - Customize for different meeting types
2. **Set up Asana integration** - Store actual intelligence in Asana projects
3. **Enable weekly analysis** - Auto-generate quality reports
4. **Add A/B testing** - Test different prompt variations

---

*Last updated: 2025-11-26*
