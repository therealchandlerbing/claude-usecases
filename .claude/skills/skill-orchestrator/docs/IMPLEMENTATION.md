# Skill Orchestrator Implementation Guide

**How to integrate, test, and maintain the orchestrator in your workflow.**

## Installation

### Step 1: Add to Skills Directory

The skill-orchestrator is already located in your skills directory:
```
.claude/skills/skill-orchestrator/
```

### Step 2: Verify Integration with using-superpowers

The orchestrator works alongside your existing `using-superpowers` skill:

**using-superpowers (existing):**
- Mandatory skill usage protocol
- Checklist for every task
- TodoWrite requirement for checklists

**skill-orchestrator (new):**
- Adds routing intelligence layer
- Coordinates multi-skill workflows
- Manages GitHub agent calls

**Integration point:**
```
User request
    |
using-superpowers: "Does a skill exist for this?"
    |
If complex/multi-skill -> Route to skill-orchestrator
If single skill -> Route to that skill directly
If no skill -> Flag for creation
```

### Step 3: Update Your Prompt Context

Add this to your system context or project instructions:

```markdown
When requests are complex or involve multiple capabilities:
1. First check: Does skill-orchestrator apply?
2. If yes: Use orchestrator to map workflow
3. Orchestrator will coordinate individual skills/agents
4. Follow orchestrator's execution plan
```

### Step 4: Configure GitHub Repository Access

Ensure access to your agents repository:

```
Repository: github.com/therealchandlerbing/claude-usecases
Access: Read permissions for agent discovery
Integration: via call_agent function
```

## Testing Strategy

### Test Suite 1: Simple Routing (Should Skip Orchestrator)

**Test cases:**

1. **Single skill request**
   - Input: "Create a presentation about innovation ecosystems"
   - Expected: Route directly to pptx skill, no orchestration
   - Validates: Orchestrator doesn't over-trigger

2. **Basic question**
   - Input: "What's the difference between a joint venture and a partnership?"
   - Expected: Answer directly, no tools needed
   - Validates: Orchestrator doesn't trigger for non-tool requests

3. **Simple information retrieval**
   - Input: "Find my email with the BIMO team"
   - Expected: Gmail search directly, no orchestration
   - Validates: Single-tool operations bypass orchestrator

### Test Suite 2: Multi-Skill Workflows (Should Use Orchestrator)

**Test cases:**

1. **Document creation pipeline**
   - Input: "Create a professional presentation about our Brazil operations with 360 branding"
   - Expected workflow: pptx -> design-director -> theme-factory
   - Validates: Sequential skill coordination

2. **Research to report**
   - Input: "Research innovation funding in Sao Paulo and create a landscape report"
   - Expected workflow: web_search -> Drive search -> synthesis -> docx -> design-director
   - Validates: Multi-source data gathering and document creation

3. **Meeting intelligence**
   - Input: "Process this meeting transcript, create follow-up emails, and add tasks to Asana"
   - Expected workflow: transcript processing -> email composition -> task creation
   - Validates: Cross-system integration

### Test Suite 3: Agent Coordination (Should Use Orchestrator)

**Test cases:**

1. **Complete payload**
   - Input: "Generate board packet for Nov 20 meeting using Client Delivery Hub"
   - Expected: Validate payload, call 360-board-packet-generator, succeed
   - Validates: Agent call with complete data

2. **Incomplete payload**
   - Input: "Generate the executive intelligence dashboard"
   - Expected: Identify missing fields (date range, data sources), clarify once, proceed
   - Validates: Payload validation and one-shot clarification

3. **Agent error handling**
   - Input: [Simulated agent call failure]
   - Expected: Capture error, explain failure, suggest recovery
   - Validates: Graceful error handling

### Test Suite 4: Complex Workflows (Should Use Orchestrator)

**Test cases:**

1. **Client assessment**
   - Input: "Create comprehensive assessment for [client] including process flows, business validation, and financial model"
   - Expected: Multi-step workflow across Drive, agents, analysis, document creation
   - Validates: Complex coordination with context preservation

2. **Partnership development**
   - Input: "Develop partnership structure for [partnership] with financial model and agreement draft"
   - Expected: Research -> strategy -> modeling -> documentation -> design
   - Validates: Strategic workflow with multiple output types

### Test Suite 5: Error Handling (Should Handle Gracefully)

**Test cases:**

