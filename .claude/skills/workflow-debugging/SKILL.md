---
name: Workflow Debugging
description: Systematic debugging toolkit for complex workflow orchestration systems, enabling rapid identification, isolation, and resolution of execution failures across multi-stakeholder projects with automated recovery and cross-region support.
version: 1.0.0
author: 360 Social Impact Studios
created: 2025-11-16
---

# Workflow Debugging Skill

## Overview

The Workflow Debugging skill provides systematic methodologies for debugging complex workflow orchestration systems used in innovation consulting contexts. It enables teams to rapidly identify, isolate, and resolve execution failures across technical implementations, partner collaborations, and cross-cultural team coordination.

### What This Skill Does

1. **Diagnoses** workflow execution failures using pattern recognition and automated analysis
2. **Isolates** root causes through systematic debugging techniques
3. **Recovers** automatically from common error patterns (60-80% of issues)
4. **Notifies** appropriate team members through Slack, Asana, and email
5. **Documents** error patterns to build institutional knowledge
6. **Supports** multi-region operations (US, Brazil, Europe) with locale-specific handling

### Core Value Proposition

- **Reduces debugging time by 60-80%** through systematic isolation techniques
- **Prevents cascade failures** in complex multi-agent workflows
- **Enables distributed team debugging** without requiring deep technical expertise
- **Creates institutional knowledge** through documented error patterns
- **Supports multilingual error handling** for international partnerships

## Use Cases

### When to Use This Skill

Use this skill when debugging:
- Multi-stage workflow failures in technology assessment or partnership coordination
- Cross-system integration issues between US and Brazil operations
- Asana integration workflows producing incomplete or duplicate tasks
- Client deliverable automation breaking during report generation
- Document approval workflows failing across geographic boundaries
- API rate limiting or authentication issues
- Encoding problems in cross-region data transfer
- Parallel task execution conflicts

### Specific Application Scenarios

**1. Technology Assessment Workflows**
- Multi-stage evaluation workflow for BIMO or NanoBioPlus fails during market validation
- Application: Isolate whether failure is in data collection agent, analysis script, or report generation

**2. Partnership Coordination Flows**
- Brazil-US joint venture workflow breaks when passing data between CNEN and Yale systems
- Application: Debug cross-system variable passing and authentication handoffs

**3. Client Deliverable Automation**
- Automated report generation for SpacePlan venture fails during financial model integration
- Application: Identify breaking point between Vianeo validation and GenIP scoring modules

**4. Asana Integration Workflows**
- Task creation workflow from meeting transcripts produces incomplete or duplicate tasks
- Application: Debug webhook triggers, data transformation, and API rate limiting issues

**5. Multi-Geography Team Workflows**
- Document approval workflow fails when routing between Seattle, São Paulo offices
- Application: Debug timezone handling, locale formatting, and permission cascades

### When NOT to Use This Skill

Do NOT use this skill for:
- Simple syntax errors or typos (use standard debugging)
- Issues that can be resolved by reading error messages directly
- Non-workflow related debugging (e.g., frontend UI bugs)
- Performance optimization without actual failures
- Security vulnerability scanning

## Operating Principles

### Systematic Debugging Methodology

**Phase 1: Error Capture**
1. Capture complete error context (stack trace, variables, system state)
2. Determine error severity (critical, high, medium, low)
3. Identify affected components and stakeholders
4. Log error with full context for analysis

**Phase 2: Diagnosis**
1. Match error against known patterns in error library
2. Identify root cause through pattern recognition
3. Assess whether error is recoverable automatically
4. Generate suggested fix and workaround options
5. Calculate estimated resolution time

**Phase 3: Recovery Attempt**
1. If auto-recovery enabled and error is recoverable, apply recovery strategy:
   - Retry with exponential backoff
   - Refresh credentials
   - Normalize data encoding
   - Apply rate limiting
   - Validate and transform data
2. Monitor recovery success
3. Log recovery outcome

**Phase 4: Notification & Escalation**
1. Notify appropriate team members based on severity and region
2. Create Asana tasks for errors requiring manual intervention
3. Send Slack alerts for critical issues
4. Escalate to on-call engineer if critical and unrecovered
5. Generate support ticket with full diagnostic information

**Phase 5: Documentation**
1. Save error logs for pattern analysis
2. Update error pattern library if new pattern discovered
3. Document resolution for institutional knowledge
4. Schedule post-mortem if critical issue

### Error Severity Classification

**🚨 CRITICAL (System-Breaking Failures)**
- Production outages affecting clients
- Data loss or corruption
- Security breaches
- Complete workflow stoppage
- Response: Immediate notification, PagerDuty alert, auto-create P1 ticket

