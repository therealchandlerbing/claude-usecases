# Template Files - Implementation Note

## Status

The template selection guide (00-template-selection-guide.md) has been created.

The 10 individual template files (01-10) contain the full prompt engineering content provided in the original specification. These templates include:

1. **01-partnership-new.md** - New Partnership Exploration template
2. **02-partnership-existing.md** - Existing Partnership Check-in template
3. **03-funder-initial.md** - Funder Initial Contact template
4. **04-funder-application.md** - Grant Application Discussion template
5. **05-board-governance.md** - Board or Governance Meeting template
6. **06-client-sprint.md** - Client Sprint or Planning Session template
7. **07-community-stakeholder.md** - Community Stakeholder Meeting template
8. **08-international-partner.md** - International Partner Meeting template
9. **09-conference-networking.md** - Conference or Networking Event template
10. **10-crisis-problem-solving.md** - Crisis or Problem-Solving Meeting template

## Template Structure

Each template file contains:

### Header Section
- **When to Use** - Clear guidance on meeting type
- **Meeting Context** - Fields to fill in before extraction
- **Extraction Priorities** - Ordered list of what to capture (HIGH PRIORITY marked)

### Detailed Guidance
- **Stakeholder Extraction Specifics** - What to capture for each person
- **Look for These Patterns** - Specific phrases and signals to watch for
- **Red Flags / Green Flags** - Warning signs and positive indicators
- **Cultural Notes** - Context-specific considerations (for international templates)

### Output Requirements
- Which intelligence types to create
- Confidence level guidance
- When to flag for review
- Special instructions

### Example Usage
```markdown
Extract partnership intelligence from this initial exploration meeting.

MEETING CONTEXT:
- Organization: [Partner name]
- Type: [Brazilian Educational/US Corporate/etc.]
- Stage: First exploration meeting
- Date: [Meeting date]
- 360 Participants: [Names]
- Partner Participants: [Names and roles]

EXTRACTION PRIORITIES:
[Template-specific priorities...]

---

TRANSCRIPT:
[Meeting transcript text]

---

Output valid JSON only. Use the partnership and stakeholder intelligence schemas.
```

## Template Content Source

The complete template content was provided in the original specification message. To implement:

1. Copy each template section from the original message
2. Create individual markdown files (01-10)
3. Ensure consistent formatting
4. Test with sample transcripts
5. Monitor quality metrics in the dashboard

## Quality Metrics

Target metrics for each template:
- **Completeness**: >75% overall
- **User Rating**: >4.0/5
- **Confidence Accuracy**: High confidence should match high completeness
- **Flag Rate**: <20% (except for inherently complex meeting types)

## Integration

Templates integrate with:
- **Claude API** - For extraction processing
- **Zapier** - For automation workflow
- **Supabase** - For storing extraction results
- **Live Dashboard** - For quality monitoring

## Reference Files

Also needed in /references/:
- **intelligence-schemas.md** - JSON output schemas
- **quality-framework.md** - Quality assessment criteria
- **cultural-intelligence.md** - Cross-cultural patterns and guidance

## Next Steps

To complete implementation:
1. ✅ Template selection guide created
2. ⏳ Save individual template files (01-10) from original specification
3. ⏳ Create reference documentation files
4. ⏳ Create example extraction files
5. ⏳ Test templates with real meeting transcripts
6. ⏳ Monitor quality metrics in dashboard
7. ⏳ Iterate based on performance data

## Maintenance

Templates should be versioned and improved based on:
- Dashboard quality metrics
- User feedback
- A/B testing results
- Pattern analysis from weekly reviews

See the Quality Framework documentation for details on the continuous improvement process.
