# Client Portfolio Health Workflow
## Specialized Reference for Board Packet Client Assessment

This file is loaded just-in-time when generating the Client Portfolio Health Report component of the board packet.

---

## Purpose

Transform Asana project data and Gmail communication patterns into an executive assessment of client relationship health, portfolio balance, and organizational capacity. This report identifies which relationships are thriving, which need attention, and whether the portfolio supports sustainable growth.

---

## Data Inputs

### From Asana Client Delivery Hub

**Project-Level Data**:
- Client name
- Contract value
- Probability percentage
- Stage (Proposal, Negotiation, Signed, Delivered, Invoiced, Paid)
- Client tier (Tier 1 Strategic, Tier 2 Major, Tier 3 Standard)
- Project type/service
- Start date
- Expected completion date
- Last project update date
- Assigned team members
- Custom fields (if available)

**Task-Level Data** (within each project):
- Open tasks vs. completed tasks
- Overdue tasks
- Task completion velocity
- Recent activity patterns

### From Gmail

**Communication Metrics** (last 60 days):
- Email interaction count (sent + received) per client
- Last communication date
- Communication frequency trend (increasing/decreasing)
- Sentiment indicators (if tone analysis available)

### From QuickBooks

**Financial Relationship Data**:
- Total revenue from client (all-time)
- Revenue this year
- Payment reliability (average days to payment)
- Outstanding receivables (if any)

---

## Dashboard Structure

### 1. Executive Summary (1 Paragraph)

Synthesize portfolio health in 3-5 sentences:

**Template**:
"360's client portfolio comprises [X] active relationships generating $[Y] in contracted value, with [Z] Tier 1 strategic partners representing [%] of total value. Portfolio health is [strong/mixed/concerning] with [X] clients showing green status, [Y] yellow (requiring attention), and [Z] red (immediate action needed). The organization is operating at [X]% capacity utilization, [indicating sustainable growth headroom / suggesting near-term capacity constraints]. [Major opportunity or risk, e.g., 'The SpacePlan JV represents a significant growth opportunity but also concentration risk at [X]% of portfolio value.']"

**Key elements**:
- Portfolio size and value
- Tier 1 strategic partner count
- Health distribution (green/yellow/red)
- Capacity utilization assessment
- One critical opportunity or risk

---

### 2. Tier 1 Strategic Partner Deep Dives

For each Tier 1 partner (SpacePlan, GenIP, ScienceLink, NanoBioPlus, CNEN), create detailed assessment.

#### Template for Each Partner

**[PARTNER NAME]**
**Relationship Status**: 🟢 Green / 🟡 Yellow / 🔴 Red

**Overview**:
[1-2 sentences describing the partnership nature and strategic importance]

**Current Engagement**:
- **Contract Value**: $[X]
- **Stage**: [Current stage]
- **Project Type**: [Description]
- **Timeline**: [Start date] - [Expected completion]
- **Team**: [Assigned team members]

**Relationship Health Indicators**:
- **Communication**: [X] interactions in last 60 days | Last contact: [date]
- **Project Activity**: Last updated [X] days ago | [Y] open tasks, [Z] overdue
- **Financial**: $[X] revenue YTD | [Payment pattern, e.g., "Pays within 30 days" or "AR: $X outstanding"]

**Recent Milestones**:
- [Milestone 1 with date]
- [Milestone 2 with date]
- [Upcoming milestone]

**Opportunities**:
- [Expansion potential, additional services, partnership leverage]

**Risks/Concerns**:
- [Any red/yellow flags: communication gaps, scope creep, payment delays, resource constraints]

**Next Steps**:
- [Immediate actions or decisions needed]
- [Timeline for next major milestone]

**Board Attention Needed**: [Yes/No - If yes, specify what]

---

#### Tier 1 Partner Specifications

**SpacePlan / 360 Space Innovation Studios JV**:
- **Strategic Importance**: Joint venture, major growth vehicle
- **Key Metrics**: JV equity stake, technology licensing value, projected revenue impact
- **Health Factors**:
  - JV governance meetings happening on schedule?
  - Technology licensing agreements finalized?
  - Partner satisfaction with collaboration?
  - Revenue projections on track?