**⚠️ ERROR (Function-Level Failures)**
- Failed API calls with no retry
- Missing critical data
- Authentication failures
- Database connection issues
- Response: Slack notification, create Asana task, attempt auto-recovery

**⚡ WARNING (Degraded Performance)**
- Slow queries requiring optimization
- Retry attempts in progress
- Approaching rate limits
- Timezone mismatches
- Response: Log warning, Asana task if recurring, no immediate alert

**ℹ️ INFO (Normal Operations)**
- Successful completions
- Routine operations
- Status updates
- Response: Log only, no notifications

### Regional Configuration

**US West (America/Los_Angeles)**
- Language: en-US
- Date format: MM/DD/YYYY
- Currency: USD
- Encoding: UTF-8
- On-call: eng-us@360studios.com

**Brazil South (America/Sao_Paulo)**
- Language: pt-BR
- Date format: DD/MM/YYYY
- Currency: BRL
- Encoding: UTF-8 (with Latin-1 fallback handling)
- On-call: eng-br@360studios.com
- Special: Portuguese error messages, PTAX currency conversion support

**Europe West (Europe/London)**
- Language: en-GB
- Date format: DD/MM/YYYY
- Currency: EUR
- Encoding: UTF-8
- On-call: eng-eu@360studios.com

## Error Pattern Library

### Common Error Patterns and Recovery Strategies

**1. Connection Timeout**
- Pattern: `timeout|timed out|connection refused`
- Root Cause: Network connectivity or API availability issue
- Recovery: Retry with exponential backoff (3 attempts, 30s/60s/120s delays)
- Workaround: Reduce batch size or use alternative endpoint

**2. Authentication Error**
- Pattern: `auth|unauthorized|forbidden|401|403`
- Root Cause: Credentials expired or permissions insufficient
- Recovery: Refresh credentials from secure storage
- Workaround: Use alternative authentication method or manual re-auth

**3. Data Validation Error**
- Pattern: `validation|invalid|schema|does not match`
- Root Cause: Input data does not match expected format
- Recovery: Validate and transform data to correct schema
- Workaround: Manual data correction or schema update

**4. Rate Limit Error**
- Pattern: `rate limit|too many requests|429`
- Root Cause: API rate limit exceeded
- Recovery: Exponential backoff with delay (1s, 2s, 4s, 8s, 16s)
- Workaround: Queue requests or upgrade API tier

**5. Encoding Error (Cross-Region)**
- Pattern: `decode|encode|utf-8|latin-1|unicode`
- Root Cause: Character encoding mismatch between US and Brazil systems
- Recovery: Normalize encoding (Latin-1 → UTF-8 conversion)
- Workaround: Force UTF-8 encoding on all inputs

**6. Parallel Execution Conflict**
- Pattern: `locked|conflict|race condition|concurrent`
- Root Cause: Multiple tasks accessing shared resource simultaneously
- Recovery: Implement resource locking with timeout
- Workaround: Serialize conflicting tasks

**7. Asana API Rate Limit**
- Pattern: Bulk task creation triggering 429 responses
- Root Cause: Exceeding Asana's 150 requests/minute limit
- Recovery: Batch requests (10 at a time) with 1-second delays
- Workaround: Queue tasks for overnight processing

## Integration Points

### Slack Integration

**Alert Channels:**
- `#alerts-critical` - Critical production failures
- `#workflow-errors` - Standard error notifications
- `#workflow-warnings` - Performance warnings
- `#workflow-recovery` - Successful auto-recoveries

**Alert Format:**
```
🔴 Workflow Error: [Workflow Name]

Client: [Client Name]
Region: [us-west|br-south|eu-west]
Error: [Error message]
Time: [Timestamp in local timezone]

[View Debug Log] [Restart Workflow] [Create Asana Task]
```

### Asana Integration

**Auto-Create Debug Tasks:**
- Project: 360 Debug Project
- Assignee: Determined by region and error type
- Priority: Based on severity (P1 for critical, P2 for high)
- Due Date: Calculated based on SLA (critical=2h, high=24h, medium=3d)
- Custom Fields: Error Type, Client, Region, Confidence Score

**Task Template:**
```
[DEBUG] [Workflow Name] - [Error Type]

Client: [Client Name]
Region: [Region]
Error: [Error message]

Root Cause: [Diagnosis]
Suggested Fix: [Recovery strategy]
Workaround: [If available]

Stack Trace: [Attached or linked]
Variables: [Attached JSON]

Debug Log: [Link to S3/Drive]
```

### Google Drive Integration

**Auto-Save Debug Logs:**
- Save comprehensive debug logs to client folders
- Format: JSON with error context, diagnosis, recommendations
- Filename: `Debug_[WorkflowID]_[Timestamp].json`
- Permissions: Shared with project team, optionally with client

