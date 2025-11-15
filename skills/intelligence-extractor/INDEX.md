# Intelligence Extractor - File Index

Complete index of all files in the Intelligence Extractor skill.

## Core Documentation

| File | Purpose | Start Here? |
|------|---------|-------------|
| [README.md](README.md) | Main documentation and overview | ✅ YES |
| [INDEX.md](INDEX.md) | This file - complete file listing | For reference |

## Templates (Prompt Engineering)

### Selection Guide
| File | Purpose |
|------|---------|
| [00-template-selection-guide.md](templates/00-template-selection-guide.md) | Quick reference for choosing the right template |

### Core Templates
| # | File | Meeting Type | Complexity | Avg Completeness |
|---|------|--------------|------------|------------------|
| 1 | [01-partnership-new.md](templates/01-partnership-new.md) | New partnership exploration | Medium | 82% |
| 2 | [02-partnership-existing.md](templates/02-partnership-existing.md) | Existing partnership check-in | Low | 78% |
| 3 | [03-funder-initial.md](templates/03-funder-initial.md) | Funder initial contact | High | 76% |
| 4 | [04-funder-application.md](templates/04-funder-application.md) | Grant application discussion | Medium | 84% |
| 5 | [05-board-governance.md](templates/05-board-governance.md) | Board/governance meetings | High | 91% |
| 6 | [06-client-sprint.md](templates/06-client-sprint.md) | Client sprint/planning | High | 79% |
| 7 | [07-community-stakeholder.md](templates/07-community-stakeholder.md) | Community stakeholder | High | 85% |
| 8 | [08-international-partner.md](templates/08-international-partner.md) | International/cross-cultural | High | 87% |
| 9 | [09-conference-networking.md](templates/09-conference-networking.md) | Conference/networking | Low | 71% |
| 10 | [10-crisis-problem-solving.md](templates/10-crisis-problem-solving.md) | Crisis/problem-solving | Medium | 81% |

**Note:** Full template content provided in original specification. Templates include:
- Meeting context fields
- Extraction priorities
- Stakeholder extraction guidance
- Pattern recognition lists
- Cultural considerations
- Output requirements
- Confidence calibration

## Reference Documentation

| File | Purpose |
|------|---------|
| [intelligence-schemas.md](references/intelligence-schemas.md) | JSON schemas for all intelligence types |
| [quality-framework.md](references/quality-framework.md) | Quality assessment and scoring framework |
| [cultural-intelligence.md](references/cultural-intelligence.md) | Cross-cultural communication patterns and guidance |

## Examples

| File | Demonstrates |
|------|-------------|
| [partnership-extraction-example.md](examples/partnership-extraction-example.md) | Full partnership extraction walkthrough |
| [funder-extraction-example.md](examples/funder-extraction-example.md) | Funding intelligence extraction |
| [stakeholder-extraction-example.md](examples/stakeholder-extraction-example.md) | Stakeholder profile creation |

## Related Systems

### Live Dashboard
| File | Purpose |
|------|---------|
| [../../intelligence-dashboard/README.md](../../intelligence-dashboard/README.md) | Dashboard technical documentation |
| [../../intelligence-dashboard/DEPLOYMENT_GUIDE.md](../../intelligence-dashboard/DEPLOYMENT_GUIDE.md) | Step-by-step deployment instructions |
| [../../intelligence-dashboard/supabase-schema.sql](../../intelligence-dashboard/supabase-schema.sql) | Database schema |
| [../../intelligence-dashboard/zapier-supabase-integration.js](../../intelligence-dashboard/zapier-supabase-integration.js) | Zapier integration code |
| [../../INTELLIGENCE_DASHBOARD_SUMMARY.md](../../INTELLIGENCE_DASHBOARD_SUMMARY.md) | High-level dashboard overview |

