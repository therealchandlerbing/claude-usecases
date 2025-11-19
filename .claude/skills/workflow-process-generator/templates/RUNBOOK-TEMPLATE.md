# Operational Runbook Template

Use this template for incident response, troubleshooting, and operational procedures.

---

## OPERATIONAL RUNBOOK

**Document ID:** RUN-[AREA]-[NUMBER]
**Title:** [System/Process Name] Runbook
**Version:** 1.0
**Effective Date:** [YYYY-MM-DD]
**Review Date:** [YYYY-MM-DD + 6 months]
**Owner:** [Role/Name]
**On-Call Rotation:** [Rotation Name]

---

### QUICK REFERENCE

#### Severity Classification

| Severity | Definition | Response | Resolution Target |
|----------|------------|----------|-------------------|
| SEV-1 | [Complete outage, all users] | [Time] | [Time] |
| SEV-2 | [Major impact, partial outage] | [Time] | [Time] |
| SEV-3 | [Minor impact, degraded service] | [Time] | [Time] |
| SEV-4 | [Minimal impact, cosmetic] | [Time] | [Time] |

#### Emergency Contacts

| Role | Name | Phone | Slack/Page |
|------|------|-------|------------|
| On-Call Engineer | [Rotation] | PagerDuty | @oncall |
| [Escalation 1] | [Name] | [Phone] | @handle |
| [Escalation 2] | [Name] | [Phone] | @handle |

---

### 1. SYSTEM OVERVIEW

**Purpose:** [What this system does]

**Architecture:** [Brief description or link to diagram]

**Dependencies:**
- [Dependency 1]
- [Dependency 2]

**Key Metrics:**
- [Metric 1]: [Normal range]
- [Metric 2]: [Normal range]

---

### 2. COMMON ISSUES AND RESOLUTION

#### Issue: [Issue Name]

**Symptoms:**
- [Observable symptom 1]
- [Observable symptom 2]

**Diagnosis:**
```bash
# [Description of command]
[command]
```

**Resolution:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Verification:**
```bash
# [Description of verification]
[command]
```

---

#### Issue: [Issue Name]

**Symptoms:**
- [Observable symptom 1]
- [Observable symptom 2]

**Diagnosis:**
[Diagnostic steps]

**Resolution:**
[Resolution steps]

**Verification:**
[Verification steps]

---

### 3. STANDARD PROCEDURES

#### 3.1 Health Check

**Purpose:** Verify system is operating normally

**Steps:**
```bash
# [Step description]
[command]

# [Step description]
[command]
```

**Expected Results:**
- [Result 1]
- [Result 2]

---

#### 3.2 Restart Procedure

**When to use:** [Circumstances]

**Pre-requisites:**
- [ ] [Check 1]
- [ ] [Check 2]

**Steps:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Verification:**
[How to confirm successful restart]

---

#### 3.3 Failover Procedure

**When to use:** [Circumstances]

**Steps:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Failback:**
[Steps to return to primary]

---

### 4. INCIDENT RESPONSE

#### 4.1 Detection

**Alerts:**
| Alert | Threshold | Severity | Action |
|-------|-----------|----------|--------|
| [Alert name] | [Condition] | [SEV-X] | [Action] |

#### 4.2 Initial Response

1. **Acknowledge alert** within response SLA
2. **Assess impact:**
   - How many users affected?
   - Which functionality impacted?
   - Is there a workaround?
3. **Classify severity** using matrix above
4. **Communicate:**
   - Post in [incident channel]
   - Page additional responders if needed

#### 4.3 Investigation

**Data Sources:**
- Logs: [Location/command]
- Metrics: [Dashboard link]
- Traces: [System]

**Common Investigation Steps:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

#### 4.4 Mitigation

**Options by speed:**

| Option | Time | Risk | When to Use |
|--------|------|------|-------------|
| [Option 1] | [Time] | [Risk] | [Scenario] |
| [Option 2] | [Time] | [Risk] | [Scenario] |

#### 4.5 Communication

**Internal Updates:**
```
:rotating_light: INCIDENT UPDATE
Status: [Investigating/Identified/Monitoring/Resolved]
Impact: [Current impact]
Next Actions: [What's happening]
ETA: [If known]
```

**External Updates:** [StatusPage procedure]

#### 4.6 Resolution

**Criteria for resolution:**
- [ ] Service restored
- [ ] Root cause identified
- [ ] Monitoring confirms stability

**Post-incident:**
- [ ] Update incident record
- [ ] Schedule post-mortem
- [ ] Create follow-up tickets

---

### 5. ROLLBACK PROCEDURE

**When to use:** [Circumstances requiring rollback]

**Pre-requisites:**
- [ ] Previous version identified: _______
- [ ] Rollback approved by: _______

**Steps:**
```bash
# [Step description]
[command]
```

**Verification:**
```bash
# Confirm rollback successful
[command]
```

---

### 6. MONITORING AND ALERTING

#### Dashboards

| Dashboard | Purpose | Link |
|-----------|---------|------|
| [Name] | [Purpose] | [URL] |

#### Key Metrics

| Metric | Normal | Warning | Critical |
|--------|--------|---------|----------|
| [Metric] | [Range] | [Range] | [Range] |

---

### 7. MAINTENANCE PROCEDURES

#### 7.1 [Maintenance Task]

**Frequency:** [Schedule]

**Steps:**
1. [Step 1]
2. [Step 2]

---

### 8. TROUBLESHOOTING GUIDE

#### Decision Tree

```
System appears slow
├─ Check CPU utilization
│  ├─ High (>80%) → Scale up or optimize
│  └─ Normal → Check next
├─ Check memory utilization
│  ├─ High (>85%) → Investigate memory leak
│  └─ Normal → Check next
├─ Check database connections
│  ├─ Near limit → Investigate connection pool
│  └─ Normal → Check external dependencies
└─ Check external dependencies
   └─ [Dependency-specific checks]
```

---

### APPENDIX: USEFUL COMMANDS

```bash
# [Description]
[command]

# [Description]
[command]

# [Description]
[command]
```

---

## TEMPLATE USAGE NOTES

**Customization Guidelines:**
1. Replace all [bracketed] content
2. Add/remove issue sections as needed
3. Include actual commands and scripts
4. Update emergency contacts quarterly
5. Test all commands before publishing

**Quality Checklist:**
- [ ] All commands tested and working
- [ ] Contact information current
- [ ] Severity definitions match organization standards
- [ ] Dashboard links valid
- [ ] Review date set appropriately
