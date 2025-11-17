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
├── .claude/
│   └── skills/                  # Managed Claude skills
│       ├── 360-client-portfolio-builder/   # Client venture portfolio page generator
│       ├── 360-executive-project-tracker/  # Multi-source project status tracking
│       ├── contract-redlining-tool/        # Automated contract review & redlining
│       ├── executive-intelligence-dashboard/  # Executive intelligence briefing system
│       ├── fda-consultant-agent/           # FDA regulatory consulting
│       └── intelligence-extractor/         # Partnership & funding intelligence extraction
├── skills/                      # User-created skills
│   ├── 360-content-converter/   # Multi-platform content conversion
│   ├── 360-newsletter-generator/  # Board updates & investor briefings
│   ├── 360-use-cases/           # 360-specific workflow skills
│   ├── design-director/         # Design elevation & visual polish
│   ├── vianeo-persona-builder/  # Vianeo persona generation & validation
│   └── workflow-process-generator/  # Workflow visualization & process documentation
├── intelligence-dashboard/      # Live quality monitoring dashboard (Next.js app)
├── docs/                        # Documentation and guides
└── examples/                    # Example implementations
```

## Quick Start

### Using an Existing Skill

1. Browse the skills by category below
2. Click the README link to view complete documentation
3. Follow the quick start guide for each skill

### Creating a New Skill

1. Copy the template: `cp skills/templates/skill-template.md skills/your-skill-name.md`
2. Customize with your specific use case
3. Follow the guidelines in `docs/CREATING-SKILLS.md`

---

## Available Skills

### Healthcare & Life Sciences Regulatory

#### FDA Consultant Agent
**Location:** `.claude/skills/fda-consultant-agent/`
**Purpose:** Expert FDA regulatory guidance for medical devices, pharmaceuticals, biologics, and combination products with 100% citation accuracy and strategic pathway recommendations.

**Quick Links:** [README](.claude/skills/fda-consultant-agent/README.md) ⭐ | [Quick Start](.claude/skills/fda-consultant-agent/QUICK-START.md) | [Skill Spec](.claude/skills/fda-consultant-agent/SKILL.md) | [Regulations Reference](.claude/skills/fda-consultant-agent/references/fda-regulations-reference.md)

**When to Use:**
- FDA pathway selection and product classification (510(k), PMA, IND, NDA, BLA)
- Quality system compliance (QSR, cGMP, ISO 13485)
- Clinical trial design and regulatory strategy
- FDA meeting preparation and inspection response
- Software as Medical Device (SaMD) and AI/ML regulatory frameworks

---

### Research & Validation

#### Vianeo Persona Builder
**Location:** `skills/vianeo-persona-builder/`
**Purpose:** Generate validated stakeholder personas from research data following the Vianeo framework with interactive dashboard visualizations.

**Quick Links:** [README](skills/vianeo-persona-builder/README.md) ⭐ | [Examples](skills/vianeo-persona-builder/examples/) | [Scoring Rubric](skills/vianeo-persona-builder/references/vianeo-scoring-rubric.md) | [Interactive Dashboard](skills/vianeo-persona-builder/powerups/interactive-dashboard/README.md)

**When to Use:**
- Building personas for technology validation projects
- Documenting stakeholder needs for partnership development
- Preparing Desirability dimension documentation for Vianeo submissions
- Creating interactive presentations for stakeholders

---

### Design & Visual Excellence

#### Design Director
**Location:** `skills/design-director/`
**Purpose:** Transform functional outputs into professionally polished, design-elevated work through systematic application of contemporary design best practices (Stripe, Linear, Apple aesthetic).

**Quick Links:** [Quick Reference](skills/design-director/QUICK-REFERENCE.md) ⭐ | [Complete Guide](skills/design-director/COMPLETE-GUIDE.md) | [Technique Catalog](skills/design-director/references/technique-catalog.md) | [Design Philosophy](skills/design-director/references/design-philosophy.md)

**When to Use:**
- Elevating dashboards, presentations, and reports to professional design quality
- Building web interfaces that match contemporary standards
- Ensuring visual consistency and WCAG AA accessibility
- Making data-heavy outputs scannable and beautiful

---

### Content Strategy & Multi-Platform Publishing

#### 360 Content Converter
**Location:** `skills/360-content-converter/`
**Purpose:** Transform one piece of content into multiple platform-optimized formats while maintaining brand consistency, strategic coherence, and cultural intelligence across 15+ platforms and 3 languages.

**Quick Links:** [README](skills/360-content-converter/README.md) ⭐ | [Prompt Templates](skills/360-content-converter/references/prompt-templates.md) | [Quality Checklist](skills/360-content-converter/references/quality-checklist.md) | [Platform Strategy](skills/360-content-converter/references/platform-strategy.md)

**When to Use:**
- Repurposing content across multiple platforms (social, email, blog, presentations)
- Adapting content for different audiences and languages with cultural intelligence
- Building cohesive content ecosystems with strategic sequencing
- Creating design-ready specifications for visual content

---

### Data Intelligence & Quality Monitoring

#### Intelligence Extractor
**Location:** `skills/intelligence-extractor/`
**Purpose:** Extract structured partnership, funding, and stakeholder intelligence from meeting transcripts with real-time quality monitoring and live web dashboard.

**Quick Links:** [README](skills/intelligence-extractor/README.md) ⭐ | [Template Selection Guide](skills/intelligence-extractor/templates/00-template-selection-guide.md) | [Cross-Linking Architecture](skills/intelligence-extractor/references/cross-linking-architecture.md) | [Live Dashboard](intelligence-dashboard/README.md)

**When to Use:**
- Extracting intelligence from partnership, funder, board, or stakeholder meetings
- Monitoring extraction quality and template performance with real-time analytics
- Cross-cultural meeting intelligence and community engagement documentation
- Building interconnected Partnership, Funding, and Stakeholder intelligence systems

#### Partnership Intelligence Dashboard
**Location:** `intelligence-dashboard/src/components/partnership/`
**Purpose:** Professional dashboard for navigating partnership conversations with data-driven intelligence from 40+ historical partnerships across 4 partner types.

**Quick Links:** [Component Docs](intelligence-dashboard/src/components/partnership/README.md) | [Summary](PARTNERSHIP_DASHBOARD_SUMMARY.md)

**When to Use:**
- Preparing for partnership conversations and qualifying potential partners
- Understanding decision-making timelines and cultural differences by partner type
- Building confidence in objection handling with proven response frameworks

---

### Executive Communication & Strategic Briefing

#### Executive Intelligence Dashboard
**Location:** `.claude/skills/executive-intelligence-dashboard/`
**Purpose:** Generate sophisticated, executive-grade weekly intelligence briefs by synthesizing Asana, Gmail, and Google Drive data into production-quality HTML dashboards suitable for board presentations.

**Quick Links:** [README](.claude/skills/executive-intelligence-dashboard/README.md) ⭐ | [Quick Start](.claude/skills/executive-intelligence-dashboard/QUICK-START.md) | [Skill Spec](.claude/skills/executive-intelligence-dashboard/SKILL.md) | [Query Guide](.claude/skills/executive-intelligence-dashboard/QUERY-GUIDE.md)

**When to Use:**
- Generating weekly 360 Impact Brief for board meetings
- Preparing comprehensive partnership or operations reports with decision support
- Board meeting preparation and quarterly strategic planning sessions
- Creating stakeholder communications with strategic context

#### 360 Executive Brief / Newsletter Generator
**Location:** `skills/360-newsletter-generator/`
**Purpose:** Generate executive intelligence briefs (confidential) and stakeholder newsletters (shareable) with interactive Chart.js visualizations and modern dashboard design.

**Quick Links:** [README](skills/360-newsletter-generator/README.md) ⭐ | [Data Collection Guide](skills/360-newsletter-generator/references/data-collection-guide.md) | [Content Analysis Framework](skills/360-newsletter-generator/references/content-analysis-framework.md)

**When to Use:**
- Creating board updates and investor briefings with confidential data
- Generating weekly/monthly newsletters for stakeholders and partners
- Preparing pre-meeting briefings with talking points

#### Executive Impact Presentation Generator
**Location:** `skills/executive-impact-presentation-generator/`
**Purpose:** Generate professional board-ready impact reports in two optimized formats (Presentation and Executive) from a single content input. Transform organizational impact data into polished, print-ready reports suitable for board meetings and stakeholder communications.

**Quick Links:** [INDEX (Start Here)](skills/executive-impact-presentation-generator/INDEX.md) ⭐ | [README](skills/executive-impact-presentation-generator/README.md) | [Skill Guide](skills/executive-impact-presentation-generator/SKILL.md) | [Quick Reference](skills/executive-impact-presentation-generator/QUICK_REFERENCE.md) | [Content Template](skills/executive-impact-presentation-generator/CONTENT_SCHEMA_TEMPLATE.md)

**When to Use:**
- Creating board presentations and annual impact reports with dual-format generation
- Generating both presentation slides (landscape deck) and executive documents (portrait pages) from single input
- Producing print-ready PDF reports with professional design and brand customization
- Showcasing organizational performance across six core sections (impact, regional portfolio, financial, outcomes, partnerships, strategic outlook)

---

### Process Documentation & Workflow Visualization

#### Workflow Process Generator
**Location:** `skills/workflow-process-generator/`
**Purpose:** Transform operational workflows from implicit tribal knowledge into explicit, shareable visual documentation through automated extraction and professional Mermaid diagrams + interactive HTML.

**Quick Links:** [README](skills/workflow-process-generator/README.md) ⭐ | [Data Extraction Guide](skills/workflow-process-generator/references/data-extraction-guide.md) | [Mermaid Standards](skills/workflow-process-generator/references/mermaid-generation-standards.md)

**When to Use:**
- Visualizing operational workflows for team onboarding
- Preparing board-ready workflow presentations
- Making processes delegation-ready and identifying bottlenecks
- Creating multi-language workflow documentation for international partnerships

---

### Project Management & Executive Intelligence

#### 360 Executive Project Tracker
**Location:** `.claude/skills/360-executive-project-tracker/`
**Purpose:** Build professionally designed, multi-source project status trackers that consolidate Gmail, Google Calendar, Google Drive, and Asana into Excel dashboards and interactive HTML visualizations.

**Quick Links:** [README](.claude/skills/360-executive-project-tracker/docs/README.md) ⭐ | [Quick Start](.claude/skills/360-executive-project-tracker/docs/QUICK_START.md) | [Deliverables Summary](.claude/skills/360-executive-project-tracker/docs/DELIVERABLES_SUMMARY.md)

**When to Use:**
- Creating comprehensive project status trackers with automated updates
- Building executive dashboards for project visibility and blocker tracking
- Generating weekly status reports and tracking multi-project portfolios
- Monitoring team workload and capacity across workstreams

---

### Legal Intelligence & Risk Management

#### Contract Redlining Tool
**Location:** `.claude/skills/contract-redlining-tool/`
**Purpose:** Automated contract review and redlining that analyzes contracts against 360's standard positions and produces attorney-quality redlines with tracked changes, margin comments, and negotiation guidance.

**Quick Links:** [README](.claude/skills/contract-redlining-tool/README.md) ⭐ | [Implementation Guide](.claude/skills/contract-redlining-tool/IMPLEMENTATION-GUIDE.md) | [Examples](.claude/skills/contract-redlining-tool/EXAMPLES.md) | [Negotiation Playbook](.claude/skills/contract-redlining-tool/NEGOTIATION-PLAYBOOK.md)

**When to Use:**
- Reviewing contracts from partners, clients, or collaborators
- Identifying risks and misalignment with standard positions (IP, payment, scope, liability)
- Preparing negotiation strategy and talking points
- Training team on contract standards and protecting business interests

---

### Client Showcasing & Business Development

#### 360 Client Portfolio Builder
**Location:** `.claude/skills/360-client-portfolio-builder/`
**Purpose:** Create professional, editorially sophisticated portfolio HTML pages for 360 client ventures using Vianeo business validation sprint data. Production-quality single-page sites that build credibility with investors and partners.

**Quick Links:** [README](.claude/skills/360-client-portfolio-builder/README.md) ⭐ | [Quick Start](.claude/skills/360-client-portfolio-builder/QUICK-START.md) | [Design Standards](.claude/skills/360-client-portfolio-builder/references/design-standards.md) | [Deployment Guides](.claude/skills/360-client-portfolio-builder/deployment/)

**When to Use:**
- Creating showcase pages for current 360 client teams
- Presenting Vianeo sprint outputs to investors or partners
- Building portfolio section for 360 website
- Partnership development and fundraising preparation materials

---

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
- Workflow automation and standardized processes
- Knowledge management and task templates
- Custom Claude behaviors and repeatable analysis patterns

## Getting Started

The best way to get started is to:
1. Browse skills by category above and click README links
2. Review the documentation in `docs/CREATING-SKILLS.md`
3. Examine the skill template in `skills/templates/`
4. Create your first skill using the template

---

**Version:** 1.8.0
**Last Updated:** 2025-11-17