### Dashboard Components
| Directory | Contains |
|-----------|----------|
| [../../intelligence-dashboard/src/app/](../../intelligence-dashboard/src/app/) | Next.js pages and layouts |
| [../../intelligence-dashboard/src/components/dashboard/](../../intelligence-dashboard/src/components/dashboard/) | Dashboard React components |
| [../../intelligence-dashboard/src/lib/](../../intelligence-dashboard/src/lib/) | Supabase client and utilities |
| [../../intelligence-dashboard/src/types/](../../intelligence-dashboard/src/types/) | TypeScript type definitions |

## Quick Navigation

### For First-Time Users
1. Read [README.md](README.md) - Overview and key features
2. Review [Template Selection Guide](templates/00-template-selection-guide.md) - Choose your template
3. Check [Examples](examples/) - See it in action
4. Deploy [Dashboard](../../intelligence-dashboard/DEPLOYMENT_GUIDE.md) - Set up monitoring

### For Template Users
1. [Template Selection Guide](templates/00-template-selection-guide.md) - Pick the right template
2. Review template-specific file (01-10)
3. Fill in context fields
4. Paste transcript and extract

### For Administrators
1. [Quality Framework](references/quality-framework.md) - Understanding quality metrics
2. [Dashboard Documentation](../../intelligence-dashboard/README.md) - System monitoring
3. [Database Schema](../../intelligence-dashboard/supabase-schema.sql) - Data structure
4. [Zapier Integration](../../intelligence-dashboard/zapier-supabase-integration.js) - Automation setup

### For Developers
1. [Intelligence Schemas](references/intelligence-schemas.md) - JSON output formats
2. [Dashboard Source Code](../../intelligence-dashboard/src/) - Frontend implementation
3. [Supabase Functions](../../intelligence-dashboard/supabase-schema.sql) - Backend queries
4. [TypeScript Types](../../intelligence-dashboard/src/types/database.ts) - Type definitions

## File Organization

```
intelligence-extractor/
├── README.md                          # Main documentation
├── INDEX.md                           # This file
│
├── templates/                         # Prompt templates
│   ├── 00-template-selection-guide.md # Quick reference
│   ├── 01-partnership-new.md
│   ├── 02-partnership-existing.md
│   ├── 03-funder-initial.md
│   ├── 04-funder-application.md
│   ├── 05-board-governance.md
│   ├── 06-client-sprint.md
│   ├── 07-community-stakeholder.md
│   ├── 08-international-partner.md
│   ├── 09-conference-networking.md
│   └── 10-crisis-problem-solving.md
│
├── references/                        # Reference documentation
│   ├── intelligence-schemas.md        # JSON schemas
│   ├── quality-framework.md           # Quality metrics
│   └── cultural-intelligence.md       # Cross-cultural guidance
│
└── examples/                          # Usage examples
    ├── partnership-extraction-example.md
    ├── funder-extraction-example.md
    └── stakeholder-extraction-example.md
```

## Version Information

- **Current Version:** 1.0.0
- **Last Updated:** 2025-01-15
- **Templates:** 10 specialized templates
- **Dashboard:** Next.js 14 + Supabase + Vercel
- **Integration:** Zapier + Claude API

## External Dependencies

- **Claude API** - For intelligence extraction
- **Supabase** - PostgreSQL database with real-time
- **Vercel** - Dashboard hosting
- **Zapier** - Workflow automation
- **Asana** - Intelligence task management (optional)

## Support Resources

- Dashboard issues: See `intelligence-dashboard/README.md`
- Template questions: Review template-specific guidance
- Quality concerns: See `references/quality-framework.md`
- Integration help: Check `intelligence-dashboard/zapier-supabase-integration.js`

---

**Quick Links:**
- [Main README](README.md)
- [Template Selection](templates/00-template-selection-guide.md)
- [Live Dashboard](../../intelligence-dashboard/README.md)
- [Deployment Guide](../../intelligence-dashboard/DEPLOYMENT_GUIDE.md)
