# Creating Skills for Claude

This guide explains how to create effective skill files for Claude that can be used as custom workflows and use cases.

## What is a Skill?

A skill is a structured document that provides Claude with specific instructions, context, and methodology for handling a particular type of task or workflow. Skills help ensure consistent, high-quality outputs by:

- Providing clear step-by-step instructions
- Defining expected inputs and outputs
- Including examples and best practices
- Setting context and prerequisites

## Skill Structure

Every skill should follow a consistent structure to make it easy to use and maintain:

1. **Title & Description** - Clear, concise explanation of what the skill does
2. **Use Case** - When and why to use this skill
3. **Prerequisites** - What's needed before using the skill
4. **Instructions** - Step-by-step process
5. **Expected Outputs** - What results to expect
6. **Examples** - Concrete examples of usage
7. **Notes** - Important considerations
8. **Related Skills** - Links to complementary skills

## Using the Template

We provide a template at `skills/templates/skill-template.md` that you can copy and customize:

```bash
cp skills/templates/skill-template.md skills/360-use-cases/your-skill-name.md
```

## Best Practices

### 1. Be Specific and Actionable
- Use clear, imperative language
- Break complex tasks into smaller steps
- Provide concrete examples

### 2. Include Context
- Explain WHY each step matters
- Note any dependencies or prerequisites
- Highlight potential pitfalls

### 3. Make it Reusable
- Write for general use cases
- Include variables for customization
- Document expected variations

### 4. Test Your Skills
- Try the skill with Claude before finalizing
- Iterate based on results
- Update based on feedback

## Skill Categories

Organize skills by category to make them easy to find:

- **vianeo-persona-builder/** - Research & validation (Vianeo personas, stakeholder analysis)
- **design-director/** - Design & visual excellence (design elevation, polish)
- **360-use-cases/** - Skills specific to 360 workflows
- **general/** - General-purpose skills
- **analysis/** - Data analysis and research skills
- **development/** - Software development skills
- **documentation/** - Documentation and writing skills

## Deploying Skills

### For Claude Desktop/CLI:
Skills can be referenced directly in conversations by sharing the file content or linking to the repository.

### For Custom Workflows:
Skills can be chained together to create complex workflows by referencing multiple skill files in sequence.

## Version Control

Always maintain version history at the bottom of each skill:

```markdown
## Version History
- v1.0 - 2024-01-15 - Initial creation
- v1.1 - 2024-01-20 - Added examples section
- v1.2 - 2024-01-25 - Updated prerequisites
```

## Getting Help

- Review existing skills in the repository for examples
- Check the main README for project overview
- Refer to Claude documentation for advanced features

## Contributing

When adding new skills:

1. Use the template as your starting point
2. Follow the naming convention: `lowercase-with-hyphens.md`
3. Place in the appropriate category folder
4. Update the main README with a link to your skill
5. Test thoroughly before committing
