# Express Workflow

**Trigger**: User requests quick research or summary

## Process

1. Generate brief research plan (skip clarification if clear)
2. Deploy 1-2 specialist agents based on query type
3. Quick synthesis of findings
4. Brief summary output (no full report)

## Total Time

10-20 minutes

## Agent Selection Based on Query Type

**Technical Questions:**
- Deploy: Technical Researcher

**Academic/Research Questions:**
- Deploy: Academic Researcher

**Market/Statistical Questions:**
- Deploy: Data Analyst

**Multi-domain Questions:**
- Deploy: 2 most relevant agents

## Output Format

Brief markdown summary with:
- Quick findings (bullet points)
- Key sources (3-5 citations)
- Confidence scores
- Next steps if deeper research needed

## When to Use

- Quick overview needed
- Preliminary research before deep dive
- Simple, focused questions
- Time constrained (10-20 minutes)
- Initial scoping for larger research project