1. **Skill failure mid-workflow**
   - Scenario: Step 3 of 5 fails
   - Expected: Preserve steps 1-2, explain failure, offer recovery (retry step 3, continue, or restart)
   - Validates: Error recovery without data loss

2. **No matching capability**
   - Input: "Generate 3D architectural rendering of innovation space"
   - Expected: Flag no matching skill/agent, suggest manual alternative or new skill creation
   - Validates: Graceful handling of capability gaps

3. **Invalid input data**
   - Scenario: Asana project ID doesn't exist
   - Expected: Validate IDs before execution, catch error, explain problem
   - Validates: Input validation prevents downstream failures

## Running Tests

### Manual Testing Protocol

For each test case:

1. **Submit test input** exactly as written
2. **Observe routing decision:**
   - Did orchestrator trigger appropriately?
   - Was routing decision correct?
3. **Track execution:**
   - Did workflow steps execute in correct order?
   - Was context preserved between steps?
4. **Validate output:**
   - Is output format correct?
   - Are all required elements present?
   - Does output match expected result?
5. **Document results:**
   - Test passed/failed
   - Any unexpected behavior
   - Performance notes (execution time)

### Automated Testing (Future)

Consider implementing automated test suite:

```python
# Pseudo-code for automated testing
test_cases = [
    {
        "name": "simple_document_creation",
        "input": "Create a presentation about X",
        "expected_orchestrator": False,
        "expected_skill": "pptx",
        "validation": check_single_artifact_created
    },
    {
        "name": "board_packet_generation",
        "input": "Generate board packet for Nov 20",
        "expected_orchestrator": True,
        "expected_workflow": ["asana", "agent_call", "docx", "design"],
        "validation": check_comprehensive_output
    }
]

run_test_suite(test_cases)
```

## Maintenance

### Weekly Checks

**Monday morning routine:**
1. Review last week's orchestrated workflows
2. Check for any error patterns
3. Verify agent availability in repository
4. Update agent list if new agents added

### Monthly Audits

**First of month:**
1. **Usage analysis:**
   - Which workflows are most common?
   - Where is orchestrator adding most value?
   - Are there new patterns emerging?

2. **Performance review:**
   - Average execution times
   - Error rates by workflow type
   - Success rates for agent calls

3. **Documentation updates:**
   - Add new common workflows to EXAMPLES.md
   - Update QUICK-START.md with new patterns
   - Refine routing logic in SKILL.md if needed

### Quarterly Reviews

**Every quarter:**
1. **Strategic assessment:**
   - Is orchestrator handling new work types?
   - Do routing rules need refinement?
   - Should new agents be developed?

2. **Capability mapping:**
   - Review all available skills and agents
   - Identify gaps in capabilities
   - Plan new skill/agent development

3. **Integration optimization:**
   - How well does orchestrator integrate with GitHub repository?
   - Are there friction points to address?
   - Can workflow patterns be automated further?

### Continuous Improvement

**When to update orchestrator:**

**Add new agent to repository:**
1. Update "GitHub Agents Available" section in SKILL.md
2. Add to agent list in QUICK-START.md
3. Create example workflow in EXAMPLES.md if complex
4. Test integration with orchestrator

**Discover new workflow pattern:**
1. Document pattern in "Special Workflow Patterns" in SKILL.md
2. Add to common workflows in QUICK-START.md
3. Create detailed example in EXAMPLES.md
4. Test pattern execution

**Routing logic needs refinement:**
1. Identify specific cases where routing was incorrect
2. Update decision tree in SKILL.md
3. Add clarifying examples
4. Test with problematic cases
5. Document changes in version notes

**Error handling gaps:**
1. Document error scenario
2. Add error type to SKILL.md if new
3. Implement recovery strategy
4. Update error handling section in README.md
5. Test recovery paths

## Performance Optimization

### Current Performance Benchmarks

Based on examples:
- Simple routing decision: <1 second
- Multi-skill workflow (3-5 steps): 30-90 seconds
- Complex workflow (5-7 steps): 2-4 minutes
- Agent payload validation: <2 seconds

### Optimization Opportunities

**Parallel execution:**
- When steps don't have dependencies, consider parallel execution
- Example: Fetching from Drive and Asana simultaneously
- Requires careful context management

**Caching:**
- Cache frequently accessed data (workspace IDs, project lists)
- Reduce redundant API calls
- Implement cache invalidation strategy

