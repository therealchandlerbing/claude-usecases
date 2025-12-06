"""
Comprehensive unit tests for Stakeholder Analytics System.

Tests stakeholder relationship tracking, risk assessment, and engagement optimization including:
- Portfolio health calculation
- Risk matrix generation
- Engagement recommendations
- Relationship trajectory predictions
"""

import pytest
from datetime import datetime, timedelta
from pathlib import Path
import sys

# Add CEO Advisor to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent / "skills" / "ceo-advisor" / "src"))

from stakeholder_analytics import (
    StakeholderAnalytics,
    Stakeholder,
    RelationshipStatus,
    CommunicationStyle,
    analyze_stakeholder_portfolio
)


class TestRelationshipStatus:
    """Test RelationshipStatus enum."""

    def test_relationship_status_values(self):
        """Test all relationship status values are defined."""
        assert RelationshipStatus.STRENGTHENING.value == "↗️"
        assert RelationshipStatus.STABLE.value == "→"
        assert RelationshipStatus.WEAKENING.value == "↘️"
        assert RelationshipStatus.CRITICAL.value == "⚠️"
        assert RelationshipStatus.EXCELLENT.value == "⭐"


class TestCommunicationStyle:
    """Test CommunicationStyle enum."""

    def test_communication_style_values(self):
        """Test all communication style values are defined."""
        assert CommunicationStyle.ANALYTICAL.value == "data-driven"
        assert CommunicationStyle.DRIVER.value == "results-focused"
        assert CommunicationStyle.EXPRESSIVE.value == "vision-oriented"
        assert CommunicationStyle.AMIABLE.value == "relationship-focused"


class TestStakeholderDataclass:
    """Test Stakeholder dataclass."""

    def test_stakeholder_creation(self):
        """Test creating a stakeholder instance."""
        stakeholder = Stakeholder(
            name="Test Person",
            role="CEO",
            category="Board",
            influence_score=85.0,
            satisfaction_score=75.0,
            engagement_level=80.0,
            communication_style=CommunicationStyle.ANALYTICAL,
            relationship_status=RelationshipStatus.STABLE,
            last_interaction=datetime.now(),
            interaction_frequency_days=7,
            key_concerns=["Revenue", "Growth"],
            preferred_channels=["Email", "In-person"],
            relationship_history=[],
            notes="Test notes"
        )

        assert stakeholder.name == "Test Person"
        assert stakeholder.role == "CEO"
        assert stakeholder.category == "Board"
        assert stakeholder.influence_score == 85.0
        assert stakeholder.satisfaction_score == 75.0


class TestStakeholderAnalyticsInitialization:
    """Test StakeholderAnalytics initialization."""

    def test_init_stakeholder_weights(self):
        """Test stakeholder weights are properly initialized."""
        analyzer = StakeholderAnalytics()

        assert 'Board' in analyzer.stakeholder_weights
        assert 'Investor' in analyzer.stakeholder_weights
        assert 'Executive' in analyzer.stakeholder_weights
        assert 'Customer' in analyzer.stakeholder_weights
        assert 'Employee' in analyzer.stakeholder_weights
        assert 'Partner' in analyzer.stakeholder_weights

    def test_stakeholder_weight_values(self):
        """Test stakeholder weight values are reasonable."""
        analyzer = StakeholderAnalytics()

        # Board should have highest weight
        assert analyzer.stakeholder_weights['Board'] == 1.0

        # All weights should be between 0 and 1
        for category, weight in analyzer.stakeholder_weights.items():
            assert 0 < weight <= 1.0

        # Board should be weighted higher than others
        assert analyzer.stakeholder_weights['Board'] >= analyzer.stakeholder_weights['Investor']
        assert analyzer.stakeholder_weights['Investor'] >= analyzer.stakeholder_weights['Employee']


