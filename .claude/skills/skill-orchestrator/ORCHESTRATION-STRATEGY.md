# Skill Orchestrator Strategic Framework

This document provides the intelligence layer that enables exceptional orchestration across 360's skill ecosystem. Use this alongside the main SKILL.md for routing decisions, workflow coordination, and quality assurance.

---

## Natural Language Routing

Users describe what they need; the orchestrator routes intelligently. No skill name knowledge required.

### Intent Recognition Patterns

**Governance & Board Communications**
| User Says | Route To | Chain With |
|-----------|----------|------------|
| "Prepare for the board meeting" | 360-board-meeting-prep | executive-intelligence-dashboard → design-director |
| "Generate the impact brief" | 360-newsletter-generator | design-director |
| "Show me executive intelligence" | executive-intelligence-dashboard | design-director |
| "What's the weekly status?" | 360-newsletter-generator | - |

**Client & Partnership Development**
| User Says | Route To | Chain With |
|-----------|----------|------------|
| "Write a proposal for [client]" | 360-proposal-builder | sales-automator → strategic-persona-builder |
| "Build a portfolio page" | 360-client-portfolio-builder | strategic-persona-builder → design-director |
| "Review this contract" | contract-redlining-tool | - |
| "Score this prospect" | sales-automator | - |
| "Who is [contact/company]?" | sales-automator | - |

**Research & Analysis**
| User Says | Route To | Chain With |
|-----------|----------|------------|
| "Research [topic] deeply" | open-deep-research-team | - |
| "Build a persona for [stakeholder]" | strategic-persona-builder | - |
| "Extract intelligence from this" | intelligence-extractor | - |
| "Analyze this transcript" | intelligence-extractor | - |

**Strategic Advisory**
| User Says | Route To | Chain With |
|-----------|----------|------------|
| "Morning brief" / "What should I focus on?" | ceo-advisor | - |
| "Prepare me for [meeting]" | ceo-advisor | strategic-persona-builder |
| "Scenario analysis for [decision]" | ceo-advisor | - |
| "How's my time looking?" | ceo-advisor | - |

**Operational & Compliance**
| User Says | Route To | Chain With |
|-----------|----------|------------|
| "Track project status" | 360-executive-project-tracker | - |
| "Document this process" | workflow-process-generator | - |
| "What's wrong with [workflow]?" | workflow-debugging | - |
| "Is this AI ethical?" | ai-ethics-advisor | - |
| "FDA pathway for [product]" | fda-consultant-agent | - |

**Financial & Impact**
| User Says | Route To | Chain With |
|-----------|----------|------------|
| "Model the impact" | financial-modeling-skills | - |
| "Generate impact presentation" | executive-impact-presentation-generator | design-director |
| "SROI analysis" | financial-modeling-skills | - |

---

## Core Workflow Chains

### Chain 1: Deal-to-Close Pipeline
**Trigger**: "Help me close [prospect/client]"

```
Step 1: sales-automator
        - Prospect research
        - Company intelligence
        - Lead scoring (A-D grade, 100-point rubric)
        Output: Enriched prospect profile + engagement recommendations

Step 2: strategic-persona-builder
        - Decision-maker personas
        - Jobs-to-be-done analysis
        - Evidence-backed profiles
        Output: Stakeholder personas for proposal customization

Step 3: 360-proposal-builder
        - Service track selection
        - Investment breakdown
        - Cultural adaptation
        - GenIP attribution
        Output: Executive-grade proposal (DOCX/PDF)

Step 4: [After acceptance] contract-redlining-tool
        - Standard position comparison
        - Risk assessment
        - Negotiation guidance
        Output: Redlined contract + executive summary
```

### Chain 2: Board Governance Cycle
**Trigger**: "Prepare for board meeting on [date]"

```
Step 1: executive-intelligence-dashboard
        - Synthesize Asana/Gmail/Drive data
        - Partnership intelligence
        - Operations status
        - Strategy updates
        Output: Intelligence synthesis + timeline

Step 2: 360-board-meeting-prep
        - Structure board packet
        - Financial dashboards (QuickBooks)
        - Portfolio health analysis
        - Action item tracking
        Output: Complete packet structure

Step 3: design-director
        - Typography elevation
        - Color application
        - Layout refinement
        - Accessibility validation
        Output: Professional, board-ready deliverables

Final Outputs:
- DOCX board packet
- HTML Financial Intelligence Dashboard
- HTML Portfolio Health Dashboard
- HTML Strategic Progress Dashboard
- PDF exports (landscape + portrait)
```

### Chain 3: Client Venture Launch
**Trigger**: "Create materials for [venture name]"

