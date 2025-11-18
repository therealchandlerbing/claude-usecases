# AI Ethics Advisor

**Comprehensive AI ethics and responsible AI development specialist**

## Overview

The AI Ethics Advisor is a comprehensive skill system for building, deploying, and monitoring AI systems that are fair, transparent, accountable, and aligned with human values. It provides everything you need from rapid ethics screens to comprehensive impact assessments.

## Key Capabilities

- **Bias Assessment**: Detect and measure bias across demographic groups using industry-standard fairness metrics
- **Fairness Evaluation**: Statistical parity, equalized odds, disparate impact ratio, and more
- **Regulatory Compliance**: EU AI Act, NIST AI RMF, GDPR, sector-specific regulations
- **Community Impact Analysis**: Stakeholder mapping, power dynamics, accessibility evaluation
- **Technical Implementation**: Production-ready bias monitoring code, explainability tools, privacy-preserving ML
- **Incident Response**: Protocols for detecting and responding to bias incidents

## What's Included

| File | Purpose |
|------|---------|
| **SKILL.md** | Complete operational specification and framework |
| **README.md** | This overview document |
| **QUICK-START.md** | 15-minute onboarding guide |
| **ASSESSMENT-TEMPLATES.md** | Ready-to-use assessment templates |
| **IMPLEMENTATION-GUIDE.md** | Code examples and CI/CD integration |

## When to Use

### Trigger Patterns

This skill activates when encountering:
- Bias or fairness concerns
- Ethical AI or responsible AI discussions
- AI safety or alignment questions
- Algorithmic justice considerations
- AI regulation or compliance needs
- Discrimination analysis
- Equity or disparate impact evaluation
- Model audit requests
- AI governance planning

### Risk-Based Approach

**Tier 1: Rapid Screen (15-30 minutes)**
- Early exploration, low-risk systems
- Quick sanity checks
- <1,000 users

**Tier 2: Comprehensive Assessment (2-4 hours)**
- Moderate-risk systems
- Human oversight present
- 1,000-100,000 users

**Tier 3: Full Impact Assessment (Days-Weeks)**
- High-risk domains (employment, lending, healthcare, criminal justice)
- >100,000 users
- Regulatory requirements

## Quick Example

```python
from bias_monitor import BiasMonitor

# Initialize monitoring
monitor = BiasMonitor(
    protected_attributes=['race', 'gender', 'age'],
    fairness_thresholds={
        'statistical_parity': 0.10,
        'disparate_impact': 0.80
    }
)

# Evaluate fairness
results = monitor.evaluate_fairness(
    predictions=y_pred,
    actuals=y_true,
    demographics=demographic_data
)

# Check for violations
if monitor.violation_log:
    trigger_incident_response()
```

## Core Philosophy

AI systems are **sociotechnical systems** that encode values, redistribute power, and shape access to opportunity. Ethics work is not compliance theater - it's about ensuring AI serves all people equitably and strengthens rather than undermines human agency and dignity.

### Foundational Principles

1. **Fairness** - Equitable treatment and outcomes across all demographic groups
2. **Transparency** - Explainable AI decision-making that affected communities can understand
3. **Accountability** - Clear responsibility chains and mechanisms for redress
4. **Privacy & Consent** - Data protection respecting individual agency
5. **Human Agency** - Preserving meaningful human control
6. **Non-Maleficence** - "Do no harm" considering direct and indirect impacts
7. **Inclusion & Access** - Expanding rather than restricting opportunity

## Getting Started

1. **Quick decisions**: Start with `QUICK-START.md`
2. **Comprehensive evaluation**: Use templates in `ASSESSMENT-TEMPLATES.md`
3. **Technical implementation**: Follow `IMPLEMENTATION-GUIDE.md`

## Model & Tools

- **Model**: opus (for comprehensive ethical analysis)
- **Tools**: Read, Write, WebSearch, Grep

## Success Metrics

### Leading Indicators
- % of AI projects with ethics review
- Time from project start to ethics review
- % of assessments including community engagement

### Lagging Indicators
- % of systems meeting fairness thresholds
- Reduction in bias incidents over time
- User understanding of AI role (survey)

## Remember

- Ethics is everyone's responsibility, not just the ethics team
- Fairness requires ongoing work, not one-time assessment
- Context matters immensely - there are few universal answers
- Perfection is impossible - aim for continuous improvement
- Listen to affected communities - they are the experts on their experience

---

**Version**: 1.0.0
**Created**: 2024-11-18
**Author**: Claude Usecases Repository
