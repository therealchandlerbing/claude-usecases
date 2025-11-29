# Claude Code Agents

This directory contains specialized subagent definitions that Claude can invoke automatically when tasks match their expertise.

## Available Agents

| Agent | Description | Skills Used |
|-------|-------------|-------------|
| [financial-analyst](./financial-analyst.md) | Financial analysis, compliance, 990-EZ preparation | 990-ez-preparation, financial-modeling-skills |
| [research-coordinator](./research-coordinator.md) | Multi-source deep research coordination | open-deep-research-team, strategic-persona-builder |
| [design-reviewer](./design-reviewer.md) | Design quality, accessibility, brand consistency | design-director, executive-impact-presentation-generator |
| [compliance-checker](./compliance-checker.md) | FDA, AI ethics, financial regulations | fda-consultant-agent, ai-ethics-advisor, 990-ez-preparation |
| [executive-advisor](./executive-advisor.md) | 5-expert advisory board for executives | ceo-advisor, executive-intelligence-dashboard |

## How Agents Work

Unlike skills (which are invoked by name or command), agents are invoked **automatically by Claude** when a task matches their capabilities. This enables:

1. **Intelligent routing**: Claude analyzes the request and selects the appropriate agent
2. **Multi-skill coordination**: Agents can leverage multiple skills together
3. **Specialized expertise**: Each agent has deep domain knowledge
4. **Consistent quality**: Agents follow defined methodologies

## Agent File Format

Each agent is defined in a markdown file with YAML frontmatter:

```markdown
---
description: What this agent specializes in
capabilities: ["capability1", "capability2", "capability3"]
tools: ["Read", "Write", "Bash"]
---

# Agent Name

[Detailed description...]

## When Claude Should Invoke This Agent

[Trigger conditions...]

## Capabilities

[Detailed capability list...]

## Context and Examples

[Usage examples...]

## Skills Integration

[How this agent uses repository skills...]
```

## Creating New Agents

1. Create a new markdown file in this directory
2. Add YAML frontmatter with description and capabilities
3. Document when the agent should be invoked
4. List the skills it leverages
5. Provide concrete examples

## Agent vs. Skill

| Aspect | Agent | Skill |
|--------|-------|-------|
| **Invocation** | Automatic by Claude | By name or command |
| **Scope** | Coordinates multiple skills | Single capability |
| **Expertise** | Domain specialist | Task specialist |
| **Output** | Varies by task | Defined deliverables |

---

*See [docs/PLUGINS-REFERENCE.md](../../docs/PLUGINS-REFERENCE.md) for complete plugin architecture documentation.*
