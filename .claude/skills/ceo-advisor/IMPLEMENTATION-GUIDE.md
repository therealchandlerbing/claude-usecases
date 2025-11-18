# CEO Advisor Implementation Guide

**Comprehensive Deployment and Integration Documentation**

This guide provides detailed instructions for deploying, configuring, integrating, and operating the CEO Advisor skill in production environments. It covers enterprise deployment patterns, data integration, customization, security considerations, and operational best practices.

---

## Table of Contents

1. [Prerequisites & Requirements](#prerequisites--requirements)
2. [Installation & Setup](#installation--setup)
3. [Configuration Deep Dive](#configuration-deep-dive)
4. [Data Integration Patterns](#data-integration-patterns)
5. [Customization Guide](#customization-guide)
6. [Security & Privacy](#security--privacy)
7. [Enterprise Deployment](#enterprise-deployment)
8. [Operational Procedures](#operational-procedures)
9. [Monitoring & Alerting](#monitoring--alerting)
10. [Troubleshooting](#troubleshooting)
11. [Performance Optimization](#performance-optimization)
12. [Future Integration Roadmap](#future-integration-roadmap)

---

## Prerequisites & Requirements

### System Requirements

**Minimum Requirements**
- Python 3.8 or higher
- 2 GB available RAM
- 500 MB disk space
- Network access for external integrations

**Recommended for Production**
- Python 3.10+
- 4+ GB available RAM
- 1 GB disk space
- Dedicated service account
- Secure credential management

### Python Dependencies

**Core Dependencies** (Required)
```
python-dateutil >= 2.8.2
pytz >= 2023.3
pandas >= 1.5.0
numpy >= 1.24.0
```

**Integration Dependencies** (Optional)
```
# Calendar Integration
google-auth >= 2.16.0
google-api-python-client >= 2.70.0

# Communication Platforms
slack-sdk >= 3.19.0

# Database Storage
sqlalchemy >= 2.0.0
psycopg2-binary >= 2.9.5

# Machine Learning (Future)
scikit-learn >= 1.2.0

# Visualization
matplotlib >= 3.6.0
plotly >= 5.12.0

# API Integrations
requests >= 2.28.0
aiohttp >= 3.8.0
```

**Development Dependencies**
```
pytest >= 7.2.0
black >= 23.1.0
flake8 >= 6.0.0
mypy >= 1.0.0
```

---

## Installation & Setup

### Standard Installation

```bash
# 1. Navigate to skill directory
cd .claude/skills/ceo-advisor

# 2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or: venv\Scripts\activate  # Windows

# 3. Install core dependencies
pip install -r config/requirements.txt

# 4. Verify installation
python src/ceo_advisor_orchestrator.py test

# 5. Generate sample data
python examples/sample_data_generator.py
```

### Docker Installation

```dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r config/requirements.txt

ENV PYTHONPATH=/app/src
CMD ["python", "src/ceo_advisor_orchestrator.py", "daily"]
```

```bash
# Build and run
docker build -t ceo-advisor .
docker run -v $(pwd)/config:/app/config ceo-advisor
```

### Enterprise Installation

For enterprise deployments, consider:

1. **Configuration Management**: Store config in secure vault
2. **Secrets Management**: Use HashiCorp Vault, AWS Secrets Manager, etc.
3. **Service Account**: Dedicated account with minimal permissions
4. **Network Isolation**: Run in private subnet with controlled egress
5. **Audit Logging**: Log all operations for compliance

---

## Configuration Deep Dive

### Configuration File Structure

The main configuration file `config/config.json` controls all system behavior:

```json
{
  "system_configuration": {
    "version": "2.0.0",
    "environment": "production",
    "timezone": "America/Los_Angeles",
    "log_level": "INFO"
  },

  "intelligence_configuration": {
    "sensitivity": "high",
    "scan_frequency": "real-time",
    "prediction_horizon_days": 30,
    "confidence_threshold": 0.75,
    "alert_thresholds": {
      "critical": 0.9,
      "warning": 0.7
    }
  },

  "stakeholder_configuration": {
    "tracking_depth": "comprehensive",
    "sentiment_analysis": true,
    "relationship_decay_rate": 0.02,
    "categories": {
      "board": {"weight": 1.0, "engagement_days": 14},
      "investor": {"weight": 0.9, "engagement_days": 30},
      "executive": {"weight": 0.85, "engagement_days": 7},
      "customer": {"weight": 0.8, "engagement_days": 30}
    }
  },

  "optimization_configuration": {
    "mode": "balanced",
    "focus_time_target_hours": 2.0,
    "meeting_batch_mode": true,
    "time_allocation_targets": {
      "strategic_thinking": {"target": 0.25, "min": 0.20, "max": 0.30},
      "team_leadership": {"target": 0.20, "min": 0.15, "max": 0.25},
      "external_engagement": {"target": 0.20, "min": 0.15, "max": 0.25},
      "operational_oversight": {"target": 0.15, "min": 0.10, "max": 0.20},
      "customer_interaction": {"target": 0.10, "min": 0.05, "max": 0.15},
      "personal_development": {"target": 0.10, "min": 0.05, "max": 0.15}
    },
    "energy_profile": {
      "peak_hours": [8, 9, 10],
      "low_hours": [13, 14, 15],
      "recovery_needed_after": ["board_meeting", "conflict_resolution"]
    }
  },

  "strategy_configuration": {
    "review_cycle": "quarterly",
    "planning_horizon_years": 3,
    "scenario_count": 3,
    "risk_tolerance": "moderate"
  },

  "financial_configuration": {
    "runway_warning_months": 9,
    "runway_critical_months": 6,
    "burn_variance_warning": 0.10,
    "burn_variance_critical": 0.20
  },

  "reporting_configuration": {
    "daily_brief": {
      "enabled": true,
      "time": "06:00",
      "format": "summary"
    },
    "weekly_report": {
      "enabled": true,
      "day": "Monday",
      "time": "07:00"
    },
    "output_formats": ["summary", "detailed", "json"]
  },

  "personalization": {
    "ceo_decision_style": "analytical",
    "communication_preference": "concise",
    "risk_tolerance": "moderate",
    "energy_pattern": "morning_peak"
  },

  "integrations": {
    "calendar": {
      "provider": "google",
      "credentials_path": "/secure/google-credentials.json",
      "calendar_id": "primary"
    },
    "crm": {
      "provider": "salesforce",
      "instance_url": "https://your-instance.salesforce.com",
      "credentials_path": "/secure/salesforce-credentials.json"
    },
    "communication": {
      "provider": "slack",
      "workspace": "your-workspace",
      "bot_token_path": "/secure/slack-token"
    }
  }
}
```

### Configuration Parameters Reference

#### Intelligence Configuration

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| sensitivity | string | "high" | Signal detection sensitivity (low/medium/high) |
| scan_frequency | string | "real-time" | How often to scan (real-time/hourly/daily) |
| prediction_horizon_days | int | 30 | How far ahead to predict |
| confidence_threshold | float | 0.75 | Minimum confidence for alerts |

#### Stakeholder Configuration

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| tracking_depth | string | "comprehensive" | Detail level (basic/standard/comprehensive) |
| sentiment_analysis | bool | true | Enable sentiment tracking |
| relationship_decay_rate | float | 0.02 | Daily decay without interaction |

#### Optimization Configuration

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| mode | string | "balanced" | Optimization mode (conservative/balanced/aggressive) |
| focus_time_target_hours | float | 2.0 | Daily strategic time goal |
| meeting_batch_mode | bool | true | Group meetings together |

#### Personalization

| Parameter | Options | Description |
|-----------|---------|-------------|
| ceo_decision_style | analytical, intuitive, directive, collaborative | How recommendations are framed |
| communication_preference | concise, narrative, visual, detailed | Output format style |
| risk_tolerance | conservative, moderate, aggressive | Risk framing in recommendations |
| energy_pattern | morning_peak, afternoon_peak, even, night_owl | Energy optimization timing |

---

## Data Integration Patterns

### Input Data Formats

#### Intelligence Data Format

```json
{
  "team_health": {
    "timestamp": "2024-11-18T08:00:00Z",
    "health_score": 75,
    "engagement_score": 72,
    "turnover_risk": 15,
    "key_concerns": ["project_deadline", "resource_constraints"],
    "trending": "stable"
  },
  "project_status": {
    "projects": [
      {
        "name": "Product Launch",
        "status": "at_risk",
        "completion": 65,
        "blockers": ["vendor_delay"],
        "milestone_date": "2024-12-15"
      }
    ]
  },
  "financial_metrics": {
    "revenue_mtd": 850000,
    "runway_months": 14,
    "burn_rate": 420000,
    "burn_trend": "stable",
    "cash_position": 5900000
  },
  "customer_health": {
    "nps_score": 42,
    "churn_risk_accounts": 3,
    "expansion_opportunities": 5,
    "support_ticket_trend": "increasing"
  }
}
```

#### Stakeholder Data Format

```json
{
  "stakeholders": [
    {
      "id": "board-001",
      "name": "Sarah Chen",
      "role": "Board Chair",
      "category": "board",
      "influence_score": 95,
      "satisfaction_score": 82,
      "engagement_level": 88,
      "communication_style": "analytical",
      "relationship_status": "stable",
      "last_interaction": "2024-11-10T14:00:00Z",
      "interaction_frequency_days": 14,
      "key_concerns": ["growth_trajectory", "market_expansion"],
      "preferred_channels": ["in_person", "email"],
      "notes": "Prefers data-backed presentations"
    }
  ]
}
```

#### Calendar Data Format

```json
{
  "events": [
    {
      "id": "evt-001",
      "title": "Strategic Planning Session",
      "start": "2024-11-18T09:00:00Z",
      "end": "2024-11-18T11:00:00Z",
      "category": "strategic_thinking",
      "subcategory": "planning",
      "attendees": ["CEO", "CFO", "COO"],
      "energy_cost": 85,
      "outcome_quality": null,
      "notes": "Q1 planning"
    }
  ]
}
```

### Integration Approaches

#### 1. File-Based Integration (Simple)

```python
# Load data from JSON files
import json

def load_intelligence_data():
    with open('data/intelligence_data.json') as f:
        return json.load(f)

def load_stakeholder_data():
    with open('data/stakeholder_data.json') as f:
        return json.load(f)
```

#### 2. API Integration (Standard)

```python
# Fetch data from APIs
import requests

class DataIntegration:
    def __init__(self, config):
        self.config = config

    def fetch_team_health(self):
        response = requests.get(
            f"{self.config['hr_api']}/team-health",
            headers=self.get_auth_headers()
        )
        return response.json()

    def fetch_financial_metrics(self):
        response = requests.get(
            f"{self.config['finance_api']}/metrics",
            headers=self.get_auth_headers()
        )
        return response.json()
```

#### 3. Database Integration (Enterprise)

```python
# Connect to data warehouse
from sqlalchemy import create_engine
import pandas as pd

class DatabaseIntegration:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)

    def get_stakeholder_data(self):
        query = """
            SELECT * FROM stakeholders
            WHERE active = true
            ORDER BY influence_score DESC
        """
        return pd.read_sql(query, self.engine)

    def get_financial_metrics(self):
        query = """
            SELECT * FROM financial_metrics
            WHERE date = CURRENT_DATE
        """
        return pd.read_sql(query, self.engine)
```

### Calendar Integration

#### Google Calendar

```python
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

class GoogleCalendarIntegration:
    def __init__(self, credentials_path):
        self.creds = Credentials.from_authorized_user_file(credentials_path)
        self.service = build('calendar', 'v3', credentials=self.creds)

    def get_events(self, time_min, time_max):
        events_result = self.service.events().list(
            calendarId='primary',
            timeMin=time_min,
            timeMax=time_max,
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        return events_result.get('items', [])
```

#### Microsoft Outlook

```python
import msal
import requests

class OutlookCalendarIntegration:
    def __init__(self, config):
        self.config = config
        self.token = self._get_token()

    def get_events(self, start, end):
        endpoint = f"https://graph.microsoft.com/v1.0/me/calendar/events"
        headers = {'Authorization': f'Bearer {self.token}'}
        params = {
            '$filter': f"start/dateTime ge '{start}' and end/dateTime le '{end}'"
        }
        response = requests.get(endpoint, headers=headers, params=params)
        return response.json()['value']
```

---

## Customization Guide

### Adding Custom Signal Sources

```python
# In executive_intelligence_system.py

class CustomSignalSource:
    """Template for adding new signal sources"""

    def __init__(self, config):
        self.config = config
        self.source_name = "custom_source"

    def scan(self, data):
        """Scan data and return signals"""
        signals = []

        # Your custom detection logic here
        if self._detect_anomaly(data):
            signals.append(Signal(
                source=self.source_name,
                category="custom",
                priority=SignalPriority.WARNING,
                message="Custom anomaly detected",
                confidence=0.85,
                action_required="Review and assess",
                impact_score=7.5,
                stakeholders=["CEO"]
            ))

        return signals

    def _detect_anomaly(self, data):
        # Implement detection logic
        pass

# Register the source
intelligence_system.register_source(CustomSignalSource(config))
```

### Adding Custom Stakeholder Categories

```python
# In config/config.json

"stakeholder_configuration": {
  "categories": {
    "board": {"weight": 1.0, "engagement_days": 14},
    "investor": {"weight": 0.9, "engagement_days": 30},

    # Add custom category
    "government": {
      "weight": 0.85,
      "engagement_days": 30,
      "communication_style": "formal",
      "risk_multiplier": 1.5
    },

    "media": {
      "weight": 0.6,
      "engagement_days": 14,
      "communication_style": "narrative",
      "influence_type": "reputational"
    }
  }
}
```

### Custom Time Categories

```python
# In config/config.json

"optimization_configuration": {
  "time_allocation_targets": {
    # Add custom category
    "fundraising": {
      "target": 0.15,
      "min": 0.10,
      "max": 0.25,
      "description": "Investor meetings, pitch prep, due diligence"
    },

    "board_governance": {
      "target": 0.05,
      "min": 0.03,
      "max": 0.10,
      "description": "Board prep, governance, compliance"
    }
  }
}
```

### Custom Energy Profiles

```python
# In config/config.json

"optimization_configuration": {
  "energy_profiles": {
    "morning_peak": {
      "peak_hours": [8, 9, 10],
      "high_hours": [7, 11],
      "moderate_hours": [12, 13, 14],
      "low_hours": [15, 16, 17],
      "recovery_hours": [18, 19]
    },

    "split_peak": {
      "peak_hours": [9, 10, 15, 16],
      "high_hours": [8, 11, 14, 17],
      "moderate_hours": [12, 13],
      "low_hours": [7, 18],
      "recovery_hours": [19, 20]
    }
  }
}
```

---

## Security & Privacy

### Data Classification

| Classification | Examples | Handling Requirements |
|----------------|----------|----------------------|
| Confidential | Financial data, M&A plans | Encrypted at rest and transit, strict access |
| Sensitive | Stakeholder details, HR data | Encrypted, role-based access |
| Internal | Meeting notes, schedules | Standard protection |
| Public | Company announcements | Standard handling |

### Credential Management

**Never store credentials in code or config files.**

Recommended approaches:

1. **Environment Variables**
```python
import os

google_credentials = os.environ['GOOGLE_CREDENTIALS_PATH']
salesforce_token = os.environ['SALESFORCE_TOKEN']
```

2. **Secrets Manager**
```python
import boto3

def get_secret(secret_name):
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId=secret_name)
    return response['SecretString']
```

3. **HashiCorp Vault**
```python
import hvac

client = hvac.Client(url='https://vault.company.com')
secret = client.secrets.kv.v2.read_secret_version(path='ceo-advisor')
```

### Access Control

```python
# Example role-based access
ROLE_PERMISSIONS = {
    'ceo': ['all'],
    'chief_of_staff': ['daily_brief', 'stakeholder', 'calendar'],
    'executive_assistant': ['calendar', 'scheduling'],
    'analyst': ['read_only']
}

def check_permission(user_role, operation):
    if 'all' in ROLE_PERMISSIONS.get(user_role, []):
        return True
    return operation in ROLE_PERMISSIONS.get(user_role, [])
```

### Audit Logging

```python
import logging
from datetime import datetime

audit_logger = logging.getLogger('audit')
audit_logger.setLevel(logging.INFO)

def log_operation(user, operation, details):
    audit_logger.info({
        'timestamp': datetime.utcnow().isoformat(),
        'user': user,
        'operation': operation,
        'details': details
    })
```

---

## Enterprise Deployment

### Architecture Patterns

#### Single-User Deployment
```
CEO Device → CEO Advisor → Local Data Files
```

#### Team Deployment
```
Executive Team → Load Balancer → CEO Advisor Cluster → Shared Database
```

#### Enterprise Deployment
```
Multiple Executives → API Gateway → CEO Advisor Services → Data Warehouse
                                  ↓
                    Integration Layer → Calendar, CRM, Finance Systems
```

### High Availability Setup

```yaml
# kubernetes deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ceo-advisor
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ceo-advisor
  template:
    metadata:
      labels:
        app: ceo-advisor
    spec:
      containers:
      - name: ceo-advisor
        image: ceo-advisor:2.0.0
        resources:
          requests:
            memory: "512Mi"
            cpu: "250m"
          limits:
            memory: "1Gi"
            cpu: "500m"
        env:
        - name: CONFIG_PATH
          value: /config/config.json
        volumeMounts:
        - name: config
          mountPath: /config
      volumes:
      - name: config
        configMap:
          name: ceo-advisor-config
```

### Disaster Recovery

1. **Backup Configuration**: Daily backup of config.json and customizations
2. **Data Backup**: Regular backup of stakeholder data, history
3. **Recovery Time Objective (RTO)**: Target 4 hours
4. **Recovery Point Objective (RPO)**: Target 24 hours

---

## Operational Procedures

### Daily Operations Checklist

- [ ] Verify morning brief generated successfully
- [ ] Check for critical alerts
- [ ] Review system health metrics
- [ ] Validate data source connections
- [ ] Monitor error logs

### Weekly Maintenance

- [ ] Review and rotate logs
- [ ] Update stakeholder data
- [ ] Validate prediction accuracy
- [ ] Review and tune thresholds
- [ ] Backup configuration

### Monthly Review

- [ ] Analyze usage patterns
- [ ] Review and update benchmarks
- [ ] Validate ROI metrics
- [ ] Update documentation
- [ ] Plan improvements

### Incident Response

1. **Detection**: Automated monitoring alerts
2. **Triage**: Classify severity (P1-P4)
3. **Response**: Follow runbook for issue type
4. **Resolution**: Fix and verify
5. **Post-mortem**: Document and improve

---

## Monitoring & Alerting

### Key Metrics to Monitor

| Metric | Normal Range | Alert Threshold |
|--------|--------------|-----------------|
| Brief Generation Time | <30 seconds | >60 seconds |
| API Response Time | <500ms | >2000ms |
| Memory Usage | <70% | >85% |
| Error Rate | <1% | >5% |
| Data Freshness | <1 hour | >4 hours |

### Health Check Endpoint

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health_check():
    checks = {
        'database': check_database(),
        'external_apis': check_external_apis(),
        'config': check_config(),
        'disk_space': check_disk_space()
    }

    status = 'healthy' if all(checks.values()) else 'unhealthy'
    return jsonify({'status': status, 'checks': checks})
```

### Alerting Configuration

```yaml
# Example Prometheus alerting rules
groups:
- name: ceo-advisor
  rules:
  - alert: BriefGenerationSlow
    expr: ceo_advisor_brief_duration_seconds > 60
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: Brief generation is slow

  - alert: HighErrorRate
    expr: rate(ceo_advisor_errors_total[5m]) > 0.05
    for: 5m
    labels:
      severity: critical
    annotations:
      summary: High error rate detected
```

---

## Troubleshooting

### Common Issues

#### Issue: "No module found"
**Cause**: Missing Python dependencies
**Solution**:
```bash
pip install -r config/requirements.txt
```

#### Issue: "Config error"
**Cause**: Invalid JSON in configuration
**Solution**:
```bash
python -m json.tool config/config.json
```

#### Issue: "No data"
**Cause**: Missing sample or real data
**Solution**:
```bash
python examples/sample_data_generator.py
```

#### Issue: "Import error"
**Cause**: Python version incompatibility
**Solution**:
```bash
python --version  # Needs 3.8+
```

#### Issue: "Calendar integration failed"
**Cause**: Invalid credentials or permissions
**Solution**:
1. Verify credentials file exists
2. Check API permissions in Google/Microsoft admin
3. Regenerate OAuth tokens if expired

### Debug Mode

```bash
# Run with verbose logging
python src/ceo_advisor_orchestrator.py daily --debug

# Check specific module
python -c "from src.stakeholder_analytics import *; print('OK')"
```

### Log Analysis

```bash
# View recent errors
grep -i error logs/ceo_advisor.log | tail -50

# View warnings
grep -i warning logs/ceo_advisor.log | tail -50

# View by timestamp
grep "2024-11-18" logs/ceo_advisor.log
```

---

## Performance Optimization

### Caching Strategy

```python
from functools import lru_cache
from datetime import datetime, timedelta

class CachedDataProvider:
    def __init__(self):
        self._cache = {}
        self._cache_duration = timedelta(minutes=15)

    def get_stakeholder_data(self):
        cache_key = 'stakeholders'
        if self._is_cache_valid(cache_key):
            return self._cache[cache_key]['data']

        data = self._fetch_stakeholder_data()
        self._cache[cache_key] = {
            'data': data,
            'timestamp': datetime.now()
        }
        return data

    def _is_cache_valid(self, key):
        if key not in self._cache:
            return False
        age = datetime.now() - self._cache[key]['timestamp']
        return age < self._cache_duration
```

### Parallel Processing

```python
from concurrent.futures import ThreadPoolExecutor

def generate_comprehensive_brief():
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {
            'intelligence': executor.submit(generate_intelligence_report),
            'stakeholders': executor.submit(analyze_stakeholder_portfolio),
            'optimization': executor.submit(optimize_ceo_time_energy),
            'strategy': executor.submit(get_strategic_context),
            'financial': executor.submit(get_financial_health)
        }

        results = {
            name: future.result()
            for name, future in futures.items()
        }

    return compile_brief(results)
```

### Memory Management

```python
import gc

def process_large_dataset(data):
    # Process in chunks
    chunk_size = 1000
    results = []

    for i in range(0, len(data), chunk_size):
        chunk = data[i:i + chunk_size]
        result = process_chunk(chunk)
        results.append(result)

        # Explicitly free memory
        del chunk
        gc.collect()

    return combine_results(results)
```

---

## Future Integration Roadmap

### v3.0.0 - Connected Intelligence (Q1 2025)

| Integration | Status | Priority |
|-------------|--------|----------|
| Google Calendar | In Development | High |
| Microsoft Outlook | Planned | High |
| Salesforce CRM | Planned | High |
| Slack | Planned | Medium |
| HubSpot | Planned | Medium |

### v4.0.0 - Predictive Learning (Q3 2025)

| Feature | Status | Description |
|---------|--------|-------------|
| Pattern Learning | Planned | ML on decision patterns |
| Personalized Recommendations | Planned | Adaptive suggestions |
| Automated Actions | Planned | Trigger-based automation |
| Voice Interface | Research | Voice-activated queries |

### v5.0.0 - Collaborative Intelligence (Q1 2026)

| Feature | Status | Description |
|---------|--------|-------------|
| Multi-Executive Support | Planned | Board-level collaboration |
| Team Delegation | Planned | Direct team integration |
| External Advisors | Research | Third-party expert connection |

---

## Support & Resources

### Documentation
- `README.md` - Overview and quick start
- `SKILL.md` - Complete operational specification
- `QUICK-START.md` - 5-minute onboarding
- `INDEX.md` - Quick reference

### Getting Help
1. Check troubleshooting section above
2. Review logs for specific errors
3. Validate configuration with JSON tool
4. Run system tests

### Contributing
1. Follow existing code patterns
2. Add tests for new features
3. Update documentation
4. Submit pull request with description

---

*This implementation guide will be updated as new features and integrations are released.*
