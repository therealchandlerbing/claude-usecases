# Example: Operational Runbook - Incident Response

**Scenario:** A DevOps team needs to document their incident response procedures. They handle a SaaS platform with 99.9% uptime SLA and need clear procedures for various severity levels.

**User Request:** "We need an incident response runbook. Our team has grown and we can't rely on tribal knowledge anymore. We have severity levels 1-4 and different on-call rotations."

---

## WORKFLOW PROCESS GENERATOR RESPONSE:

I'll create a comprehensive incident response runbook that scales with your team and maintains your SLA commitments.

**Understanding Confirmation:**
- Process: Incident detection through resolution and post-mortem
- Users: On-call engineers, incident commanders, stakeholders
- Requirements: Clear severity definitions, escalation paths, communication protocols
- Goal: Consistent response regardless of who's on call

**Documentation Strategy:**
Given the critical nature and 24/7 requirements:
1. Quick-reference severity guide (immediate access)
2. Detailed response procedures by severity
3. Communication templates
4. Escalation matrix
5. Post-incident review process

---

## INCIDENT RESPONSE RUNBOOK

**Document ID:** RUN-OPS-001
**Title:** Incident Response Runbook
**Version:** 1.0
**Effective Date:** [Date]
**Review Date:** [Date + 6 months]
**Owner:** VP of Engineering
**Classification:** Internal - Operations

---

### QUICK REFERENCE: SEVERITY CLASSIFICATION

| Severity | Definition | Response Time | Update Frequency | Example |
|----------|------------|---------------|------------------|---------|
| **SEV-1** | Complete service outage affecting all customers | 5 minutes | Every 15 minutes | Platform unreachable, data loss |
| **SEV-2** | Major feature unavailable affecting >20% customers | 15 minutes | Every 30 minutes | Payment processing down, API timeouts |
| **SEV-3** | Minor feature degraded affecting <20% customers | 1 hour | Every 2 hours | Slow reports, intermittent errors |
| **SEV-4** | Minimal impact, workaround available | 4 hours | Daily until resolved | UI bug, cosmetic issues |

---

### INCIDENT RESPONSE PHASES

#### Phase 1: Detection and Classification (0-10 minutes)

**1.1 Incident Detection**

Incidents are detected through:
- Automated monitoring alerts (PagerDuty)
- Customer reports (Support tickets, Slack)
- Internal reports (Employee observations)
- External monitoring (Pingdom, StatusPage subscribers)

**1.2 Initial Assessment**

On-call engineer performs initial assessment within **5 minutes** of notification:

```
INITIAL ASSESSMENT CHECKLIST:
[ ] What is the symptom? (error messages, behavior)
[ ] When did it start? (timestamp from monitoring)
[ ] What is the scope? (all users, specific segment, single user)
[ ] What is the business impact? (which features/capabilities affected)
[ ] Are there any recent changes? (deployments, config changes)
```

**1.3 Classify Severity**

Using the symptom and impact, classify severity:

```
IF service completely unavailable for all customers:
   → SEV-1

IF major feature unavailable OR >20% customers affected:
   → SEV-2

IF feature degraded OR <20% customers affected:
   → SEV-3

IF minimal impact with workaround available:
   → SEV-4
```

**When uncertain between two levels, choose the higher severity.** It can always be downgraded.

**1.4 Declare Incident**

Create incident record:
1. Create incident in OpsGenie
2. Set severity level
3. Set incident summary (one sentence)
4. Page appropriate responders based on severity

---

#### Phase 2: Response Activation (10-30 minutes)

**2.1 Assemble Response Team**

**SEV-1 Team:**
- Incident Commander (required)
- Primary On-call Engineer (required)
- Secondary On-call Engineer (required)
- Customer Success Lead (required)
- Engineering Manager (required)
- Executive on call (informed)

**SEV-2 Team:**
- Incident Commander (required)
- Primary On-call Engineer (required)
- Secondary On-call Engineer (as needed)
- Customer Success Lead (as needed)

**SEV-3/4 Team:**
- Primary On-call Engineer (required)

