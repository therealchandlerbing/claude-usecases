"""
Comprehensive unit tests for CEO Optimizer.

Tests time allocation analysis, energy optimization, and meeting efficiency including:
- Time allocation calculation and gap analysis
- Meeting efficiency metrics
- Focus time analysis
- Optimization opportunity identification
"""

import pytest
from datetime import datetime, timedelta
from pathlib import Path
import sys

# Add CEO Advisor to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent / "skills" / "ceo-advisor" / "src"))

from ceo_optimizer import (
    CEOOptimizer,
    TimeBlock,
    EnergyLevel,
    optimize_ceo_time_energy
)


class TestEnergyLevel:
    """Test EnergyLevel enum."""

    def test_energy_level_values(self):
        """Test all energy level values are defined."""
        assert EnergyLevel.PEAK.value == "🟢"
        assert EnergyLevel.HIGH.value == "🔵"
        assert EnergyLevel.MODERATE.value == "🟡"
        assert EnergyLevel.LOW.value == "🟠"
        assert EnergyLevel.DEPLETED.value == "🔴"


class TestTimeBlockDataclass:
    """Test TimeBlock dataclass."""

    def test_timeblock_creation(self):
        """Test creating a time block instance."""
        start = datetime.now()
        end = start + timedelta(hours=2)

        block = TimeBlock(
            start_time=start,
            end_time=end,
            category='strategic_thinking',
            subcategory='strategy_session',
            energy_cost=85.0,
            value_created=90.0,
            attendees=['CEO', 'CSO'],
            outcome_quality=88.0,
            notes='Test session'
        )

        assert block.category == 'strategic_thinking'
        assert block.subcategory == 'strategy_session'
        assert block.energy_cost == 85.0
        assert block.value_created == 90.0
        assert 'CEO' in block.attendees

    def test_timeblock_duration_calculation(self):
        """Test duration calculation from time block."""
        start = datetime.now()
        end = start + timedelta(hours=2)

        block = TimeBlock(
            start_time=start,
            end_time=end,
            category='test',
            subcategory='test',
            energy_cost=50.0,
            value_created=70.0,
            attendees=[],
            outcome_quality=75.0,
            notes=''
        )

        duration_seconds = (block.end_time - block.start_time).total_seconds()
        assert duration_seconds == 2 * 3600  # 2 hours


class TestCEOOptimizerInitialization:
    """Test CEOOptimizer initialization."""

    def test_init_optimal_allocation(self):
        """Test optimal allocation is properly initialized."""
        optimizer = CEOOptimizer()

        assert 'strategic_thinking' in optimizer.optimal_allocation
        assert 'team_leadership' in optimizer.optimal_allocation
        assert 'external_engagement' in optimizer.optimal_allocation
        assert 'operational_oversight' in optimizer.optimal_allocation
        assert 'customer_interaction' in optimizer.optimal_allocation
        assert 'personal_development' in optimizer.optimal_allocation

    def test_optimal_allocation_targets(self):
        """Test optimal allocation targets add up reasonably."""
        optimizer = CEOOptimizer()

        total_target = sum(cat['target'] for cat in optimizer.optimal_allocation.values())

        # Should add up to 100%
        assert total_target == 100

    def test_optimal_allocation_ranges(self):
        """Test min/max ranges are valid."""
        optimizer = CEOOptimizer()

        for category, targets in optimizer.optimal_allocation.items():
            assert targets['min'] <= targets['target'] <= targets['max']
            assert targets['min'] > 0
            assert targets['max'] <= 100

    def test_init_energy_costs(self):
        """Test energy costs are properly initialized."""
        optimizer = CEOOptimizer()

        assert 'board_meeting' in optimizer.energy_costs
        assert 'strategy_session' in optimizer.energy_costs
        assert 'executive_meeting' in optimizer.energy_costs
        assert 'team_meeting' in optimizer.energy_costs

        # Board meetings should cost more than team meetings
        assert optimizer.energy_costs['board_meeting'] > optimizer.energy_costs['team_meeting']