```
Step 1: strategic-persona-builder
        - Understand stakeholder types
        - Map decision-makers
        - Identify pain points
        Output: Stakeholder profiles

Step 2: 360-client-portfolio-builder
        - Vianeo sprint data integration
        - Business model narrative
        - Traction metrics
        - Visual design (Stripe/Linear quality)
        Output: Single-page HTML portfolio

Step 3: 360-proposal-builder
        - Partnership positioning
        - Investment framework
        - Cultural adaptation
        Output: Partnership proposal

Step 4: design-director
        - Editorial sophistication
        - Hand-crafted appearance
        - Asymmetric layouts
        Output: Publication-quality materials
```

### Chain 4: Weekly Operational Rhythm
**Recurring Schedule**

```
Monday Morning:
    ceo-advisor → Morning brief (3-5 priorities)
                  Stakeholder health check
                  Time optimization recommendations

Tuesday-Thursday:
    360-executive-project-tracker → Blocker detection
                                    Status aggregation
                                    Escalation identification

Friday:
    360-newsletter-generator → Impact Brief production
                               Six-section dashboard
                               Timeline events
                               Action items

As-Needed:
    executive-intelligence-dashboard → Deeper analysis
                                       Ad-hoc intelligence requests
```

### Chain 5: Research-to-Deliverable
**Trigger**: "[Complex topic] needs analysis"

```
Step 1: open-deep-research-team
        - Nine-agent research system
        - Academic + technical + data perspectives
        - Quality assurance validation
        - Confidence scoring
        Output: Comprehensive research report

Step 2: strategic-persona-builder (if stakeholder-focused)
        - Convert research to personas
        - Evidence quality scoring
        - Framework application (Vianeo/JTBD/Empathy)
        Output: Stakeholder profiles

Step 3: Delivery skill selection:
        - executive-impact-presentation-generator (for impact reports)
        - 360-proposal-builder (for client proposals)
        - workflow-process-generator (for operational documentation)

Step 4: design-director
        - Final polish
        - Accessibility compliance
        - Export optimization
        Output: Publication-ready deliverable
```

---

## Proactive Activation Rules

### Always Auto-Activate

**design-director**
- Trigger: ANY skill produces visual output
- Visual outputs include: presentations, dashboards, HTML, reports, charts
- This is mandatory for 360's quality standard

**workflow-debugging**
- Trigger: ANY skill throws an error
- Captures error context, suggests recovery, notifies if needed

**skill-orchestrator**
- Trigger: Request matches 2+ skill capabilities
- Manages dependencies, coordinates execution, aggregates results

### Contextually Auto-Activate

**ai-ethics-advisor**
- Trigger: Request involves AI system development, deployment, or evaluation
- Proactive for bias assessment, fairness evaluation, regulatory compliance

**contract-redlining-tool**
- Trigger: Proposal acceptance signal or incoming contract
- After 360-proposal-builder closes deals

**intelligence-extractor**
- Trigger: Processing meeting transcripts or partnership emails
- Structured extraction for database population

### Recommend (Ask First)

**ceo-advisor**
- Recommend: Monday mornings for weekly planning
- Context: "Would you like your morning brief?"

**360-newsletter-generator**
- Recommend: Fridays for Impact Brief production
- Context: "Ready to generate this week's Impact Brief?"

**strategic-persona-builder**
- Recommend: Before significant client/partner engagements
- Context: "Want stakeholder profiles before this meeting?"

---

## Data Source Coordination

### Primary Data Hubs

| Data Source | Consuming Skills | Refresh Pattern | Data Types |
|-------------|------------------|-----------------|------------|
| **Asana** | 360-board-meeting-prep, executive-intelligence-dashboard, 360-executive-project-tracker, 360-newsletter-generator, sales-automator | Real-time | Projects, tasks, custom fields, status updates, portfolio items |
| **Gmail** | intelligence-extractor, executive-intelligence-dashboard, sales-automator, 360-executive-project-tracker, ceo-advisor | Real-time | Partnership comms, strategic emails, client engagement |
| **Google Drive** | open-deep-research-team, executive-intelligence-dashboard, 360-board-meeting-prep | On-demand | Strategic docs, board materials, proposals, research |
| **Google Calendar** | ceo-advisor, 360-executive-project-tracker | Real-time | Meetings, follow-ups, time allocation |
| **QuickBooks** | 360-board-meeting-prep, ceo-advisor, executive-impact-presentation-generator | Weekly | Revenue, expenses, AR aging, cash position |
| **Apollo.io** | sales-automator | On-demand | People enrichment, organization data |
| **Vianeo** | 360-client-portfolio-builder, strategic-persona-builder | On-demand | Sprint data, TRL, assessment scores |

### Cross-Skill Data Flow

