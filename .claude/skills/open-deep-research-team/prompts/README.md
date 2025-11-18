# Agent System Prompts

This directory contains the system prompts for each of the nine specialized agents in the Open Deep Research Team.

## Agent Overview

### Orchestration Layer
1. **[research_orchestrator.md](research_orchestrator.md)** - Central coordinator managing the entire workflow
2. **[query_clarifier.md](query_clarifier.md)** - Transforms ambiguous questions into clear objectives
3. **[research_brief_generator.md](research_brief_generator.md)** - Creates comprehensive research plans
4. **[research_coordinator.md](research_coordinator.md)** - Designs strategic agent deployment

### Specialist Research Layer
5. **[academic_researcher.md](academic_researcher.md)** - Scholarly sources and peer-reviewed literature
6. **[technical_researcher.md](technical_researcher.md)** - Code repositories, implementations, technical documentation
7. **[data_analyst.md](data_analyst.md)** - Quantitative analysis and statistical insights

### Integration Layer
8. **[research_synthesizer.md](research_synthesizer.md)** - Consolidates findings from all specialists
9. **[report_generator.md](report_generator.md)** - Creates publication-ready reports

## Agent Workflow

```
User Query
    ↓
[Research Orchestrator] → Manages entire process
    ↓
[Query Clarifier] → Ensures clarity (if needed)
    ↓
[Research Brief Generator] → Creates research plan
    ↓
[Research Coordinator] → Plans agent deployment
    ↓
Parallel Execution:
    ├── [Academic Researcher] → Scholarly sources
    ├── [Technical Researcher] → Code & implementations
    └── [Data Analyst] → Quantitative analysis
    ↓
[Research Synthesizer] → Integrates all findings
    ↓
[Report Generator] → Produces final output
    ↓
User receives comprehensive research report
```

## Using Agent Prompts

### For Development
These prompts define each agent's:
- Identity and purpose
- Core capabilities
- Input/output specifications
- Decision-making criteria
- Quality standards

### For Customization
Modify agent prompts to:
- Add domain-specific knowledge
- Adjust prioritization criteria
- Change output formats
- Enhance quality checks

### For Understanding
Review prompts to understand:
- Agent responsibilities
- Workflow dependencies
- Quality assurance mechanisms
- Integration patterns

## Agent Capabilities Summary

| Agent | Primary Function | Key Outputs | Typical Time |
|-------|-----------------|-------------|--------------|
| Query Clarifier | Ensure actionable research questions | Refined query, clarity score | 3-7 min |
| Research Brief Generator | Create comprehensive research plan | Research framework, success criteria | 5-10 min |
| Research Coordinator | Strategic agent deployment | Task allocation, execution plan | 3-5 min |
| Academic Researcher | Scholarly research | Papers, citations, academic insights | 20-40 min |
| Technical Researcher | Code & implementation analysis | Repos, benchmarks, best practices | 15-30 min |
| Data Analyst | Quantitative analysis | Statistics, trends, metrics | 15-30 min |
| Research Synthesizer | Integrate findings | Consolidated insights, contradictions | 10-15 min |
| Report Generator | Publication-ready output | Formatted report, citations | 10-15 min |
| Research Orchestrator | Overall coordination | Complete research project | Full duration |

## Best Practices

When working with agent prompts:

1. **Maintain Consistency**: Keep terminology and standards consistent across agents
2. **Clear Interfaces**: Define clear input/output specifications
3. **Quality Standards**: Embed quality criteria in each agent
4. **Error Handling**: Include graceful degradation strategies
5. **Documentation**: Keep prompts well-documented and versioned

## Extending Agents

To enhance agent capabilities:

### Add Domain Expertise
```markdown
Additional expertise for [Agent Name]:
- Domain: [Healthcare/Finance/Legal/etc.]
- Special knowledge: [Specific expertise]
- Additional sources: [Domain-specific databases]
- Quality criteria: [Domain standards]
```

### Add New Evaluation Criteria
```markdown
Additional evaluation for [Agent Name]:
- Criterion: [What to evaluate]
- Method: [How to evaluate]
- Threshold: [Acceptance criteria]
```

### Customize Output Format
```markdown
Modified output for [Agent Name]:
- Format: [JSON/Markdown/Structured]
- Required fields: [Specifications]
- Optional fields: [Additional data]
```

## Version Control

Track agent prompt versions:
- **v2.0**: Production-grade managed skill release
- **v1.3**: Enhanced synthesis and reporting
- **v1.2**: Parallel processing improvements
- **v1.1**: Quality control enhancements
- **v1.0**: Initial agent system

## Future Enhancements

Planned agent improvements:
- **v2.1**: Research memory integration
- **v2.5**: Adaptive learning from past research
- **v3.0**: Personalization based on user preferences
- **v3.5**: Domain-specific agent variants

---

*These agent prompts are the intelligence core of the Open Deep Research Team. They embody research best practices and quality standards.*
