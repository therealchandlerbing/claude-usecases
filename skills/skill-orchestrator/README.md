# Skill Orchestrator

**Universal workflow coordinator for complex multi-skill and multi-agent operations.**

## Purpose

The skill-orchestrator sits between you and your capabilities (Claude skills + GitHub agents), intelligently routing requests and coordinating complex workflows that require multiple specialized tools working in sequence.

Think of it as your operations control center. When a request comes in that needs more than one capability, the orchestrator maps the workflow, executes each step in order, maintains context between steps, and delivers integrated results.

## When to Use

**Always use skill-orchestrator for:**

✅ **Multi-step workflows**
- "Generate board packet" (requires Asana pull, Drive fetch, synthesis, doc creation)
- "Create client assessment" (needs multiple frameworks, data gathering, analysis)
- "Process meeting and send follow-ups" (transcript processing, email drafting, task creation)

✅ **GitHub agent coordination**
- Calling specialized agents from your repository
- Validating payloads before agent calls
- Handling agent responses and errors

✅ **Unclear routing**
- Request could go several directions
- Multiple skills seem relevant
- Need to determine best path

✅ **Cross-domain operations**
- Pulling from Asana + Gmail + Drive
- Research + analysis + document creation
- Strategy + implementation workflows

**Skip orchestrator for:**

❌ Simple single-skill requests ("Create a presentation about X")
❌ Direct questions with no tool usage ("What's the difference between Y and Z?")
❌ Basic information retrieval ("Find my email with John")

## How It Works

### The Orchestration Cycle

```
1. REQUEST RECEIVED
   ↓
2. ANALYZE COMPLEXITY
   ↓
3. MAP WORKFLOW (if needed)
   ↓
4. VALIDATE REQUIREMENTS
   ↓
5. EXECUTE SEQUENCE
   ↓
6. AGGREGATE OUTPUTS
   ↓
7. DELIVER RESULT
```

### Example: Board Packet Generation

**Request:** "Generate my board packet for next week's meeting"

**Orchestrator process:**

1. **Analyzes request** → Complex, needs multiple agents/skills
2. **Maps workflow:**
   - Call 360-board-packet-generator agent
   - Pull from Asana (Client Delivery Hub)
   - Pull from QuickBooks (financial data)
   - Pull from Gmail (recent communications)
   - Synthesize into report sections
   - Create professional document with design-director
   - Apply 360 branding
3. **Validates** → Has necessary Asana project IDs? QuickBooks access? Date range?
4. **Executes sequence** → Runs each step, maintains context
5. **Aggregates** → Combines all outputs
6. **Delivers** → Professional board packet document ready for review

## Integration with Your Ecosystem

### Claude Skills (Available in Context)

The orchestrator routes to these skills when needed:

**Document Creation:**
- docx (Word documents)
- pptx (Presentations)
- xlsx (Spreadsheets)
- pdf (Forms and PDFs)

**Design & Styling:**
- design-director (elevate visual quality)
- theme-factory (apply consistent branding)

**Intelligence & Analysis:**
- executive-intelligence-dashboard
- meeting-transcript-processor
- process-flow-generator

**Communication:**
- smart-email-composer
- meeting-prep-generator

**Asana Operations:**
- Full suite of Asana tools (search, create, update, etc)

### GitHub Agents (External Repository)

The orchestrator coordinates with specialized agents in:
`github.com/therealchandlerbing/claude-usecases`

**Key Agents:**
- **360-board-packet-generator** (comprehensive board meeting preparation)
- **process-flow-generator** (operational workflow documentation)
- **executive-intelligence-dashboard** (weekly intelligence synthesis)
- **weekly-tracker-generator** (status summaries from Asana)
- **meeting-prep-generator** (pre-meeting briefs)

The orchestrator handles payload validation and agent calls so you don't have to worry about data structure.

## Workflow Patterns

### Pattern 1: Generate and Refine

**Use case:** Creating polished deliverables

```
User request → Content generation skill → design-director →
theme-factory (if needed) → Review → Refinement → Finalize
```

**Example:**
"Create a pitch deck for the Brazil partnership"

1. pptx skill (generate structure and content)
2. design-director (elevate design quality)
3. theme-factory (apply 360 branding)
4. Your review and feedback
5. Refinement iterations
6. Final artifact

### Pattern 2: Gather and Synthesize

**Use case:** Building intelligence from multiple sources

```
Multi-source data gathering → Cross-reference →
Analysis → Synthesis → Formatted output
```

**Example:**
"Give me an intelligence brief on our Brazil operations"

1. google_drive_search (internal documents)
2. Gmail search (recent communications)
3. Asana query (project status)
4. web_search (external context)
5. Cross-reference and identify patterns
6. Synthesize insights
7. executive-intelligence-dashboard formatting

### Pattern 3: Plan and Execute

