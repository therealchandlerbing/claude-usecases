# Relationship Intelligence Dashboard

A Next.js dashboard for viewing and managing relationship intelligence data extracted from meeting transcripts via the Make.com automation pipeline.

## Features

- **Action Center**: Review and approve AI-extracted intelligence before pushing to Asana
  - Pending relationships, commitments, service interests, signals, objections
  - Approve, decline, or edit extracted data

- **Attention Queue**: Track items needing immediate action
  - Cooling relationships (no contact in 30+ days)
  - Overdue commitments (ours and theirs)
  - Actionable signals

- **Intelligence Tab**: Strategic insights and patterns
  - Persona engagement metrics and battle cards
  - Service traction and pipeline by offering
  - Competitor battle cards
  - Objection patterns and winning responses

## Prerequisites

1. **Supabase Database**: The schema must be deployed to your Supabase project
2. **Make.com Pipeline**: The automation workflow must be configured and running
3. **Node.js 18+**: Required for Next.js 14

## Quick Start

### 1. Install Dependencies

```bash
cd relationship-intelligence/dashboard
npm install
```

### 2. Configure Environment

Copy the example environment file:

```bash
cp .env.example .env.local
```

Edit `.env.local` with your Supabase credentials:

```env
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJ...your-anon-key
```

**Getting Supabase Credentials:**
1. Go to [Supabase Dashboard](https://app.supabase.com)
2. Select your project
3. Navigate to **Settings → API**
4. Copy the **Project URL** and **anon public** key

### 3. Deploy Database Schema

If not already done, deploy the schema to Supabase:

1. Open Supabase Dashboard → SQL Editor
2. Paste contents of `../combined-schema.sql`
3. Click **Run**

### 4. Run Development Server

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

## Production Deployment

### Deploy to Vercel

```bash
npm install -g vercel
vercel
```

Add environment variables in Vercel dashboard:
- `NEXT_PUBLIC_SUPABASE_URL`
- `NEXT_PUBLIC_SUPABASE_ANON_KEY`

### Build Locally

```bash
npm run build
npm start
```

## Project Structure

```
dashboard/
├── src/
│   ├── app/
│   │   ├── globals.css      # Tailwind CSS styles
│   │   ├── layout.js        # Root layout
│   │   └── page.js          # Main page (renders dashboard)
│   ├── components/
│   │   └── RelationshipIntelligenceDashboard.jsx  # Main dashboard component
│   └── services/
│       └── supabase.js      # Supabase client and data fetching
├── .env.example             # Example environment variables
├── next.config.js           # Next.js configuration
├── tailwind.config.js       # Tailwind CSS configuration
└── package.json
```

## Data Flow

```
Fathom Transcript
       ↓
Make.com Webhook → Claude AI → JSON Extraction
       ↓
Supabase Tables (push_status = 'pending_review')
       ↓
Dashboard Action Center
       ↓
[Approve] → push_status = 'pushed' → Asana Task
[Decline] → push_status = 'declined'
[Edit]    → Update record → Review again
```

## Supabase Views Used

The dashboard queries these views and RPC functions:

| View/Function | Purpose |
|---------------|---------|
| `v_pending_review` | Items awaiting approval |
| `v_attention_queue` | Cooling relationships, overdue items |
| `v_persona_engagement` | Persona metrics (fallback) |
| `v_service_traction` | Service pipeline (fallback) |
| `v_competitor_battle_cards` | Competitor intelligence |
| `v_objection_patterns` | Objection analytics |
| `get_persona_dashboard_data()` | Enriched persona data (RPC) |
| `get_service_dashboard_data()` | Enriched service data (RPC) |

## Mock Data Mode

If Supabase environment variables are not set, the dashboard runs in mock data mode with empty arrays. This allows local development without a database connection.

## Troubleshooting

### "No data showing"

1. **Check Supabase connection**: Verify `.env.local` has correct credentials
2. **Check schema deployment**: Ensure `combined-schema.sql` was run successfully
3. **Check Make.com pipeline**: Verify transcripts are being processed

### "Error fetching data"

1. Check browser console for specific error messages
2. Verify Supabase RLS policies allow read access
3. Ensure the anon key has proper permissions

### "Views not found"

Run the full `combined-schema.sql` in Supabase SQL Editor. The schema creates all required views automatically.

### "RPC function not found"

The schema includes RPC functions `get_persona_dashboard_data()` and `get_service_dashboard_data()`. If these are missing, re-run the schema or add them manually from the schema file.

## Related Files

- `../combined-schema.sql` - Database schema with tables, views, and functions
- `../make-blueprint.json` - Original Make.com workflow (use with Supabase app)
- `../make-blueprint-corrected.json` - HTTP-based workflow (recommended)
- `../MAKE_POST_IMPORT_SETUP.md` - Make.com setup instructions

## Tech Stack

- **Framework**: Next.js 14 (App Router)
- **Styling**: Tailwind CSS
- **Icons**: Lucide React
- **Database**: Supabase (PostgreSQL)
- **Deployment**: Vercel (recommended)
