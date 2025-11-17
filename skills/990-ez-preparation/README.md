# IRS Form 990-EZ Preparation Skill

**Automated nonprofit tax compliance through intelligent data collection, validation, and filing package generation.**

## Overview

The 990-EZ Preparation Skill transforms complex nonprofit tax filing from a 40+ hour manual process into a streamlined 10-hour guided workflow. Built specifically for 360 Social Impact Studios and small nonprofit organizations, this skill provides expert guidance through every phase of Form 990-EZ preparation.

### Key Benefits

- **Time Savings**: Reduce preparation time by 75% through automation and intelligent guidance
- **Error Prevention**: Multi-level validation catches mathematical and regulatory errors before filing
- **Compliance Confidence**: Built-in IRS compliance checks and expert guidance
- **Complete Package**: Generates all required forms, schedules, and supporting documentation
- **Professional Quality**: Board-ready outputs with clear narratives and proper formatting

## Quick Start

### Prerequisites

- Organization must qualify for 990-EZ:
  - Gross receipts < $200,000
  - Total assets < $500,000
  - Not a donor advised fund sponsor
  - Not operating hospital facilities

### Basic Usage

```bash
# Activate the skill
"Prepare our 990-EZ for 2024"

# Check eligibility only
"Check if we qualify for 990-EZ"

# Resume existing preparation
"Continue 990-EZ preparation"
```

## What You'll Need

### Required Information

1. **Basic Organization Info**
   - Legal name and EIN
   - Tax year and fiscal year end
   - 501(c) classification

2. **Financial Data**
   - Revenue by source (contributions, program revenue, investment income)
   - Expenses by function (program, management, fundraising)
   - Beginning and ending balance sheet

3. **Program Information**
   - Program descriptions and accomplishments
   - Beneficiaries served and outcomes achieved
   - Expenses and revenue by program

4. **Governance Data**
   - Officers and directors (names, titles, hours, compensation)
   - Board policies (conflict of interest, whistleblower, etc.)
   - Related party transactions

5. **Donor Information** (if applicable)
   - List of contributors who gave $5,000 or more
   - Names, addresses, and contribution amounts

### Data Sources

The skill can work with:
- **QuickBooks**: Direct integration or CSV export (Profit & Loss, Balance Sheet)
- **Asana**: Program metrics and accomplishments from Client Delivery Hub
- **Google Drive**: Governance documents and board minutes
- **Manual Entry**: Guided data collection templates

## Workflow Overview

### Phase 1: Eligibility Verification (5 minutes)
- Verify gross receipts and total assets thresholds
- Check for disqualifying conditions
- Confirm organization qualifies for 990-EZ

### Phase 2: Data Collection (30-60 minutes)
- Guided collection of financial data
- Program accomplishment documentation
- Governance information gathering
- Donor/grant data collection (if needed)

### Phase 3: Form Population (15 minutes)
- Automated mapping of data to form fields
- Calculation of all totals and subtotals
- Generation of program narratives
- Completion of all form sections

### Phase 4: Multi-Level Validation (10 minutes)
- **Level 1**: Mathematical accuracy verification
- **Level 2**: Regulatory compliance checks
- **Level 3**: Narrative quality review
- **Level 4**: Strategic alignment assessment

### Phase 5: Filing Package Generation (10 minutes)
- Form 990-EZ (complete)
- Schedule A (Public Charity Status)
- Schedule B (Contributors $5,000+)
- Schedule O (Supplemental Information)
- Public disclosure copy (without Schedule B)
- Validation report and pre-filing checklist

## Validation Framework

### Mathematical Validation
- Revenue line items sum correctly
- Expense categories total properly
- Balance sheet equation balances
- Net assets reconcile between Part I and Part II

### Regulatory Compliance
- Public support test (for 501(c)(3) organizations)
- Expense allocation reasonableness
- Compensation documentation requirements
- Required governance policies

### Quality Indicators
- Program expense ratio (target: 65%+ for charity ratings)
- Revenue diversification
- Financial sustainability
- Governance best practices

## Example Output

```markdown
## 990-EZ Filing Package for 360 Social Impact Studios

**Tax Year**: 2024
**Filing Deadline**: May 15, 2025

### Financial Summary
- Gross Receipts: $121,200
- Total Expenses: $118,000
- Net Income: $3,200
- Total Assets: $21,200

### Validation Results
✓ Qualifies for 990-EZ filing
✓ All mathematical calculations verified
✓ Passes public support test (Schedule A)
✓ Program expense ratio: 72%
⚠️ Recommendation: Develop whistleblower policy

### Filing Package Contents
1. Form 990-EZ (complete, 4 pages)
2. Schedule A - Public Charity Status
3. Schedule B - Schedule of Contributors (IRS only)
4. Schedule O - Supplemental Information
5. Public Disclosure Copy (for posting/distribution)
6. Validation Report
7. Pre-Filing Checklist

### Next Steps
1. Review all documents for accuracy
2. Obtain board approval (recommended)
3. Obtain officer signatures (President and Treasurer)
4. File electronically by May 15, 2025
5. Complete state filings (if applicable)
```

## Configuration

### Integration Setup (Optional)

If you want to enable automated data collection:

1. **QuickBooks Integration**
   - See `docs/API-INTEGRATION.md` for setup instructions
   - Requires OAuth2 authentication
   - Enables real-time financial data extraction

2. **Asana Integration**
   - Requires personal access token
   - Pulls program metrics from Client Delivery Hub
   - Auto-populates program accomplishments

3. **Google Drive Integration**
   - Uses service account or OAuth2
   - Searches for governance documents
   - Stores final filing package

### Manual Mode (Default)

