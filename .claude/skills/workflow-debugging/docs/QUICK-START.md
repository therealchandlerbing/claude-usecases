# Workflow Debugging Quick Start Guide
*Get debugging in 5 minutes*

## Installation

```bash
# 1. Navigate to the skill directory
cd .claude/skills/workflow-debugging

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Set environment variables
export SLACK_WEBHOOK_URL="your-slack-webhook"
export ASANA_ACCESS_TOKEN="your-asana-token"
export ASANA_PROJECT_ID="your-debug-project-id"
```

## Basic Usage

### Python Integration

```python
from src.workflow_debugger import debug_workflow_error

# Wrap your workflow code
try:
    # Your workflow code here
    result = execute_workflow()
except Exception as e:
    debug_result = await debug_workflow_error(
        error=e,
        workflow_id="your-workflow-id",
        workflow_name="Your Workflow Name",
        client_name="Client Name",
        region="us-west",  # or "br-south"
        user_email="your-email@360studios.com"
    )
```

### JavaScript Integration

```javascript
const { WorkflowDebugger } = require('@360/debug-tools');

const debugger = new WorkflowDebugger({
  project: 'your-project',
  environment: 'production'
});

// Wrap your workflow
debugger.monitor(async () => {
  // Your workflow code here
}).catch(error => {
  debugger.diagnose(error);
});
```

## Common Debugging Scenarios

### Scenario 1: Asana API Rate Limit

**Error**: "429 Too Many Requests from Asana API"

**Quick Fix**:
```python
# Add rate limiting wrapper
from src.workflow_debugger import RateLimitedAsana

asana = RateLimitedAsana()
await asana.createTask(task_data)  # Automatically handles rate limits
```

### Scenario 2: Brazil Data Encoding Issue

**Error**: "UnicodeDecodeError when processing Brazilian client data"

**Quick Fix**:
```python
from src.workflow_debugger import normalize_encoding

# Normalize data before processing
normalized_data = normalize_encoding(
    data=brazilian_data,
    source_region='brazil',
    target_region='us-west'
)
```

### Scenario 3: Parallel Task Conflict

**Error**: "Resource locked by another process"

**Quick Fix**:
```python
from src.workflow_debugger import ResourceLockManager

lock_manager = ResourceLockManager()

async with lock_manager.acquire('shared-resource-id'):
    # Your critical section code
    await process_shared_resource()
```

## Team Workflows

### For Developers

1. **When error occurs**: Check Slack #workflow-alerts
2. **Access debug log**: Click link in Slack notification
3. **Apply quick fix**: Use suggested recovery strategy
4. **Test fix**: Run `workflow replay <id> --debug`
5. **Deploy**: Push fix to production

### For Project Managers

1. **Monitor status**: Check Asana debug project
2. **View impact**: See affected clients in dashboard
3. **Communicate**: Use pre-written client templates
4. **Track resolution**: Monitor ticket progress

### For Partners (Brazil Team)

1. **Portuguese errors**: Automatically translated
2. **Timezone handling**: Auto-adjusted for São Paulo
3. **Regional endpoint**: Use `br-south` region
4. **Local support**: Contact brazil-tech@360studios.com

## Environment-Specific Configuration

### Development
```yaml
# config/debug.dev.yml
auto_recovery: false  # Manual recovery only
notifications:
  - email  # No Slack spam in dev
log_level: DEBUG
```

### Staging
```yaml
# config/debug.staging.yml
auto_recovery: true
notifications:
  - slack
  - email
log_level: INFO
```

### Production
```yaml
# config/debug.prod.yml
auto_recovery: true
notifications:
  - slack
  - asana
  - email
  - pagerduty  # For critical errors
log_level: WARNING
```

## Command Line Tools

```bash
# Check workflow status
workflow status <workflow-id>

# View recent errors
workflow errors --last 24h

# Replay failed workflow
workflow replay <workflow-id> --debug

# Export debug logs
workflow export-logs --client "SpacePlan" --format json

# Clear error cache
workflow clear-cache --older-than 7d
```