### Email Notifications

**Recipients by Severity:**
- Critical: chandler@360studios.com, tech-leads@360studios.com
- Error: dev-team@360studios.com
- Warning: workflow-monitoring@360studios.com

**Email Templates:**
- Critical: Full diagnostic report with immediate action items
- Error: Summary with debug log link
- Recovery Success: Brief notification with statistics

## Workflow Implementation

### Using the Python Debugger Module

**Basic Usage:**
```python
from workflow_debugger import debug_workflow_error

try:
    # Your workflow code
    result = execute_complex_workflow()
except Exception as e:
    # Debug the error
    diagnosis = await debug_workflow_error(
        error=e,
        workflow_id="wf-project-001",
        workflow_name="SpacePlan Financial Integration",
        client_name="SpacePlan/Mercosul Ventures",
        region="br-south",
        environment="production",
        client_facing=True,
        user_email="chandler@360studios.com",
        variables=workflow_variables,
        completed_steps=completed_steps,
        current_step=current_step
    )
```

**Advanced Configuration:**
```python
from workflow_debugger import WorkflowDebugger

debugger = WorkflowDebugger({
    'auto_recovery': True,
    'max_retry_attempts': 3,
    'notification_channels': ['slack', 'asana', 'email'],
    'regions': {
        'br-south': {
            'timezone': 'America/Sao_Paulo',
            'language': 'pt-BR'
        }
    }
})

# Monitor workflow with automatic debugging
await debugger.debug_workflow(error, context)
```

### Using the Command-Line Tools

**Check Workflow Status:**
```bash
workflow status <workflow-id>
```

**View Recent Errors:**
```bash
workflow errors --last 24h --client "SpacePlan"
```

**Replay Failed Workflow:**
```bash
workflow replay <workflow-id> --debug --region br-south
```

**Export Debug Logs:**
```bash
workflow export-logs --client "SpacePlan" --format json --output ./debug-export/
```

**Clear Error Cache:**
```bash
workflow clear-cache --older-than 7d
```

## Quality Standards

### Diagnostic Quality Requirements

Every workflow debug session must deliver:

**1. Complete Error Context**
- Full stack trace captured
- All workflow variables at time of failure
- System state (memory, CPU, network)
- Timing metrics (execution time per step)

**2. Accurate Diagnosis**
- Root cause identified with >70% confidence
- Affected components listed
- Similar past errors referenced
- Recovery feasibility assessed

**3. Actionable Resolution**
- Immediate fix provided (if available)
- Workaround suggested (if applicable)
- Permanent solution outlined
- Estimated resolution time calculated

**4. Prevention Recommendations**
- Monitoring additions suggested
- Test cases proposed
- Documentation updates identified

**5. Complete Artifacts**
- Debug log URL provided
- Replay command generated (if applicable)
- Support ticket created (if critical)

### Performance Metrics

**Response Time Targets:**
- Error capture: <1 second
- Initial diagnosis: <5 seconds
- Auto-recovery attempt: <60 seconds
- Notification delivery: <10 seconds

**Accuracy Targets:**
- Root cause identification: >80% accuracy
- Auto-recovery success rate: >60%
- False positive rate: <10%

**Availability Targets:**
- Debug system uptime: >99.9%
- Notification delivery: >99.5%
- Log storage: >99.99%

## Team Workflows

### For Developers

**When Error Occurs:**
1. Check Slack #workflow-alerts for notification
2. Click debug log link in notification
3. Review diagnosis and suggested fix
4. Apply quick fix if available
5. Test with `workflow replay <id> --debug`
6. Deploy fix and mark Asana task complete

**Creating Custom Error Patterns:**
1. Document new error pattern in `error_patterns` dictionary
2. Define recovery strategy function
3. Add to recovery strategies mapping
4. Test with historical error data
5. Deploy to production

### For Project Managers

**Monitoring Workflow Health:**
1. Access dashboard at debug.360studios.com
2. Review error rate trends by client
3. Check SLA compliance (resolution times)
4. Identify recurring issues for preventive action

**Client Communication:**
1. Receive notification of client-facing errors
2. Use provided talking points for client communication
3. Share workaround if available
4. Provide realistic ETA based on estimated resolution time

### For International Partners (Brazil Team)

**Portuguese Error Handling:**
- All error messages automatically translated to Portuguese
- Date/time shown in São Paulo timezone (BRT/BRST)
- Currency amounts shown in BRL with PTAX conversion
- Brazilian holiday schedule honored for on-call routing

**Regional Support:**
- Primary contact: eng-br@360studios.com
- Escalation: brazil-tech@360studios.com
- Hours: 9am-6pm Brasília time (weekdays)
- Emergency: Use global on-call rotation