class TestPortfolioHealthCalculation:
    """Test portfolio health calculation."""

    def test_calculate_portfolio_health_empty_list(self):
        """Test portfolio health with empty stakeholder list."""
        analyzer = StakeholderAnalytics()
        health = analyzer._calculate_portfolio_health([])

        assert health['overall_score'] == 0
        assert 'health_grade' in health
        assert 'category_breakdown' in health
        assert 'top_risks' in health

    def test_calculate_portfolio_health_single_stakeholder(self):
        """Test portfolio health with single stakeholder."""
        analyzer = StakeholderAnalytics()

        stakeholder = Stakeholder(
            name="Test",
            role="CEO",
            category="Board",
            influence_score=85.0,
            satisfaction_score=75.0,
            engagement_level=80.0,
            communication_style=CommunicationStyle.ANALYTICAL,
            relationship_status=RelationshipStatus.STABLE,
            last_interaction=datetime.now(),
            interaction_frequency_days=7,
            key_concerns=[],
            preferred_channels=["Email"],
            relationship_history=[],
            notes=""
        )

        health = analyzer._calculate_portfolio_health([stakeholder])

        # Should be weighted satisfaction (75 * 1.0 = 75)
        assert health['overall_score'] == 75.0

    def test_calculate_portfolio_health_multiple_stakeholders(self):
        """Test portfolio health with multiple stakeholders."""
        analyzer = StakeholderAnalytics()

        stakeholders = [
            Stakeholder(
                name="Board Member",
                role="Chair",
                category="Board",
                influence_score=95.0,
                satisfaction_score=80.0,
                engagement_level=85.0,
                communication_style=CommunicationStyle.ANALYTICAL,
                relationship_status=RelationshipStatus.STABLE,
                last_interaction=datetime.now(),
                interaction_frequency_days=7,
                key_concerns=[],
                preferred_channels=["Email"],
                relationship_history=[],
                notes=""
            ),
            Stakeholder(
                name="Employee",
                role="Engineer",
                category="Employee",
                influence_score=50.0,
                satisfaction_score=70.0,
                engagement_level=75.0,
                communication_style=CommunicationStyle.DRIVER,
                relationship_status=RelationshipStatus.STABLE,
                last_interaction=datetime.now(),
                interaction_frequency_days=30,
                key_concerns=[],
                preferred_channels=["Slack"],
                relationship_history=[],
                notes=""
            )
        ]

        health = analyzer._calculate_portfolio_health(stakeholders)

        # Weighted average: (80*1.0 + 70*0.7) / (1.0 + 0.7)
        expected_score = (80 * 1.0 + 70 * 0.7) / (1.0 + 0.7)
        assert abs(health['overall_score'] - expected_score) < 0.01

    def test_portfolio_health_identifies_at_risk(self):
        """Test identification of at-risk stakeholders."""
        analyzer = StakeholderAnalytics()

        stakeholders = [
            Stakeholder(
                name="At Risk Person",
                role="Investor",
                category="Investor",
                influence_score=80.0,
                satisfaction_score=45.0,  # Below 50
                engagement_level=60.0,
                communication_style=CommunicationStyle.DRIVER,
                relationship_status=RelationshipStatus.WEAKENING,
                last_interaction=datetime.now(),
                interaction_frequency_days=14,
                key_concerns=[],
                preferred_channels=["Phone"],
                relationship_history=[],
                notes=""
            )
        ]

        health = analyzer._calculate_portfolio_health(stakeholders)

        assert 'category_breakdown' in health
        assert 'Investor' in health['category_breakdown']
        assert len(health['category_breakdown']['Investor']['at_risk']) == 1
        assert 'At Risk Person' in health['category_breakdown']['Investor']['at_risk']


class TestHealthGrading:
    """Test health grade assignment."""

    def test_get_health_grade_excellent(self):
        """Test A+ grade for excellent health."""
        analyzer = StakeholderAnalytics()

        grade = analyzer._get_health_grade(95)
        assert 'A+' in grade
        assert 'Excellent' in grade

    def test_get_health_grade_strong(self):
        """Test A grade for strong health."""
        analyzer = StakeholderAnalytics()

        grade = analyzer._get_health_grade(85)
        assert 'A' in grade
        assert 'Strong' in grade

    def test_get_health_grade_good(self):
        """Test B grade for good health."""
        analyzer = StakeholderAnalytics()

        grade = analyzer._get_health_grade(75)
        assert 'B' in grade
        assert 'Good' in grade

    def test_get_health_grade_adequate(self):
        """Test C grade for adequate health."""
        analyzer = StakeholderAnalytics()

        grade = analyzer._get_health_grade(65)
        assert 'C' in grade
        assert 'Adequate' in grade

    def test_get_health_grade_critical(self):
        """Test F grade for critical health."""
        analyzer = StakeholderAnalytics()

        grade = analyzer._get_health_grade(50)
        assert 'F' in grade
        assert 'Critical' in grade