class TestTimeAllocationCalculation:
    """Test time allocation calculation."""

    def test_calculate_current_allocation_empty(self):
        """Test allocation calculation with no blocks."""
        optimizer = CEOOptimizer()

        allocation = optimizer._calculate_current_allocation([])

        assert allocation == {}

    def test_calculate_current_allocation_single_block(self):
        """Test allocation with single time block."""
        optimizer = CEOOptimizer()

        start = datetime.now()
        end = start + timedelta(hours=2)

        blocks = [
            TimeBlock(
                start_time=start,
                end_time=end,
                category='strategic_thinking',
                subcategory='strategy_session',
                energy_cost=85.0,
                value_created=90.0,
                attendees=['CEO'],
                outcome_quality=88.0,
                notes=''
            )
        ]

        allocation = optimizer._calculate_current_allocation(blocks)

        assert 'strategic_thinking' in allocation
        assert allocation['strategic_thinking']['percentage'] == 100.0
        assert allocation['strategic_thinking']['hours_per_week'] == 2.0

    def test_calculate_current_allocation_multiple_blocks(self):
        """Test allocation with multiple blocks."""
        optimizer = CEOOptimizer()

        start = datetime.now()

        blocks = [
            TimeBlock(
                start_time=start,
                end_time=start + timedelta(hours=4),
                category='strategic_thinking',
                subcategory='planning',
                energy_cost=85.0,
                value_created=90.0,
                attendees=['CEO'],
                outcome_quality=88.0,
                notes=''
            ),
            TimeBlock(
                start_time=start + timedelta(hours=4),
                end_time=start + timedelta(hours=6),
                category='team_leadership',
                subcategory='1_on_1',
                energy_cost=60.0,
                value_created=80.0,
                attendees=['CEO', 'Engineer'],
                outcome_quality=85.0,
                notes=''
            )
        ]

        allocation = optimizer._calculate_current_allocation(blocks)

        # 4 hours strategic, 2 hours team = 66.7% / 33.3%
        assert abs(allocation['strategic_thinking']['percentage'] - 66.67) < 0.1
        assert abs(allocation['team_leadership']['percentage'] - 33.33) < 0.1


class TestAllocationStatus:
    """Test allocation status determination."""

    def test_get_allocation_status_under(self):
        """Test under-allocated status."""
        optimizer = CEOOptimizer()

        status = optimizer._get_allocation_status('strategic_thinking', 15)

        assert 'Under-allocated' in status
        assert '25%' in status  # Target

    def test_get_allocation_status_over(self):
        """Test over-allocated status."""
        optimizer = CEOOptimizer()

        status = optimizer._get_allocation_status('strategic_thinking', 35)

        assert 'Over-allocated' in status

    def test_get_allocation_status_optimal(self):
        """Test optimal status."""
        optimizer = CEOOptimizer()

        status = optimizer._get_allocation_status('strategic_thinking', 25)

        assert status == 'Optimal'

    def test_get_allocation_status_untracked(self):
        """Test status for untracked category."""
        optimizer = CEOOptimizer()

        status = optimizer._get_allocation_status('unknown_category', 50)

        assert status == 'Not tracked'


class TestAllocationGaps:
    """Test allocation gap identification."""

    def test_identify_allocation_gaps_empty(self):
        """Test gap identification with no blocks."""
        optimizer = CEOOptimizer()

        gaps = optimizer._identify_allocation_gaps([])

        # Should find gaps for all categories (they're all at 0%)
        assert len(gaps) > 0

    def test_identify_allocation_gaps_perfect(self):
        """Test gap identification with perfect allocation."""
        optimizer = CEOOptimizer()

        start = datetime.now()
        total_hours = 40  # 1 week

        blocks = []
        current_time = start

        for category, targets in optimizer.optimal_allocation.items():
            hours = targets['target'] * total_hours / 100
            blocks.append(
                TimeBlock(
                    start_time=current_time,
                    end_time=current_time + timedelta(hours=hours),
                    category=category,
                    subcategory='work',
                    energy_cost=50.0,
                    value_created=70.0,
                    attendees=['CEO'],
                    outcome_quality=75.0,
                    notes=''
                )
            )
            current_time += timedelta(hours=hours)

        gaps = optimizer._identify_allocation_gaps(blocks)

        # Should have no significant gaps (< 5%)
        assert all(abs(gap['gap']) <= 5 for gap in gaps)

    def test_identify_allocation_gaps_sorting(self):
        """Test gaps are sorted by magnitude."""
        optimizer = CEOOptimizer()

        start = datetime.now()

        # Only strategic thinking, everything else is missing
        blocks = [
            TimeBlock(
                start_time=start,
                end_time=start + timedelta(hours=40),
                category='strategic_thinking',
                subcategory='planning',
                energy_cost=85.0,
                value_created=90.0,
                attendees=['CEO'],
                outcome_quality=88.0,
                notes=''
            )
        ]

        gaps = optimizer._identify_allocation_gaps(blocks)

        # Should be sorted by absolute gap value
        if len(gaps) > 1:
            for i in range(len(gaps) - 1):
                assert abs(gaps[i]['gap']) >= abs(gaps[i+1]['gap'])


