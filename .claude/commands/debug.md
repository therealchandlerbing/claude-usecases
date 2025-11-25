# Debug Workflow Failure

Systematically debug complex workflows using the **Workflow Debugging** skill.

## Instructions

Invoke the `workflow-debugging` skill to identify, isolate, and resolve execution failures in multi-step workflows.

## When to Use

**Debug these scenarios:**
- Multi-stage workflow failures in technology assessment
- Cross-system integration issues (US/Brazil operations)
- Asana integration producing incomplete/duplicate tasks
- Client deliverable automation breaking during generation
- Document approval workflows failing across regions
- API rate limiting or authentication issues
- Encoding problems in cross-region data transfer
- Parallel task execution conflicts

## Debugging Methodology

### Phase 1: Pattern Recognition
- Identify error category and common patterns
- Check for known issues in error library

### Phase 2: Systematic Isolation
- Binary search through workflow stages
- Identify exact failure point
- Determine root cause

### Phase 3: Resolution
- Apply automated recovery (60-80% of issues)
- Generate fix recommendation
- Document pattern for future reference

### Phase 4: Notification
- Alert appropriate team members (Slack, Asana, email)
- Update institutional knowledge base

## Value Proposition

- **Reduces debugging time by 60-80%**
- Prevents cascade failures in multi-agent workflows
- Enables distributed team debugging without deep technical expertise
- Creates institutional knowledge through documented patterns
- Supports multilingual error handling for international partnerships

## When NOT to Use

- Simple syntax errors or typos
- Issues resolved by reading error messages directly
- Non-workflow debugging (e.g., frontend UI bugs)
- Performance optimization without actual failures

---

**Skill**: workflow-debugging
**Trigger**: "Debug this workflow" / "Workflow failing" / "Troubleshoot [integration]"
