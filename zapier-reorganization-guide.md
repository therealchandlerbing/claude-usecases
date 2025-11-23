# Zapier Workflow Reorganization Guide
**Goal:** Fix the Fathom → Claude → Supabase → Dashboard pipeline

---

## Current State Analysis

From your screenshot, here's what I see:

| Step | App | Action | Purpose | Issue |
|------|-----|--------|---------|-------|
| 1 | Fathom | New Transcript | Trigger | ✅ Correct |
| 2 | Google Docs | Create Document | ❓ Unclear | ⚠️ Might be redundant |
| 3 | Anthropic (Claude) | Send Message | Extract intelligence | ✅ Correct |
| 4 | Google Docs | Create Document | Save extraction? | ⚠️ Wrong position |
| 5 | Asana | Create Task | Track action items | ⚠️ Wrong position |
| 6 | Code by Zapier | ❓ | ❓ Supabase integration? | ❌ Wrong position |

---

## Ideal Workflow (Reorganized)

### Step 1: Fathom Trigger ✅
**App:** Fathom
**Event:** New Transcript
**Config:**
- This captures whenever a new meeting transcript is ready
- **Action:** Keep as-is

---

### Step 2: Claude Extraction ✅
**App:** Anthropic (Claude) or Code by Zapier
**Event:** Send Message (if using Anthropic app) OR Run JavaScript (if using Code by Zapier)

**Current Status:** This is your Step 3 - it's correct!

**What it should do:**
- Take the Fathom transcript text
- Extract: partnerships, funding opportunities, stakeholder insights, etc.
- Output structured data like:
  ```json
  {
    "extraction_id": "unique-id-123",
    "meeting_type": "Partnership Discussion",
    "entities_created": 5,
    "completeness_score": 85,
    "flagged_for_review": false,
    "intelligence_data": { ... }
  }
  ```

**Action Required:**
- Move this to be Step 2 (right after Fathom trigger)
- Delete the Google Docs step that's currently Step 2

---

### Step 3: Send to Supabase ⚠️ **THIS IS THE NEW STEP**
**App:** Code by Zapier
**Event:** Run JavaScript
**Name:** "Send to Supabase Dashboard"

**Input Data Setup:**
Click "+ Add a new field" for each of these and map from Step 2 (Claude extraction):

| Field Name | Map From Claude Output | Type |
|------------|------------------------|------|
| `extraction_id` | extraction_id | String |
| `source_file_name` | transcript_name OR file_name | String |
| `meeting_type` | meeting_type | String |
| `template_name` | template_name | String |
| `completeness_score` | completeness_score | Number |
| `flagged_for_review` | flagged_for_review | Boolean |
| `entities_created` | entities_created | Number |
| `items_extracted` | items_extracted | Number |
| `intelligence_data` | full_extraction_json | String (JSON) |

**Code:** Use the integration code from `zapier-supabase-integration.js`

**Action Required:**
- If Step 6 is already configured with Supabase code, **move it to Step 3**
- If Step 6 is empty or different, **create new Code by Zapier step here**

---

### Step 4: Save to Google Docs (Optional) 📄
**App:** Google Docs
**Event:** Create Document From Text
**Purpose:** Backup/historical record of extractions

**Config:**
- Document Name: `[Extraction] {{Step 2: meeting_type}} - {{Step 1: created_date}}`
- Text: `{{Step 2: intelligence_data}}`
- Folder: Choose your "Extraction Archive" folder

**Action Required:**
- If you want to keep Google Docs archiving, configure this step
- If not needed, **delete both Google Docs steps**
- This should come AFTER Supabase (Step 3)

---

### Step 5: Create Asana Task (Conditional) ✅
**App:** Asana
**Event:** Create Task
**Purpose:** Only create task if extraction needs review

**Add a Filter Before This Step:**
1. Click "+" before Asana step
2. Choose "Filter"
3. Condition: `flagged_for_review` (from Step 2) equals `true`
4. This way tasks only get created for flagged extractions

**Task Config:**
- Project: "Intelligence Review Queue"
- Task Name: `Review: {{Step 2: meeting_type}} - {{Step 2: source_file_name}}`
- Notes:
  ```
  Completeness Score: {{Step 2: completeness_score}}%
  Entities Created: {{Step 2: entities_created}}

  View in Dashboard: https://intelligence-dashboard-360-dleikewl0-chandler-lewis-projects.vercel.app

  {{Step 2: review_notes}}
  ```

**Action Required:**
- Add Filter step before Asana
- Configure task to only trigger on flagged extractions
- This should be Step 5 (after Google Docs or after Supabase if no Docs)

---

## How to Reorganize in Zapier

### Option A: Start Fresh (Recommended if heavily broken)
1. Click "Create Zap" (new Zap)
2. Build steps in order: Fathom → Claude → Supabase → Docs → Asana
3. Copy/paste your Claude code from the old Zap
4. Configure Supabase code from the guide
5. Turn OFF old Zap, turn ON new Zap