```
intelligence-extractor outputs
    ├→ ceo-advisor (executive intelligence)
    ├→ sales-automator (prospect intelligence)
    └→ strategic-persona-builder (stakeholder context)

executive-intelligence-dashboard outputs
    └→ 360-board-meeting-prep (intelligence synthesis)

sales-automator prospect data
    └→ 360-proposal-builder (prospect context)

strategic-persona-builder profiles
    ├→ 360-proposal-builder (stakeholder understanding)
    └→ 360-client-portfolio-builder (audience context)

open-deep-research-team outputs
    ├→ strategic-persona-builder (research foundation)
    └→ 360-proposal-builder (evidence base)
```

---

## Quality Gates

### Gate 1: Pre-Execution (Data Completeness)

Before any skill executes, verify:

- [ ] Required data sources are accessible
- [ ] Authentication tokens are valid
- [ ] Minimum data thresholds met:
  - Gmail: At least 7 days of relevant communications
  - Asana: Portfolio/project exists and has tasks
  - QuickBooks: Current period data available
  - Calendar: Access to relevant date range
- [ ] Context from previous workflow steps is captured
- [ ] User preferences applied (no em dashes, format choices)

### Gate 2: Post-Execution (Output Validation)

After each skill completes, verify:

- [ ] JSON syntax is valid (use JSON.parse test)
- [ ] Required output fields are present
- [ ] No sensitive data exposure (credentials, API keys)
- [ ] Design elevation applied (if visual output)
- [ ] Accessibility compliance checked (WCAG 2.1 AA)
- [ ] File artifacts saved to correct locations

### Gate 3: Chain Continuity

Between workflow steps, verify:

- [ ] Previous output format matches next input requirements
- [ ] All dependencies are resolved
- [ ] No orphaned data or lost context
- [ ] Error states are cleared before proceeding
- [ ] Intermediate artifacts preserved for debugging

---

## Simplification Strategies

### One-Shot Intent Recognition

Parse intent fully, then confirm once with complete plan:

```markdown
**Workflow Plan**

You want to prepare for the board meeting next Tuesday. This will:

1. Pull intelligence from Asana, Gmail, and Google Drive
2. Generate board packet with financial dashboards
3. Apply design elevation to all outputs

**Outputs:**
- Board packet (DOCX)
- Financial dashboards (HTML)
- PDF exports

Proceed?
```

### Smart Defaults

Apply these unless user specifies otherwise:

| Parameter | Default |
|-----------|---------|
| Time period | Current week |
| Data sources | All available |
| Design elevation | Always apply |
| Contract positions | 360's standard terms |
| Output format | Dual (presentation + document) |
| Language | English (detect for international) |
| Accessibility | WCAG 2.1 AA compliance |

### Context Preservation

Maintain session context so users can issue follow-up commands:

- "Now make it a PDF" → Apply to current deliverable
- "Add the partnership section" → Modify current document
- "Send this to the board" → Share current output
- "In Portuguese" → Translate current content
- "More detail on financials" → Expand current section

### Graceful Degradation

When data sources are unavailable:

1. Continue with available sources
2. Flag the gap clearly in output
3. Suggest manual input for missing data
4. Document what was skipped
5. Don't fail entire workflow for partial data

Example:
```markdown
**Data Availability Note**

QuickBooks data unavailable. Financial dashboards generated with:
- Asana portfolio value estimates
- Gmail payment discussions
- Manual input recommended for: AR aging, exact revenue figures
```

---

## Error Recovery Patterns

### Pattern 1: Transient Failure Retry

For network errors, rate limits, timeout:

```
Attempt 1 → Fail → Wait 2s
Attempt 2 → Fail → Wait 4s
Attempt 3 → Fail → Wait 8s
Attempt 4 → Fail → Wait 16s
Attempt 5 → Fail → Report failure with context
```

### Pattern 2: Partial Success Preservation

For mid-workflow failures:

```markdown
**Workflow Paused**

Completed successfully:
1. executive-intelligence-dashboard (output saved)
2. 360-board-meeting-prep (packet structured)

Failed at:
3. design-director (error: [specific error])

**Recovery Options:**
A. Retry step 3 with current outputs
B. Skip design elevation and deliver draft
C. Start over with fresh data pull

Completed outputs preserved at: [file paths]
```

### Pattern 3: Alternative Routing

When preferred skill is unavailable:

1. Check for equivalent capability
2. Suggest manual alternative
3. Flag for skill maintenance
4. Document workaround

Example:
```markdown
**Routing Alternative**

360-client-portfolio-builder unavailable.

Alternatives:
- Use 360-proposal-builder for narrative content
- Manual HTML creation with design-director guidance
- Export content for external design tool

Flagged for maintenance review.
```

---

## Multi-Region Support

### Regional Configurations

