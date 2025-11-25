# Orchestrate Multi-Skill Workflow

Coordinate complex multi-skill operations using the **Skill Orchestrator** skill.

## Instructions

Invoke the `skill-orchestrator` skill when your request requires multiple capabilities working together.

## When to Use

**Always use orchestrator when:**
- Request involves multiple distinct capabilities (research + analysis + synthesis)
- Need to coordinate between Claude skills and GitHub agents
- Workflow has dependencies (step B requires output from step A)
- Unclear which skill/agent to use
- Request spans multiple domains (Asana + Gmail + Drive)

**Skip orchestrator for:**
- Simple single-skill requests with obvious routing
- Direct questions without tool usage
- Basic information retrieval

## How It Works

### Phase 1: Analysis
1. Catalog check of available skills
2. Complexity assessment
3. Data completeness verification
4. Plan announcement

### Phase 2: Routing Decision
```
Request received
    │
    ├─ Single skill obvious? → Route directly
    │
    ├─ Multiple skills needed? → Map workflow
    │
    ├─ Hybrid workflow? → Coordinate skills + agents
    │
    └─ No matching capability? → Flag for creation
```

### Phase 3: Workflow Execution
For multi-skill workflows:
- Map dependencies between steps
- Execute in sequence with validation gates
- Preserve context between steps
- Deliver integrated results

## Example Workflows

**Morning Routine:**
1. ceo-advisor → Daily brief
2. intelligence-extractor → Process overnight communications

**Board Prep:**
1. 360-executive-project-tracker → Current status
2. financial-modeling-skills → Financial analysis
3. 360-board-meeting-prep → Generate packet
4. design-director → Elevate outputs

---

**Skill**: skill-orchestrator
**Trigger**: "Coordinate [complex request]" / "I need multiple skills" / "Multi-step workflow"
