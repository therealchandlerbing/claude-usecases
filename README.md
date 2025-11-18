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
│       ├── executive-impact-presentation-generator/  # Board-ready impact reports (dual-format)
│       ├── executive-intelligence-dashboard/  # Executive intelligence briefing system
│       ├── fda-consultant-agent/           # FDA regulatory consulting
│       ├── intelligence-extractor/         # Partnership & funding intelligence extraction
│       ├── open-deep-research-team/        # Multi-agent comprehensive research system
│       └── workflow-debugging/             # Systematic workflow debugging & recovery
├── 360-board-meeting-prep/      # Board meeting intelligence system & packet generator
├── skills/                      # User-created skills
│   ├── 360-content-converter/   # Multi-platform content conversion
│   ├── 360-newsletter-generator/  # Board updates & investor briefings
│   ├── 360-use-cases/           # 360-specific workflow skills (organizational directory)
│   ├── ceo-advisor/             # Strategic advisory and decision support
│   ├── design-director/         # Design elevation & visual polish
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
**Purpose:** Expert FDA regulatory guidance for medical devices, pharmaceuticals, biologics, and combination products with 100% citation accuracy.

**Quick Links:** [README](.claude/skills/fda-consultant-agent/README.md) ⭐ | [Quick Start](.claude/skills/fda-consultant-agent/QUICK-START.md) | [Skill Spec](.claude/skills/fda-consultant-agent/SKILL.md)

**When to Use:**
- FDA pathway selection and product classification (510(k), PMA, IND, NDA, BLA)
- Quality system compliance (QSR, cGMP, ISO 13485)
- Clinical trial design and regulatory strategy
- Software as Medical Device (SaMD) and AI/ML regulatory frameworks

---

### Research & Validation

#### Open Deep Research Team
**Location:** `.claude/skills/open-deep-research-team/`
**Purpose:** Sophisticated multi-agent AI research system conducting comprehensive, academic-quality research through orchestrated specialist agents. Combines academic, technical, and data-driven perspectives with rigorous quality assurance and comprehensive reporting.

**Quick Links:** [README](.claude/skills/open-deep-research-team/README.md) ⭐ | [Quick Start](.claude/skills/open-deep-research-team/QUICK-START.md) | [Skill Spec](.claude/skills/open-deep-research-team/SKILL.md) | [Examples](.claude/skills/open-deep-research-team/EXAMPLES.md)

**When to Use:**
- Conducting comprehensive research on complex topics requiring multiple perspectives
- Academic literature reviews and state-of-the-art analysis
- Technical evaluations with implementation details and code examples
- Market research and competitive intelligence with proper citations
- Business intelligence requiring academic rigor and data validation
- Research reports with executive summaries and actionable recommendations

#### Vianeo Persona Builder
**Location:** `skills/vianeo-persona-builder/`
**Purpose:** Generate validated stakeholder personas from research data following the Vianeo framework with interactive dashboard visualizations.

**Quick Links:** [README](skills/vianeo-persona-builder/README.md) ⭐ | [Examples](skills/vianeo-persona-builder/examples/) | [Scoring Rubric](skills/vianeo-persona-builder/references/vianeo-scoring-rubric.md)

**When to Use:**
- Building personas for technology validation projects
- Documenting stakeholder needs for partnership development
- Preparing Desirability dimension documentation for Vianeo submissions
- Creating interactive presentations for stakeholders

---

### Design & Visual Excellence

#### Design Director
**Location:** `skills/design-director/`
**Purpose:** Transform functional outputs into professionally polished, design-elevated work through systematic application of contemporary design best practices.

**Quick Links:** [Quick Reference](skills/design-director/QUICK-REFERENCE.md) ⭐ | [Complete Guide](skills/design-director/COMPLETE-GUIDE.md) | [Technique Catalog](skills/design-director/references/technique-catalog.md)

