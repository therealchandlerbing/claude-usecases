#!/usr/bin/env python3
"""
Stakeholder Analytics System - AI-powered relationship tracking and optimization

Tracks, predicts, and optimizes stakeholder relationships through sentiment analysis
and influence mapping.
"""

import json
from typing import Dict, List
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from enum import Enum


class RelationshipStatus(Enum):
    STRENGTHENING = "↗️"
    STABLE = "→"
    WEAKENING = "↘️"
    CRITICAL = "⚠️"
    EXCELLENT = "⭐"


class CommunicationStyle(Enum):
    ANALYTICAL = "data-driven"
    DRIVER = "results-focused"
    EXPRESSIVE = "vision-oriented"
    AMIABLE = "relationship-focused"


@dataclass
class Stakeholder:
    name: str
    role: str
    category: str  # Board, Investor, Employee, Customer, Partner
    influence_score: float
    satisfaction_score: float
    engagement_level: float
    communication_style: CommunicationStyle
    relationship_status: RelationshipStatus
    last_interaction: datetime
    interaction_frequency_days: int
    key_concerns: List[str]
    preferred_channels: List[str]
    notes: str = ""
    relationship_history: List[Dict] = field(default_factory=list)


class StakeholderAnalytics:
    def __init__(self):
        self.stakeholder_weights = {
            'Board': 1.0,
            'Investor': 0.9,
            'Executive': 0.85,
            'Customer': 0.8,
            'Employee': 0.7,
            'Partner': 0.65
        }

    def analyze_stakeholder_portfolio(self, stakeholders: List[Stakeholder]) -> Dict:
        """Comprehensive analysis of all stakeholder relationships"""
        analysis = {
            'portfolio_health': self._calculate_portfolio_health(stakeholders),
            'risk_matrix': self._create_risk_matrix(stakeholders),
            'engagement_recommendations': self._generate_engagement_plan(stakeholders),
            'relationship_predictions': self._predict_relationship_trajectories(stakeholders),
            'action_priorities': self._prioritize_actions(stakeholders)
        }

        return analysis

    def _calculate_portfolio_health(self, stakeholders: List[Stakeholder]) -> Dict:
        """Calculate overall stakeholder portfolio health"""
        total_weighted_satisfaction = 0
        total_weight = 0
        category_health = {}

        for stakeholder in stakeholders:
            weight = self.stakeholder_weights.get(stakeholder.category, 0.5)
            weighted_satisfaction = stakeholder.satisfaction_score * weight
            total_weighted_satisfaction += weighted_satisfaction
            total_weight += weight

            if stakeholder.category not in category_health:
                category_health[stakeholder.category] = {
                    'total_satisfaction': 0,
                    'count': 0,
                    'at_risk': []
                }

            category_health[stakeholder.category]['total_satisfaction'] += stakeholder.satisfaction_score
            category_health[stakeholder.category]['count'] += 1

            if stakeholder.satisfaction_score < 50:
                category_health[stakeholder.category]['at_risk'].append(stakeholder.name)

        overall_health = (total_weighted_satisfaction / total_weight) if total_weight > 0 else 0

        return {
            'overall_score': overall_health,
            'health_grade': self._get_health_grade(overall_health),
            'category_breakdown': category_health,
            'top_risks': self._identify_top_risks(stakeholders)
        }

    def _get_health_grade(self, score: float) -> str:
        """Convert health score to letter grade"""
        if score >= 90:
            return 'A+ (Excellent)'
        elif score >= 80:
            return 'A (Strong)'
        elif score >= 70:
            return 'B (Good)'
        elif score >= 60:
            return 'C (Adequate)'
        else:
            return 'F (Critical)'

    def _create_risk_matrix(self, stakeholders: List[Stakeholder]) -> Dict:
        """Create stakeholder risk matrix"""
        matrix = {
            'high_influence_low_satisfaction': [],
            'high_influence_high_satisfaction': []
        }

        for stakeholder in stakeholders:
            if stakeholder.influence_score >= 70:
                if stakeholder.satisfaction_score >= 70:
                    matrix['high_influence_high_satisfaction'].append({
                        'name': stakeholder.name,
                        'strategy': 'Maintain and leverage'
                    })
                else:
                    matrix['high_influence_low_satisfaction'].append({
                        'name': stakeholder.name,
                        'strategy': 'URGENT: Repair immediately',
                        'risk_level': 'CRITICAL'
                    })

        return matrix

    def _generate_engagement_plan(self, stakeholders: List[Stakeholder]) -> List[Dict]:
        """Generate personalized engagement recommendations"""
        recommendations = []

        for stakeholder in stakeholders:
            days_since_interaction = (datetime.now() - stakeholder.last_interaction).days

            if days_since_interaction > stakeholder.interaction_frequency_days:
                urgency = 'HIGH' if days_since_interaction > stakeholder.interaction_frequency_days * 2 else 'MEDIUM'

                recommendation = {
                    'stakeholder': stakeholder.name,
                    'urgency': urgency,
                    'days_overdue': days_since_interaction - stakeholder.interaction_frequency_days,
                    'suggested_action': self._get_engagement_action(stakeholder),
                    'channel': stakeholder.preferred_channels[0] if stakeholder.preferred_channels else 'Email'
                }

                recommendations.append(recommendation)

        recommendations.sort(key=lambda x: (x['urgency'] == 'HIGH', x['days_overdue']), reverse=True)

        return recommendations[:10]

    def _get_engagement_action(self, stakeholder: Stakeholder) -> str:
        """Get recommended engagement action based on stakeholder profile"""
        if stakeholder.satisfaction_score < 50:
            if stakeholder.category == 'Board':
                return "Schedule urgent 1-on-1 to address concerns"
            elif stakeholder.category == 'Investor':
                return "Proactive update call with positive developments"
            else:
                return "Personal check-in to understand concerns"
        else:
            if stakeholder.communication_style == CommunicationStyle.ANALYTICAL:
                return "Share detailed performance metrics and analysis"
            elif stakeholder.communication_style == CommunicationStyle.DRIVER:
                return "Quick update on key wins and results"
            else:
                return "Personal check-in on relationship and collaboration"

    def _predict_relationship_trajectories(self, stakeholders: List[Stakeholder]) -> List[Dict]:
        """Predict future relationship trajectories"""
        predictions = []

        for stakeholder in stakeholders:
            prediction = {
                'stakeholder': stakeholder.name,
                'current_status': stakeholder.relationship_status.value,
                'predicted_30_days': self._predict_status(stakeholder, 30),
                'intervention_needed': stakeholder.satisfaction_score < 60,
                'intervention_type': self._recommend_intervention(stakeholder)
            }

            predictions.append(prediction)

        predictions.sort(key=lambda x: x['intervention_needed'], reverse=True)

        return predictions

    def _predict_status(self, stakeholder: Stakeholder, days_ahead: int) -> str:
        """Predict relationship status after specified days"""
        current_satisfaction = stakeholder.satisfaction_score
        days_since = (datetime.now() - stakeholder.last_interaction).days

        # Simple projection
        decay_factor = 0.02 * days_ahead
        if days_since > stakeholder.interaction_frequency_days * 1.5:
            decay_factor += 0.2

        projected_satisfaction = current_satisfaction - decay_factor

        if projected_satisfaction >= 80:
            return RelationshipStatus.EXCELLENT.value
        elif projected_satisfaction >= 70:
            return RelationshipStatus.STABLE.value
        elif projected_satisfaction >= 60:
            return RelationshipStatus.STRENGTHENING.value
        elif projected_satisfaction >= 50:
            return RelationshipStatus.WEAKENING.value
        else:
            return RelationshipStatus.CRITICAL.value

    def _recommend_intervention(self, stakeholder: Stakeholder) -> str:
        """Recommend intervention based on trajectory"""
        if stakeholder.satisfaction_score < 40:
            return "URGENT: Executive intervention required immediately"
        elif stakeholder.satisfaction_score < 60:
            return "Proactive engagement needed within 1 week"
        else:
            return "Maintain current engagement pattern"

    def _identify_top_risks(self, stakeholders: List[Stakeholder]) -> List[Dict]:
        """Identify top relationship risks"""
        risks = []

        for stakeholder in stakeholders:
            if stakeholder.influence_score > 60 and stakeholder.satisfaction_score < 60:
                risk_score = stakeholder.influence_score * (100 - stakeholder.satisfaction_score) / 100
                risks.append({
                    'stakeholder': stakeholder.name,
                    'risk_score': risk_score,
                    'impact': 'High' if stakeholder.influence_score > 80 else 'Medium',
                    'mitigation': self._get_risk_mitigation(stakeholder)
                })

        risks.sort(key=lambda x: x['risk_score'], reverse=True)
        return risks[:5]

    def _get_risk_mitigation(self, stakeholder: Stakeholder) -> str:
        """Get risk mitigation strategy"""
        if stakeholder.category == 'Board':
            return "Schedule executive session to align on concerns"
        elif stakeholder.category == 'Investor':
            return "Prepare detailed performance update and future plans"
        else:
            return "Personalized engagement plan with regular touchpoints"

    def _prioritize_actions(self, stakeholders: List[Stakeholder]) -> List[Dict]:
        """Prioritize stakeholder actions"""
        actions = []

        for stakeholder in stakeholders:
            urgency = self._calculate_urgency(stakeholder)
            importance = stakeholder.influence_score

            priority_score = (urgency * 0.5 + importance * 0.5)

            actions.append({
                'stakeholder': stakeholder.name,
                'action': self._get_engagement_action(stakeholder),
                'priority_score': priority_score,
                'urgency': 'High' if urgency > 70 else 'Medium'
            })

        actions.sort(key=lambda x: x['priority_score'], reverse=True)
        return actions[:10]

    def _calculate_urgency(self, stakeholder: Stakeholder) -> float:
        """Calculate action urgency"""
        urgency = 50

        if stakeholder.satisfaction_score < 50:
            urgency += 30

        days_overdue = (datetime.now() - stakeholder.last_interaction).days - stakeholder.interaction_frequency_days
        if days_overdue > 0:
            urgency += min(20, days_overdue)

        return min(100, urgency)


