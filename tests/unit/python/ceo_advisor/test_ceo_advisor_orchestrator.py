"""
Comprehensive unit tests for CEO Advisor Orchestrator.

Tests all orchestrator functionality including:
- Daily intelligence brief generation
- Board meeting preparation
- Crisis response protocols
- Strategic planning sessions
- Comprehensive analysis dashboard
"""

import pytest
import json
from datetime import datetime, timedelta
from pathlib import Path
import sys

# Add CEO Advisor to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent / ".claude" / "skills" / "ceo-advisor" / "src"))

import ceo_advisor_orchestrator
from ceo_advisor_orchestrator import CEOAdvisorOrchestrator, main


class TestCEOAdvisorInitialization:
    """Test orchestrator initialization and configuration."""

    def test_init_with_default_config(self):
        """Test initialization with default configuration."""
        orchestrator = CEOAdvisorOrchestrator()

        assert orchestrator.config is not None
        assert 'intelligence' in orchestrator.config
        assert 'stakeholder' in orchestrator.config
        assert 'optimization' in orchestrator.config
        assert 'strategy' in orchestrator.config

        # Verify initial state
        assert orchestrator.intelligence_system is None
        assert orchestrator.stakeholder_analytics is None
        assert orchestrator.ceo_optimizer is None
        assert orchestrator.strategy_analyzer is None
        assert orchestrator.financial_analyzer is None
        assert orchestrator.last_analysis == {}
        assert orchestrator.alerts == []
        assert orchestrator.recommendations == []

    def test_init_with_custom_config(self):
        """Test initialization with custom configuration."""
        custom_config = {
            'intelligence': {
                'sensitivity': 'low',
                'scan_frequency': 'hourly',
                'prediction_horizon': 60
            }
        }

        orchestrator = CEOAdvisorOrchestrator(custom_config)
        assert orchestrator.config == custom_config
        assert orchestrator.config['intelligence']['sensitivity'] == 'low'

    def test_load_default_config(self):
        """Test default configuration loading."""
        orchestrator = CEOAdvisorOrchestrator()
        config = orchestrator._load_default_config()

        # Intelligence config
        assert config['intelligence']['sensitivity'] == 'high'
        assert config['intelligence']['scan_frequency'] == 'real-time'
        assert config['intelligence']['prediction_horizon'] == 30

        # Stakeholder config
        assert config['stakeholder']['tracking_depth'] == 'comprehensive'
        assert config['stakeholder']['sentiment_threshold'] == 0.7
        assert config['stakeholder']['relationship_check_frequency'] == 7

        # Optimization config
        assert config['optimization']['mode'] == 'balanced'
        assert config['optimization']['focus_time_target'] == 2.0
        assert config['optimization']['meeting_batch'] is True
        assert config['optimization']['energy_tracking'] is True

        # Strategy config
        assert config['strategy']['review_cycle'] == 'quarterly'
        assert config['strategy']['scenario_count'] == 3
        assert config['strategy']['risk_tolerance'] == 'moderate'


class TestDailyIntelligenceBrief:
    """Test daily intelligence brief generation."""

    def test_run_daily_intelligence_brief_structure(self):
        """Test that daily brief has correct structure."""
        orchestrator = CEOAdvisorOrchestrator()
        brief = orchestrator.run_daily_intelligence_brief()

        # Verify structure
        assert 'generated_at' in brief
        assert 'executive_summary' in brief
        assert 'critical_items' in brief
        assert 'stakeholder_updates' in brief
        assert 'schedule_optimization' in brief
        assert 'strategic_insights' in brief
        assert 'action_items' in brief

        # Verify types
        assert isinstance(brief['critical_items'], list)
        assert isinstance(brief['stakeholder_updates'], list)
        assert isinstance(brief['schedule_optimization'], dict)
        assert isinstance(brief['strategic_insights'], list)
        assert isinstance(brief['action_items'], list)

    def test_daily_brief_has_timestamp(self):
        """Test that brief includes valid timestamp."""
        orchestrator = CEOAdvisorOrchestrator()
        brief = orchestrator.run_daily_intelligence_brief()

        # Parse timestamp
        generated_time = datetime.fromisoformat(brief['generated_at'])

        # Should be within last minute
        assert (datetime.now() - generated_time).total_seconds() < 60

    def test_daily_brief_executive_summary_content(self):
        """Test executive summary generation."""
        orchestrator = CEOAdvisorOrchestrator()
        brief = orchestrator.run_daily_intelligence_brief()

        summary = brief['executive_summary']
        assert isinstance(summary, str)
        assert len(summary) > 0
        assert 'critical items' in summary.lower() or 'action items' in summary.lower()

    def test_daily_brief_action_items_prioritized(self):
        """Test that action items are properly prioritized."""
        orchestrator = CEOAdvisorOrchestrator()
        brief = orchestrator.run_daily_intelligence_brief()

        action_items = brief['action_items']
        if len(action_items) > 1:
            # Verify priority ordering
            priorities = [item.get('priority', 'Low') for item in action_items]
            priority_order = {'Critical': 0, 'High': 1, 'Medium': 2, 'Low': 3}
            priority_values = [priority_order.get(p, 4) for p in priorities]

            # Should be sorted (lower values first)
            assert priority_values == sorted(priority_values)


