# Quick Reference Guide

## Creating a New Skill - Fast Track

### 1. Copy the Template
```bash
cp skills/templates/skill-template.md skills/360-use-cases/my-new-skill.md
```

### 2. Fill in the Sections
- **Title**: Clear, descriptive name
- **Description**: One-line explanation
- **Use Case**: When to use this skill
- **Prerequisites**: What's needed
- **Instructions**: Step-by-step process
- **Expected Outputs**: What you'll get
- **Examples**: Real scenarios
- **Notes**: Important tips

### 3. Test It
- Use the skill with Claude
- Verify it produces expected results
- Iterate if needed

### 4. Add to Index
Update `skills/360-use-cases/README.md` with a link to your new skill

## File Naming Conventions

- Use lowercase letters
- Separate words with hyphens
- Be descriptive but concise
- Use `.md` extension

**Good Examples:**
- `customer-onboarding-workflow.md`
- `quarterly-reporting-process.md`
- `data-analysis-template.md`

**Avoid:**
- `Skill1.md` (not descriptive)
- `customer_onboarding.md` (use hyphens, not underscores)
- `WORKFLOW.md` (don't use all caps)

## Skill Section Checklist

When creating a skill, make sure you include:

- [ ] Clear title
- [ ] Brief description
- [ ] Detailed use case explanation
- [ ] List of prerequisites
- [ ] Step-by-step instructions
- [ ] Expected outputs
- [ ] At least one example
- [ ] Important notes or tips
- [ ] Related skills (if applicable)
- [ ] Version history

## Common Skill Types

### Process Documentation
Documents a repeatable business or technical process

### Analysis Template
Provides structure for analyzing data or situations

### Workflow Automation
Guides automation of repetitive tasks

### Decision Framework
Helps make consistent decisions based on criteria

### Report Generator
Templates for creating standardized reports

## Using Skills with Claude

### Method 1: Direct Reference
Share the skill file content directly in your conversation with Claude

### Method 2: Repository Link
Link to the specific skill file in this repository

### Method 3: Skill Chaining
Reference multiple skills in sequence for complex workflows:
1. Use skill A to gather information
2. Use skill B to analyze
3. Use skill C to document

## Tips for Effective Skills

1. **Be Specific**: Vague instructions lead to inconsistent results
2. **Include Context**: Explain why, not just what
3. **Add Examples**: Show don't just tell
4. **Test Thoroughly**: Use the skill yourself before sharing
5. **Iterate**: Update based on real-world usage
6. **Version Control**: Track changes over time

## Directory Structure at a Glance

```
claude-usecases/
├── skills/
│   ├── 360-use-cases/      ← Your 360 skills go here
│   └── templates/           ← Start here for new skills
├── docs/
│   ├── CREATING-SKILLS.md   ← Detailed guide
│   └── QUICK-REFERENCE.md   ← You are here
├── examples/                ← See working examples
└── README.md               ← Project overview
```

## Need Help?

- **Detailed Guide**: See `docs/CREATING-SKILLS.md`
- **Examples**: Check `examples/` directory
- **Template**: Use `skills/templates/skill-template.md`
- **Project Overview**: Read main `README.md`
