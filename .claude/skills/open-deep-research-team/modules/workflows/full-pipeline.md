# Full Pipeline Workflow

**Trigger**: User requests comprehensive research on complex topic

## Process

### Phase 1: Query Processing (5-10 minutes)

1. **Query Clarifier** analyzes request
   - If clarity_score < 0.7: Request clarification from user
   - If clarity_score >= 0.7: Proceed to brief generation
2. **Research Brief Generator** creates research plan
   - Validate with user if major assumptions made
   - Get approval for scope and approach

### Phase 2: Strategic Planning (5 minutes)

3. **Research Coordinator** designs execution strategy
   - Determine agent allocation
   - Set success metrics
   - Plan synthesis approach

### Phase 3: Parallel Research (20-40 minutes)

4. Deploy specialist agents in parallel:
   - **Academic Researcher**: Scholarly sources
   - **Technical Researcher**: Code and implementations
   - **Data Analyst**: Quantitative analysis
5. Monitor progress and handle errors
6. Collect specialist outputs

### Phase 4: Synthesis (10-15 minutes)

7. **Research Synthesizer** consolidates findings
   - Integrate all specialist outputs
   - Resolve contradictions
   - Assign confidence scores
   - Identify gaps

### Phase 5: Report Generation (10-15 minutes)

8. **Report Generator** creates final deliverable
   - Select appropriate format
   - Structure findings clearly
   - Complete citations
   - Quality assurance check

## Total Time

50-85 minutes for comprehensive research

## Quality Gates

- [ ] Query clarity validated
- [ ] Research brief approved
- [ ] Minimum source count met
- [ ] All specialists completed successfully
- [ ] Synthesis addresses all research questions
- [ ] Report passes quality checklist

## When to Use

- Complex, multi-faceted research questions
- High stakes decisions requiring rigor
- Multiple perspectives needed (academic + technical + data)
- Comprehensive documentation required
- Time available (50+ minutes)