class TestGapRecommendations:
    """Test gap recommendation generation."""

    def test_get_gap_recommendation_strategic_positive(self):
        """Test recommendation for strategic thinking gap."""
        optimizer = CEOOptimizer()

        rec = optimizer._get_gap_recommendation('strategic_thinking', 10)

        assert 'Block' in rec or 'strategic' in rec.lower()

    def test_get_gap_recommendation_operational_negative(self):
        """Test recommendation for operational over-allocation."""
        optimizer = CEOOptimizer()

        rec = optimizer._get_gap_recommendation('operational_oversight', -10)

        assert 'Delegate' in rec or 'Reduce' in rec

    def test_get_gap_recommendation_positive_generic(self):
        """Test generic positive gap recommendation."""
        optimizer = CEOOptimizer()

        rec = optimizer._get_gap_recommendation('customer_interaction', 5)

        assert 'Prioritize' in rec or 'increase' in rec.lower()


class TestMeetingEfficiency:
    """Test meeting efficiency analysis."""

    def test_analyze_meeting_efficiency_no_meetings(self):
        """Test meeting analysis with no meetings."""
        optimizer = CEOOptimizer()

        start = datetime.now()
        blocks = [
            TimeBlock(
                start_time=start,
                end_time=start + timedelta(hours=2),
                category='strategic_thinking',
                subcategory='planning',  # Not a meeting
                energy_cost=85.0,
                value_created=90.0,
                attendees=['CEO'],
                outcome_quality=88.0,
                notes=''
            )
        ]

        efficiency = optimizer._analyze_meeting_efficiency(blocks)

        assert 'status' in efficiency
        assert 'No meetings' in efficiency['status']

    def test_analyze_meeting_efficiency_with_meetings(self):
        """Test meeting analysis with meetings."""
        optimizer = CEOOptimizer()

        start = datetime.now()
        blocks = [
            TimeBlock(
                start_time=start,
                end_time=start + timedelta(hours=1),
                category='team_leadership',
                subcategory='team_meeting',
                energy_cost=50.0,
                value_created=70.0,
                attendees=['CEO', 'Team'],
                outcome_quality=75.0,
                notes=''
            ),
            TimeBlock(
                start_time=start + timedelta(hours=2),
                end_time=start + timedelta(hours=3),
                category='operational_oversight',
                subcategory='executive_meeting',
                energy_cost=65.0,
                value_created=80.0,
                attendees=['CEO', 'Execs'],
                outcome_quality=85.0,
                notes=''
            )
        ]

        efficiency = optimizer._analyze_meeting_efficiency(blocks)

        assert 'total_meeting_hours' in efficiency
        assert efficiency['total_meeting_hours'] == 2.0
        assert efficiency['meeting_count'] == 2
        assert 'average_outcome_quality' in efficiency

    def test_analyze_meeting_efficiency_load_classification(self):
        """Test meeting load classification."""
        optimizer = CEOOptimizer()

        start = datetime.now()

        # Create 25 hours of meetings (heavy load)
        blocks = []
        for i in range(25):
            blocks.append(
                TimeBlock(
                    start_time=start + timedelta(hours=i*1.5),
                    end_time=start + timedelta(hours=i*1.5 + 1),
                    category='team_leadership',
                    subcategory='meeting',
                    energy_cost=50.0,
                    value_created=60.0,
                    attendees=['CEO'],
                    outcome_quality=70.0,
                    notes=''
                )
            )

        efficiency = optimizer._analyze_meeting_efficiency(blocks)

        assert efficiency['meeting_load'] == 'Heavy'


