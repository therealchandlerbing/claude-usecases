# Creating Skills for Claude

**A comprehensive guide to creating effective, validated skills in the claude-usecases repository.**

---

## What is a Skill?

A skill is a structured set of instructions that provides Claude with specific methodology for handling tasks. Skills ensure consistent, high-quality outputs by defining:

- **Activation triggers** - When to use the skill
- **Step-by-step workflow** - How to execute
- **Validation criteria** - Quality checks
- **Expected outputs** - What to deliver

---

## Skill Types

### Managed Skills (`.claude/skills/`)
Production-ready, fully documented, maintained by 360 team.
- 100% file compliance required
- Comprehensive testing expected
- Used in production workflows

### User Skills (`skills/`)
Development or custom skills.
- More flexible requirements
- Good for experimentation
- Can be promoted to managed after validation

---

## Required File Structure

### Minimum Structure (User Skills)
```
skills/your-skill-name/
├── SKILL.md              # Required - Main logic
├── README.md             # Recommended - User docs
└── QUICK-START.md        # Recommended - Fast reference
```

### Full Structure (Managed Skills)
```
.claude/skills/your-skill-name/
├── SKILL.md              # Required - Main logic (500+ bytes)
├── README.md             # Required - User docs (200+ bytes)
├── QUICK-START.md        # Required - Fast reference (100+ bytes)
├── INDEX.md              # Recommended - Navigation
├── IMPLEMENTATION-GUIDE.md  # Recommended - Setup guide
├── EXAMPLES.md           # Recommended - Usage examples
├── src/                  # Python modules (if applicable)
├── config/               # Configuration files
├── templates/            # Output templates
├── references/           # Supporting documentation
└── docs/                 # Additional documentation
```

---

## Creating a New Skill

### Step 1: Create Directory
```bash
mkdir -p skills/your-skill-name
```

### Step 2: Create SKILL.md with Frontmatter
```markdown
---
name: your-skill-name
description: Brief description of what this skill does (20+ characters)
version: 1.0.0
author: Your Name
category: appropriate-category
created: 2025-01-01
---

# Your Skill Name

## When to Activate This Skill

Trigger this skill when the user requests:
- "Specific trigger phrase 1"
- "Specific trigger phrase 2"

## Core Capabilities

1. **Capability One**: Description
2. **Capability Two**: Description

## Workflow

### Phase 1: Initial Assessment
[Step-by-step instructions]

### Phase 2: Execution
[Step-by-step instructions]

### Phase 3: Validation
[Quality checks]

### Phase 4: Delivery
[Output generation]

## Expected Outputs

- Output 1
- Output 2

## Error Handling

[How to handle common issues]

## Integration with Other Skills

[Cross-references to related skills]
```

### Step 3: Create README.md
```markdown
# Your Skill Name

**One-line description of what this skill does.**

## Overview

Detailed explanation of the skill's purpose and value.

## Quick Start

### Prerequisites
- List requirements

### Basic Usage
\`\`\`
"Trigger phrase to activate"
\`\`\`

## Features

- Feature 1
- Feature 2

## Configuration

[Setup instructions if needed]

## Examples

[Concrete usage examples]

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Problem 1 | Solution 1 |

## Version History

- **v1.0.0** (Date): Initial release
```

### Step 4: Create QUICK-START.md
```markdown
# Your Skill Name - Quick Start

**Get started in 5 minutes.**

---

## Instant Start

Say to Claude:
\`\`\`
"Your trigger phrase here"
\`\`\`

---

## Quick Command Reference

| Task | Command |
|------|---------|
| Task 1 | "Command 1" |
| Task 2 | "Command 2" |

---

## Workflow Overview

\`\`\`
Step 1 → Step 2 → Step 3 → Done
\`\`\`

---

## Key Data Needed

- [ ] Item 1
- [ ] Item 2

---

## Get Help

- Full docs: [README.md](README.md)
- Skill spec: [SKILL.md](SKILL.md)
```

### Step 5: Validate Structure
```bash
python scripts/validate_skill_structure.py --verbose
```

---

## YAML Frontmatter Requirements

### Required Fields
| Field | Description | Example |
|-------|-------------|---------|
| `name` | Skill identifier | `your-skill-name` |
| `description` | Purpose (20+ chars for managed) | "Automated workflow for X" |
| `version` | Semantic version | `1.0.0` |

### Recommended Fields
| Field | Description | Example |
|-------|-------------|---------|
| `author` | Creator name | "360 Social Impact Studios" |
| `category` | Skill category | `financial-compliance` |
| `created` | Creation date | `2025-01-01` |

### Version Format
Use semantic versioning: `MAJOR.MINOR.PATCH`
- MAJOR: Breaking changes
- MINOR: New features
- PATCH: Bug fixes

---

## Best Practices

### 1. Be Specific and Actionable
```markdown
# Good
"Ask user for their EIN and organization name"

# Bad
"Get organization info"
```

