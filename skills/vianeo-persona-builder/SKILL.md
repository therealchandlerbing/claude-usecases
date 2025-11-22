---
name: Vianeo Persona Builder
description: Generate validated stakeholder personas using the Vianeo Business Validation framework. This skill routes to Strategic Persona Builder with Vianeo framework support. Produces evidence-backed personas for partners, innovators, stakeholders, and beneficiaries with dual outputs (strategic + platform-ready).
version: 1.0.0
author: 360 Social Impact Studios
created: 2024-09-20
updated: 2025-11-22
category: research-validation
complexity: medium
tags: [personas, vianeo, stakeholder-research, validation, evidence-based, four-layer-framework]
dependencies:
  - Strategic Persona Builder skill (.claude/skills/strategic-persona-builder/)
outputs:
  - Vianeo four-layer personas (strategic version)
  - Platform-ready personas (character limits enforced)
  - Evidence appendices with source quotes
  - Quality scoring (1-5 scale)
---

# Vianeo Persona Builder

## ⚠️ Important Notice: This Skill Has Been Consolidated

**Vianeo Persona Builder** has been integrated into the **Strategic Persona Builder** skill, which now supports multiple frameworks including Vianeo as its primary framework.

**Use this instead:** `.claude/skills/strategic-persona-builder/`

---

## Why the Consolidation?

The Strategic Persona Builder is a superset that includes:
- **Vianeo four-layer framework** (same as this skill)
- **Jobs-to-be-Done framework** (additional capability)
- **Empathy mapping framework** (additional capability)
- **Five persona types** (vs. four in Vianeo-only version)
- **Same quality standards** (evidence tracking, validation scoring)
- **Same dual outputs** (strategic + platform-ready)

**Result:** One comprehensive skill instead of multiple overlapping persona tools.

---

## How to Use Vianeo Framework with Strategic Persona Builder

### Quick Request Format

Instead of:
```
"Use vianeo-persona-builder to create partner personas from these interviews"
```

Say:
```
"Use strategic-persona-builder with Vianeo framework to create partner personas from these interviews"
```

Or simply:
```
"Build Vianeo personas from this research data"
```

(Strategic Persona Builder recognizes "Vianeo" and automatically uses the four-layer framework)

---

## What You Get (Same as Before)

### Vianeo Four-Layer Structure

**Layer 1: Requester**
- Who they are (demographics, motivations, values)
- Psychographic profile
- Decision-making authority

**Layer 2: Field of Application**
- Their world (thinks/feels, observes, does, others say)
- Environmental context
- Behavioral patterns

**Layer 3: Activities and Challenges**
- What they do and struggle with
- Tasks, pains, expectations
- Unmet needs

**Layer 4: Current Solutions**
- Their present reality
- Workarounds, makeshift solutions
- Gaps in current approaches

### Dual Outputs

**Strategic Version:**
- Comprehensive four-layer analysis
- Evidence appendix with source quotes
- Quality score (1-5) with justification
- Recommendations for improvement

**Platform-Ready Version:**
- Character limits enforced for Vianeo platform
- Condensed but complete
- Ready to paste into Vianeo system

---

## Supported Persona Types

Same four types as before:
1. **Partners** - Organizations or individuals collaborating with 360
2. **Innovators** - Technology creators, entrepreneurs, researchers
3. **Stakeholders** - Decision-makers, influencers, users
4. **Beneficiaries** - End users, impact recipients

**Plus one additional type** in Strategic Persona Builder:
5. **Customers** - Buyers, procurement decision-makers

---

## Quick Start Guide

### Step 1: Gather Research Data

Same requirements as before:
- Interview transcripts or survey responses
- Meeting notes or observation documents
- Behavioral data or project documentation
- Uploaded research files

### Step 2: Invoke Strategic Persona Builder

**Three ways to request:**

1. **Explicit framework:**
```
"Use strategic-persona-builder with Vianeo framework to build partner personas from these 8 interviews"
```

2. **Implicit (mention Vianeo):**
```
"Build Vianeo personas for these stakeholders"
```

3. **Default behavior:**
```
"Create partner personas for technology validation project"
```
(Strategic Persona Builder uses Vianeo as default framework for validation projects)

### Step 3: Review Output

You'll receive:
- 3-5 distinct Vianeo personas (four-layer structure)
- Evidence appendix with quotes and source attribution
- Quality score (1-5) with gaps identified
- Platform-ready version (character limits enforced)
- Recommendations to reach higher quality score

**Exactly the same output as the original Vianeo Persona Builder!**

