#!/usr/bin/env python3
"""
Executive Intelligence System - Real-time signal detection and analysis for CEOs

Monitors internal and external signals to detect issues before they become crises.
Provides early warnings, pattern recognition, and predictive insights.
"""

import json
from typing import Dict, List, Optional
from datetime import datetime, timedelta
from dataclasses import dataclass
from enum import Enum
import random  # For demo purposes - replace with real data sources


class SignalPriority(Enum):
    CRITICAL = "RED"      # Immediate action required
    WARNING = "YELLOW"    # Monitor closely
    OPPORTUNITY = "GREEN" # Potential upside
    INFO = "BLUE"        # Awareness only


@dataclass
class Signal:
    source: str
    category: str
    priority: SignalPriority
    message: str
    confidence: float
    action_required: str
    deadline: Optional[datetime]
    impact_score: float
    stakeholders: List[str]


class ExecutiveIntelligenceSystem:
    def __init__(self):
        self.signal_sources = {
            'internal': {
                'team_health': {'weight': 0.8, 'thresholds': {'critical': 30, 'warning': 50}},
                'project_status': {'weight': 0.7, 'thresholds': {'critical': 25, 'warning': 40}},
                'financial_metrics': {'weight': 0.9, 'thresholds': {'critical': 20, 'warning': 35}},
                'customer_health': {'weight': 0.85, 'thresholds': {'critical': 35, 'warning': 55}},
                'operational_efficiency': {'weight': 0.6, 'thresholds': {'critical': 30, 'warning': 45}}
            },
            'external': {
                'competitive_intelligence': {'weight': 0.75, 'thresholds': {'critical': 40, 'warning': 60}},
                'market_dynamics': {'weight': 0.7, 'thresholds': {'critical': 35, 'warning': 50}},
                'investor_sentiment': {'weight': 0.85, 'thresholds': {'critical': 30, 'warning': 45}},
                'regulatory_landscape': {'weight': 0.8, 'thresholds': {'critical': 25, 'warning': 40}},
                'technology_disruption': {'weight': 0.65, 'thresholds': {'critical': 30, 'warning': 50}}
            }
        }

        self.pattern_library = {
            'talent_exodus': {
                'signals': ['resignation_spike', 'engagement_drop', 'glassdoor_negative'],
                'threshold': 3,
                'action': 'Emergency all-hands and retention program'
            },
            'competitive_threat': {
                'signals': ['competitor_funding', 'talent_poaching', 'feature_parity'],
                'threshold': 2,
                'action': 'Strategic response session with executive team'
            }
        }

    def scan_all_signals(self, data_feeds: Dict) -> List[Signal]:
        """Scan all signal sources and detect anomalies"""
        detected_signals = []

        # Internal signals
        for source, config in self.signal_sources['internal'].items():
            signal = self._analyze_internal_signal(source, data_feeds.get(source, {}), config)
            if signal:
                detected_signals.append(signal)

        # External signals
        for source, config in self.signal_sources['external'].items():
            signal = self._analyze_external_signal(source, data_feeds.get(source, {}), config)
            if signal:
                detected_signals.append(signal)

        # Sort by priority and impact
        detected_signals.sort(key=lambda x: (
            x.priority.value == "RED",
            x.impact_score
        ), reverse=True)

        return detected_signals

    def _analyze_internal_signal(self, source: str, data: Dict, config: Dict) -> Optional[Signal]:
        """Analyze internal signal sources"""
        # Simulate signal detection (replace with real data analysis)
        health_score = data.get('health_score', random.randint(20, 100))

        if health_score < config['thresholds']['critical']:
            return Signal(
                source=f"Internal/{source}",
                category="Organizational Health",
                priority=SignalPriority.CRITICAL,
                message=f"Critical {source.replace('_', ' ')} issue detected: score {health_score}",
                confidence=0.85,
                action_required=self._get_action_for_source(source, 'critical'),
                deadline=datetime.now() + timedelta(days=1),
                impact_score=config['weight'] * (100 - health_score),
                stakeholders=self._get_stakeholders_for_source(source)
            )
        elif health_score < config['thresholds']['warning']:
            return Signal(
                source=f"Internal/{source}",
                category="Organizational Health",
                priority=SignalPriority.WARNING,
                message=f"Warning: {source.replace('_', ' ')} needs attention: score {health_score}",
                confidence=0.75,
                action_required=self._get_action_for_source(source, 'warning'),
                deadline=datetime.now() + timedelta(days=7),
                impact_score=config['weight'] * (100 - health_score),
                stakeholders=self._get_stakeholders_for_source(source)
            )

        return None

    def _analyze_external_signal(self, source: str, data: Dict, config: Dict) -> Optional[Signal]:
        """Analyze external signal sources"""
        threat_level = data.get('threat_level', random.randint(20, 100))

        if threat_level > (100 - config['thresholds']['critical']):
            return Signal(
                source=f"External/{source}",
                category="Market Intelligence",
                priority=SignalPriority.CRITICAL,
                message=f"Critical external threat from {source.replace('_', ' ')}: level {threat_level}",
                confidence=0.8,
                action_required=self._get_action_for_source(source, 'critical'),
                deadline=datetime.now() + timedelta(days=3),
                impact_score=config['weight'] * threat_level,
                stakeholders=self._get_stakeholders_for_source(source)
            )

        # Check for opportunities
        opportunity = data.get('opportunity_score', random.randint(0, 100))
        if opportunity > 80:
            # Apply confidence factor to opportunity impact score
            opportunity_impact = config['weight'] * opportunity * 0.95
            return Signal(
                source=f"External/{source}",
                category="Market Intelligence",
                priority=SignalPriority.OPPORTUNITY,
                message=f"Opportunity detected in {source.replace('_', ' ')}: score {opportunity}",
                confidence=0.7,
                action_required="Evaluate and potentially fast-track initiative",
                deadline=datetime.now() + timedelta(days=14),
                impact_score=opportunity_impact,
                stakeholders=self._get_stakeholders_for_source(source)
            )

        return None

    def _get_action_for_source(self, source: str, severity: str) -> str:
        """Get recommended action based on source and severity"""
        actions = {
            'team_health': {
                'critical': 'Immediate 1-on-1s with key leaders, all-hands within 48 hours',
                'warning': 'Schedule pulse survey and team health session'
            },
            'project_status': {
                'critical': 'Emergency project review, consider resource reallocation',
                'warning': 'Deep-dive in next exec meeting'
            },
            'financial_metrics': {
                'critical': 'CFO briefing today, potential board notification',
                'warning': 'Financial review in next 72 hours'
            },
            'customer_health': {
                'critical': 'Customer success war room, CEO calls to at-risk accounts',
                'warning': 'Customer health review with CS team'
            },
            'competitive_intelligence': {
                'critical': 'Competitive response team activation',
                'warning': 'Strategy session on competitive positioning'
            }
        }

        return actions.get(source, {}).get(severity, 'Review and assess')

    def _get_stakeholders_for_source(self, source: str) -> List[str]:
        """Get relevant stakeholders for a signal source"""
        stakeholder_map = {
            'team_health': ['CHRO', 'Executive Team', 'Department Heads'],
            'project_status': ['COO', 'Project Leads', 'Product Team'],
            'financial_metrics': ['CFO', 'Board', 'Finance Team'],
            'customer_health': ['CCO', 'Customer Success', 'Sales'],
            'competitive_intelligence': ['CSO', 'Product', 'Marketing'],
            'investor_sentiment': ['CFO', 'Board', 'IR Team']
        }

        return stakeholder_map.get(source, ['CEO', 'Executive Team'])

    def generate_daily_brief(self, signals: List[Signal]) -> Dict:
        """Generate executive daily intelligence brief"""
        brief = {
            'generated_at': datetime.now().isoformat(),
            'executive_summary': self._generate_summary(signals),
            'critical_actions': [],
            'watch_items': [],
            'opportunities': [],
            'predictive_insights': []
        }

        for signal in signals:
            if signal.priority == SignalPriority.CRITICAL:
                brief['critical_actions'].append({
                    'issue': signal.message,
                    'action': signal.action_required,
                    'deadline': signal.deadline.isoformat() if signal.deadline else 'ASAP',
                    'owner': signal.stakeholders[0] if signal.stakeholders else 'CEO'
                })
            elif signal.priority == SignalPriority.WARNING:
                brief['watch_items'].append({
                    'item': signal.message,
                    'monitoring': signal.action_required,
                    'escalation_trigger': f"Impact score > {signal.impact_score + 20}"
                })
            elif signal.priority == SignalPriority.OPPORTUNITY:
                brief['opportunities'].append({
                    'opportunity': signal.message,
                    'action': signal.action_required,
                    'potential_value': f"Impact score: {signal.impact_score:.1f}"
                })

        # Add predictive insights
        brief['predictive_insights'] = self._generate_predictions(signals)

        return brief

    def _generate_summary(self, signals: List[Signal]) -> str:
        """Generate executive summary of current state"""
        critical_count = sum(1 for s in signals if s.priority == SignalPriority.CRITICAL)
        warning_count = sum(1 for s in signals if s.priority == SignalPriority.WARNING)
        opportunity_count = sum(1 for s in signals if s.priority == SignalPriority.OPPORTUNITY)

        if critical_count > 0:
            summary = f"🔴 {critical_count} critical issues require immediate attention. "
        else:
            summary = "✅ No critical issues detected. "

        if warning_count > 0:
            summary += f"⚠️ {warning_count} items need monitoring. "

        if opportunity_count > 0:
            summary += f"💚 {opportunity_count} opportunities identified."

        return summary

    def _generate_predictions(self, signals: List[Signal]) -> List[Dict]:
        """Generate predictive insights based on current signals"""
        predictions = []

        if any('team_health' in s.source for s in signals):
            predictions.append({
                'prediction': 'Potential talent retention issue in next 30 days',
                'probability': '65%',
                'prevention': 'Proactive retention program and skip-level meetings'
            })

        if any('competitive' in s.source for s in signals):
            predictions.append({
                'prediction': 'Competitive product launch likely within 60 days',
                'probability': '75%',
                'prevention': 'Accelerate product roadmap and PR strategy'
            })

        return predictions


