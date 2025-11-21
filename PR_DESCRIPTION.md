# Pull Request: Refactor workflow-process-generator skill with lazy loading architecture

## Summary

This PR implements a lazy loading architecture for the `workflow-process-generator` skill, achieving a **79% reduction** in initial context load (from 2,045 lines to 428 lines).

Building on the successful refactoring of `ai-ethics-advisor` (PR #98), this refactoring applies the same modular architecture pattern to make the skill more memory-efficient while preserving all functionality.

## Key Changes

### Size Reduction
- **Before**: 2,045 lines (58KB)
- **After**: 428 lines (12KB)
- **Reduction**: 79% smaller initial load

### New Modular Structure

```
.claude/skills/workflow-process-generator/
├── SKILL.md (428 lines) - Core routing logic and quick reference
├── SKILL.md.backup (2,045 lines) - Original preserved
└── modules/
    ├── protocols/
    │   └── operational-protocols.md - 6 step-by-step protocols for documentation projects
    ├── document-types/
    │   └── document-types.md - Detailed guidance for SOPs, process maps, runbooks, etc.
    ├── templates/
    │   ├── example-sop-customer-onboarding.md - Complete SOP example (600 lines)
    │   └── example-runbook-incident-response.md - Complete runbook example (570 lines)
    ├── quality/
    │   └── quality-frameworks.md - Risk assessment, metrics, QA checklists
    └── reference/
        └── reference.md - Communication guidelines, ethics, special situations
```

## How It Works

The refactored skill uses **on-demand module loading** based on user requests:

### Example Usage Scenarios

**Scenario 1: "Document our customer onboarding process"**
- Initial load: Core SKILL.md (~400 lines)
- Then loads: operational-protocols.md (~275 lines)
- Optionally: example-sop-customer-onboarding.md (~600 lines)
- **Total: ~900-1,275 lines** vs. original 2,045 lines

**Scenario 2: "Quick job aid for a simple task"**
- Initial load: Core SKILL.md (~400 lines)
- Then loads: document-types.md work instructions section (~50 lines)
- **Total: ~450 lines** vs. original 2,045 lines

**Scenario 3: "Create an incident response runbook"**
- Initial load: Core SKILL.md (~400 lines)
- Then loads: document-types.md runbook section (~100 lines)
- Optionally: example-runbook-incident-response.md (~570 lines)
- **Total: ~500-1,070 lines** vs. original 2,045 lines

## Module Loading Strategy

The core SKILL.md includes clear routing logic:

**Operational Protocols** → Load when:
- Starting a new documentation project
- Need step-by-step guidance on process discovery
- Conducting information gathering

**Document Types** → Load when:
- User asks about specific documentation types
- Need detailed guidance on SOPs, process maps, runbooks
- Determining appropriate documentation format

**Templates** → Load when:
- User needs a complete example to reference
- Creating similar documentation

**Quality Frameworks** → Load when:
- Assessing process risk level
- Defining quality metrics and KPIs
- Need compliance or audit readiness guidance

**Reference Material** → Load when:
- Need communication guidelines
- Ethical considerations questions
- Handling special situations

## Benefits

1. **Memory Efficiency**: 79% reduction in initial context usage
2. **Targeted Loading**: Only load relevant sections for each specific task
3. **Easier Maintenance**: Update specific modules independently
4. **Clearer Structure**: Modules correspond to documentation project phases
5. **Backward Compatible**: All original capabilities preserved
6. **Better UX**: Faster skill activation and more responsive conversations

## Files Changed

- `SKILL.md` - Complete rewrite with routing logic (2,197 deletions, 290 additions)
- `SKILL.md.backup` - Original preserved (2,045 additions)
- 6 new module files created (4,616 additions)

## Testing

The refactored skill maintains:
- All 6 core expertise areas (SOPs, Process Maps, Runbooks, Work Instructions, Governance, Training)
- All specialized documentation types
- Complete examples for reference
- All quality frameworks and compliance guidance
- Full professional standards and ethical considerations

## Related Work

This follows the same lazy loading pattern successfully implemented in PR #98 for the `ai-ethics-advisor` skill, which achieved a 67% reduction in context usage.

## Review Notes

- No functionality has been removed - only reorganized into modules
- Original SKILL.md backed up as SKILL.md.backup
- Module boundaries align with natural documentation project workflows
- Routing logic tested with common user scenarios
