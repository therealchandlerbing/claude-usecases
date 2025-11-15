# Claude Use Cases & Skills

A comprehensive collection of use cases and skills that can be deployed with Claude for specialized workflows and automation. This repository provides structured, reusable skill files optimized for various business and technical use cases.

## Overview

This repository contains:
- **Skill Templates** - Standardized templates for creating new skills
- **360 Use Cases** - Customized workflows for 360-specific processes
- **Documentation** - Guides for creating and using skills
- **Examples** - Sample implementations to get started

## Repository Structure

```
claude-usecases/
├── skills/
│   ├── 360-use-cases/           # 360-specific workflow skills
│   ├── intelligence-extractor/  # Intelligence extraction & quality monitoring
│   ├── vianeo-persona-builder/  # Vianeo persona generation & validation
│   ├── design-director/         # Design elevation & visual polish
│   └── templates/               # Templates for creating new skills
├── intelligence-dashboard/      # Live quality monitoring dashboard
├── docs/                        # Documentation and guides
├── examples/                    # Example implementations
└── README.md                   # This file
```

## Quick Start

### Using an Existing Skill

1. Browse the `skills/` directory to find relevant skills
2. Open the skill file to view instructions
3. Follow the step-by-step guidance provided in the skill

### Creating a New Skill

1. Copy the template:
   ```bash
   cp skills/templates/skill-template.md skills/360-use-cases/your-skill-name.md
   ```

2. Customize the template with your specific use case

3. Follow the guidelines in `docs/CREATING-SKILLS.md`

## Available Skills

### Research & Validation

#### Vianeo Persona Builder
**Location:** `skills/vianeo-persona-builder/`
**Category:** Research & Validation
**Purpose:** Generate validated stakeholder personas from research data and behavioral patterns following the Vianeo framework

**Key Features:**
- Analyzes interview transcripts, surveys, and behavioral data
- Enforces Vianeo four-layer persona structure
- Tracks validation evidence and provides scoring guidance
- Generates dual outputs: strategic version + platform-ready version
- Supports 4 persona types: partners, innovators, stakeholders, beneficiaries
- Predicts Vianeo Desirability scores (1-5 scale)
- **NEW:** Interactive Dashboard v2.0 with three deployment options

**Quick Links:**
- [Skill Documentation](skills/vianeo-persona-builder/README.md)
- [File Index](skills/vianeo-persona-builder/INDEX.md)
- [Examples](skills/vianeo-persona-builder/examples/)
- [Scoring Rubric](skills/vianeo-persona-builder/references/vianeo-scoring-rubric.md)
- [Interactive Dashboard](skills/vianeo-persona-builder/powerups/interactive-dashboard/README.md) ⭐ NEW

**When to Use:**
- Building personas for technology validation projects
- Documenting stakeholder needs for partnership development
- Preparing Desirability dimension documentation for Vianeo submissions
- Validating assumed needs against actual behavioral data
- Creating interactive presentations for stakeholders

**Optional Powerups:**
- **Interactive Dashboard v2.0** - Explore personas through a beautiful web interface with three implementation options:
  - **Standalone HTML** (Easiest) - Zero dependencies, just open in browser
  - **Portable JSX** - Single-file React component for quick deployment
  - **Modular TypeScript** - Production-ready component architecture

---

### Design & Visual Excellence

#### Design Director
**Location:** `skills/design-director/`
**Category:** Design & Visual Excellence
**Purpose:** Transform functional outputs into professionally polished, design-elevated work through systematic application of contemporary design best practices

**Key Features:**
- Elevates 5 output types: presentations, spreadsheets, HTML/web, reports, dashboards
- Follows 6-phase systematic elevation protocol
- References 7 design exemplars: Stripe, Linear, Apple, Notion, Bauhaus, Swiss Design, Brutalism
- Applies 40+ specific design techniques across typography, color, layout, hierarchy
- Ensures hand-crafted appearance (not template-based)
- WCAG AA accessibility compliance by default
- Context-appropriate design matching (audience, purpose, medium)

**Quick Links:**
- [Quick Reference](skills/design-director/QUICK-REFERENCE.md) ⭐ Start here
- [Complete Guide](skills/design-director/COMPLETE-GUIDE.md)
- [Skill Documentation](skills/design-director/README.md)
- [File Index](skills/design-director/INDEX.md)
- [Examples](skills/design-director/examples/)
- [Design Philosophy](skills/design-director/references/design-philosophy.md)
- [Technique Catalog](skills/design-director/references/technique-catalog.md)

**When to Use:**
- Elevating functional outputs to professional design quality
- Creating polished dashboards, presentations, and reports
- Building web interfaces that match contemporary standards
- Ensuring visual consistency across deliverables
- Making data-heavy outputs scannable and beautiful

