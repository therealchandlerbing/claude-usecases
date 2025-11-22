# Skill Structure Validation

**Version**: 1.0.0
**Last Updated**: 2025-11-22

---

## Overview

The skill structure validation system automatically enforces consistent directory structure and file organization across all Claude skills in the repository. This prevents structural drift as the skill catalog grows and ensures all skills meet minimum quality standards.

### Why Validate Skill Structure?

As the repository grows with 20+ managed skills and multiple user-created skills, maintaining consistency becomes critical:

- **Discoverability**: Claude can reliably find SKILL.md, README.md, and other expected files
- **Documentation Quality**: Ensures each skill has proper user-facing documentation
- **Maintenance**: Makes it easier to update, refactor, or migrate skills
- **Onboarding**: New contributors immediately understand the expected structure
- **Quality Assurance**: Prevents incomplete or poorly structured skills from being merged

---

## How It Works

### Validation Components

1. **Configuration File**: `config/skill-structure-requirements.yaml`
   - Defines required and recommended files
   - Specifies frontmatter requirements
   - Configures validation rules
   - Customizable error messages

2. **Validation Script**: `scripts/validate_skill_structure.py`
   - Python script that reads configuration
   - Scans all skill directories
   - Validates file presence and frontmatter
   - Outputs detailed error reports

3. **CI/CD Integration**: `.github/workflows/code-quality.yml`
   - Runs automatically on every push and PR
   - Blocks merges if validation fails
   - Provides detailed failure reports

4. **Test Suite**: `tests/unit/python/test_skill_structure_validator.py`
   - 99%+ test coverage
   - Validates validator logic
   - Ensures reliable operation

### Validation Checks

The validator performs the following checks:

#### 1. File Presence Validation
- Ensures required files exist (e.g., SKILL.md, README.md)
- Checks file sizes meet minimum thresholds
- Warns about missing recommended files

#### 2. Frontmatter Validation
- Verifies YAML frontmatter in SKILL.md is valid
- Checks required fields are present (name, description, version)
- Validates field types and formats
- Enforces patterns (e.g., semantic versioning)
- Checks minimum lengths and allowed values

#### 3. Directory Exclusions
- Automatically excludes template directories
- Skips build artifacts (__pycache__, node_modules, .next, etc.)

---

## Configuration

### File Structure Requirements

The configuration file defines different requirements for **managed skills** (`.claude/skills/`) and **user skills** (`skills/`).

#### Managed Skills Requirements

Managed skills are production-ready and have stricter requirements:

**Required Files**:
- `SKILL.md` (min 500 bytes) - Main operational logic with frontmatter
- `README.md` (min 200 bytes) - User-facing documentation
- `QUICK-START.md` (min 100 bytes) - One-page quick reference

**Recommended Files**:
- `IMPLEMENTATION-GUIDE.md` - Setup and deployment instructions
- `EXAMPLES.md` - Concrete usage examples
- `INDEX.md` - Navigation guide (for complex skills)

**Required Frontmatter** (in SKILL.md):
```yaml
---
name: skill-name              # Must match directory name (string)
description: Brief description # Min 20 characters (string)
version: 1.0.0                # Semantic versioning (pattern: \d+\.\d+\.\d+)
---
```

**Recommended Frontmatter**:
```yaml
author: 360 Social Impact Studios  # Creator/maintainer (string)
created: 2024-11-18                # Creation date (YYYY-MM-DD)
category: executive-leadership     # One of allowed categories (string)
```

#### User Skills Requirements

User skills have more relaxed requirements to encourage experimentation:

**Required Files**:
- `SKILL.md` (min 200 bytes) - Main operational logic with frontmatter

**Recommended Files**:
- `README.md` - User-facing documentation
- `QUICK-START.md` - One-page quick reference

**Required Frontmatter**:
```yaml
---
name: skill-name              # Skill identifier (string)
description: Brief description # Min 10 characters (string)
---
```

**Recommended Frontmatter**:
```yaml
version: 1.0.0  # Version string
```

### Allowed Categories

For managed skills, the category field must be one of:

- `executive-leadership`
- `research-validation`
- `financial-compliance`
- `design-visual`
- `sales-business`
- `ai-governance`
- `healthcare-regulatory`
- `process-documentation`
- `workflow-coordination`
- `data-intelligence`

