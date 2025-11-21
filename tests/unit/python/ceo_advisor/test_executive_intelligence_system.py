"""
Comprehensive unit tests for Executive Intelligence System.

Tests signal detection, analysis, and intelligence brief generation including:
- Signal priority classification
- Internal and external signal analysis
- Pattern recognition
- Predictive insights generation
"""

import pytest
from datetime import datetime, timedelta
from pathlib import Path
import sys

# Add CEO Advisor to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent / "skills" / "ceo-advisor" / "src"))

from executive_intelligence_system import (
    ExecutiveIntelligenceSystem,
    Signal,
    SignalPriority,
    generate_intelligence_report
)


class TestSignalPriority:
    """Test SignalPriority enum."""

    def test_signal_priority_values(self):
        """Test all signal priority values are defined."""
        assert SignalPriority.CRITICAL.value == "RED"
        assert SignalPriority.WARNING.value == "YELLOW"
        assert SignalPriority.OPPORTUNITY.value == "GREEN"
        assert SignalPriority.INFO.value == "BLUE"


class TestSignalDataclass:
    """Test Signal dataclass."""

    def test_signal_creation(self):
        """Test creating a signal instance."""
        signal = Signal(
            source="test/source",
            category="test_category",
            priority=SignalPriority.CRITICAL,
            message="Test message",
            confidence=0.85,
            action_required="Test action",
            deadline=datetime.now(),
            impact_score=75.0,
            stakeholders=["CEO", "CTO"]
        )

        assert signal.source == "test/source"
        assert signal.category == "test_category"
        assert signal.priority == SignalPriority.CRITICAL
        assert signal.message == "Test message"
        assert signal.confidence == 0.85
        assert signal.action_required == "Test action"
        assert signal.impact_score == 75.0
        assert "CEO" in signal.stakeholders

    def test_signal_with_optional_deadline(self):
        """Test signal with None deadline."""
        signal = Signal(
            source="test",
            category="test",
            priority=SignalPriority.INFO,
            message="Test",
            confidence=0.5,
            action_required="None",
            deadline=None,
            impact_score=10.0,
            stakeholders=[]
        )

        assert signal.deadline is None


class TestExecutiveIntelligenceSystemInitialization:
    """Test ExecutiveIntelligenceSystem initialization."""

    def test_init_signal_sources(self):
        """Test signal sources are properly initialized."""
        system = ExecutiveIntelligenceSystem()

        assert 'internal' in system.signal_sources
        assert 'external' in system.signal_sources

        # Check internal sources
        internal_sources = system.signal_sources['internal']
        assert 'team_health' in internal_sources
        assert 'project_status' in internal_sources
        assert 'financial_metrics' in internal_sources
        assert 'customer_health' in internal_sources
        assert 'operational_efficiency' in internal_sources

        # Check external sources
        external_sources = system.signal_sources['external']
        assert 'competitive_intelligence' in external_sources
        assert 'market_dynamics' in external_sources
        assert 'investor_sentiment' in external_sources
        assert 'regulatory_landscape' in external_sources
        assert 'technology_disruption' in external_sources

    def test_signal_source_weights(self):
        """Test signal source weights are reasonable."""
        system = ExecutiveIntelligenceSystem()

        # All weights should be between 0 and 1
        for category in ['internal', 'external']:
            for source, config in system.signal_sources[category].items():
                assert 0 < config['weight'] <= 1.0

    def test_signal_source_thresholds(self):
        """Test signal source thresholds are defined."""
        system = ExecutiveIntelligenceSystem()

        for category in ['internal', 'external']:
            for source, config in system.signal_sources[category].items():
                assert 'thresholds' in config
                assert 'critical' in config['thresholds']
                assert 'warning' in config['thresholds']
                # Critical threshold should be more stringent than warning
                assert config['thresholds']['critical'] < config['thresholds']['warning']

    def test_pattern_library_initialization(self):
        """Test pattern library is initialized."""
        system = ExecutiveIntelligenceSystem()

        assert 'talent_exodus' in system.pattern_library
        assert 'competitive_threat' in system.pattern_library

        # Check pattern structure
        talent_exodus = system.pattern_library['talent_exodus']
        assert 'signals' in talent_exodus
        assert 'threshold' in talent_exodus
        assert 'action' in talent_exodus
        assert isinstance(talent_exodus['signals'], list)


