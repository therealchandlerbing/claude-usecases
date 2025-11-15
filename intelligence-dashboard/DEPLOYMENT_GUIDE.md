# Intelligence Dashboard - Complete Deployment Guide

Step-by-step guide to deploy your live intelligence quality dashboard.

## Prerequisites

- GitHub account
- Vercel account (free, sign up at vercel.com)
- Supabase account (free, sign up at supabase.com)
- Your existing Zapier workflows

## Deployment Checklist

- [ ] Set up Supabase database
- [ ] Deploy dashboard to Vercel
- [ ] Configure environment variables
- [ ] Update Zapier workflow
- [ ] Verify real-time functionality
- [ ] Optional: Set up custom domain

---

## Step 1: Set Up Supabase Database (15 minutes)

### 1.1 Create Supabase Project

1. Go to [supabase.com](https://supabase.com)
2. Click "Start your project"
3. Sign in with GitHub
4. Click "New Project"
5. Fill in:
   - **Name**: `intelligence-quality` (or your choice)
   - **Database Password**: Generate a strong password and **save it**
   - **Region**: Choose closest to you (e.g., `us-east-1`)
6. Click "Create new project"
7. Wait 2-3 minutes for provisioning

### 1.2 Run Database Schema

1. In Supabase dashboard, click "SQL Editor" in the left sidebar
2. Click "New Query"
3. Open the file `supabase-schema.sql` from this project
4. Copy the entire contents
5. Paste into the Supabase SQL Editor
6. Click "Run" (or Cmd/Ctrl + Enter)
7. You should see: "Success. No rows returned"

### 1.3 Verify Tables Created

1. Click "Table Editor" in left sidebar
2. You should see 4 tables:
   - `extractions` (main data table)
   - `experiments` (A/B testing)
   - `edits` (edit tracking)
   - `weekly_analyses` (analysis results)

### 1.4 Get API Credentials

1. Click "Project Settings" (gear icon in sidebar)
2. Click "API" in the settings menu
3. Copy these values (you'll need them later):
   - **URL**: `https://xxxxx.supabase.co`
   - **anon/public key**: `eyJhbGc...` (long string under "Project API keys")

**Save these somewhere safe!**

---

## Step 2: Deploy Dashboard to Vercel (10 minutes)

### 2.1 Push Code to GitHub

1. Open terminal in the `intelligence-dashboard` directory
2. Initialize git:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Intelligence Dashboard"
   ```
3. Create a new GitHub repository:
   - Go to github.com
   - Click "New repository"
   - Name it: `intelligence-dashboard`
   - Leave it public (or private if you prefer)
   - Do NOT initialize with README (we already have one)
   - Click "Create repository"

4. Push code to GitHub:
   ```bash
   # Replace YOUR_USERNAME with your GitHub username
   git remote add origin git@github.com:YOUR_USERNAME/intelligence-dashboard.git
   git branch -M main
   git push -u origin main
   ```

### 2.2 Import to Vercel

1. Go to [vercel.com](https://vercel.com)
2. Sign up/Sign in (use GitHub account for easiest setup)
3. Click "Add New..." → "Project"
4. Find your `intelligence-dashboard` repository
5. Click "Import"

### 2.3 Configure Project Settings

On the import screen:

1. **Framework Preset**: Next.js (should auto-detect)
2. **Root Directory**: `./` (leave as is)
3. **Build Command**: `npm run build` (default)
4. **Output Directory**: `.next` (default)

### 2.4 Add Environment Variables

1. Click "Environment Variables" to expand
2. Add these two variables:

   **Variable 1:**
   - Key: `NEXT_PUBLIC_SUPABASE_URL`
   - Value: `https://xxxxx.supabase.co` (from Step 1.4)

   **Variable 2:**
   - Key: `NEXT_PUBLIC_SUPABASE_ANON_KEY`
   - Value: `eyJhbGc...` (from Step 1.4)

3. Click "Deploy"

### 2.5 Wait for Deployment

- Deployment takes 1-3 minutes
- You'll see a progress screen with build logs
- When complete, you'll see "Congratulations!" with confetti

### 2.6 Visit Your Dashboard

1. Click "Visit" or copy the URL: `https://your-project.vercel.app`
2. You should see the dashboard (with no data yet)

**Bookmark this URL!**

---

## Step 3: Update Zapier Workflow (10 minutes)

Now connect your extraction pipeline to the new database.

### 3.1 Find the Right Workflow

1. Go to zapier.com
2. Find your "Intelligence Extraction" workflow
3. Click to edit it

### 3.2 Replace Google Sheets Step

1. Locate the step that writes to Google Sheets (probably after Claude extraction)
2. Click the "+" button before or after it to add a new step
3. Search for "Code by Zapier"
4. Choose "Run Python" or "Run JavaScript" (choose JavaScript)

### 3.3 Add Supabase Integration Code

1. In the code editor, delete the default code
2. Open `zapier-supabase-integration.js` from this project
3. Copy the entire contents
4. Paste into Zapier's code editor

### 3.4 Configure Variables

At the top of the code, update these lines:

```javascript
const SUPABASE_URL = 'https://xxxxx.supabase.co';  // Your Supabase URL from Step 1.4
const SUPABASE_ANON_KEY = 'eyJhbGc...';  // Your anon key from Step 1.4
```

**For security**: Use Zapier Storage for the API key:
1. Click "Storage" in Zapier's code editor
2. Add key: `supabase_anon_key`
3. Value: Your Supabase anon key
4. In code, change to: `const SUPABASE_ANON_KEY = StoreClient.getSecret('supabase_anon_key');`

### 3.5 Map Input Data

The code expects these input variables from previous steps:
- `extraction_id`
- `source_file_name`
- `meeting_type`
- `template_name`
- `completeness_score`
- etc.

Make sure these match your Zapier step outputs. You can map them in the "Input Data" section.

### 3.6 Test the Zap

1. Click "Test & Continue"
2. Zapier will run the code with sample data
3. Check for errors in the output
4. If successful, you should see: `success: true`

### 3.7 Verify Data in Supabase

1. Go to Supabase → Table Editor → extractions
2. You should see a new row with your test data
3. If you see the row, it worked!

### 3.8 Turn On the Zap

1. If test was successful, click "Publish" or "Turn On"
2. Your workflow is now live!

---

## Step 4: Verify Everything Works (5 minutes)

### 4.1 Test End-to-End

1. Create a test extraction (or wait for a real one)
2. Check that it flows through: Fathom → Drive → Zapier → Claude → Supabase
3. Go to your Vercel dashboard URL
4. You should see the new extraction appear in the "Recent Extractions" table
5. **Real-time test**: Keep dashboard open while triggering a new extraction
   - You should see it appear automatically without refreshing!

### 4.2 Check Metrics

1. Metrics cards should show counts
2. Charts should start populating (may need 2-3 data points)
3. Template performance should list your templates

---

## Step 5: Optional Enhancements

### 5.1 Set Up Custom Domain

1. Buy a domain or use a subdomain from existing domain
2. In Vercel:
   - Go to Project Settings → Domains
   - Add domain: `intelligence.360ventures.com`
   - Follow DNS configuration instructions
   - Wait for DNS propagation (can take up to 48 hours, usually < 1 hour)
3. Access your dashboard at your custom domain

### 5.2 Set Up Slack Notifications

Add a Slack integration to get notified of flagged extractions:

1. In Zapier, after the Supabase step
2. Add "Filter" step:
   - Only continue if: `flagged_for_review` is `true`
3. Add "Slack" → "Send Channel Message"
4. Message template:
   ```
   🚨 Extraction Flagged for Review

   Meeting: {{source_file_name}}
   Type: {{meeting_type}}
   Completeness: {{completeness_score}}%

   View in Dashboard: https://your-dashboard.vercel.app
   ```

### 5.3 Set Up Email Reports

Create a weekly email summary:

1. Create a new Zap
2. Trigger: Schedule (every Monday 9am)
3. Action: Webhooks → GET Request
   - URL: `https://your-project.supabase.co/rest/v1/rpc/get_dashboard_metrics`
   - Headers:
     - `apikey`: Your Supabase anon key
     - `Authorization`: `Bearer your-supabase-anon-key`
4. Action: Email or Gmail → Send Email
5. Format the metrics in email body

---

## Step 6: Maintenance & Monitoring

### Daily

- Check dashboard for flagged extractions
- Review quality trends

### Weekly

- Review weekly analysis results (when that feature is added)
- Check template performance grades
- Approve or decline improvement suggestions

### Monthly

- Review overall metrics trends
- Plan template improvements
- Check Supabase storage usage (free tier = 500MB)
- Check Vercel bandwidth usage (free tier = 100GB)

---

## Troubleshooting

### "No data available" on Dashboard

**Cause**: Dashboard can't connect to Supabase or no data in database

**Fix**:
1. Open browser console (F12 → Console tab)
2. Look for errors
3. Verify environment variables in Vercel:
   - Settings → Environment Variables
   - Check `NEXT_PUBLIC_SUPABASE_URL` and `NEXT_PUBLIC_SUPABASE_ANON_KEY`
4. Redeploy if you changed env vars:
   - Deployments → three dots → Redeploy

### Zapier Step Failing

**Cause**: Wrong Supabase credentials or malformed data

**Fix**:
1. Check Zapier task history for error message
2. Verify SUPABASE_URL and SUPABASE_ANON_KEY in code
3. Check that input data fields match variable names
4. Test with minimal data first:
   ```javascript
   const extractionData = {
     extraction_id: 'test-' + Date.now(),
     meeting_type: 'test',
     completeness_score: 75
   };
   ```

### Dashboard Not Updating in Real-Time

**Cause**: Real-time subscriptions not properly configured

**Fix**:
1. In Supabase, check Database → Replication
2. Verify `extractions` table is enabled for replication
3. In code, check browser console for subscription errors
4. Try refreshing the page

### Build Failing on Vercel

**Cause**: TypeScript errors or missing dependencies

**Fix**:
1. Check build logs in Vercel
2. Run locally to test: `npm run build`
3. Fix any TypeScript errors
4. Push fix to GitHub (auto-deploys)

---

## Next Steps

Once everything is working:

1. **Share with team**: Send dashboard URL to colleagues
2. **Set up user feedback**: Add rating mechanism in Asana
3. **Build weekly analysis**: Implement automated quality reports
4. **Create experiments**: Set up A/B testing for template improvements
5. **Add more views**: Create pages for experiments, historical analysis, etc.

---

## Support Contacts

- **Supabase**: support@supabase.com
- **Vercel**: support@vercel.com
- **Zapier**: support@zapier.com

---

## Rollback Plan

If something goes wrong and you need to go back to Google Sheets:

1. In Zapier, turn off the new step with Supabase
2. Re-enable the old Google Sheets step
3. Turn Zap back on
4. Data will flow to Google Sheets again
5. Dashboard will show historical data from Supabase but won't update

---

## Success Criteria

✅ Dashboard loads at your Vercel URL
✅ Metrics cards show data
✅ Recent extractions table populates
✅ New extraction appears in real-time
✅ Zapier successfully writes to Supabase
✅ No errors in browser console
✅ No errors in Zapier task history

---

**Congratulations! You now have a live, professional intelligence quality dashboard! 🎉**