def generate_intelligence_report(data_feeds: Dict = None) -> str:
    """Main function to generate executive intelligence report"""

    # Use sample data if none provided
    if data_feeds is None:
        data_feeds = {
            'team_health': {'health_score': 45},
            'project_status': {'health_score': 62},
            'financial_metrics': {'health_score': 38},
            'customer_health': {'health_score': 71},
            'competitive_intelligence': {'threat_level': 65},
            'investor_sentiment': {'threat_level': 42},
            'market_dynamics': {'opportunity_score': 85}
        }

    system = ExecutiveIntelligenceSystem()
    signals = system.scan_all_signals(data_feeds)
    brief = system.generate_daily_brief(signals)

    # Format output
    output = [
        "=" * 50,
        "EXECUTIVE INTELLIGENCE BRIEF",
        f"Generated: {brief['generated_at']}",
        "=" * 50,
        "",
        f"SUMMARY: {brief['executive_summary']}",
        ""
    ]

    if brief['critical_actions']:
        output.append("🔴 CRITICAL ACTIONS REQUIRED:")
        for action in brief['critical_actions']:
            output.append(f"  • {action['issue']}")
            output.append(f"    → Action: {action['action']}")
            output.append(f"    → Deadline: {action['deadline']}")
            output.append("")

    if brief['watch_items']:
        output.append("⚠️ WATCH ITEMS:")
        for item in brief['watch_items']:
            output.append(f"  • {item['item']}")
            output.append("")

    if brief['opportunities']:
        output.append("💚 OPPORTUNITIES:")
        for opp in brief['opportunities']:
            output.append(f"  • {opp['opportunity']}")
            output.append(f"    → Value: {opp['potential_value']}")
            output.append("")

    if brief['predictive_insights']:
        output.append("🔮 PREDICTIVE INSIGHTS:")
        for pred in brief['predictive_insights']:
            output.append(f"  • {pred['prediction']} ({pred['probability']})")
            output.append(f"    → Prevention: {pred['prevention']}")
            output.append("")

    return '\n'.join(output)


if __name__ == "__main__":
    print(generate_intelligence_report())