class TestInternalSignalAnalysis:
    """Test internal signal analysis."""

    def test_analyze_internal_signal_critical(self):
        """Test detection of critical internal signals."""
        system = ExecutiveIntelligenceSystem()

        config = {'weight': 0.8, 'thresholds': {'critical': 30, 'warning': 50}}
        data = {'health_score': 25}

        signal = system._analyze_internal_signal('team_health', data, config)

        assert signal is not None
        assert signal.priority == SignalPriority.CRITICAL
        assert 'Internal/team_health' in signal.source
        assert signal.confidence == 0.85
        assert signal.deadline is not None

    def test_analyze_internal_signal_warning(self):
        """Test detection of warning internal signals."""
        system = ExecutiveIntelligenceSystem()

        config = {'weight': 0.7, 'thresholds': {'critical': 30, 'warning': 50}}
        data = {'health_score': 40}

        signal = system._analyze_internal_signal('project_status', data, config)

        assert signal is not None
        assert signal.priority == SignalPriority.WARNING
        assert signal.confidence == 0.75

    def test_analyze_internal_signal_healthy(self):
        """Test no signal for healthy status."""
        system = ExecutiveIntelligenceSystem()

        config = {'weight': 0.8, 'thresholds': {'critical': 30, 'warning': 50}}
        data = {'health_score': 80}

        signal = system._analyze_internal_signal('team_health', data, config)

        assert signal is None

    def test_analyze_internal_signal_at_critical_threshold(self):
        """Test signal at exact critical threshold."""
        system = ExecutiveIntelligenceSystem()

        config = {'weight': 0.8, 'thresholds': {'critical': 30, 'warning': 50}}
        data = {'health_score': 30}

        signal = system._analyze_internal_signal('team_health', data, config)

        # At threshold should not be critical
        assert signal is None or signal.priority != SignalPriority.CRITICAL

    def test_analyze_internal_signal_at_warning_threshold(self):
        """Test signal at exact warning threshold."""
        system = ExecutiveIntelligenceSystem()

        config = {'weight': 0.8, 'thresholds': {'critical': 30, 'warning': 50}}
        data = {'health_score': 50}

        signal = system._analyze_internal_signal('team_health', data, config)

        # At threshold should not trigger warning
        assert signal is None or signal.priority != SignalPriority.WARNING

    def test_internal_signal_impact_score(self):
        """Test impact score calculation for internal signals."""
        system = ExecutiveIntelligenceSystem()

        config = {'weight': 0.8, 'thresholds': {'critical': 30, 'warning': 50}}
        data = {'health_score': 20}

        signal = system._analyze_internal_signal('team_health', data, config)

        # Impact should be weight * (100 - health_score)
        expected_impact = 0.8 * (100 - 20)
        assert signal.impact_score == expected_impact


class TestExternalSignalAnalysis:
    """Test external signal analysis."""

    def test_analyze_external_signal_critical_threat(self):
        """Test detection of critical external threats."""
        system = ExecutiveIntelligenceSystem()

        config = {'weight': 0.75, 'thresholds': {'critical': 40, 'warning': 60}}
        # threat_level needs to be > (100 - 40) = > 60 to trigger critical
        data = {'threat_level': 75}

        signal = system._analyze_external_signal('competitive_intelligence', data, config)

        assert signal is not None
        assert signal.priority == SignalPriority.CRITICAL
        assert 'External/competitive_intelligence' in signal.source

    def test_analyze_external_signal_opportunity(self):
        """Test detection of external opportunities."""
        system = ExecutiveIntelligenceSystem()

        config = {'weight': 0.7, 'thresholds': {'critical': 35, 'warning': 50}}
        # Include low threat_level to ensure it doesn't trigger critical path
        data = {'opportunity_score': 85, 'threat_level': 30}

        signal = system._analyze_external_signal('market_dynamics', data, config)

        assert signal is not None
        assert signal.priority == SignalPriority.OPPORTUNITY
        assert 'opportunity' in signal.message.lower()

    def test_analyze_external_signal_no_threat(self):
        """Test no signal for low external threat."""
        system = ExecutiveIntelligenceSystem()

        config = {'weight': 0.7, 'thresholds': {'critical': 40, 'warning': 60}}
        data = {'threat_level': 30, 'opportunity_score': 50}

        signal = system._analyze_external_signal('competitive_intelligence', data, config)

        assert signal is None

    def test_external_signal_impact_score_threat(self):
        """Test impact score for external threats."""
        system = ExecutiveIntelligenceSystem()

        config = {'weight': 0.75, 'thresholds': {'critical': 40, 'warning': 60}}
        threat_level = 75
        data = {'threat_level': threat_level}

        signal = system._analyze_external_signal('competitive_intelligence', data, config)

        expected_impact = 0.75 * threat_level
        assert signal.impact_score == expected_impact

    def test_external_signal_impact_score_opportunity(self):
        """Test impact score for external opportunities."""
        system = ExecutiveIntelligenceSystem()

        config = {'weight': 0.7, 'thresholds': {'critical': 35, 'warning': 50}}
        opportunity_score = 85
        # Include low threat_level to ensure opportunity path is taken
        data = {'opportunity_score': opportunity_score, 'threat_level': 30}

        signal = system._analyze_external_signal('market_dynamics', data, config)

        # Apply confidence factor to opportunity impact score (0.95)
        expected_impact = 0.7 * opportunity_score * 0.95
        assert signal.impact_score == expected_impact


