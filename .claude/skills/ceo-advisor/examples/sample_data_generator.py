#!/usr/bin/env python3
"""
Sample Data Generator for CEO Advisor Testing

Generates realistic sample data for testing all CEO advisor modules.
"""

import json
import random
from datetime import datetime, timedelta


def generate_intelligence_data():
    """Generate sample intelligence data"""
    return {
        'team_health': {
            'health_score': random.randint(40, 90),
            'engagement': random.randint(50, 95),
            'turnover_risk': random.randint(5, 25)
        },
        'project_status': {
            'health_score': random.randint(50, 95),
            'on_track': random.randint(60, 90),
            'at_risk': random.randint(5, 30)
        },
        'financial_metrics': {
            'health_score': random.randint(45, 95),
            'runway_months': random.randint(12, 36),
            'burn_rate': random.randint(100000, 500000)
        },
        'customer_health': {
            'health_score': random.randint(60, 95),
            'nps': random.randint(30, 80),
            'churn_risk': random.randint(5, 20)
        },
        'competitive_intelligence': {
            'threat_level': random.randint(30, 80),
            'new_entrants': random.randint(0, 5),
            'competitive_moves': random.randint(0, 10)
        },
        'investor_sentiment': {
            'threat_level': random.randint(20, 60),
            'confidence_score': random.randint(60, 90)
        },
        'market_dynamics': {
            'opportunity_score': random.randint(50, 95),
            'market_growth': random.randint(-5, 25)
        }
    }


def generate_stakeholder_data():
    """Generate sample stakeholder data"""
    stakeholders = []

    # Board members
    board_members = [
        {'name': 'John Smith', 'role': 'Board Chair'},
        {'name': 'Mary Johnson', 'role': 'Lead Independent Director'},
        {'name': 'Robert Williams', 'role': 'Board Member'}
    ]

    for member in board_members:
        stakeholders.append({
            'name': member['name'],
            'role': member['role'],
            'category': 'Board',
            'influence_score': random.randint(85, 100),
            'satisfaction_score': random.randint(60, 95),
            'engagement_level': random.randint(70, 95),
            'communication_style': random.choice(['analytical', 'driver', 'expressive', 'amiable']),
            'relationship_status': random.choice(['excellent', 'stable', 'strengthening']),
            'last_interaction_days_ago': random.randint(1, 14),
            'interaction_frequency_days': 7,
            'key_concerns': random.sample(['Revenue growth', 'Profitability', 'Market share',
                                          'Competition', 'Team scaling', 'Product roadmap'], 2),
            'preferred_channels': ['In-person', 'Email']
        })

    # Investors
    investors = [
        {'name': 'Sarah Davis', 'role': 'Lead Investor'},
        {'name': 'Michael Chen', 'role': 'Investor'}
    ]

    for investor in investors:
        stakeholders.append({
            'name': investor['name'],
            'role': investor['role'],
            'category': 'Investor',
            'influence_score': random.randint(80, 95),
            'satisfaction_score': random.randint(55, 90),
            'engagement_level': random.randint(60, 90),
            'communication_style': random.choice(['analytical', 'driver', 'expressive']),
            'relationship_status': random.choice(['stable', 'strengthening', 'weakening']),
            'last_interaction_days_ago': random.randint(5, 30),
            'interaction_frequency_days': 14,
            'key_concerns': random.sample(['Returns', 'Exit strategy', 'Market timing',
                                          'Burn rate', 'Valuation'], 2),
            'preferred_channels': ['Video call', 'Phone']
        })

    # Executives
    executives = [
        {'name': 'Alice Brown', 'role': 'CTO'},
        {'name': 'David Wilson', 'role': 'CFO'},
        {'name': 'Emma Martinez', 'role': 'COO'}
    ]

    for exec in executives:
        stakeholders.append({
            'name': exec['name'],
            'role': exec['role'],
            'category': 'Executive',
            'influence_score': random.randint(75, 90),
            'satisfaction_score': random.randint(65, 95),
            'engagement_level': random.randint(80, 100),
            'communication_style': random.choice(['analytical', 'driver', 'amiable']),
            'relationship_status': random.choice(['excellent', 'stable', 'strengthening']),
            'last_interaction_days_ago': random.randint(1, 7),
            'interaction_frequency_days': 3,
            'key_concerns': random.sample(['Team capacity', 'Resources', 'Priorities',
                                          'Strategy', 'Culture'], 2),
            'preferred_channels': ['In-person', 'Slack']
        })

    return stakeholders


