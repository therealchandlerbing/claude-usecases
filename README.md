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
│       ├── intelligence-extractor/         # Partnership & funding intelligence extraction
│       └── workflow-debugging/             # Systematic workflow debugging & recovery
├── 360-board-meeting-prep/      # Board meeting intelligence system & packet generator
├── skills/                      # User-created skills
│   ├── 360-content-converter/   # Multi-platform content conversion
│   ├── 360-newsletter-generator/  # Board updates & investor briefings
│   ├── 360-use-cases/           # 360-specific workflow skills (organizational directory)
│   ├── design-director/         # Design elevation & visual polish
│   ├── executive-impact-presentation-generator/  # Automated impact report generation
│   ├── financial-modeling-skills/  # Investment analysis & portfolio intelligence
│   ├── skill-orchestrator/      # Universal workflow coordinator for multi-skill/agent operations
│   ├── vianeo-persona-builder/  # Vianeo persona generation & validation
│   └── workflow-process-generator/  # Workflow visualization & process documentation
├── templates/                   # Production-ready HTML templates
│   └── impact-reports/          # Executive impact report templates (static & dynamic)
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
**Location:** `.claude/skills/intelligence-extractor/`
**Purpose:** Extract structured partnership, funding, and stakeholder intelligence from meeting transcripts with real-time quality monitoring and live web dashboard.

**Quick Links:** [README](.claude/skills/intelligence-extractor/README.md) ⭐ | [Skill Spec](.claude/skills/intelligence-extractor/SKILL.md) | [Template Selection Guide](.claude/skills/intelligence-extractor/templates/00-template-selection-guide.md) | [Cross-Linking Architecture](.claude/skills/intelligence-extractor/references/cross-linking-architecture.md) | [Live Dashboard](intelligence-dashboard/README.md)

**When to Use:**
- Extracting intelligence from partnership, funder, board, or stakeholder meetings
- Monitoring extraction quality and template performance with real-time analytics
- Cross-cultural meeting intelligence and community engagement documentation
- Building interconnected Partnership, Funding, and Stakeholder intelligence systems

#### Partnership Intelligence Dashboard
**Location:** `intelligence-dashboard/src/components/partnership/`
**Purpose:** Professional dashboard for navigating partnership conversations with data-driven intelligence from 40+ historical partnerships across 4 partner types.

**Quick Links:** [README](intelligence-dashboard/src/components/partnership/README.md) ⭐ | [Summary](PARTNERSHIP_DASHBOARD_SUMMARY.md) | [Dashboard Demo](intelligence-dashboard/README.md)

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

#### 360 Board Meeting Prep Agent
**Location:** `360-board-meeting-prep/`
**Purpose:** Comprehensive board meeting intelligence system that transforms data from Asana, QuickBooks, Gmail, and Google Drive into professional, governance-ready board packets following exact 360 formatting standards.

**Quick Links:** [README](360-board-meeting-prep/README.md) ⭐ | [Main Orchestrator](360-board-meeting-prep/SKILL.md) | [Financial Dashboard](360-board-meeting-prep/references/financial-dashboard.md) | [Portfolio Health](360-board-meeting-prep/references/client-portfolio-health.md) | [Strategic Initiatives](360-board-meeting-prep/references/strategic-initiatives.md) | [Motion Preparation](360-board-meeting-prep/references/motion-preparation.md)

**When to Use:**
- Preparing quarterly or annual board meetings (saves 14-19 hours per meeting)
- Generating 5 professional documents: Financial Dashboard, Client Portfolio Health, Strategic Initiatives, Governance & Compliance, Motion Tracking
- Cross-validating financial and operational data with automated consistency checks
- Pre-drafting board motions with proper parliamentary procedure
- Post-meeting action item extraction and Asana task creation

**Key Features:**
- 6-phase workflow from data collection to post-meeting follow-up
- Multi-source data synthesis (Asana pipeline, QuickBooks financials, Gmail communications, Drive materials)
- Quality assurance framework with automated flag generation
- Professional DOCX formatting with exact 360 typography standards
- Interactive review process (drafts before finalizing, never ships without approval)

#### Executive Impact Presentation Generator
**Location:** `skills/executive-impact-presentation-generator/`
**Purpose:** Generate complete impact reports from structured content input. Produces two formats (Presentation and Executive) from a single content submission. For manual template editing, see templates/impact-reports/.

**Quick Links:** [INDEX (Start Here)](skills/executive-impact-presentation-generator/INDEX.md) ⭐ | [README](skills/executive-impact-presentation-generator/README.md) | [Skill Guide](skills/executive-impact-presentation-generator/SKILL.md) | [Quick Reference](skills/executive-impact-presentation-generator/QUICK_REFERENCE.md) | [Content Template](skills/executive-impact-presentation-generator/CONTENT_SCHEMA_TEMPLATE.md)

**When to Use:**
- Quick report generation from structured data
- Consistent formatting across multiple reports
- Organizations familiar with Claude workflows
- Teams that want automated, repeatable processes

**Output:** Two HTML files (landscape presentation + portrait executive document)

**Alternative:** For manual customization without Claude, use the [Executive Impact Report Templates](templates/impact-reports/) with complete HTML/CSS control

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

