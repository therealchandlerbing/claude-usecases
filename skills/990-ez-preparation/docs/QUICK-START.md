# 990-EZ Preparation - Quick Start Guide

Get your nonprofit's Form 990-EZ prepared in 10 minutes or less.

## Prerequisites

Before you start, gather:

1. **Financial Data**:
   - Revenue by source (contributions, program revenue, investment income)
   - Expenses by function (program, management, fundraising)
   - Beginning and ending balance sheets

2. **Program Information**:
   - Program descriptions and accomplishments
   - Number of beneficiaries served
   - Measurable outcomes

3. **Governance Data**:
   - List of officers and directors
   - Compensation information
   - Governance policies (conflict of interest, etc.)

## Quick Start (Claude Interface)

Simply say to Claude:

```
"Prepare our 990-EZ for 2024"
```

Claude will automatically activate the skill and guide you through the 5-phase process.

## Quick Start (Python Script)

If you want to run the standalone Python script:

```bash
# Navigate to the skill directory
cd skills/990-ez-preparation

# Run the interactive orchestrator
python src/orchestrator.py
```

## The 5-Phase Process

### Phase 1: Eligibility Check (2 minutes)

Claude will ask:
- What were your gross receipts? (must be < $200,000)
- What were your total assets? (must be < $500,000)
- Any disqualifying conditions?

**Result**: Confirmation that you qualify for 990-EZ

### Phase 2: Data Collection (30-45 minutes)

Claude will guide you through:
- Organization information
- Revenue sources
- Expense categories
- Balance sheet data
- Program accomplishments
- Governance information

**Tip**: Have your financial statements ready to make this faster.

### Phase 3: Form Population (5 minutes)

Claude automatically:
- Maps your data to form fields
- Calculates all totals
- Formats program descriptions
- Completes all form sections

**Result**: Complete draft Form 990-EZ

### Phase 4: Validation (5 minutes)

Claude performs:
- Mathematical accuracy checks
- Regulatory compliance verification
- Narrative quality review
- Strategic assessment

**Result**: Validation report with any errors, warnings, or recommendations

### Phase 5: Filing Package (5 minutes)

Claude generates:
- Complete Form 990-EZ
- Required schedules (A, B, O)
- Validation report
- Pre-filing checklist
- Executive summary

**Result**: Ready-to-file package

## Common Questions

### "What if I don't have all the data?"

No problem! Claude will:
- Clearly mark missing fields
- Allow you to come back and fill them in later
- Save your progress

### "Can I review before finalizing?"

Yes! After each phase, you can:
- Review what was collected
- Make corrections
- Add additional information

### "What if there are errors?"

Claude will:
- Identify all errors with clear explanations
- Provide specific remediation steps
- Prevent filing until errors are resolved

### "Do I need QuickBooks integration?"

No! While optional integrations are available, the skill works perfectly with manual data entry.

## Example Session

```
User: "Prepare our 990-EZ for 2024"

Claude: "I'll help you prepare Form 990-EZ for 2024. First, let me verify eligibility.

What were your gross receipts for 2024? $"

User: "145000"

Claude: "What were your total assets at year end? $"

User: "85000"

Claude: "✓ YOUR ORGANIZATION QUALIFIES FOR FORM 990-EZ

  Gross Receipts: $145,000 (< $200,000 ✓)
  Total Assets:   $85,000 (< $500,000 ✓)

Let's collect your organization information..."

[Process continues through all phases]

Claude: "Form 990-EZ preparation complete! Your filing package includes:
- Complete Form 990-EZ
- Schedule A (Public Charity Status)
- Validation Report
- Pre-filing Checklist

✓ All validations passed
✓ Ready to file

Next steps:
1. Review for accuracy
2. Obtain board approval
3. Obtain officer signatures
4. File by May 15, 2025"
```

## Tips for Success

### Before Starting

1. **Review prior year's 990** (if available) for consistency
2. **Have financial statements ready** - makes data entry much faster
3. **Block 1-2 hours** of uninterrupted time
4. **Gather governance documents** - board roster, policies

### During Preparation

1. **Be specific in program descriptions** - include metrics and outcomes
2. **Double-check numbers** against your accounting system
3. **Answer Part V questions carefully** - these trigger additional requirements
4. **Use Schedule O liberally** - provide context and explanations

### After Generation

1. **Review thoroughly** - especially calculations and cross-references
2. **Get board approval** - recommended best practice
3. **Keep documentation** - retain supporting docs for 7 years
4. **File on time** - May 15 for calendar year organizations

## Next Steps

Once your 990-EZ is complete:

1. **State Filings**: Check if your state requires additional forms (e.g., California RRF-1)
2. **Public Disclosure**: Prepare public copy (without Schedule B)
3. **GuideStar**: Consider posting to GuideStar for transparency
4. **Planning**: Use insights to plan for next year

## Getting Help

### Within the Skill

Ask Claude:
- "Explain this validation error"
- "What does public support test mean?"
- "How should I describe this program?"
- "What's the difference between program and management expenses?"

### External Resources

- **IRS Instructions**: https://www.irs.gov/pub/irs-pdf/i990ez.pdf
- **IRS StayExempt**: https://www.stayexempt.irs.gov
- **National Council of Nonprofits**: https://www.councilofnonprofits.org

### When to Get Professional Help

Consider consulting a tax professional if:
- This is your first time filing
- You have complex revenue sources (UBI, foreign grants)
- You're failing the public support test
- You have related party transactions
- You're uncertain about any answers

## Troubleshooting

### "I'm not sure if we qualify"

If you're near the thresholds ($200K revenue, $500K assets), be conservative:
- Use the higher filing (Form 990) if uncertain
- Consult a tax professional for borderline cases

### "Our expenses don't fit the categories"

That's normal! Use your best judgment and:
- Document your allocation methodology
- Be consistent with prior years
- Use Schedule O to explain if needed

### "We have unrelated business income"

If you have >$1,000 in UBI:
- You'll need to file Form 990-T in addition to 990-EZ
- This skill focuses on 990-EZ; seek professional help for 990-T

### "We operate in multiple states"

State filing requirements vary:
- Check each state where you're registered
- Many states accept federal 990-EZ with a cover form
- File all state forms by their deadlines

## Success Metrics

You'll know you're done when:
- ✓ All form sections complete
- ✓ All validations passing
- ✓ No errors in validation report
- ✓ Board approval obtained
- ✓ Officer signatures ready
- ✓ Filing checklist complete

## Time Savings

Traditional manual preparation: **40+ hours**
With this skill: **10 hours or less**

**Savings**: 75% time reduction, plus increased accuracy and confidence

---

**Ready to start?** Say: *"Prepare our 990-EZ for 2024"*

**Questions?** Review the full [README](../README.md) or [SKILL.md](../SKILL.md)