class TestSignalScanning:
    """Test comprehensive signal scanning."""

    def test_scan_all_signals_empty_data(self):
        """Test scanning with empty data feeds."""
        system = ExecutiveIntelligenceSystem()
        signals = system.scan_all_signals({})

        # Should still return a list (may contain signals from random data)
        assert isinstance(signals, list)

    def test_scan_all_signals_with_data(self):
        """Test scanning with provided data feeds."""
        system = ExecutiveIntelligenceSystem()

        data_feeds = {
            'team_health': {'health_score': 25},
            'financial_metrics': {'health_score': 18},
            'competitive_intelligence': {'threat_level': 75}
        }

        signals = system.scan_all_signals(data_feeds)

        assert isinstance(signals, list)
        # Should detect at least the critical signals we provided
        assert len(signals) >= 2

    def test_signals_sorted_by_priority(self):
        """Test that signals are sorted by priority."""
        system = ExecutiveIntelligenceSystem()

        data_feeds = {
            'team_health': {'health_score': 80},  # No signal
            'financial_metrics': {'health_score': 25},  # Critical
            'project_status': {'health_score': 45},  # Warning
            'competitive_intelligence': {'threat_level': 75}  # Critical
        }

        signals = system.scan_all_signals(data_feeds)

        # Critical signals should come first
        if len(signals) >= 2:
            first_critical = next((i for i, s in enumerate(signals) if s.priority == SignalPriority.CRITICAL), None)
            first_warning = next((i for i, s in enumerate(signals) if s.priority == SignalPriority.WARNING), None)

            if first_critical is not None and first_warning is not None:
                assert first_critical < first_warning


class TestActionRecommendations:
    """Test action recommendation generation."""

    def test_get_action_for_source_team_health_critical(self):
        """Test critical action for team health."""
        system = ExecutiveIntelligenceSystem()

        action = system._get_action_for_source('team_health', 'critical')

        assert isinstance(action, str)
        assert len(action) > 0
        assert '1-on-1' in action.lower() or 'all-hands' in action.lower()

    def test_get_action_for_source_team_health_warning(self):
        """Test warning action for team health."""
        system = ExecutiveIntelligenceSystem()

        action = system._get_action_for_source('team_health', 'warning')

        assert isinstance(action, str)
        assert len(action) > 0

    def test_get_action_for_source_financial_critical(self):
        """Test critical action for financial metrics."""
        system = ExecutiveIntelligenceSystem()

        action = system._get_action_for_source('financial_metrics', 'critical')

        assert 'CFO' in action or 'board' in action.lower()

    def test_get_action_for_source_unknown(self):
        """Test default action for unknown source."""
        system = ExecutiveIntelligenceSystem()

        action = system._get_action_for_source('unknown_source', 'critical')

        assert action == 'Review and assess'


class TestStakeholderMapping:
    """Test stakeholder mapping."""

    def test_get_stakeholders_team_health(self):
        """Test stakeholders for team health."""
        system = ExecutiveIntelligenceSystem()

        stakeholders = system._get_stakeholders_for_source('team_health')

        assert isinstance(stakeholders, list)
        assert len(stakeholders) > 0
        assert 'CHRO' in stakeholders or 'Executive Team' in stakeholders

    def test_get_stakeholders_financial(self):
        """Test stakeholders for financial metrics."""
        system = ExecutiveIntelligenceSystem()

        stakeholders = system._get_stakeholders_for_source('financial_metrics')

        assert 'CFO' in stakeholders
        assert 'Board' in stakeholders

    def test_get_stakeholders_unknown_source(self):
        """Test default stakeholders for unknown source."""
        system = ExecutiveIntelligenceSystem()

        stakeholders = system._get_stakeholders_for_source('unknown_source')

        assert 'CEO' in stakeholders
        assert 'Executive Team' in stakeholders


