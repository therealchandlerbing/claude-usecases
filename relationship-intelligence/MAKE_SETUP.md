# Make.com Pipeline Setup Guide

## Overview

This guide walks through setting up Make.com to:
1. Watch for new JSON files in Google Drive
2. Parse the extracted intelligence
3. Insert into Supabase tables

## Prerequisites

- Make.com account (free tier: 1,000 ops/month)
- Google Drive folder with Claude extraction outputs
- Supabase project with schema deployed

## Step 1: Create New Scenario

1. Go to [make.com](https://make.com)
2. Click **Create a new scenario**
3. Name it: "Meeting Intelligence → Supabase"

## Step 2: Add Google Drive Trigger

1. Click the **+** button
2. Search for **Google Drive**
3. Select **Watch Files**
4. Configure:
   - **Connection**: Connect your Google account
   - **Watch Files**: By Created Time
   - **Folder**: Select your Claude output folder
   - **File Type**: JSON files
   - **Limit**: 10

## Step 3: Add HTTP Module (Get File Content)

1. Add another module after Google Drive
2. Search for **HTTP**
3. Select **Get a File**
4. Configure:
   - **URL**: `{{1.webContentLink}}` (from Google Drive)

## Step 4: Add JSON Parser

1. Add **JSON** module
2. Select **Parse JSON**
3. Configure:
   - **JSON string**: `{{2.data}}`

## Step 5: Add Router

The router splits the data into different Supabase insertions:

1. Add **Router** module
2. Create branches for each data type

## Step 6: Configure Supabase Modules

### Branch 1: Insert Relationship

1. Add **Supabase** module
2. Select **Create a Row**
3. Configure:
   - **Connection**: Add new (URL + API key)
   - **Table**: `relationships`
   - Map fields:
     ```
     name: {{3.relationships[].data.name}}
     organization: {{3.relationships[].data.organization}}
     title: {{3.relationships[].data.title}}
     persona_id: (lookup from persona_archetypes)
     geography: {{3.relationships[].data.geography}}
     stage: {{3.relationships[].data.stage}}
     source: {{3.relationships[].data.source}}
     notes: {{3.relationships[].data.notes}}
     push_status: "pending_review"
     ```

### Branch 2: Insert Interaction

1. Add **Supabase** > **Create a Row**
2. **Table**: `interactions`
3. Map fields:
   ```
   interaction_date: {{3.interaction.interaction_date}}
   relationship_id: (from previous insert or lookup)
   meeting_type: {{3.interaction.meeting_type}}
   meeting_format: {{3.interaction.meeting_format}}
   outcome: {{3.interaction.outcome}}
   temperature_change: {{3.interaction.temperature_change}}
   summary: {{3.interaction.summary}}
   topics: {{3.interaction.topics}}
   key_quotes: {{3.interaction.key_quotes}}
   needs_review: {{3.extraction_metadata.needs_human_review}}
   ```

### Branch 3: Insert Commitments (Iterator)

1. Add **Iterator** module
2. **Array**: `{{3.commitments}}`
3. Add **Supabase** > **Create a Row**
4. **Table**: `commitments`
5. Map fields:
   ```
   owner: {{4.data.owner}}
   description: {{4.data.description}}
   commitment_type: {{4.data.commitment_type}}
   due_date: {{4.data.due_date}}
   due_date_type: {{4.data.due_date_type}}
   push_status: "pending_review"
   ```

### Branch 4: Insert Signals (Iterator)

1. Add **Iterator** for `{{3.signals}}`
2. Add **Supabase** > **Create a Row**
3. **Table**: `signals`
4. Map fields:
   ```
   signal_type: {{5.data.signal_type}}
   description: {{5.data.description}}
   verbatim_quote: {{5.data.verbatim_quote}}
   significance: {{5.data.significance}}
   amount: {{5.data.amount}}
   actionable: {{5.data.actionable}}
   action_required: {{5.data.action_required}}
   confidence: {{5.confidence}}
   ```

### Branch 5: Insert Service Interests (Iterator)

1. Add **Iterator** for `{{3.service_interests}}`
2. Add **Supabase** > **Create a Row**
3. **Table**: `service_interest`
4. Map fields:
   ```
   service_id: (lookup from services table by name)
   interest_level: {{6.data.interest_level}}
   interest_source: {{6.data.interest_source}}
   budget_confirmed: {{6.data.budget_confirmed}}
   timeline_confirmed: {{6.data.timeline_confirmed}}
   estimated_value: {{6.data.estimated_value}}
   ```

### Branch 6: Insert Objections (Iterator)

1. Add **Iterator** for `{{3.objections}}`
2. Add **Supabase** > **Create a Row**
3. **Table**: `objections`
4. Map fields:
   ```
   objection_type: {{7.data.objection_type}}
   objection_text: {{7.data.objection_text}}
   verbatim_quote: {{7.data.verbatim_quote}}
   response_given: {{7.data.response_given}}
   response_effective: {{7.data.response_effective}}
   objection_overcome: {{7.data.objection_overcome}}
   what_worked: {{7.data.what_worked}}
   ```

### Branch 7: Insert Competitor Intel (Iterator)

1. Add **Iterator** for `{{3.competitor_mentions}}`
2. Add **Supabase** > **Create a Row**
3. **Table**: `competitor_intel`
4. Map fields:
   ```
   competitor_name: {{8.data.competitor_name}}
   competitor_type: {{8.data.competitor_type}}
   context: {{8.data.context}}
   verbatim_quote: {{8.data.verbatim_quote}}
   perceived_strengths: {{8.data.perceived_strengths}}
   perceived_weaknesses: {{8.data.perceived_weaknesses}}
   price_comparison: {{8.data.price_comparison}}
   ```

## Step 7: Relationship Lookup Function

To link records properly, you need to lookup relationship IDs:

1. Before inserting commitments/signals, add **Supabase** > **Search Rows**
2. **Table**: `relationships`
3. **Filter**: `name` equals `{{commitment.data.relationship_name}}`
4. Use the returned `id` in subsequent inserts

## Step 8: Service Lookup Function

Similar for service_interest:

1. Add **Supabase** > **Search Rows**
2. **Table**: `services`
3. **Filter**: `name` equals `{{service_interest.data.service}}`
4. Use returned `id` as `service_id`

## Step 9: Persona Lookup Function

For relationship persona assignment:

1. Add **Supabase** > **Search Rows**
2. **Table**: `persona_archetypes`
3. **Filter**: `name` equals `{{relationship.data.persona_type}}`
4. Use returned `id` as `persona_id`

## Complete Flow Diagram

```
[Google Drive: Watch Files]
         ↓
[HTTP: Get File Content]
         ↓
[JSON: Parse JSON]
         ↓
[Router]
    ├── Branch 1: [Supabase: Search persona] → [Supabase: Insert relationship]
    │                                                    ↓
    │                                          [Supabase: Insert interaction]
    │
    ├── Branch 2: [Iterator: commitments]
    │                    ↓
    │             [Supabase: Search relationship]
    │                    ↓
    │             [Supabase: Insert commitment]
    │
    ├── Branch 3: [Iterator: signals]
    │                    ↓
    │             [Supabase: Search relationship]
    │                    ↓
    │             [Supabase: Insert signal]
    │
    ├── Branch 4: [Iterator: service_interests]
    │                    ↓
    │             [Supabase: Search relationship]
    │                    ↓
    │             [Supabase: Search service]
    │                    ↓
    │             [Supabase: Insert service_interest]
    │
    ├── Branch 5: [Iterator: objections]
    │                    ↓
    │             [Supabase: Insert objection]
    │
    └── Branch 6: [Iterator: competitor_mentions]
                         ↓
                  [Supabase: Insert competitor_intel]
```

## Step 10: Enable Scenario

1. Click **Run once** to test with a sample file
2. Check Supabase tables for data
3. Enable scheduling (every 15 minutes recommended)

## Troubleshooting

**No files detected:**
- Verify folder permissions
- Check file type filter

**JSON parse errors:**
- Ensure Claude output is valid JSON
- Check for markdown code blocks (should be raw JSON)

**Supabase insert failures:**
- Verify column names match schema
- Check data types (dates, numbers)
- Look for missing required fields

**Relationship lookup fails:**
- Name matching must be exact
- Consider using ILIKE for fuzzy matching

## Cost Optimization

Free tier: 1,000 operations/month

To stay within limits:
- Process files in batches
- Use filters to skip already-processed files
- Consider daily processing vs real-time

## Alternative: Zapier Integration

If you prefer Zapier over Make.com:

1. Use existing Fathom → Zapier → Claude flow
2. Add **Webhooks by Zapier** action after Claude
3. Send to Make.com webhook (or)
4. Add **Supabase** integration directly in Zapier

Zapier has native Supabase support but operations are more expensive.
