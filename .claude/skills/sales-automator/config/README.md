# Sales Automator Configuration

This directory contains configuration files for customizing the Sales Automator skill.

## Available Configurations

### 1. [pipeline-config.yaml](pipeline-config.yaml)
Main configuration file for pipeline management, email sequences, and performance benchmarks.

**Key Sections**:
- **Pipeline Settings**: Deal stages, thresholds, custom fields
- **Sequence Configuration**: Email cadences for different campaign types
- **Performance Benchmarks**: Target metrics for email and pipeline performance
- **Alerts**: Notification settings for stuck deals and pipeline health
- **Integrations**: Asana, Gmail, Drive, Calendar settings

---

## How to Use Configurations

### Default Settings
The Sales Automator skill works out-of-the-box with sensible defaults. You don't need to modify configurations unless you want to customize behavior.

### Customizing Settings

**Step 1: Copy Configuration File**
```bash
cp config/pipeline-config.yaml config/my-pipeline-config.yaml
```

**Step 2: Edit Settings**
Open `my-pipeline-config.yaml` and modify values:
```yaml
pipeline:
  stuck_deal_thresholds:
    discovery: 7   # Change from 14 to 7 days
    proposal: 21   # Change from 30 to 21 days
```

**Step 3: Reference in Claude**
Tell Claude to use your custom configuration:
```
"Use my-pipeline-config.yaml for pipeline thresholds"
```

---

## Configuration Reference

### Pipeline Settings

#### Deal Stages
Define the stages deals move through in your sales process.

**Default Stages**:
- Outreach (21 days)
- Discovery (14 days)
- Proposal (30 days)
- Negotiation (21 days)
- Closed-Won
- Closed-Lost

**Customization Example**:
```yaml
stages:
  - name: "Prospecting"
    duration_threshold_days: 14
    conversion_probability: 0.05
```

#### Stuck Deal Thresholds
Define when a deal is considered "stuck" in each stage.

**Default Thresholds**:
- Outreach: 21 days
- Discovery: 14 days
- Proposal: 30 days
- Negotiation: 21 days

**When to Adjust**:
- Shorter sales cycles: Reduce thresholds
- Enterprise sales: Increase thresholds
- Seasonal business: Adjust by quarter

#### Custom Fields
Configure required and optional fields for deal tracking.

**Required Fields**:
- Deal Stage
- Deal Value
- Close Date
- Lead Source
- Next Action

**Optional Fields**:
- Lead Score
- Primary Contact
- Company Size
- Industry
- Competitor

---

### Email Sequence Settings

#### Sequence Types

**Cold Outreach** (5 touches, 21 days):
```yaml
cold_outreach:
  touch_count: 5
  duration_days: 21
  cadence:
    - day: 0
    - day: 3
    - day: 7
    - day: 14
    - day: 21
```

**Warm Follow-Up** (3 touches, 14 days):
```yaml
warm_followup:
  touch_count: 3
  duration_days: 14
  cadence:
    - day: 0
    - day: 5
    - day: 10
```

**Customization Examples**:

*Shorter Cold Sequence*:
```yaml
cold_outreach:
  touch_count: 3
  duration_days: 14
  cadence:
    - day: 0
    - day: 5
    - day: 10
```

*More Aggressive Follow-Up*:
```yaml
warm_followup:
  touch_count: 4
  duration_days: 10
  cadence:
    - day: 0
    - day: 2
    - day: 5
    - day: 8
```

---

### Performance Benchmarks

#### Email Performance Targets

**Cold Outreach**:
- Open Rate (Good): 45%
- Open Rate (Average): 30%
- Response Rate (Good): 10%
- Response Rate (Average): 5%

**Warm Outreach**:
- Open Rate (Good): 70%
- Open Rate (Average): 50%
- Response Rate (Good): 30%
- Response Rate (Average): 15%

**When to Adjust**:
- Industry norms differ (B2B SaaS vs. Consulting)
- Your historical performance varies
- Geographic differences (US vs. Brazil)

#### Pipeline Conversion Targets

**Stage-to-Stage Conversion**:
- Outreach → Discovery: 12%
- Discovery → Proposal: 35%
- Proposal → Negotiation: 55%
- Negotiation → Closed-Won: 75%

**Deal Velocity Targets**:
- Outreach: 18 days
- Discovery: 10 days
- Proposal: 25 days
- Negotiation: 14 days
- Total Sales Cycle: 75 days

---

### Alert Settings

#### Stuck Deal Alerts
Automatically identify deals exceeding stage thresholds.

**Default Settings**:
```yaml
stuck_deals:
  enabled: true
  check_frequency: "daily"
  notification_method: "asana_comment"
```

**Customization**:
```yaml
stuck_deals:
  enabled: true
  check_frequency: "weekly"
  notification_method: "email"
  notification_day: "friday"
```

#### Pipeline Health Alerts
Monitor overall pipeline health and coverage.

**Default Settings**:
```yaml
pipeline_health:
  enabled: true
  check_frequency: "weekly"
  notification_day: "monday"
```

**Metrics Monitored**:
- Pipeline coverage (total value / quota)
- Stage distribution
- Weighted pipeline value
- Win rate trends