class TestDailyBriefGeneration:
    """Test daily brief generation."""

    def test_generate_daily_brief_structure(self):
        """Test daily brief has correct structure."""
        system = ExecutiveIntelligenceSystem()
        signals = []

        brief = system.generate_daily_brief(signals)

        assert 'generated_at' in brief
        assert 'executive_summary' in brief
        assert 'critical_actions' in brief
        assert 'watch_items' in brief
        assert 'opportunities' in brief
        assert 'predictive_insights' in brief

    def test_generate_daily_brief_with_critical_signal(self):
        """Test brief generation with critical signal."""
        system = ExecutiveIntelligenceSystem()

        signal = Signal(
            source="test",
            category="test",
            priority=SignalPriority.CRITICAL,
            message="Test critical issue",
            confidence=0.85,
            action_required="Take action",
            deadline=datetime.now() + timedelta(days=1),
            impact_score=80.0,
            stakeholders=["CEO"]
        )

        brief = system.generate_daily_brief([signal])

        assert len(brief['critical_actions']) == 1
        assert 'Test critical issue' in brief['critical_actions'][0]['issue']
        assert 'Take action' in brief['critical_actions'][0]['action']

    def test_generate_daily_brief_with_warning_signal(self):
        """Test brief generation with warning signal."""
        system = ExecutiveIntelligenceSystem()

        signal = Signal(
            source="test",
            category="test",
            priority=SignalPriority.WARNING,
            message="Test warning",
            confidence=0.75,
            action_required="Monitor closely",
            deadline=datetime.now() + timedelta(days=7),
            impact_score=50.0,
            stakeholders=["CTO"]
        )

        brief = system.generate_daily_brief([signal])

        assert len(brief['watch_items']) == 1
        assert 'Test warning' in brief['watch_items'][0]['item']

    def test_generate_daily_brief_with_opportunity(self):
        """Test brief generation with opportunity signal."""
        system = ExecutiveIntelligenceSystem()

        signal = Signal(
            source="test",
            category="test",
            priority=SignalPriority.OPPORTUNITY,
            message="Test opportunity",
            confidence=0.7,
            action_required="Evaluate",
            deadline=datetime.now() + timedelta(days=14),
            impact_score=75.0,
            stakeholders=["CSO"]
        )

        brief = system.generate_daily_brief([signal])

        assert len(brief['opportunities']) == 1
        assert 'Test opportunity' in brief['opportunities'][0]['opportunity']

    def test_generate_daily_brief_timestamp(self):
        """Test brief has valid timestamp."""
        system = ExecutiveIntelligenceSystem()

        brief = system.generate_daily_brief([])

        timestamp = datetime.fromisoformat(brief['generated_at'])
        assert (datetime.now() - timestamp).total_seconds() < 60


class TestExecutiveSummaryGeneration:
    """Test executive summary generation."""

    def test_generate_summary_no_issues(self):
        """Test summary with no critical issues."""
        system = ExecutiveIntelligenceSystem()

        summary = system._generate_summary([])

        assert '✅' in summary or 'no critical' in summary.lower()

    def test_generate_summary_with_critical(self):
        """Test summary with critical issues."""
        system = ExecutiveIntelligenceSystem()

        signal = Signal(
            source="test",
            category="test",
            priority=SignalPriority.CRITICAL,
            message="Test",
            confidence=0.85,
            action_required="Act",
            deadline=None,
            impact_score=80.0,
            stakeholders=[]
        )

        summary = system._generate_summary([signal])

        assert '🔴' in summary or '1' in summary
        assert 'critical' in summary.lower()

    def test_generate_summary_mixed_signals(self):
        """Test summary with mixed signal priorities."""
        system = ExecutiveIntelligenceSystem()

        signals = [
            Signal("test1", "test", SignalPriority.CRITICAL, "msg", 0.8, "act", None, 80.0, []),
            Signal("test2", "test", SignalPriority.WARNING, "msg", 0.7, "act", None, 50.0, []),
            Signal("test3", "test", SignalPriority.OPPORTUNITY, "msg", 0.7, "act", None, 70.0, [])
        ]

        summary = system._generate_summary(signals)

        assert 'critical' in summary.lower()
        assert 'monitoring' in summary.lower() or 'watch' in summary.lower() or 'warning' in summary.lower()
        assert 'opportunit' in summary.lower()


