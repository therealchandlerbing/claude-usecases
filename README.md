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

#### Vianeo Business Validation Framework
**Location:** `skills/vianeo-validation-framework/`
**Category:** Research & Validation
**Purpose:** Comprehensive business validation toolkit for conducting validation sprints using the Vianeo platform and methodology

**Key Features:**
- Two complementary assessment instruments (40-question diagnostic + 29-question market maturity)
- Vianeo 5-dimension framework alignment (Legitimacy, Desirability, Acceptability, Feasibility, Viability)
- Platform character limits reference with writing strategies
- Sprint execution guide with common pitfalls and solutions
- Needs Qualification Matrix prioritization tool
- Evidence-based scoring guidance and quality standards

**Quick Links:**
- [Framework Documentation](skills/vianeo-validation-framework/README.md) ⭐ Start here
- [File Index](skills/vianeo-validation-framework/INDEX.md)
- [40-Question Diagnostic Scan](skills/vianeo-validation-framework/references/40-question-diagnostic-scan.md)
- [29-Question Market Maturity Assessment](skills/vianeo-validation-framework/references/29-question-market-maturity-assessment.md)
- [Platform Character Limits](skills/vianeo-validation-framework/references/platform-character-limits.md)
- [Sprint Execution Guide](skills/vianeo-validation-framework/references/sprint-execution-guide.md)
- [Needs Qualification Matrix](skills/vianeo-validation-framework/tools/needs-qualification-matrix.md)

**When to Use:**
- Preparing comprehensive Vianeo platform submissions
- Conducting systematic business validation sprints
- Assessing project maturity and market readiness
- Identifying validation gaps across 5 Vianeo dimensions
- Prioritizing customer needs and target segments
- Training teams on validation quality standards

**Framework Components:**
1. **Assessment Instruments:** 40-question diagnostic (internal maturity) + 29-question assessment (market validation)
2. **Platform Specifications:** Complete character limit reference for all Vianeo fields
3. **Execution Guidance:** Common pitfalls and tested solutions for validation work
4. **Analysis Tools:** Needs Qualification Matrix for systematic prioritization

**Vianeo Submission Targets:**
- **Competitive:** All dimensions ≥ 3.0, overall ≥ 3.5
- **Strong:** All dimensions ≥ 3.5, overall ≥ 4.0
- **Exceptional:** All dimensions ≥ 4.0, overall ≥ 4.5

---

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

### Executive Communication & Strategic Briefing

#### 360 Executive Brief / Newsletter Generator
**Location:** `skills/360-newsletter-generator/`
**Category:** Executive Communication & Strategic Briefing
**Purpose:** Generate executive intelligence briefs and stakeholder newsletters synthesizing updates from Asana, Gmail, and Google Drive into interactive dashboards

**Key Features:**
- Two output formats: Executive Brief (primary - confidential) + General Newsletter (secondary - shareable)
- Multi-source data integration (Asana 70%, Gmail 20%, Drive 10%)
- Automatic significance scoring and lead story selection
- Modern executive dashboard design with fixed sidebar navigation
- Interactive Chart.js visualizations (4+ charts per report)
- Print-friendly PDF export
- Content analysis and prioritization framework
- Quality assurance and tone consistency checks

**Quick Links:**
- [Skill Documentation](skills/360-newsletter-generator/README.md) ⭐ Start here
- [Data Collection Guide](skills/360-newsletter-generator/references/data-collection-guide.md)
- [Content Analysis Framework](skills/360-newsletter-generator/references/content-analysis-framework.md)
- [Writing Style Guide](skills/360-newsletter-generator/references/writing-style-guide.md)
- [Chart Specifications](skills/360-newsletter-generator/references/chart-specifications.md)

**When to Use:**
- Creating board updates and investor briefings (primary use case)
- Producing executive intelligence dashboards with confidential data
- Generating leadership briefs with financial and operational metrics
- Synthesizing comprehensive organizational updates for executives
- Generating weekly/monthly newsletters for stakeholders and partners (secondary use case)
- Preparing pre-meeting briefings with talking points

**Two Use Cases:**
1. **360 Executive Brief** (Primary) - Confidential intelligence including financials, HR updates, investment data, and strategic decisions
2. **360 Newsletter** (Secondary) - Public/stakeholder-appropriate content with high-level updates and impact stories

**Newsletter Structure:**
- Executive Summary with 3-4 key highlight cards
- Partnerships & Ecosystem section
- Programs & Innovation updates
- Impact & Outcomes metrics
- Operations & Capacity information
- Strategic Horizon planning

**Visual Components:**
- Color-coded sections (partnerships blue, operations green, strategy orange)
- Metric cards with trend indicators
- Status badges (CRITICAL, ACTION REQUIRED, MONITORING)
- Interactive charts (doughnut, bar, radar, line)

**Data Sources:**
- **Asana:** Project progress, task velocity, milestone tracking
- **Gmail:** Partnership communications, client interactions
- **Google Drive:** Reports, deliverables, impact documentation

---

### 360 Use Cases
Skills customized for 360 workflows are located in `skills/360-use-cases/`

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

### Vianeo Business Validation Framework (November 2025) ⭐ NEW
Comprehensive business validation toolkit for Vianeo platform submissions:
- **Dual assessment instruments**: 40-question diagnostic (internal maturity) + 29-question market assessment (5-dimension validation)
- **Vianeo 5-dimension framework**: Complete alignment with Legitimacy, Desirability, Acceptability, Feasibility, Viability
- **Platform specifications**: Character limits reference for all Vianeo fields with writing strategies
- **Sprint execution guide**: Common pitfalls and tested solutions based on real validation work
- **Needs Qualification Matrix**: Systematic prioritization tool (importance × satisfaction evaluation)
- **Evidence-based scoring**: Detailed guidance for scores 1-5 with validation thresholds
- **Submission targets**: Competitive (≥3.5), Strong (≥4.0), Exceptional (≥4.5) scoring benchmarks
- **Integration ready**: Works with Vianeo Persona Builder and Intelligence Extractor
- See [Vianeo Validation Framework](skills/vianeo-validation-framework/README.md) for complete documentation

### 360 Executive Brief + Newsletter Generator (November 2025) ⭐ NEW
Professional executive briefing and newsletter system with dual output formats:
- **Primary use case**: Executive Brief (confidential intelligence) - Financials, HR, strategic decisions, board updates
- **Secondary use case**: General Newsletter (shareable) - High-level updates, impact stories, stakeholder communications
- **Multi-source integration**: Asana (70%), Gmail (20%), Google Drive (10%)
- **Automatic intelligence**: Significance scoring, lead story selection, content prioritization
- **Professional design**: Modern dashboard aesthetic with fixed sidebar navigation
- **Interactive visualizations**: 4+ Chart.js charts per report (doughnut, bar, radar, line)
- **Quality framework**: Content analysis, tone consistency, formatting validation
- **Executive Brief sections**: Executive Snapshot, Partnerships, Operations, Strategy & Finance, Timeline
- **Comprehensive documentation**: Weekly production guide, content template, governance rules
- See [360 Newsletter Generator](skills/360-newsletter-generator/README.md) for complete documentation

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
