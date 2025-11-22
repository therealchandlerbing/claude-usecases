# 360 Use Cases - Quick Start

## One-Line Summary
Navigation hub for 360 Social Impact Studios-specific skills - this is NOT an executable skill, but a directory for organization-specific implementations.

---

## ⚠️ Important Notice

**360 Use Cases is a directory placeholder, not an executable skill.**

You cannot "use" this skill directly. Instead, navigate to the specific 360 skill you need from the list below.

---

## Quick Skill Finder

### I Need To...

| Task | Use This Skill | Location |
|------|---------------|----------|
| Document 360 internal processes | workflow-process-generator (360 version) | `skills/workflow-process-generator/` |
| Create client portfolio pages | 360-client-portfolio-builder | `.claude/skills/360-client-portfolio-builder/` |
| Prep for board meetings | 360-board-meeting-prep | `.claude/skills/360-board-meeting-prep/` |
| Generate weekly intelligence brief | executive-intelligence-dashboard | `.claude/skills/executive-intelligence-dashboard/` |
| Extract partnership intelligence | intelligence-extractor | `.claude/skills/intelligence-extractor/` |
| Build Vianeo personas | strategic-persona-builder | `.claude/skills/strategic-persona-builder/` |
| Create service proposals | 360-proposal-builder | `.claude/skills/360-proposal-builder/` |
| Get CEO daily briefing | ceo-advisor | `.claude/skills/ceo-advisor/` |
| Convert content to multiple platforms | 360-content-converter | `skills/360-content-converter/` |
| Review contracts for risks | contract-redlining-tool | `.claude/skills/contract-redlining-tool/` |

---

## Skill Categories

### 📊 Executive Intelligence
- `ceo-advisor` - 5-expert advisory board system
- `executive-intelligence-dashboard` - Weekly 360 Impact Briefs
- `360-board-meeting-prep` - Board packet generation

### 🤝 Client & Partnership Work
- `360-client-portfolio-builder` - Portfolio HTML pages
- `360-proposal-builder` - Service proposals
- `intelligence-extractor` - Partnership intelligence
- `contract-redlining-tool` - Contract review

### 🔬 Research & Validation
- `strategic-persona-builder` - Evidence-backed personas (includes Vianeo)
- `open-deep-research-team` - Multi-agent research system
- `ai-ethics-advisor` - Bias assessment and compliance

### 💰 Financial & Compliance
- `financial-modeling-skills` - Investment analysis, portfolio intelligence
- `990-ez-preparation` - IRS Form 990-EZ automation

### 📝 Content & Documentation
- `workflow-process-generator` (360 version) - Process flow documentation
- `360-content-converter` - Multi-platform content
- `design-director` - Professional design elevation

### 🚀 Sales & Business Development
- `sales-automator` - Intelligent outreach automation
- `contract-redlining-tool` - Attorney-quality redlines

---

## General vs. 360-Specific Skills

### When to Use General-Purpose Skills

Use skills from `.claude/skills/` when:
- Task doesn't require 360-specific context
- No integration with 360 tools/processes needed
- Universally applicable workflow

**Examples:**
- `design-director` - Works for any visual content
- `ai-ethics-advisor` - Universal bias assessment
- `fda-consultant-agent` - Regulatory guidance

### When to Use 360-Specific Skills

Use 360-customized versions when:
- Requires 360 terminology or workflows
- Integrates with 360's Asana, Drive, Gmail setup
- Follows 360 partnership or client engagement model
- Uses 360 methodologies (Vianeo, GenIP, etc.)

**Examples:**
- `workflow-process-generator` (360 version) - Extracts from 360's Asana
- `360-client-portfolio-builder` - 360 brand guidelines
- `360-board-meeting-prep` - 360 board structure

---

## Common Confusion: Skill Pairs

### workflow-process-generator

**Two versions exist:**

1. **Managed (Generic)**: `.claude/skills/workflow-process-generator/`
   - Purpose: Generic SOP generation for any organization
   - Output: Compliance-ready process documentation
   - Use when: Creating standard SOPs, runbooks, work instructions

2. **User (360-Specific)**: `skills/workflow-process-generator/`
   - Purpose: 360-specific workflow extraction from Asana/Drive/Gmail
   - Output: Mermaid diagrams, interactive HTML for 360 processes
   - Use when: Documenting 360 internal workflows

### Persona Builders

**Strategic wins:**

- **strategic-persona-builder**: Multi-framework (Vianeo + JTBD + empathy mapping)
- **vianeo-persona-builder**: Vianeo-focused subset (use strategic-persona-builder with Vianeo framework instead)

**Recommendation**: Use `strategic-persona-builder` for all persona work, including Vianeo.

### Client Portfolio Builder

**No difference - use managed version:**

- `.claude/skills/360-client-portfolio-builder/` - Production-ready, comprehensive docs

---

## Creating New 360 Skills

**Quick Decision Tree:**

```
Need new skill?
├─ Universally applicable?
│  └─ Create in skills/, consider for promotion to .claude/skills/
└─ 360-specific context/integration?
   ├─ Development: Create in skills/
   └─ Production: Create in .claude/skills/ (after validation)
```

**Required Files:**
- SKILL.md (with YAML frontmatter)
- README.md
- QUICK-START.md

**See**: [Creating Skills Guide](../../docs/CREATING-SKILLS.md)

---

## Troubleshooting

**"Claude can't find my 360 skill"**
→ Check skill has SKILL.md with proper YAML frontmatter
→ Run `python scripts/validate_skill_structure.py`
→ Ensure skill is in `skills/` or `.claude/skills/` directory

**"Should I use the user or managed version?"**
→ Managed (`.claude/skills/`) = Production-ready, comprehensive docs
→ User (`skills/`) = Development, experimental, or specialized

**"How do I know if a skill is 360-specific?"**
→ Look for "360" prefix in name
→ Check description for 360-specific context
→ Review dependencies for 360 tools (Asana projects, etc.)

---

## Next Steps

1. ✅ **Find the skill you need** from the table above
2. ✅ **Navigate to that skill's directory**
3. ✅ **Read its QUICK-START.md or README.md**
4. ✅ **Use the skill** according to its documentation

---

**This directory exists for organization only. Always use specific skills for actual work!**

Version 1.0.0 | Updated: 2025-11-22 | 360 Social Impact Studios