### Customizing Configuration

To modify validation requirements, edit `config/skill-structure-requirements.yaml`:

```yaml
# Example: Add a new required file for managed skills
managed_skills:
  required_files:
    - name: "CHANGELOG.md"
      description: "Version history"
      validation:
        - min_size_bytes: 50

# Example: Add a new category
managed_skills:
  recommended_frontmatter:
    - field: "category"
      type: "string"
      allowed_values:
        - "executive-leadership"
        - "new-category"  # Add your category
```

---

## Running Validation

### Locally (Before Committing)

Run validation on your local machine before pushing:

```bash
# Install dependencies
pip install pyyaml

# Run validation
python scripts/validate_skill_structure.py

# Run with verbose output
python scripts/validate_skill_structure.py --verbose

# Use custom config file
python scripts/validate_skill_structure.py --config path/to/config.yaml
```

### Output Examples

**Valid Skills**:
```
======================================================================
SKILL STRUCTURE VALIDATION SUMMARY
======================================================================

✅ 20 skill(s) with valid structure

----------------------------------------------------------------------
Total skills validated: 20
  ✅ Valid: 20
  ❌ Invalid: 0
  🔴 Total errors: 0
  ⚠️  Total warnings: 0
----------------------------------------------------------------------

✅ All 20 skills have valid structure
```

**Invalid Skills**:
```
======================================================================
SKILL STRUCTURE VALIDATION SUMMARY
======================================================================

❌ 2 skill(s) with errors:

  📁 my-new-skill (user)
     ❌ Required file 'SKILL.md' is missing in skill 'my-new-skill'

  📁 incomplete-skill (managed)
     ❌ Required file 'README.md' is missing in skill 'incomplete-skill'
     ❌ Required frontmatter field 'version' is missing in incomplete-skill/SKILL.md
     ⚠️  Recommended file 'QUICK-START.md' is missing in skill 'incomplete-skill'

----------------------------------------------------------------------
Total skills validated: 22
  ✅ Valid: 20
  ❌ Invalid: 2
  🔴 Total errors: 3
  ⚠️  Total warnings: 1
----------------------------------------------------------------------

❌ Validation failed: 2 skill(s) have structural errors
```

### In CI/CD (Automatic)

Validation runs automatically on:
- Every push to `main`, `master`, or `claude/**` branches
- Every pull request to `main` or `master`

**GitHub Actions Workflow**:
1. Checks out code
2. Sets up Python 3.11
3. Installs PyYAML
4. Runs `validate_skill_structure.py --verbose`
5. Uploads validation artifacts
6. **Fails the build if errors are found** (blocks merge)

### Exit Codes

- `0` - All validations passed ✅
- `1` - Validation failures found ❌
- `2` - Script error (e.g., config file not found) 🔴

---

## Fixing Validation Errors

### Common Errors and Solutions

#### Missing Required File

**Error**:
```
❌ Required file 'README.md' is missing in skill 'my-skill'
```

**Solution**:
```bash
# Create the missing file
touch skills/my-skill/README.md

# Add minimum content
cat > skills/my-skill/README.md << 'EOF'
# My Skill

Brief description of what this skill does.

## Usage

How to use this skill...
EOF
```

#### Missing Frontmatter Field

**Error**:
```
❌ Required frontmatter field 'description' is missing in my-skill/SKILL.md
```

**Solution**:
Add the frontmatter to the top of SKILL.md:

```markdown
---
name: my-skill
description: A comprehensive description of this skill (min 20 chars for managed)
version: 1.0.0
---

# My Skill Documentation

...rest of content...
```

#### Invalid Version Pattern

**Error**:
```
❌ Frontmatter field 'version' in my-skill/SKILL.md: Does not match pattern ^\d+\.\d+\.\d+$
```

**Solution**:
Use semantic versioning (MAJOR.MINOR.PATCH):

```yaml
---
version: 1.0.0  # ✅ Valid
version: v1.0   # ❌ Invalid
version: 1.0    # ❌ Invalid
---
```

#### Description Too Short

**Error**:
```
❌ Frontmatter field 'description' in my-skill/SKILL.md: Length 5 < minimum 20
```

**Solution**:
Expand the description to meet minimum length:

```yaml
---
# ❌ Too short for managed skills
description: Test skill

# ✅ Meets minimum length
description: A comprehensive skill for automated testing and validation
---
```

#### File Too Small

**Warning** (doesn't fail build):
```
⚠️  File 'SKILL.md' in skill 'my-skill' is only 50 bytes (minimum: 500)
```

**Solution**:
Add more substantial content to the file. SKILL.md should have:
- YAML frontmatter
- Clear description
- Step-by-step instructions
- Examples
- Prerequisites
- Output descriptions

---

## Creating Compliant Skills

### Quick Checklist

When creating a new skill, ensure:

**For Managed Skills** (`.claude/skills/`):
- [ ] Directory created: `.claude/skills/my-skill/`
- [ ] `SKILL.md` created with valid frontmatter (500+ bytes)
- [ ] `README.md` created (200+ bytes)
- [ ] `QUICK-START.md` created (100+ bytes)
- [ ] Frontmatter includes: name, description (20+ chars), version (x.y.z)
- [ ] Consider adding: IMPLEMENTATION-GUIDE.md, EXAMPLES.md
- [ ] Run validation: `python scripts/validate_skill_structure.py`
- [ ] All checks pass ✅

**For User Skills** (`skills/`):
- [ ] Directory created: `skills/my-skill/`
- [ ] `SKILL.md` created with valid frontmatter (200+ bytes)
- [ ] Frontmatter includes: name, description (10+ chars)
- [ ] Consider adding: README.md, QUICK-START.md
- [ ] Run validation: `python scripts/validate_skill_structure.py`
- [ ] All checks pass ✅

### Template Usage

Use the skill template as a starting point:

```bash
# Copy template
cp -r skills/templates/skill-template skills/my-new-skill

# Edit SKILL.md
# - Update frontmatter
# - Add your skill logic
vim skills/my-new-skill/SKILL.md

# Validate
python scripts/validate_skill_structure.py
```

---

## Integration with Development Workflow

### Pre-Commit Hook (Optional)

Add validation to your git pre-commit hook:

```bash
#!/bin/bash
# .git/hooks/pre-commit

echo "Running skill structure validation..."
python scripts/validate_skill_structure.py

if [ $? -ne 0 ]; then
    echo "❌ Skill structure validation failed. Fix errors before committing."
    exit 1
fi

echo "✅ Skill structure validation passed"
```

Make it executable:
```bash
chmod +x .git/hooks/pre-commit
```

### VS Code Task

Add validation task to `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Validate Skill Structure",
      "type": "shell",
      "command": "python scripts/validate_skill_structure.py --verbose",
      "problemMatcher": [],
      "group": {
        "kind": "test",
        "isDefault": false
      }
    }
  ]
}
```

Run with: `Cmd+Shift+P` → "Run Task" → "Validate Skill Structure"

---

## Maintenance

### Updating Validation Rules

When adding new requirements:

1. **Update configuration**:
   ```bash
   vim config/skill-structure-requirements.yaml
   ```

2. **Add tests** for new rules:
   ```bash
   vim tests/unit/python/test_skill_structure_validator.py
   ```

3. **Run tests** to ensure validator works:
   ```bash
   pytest tests/unit/python/test_skill_structure_validator.py -v
   ```

4. **Update documentation**:
   ```bash
   vim docs/SKILL-STRUCTURE-VALIDATION.md
   ```

5. **Create migration guide** if breaking changes:
   ```bash
   vim docs/SKILL-STRUCTURE-MIGRATION-v2.md
   ```

### Batch Fixing Existing Skills

If you update requirements and need to fix many skills:

```bash
# Generate list of invalid skills
python scripts/validate_skill_structure.py > validation-report.txt

# Extract skill names with errors
grep "📁" validation-report.txt | awk '{print $2}' > invalid-skills.txt

# Create fix script
while read skill; do
    echo "Fixing $skill..."
    # Add your fix commands here
done < invalid-skills.txt
```

---

## Troubleshooting

### Validation Script Not Found

**Error**: `ModuleNotFoundError: No module named 'yaml'`

**Solution**:
```bash
pip install pyyaml
```

### Permission Denied

**Error**: `Permission denied: scripts/validate_skill_structure.py`

**Solution**:
```bash
chmod +x scripts/validate_skill_structure.py
```

### YAML Parsing Error

**Error**: `Invalid YAML frontmatter in skill/SKILL.md`

**Solution**:
- Ensure frontmatter is wrapped in `---` markers
- Check YAML syntax (indentation, colons, quotes)
- Test YAML at https://yaml-online-parser.appspot.com/

Example of valid frontmatter:
```yaml
---
name: my-skill
description: "Description with: special characters requires quotes"
version: 1.0.0
---
```

### Skills Not Being Found

**Error**: No skills found in directory

**Solution**:
- Check you're running from project root
- Verify skill directories exist: `ls skills/` and `ls .claude/skills/`
- Check exclude patterns in config aren't too broad

---

## Advanced Usage

### Custom Validation Modes

Run validation on specific directories:

```bash
# Modify config to only validate managed skills
# Edit config/skill-structure-requirements.yaml:
settings:
  skill_directories:
    - ".claude/skills/"  # Only managed skills
```

### Programmatic Usage

Use the validator in your own Python scripts:

```python
from scripts.validate_skill_structure import SkillStructureValidator

# Initialize validator
validator = SkillStructureValidator(
    config_path='config/skill-structure-requirements.yaml',
    verbose=True
)

# Validate all skills
summaries = validator.validate_all()

# Check results
for summary in summaries:
    if not summary.is_valid:
        print(f"Skill {summary.skill_name} has errors:")
        for error in summary.errors:
            print(f"  - {error.message}")
```

### Testing Validation Rules

Test configuration changes without modifying main config:

```bash
# Create test config
cp config/skill-structure-requirements.yaml config/test-config.yaml

# Modify test config
vim config/test-config.yaml

# Test with custom config
python scripts/validate_skill_structure.py --config config/test-config.yaml
```

---

## Future Enhancements

Potential improvements to the validation system:

- **Content Quality Validation**: Check for common documentation issues
  - Broken links
  - Missing code examples
  - Insufficient detail in instructions

- **Skill Complexity Analysis**: Classify skills by complexity
  - Simple (single-file)
  - Medium (multi-file, no dependencies)
  - Complex (multi-agent, orchestrated)

- **Auto-Fix Mode**: Automatically create missing files with templates
  ```bash
  python scripts/validate_skill_structure.py --auto-fix
  ```

- **Skill Registry**: Generate catalog of all skills
  ```bash
  python scripts/generate_skill_registry.py
  # Outputs: docs/SKILL-REGISTRY.md
  ```

- **Visual Reports**: Generate HTML validation reports
- **IDE Integration**: Real-time validation in VS Code
- **Dependency Validation**: Check if required Python/Node packages are documented

---

## Related Documentation

- [Creating Skills Guide](CREATING-SKILLS.md) - How to create new skills
- [Testing Infrastructure](TESTING.md) - Testing best practices
- [CLAUDE.md](../CLAUDE.md) - Main repository guide
- [PR Merge Instructions](MERGE_INSTRUCTIONS.md) - How to merge PRs

---

## Appendix: Complete Example

### Valid Managed Skill

Directory structure:
```
.claude/skills/example-skill/
├── SKILL.md                    # 1200 bytes, with frontmatter
├── README.md                   # 450 bytes
├── QUICK-START.md              # 300 bytes
├── IMPLEMENTATION-GUIDE.md     # 800 bytes (recommended)
├── EXAMPLES.md                 # 600 bytes (recommended)
├── src/                        # Optional Python modules
│   └── orchestrator.py
└── config/                     # Optional configuration
    └── settings.yaml
```

SKILL.md:
```markdown
---
name: example-skill
description: A comprehensive example skill demonstrating best practices
version: 1.0.0
author: 360 Social Impact Studios
created: 2024-11-22
category: process-documentation
---

# Example Skill

This skill demonstrates the correct structure and documentation.

## Prerequisites

- Python 3.11+
- Access to example API

## Instructions

1. Step one...
2. Step two...
3. Step three...

## Examples

### Example 1: Basic Usage
...

## Output

The skill produces:
- Result A
- Result B
- Result C

## Troubleshooting

...
```

This skill would pass all validation checks ✅

---

**Version History**:
- v1.0.0 (2025-11-22) - Initial release