**Smart defaults:**
- Learn from user patterns (e.g., usually wants "all" data sources)
- Reduce clarification frequency
- Make assumptions explicit when using defaults

**Workflow templates:**
- Pre-configure common workflows
- Reduce mapping time for repeated operations
- Example: "Standard board packet" vs. customized requests

## Troubleshooting Guide

### Issue: Orchestrator triggers when it shouldn't

**Symptoms:**
- Simple single-skill requests getting orchestrated
- Unnecessary workflow mapping
- Extra execution time

**Diagnosis:**
- Review request phrasing
- Check if request implied complexity
- Examine orchestrator decision tree

**Fix:**
- Be more explicit in requests ("Just create a document...")
- Update routing logic to better detect simple cases
- Add anti-patterns to SKILL.md

### Issue: Context lost between workflow steps

**Symptoms:**
- Later steps missing information from earlier steps
- Data doesn't flow correctly
- Final output incomplete

**Diagnosis:**
- Review execution logs
- Check which step lost context
- Examine how data is passed between steps

**Fix:**
- Strengthen context capture in orchestrator
- Add explicit context validation between steps
- Improve data structure for passing outputs

### Issue: Agent payload validation failing repeatedly

**Symptoms:**
- Same missing fields each time
- Clarification questions becoming repetitive
- Agent calls not succeeding

**Diagnosis:**
- Review agent payload requirements
- Check if requirements changed
- Verify data source accessibility

**Fix:**
- Update agent payload templates in orchestrator
- Improve default value handling
- Document changed requirements

### Issue: Workflow fails mid-execution

**Symptoms:**
- Some steps succeed, then failure
- Error messages unclear
- No recovery path offered

**Diagnosis:**
- Identify exact failure point
- Check error type
- Review input data for failed step

**Fix:**
- Improve error handling at that step
- Add validation before step execution
- Enhance recovery path suggestions

## Integration Patterns

### Pattern 1: Orchestrator as Primary Router

**When to use:**
- Most requests are complex multi-step operations
- Heavy agent usage
- Frequent cross-system workflows

**Configuration:**
- Set orchestrator as first check after using-superpowers
- Route everything through orchestrator decision tree
- Let orchestrator handle simple passthrough

**Pros:**
- Consistent workflow management
- Comprehensive logging
- Easier to maintain single routing point

**Cons:**
- Slight overhead for simple requests
- More complex for pure question-answer

### Pattern 2: Orchestrator as Complexity Handler

**When to use:**
- Mix of simple and complex requests
- Want minimal overhead for basic operations
- Clear distinction between simple and complex

**Configuration:**
- Direct route simple single-skill requests
- Invoke orchestrator only for explicit complexity
- Use trigger phrases to activate

**Pros:**
- No overhead for simple operations
- Orchestrator reserves capacity for complexity
- More efficient overall

**Cons:**
- Need clear routing rules
- Risk of missing orchestration opportunities

### Pattern 3: Hybrid Approach (Recommended)

**When to use:**
- Default for most use cases
- Balance efficiency and capability
- Learn routing over time

**Configuration:**
- Fast path for obviously simple requests
- Orchestrator for ambiguous or complex requests
- Feedback loop to improve routing

**Pros:**
- Best of both worlds
- Adapts over time
- Maintains performance

**Cons:**
- Requires tuning
- More complex initial setup

**Implementation:**
```
Request received
    |
Quick classification:
    - Single clear skill needed? -> Route directly
    - Multiple skills/agents? -> Orchestrator
    - Ambiguous? -> Orchestrator decides
    - Question only? -> Answer directly
```

## Metrics to Track

### Orchestrator Effectiveness

**Usage metrics:**
- Orchestration trigger rate (% of requests)
- Average steps per orchestrated workflow
- Most common workflow patterns

**Performance metrics:**
- Average execution time by workflow type
- Success rate (workflows completing without error)
- Clarification rate (% requiring user input)

**Quality metrics:**
- User satisfaction with orchestrated outputs
- Rework required after orchestration
- Context preservation accuracy

**Error metrics:**
- Error rate by step type
- Recovery success rate
- Most common error types

### Analysis Framework

