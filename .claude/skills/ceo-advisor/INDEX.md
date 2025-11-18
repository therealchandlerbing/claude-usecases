# CEO Advisor - Navigation Index

Quick reference for navigating the CEO Advisor skill documentation and capabilities.

---

## Document Map

| Document | Purpose | When to Use |
|----------|---------|-------------|
| [README.md](./README.md) | Overview & value proposition | First visit, evaluating the skill |
| [QUICK-START.md](./QUICK-START.md) | 5-minute onboarding | Getting started immediately |
| [SKILL.md](./SKILL.md) | Complete operational spec | Deep understanding, Claude execution |
| [IMPLEMENTATION-GUIDE.md](./IMPLEMENTATION-GUIDE.md) | Deployment & integration | Technical setup, enterprise deployment |
| **INDEX.md** | Navigation & quick reference | Finding specific information quickly |

---

## The Five Experts - Quick Reference

### Chief Intelligence Officer
**Focus**: Real-time signal detection and early warnings
**Triggers**: "morning brief", "what should I know", "critical issues", "intelligence scan"
**Module**: `src/executive_intelligence_system.py`

### Chief Relationship Officer
**Focus**: Stakeholder analytics and relationship health
**Triggers**: "stakeholder analysis", "board prep", "relationship health", "who needs attention"
**Module**: `src/stakeholder_analytics.py`

### Chief Performance Officer
**Focus**: Time and energy optimization
**Triggers**: "optimize schedule", "time allocation", "energy management", "what to delegate"
**Module**: `src/ceo_optimizer.py`

### Chief Strategy Officer
**Focus**: Strategic analysis and scenario planning
**Triggers**: "strategic planning", "evaluate opportunity", "scenario analysis", "competitive assessment"
**Module**: Integrated in orchestrator

### Chief Financial Officer
**Focus**: Financial health and resource allocation
**Triggers**: "financial health", "resource allocation", "investment evaluation", "cash flow"
**Module**: Integrated in orchestrator

---

## Command Reference

### Primary Commands

```bash
# Daily intelligence brief
python src/ceo_advisor_orchestrator.py daily

# Board meeting preparation
python src/ceo_advisor_orchestrator.py board

# Crisis response protocol
python src/ceo_advisor_orchestrator.py crisis --crisis "description"

# Strategic planning session
python src/ceo_advisor_orchestrator.py strategy

# Comprehensive dashboard
python src/ceo_advisor_orchestrator.py full

# System test
python src/ceo_advisor_orchestrator.py test
```

### Individual Modules

```bash
# Intelligence scan
python src/executive_intelligence_system.py

# Stakeholder analysis
python src/stakeholder_analytics.py

# Time/energy optimization
python src/ceo_optimizer.py

# Generate sample data
python examples/sample_data_generator.py
```

---

## Priority Indicators

| Indicator | Meaning | Response Time |
|-----------|---------|---------------|
| 🚨 CRITICAL | Immediate executive action | Within 2 hours |
| ⚠️ HIGH | Requires attention today | Within 24 hours |
| 📋 STANDARD | Next planning cycle | Within 1 week |
| 💡 OPPORTUNITY | Potential upside | Consider soon |
| ℹ️ INFO | Awareness only | No action needed |

---

## Configuration Quick Reference

### Key Settings in `config/config.json`

**Intelligence Settings**
- `sensitivity`: high / medium / low
- `confidence_threshold`: 0.0 to 1.0
- `scan_frequency`: real-time / hourly / daily

**Optimization Settings**
- `focus_time_target_hours`: Minimum strategic hours (default: 2.0)
- `meeting_batch_mode`: true / false
- `energy_profile.peak_hours`: Best cognitive hours

**Personalization**
- `decision_style`: analytical / intuitive / directive / collaborative
- `communication_preference`: concise / narrative / visual / detailed
- `risk_tolerance`: conservative / moderate / aggressive
- `energy_pattern`: morning_peak / afternoon_peak / even / night_owl

---

## Stakeholder Categories & Weights

| Category | Weight | Engagement Target |
|----------|--------|-------------------|
| Board | 1.0 | Every 7-14 days |
| Investor | 0.9 | Every 14-30 days |
| Executive | 0.85 | Every 3-7 days |
| Customer | 0.8 | Every 14-30 days |
| Employee | 0.7 | Every 7-14 days |
| Partner | 0.65 | Every 14-30 days |