**GenIP Partnership**:
- **Strategic Importance**: IP commercialization framework partner
- **Key Metrics**: Number of IP assets under management, licensing pipeline value
- **Health Factors**:
  - Active IP assets being commercialized?
  - Pipeline of new opportunities?
  - Partner engagement in deal sourcing?

**ScienceLink Franchise**:
- **Strategic Importance**: Scalable business model, international reach potential
- **Key Metrics**: Franchise development stage, territory discussions, revenue model
- **Health Factors**:
  - Franchise framework development on track?
  - Territory partner discussions progressing?
  - Legal/compliance work completed?

**NanoBioPlus Strategic Collaboration**:
- **Strategic Importance**: Deep tech sector entry, strategic advisory positioning
- **Key Metrics**: Advisory scope, potential equity/revenue arrangements
- **Health Factors**:
  - Engagement frequency adequate?
  - Value delivery clear?
  - Expansion opportunities identified?

**CNEN Nuclear Innovation Program**:
- **Strategic Importance**: Brazil market entry, government sector credibility
- **Key Metrics**: Program scope, timeline, budget allocation
- **Health Factors**:
  - Government approvals on schedule?
  - Budget drawdown proceeding?
  - Stakeholder alignment maintained?

---

### 3. Portfolio Analytics

#### 3.1 Portfolio Summary Table

| Client Tier | # of Clients | Total Contract Value | % of Portfolio | Avg Contract Size |
|-------------|--------------|---------------------|----------------|-------------------|
| Tier 1 Strategic | [X] | $[Y] | [Z]% | $[A] |
| Tier 2 Major | [X] | $[Y] | [Z]% | $[A] |
| Tier 3 Standard | [X] | $[Y] | [Z]% | $[A] |
| **Total** | **[X]** | **$[Y]** | **100%** | **$[A]** |

**Narrative**:
"The portfolio is [concentrated/balanced/diversified] with Tier 1 strategic partners representing [X]% of total value. [Interpretation: healthy diversification / concerning concentration / appropriate for current stage]."

#### 3.2 Health Status Distribution

| Status | # of Clients | Total Value | % of Portfolio | Clients |
|--------|--------------|-------------|----------------|---------|
| 🟢 Green (Healthy) | [X] | $[Y] | [Z]% | [List names] |
| 🟡 Yellow (Attention Needed) | [X] | $[Y] | [Z]% | [List names] |
| 🔴 Red (Immediate Action) | [X] | $[Y] | [Z]% | [List names] |

**Flag**: If >20% of portfolio value in yellow/red status, note: "⚠️ Portfolio risk: [X]% of value requires management attention."

#### 3.3 Client Concentration Analysis

**Top 3 Clients**:
1. [Client 1]: $[X] ([Y]% of portfolio)
2. [Client 2]: $[X] ([Y]% of portfolio)
3. [Client 3]: $[X] ([Y]% of portfolio)

**Top 3 Total**: $[X] ([Y]% of portfolio)

**Herfindahl-Hirschman Index (HHI)**: [Calculate if possible - sum of squared market shares]

**Interpretation**:
- HHI <1500: Healthy diversification
- HHI 1500-2500: Moderate concentration
- HHI >2500: High concentration risk

#### 3.4 Client Lifecycle Distribution

| Stage | # of Clients | Total Value | Avg Time in Stage |
|-------|--------------|-------------|-------------------|
| Proposal | [X] | $[Y] | [Z] days |
| Negotiation | [X] | $[Y] | [Z] days |
| Signed | [X] | $[Y] | [Z] days |
| Delivered | [X] | $[Y] | [Z] days |
| Invoiced | [X] | $[Y] | [Z] days |
| Paid | [X] | $[Y] | - |

**Pipeline Velocity**:
- Average proposal-to-signed: [X] days
- Average signed-to-paid: [Y] days
- Total cycle time: [Z] days

**Bottlenecks**:
- [Identify any stage with unusually long average time]