### 2. Include Context
```markdown
# Good
"Verify gross receipts < $200,000 (IRS threshold for 990-EZ eligibility)"

# Bad
"Check if they qualify"
```

### 3. Provide Concrete Examples
```markdown
## Example Output
\`\`\`yaml
organization:
  name: "Example Corp"
  ein: "12-3456789"
  revenue: 150000
\`\`\`
```

### 4. Define Clear Triggers
```markdown
## When to Activate

Trigger when user says:
- "Prepare our 990-EZ for [year]"
- "Help with nonprofit tax filing"
- "Generate Form 990-EZ"
```

### 5. Include Error Handling
```markdown
## Error Handling

### If gross receipts >= $200,000
Say: "Your organization exceeds 990-EZ limits. You'll need Form 990 instead."
```

### 6. Add Quality Checks
```markdown
## Validation

Before delivering:
- [ ] All calculations verified
- [ ] Required fields complete
- [ ] Narrative quality reviewed
```

---

## Skill Categories

| Category | Description | Examples |
|----------|-------------|----------|
| `executive-leadership` | C-level decision support | ceo-advisor |
| `financial-compliance` | Tax, finance, regulatory | 990-ez-preparation |
| `research-validation` | Research and analysis | open-deep-research-team |
| `design-excellence` | Visual polish and design | design-director |
| `sales-development` | Sales and BD support | sales-automator |
| `process-documentation` | SOPs and workflows | workflow-process-generator |
| `client-showcasing` | Client presentations | 360-client-portfolio-builder |
| `data-intelligence` | Data extraction/analysis | intelligence-extractor |

---

## Testing Your Skill

### Manual Testing
1. Use the skill with Claude
2. Try various trigger phrases
3. Test edge cases
4. Verify outputs match expectations

### Automated Testing (Recommended)
```python
# tests/unit/python/test_your_skill.py
import pytest

@pytest.mark.unit
def test_skill_basic_functionality():
    # Test implementation
    pass

@pytest.mark.financial  # Use appropriate marker
def test_skill_calculations():
    # Test calculations
    pass
```

### Test Markers
- `@pytest.mark.unit` - Basic unit tests
- `@pytest.mark.integration` - Integration tests
- `@pytest.mark.financial` - Financial calculations
- `@pytest.mark.compliance` - Regulatory compliance

---

## Validation Requirements

### File Presence
```bash
python scripts/validate_skill_structure.py --verbose
```

### Checks Performed
- Required files exist
- YAML frontmatter valid
- Required fields present
- Version format correct
- Minimum file sizes met

### Fixing Validation Errors
| Error | Solution |
|-------|----------|
| "Missing SKILL.md" | Create file with frontmatter |
| "Invalid frontmatter" | Check YAML syntax |
| "Missing version" | Add `version: 1.0.0` |
| "Invalid version format" | Use X.Y.Z pattern |

---

## Promoting Skills

### From User to Managed

1. Ensure all required files exist
2. Meet minimum size requirements
3. Add comprehensive documentation
4. Pass all validation checks
5. Add tests (aim for 70%+ coverage)
6. Create PR for review
7. Move to `.claude/skills/` after approval

---

## Integration Points

### With Other Skills
```markdown
## Integration with Other Skills

### When board-meeting-prep is available
Cross-reference governance data...

### When financial-modeling-skills is available
Enhanced financial analysis...
```

### With External Systems
```markdown
## Data Sources

- **QuickBooks**: Financial data via API
- **Asana**: Project data via MCP
- **Google Drive**: Document storage
```

---

## Documentation Resources

| Resource | Location |
|----------|----------|
| Quick Reference | `docs/QUICK-REFERENCE.md` |
| Testing Guide | `docs/TESTING.md` |
| Validation Guide | `docs/SKILL-STRUCTURE-VALIDATION.md` |
| Main Documentation | `CLAUDE.md` |

---

## Example Skills to Reference

### High-Quality Examples
- **990-ez-preparation** - Financial/compliance, 99% test coverage
- **ceo-advisor** - Complex multi-module system
- **open-deep-research-team** - Multi-agent research
- **contract-redlining-tool** - Comprehensive documentation

### Study These For
- YAML frontmatter patterns
- Workflow structure
- Error handling
- Integration patterns
- Testing approaches

---

## Checklist for New Skills

- [ ] Directory created in correct location
- [ ] SKILL.md with valid YAML frontmatter
- [ ] README.md with user documentation
- [ ] QUICK-START.md with fast reference
- [ ] Clear activation triggers defined
- [ ] Step-by-step workflow documented
- [ ] Expected outputs specified
- [ ] Error handling included
- [ ] Validation passes
- [ ] Manual testing completed
- [ ] (Optional) Automated tests added

---

*Updated: November 2025 | See also: `docs/SKILL-STRUCTURE-VALIDATION.md`*