class TestReductionPotential:
    """Test meeting reduction potential calculation."""

    def test_calculate_reduction_potential_no_meetings(self):
        """Test reduction potential with no meetings."""
        optimizer = CEOOptimizer()

        reduction = optimizer._calculate_reduction_potential([])

        assert reduction['elimination_potential'] == 0
        assert reduction['delegation_potential'] == 0
        assert reduction['total_hours_saveable'] == 0

    def test_calculate_reduction_potential_low_quality(self):
        """Test elimination potential for low quality meetings."""
        optimizer = CEOOptimizer()

        start = datetime.now()
        meetings = [
            TimeBlock(
                start_time=start,
                end_time=start + timedelta(hours=2),
                category='operational_oversight',
                subcategory='meeting',
                energy_cost=50.0,
                value_created=30.0,
                attendees=['CEO', 'Team'],
                outcome_quality=40.0,  # Low quality
                notes=''
            )
        ]

        reduction = optimizer._calculate_reduction_potential(meetings)

        assert reduction['elimination_potential'] == 2.0

    def test_calculate_reduction_potential_large_meetings(self):
        """Test delegation potential for large meetings."""
        optimizer = CEOOptimizer()

        start = datetime.now()
        meetings = [
            TimeBlock(
                start_time=start,
                end_time=start + timedelta(hours=1),
                category='team_leadership',
                subcategory='meeting',
                energy_cost=50.0,
                value_created=70.0,
                attendees=['CEO', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6'],  # >5 attendees
                outcome_quality=75.0,
                notes=''
            )
        ]

        reduction = optimizer._calculate_reduction_potential(meetings)

        assert reduction['delegation_potential'] == 0.5  # 50% of 1 hour


class TestFocusTimeAnalysis:
    """Test focus time analysis."""

    def test_analyze_focus_time_no_focus(self):
        """Test focus analysis with no focus blocks."""
        optimizer = CEOOptimizer()

        start = datetime.now()
        blocks = [
            TimeBlock(
                start_time=start,
                end_time=start + timedelta(minutes=30),  # Too short
                category='strategic_thinking',
                subcategory='planning',
                energy_cost=85.0,
                value_created=60.0,
                attendees=['CEO'],
                outcome_quality=70.0,
                notes=''
            )
        ]

        focus = optimizer._analyze_focus_time(blocks)

        assert focus['total_focus_hours'] == 0
        assert focus['focus_block_count'] == 0

    def test_analyze_focus_time_with_focus(self):
        """Test focus analysis with focus blocks."""
        optimizer = CEOOptimizer()

        start = datetime.now()
        blocks = [
            TimeBlock(
                start_time=start,
                end_time=start + timedelta(hours=2),  # >= 1 hour
                category='strategic_thinking',
                subcategory='deep_work',
                energy_cost=85.0,
                value_created=95.0,
                attendees=['CEO'],
                outcome_quality=90.0,
                notes=''
            ),
            TimeBlock(
                start_time=start + timedelta(hours=3),
                end_time=start + timedelta(hours=4, minutes=30),  # 1.5 hours
                category='personal_development',
                subcategory='learning',
                energy_cost=40.0,
                value_created=85.0,
                attendees=['CEO'],
                outcome_quality=88.0,
                notes=''
            )
        ]

        focus = optimizer._analyze_focus_time(blocks)

        assert focus['total_focus_hours'] == 3.5
        assert focus['focus_block_count'] == 2
        assert focus['average_block_duration'] == 1.75


class TestFocusRecommendations:
    """Test focus time recommendations."""

    def test_get_focus_recommendation_critical(self):
        """Test recommendation for critical focus time."""
        optimizer = CEOOptimizer()

        rec = optimizer._get_focus_recommendation(3)

        assert 'CRITICAL' in rec or 'minimum' in rec.lower()

    def test_get_focus_recommendation_increase(self):
        """Test recommendation to increase focus time."""
        optimizer = CEOOptimizer()

        rec = optimizer._get_focus_recommendation(7)

        assert 'Increase' in rec

    def test_get_focus_recommendation_excellent(self):
        """Test recommendation for excellent focus time."""
        optimizer = CEOOptimizer()

        rec = optimizer._get_focus_recommendation(15)

        assert 'Excellent' in rec


class TestOptimizationOpportunities:
    """Test optimization opportunity identification."""

    def test_identify_optimization_opportunities_meeting_batching(self):
        """Test meeting batching opportunity identification."""
        optimizer = CEOOptimizer()

        start = datetime.now()
        blocks = []

        # Create scattered meetings across 5 days (2-3 per day)
        for day in range(5):
            for meeting in range(2):
                blocks.append(
                    TimeBlock(
                        start_time=start + timedelta(days=day, hours=meeting*2),
                        end_time=start + timedelta(days=day, hours=meeting*2 + 1),
                        category='team_leadership',
                        subcategory='meeting',
                        energy_cost=50.0,
                        value_created=60.0,
                        attendees=['CEO'],
                        outcome_quality=70.0,
                        notes=''
                    )
                )

        opportunities = optimizer._identify_optimization_opportunities(blocks)

        # Should suggest meeting batching
        assert any(opp['type'] == 'Meeting Batching' for opp in opportunities)

    def test_identify_optimization_opportunities_email_batching(self):
        """Test email batching opportunity identification."""
        optimizer = CEOOptimizer()

        start = datetime.now()
        blocks = []

        # Create many email processing blocks
        for i in range(8):
            blocks.append(
                TimeBlock(
                    start_time=start + timedelta(hours=i*2),
                    end_time=start + timedelta(hours=i*2 + 0.5),
                    category='operational_oversight',
                    subcategory='email_processing',
                    energy_cost=30.0,
                    value_created=40.0,
                    attendees=['CEO'],
                    outcome_quality=60.0,
                    notes=''
                )
            )

        opportunities = optimizer._identify_optimization_opportunities(blocks)

        # Should suggest email batching
        assert any(opp['type'] == 'Email Batching' for opp in opportunities)


class TestFullAnalysis:
    """Test complete time allocation analysis."""

    def test_analyze_time_allocation_comprehensive(self):
        """Test comprehensive time allocation analysis."""
        optimizer = CEOOptimizer()

        start = datetime.now()
        blocks = [
            TimeBlock(
                start_time=start,
                end_time=start + timedelta(hours=2),
                category='strategic_thinking',
                subcategory='strategy_session',
                energy_cost=85.0,
                value_created=90.0,
                attendees=['CEO', 'CSO'],
                outcome_quality=88.0,
                notes=''
            ),
            TimeBlock(
                start_time=start + timedelta(hours=3),
                end_time=start + timedelta(hours=4),
                category='team_leadership',
                subcategory='team_meeting',
                energy_cost=50.0,
                value_created=70.0,
                attendees=['CEO', 'Team'],
                outcome_quality=75.0,
                notes=''
            )
        ]

        analysis = optimizer.analyze_time_allocation(blocks)

        assert 'current_allocation' in analysis
        assert 'allocation_gaps' in analysis
        assert 'meeting_efficiency' in analysis
        assert 'focus_time_analysis' in analysis
        assert 'optimization_opportunities' in analysis


class TestMainFunction:
    """Test main optimization function."""

    def test_optimize_ceo_time_energy(self):
        """Test main optimization function."""
        report = optimize_ceo_time_energy()

        assert isinstance(report, str)
        assert 'CEO TIME & ENERGY OPTIMIZATION REPORT' in report
        assert 'TIME ALLOCATION ANALYSIS' in report
        assert 'FOCUS TIME' in report


class TestEdgeCases:
    """Test edge cases and error handling."""

    def test_zero_duration_block(self):
        """Test handling of zero duration time block."""
        optimizer = CEOOptimizer()

        start = datetime.now()
        blocks = [
            TimeBlock(
                start_time=start,
                end_time=start,  # Same time
                category='strategic_thinking',
                subcategory='planning',
                energy_cost=0.0,
                value_created=0.0,
                attendees=[],
                outcome_quality=0.0,
                notes=''
            )
        ]

        allocation = optimizer._calculate_current_allocation(blocks)

        # Should handle gracefully
        assert isinstance(allocation, dict)

    def test_very_long_block(self):
        """Test handling of very long time block."""
        optimizer = CEOOptimizer()

        start = datetime.now()
        blocks = [
            TimeBlock(
                start_time=start,
                end_time=start + timedelta(days=7),  # Full week
                category='strategic_thinking',
                subcategory='intensive_planning',
                energy_cost=85.0,
                value_created=90.0,
                attendees=['CEO'],
                outcome_quality=88.0,
                notes=''
            )
        ]

        allocation = optimizer._calculate_current_allocation(blocks)

        assert allocation['strategic_thinking']['percentage'] == 100.0

    def test_empty_attendees_list(self):
        """Test handling of empty attendees list."""
        optimizer = CEOOptimizer()

        start = datetime.now()
        blocks = [
            TimeBlock(
                start_time=start,
                end_time=start + timedelta(hours=1),
                category='personal_development',
                subcategory='reading',
                energy_cost=30.0,
                value_created=70.0,
                attendees=[],  # Empty
                outcome_quality=75.0,
                notes=''
            )
        ]

        analysis = optimizer.analyze_time_allocation(blocks)

        # Should handle gracefully
        assert 'current_allocation' in analysis

    def test_negative_outcome_quality(self):
        """Test handling of invalid outcome quality."""
        optimizer = CEOOptimizer()

        start = datetime.now()
        meetings = [
            TimeBlock(
                start_time=start,
                end_time=start + timedelta(hours=1),
                category='operational_oversight',
                subcategory='meeting',
                energy_cost=50.0,
                value_created=20.0,
                attendees=['CEO'],
                outcome_quality=-10.0,  # Invalid
                notes=''
            )
        ]

        # Should still calculate, even with invalid data
        efficiency = optimizer._analyze_meeting_efficiency(meetings)

        assert 'average_outcome_quality' in efficiency