---

### Integration Settings

#### Asana Configuration
```yaml
asana:
  workspace: "primary"
  project: "Sales Pipeline"
  create_subtasks: true
  add_followers: true
```

**Customization**:
- Change project name if not "Sales Pipeline"
- Disable subtask creation if you prefer manual control
- Configure default followers for new deals

#### Gmail Configuration
```yaml
gmail:
  search_history_days: 365
  label_prefix: "Sales/"
```

**Customization**:
- Extend search history for longer relationship tracking
- Change label prefix to match your organization system

#### Drive Configuration
```yaml
drive:
  assets_folder: "Sales Assets"
  subfolder_structure:
    - "Case Studies"
    - "Proposals"
    - "Testimonials"
```

**Customization**:
- Change folder name if different
- Add/remove subfolders based on your structure
- Specify naming conventions for files

#### Calendar Configuration
```yaml
calendar:
  search_history_days: 180
  event_prefix: "Sales:"
```

**Customization**:
- Adjust search history based on typical deal cycles
- Change event prefix to match your naming convention

---

## Configuration Best Practices

### 1. Start with Defaults
Don't customize until you've used the skill with default settings. Learn what works before changing.

### 2. Test Changes Incrementally
Change one setting at a time, test, measure impact, then adjust next setting.

### 3. Document Custom Settings
When you customize, add comments explaining why:
```yaml
pipeline:
  stuck_deal_thresholds:
    proposal: 45  # Extended to 45 days for enterprise deals (avg cycle time)
```

### 4. Version Control
If you make multiple custom configs, version them:
- `pipeline-config-v1.yaml` (original)
- `pipeline-config-v2-short-cycles.yaml` (for fast-moving deals)
- `pipeline-config-v3-enterprise.yaml` (for long-cycle enterprise sales)

### 5. Share Across Team
If multiple people use Sales Automator, agree on standard configurations and share them.

---

## Common Customization Scenarios

### Scenario 1: Shorter Sales Cycles (SMB Focus)

**Problem**: Default thresholds too long for fast-moving SMB deals

**Solution**: Reduce stage durations
```yaml
stuck_deal_thresholds:
  outreach: 10
  discovery: 7
  proposal: 14
  negotiation: 10
```

---

### Scenario 2: Enterprise Sales (Long Cycles)

**Problem**: Deals get flagged as stuck when they're just slow-moving enterprise sales

**Solution**: Increase stage durations
```yaml
stuck_deal_thresholds:
  outreach: 30
  discovery: 21
  proposal: 60
  negotiation: 45
```

---

### Scenario 3: High-Volume Outreach

**Problem**: Need to contact more prospects, willing to sacrifice some personalization

**Solution**: Shorten sequences, faster cadence
```yaml
cold_outreach:
  touch_count: 3
  duration_days: 10
  cadence:
    - day: 0
    - day: 3
    - day: 7
```

---

### Scenario 4: International Sales

**Problem**: Different response patterns and timelines for international prospects

**Solution**: Create region-specific configs
```yaml
# pipeline-config-brazil.yaml
sequences:
  cold_outreach:
    touch_count: 5
    duration_days: 30  # Longer decision cycles
    cadence:
      - day: 0
      - day: 5
      - day: 12
      - day: 20
      - day: 28
```

---

### Scenario 5: Multi-Product Sales

**Problem**: Different products have different sales cycles and deal sizes

**Solution**: Create product-specific configs
```yaml
# pipeline-config-consulting.yaml
pipeline:
  deal_value_ranges:
    tier_1: [10000, 50000]
    tier_2: [50000, 150000]
    tier_3: [150000, 500000]

# pipeline-config-saas.yaml
pipeline:
  deal_value_ranges:
    starter: [5000, 15000]
    professional: [15000, 50000]
    enterprise: [50000, 200000]
```

---

## Troubleshooting Configuration Issues

### Issue: Claude Not Using Custom Config

**Diagnosis**: Configuration file not referenced correctly

**Solution**:
1. Verify file name and location
2. Explicitly tell Claude: "Use pipeline-config-v2.yaml for this campaign"
3. Check YAML syntax is valid: `python -m yaml pipeline-config.yaml`

### Issue: Thresholds Not Working as Expected

**Diagnosis**: Deals not being flagged as stuck despite exceeding thresholds

**Solution**:
1. Verify deal has due date set in Asana
2. Check that Deal Stage custom field is populated
3. Ensure stage name matches exactly (case-sensitive)

### Issue: Email Sequences Wrong Cadence

**Diagnosis**: Emails sent on wrong days

**Solution**:
1. Check cadence days are cumulative from Day 0 (not intervals)
2. Verify sequence type matches (cold vs. warm vs. stuck)
3. Confirm subtasks in Asana have correct due dates

---

## Questions?

If you have questions about configurations:

1. Review default settings in `pipeline-config.yaml`
2. Check examples in this README
3. Ask Claude: "Help me configure [specific setting] for [use case]"
4. Reference main [SKILL.md](../SKILL.md) for workflow details

---

**Remember**: Configuration is powerful, but don't over-optimize. Start simple, measure results, iterate based on data.
