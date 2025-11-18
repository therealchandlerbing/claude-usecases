---
name: open-deep-research-team
description: Sophisticated multi-agent AI research system that conducts comprehensive, academic-quality research on complex topics through orchestrated specialist agents. Use for deep research requiring academic, technical, and data-driven perspectives with quality assurance and comprehensive reporting.
tools: Web Search, Web Fetch, Task, TodoWrite
model: sonnet
---

# Open Deep Research Team Skill

## Overview

The Open Deep Research Team is a sophisticated multi-agent research system that conducts comprehensive, academic-quality research on complex topics. This skill orchestrates nine specialized agents through a hierarchical workflow, ensuring thorough coverage, rigorous analysis, and high-quality research outputs.

## Architecture

### Core Components

**Research Workflow Phases:**
1. Query Processing (Clarification and Brief Generation)
2. Strategic Planning (Task Allocation and Coordination)
3. Parallel Research (Specialized Investigation)
4. Synthesis (Consolidation and Analysis)
5. Report Generation (Final Output Creation)

**Agent Hierarchy:**
- **Orchestrator**: Central coordinator managing all phases
- **Specialists**: Eight domain-specific research agents
- **Communication**: Structured JSON protocol for inter-agent data transfer

## Agent Capabilities

### 1. Research Orchestrator
- Manages complete research workflow from query to report
- Routes tasks to appropriate specialized agents
- Maintains quality gates between phases
- Tracks progress and handles errors gracefully

### 2. Query Clarifier
- Analyzes research queries for clarity and specificity
- Generates structured clarification questions when needed
- Produces confidence scores for query actionability
- Refines ambiguous requests into clear research objectives

### 3. Research Brief Generator
- Transforms queries into actionable research plans
- Defines specific research questions and success criteria
- Identifies appropriate sources and methodologies
- Establishes scope boundaries and timelines

### 4. Research Coordinator
- Plans task allocation across specialist researchers
- Manages parallel research threads and dependencies
- Optimizes resource utilization and workload balance
- Defines iteration strategies for comprehensive coverage

### 5. Academic Researcher
- Searches scholarly databases (ArXiv, PubMed, Google Scholar)
- Evaluates peer-reviewed sources and journal quality
- Maintains academic rigor and proper citations
- Identifies research gaps and seminal works

### 6. Technical Researcher
- Analyzes code repositories and technical documentation
- Evaluates implementation patterns and best practices
- Reviews API specifications and integration details
- Assesses technical feasibility and code quality

### 7. Data Analyst
- Provides quantitative analysis and statistical insights
- Identifies trends and patterns in numerical data
- Creates comparative analyses across datasets
- Suggests data visualizations and metrics

### 8. Research Synthesizer
- Consolidates findings from multiple sources
- Resolves contradictions and analyzes biases
- Preserves nuance while creating accessible summaries
- Generates structured insights for reporting

### 9. Report Generator
- Creates comprehensive, well-structured reports
- Manages citations and bibliography formatting
- Develops executive summaries and recommendations
- Supports multiple output formats (academic, business, technical)

## Usage Instructions

### Basic Research Request

```
Please conduct comprehensive research on [TOPIC] focusing on:
- Key developments in the last 3 years
- Technical implementation approaches
- Academic perspectives and research gaps
- Practical applications and case studies
```

### Advanced Configuration

```json
{
  "research_query": "Your research topic",
  "configuration": {
    "depth": "comprehensive|standard|quick",
    "focus_areas": ["academic", "technical", "practical"],
    "source_preferences": ["peer_reviewed", "industry_reports", "case_studies"],
    "output_format": "academic|business|technical",
    "time_frame": "last_3_years",
    "include_contradictions": true,
    "confidence_threshold": 0.7
  }
}
```

### Workflow Triggers

**Full Research Pipeline:**
```
Trigger: "Conduct deep research on..."
Flow: Orchestrator → Clarifier → Brief → Coordinator → Specialists → Synthesizer → Report
```

**Quick Research:**
```
Trigger: "Quick research summary on..."
Flow: Brief → Coordinator → Reduced Specialist Set → Synthesizer → Summary
```

**Academic Focus:**
```
Trigger: "Academic research on..."
Flow: Brief → Academic Researcher (primary) → Other Specialists (support) → Academic Report
```

## Integration Patterns

### Sequential Processing
Each phase completes before the next begins, ensuring quality control and proper dependency management.

### Parallel Execution
Specialist researchers work simultaneously during the research phase, maximizing efficiency.

### State Management
The orchestrator maintains persistent context throughout the workflow:
- Research findings accumulation
- Source tracking and citation management
- Quality metrics and confidence scoring
- Progress tracking and milestone completion

### Error Handling
- Graceful degradation when sources are unavailable
- Retry mechanisms for transient failures
- Alternative path selection for blocked research avenues
- Partial result compilation when full research cannot be completed

## Quality Control

### Validation Checkpoints
1. **Query Validation**: Ensures research question is clear and actionable
2. **Brief Review**: Confirms research plan completeness
3. **Source Verification**: Validates credibility and relevance
4. **Synthesis Check**: Ensures comprehensive coverage
5. **Report QA**: Final quality assurance before delivery

