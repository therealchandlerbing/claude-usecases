"""
Unit tests for CEO Advisor components.

Tests cover:
1. CEOAdvisorOrchestrator configuration handling
2. CEOOptimizer time allocation with edge cases
3. ExecutiveIntelligenceSystem signal analysis
4. StakeholderAnalytics with various stakeholder configurations
"""

import pytest
import sys
from pathlib import Path
from datetime import datetime, timedelta

# Add skills directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "skills" / "ceo-advisor" / "src"))

from ceo_advisor_orchestrator import CEOAdvisorOrchestrator
from ceo_optimizer import CEOOptimizer, TimeBlock
from executive_intelligence_system import ExecutiveIntelligenceSystem, SignalPriority
from stakeholder_analytics import Stakeholder, StakeholderAnalytics, CommunicationStyle, RelationshipStatus


# ============================================================================
# CEOAdvisorOrchestrator Tests
# ============================================================================

@pytest.mark.unit
class TestCEOAdvisorOrchestrator:
    """Tests for CEOAdvisorOrchestrator configuration."""

    def test_empty_config_initialization(self):
        """Test that empty config dict is preserved, not replaced with defaults."""
        orchestrator = CEOAdvisorOrchestrator(config={})
        assert orchestrator.config == {}

    def test_none_config_loads_defaults(self):
        """Test that None config loads default configuration."""
        orchestrator = CEOAdvisorOrchestrator(config=None)
        assert orchestrator.config != {}
        assert 'intelligence' in orchestrator.config
        assert 'stakeholder' in orchestrator.config

    def test_no_config_argument_loads_defaults(self):
        """Test that omitting config argument loads defaults."""
        orchestrator = CEOAdvisorOrchestrator()
        assert orchestrator.config != {}
        assert 'optimization' in orchestrator.config


# ============================================================================
# CEOOptimizer Tests
# ============================================================================

@pytest.mark.unit
class TestCEOOptimizer:
    """Tests for CEOOptimizer time allocation analysis."""

    def test_zero_duration_block(self):
        """Test that zero-duration time blocks don't cause division by zero."""
        optimizer = CEOOptimizer()
        now = datetime.now()

        # Create a time block with zero duration (start_time == end_time)
        calendar_data = [
            TimeBlock(
                start_time=now.replace(hour=9, minute=0),
                end_time=now.replace(hour=9, minute=0),  # Zero duration
                category='strategic_thinking',
                subcategory='planning',
                energy_cost=40,
                value_created=0,
                attendees=['CEO'],
                outcome_quality=0,
                notes='Cancelled meeting'
            )
        ]

        # This should not raise a ZeroDivisionError
        analysis = optimizer.analyze_time_allocation(calendar_data)
        assert analysis is not None
        assert 'current_allocation' in analysis

    def test_normal_time_allocation(self):
        """Test normal time allocation calculation."""
        optimizer = CEOOptimizer()
        now = datetime.now()

        calendar_data = [
            TimeBlock(
                start_time=now.replace(hour=8, minute=0),
                end_time=now.replace(hour=10, minute=0),
                category='strategic_thinking',
                subcategory='strategy_session',
                energy_cost=85,
                value_created=90,
                attendees=['CEO', 'CSO'],
                outcome_quality=88,
                notes='Quarterly strategy'
            )
        ]

        analysis = optimizer.analyze_time_allocation(calendar_data)
        assert 'strategic_thinking' in analysis['current_allocation']
        assert analysis['current_allocation']['strategic_thinking']['hours_per_week'] == 2.0


# ============================================================================
# ExecutiveIntelligenceSystem Tests
# ============================================================================

@pytest.mark.unit
class TestExecutiveIntelligenceSystem:
    """Tests for ExecutiveIntelligenceSystem signal detection."""

    def test_external_signal_impact_score_opportunity(self):
        """Test that opportunity impact score is calculated correctly."""
        system = ExecutiveIntelligenceSystem()

        # Create data with a high opportunity score and low threat level
        # to ensure we get an OPPORTUNITY signal, not a CRITICAL threat
        data = {
            'opportunity_score': 84,
            'threat_level': 20  # Low threat to avoid triggering critical signal
        }

        # Using competitive_intelligence source which has weight 0.75
        config = system.signal_sources['external']['competitive_intelligence']

        signal = system._analyze_external_signal('competitive_intelligence', data, config)

        # Expected: 84 * 0.75 = 63
        assert signal is not None
        assert signal.priority == SignalPriority.OPPORTUNITY
        assert signal.impact_score == pytest.approx(63.0)

    def test_critical_signal_detection(self):
        """Test detection of critical signals."""
        system = ExecutiveIntelligenceSystem()

        data = {'threat_level': 80}
        config = system.signal_sources['external']['competitive_intelligence']

        signal = system._analyze_external_signal('competitive_intelligence', data, config)

        assert signal is not None
        assert signal.priority == SignalPriority.CRITICAL


# ============================================================================
# StakeholderAnalytics Tests
# ============================================================================

@pytest.mark.unit
class TestStakeholderAnalytics:
    """Tests for StakeholderAnalytics."""

    def test_stakeholder_with_no_preferred_channels(self):
        """Test Stakeholder with empty preferred channels list."""
        stakeholder = Stakeholder(
            name="Test Stakeholder",
            role="Board Member",
            category="Board",
            influence_score=85.0,
            satisfaction_score=70.0,
            engagement_level=75.0,
            communication_style=CommunicationStyle.ANALYTICAL,
            relationship_status=RelationshipStatus.STABLE,
            last_interaction=datetime.now() - timedelta(days=5),
            interaction_frequency_days=7,
            key_concerns=["Revenue growth"],
            preferred_channels=[],  # No preferred channels
            relationship_history=[],
            notes=""
        )

        assert stakeholder.name == "Test Stakeholder"
        assert stakeholder.preferred_channels == []
        assert stakeholder.relationship_history == []

    def test_stakeholder_with_relationship_history(self):
        """Test Stakeholder with relationship_history provided."""
        history = [{'date': '2024-01-01', 'satisfaction': 75}]

        stakeholder = Stakeholder(
            name="Test Stakeholder 2",
            role="Investor",
            category="Investor",
            influence_score=90.0,
            satisfaction_score=80.0,
            engagement_level=85.0,
            communication_style=CommunicationStyle.DRIVER,
            relationship_status=RelationshipStatus.STRENGTHENING,
            last_interaction=datetime.now() - timedelta(days=3),
            interaction_frequency_days=14,
            key_concerns=["Market timing"],
            preferred_channels=["Email", "Phone"],
            notes="VIP investor",
            relationship_history=history
        )

        assert stakeholder.relationship_history == history

    def test_portfolio_health_calculation(self):
        """Test stakeholder portfolio health calculation."""
        analytics = StakeholderAnalytics()

        stakeholders = [
            Stakeholder(
                name="High Performer",
                role="Board Chair",
                category="Board",
                influence_score=95.0,
                satisfaction_score=85.0,
                engagement_level=90.0,
                communication_style=CommunicationStyle.ANALYTICAL,
                relationship_status=RelationshipStatus.EXCELLENT,
                last_interaction=datetime.now() - timedelta(days=2),
                interaction_frequency_days=7,
                key_concerns=[],
                preferred_channels=["In-person"],
                relationship_history=[],
                notes=""
            )
        ]

        health = analytics._calculate_portfolio_health(stakeholders)
        assert 'overall_score' in health
        assert health['overall_score'] > 0