#### 3.5 Retention & Acquisition

**Retention Metrics** (if historical data available):
- Client retention rate: [X]% (clients active this year who were active last year)
- Revenue retention: [Y]% (revenue from returning clients)
- Expansion revenue: $[Z] (additional revenue from existing clients)

**Acquisition Metrics**:
- New clients this year: [X]
- Total new client value: $[Y]
- Average new client acquisition cost: $[Z] (if trackable)

**Acquisition Funnel**:
- Proposals sent: [X]
- Negotiations reached: [Y] ([Z]% conversion)
- Contracts signed: [A] ([B]% conversion)
- Overall win rate: [C]%

---

### 4. Capacity Analysis

#### 4.1 Team Utilization

**Available Capacity**:
- Chandler Lewis: [X] hours/month available for client work
- Claude Amar: [Y] hours/month
- Yiyun: [Z] hours/month
- Felipe (Brazil operations): [A] hours/month
- Other team/contractors: [B] hours/month
- **Total Available**: [C] hours/month

**Current Commitments**:
From Asana project assignments, calculate hours allocated:
- SpacePlan JV: [X] hours/month
- GenIP: [Y] hours/month
- [Continue for all active projects]
- **Total Committed**: [Z] hours/month

**Utilization**:
- Utilization rate: [Committed ÷ Available]%
- Available capacity: [Available - Committed] hours/month

**Capacity Thresholds**:
- <70%: Under-utilized, room for growth
- 70-85%: Optimal, sustainable
- 85-95%: Near capacity, limited new work possible
- >95%: Over-committed, quality/delivery risk

**Flag**: If >90% utilization, note: "⚠️ Capacity constraint: Organization at [X]% utilization. Limited capacity for new work without additional resources or project completion."

#### 4.2 Capacity by Client Tier

| Tier | Hours Committed | % of Total Capacity | Value per Hour |
|------|----------------|---------------------|----------------|
| Tier 1 Strategic | [X] | [Y]% | $[Z]/hr |
| Tier 2 Major | [X] | [Y]% | $[Z]/hr |
| Tier 3 Standard | [X] | [Y]% | $[Z]/hr |

**Strategic Alignment**:
"Tier 1 strategic partners consume [X]% of capacity and generate [Y]% of revenue. [This allocation is appropriate for strategic priorities / Consider rebalancing toward higher-value work]."

#### 4.3 Capacity Planning

**Current Quarter Capacity Outlook**:
- Projects completing: [List projects ending this quarter]
- Capacity freed: [X] hours/month
- Projects starting: [List new projects]
- New capacity needed: [Y] hours/month
- Net capacity change: [±Z] hours/month

**Next Quarter Projections**:
Based on pipeline (from Asana):
- Projects likely to close: [List with probability]
- Estimated capacity needed: [X] hours/month
- Gap/surplus: [±Y] hours/month

**Recommendation**:
"[If gap: 'To support pipeline conversion, 360 will need to add [X] hours/month capacity through hiring, contracting, or efficiency gains.' / If surplus: 'Current capacity is adequate to support projected growth.']"

---

### 5. Relationship Health Scoring

#### Scoring Methodology

For each client, calculate composite health score (0-100):

**Communication Health (30 points)**:
- 10+ interactions/60 days: 30 points
- 5-9 interactions: 20 points
- 2-4 interactions: 10 points
- 0-1 interactions: 0 points

**Project Activity Health (30 points)**:
- Updated within 7 days: 30 points
- Updated 8-14 days ago: 20 points
- Updated 15-30 days ago: 10 points
- Updated >30 days ago: 0 points

**Financial Health (25 points)**:
- No outstanding AR, pays <30 days: 25 points
- Pays 31-60 days: 15 points
- Pays 61-90 days or has small AR: 10 points
- >90 days or significant AR: 0 points

**Deliverable Health (15 points)**:
- No overdue tasks: 15 points
- 1-2 overdue tasks: 10 points
- 3-5 overdue tasks: 5 points
- >5 overdue tasks: 0 points