class TestBoardPreparation:
    """Test board meeting preparation functionality."""

    def test_run_board_preparation_structure(self):
        """Test board preparation output structure."""
        orchestrator = CEOAdvisorOrchestrator()
        board_date = datetime.now() + timedelta(days=7)
        prep = orchestrator.run_board_preparation(board_date)

        # Verify structure
        assert 'meeting_date' in prep
        assert 'board_member_analysis' in prep
        assert 'likely_questions' in prep
        assert 'narrative_strategy' in prep
        assert 'risk_areas' in prep
        assert 'supporting_materials' in prep
        assert 'follow_up_plan' in prep

        # Verify types
        assert isinstance(prep['board_member_analysis'], list)
        assert isinstance(prep['likely_questions'], list)
        assert isinstance(prep['narrative_strategy'], dict)
        assert isinstance(prep['risk_areas'], list)
        assert isinstance(prep['supporting_materials'], list)
        assert isinstance(prep['follow_up_plan'], dict)

    def test_board_preparation_date_handling(self):
        """Test board date is properly stored."""
        orchestrator = CEOAdvisorOrchestrator()
        board_date = datetime.now() + timedelta(days=14)
        prep = orchestrator.run_board_preparation(board_date)

        meeting_date = datetime.fromisoformat(prep['meeting_date'])
        assert meeting_date.date() == board_date.date()

    def test_board_member_analysis_content(self):
        """Test board member analysis includes key information."""
        orchestrator = CEOAdvisorOrchestrator()
        board_date = datetime.now() + timedelta(days=7)
        prep = orchestrator.run_board_preparation(board_date)

        members = prep['board_member_analysis']
        assert len(members) > 0

        # Check first member has required fields
        member = members[0]
        assert 'name' in member
        assert 'sentiment' in member
        assert 'concerns' in member
        assert 'communication_style' in member
        assert 'engagement_strategy' in member

    def test_likely_questions_prediction(self):
        """Test board question prediction."""
        orchestrator = CEOAdvisorOrchestrator()
        board_date = datetime.now() + timedelta(days=7)
        prep = orchestrator.run_board_preparation(board_date)

        questions = prep['likely_questions']
        assert len(questions) > 0

        # Check question structure
        question = questions[0]
        assert 'question' in question
        assert 'probability' in question
        assert 'preparation' in question
        assert 0 <= question['probability'] <= 1