class TestPredictiveInsights:
    """Test predictive insights generation."""

    def test_generate_predictions_team_health(self):
        """Test prediction for team health signals."""
        system = ExecutiveIntelligenceSystem()

        signal = Signal(
            source="Internal/team_health",
            category="test",
            priority=SignalPriority.WARNING,
            message="Team health declining",
            confidence=0.75,
            action_required="Monitor",
            deadline=None,
            impact_score=60.0,
            stakeholders=[]
        )

        predictions = system._generate_predictions([signal])

        assert len(predictions) > 0
        assert any('talent' in p['prediction'].lower() or 'retention' in p['prediction'].lower()
                  for p in predictions)

    def test_generate_predictions_competitive(self):
        """Test prediction for competitive signals."""
        system = ExecutiveIntelligenceSystem()

        signal = Signal(
            source="External/competitive_intelligence",
            category="test",
            priority=SignalPriority.CRITICAL,
            message="Competitive threat",
            confidence=0.8,
            action_required="Respond",
            deadline=None,
            impact_score=75.0,
            stakeholders=[]
        )

        predictions = system._generate_predictions([signal])

        assert len(predictions) > 0
        assert any('competitive' in p['prediction'].lower() or 'product' in p['prediction'].lower()
                  for p in predictions)

    def test_generate_predictions_no_signals(self):
        """Test predictions with no relevant signals."""
        system = ExecutiveIntelligenceSystem()

        predictions = system._generate_predictions([])

        assert isinstance(predictions, list)


class TestIntelligenceReportGeneration:
    """Test main intelligence report generation function."""

    def test_generate_intelligence_report_with_defaults(self):
        """Test report generation with default data."""
        report = generate_intelligence_report()

        assert isinstance(report, str)
        assert 'EXECUTIVE INTELLIGENCE BRIEF' in report
        assert 'Generated:' in report

    def test_generate_intelligence_report_with_custom_data(self):
        """Test report generation with custom data."""
        data_feeds = {
            'team_health': {'health_score': 25},
            'financial_metrics': {'health_score': 20}
        }

        report = generate_intelligence_report(data_feeds)

        assert isinstance(report, str)
        assert 'EXECUTIVE INTELLIGENCE BRIEF' in report
        # Should contain critical actions for low health scores
        assert '🔴' in report or 'CRITICAL' in report


class TestEdgeCases:
    """Test edge cases and error handling."""

    def test_signal_with_zero_impact(self):
        """Test signal with zero impact score."""
        signal = Signal(
            source="test",
            category="test",
            priority=SignalPriority.INFO,
            message="Low impact",
            confidence=0.5,
            action_required="None",
            deadline=None,
            impact_score=0.0,
            stakeholders=[]
        )

        assert signal.impact_score == 0.0

    def test_signal_with_very_high_confidence(self):
        """Test signal with maximum confidence."""
        signal = Signal(
            source="test",
            category="test",
            priority=SignalPriority.CRITICAL,
            message="High confidence alert",
            confidence=1.0,
            action_required="Act immediately",
            deadline=None,
            impact_score=100.0,
            stakeholders=[]
        )

        assert signal.confidence == 1.0

    def test_empty_stakeholders_list(self):
        """Test handling of empty stakeholders."""
        system = ExecutiveIntelligenceSystem()

        signal = Signal(
            source="test",
            category="test",
            priority=SignalPriority.CRITICAL,
            message="Test",
            confidence=0.8,
            action_required="Act",
            deadline=None,
            impact_score=80.0,
            stakeholders=[]
        )

        brief = system.generate_daily_brief([signal])

        # Should default to 'CEO' when no stakeholders
        assert brief['critical_actions'][0]['owner'] == 'CEO'

    def test_scan_with_partial_data(self):
        """Test scanning with only some data sources."""
        system = ExecutiveIntelligenceSystem()

        data_feeds = {
            'team_health': {'health_score': 30}
            # Missing other sources
        }

        signals = system.scan_all_signals(data_feeds)

        # Should not crash, returns valid list
        assert isinstance(signals, list)