**When to Use:**
- Elevating dashboards, presentations, and reports to professional design quality
- Building web interfaces that match contemporary standards
- Ensuring visual consistency and WCAG AA accessibility
- Making data-heavy outputs scannable and beautiful

---

### Content Strategy & Multi-Platform Publishing

#### 360 Content Converter
**Location:** `skills/360-content-converter/`
**Purpose:** Transform one piece of content into multiple platform-optimized formats while maintaining brand consistency across 15+ platforms and 3 languages.

**Quick Links:** [README](skills/360-content-converter/README.md) ⭐ | [Prompt Templates](skills/360-content-converter/references/prompt-templates.md) | [Quality Checklist](skills/360-content-converter/references/quality-checklist.md)

**When to Use:**
- Repurposing content across multiple platforms (social, email, blog, presentations)
- Adapting content for different audiences and languages with cultural intelligence
- Building cohesive content ecosystems with strategic sequencing
- Creating design-ready specifications for visual content

---

### Data Intelligence & Quality Monitoring

#### Intelligence Extractor
**Location:** `.claude/skills/intelligence-extractor/`
**Purpose:** Extract structured partnership, funding, and stakeholder intelligence from meeting transcripts with real-time quality monitoring.

**Quick Links:** [README](.claude/skills/intelligence-extractor/README.md) ⭐ | [Skill Spec](.claude/skills/intelligence-extractor/SKILL.md) | [Template Selection Guide](.claude/skills/intelligence-extractor/templates/00-template-selection-guide.md)

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
**Purpose:** Generate executive-grade weekly intelligence briefs by synthesizing Asana, Gmail, and Google Drive data into HTML dashboards.

**Quick Links:** [README](.claude/skills/executive-intelligence-dashboard/README.md) ⭐ | [Quick Start](.claude/skills/executive-intelligence-dashboard/QUICK-START.md) | [Skill Spec](.claude/skills/executive-intelligence-dashboard/SKILL.md)

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
**Purpose:** Transform data from Asana, QuickBooks, Gmail, and Google Drive into professional board packets with automated quality checks.

**Quick Links:** [README](360-board-meeting-prep/README.md) ⭐ | [Main Orchestrator](360-board-meeting-prep/SKILL.md) | [Financial Dashboard](360-board-meeting-prep/references/financial-dashboard.md)

**When to Use:**
- Preparing quarterly or annual board meetings
- Generating comprehensive board documents with multi-source data synthesis
- Cross-validating financial and operational data
- Pre-drafting board motions and post-meeting action items

#### Executive Impact Presentation Generator
**Location:** `.claude/skills/executive-impact-presentation-generator/`
**Purpose:** Generate professional, board-ready impact reports in dual formats (presentation deck and executive document) from a single content input, with brand customization, accessibility compliance, and print optimization.

**Quick Links:** [README](.claude/skills/executive-impact-presentation-generator/README.md) ⭐ | [Quick Start](.claude/skills/executive-impact-presentation-generator/QUICK-START.md) | [Skill Spec](.claude/skills/executive-impact-presentation-generator/SKILL.md) | [Examples](.claude/skills/executive-impact-presentation-generator/EXAMPLES.md) | [Implementation Guide](.claude/skills/executive-impact-presentation-generator/IMPLEMENTATION-GUIDE.md)

**When to Use:**
- Creating quarterly or annual board presentations with dual-format outputs
- Generating stakeholder impact reports with professional polish and accessibility
- Building repeatable reporting workflows (10-20 minutes vs 8-12 hours manually)
- Distributing board-ready presentations (landscape deck) and comprehensive documents (portrait)
- Customizing reports with brand colors and maintaining visual consistency
- Ensuring WCAG 2.1 AA accessibility compliance and perfect PDF print exports

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
**Purpose:** Universal workflow coordinator that intelligently routes requests and coordinates complex multi-skill and multi-agent operations.

