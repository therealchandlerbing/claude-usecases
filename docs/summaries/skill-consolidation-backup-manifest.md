# Skill Consolidation Backup Manifest
Generated: 2025-12-06 UTC

## Purpose
This document records the state of all duplicate skills BEFORE consolidation.
Use this to verify no data was lost during the consolidation process.

## Duplicate Skills Inventory

The following 8 skills exist in both locations:
1. ceo-advisor
2. design-director
3. executive-impact-presentation-generator
4. 360-client-portfolio-builder
5. intelligence-extractor
6. open-deep-research-team
7. skill-orchestrator
8. workflow-process-generator

## Consolidation Strategy Summary

| Skill | Canonical Location | Action |
|-------|-------------------|--------|
| ceo-advisor | .claude/skills/ | Merge unique files + config pattern from skills/ |
| design-director | .claude/skills/ (v1.1.0) | Merge COMPLETE-GUIDE.md, QUICK-REFERENCE.md |
| executive-impact-presentation-generator | .claude/skills/ (v1.1.0) | Merge INDEX.md, CONTENT_SCHEMA_TEMPLATE.md, QUICK_REFERENCE.md |
| 360-client-portfolio-builder | .claude/skills/ | Direct symlink (no unique files in skills/) |
| intelligence-extractor | skills/ (v1.1.0) → .claude/skills/ | Reverse merge: move skills/ to .claude/, add unique files |
| open-deep-research-team | .claude/skills/ (v2.1.0) | Merge docs/, examples/workflow_example.md |
| skill-orchestrator | .claude/skills/ | Merge EXAMPLES.md, IMPLEMENTATION.md, REFERENCE.md |
| workflow-process-generator | .claude/skills/ (v2.0.0) | Merge INDEX.md, examples/, references/, templates/* |

## File Structures Before Consolidation

### ceo-advisor

**.claude/skills/ceo-advisor:**
- .claude/skills/ceo-advisor/IMPLEMENTATION-GUIDE.md (25680 bytes)
- .claude/skills/ceo-advisor/INDEX.md (8091 bytes)
- .claude/skills/ceo-advisor/QUICK-START.md (5725 bytes)
- .claude/skills/ceo-advisor/README.md (8505 bytes)
- .claude/skills/ceo-advisor/SKILL.md (23935 bytes)
- .claude/skills/ceo-advisor/config/config.json (3338 bytes)
- .claude/skills/ceo-advisor/config/requirements.txt (751 bytes)
- .claude/skills/ceo-advisor/docs/QUALITY-VALIDATION.md (8248 bytes)
- .claude/skills/ceo-advisor/examples/SCENARIOS.md (15696 bytes)
- .claude/skills/ceo-advisor/examples/sample_data_generator.py (10459 bytes)
- .claude/skills/ceo-advisor/src/__init__.py (2687 bytes)
- .claude/skills/ceo-advisor/src/ceo_advisor_orchestrator.py (28716 bytes)
- .claude/skills/ceo-advisor/src/ceo_optimizer.py (12168 bytes)
- .claude/skills/ceo-advisor/src/executive_intelligence_system.py (14262 bytes)
- .claude/skills/ceo-advisor/src/financial_advisor.py (26356 bytes)
- .claude/skills/ceo-advisor/src/stakeholder_analytics.py (14727 bytes)
- .claude/skills/ceo-advisor/src/strategy_advisor.py (29529 bytes)
- .claude/skills/ceo-advisor/templates/EXECUTIVE-FRAMEWORKS.md (11701 bytes)

**skills/ceo-advisor:**
- skills/ceo-advisor/QUICK-START.md (5357 bytes)
- skills/ceo-advisor/README.md (9857 bytes)
- skills/ceo-advisor/SKILL.md (9734 bytes)
- skills/ceo-advisor/config/config.json (3338 bytes)
- skills/ceo-advisor/config/requirements.txt (751 bytes)
- skills/ceo-advisor/docs/QUICKSTART.md (4664 bytes) ← UNIQUE
- skills/ceo-advisor/docs/prompt_templates.md (7288 bytes) ← UNIQUE
- skills/ceo-advisor/examples/sample_data_generator.py (10459 bytes)
- skills/ceo-advisor/src/ceo_advisor_orchestrator.py (28886 bytes) ← HAS BETTER CONFIG PATTERN
- skills/ceo-advisor/src/ceo_optimizer.py (12296 bytes)
- skills/ceo-advisor/src/executive_intelligence_system.py (14387 bytes)
- skills/ceo-advisor/src/stakeholder_analytics.py (14769 bytes)

### design-director

**.claude/skills/design-director:**
- .claude/skills/design-director/INDEX.md (7354 bytes)
- .claude/skills/design-director/QUICK-START.md (5388 bytes)
- .claude/skills/design-director/README.md (6702 bytes)
- .claude/skills/design-director/SKILL.md (18281 bytes)
- .claude/skills/design-director/examples/README.md (7049 bytes)
- .claude/skills/design-director/references/brands/360-social-impact/360-brand-standards.md (17444 bytes)
- .claude/skills/design-director/references/brands/360-social-impact/360-integration-guide.md (21961 bytes)
- .claude/skills/design-director/references/brands/360-social-impact/360-quality-checklist.md (13134 bytes)
- .claude/skills/design-director/references/brands/360-social-impact/360-quick-reference.md (10395 bytes)
- .claude/skills/design-director/references/design-philosophy.md (4496 bytes)
- .claude/skills/design-director/references/elevation-protocol.md (10439 bytes)
- .claude/skills/design-director/references/exemplars.md (9521 bytes)
- .claude/skills/design-director/references/interrogation-checklist.md (6333 bytes)
- .claude/skills/design-director/references/technique-catalog.md (10830 bytes)

**skills/design-director:**
- skills/design-director/COMPLETE-GUIDE.md (10859 bytes) ← UNIQUE
- skills/design-director/INDEX.md (7186 bytes)
- skills/design-director/QUICK-REFERENCE.md (6757 bytes) ← UNIQUE
- skills/design-director/QUICK-START.md (5486 bytes)
- skills/design-director/README.md (17213 bytes)
- skills/design-director/SKILL.md (15812 bytes)
- skills/design-director/examples/README.md (7049 bytes)
- skills/design-director/references/design-philosophy.md (4496 bytes)
- skills/design-director/references/elevation-protocol.md (10439 bytes)
- skills/design-director/references/exemplars.md (9521 bytes)
- skills/design-director/references/interrogation-checklist.md (6333 bytes)
- skills/design-director/references/technique-catalog.md (10830 bytes)

### executive-impact-presentation-generator

**.claude/skills/executive-impact-presentation-generator:**
- .claude/skills/executive-impact-presentation-generator/EXAMPLES.md (22091 bytes)
- .claude/skills/executive-impact-presentation-generator/IMPLEMENTATION-GUIDE.md (29828 bytes)
- .claude/skills/executive-impact-presentation-generator/QUICK-START.md (7548 bytes)
- .claude/skills/executive-impact-presentation-generator/README.md (14596 bytes)
- .claude/skills/executive-impact-presentation-generator/SKILL.md (14007 bytes)
- .claude/skills/executive-impact-presentation-generator/SKILL.md.backup (41905 bytes)
- .claude/skills/executive-impact-presentation-generator/modules/* (various)
- .claude/skills/executive-impact-presentation-generator/templates/* (various)

**skills/executive-impact-presentation-generator:**
- skills/executive-impact-presentation-generator/CONTENT_SCHEMA_TEMPLATE.md (9965 bytes) ← UNIQUE
- skills/executive-impact-presentation-generator/INDEX.md (5630 bytes) ← UNIQUE
- skills/executive-impact-presentation-generator/QUICK_REFERENCE.md (6950 bytes) ← UNIQUE
- skills/executive-impact-presentation-generator/README.md (10619 bytes)
- skills/executive-impact-presentation-generator/SKILL.md (25763 bytes)
- skills/executive-impact-presentation-generator/templates/* (duplicates)

### 360-client-portfolio-builder

**.claude/skills/360-client-portfolio-builder:**
- Complete implementation with IMPLEMENTATION-GUIDE.md, INDEX.md, QUICK-START.md
- Full references/, deployment/, templates/, examples/ directories
- Total: 326K

**skills/360-client-portfolio-builder:**
- Subset of .claude/skills/ version
- No unique files identified
- Total: 107K

### intelligence-extractor

**.claude/skills/intelligence-extractor:**
- .claude/skills/intelligence-extractor/ASANA-SETUP.md (27872 bytes) ← UNIQUE
- .claude/skills/intelligence-extractor/QUICK-START.md (9809 bytes)
- .claude/skills/intelligence-extractor/README.md (17369 bytes)
- .claude/skills/intelligence-extractor/SKILL.md (22411 bytes)
- .claude/skills/intelligence-extractor/ZAPIER-INTEGRATION.md (20640 bytes) ← UNIQUE
- .claude/skills/intelligence-extractor/templates/template-1-partnership-new.md (18416 bytes) ← UNIQUE
- .claude/skills/intelligence-extractor/templates/template-3-funder-initial.md (20092 bytes) ← UNIQUE

**skills/intelligence-extractor:** (v1.1.0 - NEWER)
- skills/intelligence-extractor/INDEX.md (8342 bytes) ← UNIQUE
- skills/intelligence-extractor/QUICK-START.md (9806 bytes)
- skills/intelligence-extractor/README.md (16040 bytes)
- skills/intelligence-extractor/SKILL.md (20992 bytes)
- skills/intelligence-extractor/references/cross-linking-architecture.md (26781 bytes) ← UNIQUE
- skills/intelligence-extractor/references/intelligence-schemas.md (36296 bytes) ← UNIQUE
- skills/intelligence-extractor/templates/00-template-selection-guide.md (9908 bytes) ← UNIQUE
- skills/intelligence-extractor/templates/NOTE.md (3954 bytes) ← UNIQUE

### open-deep-research-team

**.claude/skills/open-deep-research-team:** (v2.1.0 - CANONICAL)
- Complete implementation with all modules, prompts, quality, templates
- Total: 345K

**skills/open-deep-research-team:**
- skills/open-deep-research-team/docs/implementation_guide.md (10131 bytes) ← UNIQUE PATH
- skills/open-deep-research-team/examples/workflow_example.md (10752 bytes) ← UNIQUE
- Total: 140K

### skill-orchestrator

**.claude/skills/skill-orchestrator:** (CANONICAL)
- .claude/skills/skill-orchestrator/INDEX.md (9711 bytes)
- .claude/skills/skill-orchestrator/ORCHESTRATION-STRATEGY.md (20270 bytes)
- .claude/skills/skill-orchestrator/QUICK-START.md (10045 bytes)
- .claude/skills/skill-orchestrator/README.md (15440 bytes)
- .claude/skills/skill-orchestrator/SKILL.md (12659 bytes)
- .claude/skills/skill-orchestrator/docs/EXAMPLES.md (27687 bytes)
- .claude/skills/skill-orchestrator/docs/IMPLEMENTATION.md (18635 bytes)

**skills/skill-orchestrator:**
- skills/skill-orchestrator/EXAMPLES.md (27732 bytes) ← DUPLICATE (root level)
- skills/skill-orchestrator/IMPLEMENTATION.md (18673 bytes) ← DUPLICATE (root level)
- skills/skill-orchestrator/INDEX.md (9903 bytes)
- skills/skill-orchestrator/README.md (15549 bytes)
- skills/skill-orchestrator/REFERENCE.md (10170 bytes) ← UNIQUE
- skills/skill-orchestrator/SKILL.md (12553 bytes)

### workflow-process-generator

**.claude/skills/workflow-process-generator:** (v2.0.0 - CANONICAL)
- Complete implementation with modules/, templates/
- Total: 274K

**skills/workflow-process-generator:**
- skills/workflow-process-generator/INDEX.md (11328 bytes) ← UNIQUE
- skills/workflow-process-generator/examples/partnership-development.md (28825 bytes) ← UNIQUE
- skills/workflow-process-generator/references/* ← UNIQUE DIRECTORY
- skills/workflow-process-generator/templates/mermaid-flowchart.md (7260 bytes) ← UNIQUE
- skills/workflow-process-generator/templates/workflow-json-schema.json (9595 bytes) ← UNIQUE
- Total: 188K

## Verification Checklist

After consolidation, verify:
- [ ] All unique files from skills/ are in .claude/skills/
- [ ] Symlinks work correctly
- [ ] Skill structure validation passes
- [ ] Tests pass
- [ ] No broken imports or references

## Rollback Instructions

If issues occur:
```bash
git checkout claude/skill-consolidation-phase-1-019BRy87owJ8NDf3w5ijpqLL~1
# Or restore from this manifest and rebuild
```
