---
name: 360 Use Cases
description: Repository directory for 360 Social Impact Studios-specific skills and workflows. This is a placeholder skill that provides navigation to 360-customized implementations of general-purpose skills, internal process documentation, and organization-specific automation.
version: 1.0.0
author: 360 Social Impact Studios
created: 2024-08-15
updated: 2025-11-22
category: meta
complexity: low
tags: [360-specific, internal-workflows, organization-specific, skill-directory, navigation]
dependencies: []
outputs:
  - Routing to appropriate 360-specific skills
  - Internal workflow documentation
---

# 360 Use Cases - Skill Directory

## Purpose

This is a **meta-skill** and directory placeholder for 360 Social Impact Studios-specific implementations. It serves as a navigation hub for skills that have been customized for 360's operations, partnerships, and internal workflows.

## What This Skill Does

**360 Use Cases is NOT an executable skill.** Instead, it's a directory organization pattern that:
- Houses 360-customized versions of general-purpose skills
- Provides internal process documentation specific to 360 operations
- Maintains organization-specific workflow automation
- Enables version control for 360-only implementations

## When to Use

**You should NOT directly invoke "360 Use Cases" as a skill.**

Instead, use the specific skills within related categories:

### Internal Workflows
- **workflow-process-generator** (360-specific) - Extract 360 workflows from Asana, Drive, Gmail
- **executive-intelligence-dashboard** - 360 weekly impact briefs
- **360-board-meeting-prep** - Board packet generation for 360

### Client-Facing Work
- **360-client-portfolio-builder** - Portfolio pages for 360 client ventures
- **360-proposal-builder** - 360 service proposals
- **360-content-converter** - Multi-platform content for 360 communications

### Partnership & Ecosystem
- **intelligence-extractor** - Extract partnership intelligence from meetings
- **strategic-persona-builder** - Build personas using Vianeo framework

## Directory Structure

Skills in this directory follow the pattern:

```
360-use-cases/
├── SKILL.md (this file)
├── README.md
└── QUICK-START.md
```

Individual 360-specific skills are located elsewhere in the repository:
- `skills/` - User-created 360-specific skills
- `.claude/skills/` - Managed 360 skills (production-ready)

## Relationship to Other Skills

| General-Purpose Skill | 360-Specific Version | Location |
|----------------------|---------------------|----------|
| workflow-process-generator (generic SOPs) | workflow-process-generator (360 Asana extraction) | `skills/workflow-process-generator/` |
| strategic-persona-builder (multi-framework) | vianeo-persona-builder (Vianeo-focused) | `skills/vianeo-persona-builder/` |
| Generic portfolio builder | 360-client-portfolio-builder | `skills/360-client-portfolio-builder/` |

## Navigation Guide

**If you need:**
- **Internal 360 process documentation** → Use `workflow-process-generator` (360 version)
- **Client showcase pages** → Use `360-client-portfolio-builder`
- **Board meeting preparation** → Use `360-board-meeting-prep`
- **Partnership intelligence** → Use `intelligence-extractor`
- **Vianeo personas** → Use `strategic-persona-builder` with Vianeo framework
- **360 proposals** → Use `360-proposal-builder`
- **Executive briefings** → Use `executive-intelligence-dashboard` or `ceo-advisor`

## Creating New 360-Specific Skills

When creating skills specifically for 360 operations:

### Step 1: Determine if Customization is Needed

**Create a 360-specific version if:**
- Skill requires 360 terminology, processes, or context
- Integration with 360-specific tools (Asana projects, Drive structure, etc.)
- Workflow reflects 360's unique partnership or client engagement model
- Contains proprietary 360 methodologies or frameworks

**Use general-purpose skill if:**
- Functionality is universal across organizations
- No 360-specific context required
- Skill can serve broader use cases

### Step 2: Choose Location

**User Skills** (`skills/`):
- Development and testing
- 360-specific but not yet production-ready
- Experimental or specialized workflows

**Managed Skills** (`.claude/skills/`):
- Production-ready, field-tested
- Comprehensive documentation
- Used regularly across 360 operations

### Step 3: Follow Skill Structure

All 360-specific skills must include:
- **SKILL.md** - Operational logic with YAML frontmatter
- **README.md** - User-facing documentation
- **QUICK-START.md** - Fast reference guide
- Supporting files (templates/, references/, examples/) as needed

See [Creating Skills Guide](../../docs/CREATING-SKILLS.md) for complete instructions.

## Version History

- **v1.0.0** (2025-11-22) - Created meta-skill for 360 use cases directory
  - Established as navigation hub
  - Documented relationship to 360-specific skills
  - Added skill creation guidelines

---

## Troubleshooting

**"I can't find the 360 skill I'm looking for"**
→ Check `.claude/skills/` for managed versions
→ Search by category in main README.md
→ Look for "360-" prefix in skill names

**"Should I create a 360-specific version or use the general skill?"**
→ If it requires 360 context, processes, or integrations: create 360 version
→ If it's universally applicable: use general-purpose skill

**"Where do I put a new 360 skill?"**
→ Development: `skills/your-skill-name/`
→ Production: `.claude/skills/your-skill-name/` (after validation)

---

## Related Documentation

- [Creating Skills Guide](../../docs/CREATING-SKILLS.md)
- [Skill Structure Validation](../../docs/SKILL-STRUCTURE-VALIDATION.md)
- [Main README](../../README.md) - Complete skill catalog
- [CLAUDE.md](../../CLAUDE.md) - Repository instructions for AI assistants

---

**Note**: This is a meta-skill for organization purposes. For actual workflow execution, use the specific 360 skills listed above.