---

## Communication Styles

| Style | Characteristics | Approach |
|-------|-----------------|----------|
| ANALYTICAL | Data-driven, thorough | Lead with facts, detailed analysis |
| DRIVER | Results-focused, direct | Get to the point, focus on outcomes |
| EXPRESSIVE | Vision-oriented, creative | Big picture, exploration |
| AMIABLE | Relationship-focused, patient | Build rapport, show appreciation |

---

## Time Allocation Benchmarks

| Category | Target | Range | Description |
|----------|--------|-------|-------------|
| Strategic Thinking | 25% | 20-30% | Vision, planning |
| Team Leadership | 20% | 15-25% | 1:1s, coaching |
| External Engagement | 20% | 15-25% | Investors, partners |
| Operational Oversight | 15% | 10-20% | Reviews, approvals |
| Customer Interaction | 10% | 5-15% | Direct engagement |
| Personal Development | 10% | 5-15% | Learning, health |

---

## Energy Cost Reference

| Activity | Cost | Best Time |
|----------|------|-----------|
| Board Meeting | 90/100 | Peak only |
| Strategy Session | 85/100 | Peak only |
| Conflict Resolution | 80/100 | Morning |
| Investor Pitch | 75/100 | Peak |
| All-Hands | 70/100 | Mid-morning |
| Executive Meeting | 65/100 | AM/Early PM |
| 1:1 Meeting | 60/100 | Flexible |
| Customer Meeting | 55/100 | AM/Early PM |
| Team Meeting | 50/100 | Any |
| Planning | 40/100 | Peak |
| Email | 30/100 | Off-peak |

---

## File Structure

```
ceo-advisor/
├── README.md                          # Entry point
├── SKILL.md                           # Operational spec
├── QUICK-START.md                     # 5-min onboarding
├── IMPLEMENTATION-GUIDE.md            # Deployment guide
├── INDEX.md                           # This file
├── src/
│   ├── ceo_advisor_orchestrator.py    # Main hub
│   ├── executive_intelligence_system.py
│   ├── stakeholder_analytics.py
│   └── ceo_optimizer.py
├── config/
│   ├── config.json                    # System configuration
│   └── requirements.txt               # Dependencies
├── examples/
│   ├── sample_data_generator.py       # Test data
│   └── scenarios/                     # Example scenarios
├── templates/
│   └── frameworks/                    # Executive frameworks
├── references/
│   └── strategic-frameworks/          # Best practices
└── docs/
    └── prompt_templates.md            # AI interaction patterns
```

---

## Troubleshooting Quick Reference

| Issue | Solution |
|-------|----------|
| No module found | `pip install -r config/requirements.txt` |
| Config error | `python -m json.tool config/config.json` |
| No data | `python examples/sample_data_generator.py` |
| Import error | Check Python 3.8+ installed |
| Permission denied | Check file permissions |

---

## Success Metrics Targets

| Category | Metric | Target |
|----------|--------|--------|
| Time | Strategic allocation | 25% |
| Time | Meeting efficiency | 85% |
| Decisions | Quality score | 90% |
| Decisions | Speed | <24 hours |
| Relationships | Satisfaction | >80 |
| Relationships | At-risk | <10% |
| Energy | Peak utilization | >80% |
| Energy | Burnout risk | <20% |

---

## Version Information

**Current Version**: 2.0.0 - Team of Experts Architecture

**Key Features**:
- Five integrated AI expert advisors
- Real-Time Executive Intelligence System
- Stakeholder Sentiment Analytics
- CEO Time & Energy Optimization
- Strategic Analysis & Scenario Modeling
- Financial Health & Resource Allocation

**Next Version**: 3.0.0 - Connected Intelligence (Live integrations)

---

## Quick Invocations

### Via Command Line
```bash
python src/ceo_advisor_orchestrator.py daily
```

### Via Claude Code
```
"I need CEO advisory support"
"Generate my morning brief"
"Prepare me for the board meeting"
"Optimize my schedule"
"Crisis: [describe situation]"
```

---

*Find what you need fast. Your advisory board is ready.*