**Use case:** Strategic work that needs both thinking and doing

```
Strategic planning → Approval → Break down →
Sequential execution → Validation
```

**Example:**
"Plan and implement our Q1 partnership outreach"

1. Brainstorming skill (strategy options)
2. Your approval of direction
3. Break strategy into actionable steps
4. Execute: email drafts, Asana projects, tracking systems
5. Validate completeness
6. Deliver execution-ready plan

### Pattern 4: Research to Report

**Use case:** Information gathering that becomes a deliverable

```
Research → Analysis → Synthesis → Document creation →
Design enhancement → Final report
```

**Example:**
"Research innovation ecosystem in São Paulo and create a landscape report"

1. web_search (current ecosystem)
2. google_drive_search (our existing research)
3. Analysis of findings
4. Synthesis of insights
5. docx skill (create report structure)
6. design-director (elevate quality)
7. Final landscape report

## Configuration & Customization

### Adding New Agents

When you add agents to your GitHub repository:

1. Document the agent in the "GitHub Agents Available" section of SKILL.md
2. Specify required payload fields
3. Note any special considerations
4. Update the REFERENCE.md quick lookup

### Adding New Workflow Patterns

When new patterns emerge from your work:

1. Document the pattern in "Special Workflow Patterns" section
2. Provide concrete example
3. Note when to use vs. other patterns
4. Add to REFERENCE.md

### Tuning Routing Logic

If routing decisions need refinement:

1. Update the decision tree in SKILL.md
2. Add clarifying examples
3. Document edge cases
4. Test with representative requests

## Error Handling

### Common Errors and Recovery

**Agent payload incomplete:**
```
Orchestrator clarifies → You provide missing data →
Payload validated → Agent called → Results returned
```

**Skill fails mid-workflow:**
```
Capture completed work → Explain failure point →
Offer: retry, continue from failure, or restart
```

**Agent unavailable:**
```
Check for equivalent skill → Suggest manual alternative →
Flag for repository update
```

**No matching capability:**
```
Document the request → Flag for new skill creation →
Suggest workaround if possible
```

### Error Output Format

All errors return structured JSON:

```json
{
  "status": "error",
  "error_type": "skill_execution|agent_call|routing",
  "failed_at": "specific component",
  "error_message": "what happened",
  "completed_steps": ["successful steps"],
  "partial_output": "any usable output",
  "suggested_recovery": "what to try next"
}
```

## Quality Standards

### The Orchestrator Always:

✅ Validates all inputs before execution
✅ Announces what it's orchestrating
✅ Maintains context between steps
✅ Returns valid JSON for structured outputs
✅ Surfaces errors with recovery paths
✅ Follows your communication preferences (no em dashes!)
✅ Respects your time with efficient routing

### The Orchestrator Never:

❌ Over-orchestrates simple requests
❌ Loses context between workflow steps
❌ Asks multiple clarifying questions in sequence
❌ Guesses at critical payload data
❌ Hides errors or fails silently
❌ Returns invalid JSON
❌ Uses em dashes (seriously, never)

## Best Practices

### For You (Using the Orchestrator)

**Be clear about desired outcome:**
- Good: "Generate a board packet with financial dashboard, client health, and strategic initiatives"
- Better: "Generate board packet for Nov 20 meeting using Asana Client Delivery Hub data"

**Provide context when needed:**
- If request involves specific projects, provide Asana project names/IDs
- If timeline matters, specify date ranges
- If stakeholders matter, mention who's involved

**Trust the workflow:**
- Let orchestrator map complex workflows before executing
- Review workflow maps for high-stakes operations
- Provide feedback on routing decisions

### For Maintenance

**Regular updates:**
- Review and update agent list quarterly
- Document new workflow patterns as they emerge
- Refine routing logic based on usage
- Keep examples current with actual work

**Quality checks:**
- Test orchestrator with representative requests
- Verify agent payload formats match current specs
- Ensure error handling covers common failures
- Validate JSON outputs

## Integration with using-superpowers

The orchestrator works in harmony with your using-superpowers skill:

**using-superpowers establishes:**
- Must check for relevant skills before any task
- Must use skills if they exist
- Must create TodoWrite todos for checklists
- Must announce skill usage

**skill-orchestrator extends:**
- Routes to correct skill(s)
- Coordinates multiple skills
- Manages complex workflows
- Interfaces with GitHub agents

They're complementary, not competing. Think of it as:
1. **using-superpowers** = mandatory protocol
2. **skill-orchestrator** = intelligent routing layer
3. **individual skills** = specialized execution

## Troubleshooting

### "Orchestrator didn't route correctly"

**Check:**
- Was request ambiguous? May need clarification
- Is routing logic in SKILL.md current?
- Are all relevant skills in context?
- Could request be interpreted multiple ways?

