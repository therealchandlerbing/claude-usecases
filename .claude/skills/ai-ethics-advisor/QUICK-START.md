# AI Ethics Advisor: Quick Start Guide

**Get started in 15 minutes**

## The 5-Minute Fairness Test

Before anything else, run this quick check on your AI system:

### 1. Who's in your training data?
- Does it match who will be affected?
- Any groups missing or underrepresented?

### 2. Test on at least 3 demographic groups:
- Compare accuracy/error rates
- **Red flag**: >10% difference between groups

### 3. Look for the "80% rule":
```
Selection rate for protected group / Selection rate for reference group
```
- **Red flag**: <0.8 (this is the legal standard for disparate impact)

### 4. Check the edges:
- What happens with unusual inputs?
- Who gets weird errors?

### 5. Ask someone different:
- Would this seem fair to someone from an affected group?
- Have you actually asked them?

## Decision Tree: What Assessment Do You Need?

```
START: Are you building/deploying AI?
  |
  +-- Does it make decisions about people?
  |    |
  |    YES --> Are decisions consequential?
  |    |       (affect opportunity, resources, rights)
  |    |         |
  |    |         YES --> Use COMPREHENSIVE assessment (Tier 2)
  |    |         NO  --> Use Rapid Screen (Tier 1)
  |    |
  |    NO --> Consider Rapid Screen to build ethical culture
  |
  +-- Does it affect vulnerable populations?
       |
       YES --> Use COMPREHENSIVE assessment minimum
       NO  --> Follow risk-based approach above
```

## Red Flags Checklist

Stop and escalate immediately if you see:

### Critical Red Flags
- [ ] System makes decisions about children
- [ ] Uses biometric data (facial recognition, voice, etc.)
- [ ] Criminal justice or law enforcement context
- [ ] Healthcare diagnostic or treatment decisions
- [ ] Housing or employment decisions at scale
- [ ] No human review possible
- [ ] Training data has known bias issues
- [ ] Can't explain how decisions are made
- [ ] Vulnerable populations disproportionately affected

### High-Priority Red Flags
- [ ] Demographic data used as features
- [ ] Historical data reflects discriminatory practices
- [ ] No diversity in design team
- [ ] Affected communities not consulted
- [ ] Privacy safeguards unclear
- [ ] No monitoring plan

## Essential Fairness Metrics

Choose based on your context:

| Context | Primary Metric | Why |
|---------|---------------|-----|
| Credit/lending | Equalized Odds | Legal requirement, balances opportunity and risk |
| Hiring | Equal Opportunity | Focus on not missing qualified candidates |
| Healthcare | Calibration | Predicted probabilities must be accurate |
| Resource allocation | Statistical Parity | Equal access to benefits |
| Fraud detection | Equalized Odds | Balance detection and false accusation |

## Quick Calculation

```python
# Statistical Parity Difference
positive_rate_group_a = (predictions[group_a] == 1).mean()
positive_rate_group_b = (predictions[group_b] == 1).mean()
spd = abs(positive_rate_group_a - positive_rate_group_b)
# Flag if spd > 0.1 (10%)

# Disparate Impact Ratio (80% rule)
di_ratio = min(positive_rate_group_a, positive_rate_group_b) / \
           max(positive_rate_group_a, positive_rate_group_b)
# Flag if di_ratio < 0.8
```

## Tier 1: Rapid Ethics Screen

**Time**: 15-30 minutes
**When**: Early exploration, low-risk systems, quick sanity check

### System Profile
- What decisions does this AI make?
- Who is affected by these decisions?
- What's the consequence of getting it wrong?
- Can decisions be appealed or overridden?

### Risk Level Determination
- **Low**: 0 critical flags, 0-2 high-priority flags
- **Medium**: 0 critical flags, 3+ high-priority flags
- **High**: 1+ critical flags
- **Critical**: 2+ critical flags OR severe harm possible

### Next Steps
- **Low risk**: Document and proceed with basic best practices
- **Medium+ risk**: Proceed to Tier 2 Comprehensive Assessment

## Tier 2: Comprehensive Assessment

**Time**: 2-4 hours
**When**: Moderate to high-risk systems, before production deployment

See `ASSESSMENT-TEMPLATES.md` for the full template.

### Key Sections
1. Context & Impact Analysis
2. Bias & Fairness Assessment
3. Explainability & Transparency Audit
4. Accountability & Governance
5. Privacy & Data Protection
6. Human Oversight & Control
7. Community Impact Assessment
8. Regulatory Compliance Analysis
9. Technical Safeguards
10. Deployment Decision

## Common Mistakes to Avoid

**"We're just using AI to help humans decide"**
- Still responsible for fairness. Humans often defer to AI.

**"Our data is objective"**
- All data reflects human choices and historical bias.

**"We're not using protected attributes as features"**
- Proxies exist. Zip code correlates with race. First name correlates with gender/ethnicity.

**"The model is too complex to explain"**
- Then it's too complex to deploy responsibly. Find a way.

**"We'll fix bias issues after launch"**
- Much harder and more harmful. Fix before deployment.

## Three Questions Before Any Deployment

1. **Would this be fair if used on me or my family?**
   - If not, it's not ready

2. **Can I explain and defend this system publicly?**
   - If not, more transparency needed

3. **Do I trust the oversight and accountability mechanisms?**
   - If not, strengthen governance

**If you answer "no" to any question, the system is not ready to deploy.**

## Next Steps

1. Run the 5-minute fairness test
2. Complete the red flags checklist
3. Determine your risk level
4. Use appropriate assessment template
5. Implement monitoring before deployment

## Resources

- **Full Framework**: `SKILL.md`
- **Templates**: `ASSESSMENT-TEMPLATES.md`
- **Implementation Code**: `IMPLEMENTATION-GUIDE.md`

---

**Remember**: Ethics isn't a blocker, it's a foundation for sustainable impact. Taking time to get it right protects both the people you serve and your organization's mission.