class TestCrisisResponse:
    """Test crisis response protocol functionality."""

    def test_run_crisis_response_structure(self):
        """Test crisis response output structure."""
        orchestrator = CEOAdvisorOrchestrator()
        crisis = "Major customer threatening to leave"
        response = orchestrator.run_crisis_response(crisis)

        # Verify structure
        assert 'crisis' in response
        assert 'severity_assessment' in response
        assert 'immediate_actions' in response
        assert 'stakeholder_communications' in response
        assert 'resource_allocation' in response
        assert 'monitoring_plan' in response
        assert 'recovery_roadmap' in response

        assert response['crisis'] == crisis

    def test_crisis_severity_assessment_high(self):
        """Test high severity crisis assessment."""
        orchestrator = CEOAdvisorOrchestrator()

        high_severity_keywords = ['critical', 'emergency', 'breach', 'lawsuit', 'major']
        for keyword in high_severity_keywords:
            crisis = f"We have a {keyword} situation"
            severity = orchestrator._assess_crisis_severity(crisis)

            assert severity['level'] == 'High'
            assert severity['impact_score'] >= 80
            assert severity['urgency'] == 'Immediate'
            assert 'Board' in severity['stakeholders_affected']

    def test_crisis_severity_assessment_medium(self):
        """Test medium severity crisis assessment."""
        orchestrator = CEOAdvisorOrchestrator()

        crisis = "We have a problem with a customer"
        severity = orchestrator._assess_crisis_severity(crisis)

        assert severity['level'] == 'Medium'
        assert 50 <= severity['impact_score'] < 80
        assert severity['urgency'] == 'Within 24 hours'

    def test_crisis_severity_assessment_low(self):
        """Test low severity crisis assessment."""
        orchestrator = CEOAdvisorOrchestrator()

        crisis = "Minor inconvenience reported"
        severity = orchestrator._assess_crisis_severity(crisis)

        assert severity['level'] == 'Low'
        assert severity['impact_score'] < 50

    def test_crisis_actions_high_severity(self):
        """Test crisis actions for high severity."""
        orchestrator = CEOAdvisorOrchestrator()

        crisis = "Critical data breach detected"
        severity = orchestrator._assess_crisis_severity(crisis)
        actions = orchestrator._generate_crisis_actions(crisis, severity)

        assert len(actions) >= 3

        # Should include critical actions
        action_texts = [a['action'].lower() for a in actions]
        assert any('crisis response team' in text for text in action_texts)
        assert any('board' in text or 'notify' in text for text in action_texts)

    def test_crisis_communications_plan(self):
        """Test crisis communications planning."""
        orchestrator = CEOAdvisorOrchestrator()

        comms = orchestrator._plan_crisis_communications()

        assert len(comms) > 0
        assert isinstance(comms, list)

        # Check communication structure
        comm = comms[0]
        assert 'audience' in comm
        assert 'channel' in comm
        assert 'timing' in comm
        assert 'message' in comm

    def test_crisis_resource_allocation(self):
        """Test crisis resource allocation."""
        orchestrator = CEOAdvisorOrchestrator()

        resources = orchestrator._allocate_crisis_resources()

        assert 'human_resources' in resources
        assert 'financial_resources' in resources
        assert isinstance(resources['human_resources']['crisis_team'], list)
        assert len(resources['human_resources']['crisis_team']) > 0


class TestStrategicPlanning:
    """Test strategic planning session functionality."""

    def test_run_strategic_planning_structure(self):
        """Test strategic planning output structure."""
        orchestrator = CEOAdvisorOrchestrator()
        session = orchestrator.run_strategic_planning_session()

        # Verify structure
        assert 'environmental_scan' in session
        assert 'strategic_options' in session
        assert 'financial_scenarios' in session
        assert 'risk_assessment' in session
        assert 'implementation_roadmap' in session
        assert 'success_metrics' in session

    def test_strategic_options_generation(self):
        """Test strategic options are generated."""
        orchestrator = CEOAdvisorOrchestrator()
        options = orchestrator._generate_strategic_options()

        assert len(options) > 0

        # Check option structure
        option = options[0]
        assert 'option' in option
        assert 'investment' in option
        assert 'timeline' in option
        assert 'expected_return' in option

    def test_success_metrics_definition(self):
        """Test success metrics are defined."""
        orchestrator = CEOAdvisorOrchestrator()
        metrics = orchestrator._define_success_metrics()

        assert len(metrics) > 0

        # Check metric structure
        metric = metrics[0]
        assert 'metric' in metric
        assert 'current' in metric
        assert 'year_1_target' in metric


class TestComprehensiveAnalysis:
    """Test comprehensive CEO dashboard functionality."""

    def test_run_comprehensive_analysis_structure(self):
        """Test comprehensive analysis output structure."""
        orchestrator = CEOAdvisorOrchestrator()
        dashboard = orchestrator.run_comprehensive_analysis()

        # Verify structure
        assert 'timestamp' in dashboard
        assert 'intelligence' in dashboard
        assert 'stakeholders' in dashboard
        assert 'optimization' in dashboard
        assert 'strategy' in dashboard
        assert 'financials' in dashboard
        assert 'integrated_insights' in dashboard
        assert 'priority_actions' in dashboard

    def test_comprehensive_analysis_timestamp(self):
        """Test dashboard has valid timestamp."""
        orchestrator = CEOAdvisorOrchestrator()
        dashboard = orchestrator.run_comprehensive_analysis()

        timestamp = datetime.fromisoformat(dashboard['timestamp'])
        assert (datetime.now() - timestamp).total_seconds() < 60