### Confidence Scoring
- Each finding includes confidence level (0.0-1.0)
- Sources are weighted by credibility and recency
- Contradictions are explicitly noted with evidence strength
- Overall research confidence score provided in final report

## Output Formats

### Academic Report
- Abstract and introduction
- Literature review
- Methodology discussion
- Findings and analysis
- Conclusions and future work
- Full bibliography with DOI links

### Business Report
- Executive summary
- Key findings and insights
- Market analysis and trends
- Recommendations and action items
- Risk assessment
- Appendices with supporting data

### Technical Documentation
- Technical overview
- Implementation details
- Code examples and snippets
- Performance benchmarks
- Integration guidelines
- API documentation references

## Best Practices

### For Optimal Results
1. Provide specific research objectives rather than broad topics
2. Indicate preferred source types and quality requirements
3. Specify time constraints and depth expectations
4. Include any existing knowledge or context
5. Clarify output format and intended audience

### Common Use Cases

**Academic Research:**
- Literature reviews for research proposals
- State-of-the-art surveys
- Research gap identification
- Citation network analysis

**Technical Investigation:**
- Technology stack evaluations
- Implementation pattern research
- Best practice compilation
- Tool and framework comparisons

**Business Intelligence:**
- Market research and analysis
- Competitive intelligence gathering
- Trend analysis and forecasting
- Industry report synthesis

**Data-Driven Analysis:**
- Statistical trend identification
- Benchmark comparisons
- Performance metric analysis
- Quantitative research synthesis

## Advanced Features

### Iteration Strategies
The system supports multiple research iterations:
- **Breadth-first**: Wide coverage across all aspects
- **Depth-first**: Deep dive into specific areas
- **Adaptive**: Adjusts based on initial findings
- **Targeted**: Focuses on user-specified priorities

### Source Management
- Automatic deduplication across researchers
- Source credibility scoring
- Recency weighting for time-sensitive topics
- Citation format standardization

### Collaboration Features
- Progress tracking with TodoWrite integration
- Intermediate result sharing
- Research checkpoint saves
- Collaborative annotation support

## Troubleshooting

### Common Issues

**Query Too Broad:**
- System will request clarification
- Provide specific subtopics or focus areas
- Consider breaking into multiple research requests

**Insufficient Sources:**
- System will note limitations
- Consider expanding search parameters
- May suggest alternative research approaches

**Contradictory Findings:**
- System preserves all perspectives
- Provides evidence strength for each position
- Suggests areas needing further investigation

## Performance Metrics

### Expected Timelines
- Quick Research: 5-10 minutes
- Standard Research: 15-30 minutes
- Comprehensive Research: 30-60 minutes

### Coverage Metrics
- Source diversity: 10-50+ sources per research
- Perspective variety: Academic, industry, practical
- Time span: Configurable from recent to historical
- Geographic coverage: Global perspective when relevant

## When to Use This Skill

**Use open-deep-research-team when:**
- User requests comprehensive research on a complex topic
- User needs academic, technical, and business perspectives combined
- User asks for a literature review or state-of-the-art analysis
- User wants competitive intelligence with thorough sourcing
- User needs research with proper citations and bibliography
- User requests analysis of contradictory information
- User wants a research report with executive summary

**Trigger phrases:**
- "Conduct deep research on..."
- "I need comprehensive research about..."
- "Research the current state of..."
- "Give me a thorough analysis of..."
- "What does the research say about..."
- "Analyze all perspectives on..."
- "Literature review on..."
- "State of the art in..."

## Integration with Ecosystem

**Data Sources:**
- Web Search (current information, news, industry reports)
- ArXiv, PubMed, Google Scholar (academic research)
- GitHub (code repositories, technical implementations)
- Industry databases (market data, statistics)

**Output Integration:**
- Can feed findings into other skills for actionable next steps
- Research reports can inform strategic planning
- Technical findings can guide implementation decisions
- Market analysis can drive business strategy

## Important Rules

1. **Always clarify ambiguous queries** - Ensure research questions are actionable
2. **Maintain academic rigor** - Proper citations, source evaluation, confidence scoring
3. **Track progress** - Use TodoWrite to show research phases
4. **Preserve contradictions** - Don't oversimplify when sources disagree
5. **Evidence-based synthesis** - All conclusions backed by sources
6. **Transparent limitations** - Acknowledge gaps and uncertainties
7. **Multi-perspective** - Include academic, technical, and practical viewpoints
8. **Quality over speed** - Thorough research takes time
9. **Structured output** - Clear organization with executive summary
10. **Actionable insights** - Provide recommendations where appropriate

## Version History

- **v1.0**: Initial multi-agent system with core functionality
- **v1.1**: Added parallel processing and state management
- **v1.2**: Enhanced synthesis and report generation
- **v1.3**: Improved error handling and quality control

## Remember

This skill orchestrates multiple specialized agents to conduct research at a level of depth and rigor that matches academic standards. Always prioritize quality, acknowledge uncertainty, preserve nuance, and provide properly cited, comprehensive analysis.

For detailed agent-specific instructions, see the `/prompts` directory.
For implementation examples, see the `/examples` directory.
For usage guidance, see the `/docs` directory.
