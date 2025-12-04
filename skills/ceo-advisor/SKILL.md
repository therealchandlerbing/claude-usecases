---
name: ceo-advisor
description: Routes to the managed CEO Advisor skill. Use `.claude/skills/ceo-advisor/` for the full implementation.
version: 2.0.0
author: 360 Social Impact Studios
created: 2024-09-01
updated: 2025-12-04
category: executive-leadership
complexity: high
tags: [ceo, executive, intelligence, stakeholder-analytics, optimization]
dependencies:
  - CEO Advisor skill (.claude/skills/ceo-advisor/)
---

# CEO Advisor

## This Skill Has Been Consolidated

**CEO Advisor** is now available in the **managed skills location** with full implementation.

**Use this instead:** `.claude/skills/ceo-advisor/`

---

## Why the Consolidation?

The managed location (`.claude/skills/ceo-advisor/`) is the canonical source that includes:

- **Executive Intelligence System** - Real-time intelligence aggregation and alerts
- **Stakeholder Analytics** - Relationship tracking and sentiment analysis
- **CEO Time & Energy Optimization** - Personal effectiveness maximization
- **Strategy Advisor** - Strategic planning and competitive analysis
- **Financial Advisor** - Scenario modeling and financial oversight
- **Full documentation** - INDEX.md, IMPLEMENTATION-GUIDE.md, templates

**Result:** Single source of truth for the CEO Advisor capabilities.

---

## How to Use CEO Advisor

### Quick Request Format

Instead of referencing `skills/ceo-advisor/`, use:

```
"Use the CEO advisor to generate a daily intelligence brief"
```

Or explicitly:

```
"Using .claude/skills/ceo-advisor, prepare for my board meeting next week"
```

### Common Commands

1. **Daily Intelligence Brief**
   ```
   "Generate a CEO morning intelligence brief"
   ```

2. **Board Meeting Prep**
   ```
   "Prepare comprehensive board meeting materials"
   ```

3. **Stakeholder Analysis**
   ```
   "Analyze my stakeholder relationships and identify at-risk relationships"
   ```

4. **Time Optimization**
   ```
   "Optimize my schedule for the coming week"
   ```

5. **Strategic Planning**
   ```
   "Run a strategic position assessment for Q1 planning"
   ```

---

## Managed Skill Location

**Canonical Path:** `.claude/skills/ceo-advisor/`

### Key Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Complete operational instructions |
| `INDEX.md` | Navigation and file inventory |
| `IMPLEMENTATION-GUIDE.md` | Setup and deployment guide |
| `README.md` | User documentation |
| `QUICK-START.md` | 5-minute getting started |
| `src/ceo_advisor_orchestrator.py` | Main integration hub |
| `src/executive_intelligence_system.py` | Intelligence system |
| `src/stakeholder_analytics.py` | Relationship analytics |
| `src/ceo_optimizer.py` | Time/energy optimization |
| `src/strategy_advisor.py` | Strategic analysis |
| `src/financial_advisor.py` | Financial modeling |

---

## Migration Note

If you have custom configurations or extensions built on `skills/ceo-advisor/`:

1. Review `.claude/skills/ceo-advisor/config/config.json` for new options
2. Move any custom scripts to work with the managed location
3. Update any import paths from `skills/ceo-advisor/src/` to `.claude/skills/ceo-advisor/src/`

The managed version is a superset of the user version with additional advisors (Strategy, Financial) and comprehensive documentation.

---

## Version History

- **v2.0.0** (2025-12-04) - Consolidated to managed skills location
- **v1.0.0** - Original user-location implementation

---

*For the full CEO Advisor experience, see `.claude/skills/ceo-advisor/SKILL.md`*