def analyze_stakeholder_portfolio() -> str:
    """Main function to analyze stakeholder portfolio"""

    # Sample stakeholders
    stakeholders = [
        Stakeholder(
            name="John Smith",
            role="Board Chair",
            category="Board",
            influence_score=95,
            satisfaction_score=72,
            engagement_level=80,
            communication_style=CommunicationStyle.ANALYTICAL,
            relationship_status=RelationshipStatus.STABLE,
            last_interaction=datetime.now() - timedelta(days=8),
            interaction_frequency_days=7,
            key_concerns=["Revenue growth", "Competition"],
            preferred_channels=["In-person", "Email"],
            relationship_history=[{'satisfaction': 70}, {'satisfaction': 72}],
            notes="Prefers detailed analysis"
        ),
        Stakeholder(
            name="Sarah Johnson",
            role="Lead Investor",
            category="Investor",
            influence_score=88,
            satisfaction_score=45,
            engagement_level=60,
            communication_style=CommunicationStyle.DRIVER,
            relationship_status=RelationshipStatus.WEAKENING,
            last_interaction=datetime.now() - timedelta(days=22),
            interaction_frequency_days=14,
            key_concerns=["Burn rate", "Market timing"],
            preferred_channels=["Video call", "Phone"],
            relationship_history=[{'satisfaction': 65}, {'satisfaction': 45}],
            notes="Concerned about performance"
        )
    ]

    analyzer = StakeholderAnalytics()
    analysis = analyzer.analyze_stakeholder_portfolio(stakeholders)

    # Format output
    output = [
        "=" * 50,
        "STAKEHOLDER RELATIONSHIP ANALYTICS REPORT",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "=" * 50,
        "",
        f"PORTFOLIO HEALTH: {analysis['portfolio_health']['overall_score']:.1f}/100",
        f"Grade: {analysis['portfolio_health']['health_grade']}",
        ""
    ]

    # Risk Matrix
    high_risk = analysis['risk_matrix']['high_influence_low_satisfaction']
    if high_risk:
        output.append("🔴 HIGH RISK (High Influence, Low Satisfaction):")
        for item in high_risk:
            output.append(f"  • {item['name']}: {item['strategy']}")
        output.append("")

    # Top Risks
    if analysis['portfolio_health']['top_risks']:
        output.append("TOP RELATIONSHIP RISKS:")
        for risk in analysis['portfolio_health']['top_risks'][:3]:
            output.append(f"  • {risk['stakeholder']} (Risk Score: {risk['risk_score']:.1f})")
            output.append(f"    → Mitigation: {risk['mitigation']}")
        output.append("")

    # Engagement Recommendations
    if analysis['engagement_recommendations']:
        output.append("PRIORITY ENGAGEMENTS:")
        for rec in analysis['engagement_recommendations'][:5]:
            output.append(f"  {rec['stakeholder']} ({rec['urgency']} urgency)")
            output.append(f"    • Days overdue: {rec['days_overdue']}")
            output.append(f"    • Action: {rec['suggested_action']}")
            output.append("")

    return '\n'.join(output)


if __name__ == "__main__":
    print(analyze_stakeholder_portfolio())