## Debugging Checklist

### Before Starting
- [ ] Check if error is already known (search error database)
- [ ] Verify you have access to affected systems
- [ ] Check system status page for known outages

### During Debug
- [ ] Capture full error context
- [ ] Try suggested quick fix first
- [ ] Test fix in staging before production
- [ ] Document any new error patterns

### After Resolution
- [ ] Update documentation if new error type
- [ ] Notify affected stakeholders
- [ ] Schedule post-mortem if critical

## Error Code Reference

| Code | Meaning | Quick Action |
|------|---------|--------------|
| WF001 | Workflow not found | Check workflow ID spelling |
| WF002 | Authentication failed | Refresh credentials |
| WF003 | Timeout exceeded | Increase timeout or retry |
| WF004 | Rate limit hit | Wait and retry with backoff |
| WF005 | Data validation error | Check data format |
| WF006 | Permission denied | Verify user permissions |
| WF007 | Network error | Check connectivity |
| WF008 | Encoding error | Normalize encoding |
| WF009 | Parallel conflict | Add resource lock |
| WF010 | Memory exceeded | Reduce batch size |

## Integration Examples

### With Asana

```python
# Auto-create debug task
from src.workflow_debugger import create_debug_task

await create_debug_task(
    error=error,
    project_id="your-asana-project",
    assignee="team-member@360studios.com",
    priority="High"
)
```

### With Slack

```python
# Send custom alert
from src.workflow_debugger import send_slack_alert

await send_slack_alert(
    channel="#client-alerts",
    error=error,
    mentions=["@chandler"] if critical else []
)
```

### With Google Drive

```python
# Save debug report
from src.workflow_debugger import save_debug_report

report_url = await save_debug_report(
    error=error,
    folder_id="client-google-drive-folder",
    format="pdf"
)
```

## Monitoring Dashboard

Access real-time debugging metrics:
- **URL**: https://debug.360studios.com
- **Login**: Your 360 email
- **Dashboards**:
  - Overview: All workflows
  - Client View: Per-client errors
  - Regional: US/Brazil/Europe
  - Performance: Response times

## Support Escalation

### Level 1: Self-Service (0-5 min)
- Check this guide
- Try quick fixes
- Search error database

### Level 2: Team Support (5-15 min)
- Post in #workflow-help Slack
- Check with team member
- Review recent similar errors

### Level 3: Expert Support (15-30 min)
- Create support ticket
- Tag senior developer
- Schedule debug session

### Level 4: External Support (30+ min)
- Contact vendor support (Asana, etc.)
- Engage consulting partner
- Emergency hotline: +1-555-DEBUG-NOW

## Best Practices

### DO ✅
- Always capture full context
- Test fixes in staging first
- Document new error patterns
- Share learnings with team
- Keep debug logs for audit

### DON'T ❌
- Ignore recurring errors
- Skip error logging
- Debug directly in production
- Remove error handling
- Share sensitive data in logs

## Troubleshooting Tips

### "Can't reproduce error"
1. Check exact timestamp
2. Use same region/environment
3. Replay with exact same data
4. Check for race conditions

### "Fix doesn't work"
1. Verify fix was deployed
2. Clear any caches
3. Check for multiple error causes
4. Test with minimal case

### "Getting too many alerts"
1. Adjust notification throttling
2. Group similar errors
3. Set severity thresholds
4. Use digest mode

## Resources

- **Documentation**: See IMPLEMENTATION-GUIDE.md
- **Error Database**: Local debug-logs/ directory
- **Status Page**: Check your monitoring dashboard
- **Team Calendar**: On-call schedule in Asana
- **Training Videos**: Team Resources folder

## Contact

- **General Support**: dev-team@360studios.com
- **US Team**: eng-us@360studios.com
- **Brazil Team**: eng-br@360studios.com
- **Emergency**: Use PagerDuty or Slack #emergency

---

*Last updated: November 2024 | Version 1.0*