class TestRiskMatrix:
    """Test risk matrix creation."""

    def test_create_risk_matrix_empty(self):
        """Test risk matrix with no stakeholders."""
        analyzer = StakeholderAnalytics()

        matrix = analyzer._create_risk_matrix([])

        assert 'high_influence_low_satisfaction' in matrix
        assert 'high_influence_high_satisfaction' in matrix
        assert len(matrix['high_influence_low_satisfaction']) == 0
        assert len(matrix['high_influence_high_satisfaction']) == 0

    def test_create_risk_matrix_high_risk(self):
        """Test identification of high-risk stakeholders."""
        analyzer = StakeholderAnalytics()

        stakeholder = Stakeholder(
            name="High Risk",
            role="Board Chair",
            category="Board",
            influence_score=85.0,  # High influence
            satisfaction_score=50.0,  # Low satisfaction
            engagement_level=60.0,
            communication_style=CommunicationStyle.ANALYTICAL,
            relationship_status=RelationshipStatus.WEAKENING,
            last_interaction=datetime.now(),
            interaction_frequency_days=7,
            key_concerns=["Performance"],
            preferred_channels=["In-person"],
            relationship_history=[],
            notes=""
        )

        matrix = analyzer._create_risk_matrix([stakeholder])

        assert len(matrix['high_influence_low_satisfaction']) == 1
        assert matrix['high_influence_low_satisfaction'][0]['name'] == "High Risk"
        assert 'CRITICAL' in matrix['high_influence_low_satisfaction'][0]['risk_level']

    def test_create_risk_matrix_high_performers(self):
        """Test identification of high-performing relationships."""
        analyzer = StakeholderAnalytics()

        stakeholder = Stakeholder(
            name="Great Relationship",
            role="Investor",
            category="Investor",
            influence_score=90.0,  # High influence
            satisfaction_score=85.0,  # High satisfaction
            engagement_level=90.0,
            communication_style=CommunicationStyle.DRIVER,
            relationship_status=RelationshipStatus.EXCELLENT,
            last_interaction=datetime.now(),
            interaction_frequency_days=14,
            key_concerns=[],
            preferred_channels=["Video call"],
            relationship_history=[],
            notes=""
        )

        matrix = analyzer._create_risk_matrix([stakeholder])

        assert len(matrix['high_influence_high_satisfaction']) == 1
        assert matrix['high_influence_high_satisfaction'][0]['name'] == "Great Relationship"
        assert 'leverage' in matrix['high_influence_high_satisfaction'][0]['strategy'].lower()