**Reference Documentation:**
- **Design Philosophy** - Core principles and decision framework
- **Interrogation Checklist** - Comprehensive evaluation criteria
- **Technique Catalog** - 40+ specific design techniques
- **Design Exemplars** - Patterns from Stripe, Linear, Apple, and more
- **Elevation Protocol** - Complete 6-phase systematic process

---

### Data Intelligence & Quality Monitoring

#### Intelligence Extractor
**Location:** `skills/intelligence-extractor/`
**Category:** Data Intelligence & Quality Monitoring
**Purpose:** Extract structured partnership, funding, and stakeholder intelligence from meeting transcripts with real-time quality monitoring

**Key Features:**
- 10 meeting-type specific prompt templates
- Live web dashboard for quality monitoring
- Automated completeness scoring and quality tracking
- Template performance analytics
- Real-time updates via Supabase + Vercel
- Zapier integration for automation
- Cultural intelligence capture for cross-cultural contexts

**Quick Links:**
- [Skill Documentation](skills/intelligence-extractor/README.md)
- [Template Selection Guide](skills/intelligence-extractor/templates/00-template-selection-guide.md) ⭐ Start here
- [Cross-Linking Architecture](skills/intelligence-extractor/references/cross-linking-architecture.md) ⭐ NEW
- [Intelligence Schemas](skills/intelligence-extractor/references/intelligence-schemas.md) ⭐ NEW
- [File Index](skills/intelligence-extractor/INDEX.md)
- [Live Dashboard](intelligence-dashboard/README.md)
- [Dashboard Deployment Guide](intelligence-dashboard/DEPLOYMENT_GUIDE.md)
- [Dashboard Overview](INTELLIGENCE_DASHBOARD_SUMMARY.md)

**When to Use:**
- Extracting intelligence from partnership meetings
- Capturing funder relationship and application intelligence
- Profiling stakeholders and board members
- Monitoring extraction quality and template performance
- Cross-cultural meeting intelligence
- Community stakeholder engagement documentation
- Crisis or problem-solving meeting analysis

**Template Types:**
1. **Partnership New** - First meeting with potential partner
2. **Partnership Existing** - Follow-up with established partner
3. **Funder Initial** - First contact with funding source
4. **Funder Application** - Grant discussion, LOI feedback
5. **Board Governance** - Board meetings, governance sessions
6. **Client Sprint** - Working sessions, strategic planning
7. **Community Stakeholder** - Grassroots leaders, community orgs
8. **International Partner** - Cross-cultural meetings
9. **Conference Networking** - Brief networking interactions
10. **Crisis Problem-Solving** - Emergency, conflict resolution

**Intelligence System Architecture:** ⭐ NEW
- **Three-Layer Integration** - Partnership (HOW), Funding (RESOURCES), and Stakeholder (WHO) Intelligence work together as an interconnected ecosystem
- **Cross-Linking Mechanisms** - Task relationships, shared custom fields, and naming conventions enable portfolio views
- **Information Flow Patterns** - Structured workflows for discovery cascades and relationship evolution
- **Dashboard Views** - Cross-system queries for relationship health monitoring and strategic opportunity spotting
- See [Cross-Linking Architecture](skills/intelligence-extractor/references/cross-linking-architecture.md) for complete implementation guide

**Live Dashboard Features:**
- Real-time metrics tracking (extractions, completeness, ratings)
- 30-day quality trend visualization
- Template performance comparison
- Recent activity feed with live updates
- Automated quality flags and alerts
- Free hosting on Vercel + Supabase

**Technology Stack:**
- **Extraction**: Claude API + Zapier automation
- **Database**: Supabase (PostgreSQL with real-time subscriptions)
- **Dashboard**: Next.js 14 + TypeScript + Tailwind CSS
- **Hosting**: Vercel (auto-deploy from GitHub)
- **Charts**: Recharts for data visualization

**Cost:** Free tier available (Supabase 500MB + Vercel 100GB bandwidth)

#### Partnership Intelligence Dashboard
**Location:** `intelligence-dashboard/src/components/partnership/` ⭐ NEW
**Category:** Strategic Intelligence & Decision Support
**Purpose:** Professional dashboard for navigating partnership conversations with data-driven intelligence from 40+ historical partnerships

**Key Features:**
- 4 partner type profiles: JV Partners, Brazil Tech Transfer, US Corporate/VC, Foundations
- Success patterns and timelines based on real partnership data (25-60% success rates, 4-11 month timelines)
- Value alignment and cultural communication strategies
- Qualification questions organized by decision criteria
- Common hesitations with proven response frameworks
- Walk-away signals to identify poor partnership fit
- Comparison view across all partner types with strategic recommendations
- Professional design with smooth animations and visual hierarchy