**2.2 Establish Communication Channels**

**For SEV-1 and SEV-2:**

1. Create incident Slack channel: `#inc-YYYYMMDD-brief-description`
2. Start incident bridge (Zoom link in PagerDuty)
3. Pin key information to channel:
   - Incident summary
   - Current severity
   - Bridge link
   - Status page link
   - Key timelines

**2.3 Incident Commander Responsibilities**

The Incident Commander (IC) **does not troubleshoot.** IC responsibilities:
- Coordinate response team
- Make severity/escalation decisions
- Manage communications
- Track timeline
- Remove blockers
- Ensure handoffs

If no IC is assigned within 10 minutes of SEV-1/SEV-2 declaration, Engineering Manager on call assumes IC role.

---

#### Phase 3: Investigation and Diagnosis (Ongoing)

**3.1 Initial Investigation**

Check these common causes in order:

```
1. RECENT CHANGES
   - Check deployment log (last 24 hours)
   - Check config changes
   - Check infrastructure changes
   - Check third-party status pages

2. INFRASTRUCTURE
   - Check AWS Health Dashboard
   - Check database performance
   - Check server resource utilization
   - Check network connectivity

3. APPLICATION
   - Check error logs
   - Check application metrics
   - Check request patterns
   - Check dependency health

4. EXTERNAL
   - Check third-party APIs
   - Check DNS resolution
   - Check SSL certificates
   - Check CDN status
```

**3.2 Investigation Documentation**

Document all investigation activities in the incident channel:

```
Format: [HH:MM] [Name] [Action] - [Result]

Example:
[14:32] @alice Checked deployment log - Found deployment at 14:15 to production
[14:35] @alice Checked error rates - 500 errors increased 10x at 14:17
[14:38] @alice Hypothesis: Recent deployment caused error spike
```

**3.3 Escalation Triggers**

Escalate to next level if:
- No progress after 15 minutes (SEV-1) or 30 minutes (SEV-2)
- Additional expertise needed
- Customer impact is increasing
- Root cause requires system owner

**Escalation Paths:**

| System | Primary | Secondary | After Hours |
|--------|---------|-----------|-------------|
| Database | @db-team | @alice | PagerDuty: db-oncall |
| API | @api-team | @bob | PagerDuty: api-oncall |
| Infrastructure | @infra-team | @carol | PagerDuty: infra-oncall |
| Payments | @payments-team | @dave | PagerDuty: payments-oncall |
| Auth | @auth-team | @eve | PagerDuty: auth-oncall |

---

#### Phase 4: Mitigation and Resolution

**4.1 Mitigation Options**

Consider these options in order of speed:

| Option | Speed | Risk | When to Use |
|--------|-------|------|-------------|
| Rollback deployment | Fast (5 min) | Low | Deployment-related issues |
| Feature flag disable | Fast (2 min) | Low | Feature-specific issues |
| Scale up resources | Medium (10 min) | Low | Capacity issues |
| Failover to backup | Medium (15 min) | Medium | Primary system failure |
| Apply hotfix | Slow (30+ min) | Medium | Specific bug fix needed |

**4.2 Mitigation Approval**

| Action | SEV-1 | SEV-2 | SEV-3/4 |
|--------|-------|-------|---------|
| Rollback | IC approval | IC approval | On-call judgment |
| Feature flag | IC approval | On-call judgment | On-call judgment |
| Scale up | On-call judgment | On-call judgment | On-call judgment |
| Failover | IC + Engineering Manager | IC approval | N/A |
| Hotfix | IC + Engineering Manager | IC approval | On-call judgment |

**4.3 Implementing Mitigation**

Before implementing:
1. Communicate plan to IC and team
2. Confirm rollback procedure if mitigation fails
3. Identify verification method

During implementation:
1. Announce start in incident channel
2. Execute mitigation
3. Monitor impact

After implementation:
1. Verify mitigation effectiveness
2. Announce result in incident channel
3. Update severity if impact reduced

**4.4 Resolution Criteria**

