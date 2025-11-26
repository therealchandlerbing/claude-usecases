# 360 Relationship Intelligence System

A comprehensive system for extracting relationship intelligence from meeting transcripts, storing it in Supabase, and visualizing it through a React dashboard.

## Architecture

```
Fathom Transcripts → Zapier → Claude (Extract) → Google Drive (JSON)
                                                        ↓
                                                  Make.com
                                                        ↓
                                                   Supabase
                                                        ↓
                                              React Dashboard (Vercel)
```

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

### Configure Extraction Pipeline

See `MAKE_SETUP.md` for Make.com configuration.

### Deploy Dashboard

```bash
cd dashboard
npm install
npm run dev
```

For production, deploy to Vercel.

## Supabase Connection

```javascript
const supabaseUrl = 'https://pblxazslxcotbdxtvnlb.supabase.co';
const supabaseKey = 'your-anon-key';
```

## Key Views

| View | Purpose |
|------|---------|
| `v_pending_review` | Items awaiting push decision |
| `v_attention_queue` | Cooling relationships, overdue items |
| `v_portfolio_health` | Aggregated metrics |
| `v_persona_battle_cards` | Persona engagement playbooks |
| `v_service_battle_cards` | Service intelligence |
| `v_competitor_battle_cards` | Competitive positioning |

## Temperature Thresholds

- 0-30 days: Maintain current
- 30-60 days: warm → cool
- 60-90 days: cool → cold
- 90+ days: cold

Auto-calculated by database triggers.

## License

Internal use only - 360 Social Impact Studios