**Quick Links:**
- [Component Documentation](intelligence-dashboard/src/components/partnership/README.md)
- [Live Demo Route](intelligence-dashboard/src/app/partnership/page.tsx)
- Access at `/partnership` when running the intelligence dashboard

**When to Use:**
- Preparing for partnership conversations and qualifying potential partners
- Training team members on partnership patterns and decision criteria
- Understanding decision-making timelines by partner type
- Navigating cultural differences in partnership approaches (Brazil vs US)
- Building confidence in objection handling and hesitation responses
- Making data-driven decisions about which partnerships to pursue

**Design Highlights:**
- Modular TypeScript component architecture with 8 specialized components
- Tailwind CSS with custom animations and gradient backgrounds
- Responsive design optimized for all screen sizes
- Smooth transitions (200-300ms) and hover states throughout
- Color-coded success indicators (green ≥50%, yellow ≥30%, orange <30%)
- Progressive disclosure through tabbed interface
- Professional polish matching contemporary design standards

**Intelligence Captured:**
- 63 total partnerships explored across 4 partner types
- Historical success rates: Brazil (60%), Foundations (28%), US Corp (27%), JV (25%)
- Average timelines: US Corp (4.2 mo), Brazil (6.8 mo), Foundation (8.5 mo), JV (11.5 mo)
- 40+ qualification questions, 30+ hesitation responses, 24 walk-away signals
- Partner-specific patterns, cultural insights, and strategic framing guidance

---

### 360 Use Cases
Skills customized for 360 workflows are located in `skills/360-use-cases/`

*Additional 360 skills will be listed here as they are added*

## Documentation

- [Creating Skills Guide](docs/CREATING-SKILLS.md) - Comprehensive guide for creating new skills
- [Skill Template](skills/templates/skill-template.md) - Template for new skills

## Contributing

When adding new skills:
1. Use the provided template
2. Follow naming conventions (lowercase-with-hyphens)
3. Place skills in appropriate category folders
4. Update this README with links to new skills
5. Test thoroughly before committing

## Use Cases

This repository supports:
- Workflow automation
- Standardized processes
- Knowledge management
- Task templates
- Custom Claude behaviors
- Repeatable analysis patterns

## Getting Started

The best way to get started is to:
1. Review the documentation in `docs/CREATING-SKILLS.md`
2. Examine the skill template in `skills/templates/`
3. Look at examples in the `examples/` directory
4. Create your first skill using the template

## License

[Add your license information here]

## Recent Additions

### Intelligence System Cross-Linking Architecture (November 2025) ⭐ NEW
Comprehensive architecture for integrating the three intelligence systems:
- **Three-layer model**: Partnership (HOW), Funding (RESOURCES), Stakeholder (WHO) Intelligence
- **Technical linking mechanisms**: Task relationships, shared custom fields, naming conventions
- **Information flow patterns**: Discovery cascades, reverse cascades, relationship evolution
- **Workflow integration**: Meeting prep, grant applications, quarterly portfolio reviews
- **Dashboard views**: Cross-system queries for ecosystem views and relationship health monitoring
- **Implementation roadmap**: 3-month plan from foundation to pattern recognition
- See [Cross-Linking Architecture](skills/intelligence-extractor/references/cross-linking-architecture.md) and [Intelligence Schemas](skills/intelligence-extractor/references/intelligence-schemas.md)

### Partnership Intelligence Dashboard (November 2025) ⭐ NEW
Strategic partnership navigation dashboard with intelligence from 40+ historical partnerships:
- 4 partner type profiles (JV, Brazil Tech, US Corp/VC, Foundations)
- 35% overall success rate with 7.8 month average timeline
- 40+ qualification questions, 30+ hesitation responses, 24 walk-away signals
- Professional design with interactive components and comparison view
- Built with modern React/TypeScript, integrated at `/partnership` route
- See [PARTNERSHIP_DASHBOARD_SUMMARY.md](PARTNERSHIP_DASHBOARD_SUMMARY.md) for complete overview

### Intelligence Extractor + Live Dashboard (November 2025)
Complete intelligence extraction and quality monitoring system with:
- 10 specialized extraction templates for different meeting types
- Professional web dashboard with real-time updates
- Automated quality tracking and analytics
- Template performance monitoring
- 15-minute deployment to production
- See [INTELLIGENCE_DASHBOARD_SUMMARY.md](INTELLIGENCE_DASHBOARD_SUMMARY.md) for complete overview

## Version

Current Version: 1.2.0
Last Updated: 2025-11-15 
