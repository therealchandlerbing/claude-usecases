# Skill Orchestrator Quick Reference

**Fast lookup for common orchestrator operations and decisions.**

## Quick Decision: Do I Need Orchestrator?

```
Single skill needed -> NO, route directly
Multiple skills in sequence -> YES, orchestrate
GitHub agent call -> YES, orchestrate (payload validation)
Unclear which skill -> YES, orchestrate (routing decision)
Simple question -> NO, answer directly
```

## Orchestrator Activation

**Trigger phrases that need orchestrator:**
- "Generate [complex deliverable] using [multiple sources]"
- "Create assessment package for [client]"
- "Process [meeting] and send follow-ups"
- "Pull data from [system A] and [system B], then synthesize"
- "Research [topic] and create [deliverable]"

**Don't trigger for:**
- "Create a presentation about X"
- "Find my email with Y"
- "What's the difference between A and B?"

## Common Workflows

### Workflow 1: Board Packet
```
Request -> 360-board-packet-generator agent ->
Asana pull -> QuickBooks data -> Gmail context ->
Synthesis -> docx creation -> design-director -> Final packet
```

**When to use:** Quarterly board meetings, comprehensive status reports

### Workflow 2: Client Assessment
```
Request -> Drive search (client docs) ->
Process flow analysis -> Business validation framework ->
Financial modeling -> Synthesis -> design-director -> Assessment package
```

**When to use:** New client evaluation, project validation, partnership due diligence

### Workflow 3: Meeting Intelligence
```
Request -> meeting-transcript-processor ->
Action items extraction -> smart-email-composer (follow-ups) ->
Asana task creation -> Meeting summary
```

**When to use:** Post-meeting processing, action item tracking, stakeholder communication

### Workflow 4: Weekly Status
```
Request -> Asana workspace query ->
Multi-project task pull -> Cross-project synthesis ->
weekly-tracker-generator -> Formatted status update
```

**When to use:** Weekly team updates, portfolio status, executive summaries

### Workflow 5: Research Report
```
Request -> web_search (external) -> google_drive_search (internal) ->
Analysis -> Synthesis -> docx creation -> design-director -> Final report
```

**When to use:** Market research, ecosystem mapping, landscape analysis

## Skill Routing Map

### Document Creation
- **docx** -> Word documents, reports, briefs
- **pptx** -> Presentations, pitch decks, slide decks
- **xlsx** -> Spreadsheets, financial models, data tables
- **pdf** -> Forms, fillable documents, standardized templates

### Design & Quality
- **design-director** -> Elevate any visual output (use before finalizing)
- **theme-factory** -> Apply brand themes (360, client brands)

### Intelligence & Analysis
- **executive-intelligence-dashboard** -> Weekly intelligence synthesis
- **meeting-transcript-processor** -> Meeting notes, action items, follow-ups
- **process-flow-generator** -> Operational workflow documentation

### Communication
- **smart-email-composer** -> Context-aware email drafting
- **meeting-prep-generator** -> Pre-meeting briefs with relationship history

### Data & Systems
- **Asana suite** -> Project management, task tracking, portfolio operations
- **Gmail tools** -> Email search, thread reading, message analysis
- **Drive tools** -> Document search, file retrieval, content access

## GitHub Agents

**Location:** `github.com/therealchandlerbing/claude-usecases`

### Agent: 360-board-packet-generator

**Purpose:** Comprehensive board meeting preparation

**Required fields:**
- meeting_date (ISO 8601)
- asana_project_ids (Client Delivery Hub)
- quickbooks_access (boolean)
- date_range (lookback period)

**Returns:** Multi-section board packet (financial, client health, strategic initiatives)

### Agent: process-flow-generator

**Purpose:** Extract and document operational workflows

**Required fields:**
- workflow_type (partnership, client, assessment, ecosystem, internal)
- data_sources (Asana, Drive, Gmail)
- output_format (mermaid, html, documentation)

**Returns:** Visual process flows, delegation-ready documentation

### Agent: executive-intelligence-dashboard

**Purpose:** Weekly intelligence brief synthesis

**Required fields:**
- date_range (week start/end)
- data_sources (Asana, Gmail, Drive)
- format (html, pdf)

**Returns:** Executive-grade intelligence dashboard

### Agent: weekly-tracker-generator

**Purpose:** Status summaries from Asana projects

**Required fields:**
- asana_project_ids (list)
- date_range (week)

**Returns:** Formatted weekly status update

### Agent: meeting-prep-generator

**Purpose:** Pre-meeting briefs with context

**Required fields:**
- attendees (list)
- meeting_topic (string)
- data_sources (Gmail, Drive for history)

**Returns:** Meeting brief with relationship history, pending items, talking points

## Payload Validation Checklist

Before calling ANY agent:

- [ ] All required fields present?
- [ ] Field types correct (string, int, date)?
- [ ] Date format is ISO 8601 (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSZ)?
- [ ] IDs are valid and accessible?
- [ ] Context sufficient for agent execution?

**If validation fails:** Orchestrator will ask ONE clarifying question to gather missing info.

## Error Quick Reference

### Error Types

**skill_execution** -> Skill failed during workflow
- Check: Which step failed, what was input, is skill available?
- Fix: Retry step, validate input, check skill status

**agent_call** -> Agent call failed
- Check: Payload format, required fields, agent availability
- Fix: Validate payload, provide missing data, verify agent

**routing** -> No matching capability
- Check: Is request clear, do capabilities exist?
- Fix: Clarify request, flag for new skill creation

### Recovery Actions

**Skill fails mid-workflow:**
-> Orchestrator captures completed work, offers retry or continue

**Agent payload incomplete:**
-> Orchestrator asks for missing data, then retries call

**No matching capability:**
-> Orchestrator flags for skill creation, suggests workaround

## Output Formats

### Success Output
```json
{
  "status": "complete",
  "workflow_executed": [steps],
  "final_result": {ready for use},
  "artifacts_created": [file paths],
  "next_actions": [if relevant]
}
```

### Clarification Output
```json
{
  "status": "clarification_needed",
  "question": "specific question",
  "context": "why this matters",
  "options": [if applicable]
}
```

### Error Output
```json
{
  "status": "error",
  "error_type": "type",
  "failed_at": "component",
  "error_message": "what happened",
  "suggested_recovery": "what to try"
}
```

## Communication Checklist

Orchestrator always:

- No em dashes (use commas, periods, parentheses)
- Bullets for lists and options
- Prose for analysis and strategy
- Announces what it's orchestrating
- Grounded + visionary tone
- Action-ready outputs

Orchestrator never:

- Uses em dashes
- Over-orchestrates simple requests
- Asks multiple clarifying questions
- Loses context between steps
- Returns invalid JSON
- Hides errors

## Integration with using-superpowers

**using-superpowers layer:**
- Mandatory skill usage protocol
- Check if skill exists, use it
- Follow it exactly

**skill-orchestrator layer:**
- Routing decisions (which skill)
- Coordination (multiple skills)
- Workflow management (complex operations)

**They work together, not against each other.**

## Quick Troubleshooting

### "Wrong skill was used"
-> Request might be ambiguous, provide more context

### "Workflow lost context"
-> Report specific step, orchestrator should maintain context

### "Agent call failed"
-> Check payload validation, provide missing fields

### "Got invalid JSON"
-> Report specific error, check which step produced it

### "Over-orchestrated simple request"
-> Be more specific about single-skill intent

## Update Triggers

**Update orchestrator when:**
- New agent added to repository -> Update agent list
- New workflow pattern emerges -> Document it
- Routing logic needs refinement -> Update decision tree
- Error pattern identified -> Enhance error handling

**Where to update:**
- Agent list -> SKILL.md "GitHub Agents Available"
- Workflow patterns -> SKILL.md "Special Workflow Patterns"
- Routing logic -> SKILL.md "Routing Decision Tree"
- Examples -> README.md "Real-World Examples"

## Key Patterns to Remember

**Generate and Refine**
Content creation -> Design elevation -> Theme application -> Review -> Finalize

**Gather and Synthesize**
Multi-source gathering -> Cross-reference -> Analysis -> Synthesis -> Format

**Plan and Execute**
Strategic planning -> Approval -> Break down -> Execute -> Validate

**Research to Report**
Research -> Analysis -> Synthesis -> Document creation -> Design -> Final

## Success Indicators

**Orchestrator working well:**
- Complex requests mapped clearly
- Multi-step processes complete without context loss
- Agent calls succeed
- Errors surface with recovery paths
- Time saved through intelligent automation

**Orchestrator needs tuning:**
- Simple requests over-orchestrated
- Frequent routing errors
- Context loss between steps
- Agent payload validation failures
- Unclear error messages

## Most Common Operations

**1. Board packet generation**
Frequency: Monthly
Pattern: agent call -> multi-source data -> synthesis -> document

**2. Client assessment**
Frequency: Per new client
Pattern: research -> framework application -> synthesis -> package

**3. Meeting processing**
Frequency: Weekly
Pattern: transcript -> action items -> follow-ups -> tasks

**4. Weekly status**
Frequency: Weekly
Pattern: Asana pull -> synthesis -> formatted update

**5. Partnership development**
Frequency: Quarterly
Pattern: research -> strategy -> modeling -> documentation

## Remember

**Orchestrator is for:**
Complexity coordination, multi-step workflows, agent management

**Orchestrator is not for:**
Simple requests, single skills, basic questions

**When in doubt:**
Let orchestrator map it, provide feedback, trust the routing

**Core value:**
Saves time by automating coordination so you focus on decisions