class TestIntelligenceMethods:
    """Test intelligence scanning methods."""

    def test_run_intelligence_scan_structure(self):
        """Test intelligence scan returns proper structure."""
        orchestrator = CEOAdvisorOrchestrator()
        intelligence = orchestrator._run_intelligence_scan()

        assert 'critical_actions' in intelligence
        assert 'watch_items' in intelligence
        assert 'opportunities' in intelligence
        assert 'predictions' in intelligence

    def test_intelligence_critical_actions(self):
        """Test critical actions have required fields."""
        orchestrator = CEOAdvisorOrchestrator()
        intelligence = orchestrator._run_intelligence_scan()

        if len(intelligence['critical_actions']) > 0:
            action = intelligence['critical_actions'][0]
            assert 'issue' in action
            assert 'action' in action
            assert 'impact' in action
            assert 'confidence' in action
            assert 0 <= action['confidence'] <= 1


class TestStakeholderMethods:
    """Test stakeholder analysis methods."""

    def test_analyze_stakeholders_structure(self):
        """Test stakeholder analysis returns proper structure."""
        orchestrator = CEOAdvisorOrchestrator()
        stakeholder_data = orchestrator._analyze_stakeholders()

        assert 'portfolio_health' in stakeholder_data
        assert 'at_risk_relationships' in stakeholder_data
        assert 'priority_engagements' in stakeholder_data
        assert 'relationship_forecast' in stakeholder_data

    def test_analyze_board_members(self):
        """Test board member analysis."""
        orchestrator = CEOAdvisorOrchestrator()
        members = orchestrator._analyze_board_members()

        assert len(members) > 0
        member = members[0]
        assert 'name' in member
        assert 'sentiment' in member
        assert 'concerns' in member
        assert isinstance(member['concerns'], list)


class TestOptimizationMethods:
    """Test schedule optimization methods."""

    def test_optimize_schedule_structure(self):
        """Test schedule optimization returns proper structure."""
        orchestrator = CEOAdvisorOrchestrator()
        schedule = orchestrator._optimize_schedule()

        assert 'original_efficiency' in schedule
        assert 'optimized_efficiency' in schedule
        assert 'changes' in schedule
        assert 'delegation_opportunities' in schedule

    def test_schedule_efficiency_improvement(self):
        """Test that optimization improves efficiency."""
        orchestrator = CEOAdvisorOrchestrator()
        schedule = orchestrator._optimize_schedule()

        assert schedule['optimized_efficiency'] >= schedule['original_efficiency']

    def test_optimization_analysis_structure(self):
        """Test optimization analysis returns proper structure."""
        orchestrator = CEOAdvisorOrchestrator()
        analysis = orchestrator._run_optimization_analysis()

        assert 'time_allocation' in analysis
        assert 'energy_profile' in analysis
        assert 'meeting_efficiency' in analysis


class TestStrategyMethods:
    """Test strategy analysis methods."""

    def test_generate_strategic_insights(self):
        """Test strategic insights generation."""
        orchestrator = CEOAdvisorOrchestrator()
        insights = orchestrator._generate_strategic_insights()

        assert len(insights) > 0
        insight = insights[0]
        assert 'insight' in insight
        assert 'timeframe' in insight
        assert 'action' in insight
        assert 'confidence' in insight

    def test_run_strategy_analysis(self):
        """Test strategy analysis."""
        orchestrator = CEOAdvisorOrchestrator()
        analysis = orchestrator._run_strategy_analysis()

        assert 'strategic_health' in analysis
        assert 'market_position' in analysis
        assert 'competitive_advantage' in analysis
        assert 'growth_trajectory' in analysis
        assert 'strategic_options' in analysis