**Status Assignment**:
- 80-100 points: 🟢 Green (Healthy)
- 60-79 points: 🟡 Yellow (Attention Needed)
- <60 points: 🔴 Red (Immediate Action)

#### Health Score Table

| Client | Communication | Activity | Financial | Deliverables | Total | Status |
|--------|--------------|----------|-----------|--------------|-------|--------|
| [Client 1] | [X]/30 | [Y]/30 | [Z]/25 | [A]/15 | [B]/100 | 🟢/🟡/🔴 |
| [Continue for all active clients] |

---

## Data Collection Logic

### Asana Project Data

```python
def collect_client_portfolio_data():
    """Collect comprehensive client portfolio data from Asana"""

    portfolio_gid = "1211712180134240"
    projects = asana_get_items_for_portfolio(portfolio_gid)

    portfolio = []

    for project in projects:
        project_data = asana_get_project(project['gid'])

        # Extract custom fields
        contract_value = get_custom_field(project_data, 'contract_value')
        probability = get_custom_field(project_data, 'probability')
        stage = get_custom_field(project_data, 'stage')
        client_tier = get_custom_field(project_data, 'client_tier')
        start_date = get_custom_field(project_data, 'start_date')
        expected_completion = get_custom_field(project_data, 'expected_completion')

        # Get task metrics
        tasks = asana_get_tasks(project_gid=project['gid'])
        open_tasks = [t for t in tasks if not t['completed']]
        overdue_tasks = [t for t in open_tasks if t['due_on'] and t['due_on'] < date.today()]

        # Get assigned team members
        team_members = [m['name'] for m in project_data.get('members', [])]

        # Calculate days since last update
        last_modified = datetime.fromisoformat(project_data['modified_at'].replace('Z', '+00:00'))
        days_since_update = (datetime.now(timezone.utc) - last_modified).days

        portfolio.append({
            'client_name': project_data['name'],
            'contract_value': contract_value,
            'probability': probability,
            'stage': stage,
            'client_tier': client_tier,
            'start_date': start_date,
            'expected_completion': expected_completion,
            'team_members': team_members,
            'open_tasks': len(open_tasks),
            'overdue_tasks': len(overdue_tasks),
            'completed_tasks': len([t for t in tasks if t['completed']]),
            'days_since_update': days_since_update,
            'project_gid': project['gid']
        })

    return portfolio
```

### Gmail Communication Analysis

```python
def analyze_client_communications(client_names):
    """Analyze email communication patterns for each client"""

    communication_data = {}

    for client in client_names:
        # Search for emails in last 60 days
        query = f'(from:*{client}* OR to:*{client}*) after:{60_days_ago}'
        messages = search_gmail_messages(query=query)

        # Count interactions
        interaction_count = len(messages)

        # Find last interaction date
        if messages:
            last_message = messages[0]  # Assuming sorted by date desc
            last_contact = last_message['internalDate']
        else:
            last_contact = None

        # Calculate trend (compare last 30 days to prior 30 days)
        query_recent = f'(from:*{client}* OR to:*{client}*) after:{30_days_ago}'
        query_prior = f'(from:*{client}* OR to:*{client}*) after:{60_days_ago} before:{30_days_ago}'
        recent_count = len(search_gmail_messages(query=query_recent))
        prior_count = len(search_gmail_messages(query=query_prior))

        trend = "increasing" if recent_count > prior_count else "decreasing" if recent_count < prior_count else "stable"

        communication_data[client] = {
            'interaction_count_60d': interaction_count,
            'last_contact_date': last_contact,
            'trend': trend,
            'recent_activity': recent_count,
            'prior_activity': prior_count
        }

    return communication_data
```

### Capacity Calculation

