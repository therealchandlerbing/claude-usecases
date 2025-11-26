# 360 Relationship Intelligence System

A comprehensive system for extracting relationship intelligence from meeting transcripts, storing it in Supabase, and visualizing it through a React dashboard.

## Architecture

### Option A: Direct Pipeline (Recommended)

```
Fathom → Make.com (Webhook) → Claude API → Supabase → Dashboard (Vercel)
```

Single platform, faster processing, easier debugging. See `MAKE_DIRECT_SETUP.md`.

### Option B: Zapier + Make.com Pipeline

```
Fathom → Zapier → Claude → Google Drive (JSON) → Make.com → Supabase → Dashboard
```

Uses existing Zapier setup, stores JSON intermediates. See `MAKE_SETUP.md`.

## Components

### 1. Database Schema (`combined-schema.sql`)

Core tables:
- `relationships` - People and organizations
- `interactions` - Meeting history
- `commitments` - Two-way promise tracking
- `signals` - Strategic intelligence
- `introductions` - Network flow tracking

Intelligence tables:
- `persona_archetypes` - Engagement playbooks by persona type
- `services` - 360's service offerings
- `service_interest` - Links relationships to services
- `objections` - Battle intelligence
- `competitor_intel` - Competitive positioning
- `proof_points` - Evidence tracking

### 2. Extraction Prompt (`meeting-intelligence-extractor-v2.md`)

Claude prompt that extracts:
- Persona classification
- Service interest signals
- Commitments (ours and theirs)
- Strategic signals
- Objections with responses
- Competitor mentions
- Proof point effectiveness
- Engagement insights

### 3. React Dashboard (`dashboard/`)

Four main views:
- **Action Center** - Process new extractions, handle attention items
- **Persona Playbooks** - Engagement guidance by persona type
- **Service Traction** - Pipeline by service offering
- **Battle Intelligence** - Competitors and objection patterns

## Setup

### Deploy Database

1. Go to Supabase SQL Editor
2. Paste entire `combined-schema.sql`
3. Click Run
4. Verify tables in Table Editor

The schema includes:
- 17 tables (core + intelligence)
- 13 views for dashboard queries
- 9 functions (triggers, scheduled jobs, and dashboard RPC)
- Seed data for persona archetypes and services

### Configure Extraction Pipeline

#### Make.com Blueprint Files

| File | Description | Use When |
|------|-------------|----------|
| `make-blueprint-corrected.json` | **Recommended** - Uses HTTP modules for Supabase REST API | New setups, or if Supabase modules give "Module Not Found" errors |
| `make-blueprint.json` | Uses Supabase native app modules | You have Supabase app installed and prefer native modules |

**After importing either blueprint:**
- See `MAKE_POST_IMPORT_SETUP.md` for step-by-step configuration
- You'll need to configure: Supabase connection, Anthropic API key, Webhook URL

**Detailed Setup Guides:**

**Option A (Recommended):** Direct Fathom → Make.com → Claude → Supabase
- See `MAKE_DIRECT_SETUP.md` for complete setup

**Option B:** Existing Zapier flow with Make.com for database inserts
- See `MAKE_SETUP.md` for Google Drive → Make.com → Supabase setup

### Deploy Dashboard to Vercel

**Local Development:**
```bash
cd dashboard
npm install
cp .env.example .env.local
# Edit .env.local with your Supabase anon key
npm run dev
```

**Production Deployment:**

1. Push code to GitHub (already done)

2. Go to [vercel.com](https://vercel.com) → **Add New Project**

3. Import the GitHub repository

4. Configure:
   - **Root Directory**: `relationship-intelligence/dashboard`
   - **Framework Preset**: Next.js (auto-detected)

5. Add Environment Variables:
   ```
   NEXT_PUBLIC_SUPABASE_URL = https://pblxazslxcotbdxtvnlb.supabase.co
   NEXT_PUBLIC_SUPABASE_ANON_KEY = (your anon key)
   ```

6. Click **Deploy**

**After Deployment:**
- Dashboard will be live at: `https://your-project.vercel.app`
- Auto-deploys on every push to main branch

**For more dashboard details:** See `dashboard/README.md`

## Supabase Connection

```javascript
const supabaseUrl = 'https://pblxazslxcotbdxtvnlb.supabase.co';
const supabaseKey = 'your-anon-key';
```

## Key Views & Functions

| View/Function | Purpose |
|---------------|---------|
| `v_pending_review` | Items awaiting push decision |
| `v_attention_queue` | Cooling relationships, overdue items |
| `v_portfolio_health` | Aggregated metrics |
| `v_persona_battle_cards` | Persona engagement playbooks |
| `v_service_battle_cards` | Service intelligence |
| `v_competitor_battle_cards` | Competitive positioning |
| `v_persona_engagement` | Persona metrics for dashboard |
| `v_service_traction` | Service pipeline for dashboard |
| `get_persona_dashboard_data()` | RPC: Enriched persona data |
| `get_service_dashboard_data()` | RPC: Enriched service data |

## Temperature Thresholds

- 0-30 days: Maintain current
- 30-60 days: warm → cool
- 60-90 days: cool → cold
- 90+ days: cold

Auto-calculated by database triggers.

## License

Internal use only - 360 Social Impact Studios