def generate_calendar_data():
    """Generate sample calendar data"""
    now = datetime.now()
    calendar = []

    # Week of sample data
    for day in range(5):  # Monday to Friday
        current_day = now + timedelta(days=day)

        # Morning strategy session
        calendar.append({
            'start_time': current_day.replace(hour=8, minute=0).isoformat(),
            'end_time': current_day.replace(hour=9, minute=30).isoformat(),
            'category': 'strategic_thinking',
            'subcategory': 'strategy_session',
            'energy_cost': random.randint(75, 90),
            'value_created': random.randint(80, 95),
            'attendees': ['CEO', 'Strategy Team'],
            'outcome_quality': random.randint(75, 95),
            'notes': 'Weekly strategy review'
        })

        # Executive meeting
        calendar.append({
            'start_time': current_day.replace(hour=10, minute=0).isoformat(),
            'end_time': current_day.replace(hour=11, minute=0).isoformat(),
            'category': 'team_leadership',
            'subcategory': 'executive_meeting',
            'energy_cost': random.randint(60, 75),
            'value_created': random.randint(70, 85),
            'attendees': ['CEO', 'Executive Team'],
            'outcome_quality': random.randint(70, 90),
            'notes': 'Executive team sync'
        })

        # Customer meeting
        calendar.append({
            'start_time': current_day.replace(hour=14, minute=0).isoformat(),
            'end_time': current_day.replace(hour=15, minute=0).isoformat(),
            'category': 'customer_interaction',
            'subcategory': 'customer_meeting',
            'energy_cost': random.randint(50, 65),
            'value_created': random.randint(75, 90),
            'attendees': ['CEO', 'Customer'],
            'outcome_quality': random.randint(80, 95),
            'notes': 'Customer business review'
        })

        # Operational review
        calendar.append({
            'start_time': current_day.replace(hour=16, minute=0).isoformat(),
            'end_time': current_day.replace(hour=17, minute=0).isoformat(),
            'category': 'operational_oversight',
            'subcategory': 'operations_review',
            'energy_cost': random.randint(40, 55),
            'value_created': random.randint(50, 70),
            'attendees': ['CEO', 'Operations Team'],
            'outcome_quality': random.randint(60, 80),
            'notes': 'Weekly ops review'
        })

    return calendar


def generate_test_scenarios():
    """Generate crisis test scenarios"""
    return [
        {
            'scenario': 'Major Customer Churn',
            'description': 'Top customer threatening to leave due to product issues',
            'severity': 'high',
            'category': 'customer'
        },
        {
            'scenario': 'Key Executive Departure',
            'description': 'CTO resigned with 2-week notice',
            'severity': 'high',
            'category': 'talent'
        },
        {
            'scenario': 'Competitive Threat',
            'description': 'Major competitor launched similar product',
            'severity': 'medium',
            'category': 'market'
        },
        {
            'scenario': 'Funding Shortfall',
            'description': 'Burn rate higher than expected, runway at risk',
            'severity': 'high',
            'category': 'financial'
        },
        {
            'scenario': 'PR Crisis',
            'description': 'Negative media coverage on company practices',
            'severity': 'medium',
            'category': 'reputation'
        }
    ]


def main():
    """Generate all sample data files"""
    print("Generating sample data for CEO Advisor...")

    # Generate intelligence data
    intelligence_data = generate_intelligence_data()
    with open('sample_intelligence_data.json', 'w') as f:
        json.dump(intelligence_data, f, indent=2)
    print("✓ Generated sample_intelligence_data.json")

    # Generate stakeholder data
    stakeholder_data = generate_stakeholder_data()
    with open('sample_stakeholder_data.json', 'w') as f:
        json.dump(stakeholder_data, f, indent=2)
    print("✓ Generated sample_stakeholder_data.json")

    # Generate calendar data
    calendar_data = generate_calendar_data()
    with open('sample_calendar_data.json', 'w') as f:
        json.dump(calendar_data, f, indent=2)
    print("✓ Generated sample_calendar_data.json")

    # Generate test scenarios
    test_scenarios = generate_test_scenarios()
    with open('test_scenarios.json', 'w') as f:
        json.dump(test_scenarios, f, indent=2)
    print("✓ Generated test_scenarios.json")

    # Generate combined dataset
    combined_data = {
        'intelligence': intelligence_data,
        'stakeholders': stakeholder_data,
        'calendar': calendar_data,
        'test_scenarios': test_scenarios,
        'generated_at': datetime.now().isoformat()
    }

    with open('sample_data_complete.json', 'w') as f:
        json.dump(combined_data, f, indent=2)
    print("✓ Generated sample_data_complete.json")

    print("\nSample data generation complete!")
    print("\nGenerated files:")
    print("  - sample_intelligence_data.json")
    print("  - sample_stakeholder_data.json")
    print("  - sample_calendar_data.json")
    print("  - test_scenarios.json")
    print("  - sample_data_complete.json")
    print("\nYou can now run the CEO advisor modules with realistic test data.")


if __name__ == "__main__":
    main()