### Workflow Coordination & Orchestration

#### Skill Orchestrator
**Location:** `skills/skill-orchestrator/`
**Purpose:** Universal workflow coordinator that intelligently routes requests and coordinates complex multi-skill and multi-agent operations, maintaining context across steps and delivering integrated results.

**Quick Links:** [INDEX (Start Here)](skills/skill-orchestrator/INDEX.md) ⭐ | [README](skills/skill-orchestrator/README.md) | [Skill Logic](skills/skill-orchestrator/SKILL.md) | [Quick Reference](skills/skill-orchestrator/REFERENCE.md) | [Examples](skills/skill-orchestrator/EXAMPLES.md) | [Implementation Guide](skills/skill-orchestrator/IMPLEMENTATION.md)

**When to Use:**
- Multi-step workflows requiring coordination of multiple skills/agents
- GitHub agent coordination with payload validation
- Unclear routing decisions between available capabilities
- Cross-domain operations (Asana + Gmail + Drive integration)
- Complex workflows requiring context preservation across steps

**Key Features:**
- Intelligent routing decision tree (single skill vs. multi-skill vs. agent)
- 3-phase workflow orchestration (Map → Execute → Aggregate)
- Agent payload validation and one-shot clarifications
- Context preservation across workflow steps
- Graceful error handling with recovery paths
- Integration with using-superpowers skill for enhanced capability coordination

**Common Workflows:**
- Board packet generation (Asana + QuickBooks + synthesis + document creation)
- Client assessments (Drive search + framework application + analysis + deliverable)
- Meeting intelligence (transcript processing + email drafting + task creation)
- Weekly status synthesis (multi-project data gathering + formatting)
- Partnership development (research + strategy + modeling + documentation)

**Time Savings:**
- Board packets: 2-3 hours → 3 minutes
- Client assessments: 4-5 hours → 15 minutes
- Meeting intelligence: 45 minutes → 45 seconds
- Weekly status: 30-45 minutes → 30 seconds

#### Workflow Debugging
**Location:** `.claude/skills/workflow-debugging/`
**Purpose:** Systematic debugging toolkit for complex workflow orchestration systems, enabling rapid identification, isolation, and resolution of execution failures across multi-stakeholder projects with automated recovery and cross-region support.

**Quick Links:** [README](.claude/skills/workflow-debugging/README.md) ⭐ | [Skill Spec](.claude/skills/workflow-debugging/SKILL.md) | [Implementation Guide](.claude/skills/workflow-debugging/IMPLEMENTATION-GUIDE.md) | [Quick Start](.claude/skills/workflow-debugging/docs/QUICK-START.md)

**When to Use:**
- Debugging multi-stage evaluation workflows during technology assessments
- Troubleshooting cross-system integration failures (Brazil-US partnerships, CNEN-Yale systems)
- Handling client deliverable automation errors (Vianeo-GenIP integration)
- Resolving Asana integration issues (webhooks, duplicates, rate limiting)
- Managing multi-geography workflow errors (timezone, locale, permissions)

**Key Features:**
- 60-80% reduction in debugging time through systematic isolation
- Automated recovery from 60% of common error patterns
- Multi-region support (US, Brazil, Europe) with locale-specific handling
- Multi-channel notifications (Slack, Asana, Email, PagerDuty)
- Mean Time to Resolution (MTTR) < 15 minutes

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

### Financial Analysis & Investment Intelligence

#### Financial Modeling Skills
**Location:** `skills/financial-modeling-skills/`
**Purpose:** Strategic toolkit transforming financial analysis into systematic intelligence generation with institutional-grade workflows for investment analysis, portfolio management, and impact measurement.

**Quick Links:** [README](skills/financial-modeling-skills/README.md) ⭐ | [Investment Analysis](skills/financial-modeling-skills/investment-analysis/) | [Portfolio Intelligence](skills/financial-modeling-skills/portfolio-intelligence/) | [Impact Modeling](skills/financial-modeling-skills/impact-modeling/) | [File Inventory](skills/financial-modeling-skills/FILE_INVENTORY.md)

**When to Use:**
- Investment evaluation and multi-scenario financial modeling
- Portfolio performance analytics and strategic allocation optimization
- Market opportunity assessment and comparable company analysis
- Social return on investment (SROI) and impact-weighted accounting
- Cross-border valuations and international market analysis
- Technology transfer valuation and IP portfolio assessment

**Key Capabilities:**
- **Investment Analysis Suite:** Complete IC memos with DCF models, risk assessment, exit strategy evaluation
- **Portfolio Intelligence:** Cross-portfolio analytics, risk correlation, impact measurement, quarterly reporting
- **Deal Sourcing Engine:** Market assessment, valuation benchmarking, pipeline prioritization
- **Impact Modeling:** SROI, blended finance structuring, theory of change financial modeling
- **Innovation Valuation:** Technology transfer, research commercialization, university spin-out structuring

**Output Formats:**
- Excel models with working formulas and scenario testing
- Interactive HTML dashboards with drill-downs
- Board presentation decks and investment committee memos
- Partnership term sheets and valuation frameworks

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

**Version:** 2.0.0
**Last Updated:** 2025-11-17