---

## Migration Benefits

### What You Gain

✅ **Additional frameworks** - Can use JTBD or empathy mapping if Vianeo isn't the best fit
✅ **Better maintenance** - One skill to update instead of multiple
✅ **Comprehensive documentation** - Strategic Persona Builder has extensive references
✅ **More persona types** - Can create customer personas in addition to Vianeo's four
✅ **Same quality standards** - Evidence tracking and validation scoring preserved

### What Stays the Same

✅ **Vianeo four-layer framework** - Identical structure
✅ **Dual outputs** - Strategic + platform-ready
✅ **Evidence tracking** - Every claim sourced
✅ **Quality scoring** - 1-5 scale with improvement pathways
✅ **Validation modes** - Validated, inferred, hybrid

---

## Common Questions

**Q: Will my existing Vianeo personas still work?**
A: Yes! The format and structure are identical. Strategic Persona Builder uses the same Vianeo four-layer framework.

**Q: Do I need to learn a new skill?**
A: No. Just mention "Vianeo" in your request and Strategic Persona Builder automatically uses the Vianeo framework.

**Q: Can I still get platform-ready output?**
A: Yes. Strategic Persona Builder produces the same dual outputs (strategic + platform-ready with character limits).

**Q: What if I ONLY want Vianeo framework?**
A: Simply request "Vianeo personas" and Strategic Persona Builder will use only the Vianeo framework.

**Q: Is the quality the same?**
A: Yes. Same evidence tracking, same quality scoring (1-5), same validation standards.

---

## Quick Reference: Strategic Persona Builder Location

**Managed Skill Location:**
`.claude/skills/strategic-persona-builder/`

**Key Files:**
- `SKILL.md` - Complete operational specification
- `QUICK-START.md` - 5-minute quick reference
- `README.md` - Overview and use cases
- `references/vianeo-framework-guide.md` - Vianeo-specific documentation
- `references/framework-comparison.md` - When to use which framework

---

## Example Requests

### Before (Vianeo Persona Builder)
```
"Use vianeo-persona-builder to create partner personas from these university collaboration interviews"
```

### After (Strategic Persona Builder)
```
"Build Vianeo partner personas from these university collaboration interviews"
```

**Result:** Identical output, more flexible skill.

---

## Supporting Documentation

### In Strategic Persona Builder

**Vianeo-specific:**
- `references/vianeo-framework-guide.md` - Complete Vianeo documentation
- `references/vianeo-platform-guide.md` - Platform character limits and formatting
- `examples/vianeo-partner-example.md` - Gold standard partner persona
- `examples/vianeo-beneficiary-example.md` - Gold standard beneficiary persona

**General:**
- `QUICK-START.md` - Fast reference (5 min)
- `SKILL.md` - Complete operational specification
- `README.md` - Overview and use cases

---

## Troubleshooting

**"I want ONLY Vianeo, not other frameworks"**
→ Mention "Vianeo" in your request
→ Strategic Persona Builder will use only Vianeo framework

**"Output format looks different"**
→ It shouldn't - Vianeo four-layer structure is identical
→ If you see differences, it may be improvements or bug fixes
→ Report discrepancies for review

**"I can't find my old Vianeo persona files"**
→ Check `skills/vianeo-persona-builder/examples/` directory
→ All examples have been preserved
→ Reference files migrated to `.claude/skills/strategic-persona-builder/references/`

**"Do I need to update my workflows?"**
→ Not immediately - this routing skill ensures continuity
→ Over time, transition to "strategic-persona-builder" requests
→ Both approaches work during transition period

---

## Version History

- **v1.0.0** (2025-11-22) - Consolidation routing to Strategic Persona Builder
  - Vianeo framework fully supported in Strategic Persona Builder
  - Identical output quality and format
  - This skill now serves as routing documentation

- **Previous versions** - See git history in `skills/vianeo-persona-builder/`

---

## Next Steps

1. ✅ **Read Strategic Persona Builder docs**: `.claude/skills/strategic-persona-builder/QUICK-START.md`
2. ✅ **Try a Vianeo persona request**: "Build Vianeo personas from [your research data]"
3. ✅ **Compare output**: Same four-layer structure, same quality
4. ✅ **Explore other frameworks**: Try JTBD or empathy mapping if relevant

---

**For Vianeo persona work, use:** `.claude/skills/strategic-persona-builder/`

**This routing documentation ensures continuity during the transition to consolidated skills.**

Version 1.0.0 | Updated: 2025-11-22 | 360 Social Impact Studios