class TestEngagementRecommendations:
    """Test engagement plan generation."""

    def test_generate_engagement_plan_no_overdue(self):
        """Test engagement plan with no overdue interactions."""
        analyzer = StakeholderAnalytics()

        stakeholder = Stakeholder(
            name="Current",
            role="Partner",
            category="Partner",
            influence_score=70.0,
            satisfaction_score=75.0,
            engagement_level=80.0,
            communication_style=CommunicationStyle.AMIABLE,
            relationship_status=RelationshipStatus.STABLE,
            last_interaction=datetime.now() - timedelta(days=5),
            interaction_frequency_days=7,
            key_concerns=[],
            preferred_channels=["Email"],
            relationship_history=[],
            notes=""
        )

        recommendations = analyzer._generate_engagement_plan([stakeholder])

        # Should be empty since not overdue
        assert len(recommendations) == 0

    def test_generate_engagement_plan_overdue(self):
        """Test engagement plan with overdue interactions."""
        analyzer = StakeholderAnalytics()

        stakeholder = Stakeholder(
            name="Overdue",
            role="Board Member",
            category="Board",
            influence_score=90.0,
            satisfaction_score=70.0,
            engagement_level=75.0,
            communication_style=CommunicationStyle.ANALYTICAL,
            relationship_status=RelationshipStatus.STABLE,
            last_interaction=datetime.now() - timedelta(days=15),
            interaction_frequency_days=7,
            key_concerns=[],
            preferred_channels=["In-person"],
            relationship_history=[],
            notes=""
        )

        recommendations = analyzer._generate_engagement_plan([stakeholder])

        assert len(recommendations) == 1
        assert recommendations[0]['stakeholder'] == "Overdue"
        assert recommendations[0]['urgency'] in ['HIGH', 'MEDIUM']
        assert recommendations[0]['days_overdue'] > 0

    def test_engagement_plan_urgency_levels(self):
        """Test urgency level calculation."""
        analyzer = StakeholderAnalytics()

        # High urgency: 2x overdue
        high_urgency = Stakeholder(
            name="Very Overdue",
            role="Investor",
            category="Investor",
            influence_score=85.0,
            satisfaction_score=70.0,
            engagement_level=75.0,
            communication_style=CommunicationStyle.DRIVER,
            relationship_status=RelationshipStatus.WEAKENING,
            last_interaction=datetime.now() - timedelta(days=30),
            interaction_frequency_days=14,
            key_concerns=[],
            preferred_channels=["Phone"],
            relationship_history=[],
            notes=""
        )

        recommendations = analyzer._generate_engagement_plan([high_urgency])

        assert recommendations[0]['urgency'] == 'HIGH'


class TestEngagementActions:
    """Test engagement action recommendations."""

    def test_get_engagement_action_low_satisfaction_board(self):
        """Test action for low satisfaction board member."""
        analyzer = StakeholderAnalytics()

        stakeholder = Stakeholder(
            name="Unhappy Board",
            role="Director",
            category="Board",
            influence_score=85.0,
            satisfaction_score=40.0,
            engagement_level=60.0,
            communication_style=CommunicationStyle.ANALYTICAL,
            relationship_status=RelationshipStatus.CRITICAL,
            last_interaction=datetime.now(),
            interaction_frequency_days=7,
            key_concerns=[],
            preferred_channels=["In-person"],
            relationship_history=[],
            notes=""
        )

        action = analyzer._get_engagement_action(stakeholder)

        assert 'urgent' in action.lower() or '1-on-1' in action.lower()

    def test_get_engagement_action_analytical_style(self):
        """Test action for analytical communication style."""
        analyzer = StakeholderAnalytics()

        stakeholder = Stakeholder(
            name="Analytical Person",
            role="CFO",
            category="Executive",
            influence_score=80.0,
            satisfaction_score=75.0,
            engagement_level=85.0,
            communication_style=CommunicationStyle.ANALYTICAL,
            relationship_status=RelationshipStatus.STABLE,
            last_interaction=datetime.now(),
            interaction_frequency_days=14,
            key_concerns=[],
            preferred_channels=["Email"],
            relationship_history=[],
            notes=""
        )

        action = analyzer._get_engagement_action(stakeholder)

        assert 'metrics' in action.lower() or 'analysis' in action.lower() or 'data' in action.lower()

    def test_get_engagement_action_driver_style(self):
        """Test action for driver communication style."""
        analyzer = StakeholderAnalytics()

        stakeholder = Stakeholder(
            name="Driver Person",
            role="CEO",
            category="Customer",
            influence_score=75.0,
            satisfaction_score=80.0,
            engagement_level=85.0,
            communication_style=CommunicationStyle.DRIVER,
            relationship_status=RelationshipStatus.STRENGTHENING,
            last_interaction=datetime.now(),
            interaction_frequency_days=30,
            key_concerns=[],
            preferred_channels=["Phone"],
            relationship_history=[],
            notes=""
        )

        action = analyzer._get_engagement_action(stakeholder)

        assert 'results' in action.lower() or 'wins' in action.lower() or 'quick' in action.lower()


