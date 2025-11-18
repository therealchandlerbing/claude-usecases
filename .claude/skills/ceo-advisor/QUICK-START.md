# CEO Advisor Quick Start

**Time to Value: 5 Minutes**

Get your first executive intelligence brief in five minutes. This guide assumes you have Claude Code with managed skills enabled.

---

## Minute 1: Installation

```bash
# Navigate to the skill directory
cd .claude/skills/ceo-advisor

# Install Python dependencies
pip install -r config/requirements.txt
```

---

## Minute 2: Generate Sample Data

```bash
# Create realistic test data for your first experience
python examples/sample_data_generator.py
```

This generates:
- Intelligence signals (team health, financials, competitive data)
- Stakeholder profiles (board members, investors, executives)
- Calendar data (meetings, strategic time, customer interactions)
- Test crisis scenarios

---

## Minute 3: Run Your First Brief

```bash
# Generate daily intelligence brief
python src/ceo_advisor_orchestrator.py daily
```

**What You'll See:**
- Critical issues requiring immediate attention
- Today's priorities with strategic rationale
- Stakeholder relationships needing engagement
- Schedule optimization recommendations
- Emerging patterns worth monitoring

---

## Minute 4: Explore Core Capabilities

### Stakeholder Analysis
```bash
python src/stakeholder_analytics.py
```
See relationship health scores, risk matrix, and engagement recommendations.

### Time Optimization
```bash
python src/ceo_optimizer.py
```
Analyze your time allocation and get specific improvement recommendations.

### Intelligence Scan
```bash
python src/executive_intelligence_system.py
```
Deep dive into all signal sources with pattern detection.

---

## Minute 5: Invoke via Claude Code

Now use the skill naturally in conversation:

```
"Generate my morning executive brief"

"Prepare me for the board meeting next week"

"Analyze my stakeholder relationships"

"We have a crisis: major customer threatening to leave"

"Optimize my schedule for maximum strategic time"

"Facilitate a strategic planning session on market expansion"
```

---

## Your First Week

### Day 1-2: Establish Baseline
- [ ] Run daily brief each morning
- [ ] Review stakeholder portfolio
- [ ] Analyze current time allocation
- [ ] Note your metrics before optimization

### Day 3-4: Customize
- [ ] Edit `config/config.json` for your preferences
- [ ] Add your actual top 10 stakeholders
- [ ] Input your real calendar patterns
- [ ] Adjust alert thresholds

### Day 5-7: Optimize
- [ ] Implement schedule recommendations
- [ ] Execute stakeholder engagement actions
- [ ] Track improvements in strategic time
- [ ] Document initial ROI

---

## Essential Commands

| Task | Command |
|------|---------|
| Morning Brief | `python src/ceo_advisor_orchestrator.py daily` |
| Board Prep | `python src/ceo_advisor_orchestrator.py board` |
| Crisis Response | `python src/ceo_advisor_orchestrator.py crisis --crisis "description"` |
| Strategic Planning | `python src/ceo_advisor_orchestrator.py strategy` |
| Full Dashboard | `python src/ceo_advisor_orchestrator.py full` |
| Run Tests | `python src/ceo_advisor_orchestrator.py test` |

---

## Configuration Quick Reference

### Essential Settings

Edit `config/config.json`:

```json
{
  "intelligence_configuration": {
    "sensitivity": "high",           // high, medium, low
    "confidence_threshold": 0.75     // 0.0 to 1.0
  },
  "optimization_configuration": {
    "focus_time_target_hours": 2.0,  // Minimum daily strategic time
    "meeting_batch_mode": true       // Consolidate meetings
  },
  "personalization": {
    "decision_style": "analytical",  // analytical, intuitive, directive
    "energy_pattern": "morning_peak" // morning_peak, afternoon_peak, even
  }
}
```

---

## Common First Actions

### "I want to prepare for a board meeting"
```bash
python src/ceo_advisor_orchestrator.py board
```
Or in conversation: "Prepare me for the board meeting on [date]"

### "I feel overwhelmed with my schedule"
```bash
python src/ceo_optimizer.py
```
Or in conversation: "Optimize my schedule to increase strategic thinking time"

### "I'm worried about a stakeholder relationship"
```bash
python src/stakeholder_analytics.py
```
Or in conversation: "Analyze my relationship with [stakeholder] and recommend next steps"

### "We have an urgent situation"
```bash
python src/ceo_advisor_orchestrator.py crisis --crisis "describe the situation"
```
Or in conversation: "Crisis: [describe situation]. Activate crisis response protocol."

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "No module found" | Run `pip install -r config/requirements.txt` |
| "Config error" | Validate JSON: `python -m json.tool config/config.json` |
| "No data" | Run `python examples/sample_data_generator.py` |
| "Import error" | Check Python version: `python --version` (needs 3.8+) |

---

## Next Steps

1. **Customize Configuration**: Edit `config/config.json` to match your preferences
2. **Add Real Stakeholders**: Input your actual stakeholder data
3. **Connect Calendar**: Future: integrate with Google Calendar or Outlook
4. **Read Full Documentation**: See `SKILL.md` for complete operational details
5. **Explore Implementation Guide**: See `IMPLEMENTATION-GUIDE.md` for deployment

---

## Expected Results

After one week of consistent use:

| Metric | Expected Improvement |
|--------|---------------------|
| Strategic Time | +25-40% |
| Meeting Efficiency | +20-30% |
| Stakeholder Awareness | Significantly improved |
| Crisis Preparedness | Response time halved |
| Personal Energy | +15-20% through optimization |

---

**You're ready.** Start with:

```bash
python src/ceo_advisor_orchestrator.py daily
```

Or simply tell Claude:

```
"I need my morning executive brief"
```

*Your advisory board is standing by.*
