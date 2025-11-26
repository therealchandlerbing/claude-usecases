# Make.com Post-Import Setup Guide

## After Importing the Blueprint

You've imported `make-blueprint.json` and see "Module Not Found" errors on the Supabase modules. This is expected - the blueprint contains the workflow structure but connections need to be configured manually.

```
Current State:
[Webhooks ✓] → [HTTP ✓] → [JSON ✓] → [Router ✓]
                                          ↓
                              [Supabase ❌ Module Not Found]
                              [Supabase ❌ Module Not Found]
                              ...
```

---

## Step 1: Create Supabase Connection (Do This First!)

This fixes ALL the "Module Not Found" errors at once.

### 1.1 Click Any Gray Supabase Module

Click on any module showing "Module Not Found" (the gray circles with red exclamation marks).

### 1.2 Add New Connection

1. In the module settings panel, find **Connection**
2. Click **Add** or **Create a connection**
3. Fill in:

| Field | Value |
|-------|-------|
| **Connection name** | `360-intelligence` |
| **Supabase URL** | `https://pblxazslxcotbdxtvnlb.supabase.co` |
| **API Key** | Your Supabase **anon/public** key |

### 1.3 Get Your Supabase API Key

1. Go to [Supabase Dashboard](https://app.supabase.com)
2. Select your project
3. Go to **Settings** → **API**
4. Copy the **anon public** key (starts with `eyJ...`)

### 1.4 Save and Propagate

1. Click **Save** on the connection
2. The module should turn green with a checkmark
3. **IMPORTANT**: Repeat for each Supabase module OR use the connection dropdown to select your new `360-intelligence` connection

---

## Step 2: Configure HTTP Module (Claude API)

### 2.1 Click the HTTP Module

Click on module #2 (the blue globe labeled "HTTP - Make a request")

### 2.2 Update the API Key Header

1. Find the **Headers** section
2. Look for the header named `x-api-key`
3. Replace the value with your actual Anthropic API key

| Header | Current Value | Change To |
|--------|---------------|-----------|
| `x-api-key` | `{{parameters.anthropic_api_key}}` | `sk-ant-api03-YOUR-ACTUAL-KEY` |

### 2.3 Get Your Anthropic API Key

1. Go to [Anthropic Console](https://console.anthropic.com)
2. Navigate to **API Keys**
3. Create or copy your API key (starts with `sk-ant-api03-...`)

### 2.4 Save the Module

Click **OK** to save the HTTP module configuration.

---

## Step 3: Create the Webhook

### 3.1 Click the Webhooks Module

Click on module #1 (the red webhook icon)

### 3.2 Add a Webhook

1. Click **Add** next to the Webhook dropdown
2. Enter webhook name: `fathom-transcript-webhook`
3. Click **Save**
4. **Copy the generated webhook URL** - you'll need this for Fathom

Example URL:
```
https://hook.us1.make.com/abc123xyz789...
```

---

## Step 4: Connect Each Supabase Module

After creating the connection in Step 1, you need to assign it to each Supabase module.

### Module Connection Checklist

Click each of these modules and select `360-intelligence` from the Connection dropdown:

**Branch 1: Relationships + Interactions**
- [ ] Module 5: Supabase - Search Rows (persona_archetypes)
- [ ] Module 6: Supabase - Create Row (relationships)
- [ ] Module 7: Supabase - Create Row (interactions)

**Branch 2: Commitments**
- [ ] Module 9: Supabase - Search Rows (relationships)
- [ ] Module 10: Supabase - Create Row (commitments)

**Branch 3: Signals**
- [ ] Module 12: Supabase - Search Rows (relationships)
- [ ] Module 13: Supabase - Create Row (signals)

**Branch 4: Service Interests**
- [ ] Module 15: Supabase - Search Rows (relationships)
- [ ] Module 16: Supabase - Search Rows (services)
- [ ] Module 17: Supabase - Create Row (service_interest)

**Branch 5: Objections**
- [ ] Module 19: Supabase - Create Row (objections)

**Branch 6: Competitor Intel**
- [ ] Module 21: Supabase - Create Row (competitor_intel)

**Branch 7: Introductions**
- [ ] Module 23: Supabase - Create Row (introductions)

**Total: 13 Supabase modules to configure**

---

## Step 5: Verify Table Mappings

Each Supabase module should already have the correct table and field mappings from the import. Verify these are correct:

### Quick Verification

Click each "Create Row" module and confirm the **Table** field matches:

| Module | Expected Table |
|--------|----------------|
| Module 6 | `relationships` |
| Module 7 | `interactions` |
| Module 10 | `commitments` |
| Module 13 | `signals` |
| Module 17 | `service_interest` |
| Module 19 | `objections` |
| Module 21 | `competitor_intel` |
| Module 23 | `introductions` |

---

## Step 6: Test the Pipeline

### 6.1 Run Once with Test Data

1. Click **Run once** (play button at bottom)
2. Make.com will wait for webhook data

### 6.2 Send Test Webhook

Open a terminal and run:

```bash
curl -X POST "YOUR_WEBHOOK_URL_FROM_STEP_3" \
  -H "Content-Type: application/json" \
  -d '{
    "transcript": "John: We love what 360 is doing with Innovation Compass. Sarah mentioned your work with universities.\nJane: Yes, we have strong TTO partnerships. What timeline are you working with?\nJohn: Board meeting is in 6 weeks. Budget is approved - around $50k.\nJane: Perfect. I will send a proposal by Friday.",
    "title": "Discovery - Tech Corp",
    "date": "2024-11-26",
    "duration": "30:00",
    "participants": ["John Smith (Tech Corp CIO)", "Jane Doe (360)"]
  }'
```

### 6.3 Check Execution

1. Watch the scenario execute in Make.com
2. Each module should show a green checkmark
3. Check Supabase tables for new data

---

## Step 7: Enable Scheduling

Once testing is successful:

1. Toggle the scenario **ON** (top right switch)
2. The webhook is always listening - no schedule needed
3. Every Fathom transcript will automatically process

---

## Troubleshooting

### "Module Not Found" Still Showing

**Cause**: Connection not saved or not selected for that module

**Fix**:
1. Click the gray module
2. Look for "Connection" dropdown
3. Select `360-intelligence`
4. Click OK

### "Invalid API Key" from HTTP Module

**Cause**: Anthropic API key not configured correctly

**Fix**:
1. Click HTTP module
2. Find Headers section
3. Ensure `x-api-key` has your actual key (not the placeholder)

### "Table not found" from Supabase

**Cause**: Database schema not deployed

**Fix**: Run the `combined-schema.sql` in your Supabase SQL editor

### "Column not found" from Supabase

**Cause**: Schema mismatch between blueprint and database

**Fix**: Verify your Supabase schema matches the expected columns:

```sql
-- Check tables exist
SELECT table_name FROM information_schema.tables
WHERE table_schema = 'public';

-- Check relationships columns
SELECT column_name FROM information_schema.columns
WHERE table_name = 'relationships';
```

### Webhook Not Receiving Data

**Cause**: URL not configured in Fathom or Zapier

**Fix**:
1. Copy webhook URL from Make.com module #1
2. Configure in your Fathom integration settings
3. Or use Zapier as intermediary (see MAKE_DIRECT_SETUP.md)

### Empty Arrays (No Data Extracted)

**Cause**: Transcript doesn't contain extractable information

**Fix**:
1. Check Claude's raw response in module #2
2. Verify transcript has names, dates, actionable content
3. Test with the sample transcript above

---

## Architecture Reference

```
[1. Webhooks]          Receives Fathom transcript JSON
       ↓
[2. HTTP]              Sends to Claude API for extraction
       ↓
[3. JSON Parse]        Parses Claude's response
       ↓
[4. Router]            Splits data to parallel branches
       ↓
┌──────┴──────┬──────┬──────┬──────┬──────┬──────┐
│             │      │      │      │      │      │
Branch 1   Branch 2  Branch 3  Branch 4  Branch 5  Branch 6  Branch 7
Relationships  Commitments  Signals  Services  Objections  Competitors  Intros
       │             │      │      │      │      │      │
       ↓             ↓      ↓      ↓      ↓      ↓      ↓
[Supabase]     [Supabase] [Supabase] [Supabase] [Supabase] [Supabase] [Supabase]
```

---

## Quick Setup Checklist

- [ ] Create Supabase connection (`360-intelligence`)
- [ ] Configure HTTP module with Anthropic API key
- [ ] Create webhook and copy URL
- [ ] Connect all 13 Supabase modules to `360-intelligence`
- [ ] Deploy database schema to Supabase (if not done)
- [ ] Test with sample transcript
- [ ] Enable scenario

---

## Need Help?

- **Supabase Schema**: See `combined-schema.sql`
- **Full Setup Details**: See `MAKE_DIRECT_SETUP.md`
- **Alternative with Google Drive**: See `MAKE_SETUP.md`
- **Dashboard Setup**: See `dashboard/README.md`
