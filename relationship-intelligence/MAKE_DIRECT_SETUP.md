# Direct Pipeline: Fathom → Make.com → Claude → Supabase

## Overview

This workflow eliminates Zapier and Google Drive, sending Fathom transcripts directly through Make.com to Claude API for extraction, then into Supabase.

```
Fathom (Webhook) → Make.com → Claude API (Extract) → Supabase
```

**Benefits:**
- Single automation platform (Make.com only)
- No intermediate storage (Google Drive)
- Faster processing (fewer hops)
- Easier debugging (one place to monitor)

## Prerequisites

- Make.com account (free tier: 1,000 ops/month)
- Anthropic API key (for Claude)
- Supabase project with schema deployed
- Fathom account with webhook access

## Cost Estimate

| Service | Free Tier | Estimated Usage |
|---------|-----------|-----------------|
| Make.com | 1,000 ops/month | ~50-100 ops per transcript |
| Claude API | Pay-per-use | ~$0.01-0.05 per transcript |
| Supabase | 500MB + 2GB bandwidth | Minimal |

---

## Step 1: Create Make.com Webhook

1. Go to [make.com](https://make.com)
2. Click **Create a new scenario**
3. Name it: `Fathom Direct → Intelligence Pipeline`
4. Click the **+** to add first module
5. Search for **Webhooks**
6. Select **Custom webhook**
7. Click **Add** → Name it `fathom-transcript-webhook`
8. **Copy the webhook URL** (you'll need this for Fathom)

Example URL:
```
https://hook.us1.make.com/abc123xyz789...
```

---

## Step 2: Configure Fathom Webhook

### Option A: Fathom Native Integration (if available)

1. Go to Fathom → Settings → Integrations
2. Look for Webhooks or Custom Integration
3. Add your Make.com webhook URL
4. Select trigger: "When call recording is ready"

### Option B: Fathom → Zapier → Make Webhook (fallback)

If Fathom doesn't support direct webhooks:

1. In Zapier, create a Zap:
   - Trigger: **Fathom** → New Recording
   - Action: **Webhooks by Zapier** → POST
   - URL: Your Make.com webhook URL
   - Payload Type: JSON
   - Data:
     ```json
     {
       "transcript": "{{transcript}}",
       "title": "{{title}}",
       "date": "{{date}}",
       "duration": "{{duration}}",
       "participants": "{{participants}}"
     }
     ```

### Option C: Manual Testing

For testing, use Make.com's "Run once" with sample data:

```json
{
  "transcript": "John: Thanks for meeting today. We're really interested in your Innovation Compass service.\nJane: Great! What specific challenges are you trying to solve?\nJohn: We need to validate our market assumptions before the board meeting next month.\nJane: Perfect. I'll send over a proposal by Friday.",
  "title": "Discovery Call - Acme Corp",
  "date": "2024-11-26",
  "duration": "45:00",
  "participants": ["John Smith (Acme Corp)", "Jane Doe (360)"]
}
```

---

## Step 3: Add Claude API Module

After the webhook, add the Claude extraction:

1. Click **+** after Webhooks module
2. Search for **HTTP**
3. Select **Make a request**
4. Configure:

**URL:**
```
https://api.anthropic.com/v1/messages
```

**Method:** POST

**Headers:**
| Key | Value |
|-----|-------|
| `x-api-key` | `your-anthropic-api-key` |
| `anthropic-version` | `2023-06-01` |
| `content-type` | `application/json` |

**Body type:** Raw

**Content type:** JSON (application/json)

**Request content:**
```json
{
  "model": "claude-sonnet-4-20250514",
  "max_tokens": 4096,
  "messages": [
    {
      "role": "user",
      "content": "You are an expert relationship intelligence analyst for 360 Social Impact Studios.\n\nExtract structured intelligence from this meeting transcript.\n\n## TRANSCRIPT\nTitle: {{1.title}}\nDate: {{1.date}}\nParticipants: {{1.participants}}\n\n{{1.transcript}}\n\n## OUTPUT FORMAT\nRespond with ONLY valid JSON (no markdown, no explanation):\n\n{\n  \"extraction_metadata\": {\n    \"meeting_title\": \"string\",\n    \"meeting_date\": \"YYYY-MM-DD\",\n    \"confidence_score\": 0.0-1.0,\n    \"needs_human_review\": boolean,\n    \"review_reasons\": [\"string\"]\n  },\n  \"interaction\": {\n    \"meeting_type\": \"discovery|followup|presentation|negotiation|closing|check_in|introduction\",\n    \"meeting_format\": \"video|phone|in_person|async\",\n    \"outcome\": \"positive|neutral|negative|mixed\",\n    \"temperature_change\": \"warming|cooling|stable\",\n    \"summary\": \"2-3 sentence summary\",\n    \"topics\": [\"topic1\", \"topic2\"],\n    \"key_quotes\": [\"verbatim quote 1\"]\n  },\n  \"relationships\": [\n    {\n      \"data\": {\n        \"name\": \"Full Name\",\n        \"organization\": \"Company\",\n        \"title\": \"Job Title\",\n        \"persona_type\": \"government_innovation|university_tto|corporate_innovation|vc_partner|foundation_program|startup_founder|research_director|c_suite_executive\",\n        \"geography\": \"City, Country\",\n        \"stage\": \"prospect|active|partner|dormant\",\n        \"source\": \"referral|conference|inbound|outbound\",\n        \"notes\": \"Key context\"\n      },\n      \"confidence\": 0.0-1.0\n    }\n  ],\n  \"service_interests\": [\n    {\n      \"data\": {\n        \"service\": \"innovation_compass|vianeo_validation|ip_assessment|university_partnership|venture_studio|market_entry_brazil|innovation_strategy|franchise_development\",\n        \"interest_level\": \"mentioned|exploring|evaluating|ready_to_buy\",\n        \"interest_source\": \"explicit|inferred\",\n        \"budget_confirmed\": boolean,\n        \"timeline_confirmed\": boolean,\n        \"estimated_value\": number or null\n      },\n      \"confidence\": 0.0-1.0\n    }\n  ],\n  \"commitments\": [\n    {\n      \"data\": {\n        \"owner\": \"ours|theirs\",\n        \"relationship_name\": \"Name of person\",\n        \"description\": \"What was promised\",\n        \"commitment_type\": \"deliverable|meeting|introduction|information|decision\",\n        \"due_date\": \"YYYY-MM-DD or null\",\n        \"due_date_type\": \"explicit|inferred|none\"\n      },\n      \"confidence\": 0.0-1.0\n    }\n  ],\n  \"signals\": [\n    {\n      \"data\": {\n        \"signal_type\": \"budget|timeline|authority|need|competition|risk|opportunity|relationship\",\n        \"description\": \"What was signaled\",\n        \"verbatim_quote\": \"Exact quote if available\",\n        \"significance\": \"high|medium|low\",\n        \"amount\": number or null,\n        \"actionable\": boolean,\n        \"action_required\": \"Recommended action or null\"\n      },\n      \"confidence\": 0.0-1.0\n    }\n  ],\n  \"objections\": [\n    {\n      \"data\": {\n        \"objection_type\": \"price|timing|authority|need|trust|competition|scope|process\",\n        \"objection_text\": \"Summary of objection\",\n        \"verbatim_quote\": \"Exact quote\",\n        \"response_given\": \"How we responded or null\",\n        \"response_effective\": boolean or null,\n        \"objection_overcome\": boolean,\n        \"what_worked\": \"What worked or null\"\n      },\n      \"confidence\": 0.0-1.0\n    }\n  ],\n  \"competitor_mentions\": [\n    {\n      \"data\": {\n        \"competitor_name\": \"Company name\",\n        \"competitor_type\": \"direct|indirect|alternative|incumbent\",\n        \"context\": \"How they came up\",\n        \"verbatim_quote\": \"Exact quote or null\",\n        \"perceived_strengths\": [\"strength1\"],\n        \"perceived_weaknesses\": [\"weakness1\"],\n        \"price_comparison\": \"cheaper|similar|expensive|unknown\"\n      },\n      \"confidence\": 0.0-1.0\n    }\n  ],\n  \"introductions\": [\n    {\n      \"data\": {\n        \"introduced_name\": \"Name\",\n        \"introduced_org\": \"Organization\",\n        \"introduced_by\": \"Who made intro\",\n        \"context\": \"Why introduced\",\n        \"warmth\": \"hot|warm|cold\"\n      },\n      \"confidence\": 0.0-1.0\n    }\n  ]\n}"
    }
  ]
}
```

**Parse response:** Yes

---

## Step 4: Add JSON Parser

1. Click **+** after HTTP module
2. Search for **JSON**
3. Select **Parse JSON**
4. Configure:
   - **JSON string:** `{{2.data.content[].text}}`

This extracts Claude's response into structured data.

---

## Step 5: Add Router for Database Inserts

1. Click **+** after JSON module
2. Search for **Router**
3. Add router

The router splits the extraction into parallel Supabase inserts.

---

## Step 6: Configure Supabase Connection

Before adding branches, set up Supabase:

1. In any Supabase module, click **Add connection**
2. Configure:
   - **Connection name:** `360-intelligence`
   - **Supabase URL:** `https://pblxazslxcotbdxtvnlb.supabase.co`
   - **API Key:** Your anon key

---

## Step 7: Add Database Insert Branches

### Branch 1: Relationship + Interaction

**Step 1: Search Persona**
1. Add **Supabase** → **Search Rows**
2. Table: `persona_archetypes`
3. Filter: `name` equals `{{3.relationships[1].data.persona_type}}`

**Step 2: Insert Relationship**
1. Add **Supabase** → **Create a Row**
2. Table: `relationships`
3. Map fields:

| Field | Value |
|-------|-------|
| name | `{{3.relationships[1].data.name}}` |
| organization | `{{3.relationships[1].data.organization}}` |
| title | `{{3.relationships[1].data.title}}` |
| persona_id | `{{4.id}}` (from persona search) |
| geography | `{{3.relationships[1].data.geography}}` |
| stage | `{{3.relationships[1].data.stage}}` |
| source | `{{3.relationships[1].data.source}}` |
| notes | `{{3.relationships[1].data.notes}}` |
| push_status | `pending_review` |

**Step 3: Insert Interaction**
1. Add **Supabase** → **Create a Row**
2. Table: `interactions`
3. Map fields:

| Field | Value |
|-------|-------|
| relationship_id | `{{5.id}}` (from relationship insert) |
| interaction_date | `{{3.extraction_metadata.meeting_date}}` |
| meeting_type | `{{3.interaction.meeting_type}}` |
| meeting_format | `{{3.interaction.meeting_format}}` |
| outcome | `{{3.interaction.outcome}}` |
| temperature_change | `{{3.interaction.temperature_change}}` |
| summary | `{{3.interaction.summary}}` |
| topics | `{{3.interaction.topics}}` |
| key_quotes | `{{3.interaction.key_quotes}}` |
| needs_review | `{{3.extraction_metadata.needs_human_review}}` |

---

### Branch 2: Commitments (Iterator)

1. Add **Iterator** module
2. **Array:** `{{3.commitments}}`

3. Add **Supabase** → **Search Rows**
   - Table: `relationships`
   - Filter: `name` contains `{{4.data.relationship_name}}`

4. Add **Supabase** → **Create a Row**
   - Table: `commitments`

| Field | Value |
|-------|-------|
| relationship_id | `{{5.id}}` |
| owner | `{{4.data.owner}}` |
| description | `{{4.data.description}}` |
| commitment_type | `{{4.data.commitment_type}}` |
| due_date | `{{4.data.due_date}}` |
| due_date_type | `{{4.data.due_date_type}}` |
| status | `pending` |
| push_status | `pending_review` |

---

### Branch 3: Signals (Iterator)

1. Add **Iterator** for `{{3.signals}}`
2. Add **Supabase** → **Search Rows** (relationships by name)
3. Add **Supabase** → **Create a Row** (signals table)

| Field | Value |
|-------|-------|
| relationship_id | (from search) |
| signal_type | `{{iterator.data.signal_type}}` |
| description | `{{iterator.data.description}}` |
| verbatim_quote | `{{iterator.data.verbatim_quote}}` |
| significance | `{{iterator.data.significance}}` |
| amount | `{{iterator.data.amount}}` |
| actionable | `{{iterator.data.actionable}}` |
| action_required | `{{iterator.data.action_required}}` |
| confidence | `{{iterator.confidence}}` |

---

### Branch 4: Service Interests (Iterator)

1. Add **Iterator** for `{{3.service_interests}}`

2. Add **Supabase** → **Search Rows**
   - Table: `relationships`
   - (get relationship_id)

3. Add **Supabase** → **Search Rows**
   - Table: `services`
   - Filter: `name` equals `{{iterator.data.service}}`

4. Add **Supabase** → **Create a Row**
   - Table: `service_interest`

| Field | Value |
|-------|-------|
| relationship_id | (from relationship search) |
| service_id | (from service search) |
| interest_level | `{{iterator.data.interest_level}}` |
| interest_source | `{{iterator.data.interest_source}}` |
| budget_confirmed | `{{iterator.data.budget_confirmed}}` |
| timeline_confirmed | `{{iterator.data.timeline_confirmed}}` |
| estimated_value | `{{iterator.data.estimated_value}}` |

---

### Branch 5: Objections (Iterator)

1. Add **Iterator** for `{{3.objections}}`
2. Add **Supabase** → **Create a Row** (objections table)

| Field | Value |
|-------|-------|
| objection_type | `{{iterator.data.objection_type}}` |
| objection_text | `{{iterator.data.objection_text}}` |
| verbatim_quote | `{{iterator.data.verbatim_quote}}` |
| response_given | `{{iterator.data.response_given}}` |
| response_effective | `{{iterator.data.response_effective}}` |
| objection_overcome | `{{iterator.data.objection_overcome}}` |
| what_worked | `{{iterator.data.what_worked}}` |

---

### Branch 6: Competitor Intel (Iterator)

1. Add **Iterator** for `{{3.competitor_mentions}}`
2. Add **Supabase** → **Create a Row** (competitor_intel table)

| Field | Value |
|-------|-------|
| competitor_name | `{{iterator.data.competitor_name}}` |
| competitor_type | `{{iterator.data.competitor_type}}` |
| context | `{{iterator.data.context}}` |
| verbatim_quote | `{{iterator.data.verbatim_quote}}` |
| perceived_strengths | `{{iterator.data.perceived_strengths}}` |
| perceived_weaknesses | `{{iterator.data.perceived_weaknesses}}` |
| price_comparison | `{{iterator.data.price_comparison}}` |

---

### Branch 7: Introductions (Iterator)

1. Add **Iterator** for `{{3.introductions}}`
2. Add **Supabase** → **Create a Row** (introductions table)

| Field | Value |
|-------|-------|
| introduced_name | `{{iterator.data.introduced_name}}` |
| introduced_org | `{{iterator.data.introduced_org}}` |
| introduced_by | `{{iterator.data.introduced_by}}` |
| context | `{{iterator.data.context}}` |
| warmth | `{{iterator.data.warmth}}` |

---

## Complete Flow Diagram

```
[Webhook: Fathom Transcript]
         ↓
[HTTP: Claude API Extraction]
         ↓
[JSON: Parse Response]
         ↓
[Router]
    ├── Branch 1: [Search persona] → [Insert relationship] → [Insert interaction]
    │
    ├── Branch 2: [Iterator: commitments]
    │                    ↓
    │             [Search relationship] → [Insert commitment]
    │
    ├── Branch 3: [Iterator: signals]
    │                    ↓
    │             [Search relationship] → [Insert signal]
    │
    ├── Branch 4: [Iterator: service_interests]
    │                    ↓
    │             [Search relationship] → [Search service] → [Insert service_interest]
    │
    ├── Branch 5: [Iterator: objections]
    │                    ↓
    │             [Insert objection]
    │
    ├── Branch 6: [Iterator: competitor_mentions]
    │                    ↓
    │             [Insert competitor_intel]
    │
    └── Branch 7: [Iterator: introductions]
                         ↓
                  [Insert introduction]
```

---

## Step 8: Error Handling

Add error handlers for robustness:

1. After Claude HTTP module, add **Router**
2. Add filter on first route: `{{2.statusCode}}` equals `200`
3. Add second route for errors → **Email** or **Slack** notification

For Supabase errors:
1. Enable **Error handling** on each Supabase module
2. Set to **Ignore** or **Break** depending on preference

---

## Step 9: Test the Pipeline

1. Click **Run once** in Make.com
2. Send test data to webhook:

```bash
curl -X POST "YOUR_WEBHOOK_URL" \
  -H "Content-Type: application/json" \
  -d '{
    "transcript": "John: We love what 360 is doing with Innovation Compass. Sarah mentioned your work with universities.\nJane: Yes, we have strong TTO partnerships. What timeline are you working with?\nJohn: Board meeting is in 6 weeks. Budget is approved - around $50k.\nJane: Perfect. I will send a proposal by Friday.",
    "title": "Discovery - Tech Corp",
    "date": "2024-11-26",
    "duration": "30:00",
    "participants": ["John Smith (Tech Corp CIO)", "Jane Doe (360)"]
  }'
```

3. Check Make.com execution log
4. Verify data in Supabase tables

---

## Step 10: Enable Scheduling

1. Click the **clock** icon on the webhook
2. Webhook is always listening (no schedule needed)
3. Set scenario to **On** (top right toggle)

---

## Troubleshooting

**Webhook not receiving data:**
- Verify URL is correct in Fathom/Zapier
- Check Make.com scenario is ON
- Test with curl command above

**Claude API errors:**
- Verify API key is correct
- Check model name (`claude-sonnet-4-20250514`)
- Review rate limits

**JSON parse errors:**
- Claude may return markdown-wrapped JSON
- Add text processing to strip ```json wrapper if needed

**Supabase insert failures:**
- Check column names match schema exactly
- Verify data types (dates, booleans, numbers)
- Check foreign key constraints

**Empty arrays (no data extracted):**
- Transcript may not contain relevant information
- Lower confidence threshold in prompt
- Review Claude's raw response

---

## Operations Estimate

Per transcript processed:
- 1 webhook receive
- 1 HTTP call (Claude)
- 1 JSON parse
- 1 router
- ~5-15 Supabase operations (depending on content)

**Total: ~10-20 operations per transcript**

With 1,000 free ops/month: **~50-100 transcripts/month**

For higher volume, consider Make.com paid plans or batch processing.

---

## Alternative: Batch Processing

To reduce operations, batch multiple transcripts:

1. Store transcripts in Google Sheet or Supabase staging table
2. Run scenario on schedule (daily)
3. Process all pending transcripts in one run
4. Use aggregator modules to batch Supabase inserts

This can reduce operations by 50-70%.