Incident is resolved when:
- [ ] Service restored to normal operation
- [ ] Root cause identified (or clear path to identify)
- [ ] No ongoing customer impact
- [ ] Monitoring confirms stability (10+ minutes)

---

#### Phase 5: Communication

**5.1 Internal Communication**

**Incident Channel Updates:**

Format:
```
:rotating_light: INCIDENT UPDATE :rotating_light:
**Status:** [Investigating/Identified/Monitoring/Resolved]
**Impact:** [Current impact description]
**Next Actions:** [What we're doing next]
**ETA:** [If known]
```

Update frequency:
- SEV-1: Every 15 minutes
- SEV-2: Every 30 minutes
- SEV-3/4: Every 2 hours or on significant change

**Stakeholder Updates:**

SEV-1 and SEV-2 require executive updates:
- First update: Within 30 minutes of declaration
- Ongoing: Every hour until resolved
- Resolution: Within 30 minutes of resolution

Use template: TEMPLATE-EXEC-INCIDENT

**5.2 External Communication**

**Status Page Updates:**

| Event | Update Status Page? | Template |
|-------|--------------------|---------|
| SEV-1 declared | Yes, immediately | TEMPLATE-STATUS-INVESTIGATING |
| SEV-2 declared | Yes, within 15 min | TEMPLATE-STATUS-INVESTIGATING |
| SEV-3 declared | Only if customer-reported | TEMPLATE-STATUS-DEGRADED |
| Impact identified | Yes | TEMPLATE-STATUS-IDENTIFIED |
| Mitigation implemented | Yes | TEMPLATE-STATUS-MONITORING |
| Incident resolved | Yes | TEMPLATE-STATUS-RESOLVED |

**Customer Communication:**

For SEV-1 and SEV-2:
1. Customer Success drafts communication
2. IC reviews and approves
3. Send via email and in-app notification
4. Post to status page

Templates in: /templates/incident-communication/

**5.3 Communication Templates**

**Status Page - Investigating:**
```
[Service Name] - Investigating Issues

We are currently investigating issues with [affected service].
Some users may experience [symptoms]. We will provide updates
as we learn more.

Current impact: [description]
Started: [time]
```

**Status Page - Identified:**
```
[Service Name] - Issue Identified

We have identified the cause of the [service] issues and are
implementing a fix. [Brief cause description without sensitive details]

Current impact: [description]
Expected resolution: [time if known, or "as soon as possible"]
```

**Status Page - Resolved:**
```
[Service Name] - Resolved

The issues affecting [service] have been resolved. All systems
are operating normally.

Duration: [start time] to [end time]
Impact: [summary of what was affected]

We apologize for any inconvenience and will publish a post-incident
review within [timeframe].
```

---

#### Phase 6: Post-Incident Activities

**6.1 Immediate Actions (Within 24 hours)**

1. Incident Commander completes incident record:
   - Final timeline
   - Root cause summary
   - Mitigation actions taken
   - Customer impact summary

2. Schedule post-incident review:
   - SEV-1: Within 48 hours
   - SEV-2: Within 1 week
   - SEV-3/4: As needed

3. Create follow-up tickets:
   - Permanent fix (if hotfix applied)
   - Monitoring improvements
   - Process improvements

**6.2 Post-Incident Review (Blameless)**

**Participants:**
- Incident Commander
- Responding engineers
- Engineering Manager
- Customer Success (if customer impact)
- Others involved in response

**Agenda:**
1. Timeline walkthrough (15 min)
2. Root cause analysis (15 min)
3. What went well (10 min)
4. What could be improved (10 min)
5. Action items (10 min)

**Ground Rules:**
- Focus on systems and processes, not people
- Assume everyone did their best with available information
- Identify systemic improvements
- No blame or punishment

**6.3 Post-Incident Report**

Document structure:
```
## Incident Summary
- Date/time
- Duration
- Severity
- Impact

## Timeline
- Minute-by-minute sequence of events

## Root Cause
- Technical root cause
- Contributing factors

## Resolution
- What fixed it
- Verification method

## Impact
- Number of affected customers
- Revenue impact (if applicable)
- SLA impact

## Lessons Learned
- What went well
- What could be improved

## Action Items
- Preventive measures
- Detection improvements
- Process improvements
```