**Monthly metrics review:**
```markdown
## Orchestrator Performance (Month of [Month])

**Usage:**
- Total requests: X
- Orchestrated: Y (Z%)
- Avg steps per workflow: N

**Performance:**
- Avg execution time: Xs
- Success rate: Y%
- Clarification rate: Z%

**Top Workflows:**
1. [Workflow type]: X occurrences
2. [Workflow type]: Y occurrences
3. [Workflow type]: Z occurrences

**Errors:**
- Total errors: X
- By type: [distribution]
- Recovery rate: Y%

**Improvements Needed:**
- [Specific area 1]
- [Specific area 2]
```

## Future Enhancements

### Phase 1: Intelligence (Next 1-2 months)

**Learning from patterns:**
- Track successful workflows
- Build workflow library
- Suggest workflows proactively

**Predictive routing:**
- Based on request pattern
- Time of day/week context
- Current project context

### Phase 2: Automation (Next 3-4 months)

**Auto-recovery:**
- Common error automatic fixes
- Retry logic with variations
- Fallback strategies

**Workflow optimization:**
- Parallel execution where possible
- Smart caching
- Resource pre-loading

### Phase 3: Advanced Coordination (Next 6+ months)

**Multi-agent choreography:**
- Parallel agent execution
- Agent-to-agent communication
- Complex dependency management

**Workflow versioning:**
- Track workflow versions
- A/B test workflow variations
- Optimize based on performance

**Adaptive learning:**
- Adjust routing based on outcomes
- Learn user preferences
- Personalize workflows

## Version History

### v1.0.0 (Current)

**Features:**
- Basic routing intelligence
- Multi-skill coordination
- Agent payload validation
- Error handling with recovery
- Context preservation
- One-shot clarifications

**Known limitations:**
- Sequential execution only
- Manual workflow patterns
- No learning capability
- Limited error prediction

### v1.1 (Planned)

**Enhancements:**
- Workflow pattern library
- Improved error prediction
- Performance optimizations
- Enhanced logging

### v2.0 (Future)

**Major features:**
- Parallel execution
- Adaptive learning
- Auto-recovery
- Workflow optimization

## Support

### Getting Help

**For orchestrator issues:**
1. Check QUICK-START.md for quick answers
2. Review EXAMPLES.md for similar scenarios
3. Examine SKILL.md for detailed logic
4. Review this IMPLEMENTATION.md for integration issues

**For GitHub repository issues:**
1. Verify repository access
2. Check agent availability
3. Review agent payload requirements
4. Test call_agent function directly

**For skill integration issues:**
1. Verify using-superpowers is active
2. Check skill availability in context
3. Test individual skills directly
4. Review integration patterns above

### Reporting Issues

**When reporting issues, include:**
1. **Request that triggered issue:** Exact phrasing
2. **Expected behavior:** What should have happened
3. **Actual behavior:** What actually happened
4. **Context:** Relevant projects, dates, systems involved
5. **Error messages:** If any
6. **Workflow state:** What steps completed before failure

**Example issue report:**
```markdown
## Issue: Context lost between steps

**Request:** "Create client assessment for BIMO project"

**Expected:**
- Drive search -> Process flows -> Analysis -> Document
- All steps preserve BIMO context

**Actual:**
- Drive search succeeded (found BIMO docs)
- Process flows step lost BIMO context, asked which client
- Had to manually re-specify

**Context:**
- BIMO project in Drive
- Multiple BIMO-related documents
- Request was clear about client

**Workaround:**
- Broke into two requests: Drive search first, then assessment with explicit doc references
```

## Success Criteria

**Orchestrator is successful when:**

- Complex workflows execute reliably (>90% success rate)
- Context preserved across all steps
- Clarifications are minimal and one-shot
- Error handling provides clear recovery paths
- Time savings are measurable and significant
- Output quality is consistently high
- Integration is seamless with existing tools

**Orchestrator needs improvement when:**

- Frequent routing errors
- Context loss between steps
- Multiple clarification rounds needed
- Unclear error messages
- Workflows fail without recovery
- Overhead exceeds value for simple tasks

## Conclusion

The skill-orchestrator is designed to be:
- **Intelligent:** Routes based on complexity and context
- **Reliable:** Maintains context and handles errors gracefully
- **Efficient:** Minimizes overhead and maximizes value
- **Maintainable:** Clear structure, good documentation, testable
- **Extensible:** Easy to add workflows, agents, and capabilities

With proper implementation, testing, and maintenance, the orchestrator becomes your operations control center, coordinating complexity so you can focus on strategy and decisions.

Start with the testing suite, monitor performance metrics, gather feedback, and continuously refine. The orchestrator will learn and improve with use.
