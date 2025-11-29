# Plugins Reference for Claude-Usecases

**A comprehensive guide to leveraging Claude Code's plugin architecture within the 360 Social Impact Studios skill ecosystem.**

---

## Table of Contents

1. [Overview](#overview)
2. [Architecture Mapping](#architecture-mapping)
3. [Plugin Components in This Repository](#plugin-components-in-this-repository)
4. [Hooks System](#hooks-system)
5. [Agents Directory](#agents-directory)
6. [MCP Server Configuration](#mcp-server-configuration)
7. [Plugin Manifest Format](#plugin-manifest-format)
8. [Distribution & Packaging](#distribution--packaging)
9. [Migration Guide](#migration-guide)

---

## Overview

This repository implements a sophisticated skill-based architecture that aligns with Claude Code's plugin system. The Claude Code plugin system provides five types of components:

| Plugin Component | This Repository's Implementation |
|-----------------|----------------------------------|
| **Commands** | `.claude/commands/*.md` (34 commands) |
| **Agents** | `.claude/agents/*.md` (NEW - to be created) |
| **Skills** | `.claude/skills/` and `skills/` (33 skills) |
| **Hooks** | `.claude/hooks/hooks.json` (NEW - to be created) |
| **MCP Servers** | `.mcp.json` (2 servers configured) |

### Key Differences

| Aspect | Standard Plugin | This Repository |
|--------|----------------|-----------------|
| **Location** | `.claude-plugin/` | `.claude/` (adapted structure) |
| **Manifest** | `plugin.json` | YAML frontmatter in SKILL.md |
| **Skills** | `skills/SKILL.md` | `.claude/skills/*/SKILL.md` |
| **Commands** | `commands/*.md` | `.claude/commands/*.md` |

---

## Architecture Mapping

### Standard Plugin Structure vs. This Repository

**Standard Claude Code Plugin:**
```
my-plugin/
├── .claude-plugin/
│   └── plugin.json           # Plugin manifest
├── commands/                  # Slash commands
│   └── my-command.md
├── agents/                    # Subagents
│   └── my-agent.md
├── skills/                    # Agent Skills
│   └── my-skill/
│       └── SKILL.md
├── hooks/
│   └── hooks.json            # Event handlers
└── .mcp.json                 # MCP servers
```

**This Repository (Adapted):**
```
claude-usecases/
├── .claude/
│   ├── commands/             # ✅ 34 slash commands
│   ├── skills/               # ✅ 20 managed skills
│   ├── agents/               # NEW: Subagent definitions
│   └── hooks/                # NEW: Hook configurations
├── skills/                   # ✅ 13 user skills
├── .mcp.json                 # ✅ MCP server config
└── plugin.json               # NEW: Repository-level manifest
```

---

## Plugin Components in This Repository

### 1. Commands (`.claude/commands/`)

Commands are already fully implemented with 34 markdown-based slash commands.

**Command Types:**

| Type | Count | Example |
|------|-------|---------|
| Single-skill routing | 21 | `/brief`, `/elevate`, `/finance` |
| Multi-skill workflows | 10 | `/morning`, `/venture-launch` |
| Catalog/reference | 3 | `/skills`, `/help` |

**Command Format (Current):**
```markdown
# Command Name

**Skill**: skill-name
**Trigger Phrases**: "trigger1", "trigger2"

## Instructions
[Workflow steps]

## Output Format
[Expected deliverables]
```

**Enhanced Format (With Plugin Frontmatter):**
```markdown
---
name: command-name
description: Brief description
allowed_args: $ARGUMENTS
---

# Command Name

[Content...]
```

### 2. Skills (`.claude/skills/` and `skills/`)

Skills follow the standard SKILL.md format with YAML frontmatter:

```markdown
---
name: skill-name
description: Description (20+ chars)
version: 1.0.0
author: 360 Social Impact Studios
category: category-name
---

# Skill Name

[Operational instructions for Claude...]
```

### 3. Agents (`.claude/agents/`) - NEW

Agents are specialized subagents that Claude can invoke for specific tasks. See [Agents Directory](#agents-directory) below.

### 4. Hooks (`.claude/hooks/`) - NEW

Hooks provide event-based automation. See [Hooks System](#hooks-system) below.

### 5. MCP Servers (`.mcp.json`) - EXISTING

Already configured with:
- **Supabase MCP**: Real-time database access
- **Google Drive MCP**: File search and retrieval

---

## Hooks System

### What Are Hooks?

Hooks are event handlers that execute automatically in response to Claude Code events. They enable:

- **Pre-execution validation**: Check conditions before tool use
- **Post-execution automation**: Format code, run tests, update logs
- **Quality enforcement**: Validate outputs meet standards
- **Integration triggers**: Sync with external systems

### Hook Events

| Event | Trigger | Use Case |
|-------|---------|----------|
| `PreToolUse` | Before any tool use | Validate inputs, check permissions |
| `PostToolUse` | After tool completes | Format files, run linters |
| `PermissionRequest` | Permission dialog shown | Log access requests |
| `UserPromptSubmit` | User submits prompt | Log interactions |
| `Notification` | Claude sends notification | Forward to Slack/Teams |
| `Stop` | Claude attempts to stop | Cleanup operations |
| `SubagentStop` | Subagent stops | Aggregate results |
| `SessionStart` | Session begins | Initialize environment |
| `SessionEnd` | Session ends | Save state, cleanup |
| `PreCompact` | Before history compaction | Preserve important context |

### Hook Configuration

**Location:** `.claude/hooks/hooks.json`

**Basic Structure:**
```json
{
  "hooks": {
    "EventName": [
      {
        "matcher": "ToolPattern|AnotherPattern",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/handler.sh"
          }
        ]
      }
    ]
  }
}
```

### Recommended Hooks for This Repository

See `.claude/hooks/hooks.json` for the full implementation:

1. **PostToolUse - Write/Edit**: Format Python/TypeScript files
2. **PostToolUse - Write/Edit**: Validate skill structure
3. **SessionStart**: Load skill catalog context
4. **UserPromptSubmit**: Log interaction for analytics
5. **PreToolUse - Bash**: Security scan for dangerous commands

---

## Agents Directory

### What Are Agents?

Agents are specialized subagents that Claude can invoke automatically when a task matches their expertise. Unlike skills (which are invoked by name), agents are invoked based on task context.

### Agent Definition Format

**Location:** `.claude/agents/`

```markdown
---
description: What this agent specializes in
capabilities: ["capability1", "capability2", "capability3"]
---

# Agent Name

Detailed description of the agent's role, expertise, and when Claude should invoke it.

## Capabilities

- Specific task the agent excels at
- Another specialized capability
- When to use this agent vs others

## Context and Examples

Provide examples of when this agent should be used and what kinds of problems it solves.

## Integration

How this agent works with skills in this repository.
```

### Recommended Agents for This Repository

| Agent | Description | Skills Used |
|-------|-------------|-------------|
| `financial-analyst` | Financial analysis, compliance, and nonprofit tax preparation | 990-ez-preparation, financial-modeling-skills, executive-intelligence-dashboard |
| `research-coordinator` | Multi-source research across academic, technical, and market domains | open-deep-research-team, strategic-persona-builder, ai-ethics-advisor, fda-consultant-agent |
| `design-reviewer` | Design quality, accessibility, and brand consistency | design-director, executive-impact-presentation-generator, 360-client-portfolio-builder |
| `compliance-checker` | FDA, AI ethics, financial, and privacy compliance | fda-consultant-agent, ai-ethics-advisor, 990-ez-preparation, contract-redlining-tool |
| `executive-advisor` | 5-expert advisory board for executive decision support | ceo-advisor, executive-intelligence-dashboard, 360-board-meeting-prep, intelligence-extractor |

---

## MCP Server Configuration

### Current Configuration

**File:** `.mcp.json`

```json
{
  "mcpServers": {
    "supabase": {
      "transport": "http",
      "url": "https://mcp.supabase.com/mcp?project_ref=PROJECT_REF",
      "headers": {
        "Authorization": "Bearer TOKEN"
      }
    },
    "gdrive": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-gdrive"]
    }
  }
}
```

### Adding New MCP Servers

```json
{
  "mcpServers": {
    "existing-server": { ... },
    "new-server": {
      "command": "npx",
      "args": ["-y", "@org/mcp-server-name", "--option", "value"],
      "env": {
        "API_KEY": "${API_KEY}"
      },
      "cwd": "${CLAUDE_PLUGIN_ROOT}"
    }
  }
}
```

### Recommended Additional Servers

| Server | Purpose | Package |
|--------|---------|---------|
| Asana | Project management | `@anthropic/mcp-server-asana` |
| GitHub | Repository access | `@anthropic/mcp-server-github` |
| Slack | Team communication | `@anthropic/mcp-server-slack` |
| PostgreSQL | Direct database access | `@anthropic/mcp-server-postgres` |

---

## Plugin Manifest Format

### Repository-Level Manifest

Create `plugin.json` at repository root to formalize the entire repository as a distributable plugin:

```json
{
  "name": "claude-usecases",
  "version": "2.8.0",
  "description": "Comprehensive Claude AI skills and workflows for business automation",
  "author": {
    "name": "360 Social Impact Studios",
    "email": "dev@360socialimpact.com",
    "url": "https://github.com/therealchandlerbing"
  },
  "homepage": "https://github.com/therealchandlerbing/claude-usecases",
  "repository": "https://github.com/therealchandlerbing/claude-usecases",
  "license": "MIT",
  "keywords": [
    "claude-code",
    "ai-skills",
    "business-automation",
    "executive-intelligence",
    "financial-compliance"
  ],
  "commands": "./.claude/commands/",
  "agents": "./.claude/agents/",
  "hooks": "./.claude/hooks/hooks.json",
  "mcpServers": "./.mcp.json"
}
```

### Skill-Level Manifests (Optional)

For distributing individual skills as standalone plugins, create a manifest in the skill directory:

```json
{
  "name": "skill-name",
  "version": "1.0.0",
  "description": "Skill description",
  "author": {
    "name": "360 Social Impact Studios"
  },
  "keywords": ["skill-type", "domain"]
}
```

---

## Distribution & Packaging

### Distributing Skills as Plugins

To package a skill for distribution:

1. **Create skill plugin structure:**
   ```
   skill-name-plugin/
   ├── .claude-plugin/
   │   └── plugin.json
   ├── skills/
   │   └── skill-name/
   │       └── SKILL.md
   └── README.md
   ```

2. **Create minimal plugin.json:**
   ```json
   {
     "name": "skill-name",
     "version": "1.0.0",
     "description": "Brief description"
   }
   ```

3. **Publish to GitHub/npm/marketplace**

### Installing Skills as Plugins

```bash
# From Git repository
claude plugins install github:username/skill-plugin

# From local path
claude plugins install ./path/to/skill-plugin
```

---

## Migration Guide

### Migrating Existing Skills to Plugin Format

**Step 1: Add Plugin Manifest**

Create `.claude-plugin/plugin.json`:
```json
{
  "name": "skill-name",
  "version": "1.0.0",
  "description": "From SKILL.md frontmatter"
}
```

**Step 2: Restructure if Needed**

Move SKILL.md to `skills/skill-name/SKILL.md` if distributing standalone.

**Step 3: Add Hooks (Optional)**

Create `hooks/hooks.json` for automation.

**Step 4: Test Distribution**

```bash
# Install locally
claude plugins install ./skill-directory

# Verify
claude plugins list
```

### Backward Compatibility

The current skill structure remains fully compatible. The plugin format is additive - you can:

1. Keep existing `.claude/skills/` structure
2. Add plugin manifests gradually
3. Add hooks and agents incrementally
4. Distribute individual skills as needed

---

## Environment Variables

### Available in Hooks and Scripts

| Variable | Description |
|----------|-------------|
| `${CLAUDE_PLUGIN_ROOT}` | Absolute path to plugin root |

### Usage Example

```json
{
  "hooks": {
    "PostToolUse": [{
      "hooks": [{
        "type": "command",
        "command": "${CLAUDE_PLUGIN_ROOT}/scripts/format.sh"
      }]
    }]
  }
}
```

---

## Debugging

### Enable Debug Mode

```bash
claude --debug
```

Shows:
- Plugin loading details
- Command/agent/hook registration
- MCP server initialization
- Any errors in manifests

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Plugin not loading | Invalid JSON | Validate plugin.json syntax |
| Hooks not firing | Script not executable | `chmod +x script.sh` |
| Commands missing | Wrong directory | Ensure at root, not in .claude-plugin/ |
| MCP fails | Missing env var | Use `${CLAUDE_PLUGIN_ROOT}` for paths |

---

## Quick Reference

### File Locations

| Component | Location |
|-----------|----------|
| Commands | `.claude/commands/*.md` |
| Skills (managed) | `.claude/skills/*/SKILL.md` |
| Skills (user) | `skills/*/SKILL.md` |
| Agents | `.claude/agents/*.md` |
| Hooks | `.claude/hooks/hooks.json` |
| MCP Servers | `.mcp.json` |
| Plugin Manifest | `plugin.json` or `.claude-plugin/plugin.json` |

### Key Commands

```bash
# List installed plugins
claude plugins list

# Install plugin
claude plugins install <source>

# Enable debug
claude --debug

# Validate skill structure
python scripts/validate_skill_structure.py --verbose
```

---

## See Also

- [Creating Skills](./CREATING-SKILLS.md) - Skill creation guide
- [Testing](./TESTING.md) - Testing infrastructure
- [Skill Structure Validation](./SKILL-STRUCTURE-VALIDATION.md) - Validation requirements
- [CLAUDE.md](../CLAUDE.md) - Main repository documentation

---

*Updated: November 2025 | Version: 1.0.0*