**Fix:**
- Provide more specific request
- Update routing decision tree
- Verify skill availability
- Add clarifying example to REFERENCE.md

### "Workflow failed mid-execution"

**Check:**
- What step failed? (orchestrator should tell you)
- Was input data correct?
- Is skill/agent currently available?
- Did context get lost between steps?

**Fix:**
- Review error output for specific failure
- Validate input data
- Check skill/agent status
- Retry from failure point if possible

### "Agent payload validation failed"

**Check:**
- Are all required fields present?
- Are field types correct?
- Do IDs actually exist in systems?
- Is date format correct (ISO 8601)?

**Fix:**
- Review agent payload requirements
- Provide missing data
- Verify ID accessibility
- Correct date formats

### "Got invalid JSON output"

**Check:**
- Which step produced invalid JSON?
- Is skill outputting properly?
- Did orchestrator aggregate correctly?

**Fix:**
- Report specific JSON error
- Check problematic skill
- Update aggregation logic if needed

## Real-World Examples

### Example 1: Client Assessment Package

**Request:** "Create comprehensive assessment package for BIMO project"

**Orchestrated workflow:**
1. google_drive_search ("BIMO project documents")
2. Process flow analysis (understand their operations)
3. Vianeo Business Validation framework application
4. Financial model development (if needed)
5. Synthesis into assessment report
6. design-director (elevate presentation)
7. Final package ready for client

**Orchestrator value:** Coordinated 5+ capabilities, maintained context about BIMO throughout, delivered integrated assessment vs. disconnected pieces.

### Example 2: Weekly Status Synthesis

**Request:** "Generate my weekly tracker for all active projects"

**Orchestrated workflow:**
1. asana_list_workspaces (get context)
2. asana_typeahead_search (find relevant projects)
3. asana_search_tasks (get this week's activities)
4. Cross-project synthesis
5. weekly-tracker-generator agent (format)
6. Output ready for stakeholders

**Orchestrator value:** Automated multi-project status compilation that would otherwise require manual assembly.

### Example 3: Partnership Development

**Request:** "Develop partnership structure for 360 Space Innovation Studios with SpacePlan"

**Orchestrated workflow:**
1. google_drive_search (existing partnership docs)
2. Brainstorming skill (structure options)
3. Your feedback on direction
4. Financial modeling (revenue shares, equity splits)
5. Legal framework considerations
6. docx creation (partnership agreement draft)
7. design-director (professional presentation)
8. Final partnership structure package

**Orchestrator value:** Coordinated strategic thinking + financial analysis + legal considerations + document creation in one cohesive workflow.

## Metrics & Success Indicators

**The orchestrator is working well when:**

✅ Complex requests get mapped into clear workflows
✅ Multi-step processes complete without losing context
✅ Agent calls succeed with proper payload validation
✅ Errors surface clearly with actionable recovery paths
✅ Your time is saved through intelligent automation
✅ Deliverables are integrated vs. fragmented

**The orchestrator needs tuning when:**

❌ Simple requests get over-orchestrated
❌ Routing decisions are frequently wrong
❌ Context gets lost between steps
❌ Agent calls frequently fail on payload validation
❌ Error messages are unclear
❌ You're doing manual coordination that should be automated

## Future Enhancements

**Planned improvements:**

- **Learning from patterns:** Track successful workflows to improve routing
- **Predictive routing:** Suggest orchestration before you ask
- **Dependency mapping:** Visualize complex workflow chains
- **Performance metrics:** Track execution times and success rates
- **Auto-recovery:** Attempt common error fixes before asking

**Contribute improvements:**
- Document new workflow patterns as you discover them
- Flag routing issues when they occur
- Suggest enhancements based on your usage
- Share successful configurations

## Support & Maintenance

**Questions about orchestrator behavior:**
- Review REFERENCE.md for quick answers
- Check workflow examples in this README
- Examine SKILL.md for detailed logic

**Updates needed:**
- New agent added: Update agent list in SKILL.md
- New pattern emerges: Document in Special Workflow Patterns
- Routing needs refinement: Update decision tree
- Error handling gaps: Enhance error protocols

**Issues to report:**
- Incorrect routing with specific example
- Context loss with reproducible case
- Error handling gaps
- Performance concerns

## Key Takeaways

**Remember:**
1. Orchestrator = routing + coordination, not execution
2. Works with using-superpowers, doesn't replace it
3. Valuable for complexity, invisible for simplicity
4. Maintains context, validates payloads, surfaces errors
5. Follows your communication style religiously (no em dashes!)
6. Designed to save time, not create overhead

**When in doubt:**
- Let orchestrator map complex workflows
- Trust the routing for multi-step operations
- Provide feedback on orchestration decisions
- Update patterns as your work evolves

The orchestrator is your operations control center. Use it to coordinate complexity so you can focus on decisions and strategy.
