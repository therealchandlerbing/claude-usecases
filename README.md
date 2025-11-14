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
│   ├── 360-use-cases/          # 360-specific workflow skills
│   ├── vianeo-persona-builder/ # Vianeo persona generation & validation
│   ├── design-director/        # Design elevation & visual polish
│   └── templates/              # Templates for creating new skills
├── docs/                       # Documentation and guides
├── examples/                   # Example implementations
└── README.md                  # This file
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

## Version

Current Version: 1.0.0
Last Updated: 2025-11-14 
