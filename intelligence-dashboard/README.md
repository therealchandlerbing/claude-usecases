# Intelligence Extraction Quality Dashboard

Real-time web dashboard for monitoring and analyzing partnership, funding, and stakeholder intelligence extraction quality.

## Features

- **Real-time Updates**: Dashboard updates live as new extractions are processed
- **Quality Metrics**: Track completeness, user ratings, and flags across all extractions
- **Template Performance**: Monitor which extraction templates perform best
- **Trend Analysis**: Visualize quality trends over 30 days
- **Recent Activity**: See latest extractions with drill-down capabilities

## Tech Stack

- **Frontend**: Next.js 14 + React + TypeScript
- **Styling**: Tailwind CSS
- **Database**: Supabase (PostgreSQL with real-time subscriptions)
- **Charts**: Recharts
- **Hosting**: Vercel (auto-deploy from GitHub)
- **Data Pipeline**: Zapier → Claude → Supabase

## Architecture

```
Fathom Transcripts → Google Drive → Zapier → Claude Extraction → Supabase
                                                                      ↓
                                                             Next.js Dashboard
                                                                      ↓
                                                          Vercel (Auto-deploy)
```

## Setup Instructions

### 1. Set Up Supabase Database

1. Go to [supabase.com](https://supabase.com) and create a new project
2. Wait for the project to initialize (2-3 minutes)
3. Go to the SQL Editor in Supabase
4. Copy the contents of `supabase-schema.sql` and run it
5. Verify tables were created:
   - extractions
   - experiments
   - edits
   - weekly_analyses
6. Go to Project Settings → API to get your credentials:
   - **Project URL**: `https://your-project.supabase.co`
   - **Anon/Public Key**: `eyJhbGc...` (long string)

### 2. Configure Environment Variables

1. Copy `.env.local.example` to `.env.local`:
   ```bash
   cp .env.local.example .env.local
   ```

2. Edit `.env.local` and add your Supabase credentials:
   ```
   NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
   NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key-here
   ```

### 3. Install Dependencies

```bash
npm install
```

### 4. Run Development Server

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to see the dashboard.

### 5. Deploy to Vercel

#### Option A: Deploy via Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel

# Follow prompts to:
# - Link to your GitHub repo (recommended)
# - Add environment variables
# - Deploy to production
```

#### Option B: Deploy via GitHub Integration

1. Push this code to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Intelligence Dashboard"
   git remote add origin git@github.com:yourusername/intelligence-dashboard.git
   git push -u origin main
   ```

2. Go to [vercel.com](https://vercel.com)
3. Click "Add New Project"
4. Import your GitHub repository
5. Configure environment variables in Vercel:
   - `NEXT_PUBLIC_SUPABASE_URL`
   - `NEXT_PUBLIC_SUPABASE_ANON_KEY`
6. Click "Deploy"

**Auto-deployment**: Every push to `main` will automatically trigger a new deployment.

### 6. Configure Zapier to Write to Supabase

1. In your Zapier extraction workflow, find the step that currently writes to Google Sheets
2. Replace it with "Code by Zapier" action
3. Copy the code from `zapier-supabase-integration.js`
4. Update the configuration variables at the top:
   ```javascript
   const SUPABASE_URL = 'https://your-project.supabase.co';
   const SUPABASE_ANON_KEY = 'your-anon-key';  // Use Zapier Storage for security
   ```
5. Test the Zap to ensure data flows to Supabase
6. Check your dashboard to see the real-time update

### 7. Optional: Set Up Custom Domain

In Vercel:
1. Go to Project Settings → Domains
2. Add your custom domain (e.g., `intelligence.360ventures.com`)
3. Configure DNS records as instructed
4. Enable HTTPS (automatic with Vercel)

## Usage

### Viewing the Dashboard

The dashboard shows:

1. **Metrics Cards** (top row):
   - Total extractions (last 7 days)
   - Average completeness score
   - Average user rating
   - Flagged rate
   - All with trend indicators vs. previous week

2. **Quality Trend Chart** (left):
   - 30-day line chart showing completeness and user rating trends

3. **Template Performance** (right):
   - List of all templates with performance grades
   - Shows completeness, rating, and edit count for each

4. **Recent Extractions Table** (bottom):
   - Last 10 extractions with details
   - Real-time updates as new extractions arrive

### Real-Time Updates

The dashboard automatically refreshes when:
- New extractions are added to Supabase
- Existing extractions are updated
- Edits are recorded

You'll see changes appear instantly without refreshing the page.

### Embedding Metrics

You can embed dashboard metrics in other tools:

```html
<!-- Embed completeness metric -->
<iframe src="https://your-dashboard.vercel.app/api/metrics?metric=completeness" width="200" height="100"></iframe>
```

## Development

### Project Structure

```
intelligence-dashboard/
├── src/
│   ├── app/                      # Next.js app directory
│   │   ├── layout.tsx            # Root layout
│   │   ├── page.tsx              # Main dashboard page
│   │   └── globals.css           # Global styles
│   ├── components/
│   │   ├── dashboard/            # Dashboard-specific components
│   │   │   ├── MetricsCards.tsx
│   │   │   ├── QualityTrend.tsx
│   │   │   ├── TemplatePerformance.tsx
│   │   │   └── RecentExtractions.tsx
│   │   └── ui/                   # Reusable UI components
│   ├── lib/
│   │   └── supabase.ts           # Supabase client setup
│   └── types/
│       └── database.ts           # TypeScript types for database
├── public/                        # Static files
├── supabase-schema.sql           # Database schema
├── zapier-supabase-integration.js # Zapier integration code
└── package.json
```

### Adding New Features

#### Add a New Dashboard Page

1. Create a new file in `src/app/[page-name]/page.tsx`
2. Import and use Supabase client:
   ```typescript
   import { supabase } from '@/lib/supabase';

   const { data } = await supabase.from('extractions').select('*');
   ```

#### Add a New Chart

1. Create component in `src/components/charts/`
2. Use Recharts or Chart.js for visualization
3. Subscribe to real-time updates:
   ```typescript
   useEffect(() => {
     const channel = supabase
       .channel('my-channel')
       .on('postgres_changes', { event: '*', schema: 'public', table: 'extractions' },
         payload => {
           // Update chart data
         })
       .subscribe();
     return () => channel.unsubscribe();
   }, []);
   ```

### Database Queries

Use Supabase RPC functions for complex queries:

```typescript
// Call a database function
const { data } = await supabase.rpc('get_dashboard_metrics');

// Standard query
const { data } = await supabase
  .from('extractions')
  .select('*')
  .eq('flagged_for_review', true)
  .order('created_at', { ascending: false });

// With filters
const { data } = await supabase
  .from('extractions')
  .select('*')
  .gte('completeness_score', 80)
  .lte('created_at', '2025-01-01');
```

## Cost Estimate

### Free Tier (Recommended to Start)

- **Supabase**: Free tier includes:
  - 500MB database storage
  - 2GB bandwidth
  - Unlimited API requests
  - Real-time subscriptions

- **Vercel**: Free tier includes:
  - Unlimited deployments
  - 100GB bandwidth
  - Automatic HTTPS
  - Custom domains

**Total Cost: $0/month**

### Paid Tier (If You Outgrow Free)

- **Supabase Pro**: $25/month
  - 8GB database storage
  - 50GB bandwidth
  - Better performance

- **Vercel Pro**: $20/month
  - More team features
  - Analytics
  - Better support

**Total Cost: ~$45/month**

This is approximately what you'd pay for advanced Google Sheets + Zapier integrations, but with a much more professional, scalable solution.

## Troubleshooting

### Dashboard Shows "No data available"

1. Check Supabase connection:
   ```bash
   # In browser console
   console.log(process.env.NEXT_PUBLIC_SUPABASE_URL)
   ```
2. Verify database has data:
   - Go to Supabase → Table Editor → extractions
   - Check if there are rows
3. Test database function:
   - Go to Supabase → SQL Editor
   - Run: `SELECT get_dashboard_metrics();`

### Real-time Updates Not Working

1. Verify real-time is enabled:
   - Go to Supabase → Database → Replication
   - Ensure `extractions` table is enabled
2. Check browser console for subscription errors
3. Verify RLS policies allow read access

### Zapier Integration Failing

1. Check Supabase URL and API key in Zapier Code step
2. Look at Zapier task history for error messages
3. Test with simple data first:
   ```javascript
   const testData = {
     extraction_id: 'test-123',
     meeting_type: 'test',
     completeness_score: 75
   };
   ```
4. Verify API response in Zapier output

### Deployment Issues

1. Check build logs in Vercel
2. Ensure all environment variables are set
3. Verify TypeScript has no errors:
   ```bash
   npm run build
   ```

## Support

For issues or questions:
1. Check Supabase docs: https://supabase.com/docs
2. Check Next.js docs: https://nextjs.org/docs
3. Check Vercel docs: https://vercel.com/docs

## License

MIT