**Quick Links:** [INDEX (Start Here)](skills/skill-orchestrator/INDEX.md) ⭐ | [README](skills/skill-orchestrator/README.md) | [Examples](skills/skill-orchestrator/EXAMPLES.md)

**When to Use:**
- Multi-step workflows requiring coordination of multiple skills/agents
- Cross-domain operations (Asana + Gmail + Drive integration)
- Complex workflows requiring context preservation across steps
- GitHub agent coordination with payload validation

#### Workflow Debugging
**Location:** `.claude/skills/workflow-debugging/`
**Purpose:** Systematic debugging toolkit for workflow orchestration systems with automated error recovery and multi-region support.

**Quick Links:** [README](.claude/skills/workflow-debugging/README.md) ⭐ | [Skill Spec](.claude/skills/workflow-debugging/SKILL.md) | [Implementation Guide](.claude/skills/workflow-debugging/IMPLEMENTATION-GUIDE.md)

**When to Use:**
- Debugging multi-stage evaluation workflows and technology assessments
- Troubleshooting cross-system integration failures
- Resolving Asana integration issues (webhooks, duplicates, rate limiting)
- Managing multi-geography workflow errors (timezone, locale, permissions)

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

### Sales & Business Development

#### Sales Automator
**Location:** `skills/sales-automator/`
**Purpose:** Intelligent sales automation with relationship intelligence, deal pipeline tracking, and competitive analysis. Transforms basic email automation into a context-aware conversion engine that researches prospects, tracks deals, and generates hyper-personalized outreach grounded in real intelligence.

**Quick Links:** [README](skills/sales-automator/README.md) ⭐ | [Quick Start](skills/sales-automator/docs/QUICK-START.md) | [Installation](skills/sales-automator/docs/INSTALLATION.md) | [Templates](skills/sales-automator/references/REFERENCE.md)

**When to Use:**
- Cold outreach campaigns (5-touch sequences with research-backed personalization)
- Warm lead follow-up (re-engage prospects with past conversation context)
- Stuck deal re-activation (identify and re-engage stalled opportunities)
- Proposal generation (comprehensive partnership proposals with case studies)
- Pipeline health monitoring (weekly reviews, forecasting, conversion tracking)
- Competitive positioning (research and position against alternatives)

---

### Financial Analysis & Investment Intelligence

#### Financial Modeling Skills
**Location:** `skills/financial-modeling-skills/`
**Purpose:** Institutional-grade financial analysis toolkit for investment evaluation, portfolio management, and impact measurement.

**Quick Links:** [README](skills/financial-modeling-skills/README.md) ⭐ | [Investment Analysis](skills/financial-modeling-skills/investment-analysis/) | [Portfolio Intelligence](skills/financial-modeling-skills/portfolio-intelligence/)

**When to Use:**
- Investment evaluation and multi-scenario financial modeling
- Portfolio performance analytics and strategic allocation optimization
- Social return on investment (SROI) and impact-weighted accounting
- Technology transfer valuation and IP portfolio assessment

#### IRS Form 990-EZ Preparation
**Location:** `skills/990-ez-preparation/`
**Purpose:** Automated nonprofit tax compliance through intelligent data collection, multi-level validation, and complete filing package generation. Reduces preparation time from 40+ hours to under 10 hours.

**Quick Links:** [README](skills/990-ez-preparation/README.md) ⭐ | [Quick Start](skills/990-ez-preparation/docs/QUICK-START.md) | [Skill Spec](skills/990-ez-preparation/SKILL.md)

**When to Use:**
- Preparing annual IRS Form 990-EZ for small nonprofits (receipts < $200K, assets < $500K)
- Automated eligibility verification and compliance checking
- Multi-level validation (mathematical, regulatory, narrative, strategic)
- Complete filing package generation with Schedules A, B, and O
- Board-ready presentation with validation reports and pre-filing checklists

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

**Version:** 2.0.1
**Last Updated:** 2025-11-18