## Configuration

### Environment Variables Required

```bash
# Slack Integration
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL

# Asana Integration
ASANA_ACCESS_TOKEN=your_asana_personal_access_token
ASANA_WORKSPACE_ID=your_workspace_id
ASANA_DEBUG_PROJECT_ID=your_debug_project_id

# Google Drive Integration
GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account-key.json
GOOGLE_DRIVE_DEBUG_FOLDER=folder_id_for_debug_logs

# Database (Optional)
DATABASE_URL=postgresql://user:pass@host:5432/dbname

# Redis (Optional - for caching)
REDIS_PASSWORD=your_redis_password

# Authentication (Optional - for debug dashboard)
AUTH0_DOMAIN=your-tenant.auth0.com
AUTH0_CLIENT_ID=your_client_id
AUTH0_CLIENT_SECRET=your_client_secret

# Encryption (Optional - for sensitive data)
ENCRYPTION_KEY_PATH=/path/to/encryption.key
```

### Client-Specific Overrides

**SpacePlan Configuration:**
```yaml
clients:
  spacePlan:
    notifications:
      email:
        recipients: ["spacePlan-tech@360studios.com"]
    integrations:
      custom_api: "https://api.spacePlan.com"
    regions:
      preferred: "br-south"
```

**CNEN Configuration:**
```yaml
clients:
  cnen:
    regions:
      preferred: "br-south"
    security:
      extra_encryption: true
    language: "pt-BR"
```

## Success Metrics

### Key Performance Indicators

**Efficiency Metrics:**
- Mean Time to Detection (MTTD): Target <30 seconds
- Mean Time to Resolution (MTTR): Target <15 minutes
- Auto-Recovery Rate: Target >60%
- False Positive Rate: Target <5%

**Quality Metrics:**
- Root Cause Accuracy: Target >80%
- Fix Success Rate: Target >90%
- Error Recurrence Rate: Target <10%

**Business Impact:**
- Client-Facing Error Reduction: Target >70%
- Debugging Time Savings: Target >40 hours/month
- Team Productivity: Target <10% time on debugging
- Client Satisfaction: No degradation due to technical issues

## Quick Reference

### Common Quick Fixes

| Symptom | Likely Cause | Quick Fix |
|---------|--------------|-----------|
| Timeout | API slow/down | Increase timeout, add retry |
| Variable undefined | Typo or timing | Check spelling, add wait step |
| Auth failed | Token expired | Refresh credentials |
| Data corrupted | Encoding issue | Force UTF-8, normalize encoding |
| Duplicate execution | Missing idempotency | Add execution lock/deduplication |
| Rate limit | Too many requests | Add backoff delay, batch requests |

### Escalation Path (Time-Based)

1. **0-5 min**: Try quick fix from error pattern library
2. **5-10 min**: Run diagnostic tool and review suggestions
3. **10-15 min**: Check documentation and similar errors
4. **15-20 min**: Ask team in #workflow-help Slack
5. **20-25 min**: Create support ticket with full diagnostics
6. **25-30 min**: Schedule emergency call if critical

### Key Contacts

- **US Technical**: dev-team@360studios.com
- **Brazil Technical**: brazil-tech@360studios.com, eng-br@360studios.com
- **Project Management**: chandler@360studios.com
- **Emergency**: Use PagerDuty or #emergency Slack channel

## Additional Resources

For comprehensive implementation details, refer to:

- **IMPLEMENTATION-GUIDE.md** - Complete implementation library with setup, configuration, and advanced usage
- **QUICK-START.md** - Get debugging in 5 minutes with basic usage examples
- **README.md** - Executive summary with ROI analysis and implementation roadmap
- **src/workflow_debugger.py** - Production-ready Python implementation
- **config/debug-config-template.yml** - Complete configuration template
- **requirements.txt** - Python dependencies for installation

## Important Reminders

1. **Always capture full context**: Incomplete context leads to misdiagnosis and wasted time.

2. **Region matters**: Apply correct timezone, language, and encoding for each region.

3. **Auto-recovery is not magic**: Monitor recovery success rates and disable for unstable patterns.

4. **Notify the right people**: Route critical errors to on-call, standard errors to team, warnings to monitoring.

5. **Document new patterns**: Every new error type should be added to the pattern library for future auto-recovery.

6. **Client communication is key**: For client-facing errors, prioritize communication over perfect fixes.

7. **Prevention over cure**: Use error patterns to add proactive monitoring and prevent future issues.

8. **Security first**: Always mask sensitive data (credentials, PII, API keys) in logs and notifications.

---

**Ready to debug workflows systematically. Install the Python module from src/workflow_debugger.py or use the quick-start guide for immediate implementation.**
