# CEO Advisor - 5 Minute Quickstart

Get up and running with the CEO Advisor in 5 minutes.

## Step 1: Installation (1 minute)

```bash
# Navigate to CEO advisor directory
cd skills/ceo-advisor

# Install dependencies
pip install -r config/requirements.txt
```

## Step 2: First Intelligence Brief (1 minute)

```bash
# Generate your first daily intelligence brief
python src/ceo_advisor_orchestrator.py daily
```

You'll see output like:
```
====================================
GENERATING DAILY INTELLIGENCE BRIEF
====================================

1. Running Intelligence Scan...
2. Analyzing Stakeholder Relationships...
3. Optimizing Today's Schedule...
4. Generating Strategic Insights...
5. Prioritizing Action Items...

CEO ADVISOR - EXECUTIVE SUMMARY
====================================

SUMMARY: 1 critical items requiring immediate attention.
2 stakeholder engagements needed. 5 total action items prioritized.
Schedule optimized for peak performance.

TOP PRIORITY ACTIONS:
1. Schedule 1-on-1 with CTO within 24 hours [Critical]
   Deadline: 24 hours

CRITICAL ITEMS:
• Team health score declining in Engineering
  → Schedule 1-on-1 with CTO within 24 hours
```

## Step 3: Analyze Stakeholders (1 minute)

```bash
# Run stakeholder analysis
python src/stakeholder_analytics.py
```

Output:
```
STAKEHOLDER RELATIONSHIP ANALYTICS REPORT
==========================================

PORTFOLIO HEALTH: 72.5/100
Grade: B (Good)

🔴 HIGH RISK (High Influence, Low Satisfaction):
  • Sarah Johnson: URGENT: Repair immediately

PRIORITY ENGAGEMENTS:
  John Smith (HIGH urgency)
    • Days overdue: 1
    • Action: Schedule urgent 1-on-1 to address concerns
```

## Step 4: Optimize Your Time (1 minute)

```bash
# Run time & energy optimization
python src/ceo_optimizer.py
```

Output:
```
CEO TIME & ENERGY OPTIMIZATION REPORT
======================================

TIME ALLOCATION ANALYSIS:

  strategic_thinking: 15.0% (Under-allocated (target: 25%))
  operational_oversight: 25.0% (Over-allocated (target: 15%))

CRITICAL GAPS:
  strategic_thinking: -10.0% gap
    → Block 2-3 hour sessions for deep strategic work

FOCUS TIME:
  Total: 3.0 hours
  Increase focus time to 2-3 hours daily
```

## Step 5: Run Full Dashboard (1 minute)

```bash
# Generate comprehensive CEO dashboard
python src/ceo_advisor_orchestrator.py full
```

This runs all modules and provides integrated insights.

## Next Steps

### Customize Configuration

Edit `config/config.json`:

```json
{
  "intelligence_configuration": {
    "sensitivity": "high",
    "confidence_threshold": 0.75
  },
  "optimization_configuration": {
    "focus_time_target_hours": 2.0
  }
}
```

### Add Real Stakeholders

Create a stakeholder data file or modify the sample data in the Python files.

### Schedule Daily Briefs

Add to your crontab (Linux/Mac):
```bash
# Run daily at 6 AM
0 6 * * * cd /path/to/ceo-advisor && python src/ceo_advisor_orchestrator.py daily > daily_brief.txt
```

Or use Task Scheduler (Windows).

### Integrate Calendar

Install calendar integration dependencies:
```bash
pip install google-auth google-auth-oauthlib google-api-python-client
```

### Test All Modules

```bash
# Run comprehensive test
python src/ceo_advisor_orchestrator.py test
```

## Common Commands

| Command | Purpose |
|---------|---------|
| `python src/ceo_advisor_orchestrator.py daily` | Daily intelligence brief |
| `python src/ceo_advisor_orchestrator.py board` | Board meeting prep |
| `python src/ceo_advisor_orchestrator.py crisis --crisis "description"` | Crisis response |
| `python src/ceo_advisor_orchestrator.py strategy` | Strategic planning |
| `python src/ceo_advisor_orchestrator.py full` | Full dashboard |

## Tips for Success

1. **Start Small**: Use daily briefs for one week before expanding
2. **Customize**: Adjust thresholds in config.json to match your context
3. **Track Progress**: Document initial metrics to measure improvement
4. **Iterate**: Refine based on what's most valuable to you
5. **Integrate**: Connect real data sources as you see value

## Getting Help

- See `README.md` for comprehensive documentation
- See `SKILL.md` for detailed capability reference
- Run commands with `--help` for options
- Check `config/config.json` for all settings

## Success Checklist

After 5 minutes, you should have:
- [ ] Installed dependencies
- [ ] Run daily intelligence brief
- [ ] Analyzed stakeholder portfolio
- [ ] Optimized time allocation
- [ ] Reviewed comprehensive dashboard

**You're ready!** Start transforming your leadership from reactive to predictive.

---

*Next: Read the full README.md for advanced features and customization.*