```python
def calculate_capacity_utilization(portfolio, team_capacity):
    """Calculate team capacity utilization based on project assignments"""

    # Define available capacity (hours/month per team member)
    available_capacity = {
        'Chandler Lewis': team_capacity.get('chandler', 80),  # hours/month
        'Claude Amar': team_capacity.get('claude', 120),
        'Yiyun': team_capacity.get('yiyun', 160),
        'Felipe': team_capacity.get('felipe', 80)
    }

    total_available = sum(available_capacity.values())

    # Estimate committed capacity
    # Simple heuristic: Tier 1 = 40 hrs/month, Tier 2 = 20 hrs/month, Tier 3 = 10 hrs/month
    tier_hours = {
        'Tier 1 Strategic': 40,
        'Tier 2 Major': 20,
        'Tier 3 Standard': 10
    }

    committed_capacity = {}
    for person in available_capacity.keys():
        committed_capacity[person] = 0

    for project in portfolio:
        if project['stage'] in ['Signed', 'Delivered']:  # Active work
            hours_needed = tier_hours.get(project['client_tier'], 15)

            # Distribute hours among assigned team members
            if project['team_members']:
                hours_per_person = hours_needed / len(project['team_members'])
                for member in project['team_members']:
                    if member in committed_capacity:
                        committed_capacity[member] += hours_per_person

    total_committed = sum(committed_capacity.values())
    utilization_rate = (total_committed / total_available * 100) if total_available > 0 else 0

    return {
        'total_available': total_available,
        'total_committed': total_committed,
        'utilization_rate': utilization_rate,
        'by_person': {
            person: {
                'available': available_capacity[person],
                'committed': committed_capacity[person],
                'utilization': (committed_capacity[person] / available_capacity[person] * 100)
            }
            for person in available_capacity.keys()
        }
    }
```

### Health Scoring

```python
def calculate_health_score(client_data, communication_data, financial_data):
    """Calculate composite health score for a client"""

    client_name = client_data['client_name']

    # Communication health (30 points)
    comm = communication_data.get(client_name, {})
    interaction_count = comm.get('interaction_count_60d', 0)

    if interaction_count >= 10:
        comm_score = 30
    elif interaction_count >= 5:
        comm_score = 20
    elif interaction_count >= 2:
        comm_score = 10
    else:
        comm_score = 0

    # Activity health (30 points)
    days_since_update = client_data['days_since_update']

    if days_since_update <= 7:
        activity_score = 30
    elif days_since_update <= 14:
        activity_score = 20
    elif days_since_update <= 30:
        activity_score = 10
    else:
        activity_score = 0

    # Financial health (25 points)
    fin = financial_data.get(client_name, {})
    avg_days_to_pay = fin.get('avg_days_to_pay', 30)
    outstanding_ar = fin.get('outstanding_ar', 0)

    if outstanding_ar == 0 and avg_days_to_pay <= 30:
        financial_score = 25
    elif avg_days_to_pay <= 60:
        financial_score = 15
    elif avg_days_to_pay <= 90 or outstanding_ar < 5000:
        financial_score = 10
    else:
        financial_score = 0

    # Deliverable health (15 points)
    overdue_tasks = client_data['overdue_tasks']

    if overdue_tasks == 0:
        deliverable_score = 15
    elif overdue_tasks <= 2:
        deliverable_score = 10
    elif overdue_tasks <= 5:
        deliverable_score = 5
    else:
        deliverable_score = 0

    # Total score
    total_score = comm_score + activity_score + financial_score + deliverable_score

    # Status
    if total_score >= 80:
        status = "🟢 Green"
    elif total_score >= 60:
        status = "🟡 Yellow"
    else:
        status = "🔴 Red"

    return {
        'communication_score': comm_score,
        'activity_score': activity_score,
        'financial_score': financial_score,
        'deliverable_score': deliverable_score,
        'total_score': total_score,
        'status': status
    }
```

---

## Flag Generation Logic