class TestFinancialMethods:
    """Test financial analysis methods."""

    def test_run_financial_analysis_structure(self):
        """Test financial analysis returns proper structure."""
        orchestrator = CEOAdvisorOrchestrator()
        financials = orchestrator._run_financial_analysis()

        assert 'current_runway' in financials
        assert 'scenarios' in financials
        assert 'recommendation' in financials

    def test_financial_scenarios(self):
        """Test financial scenarios include key data."""
        orchestrator = CEOAdvisorOrchestrator()
        financials = orchestrator._run_financial_analysis()

        scenarios = financials['scenarios']
        assert len(scenarios) >= 3  # Aggressive, Base, Conservative

        for scenario in scenarios:
            assert 'name' in scenario
            assert 'probability' in scenario
            assert 'npv' in scenario
            assert 'break_even' in scenario
            assert 0 <= scenario['probability'] <= 1


class TestOutputFormatting:
    """Test output formatting helpers."""

    def test_format_output_summary_includes_key_sections(self):
        """Summary output should highlight executive summary and actions."""
        orchestrator = CEOAdvisorOrchestrator()
        results = {
            'executive_summary': 'Summary text',
            'action_items': [
                {'action': 'Do something important', 'priority': 'Critical', 'deadline': 'Today'},
                {'action': 'Secondary task', 'priority': 'High', 'deadline': 'Tomorrow'},
            ],
            'critical_items': [
                {'issue': 'Issue 1', 'action': 'Resolve'},
                {'issue': 'Issue 2', 'action': 'Monitor'},
            ],
        }

        output = orchestrator.format_output(results, output_type='summary')

        assert "CEO ADVISOR - EXECUTIVE SUMMARY" in output
        assert "SUMMARY: Summary text" in output
        assert "1. Do something important [Critical]" in output
        assert "2. Secondary task [High]" in output
        assert "CRITICAL ITEMS:" in output
        assert "• Issue 1" in output

    def test_format_output_detailed_renders_json(self):
        """Detailed output should render JSON payload."""
        orchestrator = CEOAdvisorOrchestrator()
        results = {'executive_summary': 'Summary text', 'action_items': []}

        output = orchestrator.format_output(results, output_type='detailed')

        assert "CEO ADVISOR - DETAILED ANALYSIS" in output
        assert json.dumps(results, indent=2) in output


class TestMainEntryPoint:
    """Test CLI entry point behavior."""

    def test_main_loads_config_and_runs_daily(self, monkeypatch, tmp_path, capsys):
        """Main should load config file and execute daily command."""

        captured_config = {}

        class DummyOrchestrator:
            def __init__(self, config=None):
                captured_config['config'] = config

            def run_daily_intelligence_brief(self):
                return {
                    'executive_summary': 'Summary text',
                    'action_items': [],
                    'critical_items': [],
                }

            def format_output(self, results, output_type='summary'):
                return f"Output: {results['executive_summary']} ({output_type})"

        # Create custom config file
        config_data = {'intelligence': {'sensitivity': 'low'}}
        config_file = tmp_path / "config.json"
        config_file.write_text(json.dumps(config_data))

        # Replace orchestrator class
        monkeypatch.setattr(ceo_advisor_orchestrator, 'CEOAdvisorOrchestrator', DummyOrchestrator)

        # Invoke CLI
        monkeypatch.setattr(sys, 'argv', ['prog', 'daily', '--config', str(config_file)])
        main()

        # Verify config was loaded and output printed
        assert captured_config['config'] == config_data
        captured = capsys.readouterr().out
        assert "Output: Summary text (summary)" in captured


class TestIntegrationMethods:
    """Test integration and prioritization methods."""

    def test_prioritize_actions_empty_sources(self):
        """Test action prioritization with empty sources."""
        orchestrator = CEOAdvisorOrchestrator()
        actions = orchestrator._prioritize_actions()

        assert isinstance(actions, list)

    def test_prioritize_actions_with_data(self):
        """Test action prioritization with data sources."""
        orchestrator = CEOAdvisorOrchestrator()

        source1 = {
            'critical_actions': [
                {'action': 'Test action 1', 'impact': 'High'},
                {'action': 'Test action 2', 'impact': 'Medium'}
            ]
        }

        actions = orchestrator._prioritize_actions(source1)

        assert isinstance(actions, list)
        assert len(actions) <= 10  # Should return top 10

    def test_generate_executive_summary(self):
        """Test executive summary generation."""
        orchestrator = CEOAdvisorOrchestrator()

        brief = {
            'critical_items': [{'item': 'test'}],
            'stakeholder_updates': [{'update': 'test'}],
            'action_items': [{'action': 'test'}],
            'schedule_optimization': {'optimized_efficiency': 75}
        }

        summary = orchestrator._generate_executive_summary(brief)

        assert isinstance(summary, str)
        assert len(summary) > 0
        assert 'critical items' in summary.lower()


