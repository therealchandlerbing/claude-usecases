# Troubleshooting Guide

## Issue: Query Too Broad

**Symptoms:**
- Query Clarifier requests extensive clarification
- Estimated time exceeds available resources
- Scope unbounded

**Solutions:**
- Break into multiple focused research projects
- Specify subtopics or priority areas
- Define time or geographic constraints
- Start with Express mode for overview, then deep dive

**Example:**
- **Too Broad**: "Research renewable energy"
- **Better**: "Research solar energy storage solutions for residential use in the US, focusing on current technologies, cost trends, and 2024-2030 projections"

---

## Issue: Insufficient Sources Found

**Symptoms:**
- Specialist agents return fewer sources than minimum
- Low confidence scores across findings
- Limited perspectives available

**Solutions:**
- Expand search parameters (time frame, geography)
- Include additional source types (preprints, technical blogs)
- Consider alternative search terms
- Accept limitations and note in research gaps

**Example:**
- If academic sources limited, leverage technical implementations
- If recent data scarce, analyze historical trends
- If geography-specific data missing, use regional proxies

---

## Issue: Contradictory Findings

**Symptoms:**
- Research Synthesizer identifies multiple contradictions
- Sources disagree on key points
- No clear consensus

**Solutions:**
- This is a feature, not a bug! Preserve both perspectives
- Analyze evidence strength for each position
- Check for methodological differences
- Consider context (different use cases, time periods)
- Provide balanced view with confidence scores

**Example:**
"Research shows contradictory findings on [TOPIC]. Position A (confidence: 0.6) suggests [FINDING] based on [EVIDENCE]. Position B (confidence: 0.7) argues [DIFFERENT FINDING] supported by [EVIDENCE]. The contradiction appears to stem from [METHODOLOGICAL DIFFERENCE]. For your use case, Position B may be more applicable because [REASONING]."

---

## Issue: Research Taking Too Long

**Symptoms:**
- Exceeding estimated timeline
- Specialist agents still processing
- User time-constrained

**Solutions:**
- Switch to Express mode for initial results
- Focus on highest-priority research questions
- Limit specialist agent deployment (2-3 instead of all)
- Set explicit time limits per phase
- Deliver partial results with plan for completion

---

## Issue: Too Technical / Too Academic

**Symptoms:**
- Output not accessible for intended audience
- Excessive jargon or complexity
- User feedback indicates comprehension issues

**Solutions:**
- Request different output format (business vs academic)
- Ask Report Generator to simplify language
- Include glossary of technical terms
- Provide both executive summary and detailed analysis
- Use more analogies and examples