```python
def generate_portfolio_flags(portfolio, capacity, health_scores):
    """Generate risk and opportunity flags for the portfolio"""

    flags = []

    # Concentration risk
    total_value = sum([p['contract_value'] for p in portfolio if p['contract_value']])
    if total_value > 0:
        for project in portfolio:
            if project['contract_value']:
                concentration = (project['contract_value'] / total_value * 100)
                if concentration > 40:
                    flags.append({
                        'severity': 'Warning',
                        'category': 'Concentration Risk',
                        'message': f'⚠️ {project["client_name"]} represents {concentration:.0f}% of portfolio value',
                        'recommendation': 'Diversify client base to reduce dependency'
                    })

    # Capacity constraint
    if capacity['utilization_rate'] > 90:
        flags.append({
            'severity': 'Critical' if capacity['utilization_rate'] > 95 else 'Warning',
            'category': 'Capacity',
            'message': f'⚠️ Team at {capacity["utilization_rate"]:.0f}% capacity utilization',
            'recommendation': 'Consider additional resources or prioritize high-value work'
        })

    # Stale projects
    for project in portfolio:
        if project['days_since_update'] > 14 and project['stage'] in ['Signed', 'Delivered']:
            flags.append({
                'severity': 'Info',
                'category': 'Project Management',
                'message': f'ℹ️ {project["client_name"]} not updated in {project["days_since_update"]} days',
                'recommendation': 'Update project status or close if complete'
            })

    # Low communication with Tier 1
    for project in portfolio:
        if project['client_tier'] == 'Tier 1 Strategic':
            # Check communication data
            # If <2 interactions in 60 days, flag
            pass  # Logic from communication analysis

    # Yellow/red clients with high value
    for client, health in health_scores.items():
        if health['status'] in ['🟡 Yellow', '🔴 Red']:
            project = next((p for p in portfolio if p['client_name'] == client), None)
            if project and project['contract_value'] > 10000:
                flags.append({
                    'severity': 'Warning',
                    'category': 'Relationship Health',
                    'message': f'⚠️ High-value client {client} ({health["status"]}) needs attention',
                    'recommendation': 'Review relationship and address issues proactively'
                })

    return flags
```

---

## Output Format (Markdown for Draft)

```markdown
# CLIENT PORTFOLIO HEALTH REPORT

## Executive Summary

[Generated summary paragraph]

---

## Tier 1 Strategic Partner Deep Dives

### SpacePlan / 360 Space Innovation Studios JV
**Relationship Status**: 🟢 Green

[Detailed assessment following template]

---

### GenIP Partnership
**Relationship Status**: 🟡 Yellow

[Detailed assessment]

---

[Continue for all Tier 1 partners]

---

## Portfolio Analytics

### Portfolio Summary

[Table: Portfolio by tier]

[Narrative on portfolio balance]

### Health Status Distribution

[Table: Clients by health status]

[Flag if >20% in yellow/red]

### Client Concentration Analysis

[Top 3 clients table and HHI calculation]

### Client Lifecycle Distribution

[Table: Clients by stage]

[Pipeline velocity metrics]

### Retention & Acquisition

[Metrics on retention and new client acquisition]

---

## Capacity Analysis

### Team Utilization

[Capacity calculation and utilization rate]

[Flag if >90% utilization]

### Capacity by Client Tier

[Table: Hours by tier]

[Strategic alignment assessment]

### Capacity Planning

[Current and next quarter projections]

[Recommendation on capacity needs]

---

## Relationship Health Scores

[Table: Health scores for all clients]

[Narrative on overall portfolio health]

---

*Portfolio data from Asana Client Delivery Hub as of [date]*
*Communication data from Gmail analysis (60-day window)*
*Financial data from QuickBooks as of [date]*
```

---

## User Interaction Points

**During data collection**:
- If client tier not set in Asana: "I don't see client_tier set for [list of projects]. Can you categorize these as Tier 1/2/3?"
- If capacity data unavailable: "To calculate utilization, how many hours/month is each team member available for client work?"

**During draft review**:
- "Here's the draft Client Portfolio Health Report. Key findings:
  - [X] clients in green status
  - [Y] clients need attention (yellow)
  - [Z] clients require immediate action (red)
  - Capacity utilization: [X]%

  Health flags:
  - [List all flags]

  Do these assessments match your view of the client relationships?"

**After user review**:
- "Updated Client Portfolio Health Report. [Summary of changes]. Ready for next document?"

---

*End of Client Portfolio Health Workflow*