The skill works perfectly well without integrations:
- Provides structured data collection templates
- Guides you through each required data point
- Validates data as you enter it
- Generates complete filing package

## Tips for Best Results

### Before You Start

1. **Gather your documents**:
   - Financial statements (Profit & Loss, Balance Sheet)
   - Program reports or annual report
   - Board roster and minutes
   - Donor/grant list

2. **Review prior year** (if available):
   - Check for consistency in reporting
   - Note any significant changes
   - Verify officer information is current

3. **Set aside time**:
   - Plan for 1-2 hours of focused work
   - Have all data readily accessible
   - Review in batches (data collection, then validation)

### During Preparation

1. **Be specific in program descriptions**:
   - Use concrete metrics (# served, outcomes achieved)
   - Describe WHO you serve, WHAT you do, and IMPACT achieved
   - Keep descriptions clear and public-disclosure appropriate

2. **Allocate expenses appropriately**:
   - Program services should typically be 65%+
   - Document allocation methodology
   - Be consistent with prior years unless changes justified

3. **Review governance questions carefully**:
   - Answer Part V questions accurately
   - Flag any "Yes" answers that might require explanation
   - Document governance policies

### After Generation

1. **Review thoroughly**:
   - Check all numbers against source documents
   - Read program narratives for clarity
   - Verify officer information is current

2. **Get board approval** (recommended):
   - Present validation report to board
   - Obtain formal approval before filing
   - Document approval in board minutes

3. **Retain documentation**:
   - Keep complete filing package for records
   - Maintain supporting documentation (7 years)
   - Prepare public disclosure copy

## Compliance Guide

### Filing Deadlines

- **Regular Deadline**: 15th day of 5th month after fiscal year end
  - Calendar year orgs (12/31): May 15
  - June 30 fiscal year: November 15

- **Extension Available**: Form 8868 provides 6-month automatic extension
  - Must be filed before regular deadline
  - Extends filing deadline, not payment deadline (if tax owed)

### Public Disclosure Requirements

Organizations must make available for public inspection:
- Form 990-EZ (WITHOUT Schedule B)
- Schedule A and Schedule O
- Form 1023/1024 (exemption application)

**Not Public**: Schedule B (contributor information)

### State Filing Requirements

Many states require:
- Copy of federal Form 990-EZ
- State-specific forms (e.g., California RRF-1, New York CHAR500)
- Annual registration renewals
- Charitable solicitation compliance

The skill will flag state requirements based on your jurisdiction.

### Common Compliance Issues

**Avoid These Errors**:
- ❌ Incorrect EIN or organization name
- ❌ Math errors or unbalanced balance sheet
- ❌ Missing required schedules (Schedule A for 501(c)(3))
- ❌ Incomplete Part V answers
- ❌ Missing officer signatures

**Best Practices**:
- ✓ Double-check all figures against source documents
- ✓ Have a second person review before filing
- ✓ Keep detailed documentation of all entries
- ✓ File on time or request extension
- ✓ Post public disclosure copy to website

## Troubleshooting

### "We don't qualify for 990-EZ"

If gross receipts >= $200K or assets >= $500K:
- You must file Form 990 (full version)
- This skill focuses on 990-EZ, but can help with data organization
- Consider professional assistance for full 990

### "Our expenses don't fit the categories"

Functional allocation can be complex:
- Document your methodology clearly
- Use reasonable allocation percentages
- Be consistent with prior years
- Consider using Schedule O to explain

### "We're failing the public support test"

If public support < 33.33%:
- Review 5-year support calculation
- Consider "facts and circumstances" test
- May need to reclassify as private foundation
- Seek professional tax advice

### "We have foreign grants/activities"

Special reporting may be required:
- Foreign grants may require Schedule F
- Foreign activities may trigger additional reporting
- This skill handles domestic operations best
- Consult tax professional for international activities

## Support & Resources

### Skill Documentation

- **SKILL.md**: Complete workflow and technical details
- **API-INTEGRATION.md**: Integration setup guide
- **COMPLIANCE-GUIDE.md**: Tax compliance reference
- **Examples**: Sample data and completed forms

### External Resources

- **IRS Form 990-EZ Instructions**: https://www.irs.gov/forms-pubs/about-form-990-ez
- **IRS Publication 557**: Tax-Exempt Status for Your Organization
- **StayExempt.IRS.gov**: Free online training and resources
- **National Council of Nonprofits**: Best practices and guides

### When to Seek Professional Help

Consider engaging a tax professional if:
- First time filing Form 990-EZ
- Significant changes from prior year
- Complex revenue sources (UBI, foreign grants)
- Related party transactions
- Compensation > $150,000
- Failing public support test
- Political or lobbying activities
- Uncertain about any answers

## Contributing

This skill is part of the claude-usecases repository. Contributions welcome:

1. Report issues or suggest improvements
2. Share your experience using the skill
3. Contribute additional validation rules
4. Add integration modules for other accounting systems

## Version History

- **v1.0.0** (November 2025): Initial release
  - Core eligibility verification
  - Complete form population workflow
  - Multi-level validation framework
  - Schedule generation (A, B, O)
  - Filing package creation
  - Comprehensive documentation

## License

This skill is provided for use by 360 Social Impact Studios and the nonprofit community. Use responsibly and verify all outputs with qualified professionals before filing.

---

**Ready to get started?** Simply say: *"Prepare our 990-EZ for 2024"*

**Questions?** Review the [SKILL.md](SKILL.md) for complete technical details or [COMPLIANCE-GUIDE.md](docs/COMPLIANCE-GUIDE.md) for tax guidance.

---

*Built with care for nonprofit organizations*
*Version 1.0 | November 2025*