class TestOutputFormatting:
    """Test output formatting methods."""

    def test_format_output_summary(self):
        """Test summary format output."""
        orchestrator = CEOAdvisorOrchestrator()

        results = {
            'executive_summary': 'Test summary',
            'action_items': [
                {'action': 'Action 1', 'priority': 'High', 'deadline': '24 hours'}
            ],
            'critical_items': [
                {'issue': 'Issue 1', 'action': 'Action required'}
            ]
        }

        output = orchestrator.format_output(results, 'summary')

        assert isinstance(output, str)
        assert 'CEO ADVISOR' in output
        assert 'Test summary' in output

    def test_format_output_detailed(self):
        """Test detailed format output."""
        orchestrator = CEOAdvisorOrchestrator()

        results = {'test': 'data'}

        output = orchestrator.format_output(results, 'detailed')

        assert isinstance(output, str)
        assert 'CEO ADVISOR' in output
        # Should contain JSON output
        assert '{' in output


class TestEdgeCases:
    """Test edge cases and error handling."""

    def test_empty_config_initialization(self):
        """Test initialization with empty config.

        Note: The managed version treats empty dict as falsy and loads defaults.
        """
        orchestrator = CEOAdvisorOrchestrator({})
        # Empty dict is falsy in Python, so defaults are loaded
        assert orchestrator.config != {}
        assert 'intelligence' in orchestrator.config

    def test_crisis_with_empty_description(self):
        """Test crisis response with empty description."""
        orchestrator = CEOAdvisorOrchestrator()
        response = orchestrator.run_crisis_response("")

        assert 'severity_assessment' in response
        assert response['severity_assessment']['level'] == 'Low'

    def test_board_preparation_past_date(self):
        """Test board preparation with past date."""
        orchestrator = CEOAdvisorOrchestrator()
        past_date = datetime.now() - timedelta(days=7)
        prep = orchestrator.run_board_preparation(past_date)

        # Should still generate preparation
        assert 'board_member_analysis' in prep

    def test_multiple_consecutive_briefs(self):
        """Test generating multiple briefs consecutively."""
        orchestrator = CEOAdvisorOrchestrator()

        brief1 = orchestrator.run_daily_intelligence_brief()
        brief2 = orchestrator.run_daily_intelligence_brief()

        # Both should be valid
        assert 'generated_at' in brief1
        assert 'generated_at' in brief2

        # Timestamps should be different
        time1 = datetime.fromisoformat(brief1['generated_at'])
        time2 = datetime.fromisoformat(brief2['generated_at'])
        assert time2 >= time1


class TestIntegrationScenarios:
    """Test realistic integration scenarios."""

    def test_complete_daily_workflow(self):
        """Test a complete daily workflow."""
        orchestrator = CEOAdvisorOrchestrator()

        # Morning brief
        brief = orchestrator.run_daily_intelligence_brief()
        assert len(brief['action_items']) > 0

        # If there's a critical issue, might need crisis response
        if len(brief['critical_items']) > 0:
            crisis = brief['critical_items'][0]['issue']
            response = orchestrator.run_crisis_response(crisis)
            assert 'immediate_actions' in response

    def test_board_meeting_cycle(self):
        """Test board meeting preparation cycle."""
        orchestrator = CEOAdvisorOrchestrator()

        # Prepare for upcoming board meeting
        board_date = datetime.now() + timedelta(days=7)
        prep = orchestrator.run_board_preparation(board_date)

        # Should have comprehensive preparation
        assert len(prep['board_member_analysis']) > 0
        assert len(prep['likely_questions']) > 0
        assert len(prep['supporting_materials']) > 0

    def test_strategic_planning_to_execution(self):
        """Test strategic planning to execution flow."""
        orchestrator = CEOAdvisorOrchestrator()

        # Strategic planning session
        session = orchestrator.run_strategic_planning_session()

        # Should generate actionable options
        assert len(session['strategic_options']) > 0
        assert 'implementation_roadmap' in session
        assert 'success_metrics' in session

        # Should be able to track in daily brief
        brief = orchestrator.run_daily_intelligence_brief()
        assert 'strategic_insights' in brief