| Region | Skills | Language | Timezone | Special Considerations |
|--------|--------|----------|----------|------------------------|
| **US West** | All | en-US | America/Los_Angeles | Default configuration |
| **Brazil** | 360-proposal-builder, contract-redlining-tool, workflow-debugging, intelligence-extractor | pt-BR | America/Sao_Paulo | CCBC arbitration, Brazilian law, BRL currency |
| **Europe** | 360-proposal-builder, workflow-debugging | en-GB | Europe/London | EU AI Act compliance, GDPR |

### Cultural Adaptation

For Latin American engagements:
- 360-proposal-builder: Relationship-first positioning, longer timelines
- contract-redlining-tool: Brazilian Civil Code references, CCBC clauses
- intelligence-extractor: Portuguese/Spanish language processing

For European engagements:
- ai-ethics-advisor: EU AI Act compliance emphasis
- 360-proposal-builder: Formal tone, regulatory awareness

---

## Performance Expectations

### Response Time Targets

| Category | Skills | Target Time |
|----------|--------|-------------|
| **Real-time** | workflow-debugging | <30 seconds |
| **Quick** | contract-redlining-tool, ceo-advisor (morning brief), intelligence-extractor | <5 minutes |
| **Standard** | 360-board-meeting-prep, executive-intelligence-dashboard, 360-newsletter-generator, 360-executive-project-tracker | 10-20 minutes |
| **Extended** | 360-proposal-builder, 360-client-portfolio-builder, strategic-persona-builder | 30-60 minutes |
| **Deep** | open-deep-research-team (full), executive-impact-presentation-generator | 1-2 hours |

### Complexity Indicators

Simple (single skill):
- Direct question answering
- Single document generation
- Basic data retrieval

Medium (2-3 skills):
- Proposal with prospect research
- Dashboard with design elevation
- Process documentation with validation

Complex (4+ skills):
- Full board preparation cycle
- Deal pipeline from prospect to contract
- Research to publication-ready deliverable

---

## Anti-Patterns to Avoid

### Don't Over-Orchestrate
If a single skill handles the request completely, route directly without orchestration overhead.

### Don't Ask Multiple Questions
Parse intent fully, then confirm once. Never:
- "What format?" → "What time period?" → "Which data sources?"
Instead:
- "Here's my understanding... Proceed?"

### Don't Lose Context
Preserve all outputs between workflow steps. Never require re-execution of completed steps.

### Don't Hide Failures
Surface errors immediately with:
- What failed
- What succeeded
- Recovery options
- Preserved outputs

### Don't Force Chains
If user explicitly requests single skill output, deliver it. Don't auto-add steps they didn't ask for.

### Don't Guess Payloads
If critical data is missing for agent calls, ask once for all missing items. Never fabricate data.

---

## Success Indicators

### Orchestration Quality Metrics

**Efficiency**
- Single-skill requests route in <1 second
- Multi-skill workflows announce plan before execution
- No redundant data fetches across chain

**Accuracy**
- Intent recognition matches user expectation
- Output format matches request
- All required fields populated

**Resilience**
- Graceful handling of partial data
- Recovery options for failures
- Context preservation across retries

**Quality**
- Design elevation on all visual outputs
- Accessibility compliance validated
- JSON syntax correct

### User Experience Goals

- Never ask "which skill do you want?"
- Never require skill name knowledge
- Always confirm complex workflows before execution
- Always preserve completed work during failures
- Always apply quality standards automatically

---

## Continuous Improvement

### When to Update This Strategy

**Add new routing patterns when:**
- New skills are created
- Common intent patterns emerge
- User feedback indicates confusion

**Update workflow chains when:**
- Skill capabilities change
- Data source integrations evolve
- Better patterns discovered

**Refine quality gates when:**
- New validation requirements identified
- Error patterns indicate gaps
- Quality standards evolve

### Feedback Integration Points

- workflow-debugging insights → improve error handling
- contract-redlining-tool patterns → update standard positions
- sales-automator conversion data → refine scoring models
- design-director applications → expand exemplar library

---

## Quick Reference

### Skill Ecosystem at a Glance

**Governance**: 360-board-meeting-prep, 360-newsletter-generator, executive-intelligence-dashboard

**Sales**: sales-automator, 360-proposal-builder, contract-redlining-tool

**Research**: open-deep-research-team, strategic-persona-builder, intelligence-extractor

**Advisory**: ceo-advisor, ai-ethics-advisor, fda-consultant-agent

**Operations**: 360-executive-project-tracker, workflow-debugging, workflow-process-generator

**Delivery**: design-director, 360-client-portfolio-builder, executive-impact-presentation-generator

**Financial**: financial-modeling-skills

### The Golden Rules

1. **Design elevation is mandatory** for all visual outputs
2. **One-shot clarification** not multiple questions
3. **Preserve completed work** during failures
4. **Smart defaults** reduce friction
5. **Context preservation** enables natural conversation
6. **Graceful degradation** over hard failures

---

*This strategy document is a living reference. Update as the skill ecosystem evolves.*
