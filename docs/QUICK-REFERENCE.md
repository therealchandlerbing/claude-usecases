# Quick Reference Guide

**Fast answers for common tasks in the claude-usecases repository.**

---

## Skill Locations

| Type | Location | Purpose |
|------|----------|---------|
| **Managed Skills** | `.claude/skills/` | Production-ready, fully tested (20 skills) |
| **User Skills** | `skills/` | Development, custom implementations (12+ skills) |
| **Templates** | `skills/templates/` | Starting point for new skills |

---

## Creating a New Skill

### 1. Create Directory Structure
```bash
mkdir -p skills/your-skill-name/{src,config,templates,docs}
```

### 2. Create Required Files
```bash
# Required
touch skills/your-skill-name/SKILL.md
touch skills/your-skill-name/README.md
touch skills/your-skill-name/QUICK-START.md
```

### 3. Add YAML Frontmatter to SKILL.md
```yaml
---
name: your-skill-name
description: Brief description of what this skill does
version: 1.0.0
author: Your Name
category: appropriate-category
---

# Your Skill Name

## When to Activate
...
```

### 4. Validate Structure
```bash
python scripts/validate_skill_structure.py --verbose
```

---

## Required Files by Skill Type

### Managed Skills (.claude/skills/)
| File | Required | Min Size |
|------|----------|----------|
| SKILL.md | Yes | 500 bytes |
| README.md | Yes | 200 bytes |
| QUICK-START.md | Yes | 100 bytes |
| INDEX.md | Recommended | - |
| IMPLEMENTATION-GUIDE.md | Recommended | - |

### User Skills (skills/)
| File | Required | Min Size |
|------|----------|----------|
| SKILL.md | Yes | 200 bytes |
| README.md | Recommended | - |
| QUICK-START.md | Recommended | - |

---

## YAML Frontmatter Requirements

```yaml
---
name: skill-name              # Required: lowercase-with-hyphens
description: What it does     # Required: 20+ characters for managed
version: 1.0.0               # Required: semantic versioning (X.Y.Z)
author: Author Name          # Recommended
category: skill-category     # Recommended
created: 2025-01-01         # Optional
---
```

---

## Running Tests

### Python Tests
```bash
# All tests
pytest

# With coverage
pytest --cov

# Specific marker
pytest -m financial
pytest -m compliance

# Single file
pytest tests/unit/python/test_990_orchestrator.py -v
```

### TypeScript Tests
```bash
# Intelligence Dashboard
cd intelligence-dashboard && npm test

# With coverage
npm run test:coverage

# Watch mode
npm run test:watch
```

---

## Test Markers

| Marker | Purpose |
|--------|---------|
| `@pytest.mark.unit` | Unit tests |
| `@pytest.mark.integration` | Integration tests |
| `@pytest.mark.financial` | Financial calculations (HIGH PRIORITY) |
| `@pytest.mark.compliance` | Regulatory compliance (HIGH PRIORITY) |
| `@pytest.mark.slow` | Long-running tests |

---

## Git Workflow

### Branch Naming
```
claude/feature-description-{session-id}
```

### Commit & Push
```bash
git add -A
git commit -m "Description of changes"
git push -u origin claude/your-branch-name
```

### Create PR
Use GitHub UI with `.github/pull_request_template.md`

---

## CI/CD Overview

| Workflow | Triggers | Blocking |
|----------|----------|----------|
| `tests.yml` | Push, PR | Yes (all tests) |
| `code-quality.yml` | Push, PR | No (informational) |
| `coverage.yml` | Push to main, PR | No (informational) |

---

## Skill Categories

| Category | Skills | Example |
|----------|--------|---------|
| Executive Intelligence | ceo-advisor, executive-intelligence-dashboard | Daily briefs, board prep |
| Financial/Compliance | 990-ez-preparation, financial-modeling-skills | Tax filing, analysis |
| Research | open-deep-research-team, strategic-persona-builder | Multi-agent research |
| Design | design-director, executive-impact-presentation | Professional polish |
| Sales | sales-automator, 360-proposal-builder | Outreach, proposals |
| Process | workflow-process-generator, workflow-debugging | SOPs, debugging |

---

## Common Commands

### Skill Validation
```bash
python scripts/validate_skill_structure.py --verbose
```

### Run Specific Skill
```bash
# CEO Advisor
python skills/ceo-advisor/src/ceo_advisor_orchestrator.py daily

# Invoke via Claude
"Prepare our 990-EZ for 2024"
"Generate daily intelligence brief"
```

### Check Coverage
```bash
pytest --cov=skills --cov-report=html
open htmlcov/index.html
```

---

## Directory Structure

```
claude-usecases/
├── .claude/skills/          # 20 managed production skills
├── skills/                  # 12+ user/development skills
├── intelligence-dashboard/  # Next.js real-time dashboard
├── tests/                   # pytest + vitest test suites
├── docs/                    # Documentation hub
├── config/                  # Validation configuration
├── scripts/                 # Automation utilities
├── templates/               # Output templates
└── .github/workflows/       # CI/CD pipelines
```

---

## Key Configuration Files

| File | Purpose |
|------|---------|
| `CLAUDE.md` | AI assistant guide (1,564 lines) |
| `pytest.ini` | Python test configuration |
| `requirements-test.txt` | Test dependencies |
| `config/skill-structure-requirements.yaml` | Validation rules |

---

## Fixtures Available (conftest.py)

| Fixture | Returns |
|---------|---------|
| `project_root` | Path to repo root |
| `skills_dir` | Path to skills/ |
| `claude_skills_dir` | Path to .claude/skills/ |
| `test_data_dir` | Path to tests/data/ |
| `temp_output_dir` | Temporary directory |
| `sample_financial_data` | Sample financial dict |
| `sample_990_data` | Sample IRS 990 data |
| `sample_persona_data` | Sample Vianeo persona |

---

## Getting Help

| Resource | Location |
|----------|----------|
| Full documentation | `CLAUDE.md` |
| Testing guide | `docs/TESTING.md` |
| Skill creation | `docs/CREATING-SKILLS.md` |
| Validation guide | `docs/SKILL-STRUCTURE-VALIDATION.md` |
| Individual skill docs | Each skill's README.md |

---

## Quick Troubleshooting

| Issue | Solution |
|-------|----------|
| Import errors | Add to PYTHONPATH: `export PYTHONPATH="${PYTHONPATH}:$(pwd)"` |
| Missing module | `pip install -r requirements-test.txt` |
| TypeScript errors | `cd intelligence-dashboard && npm install` |
| Validation fails | Check YAML frontmatter in SKILL.md |
| Push rejected | Ensure branch starts with `claude/` |

---

*Updated: November 2025 | Repository v2.7.0*