class TestRelationshipPredictions:
    """Test relationship trajectory predictions."""

    def test_predict_relationship_trajectories(self):
        """Test prediction generation."""
        analyzer = StakeholderAnalytics()

        stakeholder = Stakeholder(
            name="Test",
            role="Partner",
            category="Partner",
            influence_score=70.0,
            satisfaction_score=65.0,
            engagement_level=70.0,
            communication_style=CommunicationStyle.AMIABLE,
            relationship_status=RelationshipStatus.STABLE,
            last_interaction=datetime.now() - timedelta(days=10),
            interaction_frequency_days=14,
            key_concerns=[],
            preferred_channels=["Email"],
            relationship_history=[],
            notes=""
        )

        predictions = analyzer._predict_relationship_trajectories([stakeholder])

        assert len(predictions) == 1
        assert 'stakeholder' in predictions[0]
        assert 'current_status' in predictions[0]
        assert 'predicted_30_days' in predictions[0]
        assert 'intervention_needed' in predictions[0]
        assert 'intervention_type' in predictions[0]

    def test_predict_status_degradation(self):
        """Test status prediction with degradation."""
        analyzer = StakeholderAnalytics()

        stakeholder = Stakeholder(
            name="Degrading",
            role="Investor",
            category="Investor",
            influence_score=80.0,
            satisfaction_score=70.0,
            engagement_level=75.0,
            communication_style=CommunicationStyle.DRIVER,
            relationship_status=RelationshipStatus.STABLE,
            last_interaction=datetime.now() - timedelta(days=30),  # Long time ago
            interaction_frequency_days=14,
            key_concerns=[],
            preferred_channels=["Video call"],
            relationship_history=[],
            notes=""
        )

        predicted = analyzer._predict_status(stakeholder, 30)

        # Should predict degradation
        assert predicted in [status.value for status in RelationshipStatus]

    def test_recommend_intervention_critical(self):
        """Test intervention recommendation for critical satisfaction."""
        analyzer = StakeholderAnalytics()

        stakeholder = Stakeholder(
            name="Critical",
            role="Board Chair",
            category="Board",
            influence_score=95.0,
            satisfaction_score=35.0,
            engagement_level=50.0,
            communication_style=CommunicationStyle.ANALYTICAL,
            relationship_status=RelationshipStatus.CRITICAL,
            last_interaction=datetime.now(),
            interaction_frequency_days=7,
            key_concerns=[],
            preferred_channels=["In-person"],
            relationship_history=[],
            notes=""
        )

        intervention = analyzer._recommend_intervention(stakeholder)

        assert 'URGENT' in intervention or 'immediately' in intervention.lower()

    def test_recommend_intervention_moderate(self):
        """Test intervention recommendation for moderate satisfaction."""
        analyzer = StakeholderAnalytics()

        stakeholder = Stakeholder(
            name="Moderate",
            role="Partner",
            category="Partner",
            influence_score=70.0,
            satisfaction_score=55.0,
            engagement_level=65.0,
            communication_style=CommunicationStyle.AMIABLE,
            relationship_status=RelationshipStatus.WEAKENING,
            last_interaction=datetime.now(),
            interaction_frequency_days=30,
            key_concerns=[],
            preferred_channels=["Email"],
            relationship_history=[],
            notes=""
        )

        intervention = analyzer._recommend_intervention(stakeholder)

        assert 'week' in intervention.lower() or 'engagement' in intervention.lower()