Store in: /incident-reports/YYYY/MM/incident-YYYYMMDD-description.md

**6.4 Action Item Tracking**

All action items from post-incident reviews:
1. Created as Jira tickets
2. Tagged with incident ID
3. Assigned owner and due date
4. Tracked in weekly engineering review
5. Closed when implemented and verified

---

### ON-CALL PROCEDURES

**On-Call Rotations:**

| Rotation | Schedule | Primary | Secondary |
|----------|----------|---------|-----------|
| Primary On-call | Weekly (Mon-Mon) | See PagerDuty | Automatic escalation |
| IC Rotation | Weekly (Mon-Mon) | See PagerDuty | Engineering Manager |
| Customer Success | Weekly | See rotation calendar | CS Manager |
| Executive | Monthly | See rotation calendar | CEO |

**On-Call Responsibilities:**
- Respond to pages within response time SLA
- Triage and classify incoming issues
- Initiate incident response when warranted
- Hand off clearly at rotation end

**On-Call Handoff:**
```
At end of rotation, post in #ops-oncall:

On-Call Handoff: [Your Name] → [Next Person]

**Active Issues:**
- [Issue 1]: [Status, next steps]
- [Issue 2]: [Status, next steps]

**Heads Up:**
- [Upcoming deployment/maintenance]
- [Known issue to monitor]

**Recent Incidents:**
- [Brief summary of anything notable]
```

---

### ESCALATION MATRIX

**Management Escalation:**

| Scenario | Contact | Method |
|----------|---------|--------|
| SEV-1 declared | Engineering Manager | PagerDuty |
| SEV-1 > 30 min | VP Engineering | PagerDuty |
| SEV-1 > 1 hour | CTO | Phone call |
| Customer escalation | Customer Success Manager | Slack |
| Security incident | Security Lead | PagerDuty |
| Legal/PR required | Legal/Communications | Phone call |

**Vendor Escalation:**

| Vendor | Support Portal | Phone | Premium Support |
|--------|---------------|-------|-----------------|
| AWS | Support Console | (AWS Support) | Account Manager: [name] |
| Datadog | Help → Contact | N/A | [email] |
| PagerDuty | Support Portal | (Support line) | N/A |

---

### TOOLS AND ACCESS

**Required Tools:**

| Tool | Purpose | Access |
|------|---------|--------|
| PagerDuty | Alerting and escalation | All on-call |
| OpsGenie | Incident management | All on-call |
| Datadog | Monitoring | All engineers |
| AWS Console | Infrastructure | Ops team + on-call |
| Slack | Communication | All team |
| StatusPage | External communication | CS + Ops leads |

**Runbook Resources:**

| Resource | Location |
|----------|----------|
| Runbooks | /runbooks |
| Communication templates | /templates/incident-communication |
| Escalation contacts | PagerDuty schedules |
| Architecture diagrams | /docs/architecture |
| Post-incident reports | /incident-reports |

---

## Implementation Guidance:

1. **Training Requirements:**
   - All engineers: Full runbook walkthrough (2 hours)
   - IC certification: Facilitated incident simulation (4 hours)
   - Quarterly game days for practice

2. **Success Metrics:**
   - Mean time to detect (MTTD): <5 min
   - Mean time to acknowledge (MTTA): <15 min
   - Mean time to resolve (MTTR): Track by severity
   - Post-incident review completion: 100% for SEV-1/2

3. **Continuous Improvement:**
   - Monthly review of incident trends
   - Quarterly runbook updates
   - Action item completion tracking
   - On-call feedback collection

---

## Quality Assurance Checklist:

- [x] Clear severity definitions with examples
- [x] Specific response times by severity
- [x] Escalation paths with contacts
- [x] Communication templates included
- [x] Tool access documented
- [x] Post-incident process defined
- [x] Training requirements specified
- [x] Metrics defined for improvement