### Option B: Modify Existing (Faster)
1. **Delete Step 2** (first Google Docs)
   - Click the 3-dot menu on Step 2
   - Select "Delete"

2. **Your Claude step becomes Step 2** (automatically renumbers)

3. **Move Step 6 (Code by Zapier) to Step 3:**
   - Unfortunately, Zapier doesn't let you drag/drop steps
   - You need to:
     - Note down the configuration of Step 6
     - Delete Step 6
     - Add new "Code by Zapier" step after Claude (Step 2)
     - Reconfigure with Supabase code

4. **Fix Step 3** (old Step 4 Google Docs):
   - Reconfigure to use data from Claude (now Step 2)
   - Update document name to be descriptive

5. **Add Filter before Asana:**
   - Click "+" before Asana step
   - Add "Filter" step
   - Set condition: `flagged_for_review = true`

6. **Test the whole flow:**
   - Click "Test" on each step
   - Make sure data flows correctly

---

## Verification Checklist

After reorganization, verify:

- [ ] **Step 1:** Fathom trigger is configured
- [ ] **Step 2:** Claude extraction outputs structured data
- [ ] **Step 3:** Supabase code runs successfully (`success: true`)
- [ ] **Step 3:** Data appears in dashboard (check https://intelligence-dashboard-360-dleikewl0-chandler-lewis-projects.vercel.app)
- [ ] **Step 4:** Google Docs saves extraction (or step is deleted if not needed)
- [ ] **Step 5:** Filter before Asana checks `flagged_for_review`
- [ ] **Step 5:** Asana task created ONLY when flagged
- [ ] **Zap is turned ON** (green toggle in top right)

---

## Testing Protocol

### Test 1: End-to-End with Sample Data
1. In Zapier editor, click "Test" on Step 1 (Fathom)
2. Select a sample transcript
3. Click "Test step" on each subsequent step
4. Verify:
   - Claude extracts data ✅
   - Supabase returns `success: true` ✅
   - Dashboard shows new row ✅
   - Google Doc created (if enabled) ✅
   - Asana task created ONLY if flagged ✅

### Test 2: Real Meeting
1. Have a Fathom meeting (or use existing transcript)
2. Wait 5 minutes for Zap to run
3. Check "Zap History" in Zapier dashboard
4. Verify all steps succeeded
5. Check Intelligence Dashboard for new data

### Test 3: Real-Time Updates
1. Open dashboard: https://intelligence-dashboard-360-dleikewl0-chandler-lewis-projects.vercel.app
2. Trigger a new extraction (run Zap manually or new meeting)
3. Watch the dashboard update in real-time without refresh
4. If it doesn't update immediately, refresh once

---

## Common Issues & Fixes

### Issue: "Code by Zapier fails with 401 error"
**Cause:** Supabase API key incorrect
**Fix:**
1. Go to Step 3 (Supabase code)
2. Check `SUPABASE_ANON_KEY` matches exactly:
   ```
   eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im56dm1paGRnYnZvbWpsa2VsY3VtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjM3OTg0MzYsImV4cCI6MjA3OTM3NDQzNn0.8Z88SBISSMMJPoIqz_i3nc5KoiYKeNCJbaoI82Ijl30
   ```

### Issue: "Cannot read property 'extraction_id' of undefined"
**Cause:** Input data not mapped correctly
**Fix:**
1. Go to Step 3 (Supabase code)
2. In "Set up action", verify each input field is mapped from Step 2 (Claude)
3. Click in the value field and select the corresponding output from Claude dropdown

### Issue: "Dashboard doesn't show new data"
**Cause:** Either code failed or real-time not enabled
**Fix:**
1. Check Zap History - did Step 3 succeed?
2. If yes, go to Supabase → Database → Replication
3. Enable replication for `extractions` table
4. Refresh dashboard

### Issue: "Asana creates tasks for EVERY meeting"
**Cause:** Missing filter before Asana step
**Fix:**
1. Add "Filter" step before Asana
2. Set condition: `(Only continue if...) flagged_for_review = true`
3. Save and test

---

## Next Steps After Setup

1. **Run 3-5 real meetings** to populate dashboard with data
2. **Monitor quality trends** in dashboard
3. **Review flagged extractions** in Asana
4. **Refine Claude extraction prompt** based on completeness scores
5. **Set up weekly review** of dashboard insights

---

## Support

If you get stuck:
1. Check Zap History for error messages
2. Test each step individually
3. Verify Supabase credentials
4. Check dashboard console for errors (F12 in browser)

**Dashboard URL:**
https://intelligence-dashboard-360-dleikewl0-chandler-lewis-projects.vercel.app

**Supabase Dashboard:**
https://supabase.com/dashboard/project/nzvmihdgbvomjlkelcum