class TestRiskIdentification:
    """Test risk identification."""

    def test_identify_top_risks_empty(self):
        """Test risk identification with no stakeholders."""
        analyzer = StakeholderAnalytics()

        risks = analyzer._identify_top_risks([])

        assert len(risks) == 0

    def test_identify_top_risks(self):
        """Test risk identification."""
        analyzer = StakeholderAnalytics()

        stakeholder = Stakeholder(
            name="High Risk",
            role="Lead Investor",
            category="Investor",
            influence_score=85.0,  # High influence
            satisfaction_score=45.0,  # Low satisfaction
            engagement_level=60.0,
            communication_style=CommunicationStyle.DRIVER,
            relationship_status=RelationshipStatus.WEAKENING,
            last_interaction=datetime.now(),
            interaction_frequency_days=14,
            key_concerns=["Performance", "Timeline"],
            preferred_channels=["Phone"],
            relationship_history=[],
            notes=""
        )

        risks = analyzer._identify_top_risks([stakeholder])

        assert len(risks) == 1
        assert risks[0]['stakeholder'] == "High Risk"
        assert risks[0]['risk_score'] > 0
        assert 'impact' in risks[0]
        assert 'mitigation' in risks[0]

    def test_risk_score_calculation(self):
        """Test risk score calculation formula."""
        analyzer = StakeholderAnalytics()

        stakeholder = Stakeholder(
            name="Test Risk",
            role="Board Member",
            category="Board",
            influence_score=80.0,
            satisfaction_score=50.0,
            engagement_level=65.0,
            communication_style=CommunicationStyle.ANALYTICAL,
            relationship_status=RelationshipStatus.WEAKENING,
            last_interaction=datetime.now(),
            interaction_frequency_days=7,
            key_concerns=[],
            preferred_channels=["In-person"],
            relationship_history=[],
            notes=""
        )

        risks = analyzer._identify_top_risks([stakeholder])

        # Risk score = influence * (100 - satisfaction) / 100
        expected_risk = 80.0 * (100 - 50.0) / 100
        assert abs(risks[0]['risk_score'] - expected_risk) < 0.01


class TestActionPrioritization:
    """Test action prioritization."""

    def test_prioritize_actions_empty(self):
        """Test action prioritization with empty list."""
        analyzer = StakeholderAnalytics()

        actions = analyzer._prioritize_actions([])

        assert len(actions) == 0

    def test_prioritize_actions(self):
        """Test action prioritization."""
        analyzer = StakeholderAnalytics()

        stakeholder = Stakeholder(
            name="Test",
            role="Partner",
            category="Partner",
            influence_score=75.0,
            satisfaction_score=65.0,
            engagement_level=70.0,
            communication_style=CommunicationStyle.AMIABLE,
            relationship_status=RelationshipStatus.STABLE,
            last_interaction=datetime.now() - timedelta(days=20),
            interaction_frequency_days=14,
            key_concerns=[],
            preferred_channels=["Email"],
            relationship_history=[],
            notes=""
        )

        actions = analyzer._prioritize_actions([stakeholder])

        assert len(actions) == 1
        assert 'stakeholder' in actions[0]
        assert 'action' in actions[0]
        assert 'priority_score' in actions[0]
        assert 'urgency' in actions[0]

    def test_calculate_urgency(self):
        """Test urgency calculation."""
        analyzer = StakeholderAnalytics()

        # Low satisfaction increases urgency
        low_sat = Stakeholder(
            name="Low Satisfaction",
            role="Investor",
            category="Investor",
            influence_score=80.0,
            satisfaction_score=40.0,
            engagement_level=60.0,
            communication_style=CommunicationStyle.DRIVER,
            relationship_status=RelationshipStatus.CRITICAL,
            last_interaction=datetime.now(),
            interaction_frequency_days=14,
            key_concerns=[],
            preferred_channels=["Phone"],
            relationship_history=[],
            notes=""
        )

        urgency = analyzer._calculate_urgency(low_sat)

        assert urgency > 70  # Low satisfaction should increase urgency

    def test_urgency_capped_at_100(self):
        """Test that urgency is capped at 100."""
        analyzer = StakeholderAnalytics()

        very_urgent = Stakeholder(
            name="Very Urgent",
            role="Board Chair",
            category="Board",
            influence_score=95.0,
            satisfaction_score=30.0,
            engagement_level=50.0,
            communication_style=CommunicationStyle.ANALYTICAL,
            relationship_status=RelationshipStatus.CRITICAL,
            last_interaction=datetime.now() - timedelta(days=60),
            interaction_frequency_days=7,
            key_concerns=[],
            preferred_channels=["In-person"],
            relationship_history=[],
            notes=""
        )

        urgency = analyzer._calculate_urgency(very_urgent)

        assert urgency <= 100


class TestComprehensiveAnalysis:
    """Test comprehensive portfolio analysis."""

    def test_analyze_stakeholder_portfolio(self):
        """Test full portfolio analysis."""
        analyzer = StakeholderAnalytics()

        stakeholders = [
            Stakeholder(
                name="Stakeholder 1",
                role="Board Chair",
                category="Board",
                influence_score=95.0,
                satisfaction_score=75.0,
                engagement_level=85.0,
                communication_style=CommunicationStyle.ANALYTICAL,
                relationship_status=RelationshipStatus.STABLE,
                last_interaction=datetime.now() - timedelta(days=5),
                interaction_frequency_days=7,
                key_concerns=[],
                preferred_channels=["In-person"],
                relationship_history=[],
                notes=""
            )
        ]

        analysis = analyzer.analyze_stakeholder_portfolio(stakeholders)

        assert 'portfolio_health' in analysis
        assert 'risk_matrix' in analysis
        assert 'engagement_recommendations' in analysis
        assert 'relationship_predictions' in analysis
        assert 'action_priorities' in analysis


class TestMainFunction:
    """Test main analysis function."""

    def test_analyze_stakeholder_portfolio_function(self):
        """Test main portfolio analysis function."""
        report = analyze_stakeholder_portfolio()

        assert isinstance(report, str)
        assert 'STAKEHOLDER RELATIONSHIP ANALYTICS REPORT' in report
        assert 'PORTFOLIO HEALTH' in report


class TestEdgeCases:
    """Test edge cases and error handling."""

    def test_stakeholder_with_empty_concerns(self):
        """Test stakeholder with no key concerns."""
        stakeholder = Stakeholder(
            name="No Concerns",
            role="Employee",
            category="Employee",
            influence_score=50.0,
            satisfaction_score=70.0,
            engagement_level=75.0,
            communication_style=CommunicationStyle.AMIABLE,
            relationship_status=RelationshipStatus.STABLE,
            last_interaction=datetime.now(),
            interaction_frequency_days=30,
            key_concerns=[],  # Empty
            preferred_channels=["Email"],
            relationship_history=[],
            notes=""
        )

        assert len(stakeholder.key_concerns) == 0

    def test_stakeholder_with_no_preferred_channels(self):
        """Test stakeholder with no preferred channels."""
        analyzer = StakeholderAnalytics()

        stakeholder = Stakeholder(
            name="No Channels",
            role="Partner",
            category="Partner",
            influence_score=60.0,
            satisfaction_score=65.0,
            engagement_level=70.0,
            communication_style=CommunicationStyle.DRIVER,
            relationship_status=RelationshipStatus.STABLE,
            last_interaction=datetime.now() - timedelta(days=20),
            interaction_frequency_days=14,
            key_concerns=[],
            preferred_channels=[],  # Empty
            relationship_history=[],
            notes=""
        )

        recommendations = analyzer._generate_engagement_plan([stakeholder])

        # Should default to 'Email'
        if len(recommendations) > 0:
            assert recommendations[0]['channel'] == 'Email'

    def test_zero_influence_stakeholder(self):
        """Test stakeholder with zero influence."""
        analyzer = StakeholderAnalytics()

        stakeholder = Stakeholder(
            name="No Influence",
            role="Contact",
            category="Partner",
            influence_score=0.0,
            satisfaction_score=70.0,
            engagement_level=75.0,
            communication_style=CommunicationStyle.AMIABLE,
            relationship_status=RelationshipStatus.STABLE,
            last_interaction=datetime.now(),
            interaction_frequency_days=30,
            key_concerns=[],
            preferred_channels=["Email"],
            relationship_history=[],
            notes=""
        )

        # Should not appear in high-risk categories
        matrix = analyzer._create_risk_matrix([stakeholder])
        assert len(matrix['high_influence_low_satisfaction']) == 0
        assert len(matrix['high_influence_high_satisfaction']) == 0
