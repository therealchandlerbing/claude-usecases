#!/usr/bin/env python3
"""
CEO Time & Energy Optimization Engine - Personal effectiveness maximizer

Analyzes CEO time allocation, energy patterns, and decision quality to
optimize performance.
"""

import json
from typing import Dict, List
from datetime import datetime, timedelta, time
from dataclasses import dataclass
from enum import Enum


class EnergyLevel(Enum):
    PEAK = "🟢"
    HIGH = "🔵"
    MODERATE = "🟡"
    LOW = "🟠"
    DEPLETED = "🔴"


@dataclass
class TimeBlock:
    start_time: datetime
    end_time: datetime
    category: str
    subcategory: str
    energy_cost: float
    value_created: float
    attendees: List[str]
    outcome_quality: float
    notes: str


class CEOOptimizer:
    def __init__(self):
        self.optimal_allocation = {
            'strategic_thinking': {'target': 25, 'min': 20, 'max': 30},
            'team_leadership': {'target': 20, 'min': 15, 'max': 25},
            'external_engagement': {'target': 20, 'min': 15, 'max': 25},
            'operational_oversight': {'target': 15, 'min': 10, 'max': 20},
            'customer_interaction': {'target': 10, 'min': 5, 'max': 15},
            'personal_development': {'target': 10, 'min': 5, 'max': 15}
        }

        self.energy_costs = {
            'board_meeting': 90,
            'strategy_session': 85,
            'conflict_resolution': 80,
            'investor_pitch': 75,
            'all_hands': 70,
            'executive_meeting': 65,
            '1_on_1': 60,
            'customer_meeting': 55,
            'team_meeting': 50,
            'email_processing': 30,
            'planning': 40
        }

    def analyze_time_allocation(self, calendar_data: List[TimeBlock]) -> Dict:
        """Analyze how time is being allocated vs optimal"""
        analysis = {
            'current_allocation': self._calculate_current_allocation(calendar_data),
            'allocation_gaps': self._identify_allocation_gaps(calendar_data),
            'meeting_efficiency': self._analyze_meeting_efficiency(calendar_data),
            'focus_time_analysis': self._analyze_focus_time(calendar_data),
            'optimization_opportunities': self._identify_optimization_opportunities(calendar_data)
        }

        return analysis

    def _calculate_current_allocation(self, calendar_data: List[TimeBlock]) -> Dict:
        """Calculate current time allocation by category"""
        total_minutes = 0
        category_minutes = {}

        for block in calendar_data:
            duration = (block.end_time - block.start_time).total_seconds() / 60
            # Skip blocks with zero duration
            if duration == 0:
                continue
            total_minutes += duration

            if block.category not in category_minutes:
                category_minutes[block.category] = 0
            category_minutes[block.category] += duration

        allocation = {}
        for category, minutes in category_minutes.items():
            allocation[category] = {
                'percentage': (minutes / total_minutes * 100) if total_minutes > 0 else 0,
                'hours_per_week': minutes / 60,
                'status': self._get_allocation_status(category, (minutes / total_minutes * 100) if total_minutes > 0 else 0)
            }

        return allocation

    def _get_allocation_status(self, category: str, percentage: float) -> str:
        """Determine if allocation is optimal"""
        if category in self.optimal_allocation:
            target = self.optimal_allocation[category]
            if percentage < target['min']:
                return f"Under-allocated (target: {target['target']}%)"
            elif percentage > target['max']:
                return f"Over-allocated (target: {target['target']}%)"
            else:
                return "Optimal"
        return "Not tracked"

    def _identify_allocation_gaps(self, calendar_data: List[TimeBlock]) -> List[Dict]:
        """Identify gaps between current and optimal allocation"""
        current = self._calculate_current_allocation(calendar_data)
        gaps = []

        for category, targets in self.optimal_allocation.items():
            current_pct = current.get(category, {}).get('percentage', 0)
            gap = targets['target'] - current_pct

            if abs(gap) > 5:
                gaps.append({
                    'category': category,
                    'current': current_pct,
                    'target': targets['target'],
                    'gap': gap,
                    'weekly_hours_needed': gap * 40 / 100,
                    'recommendation': self._get_gap_recommendation(category, gap)
                })

        gaps.sort(key=lambda x: abs(x['gap']), reverse=True)
        return gaps

    def _get_gap_recommendation(self, category: str, gap: float) -> str:
        """Get recommendation for closing allocation gap"""
        if gap > 0:
            if category == 'strategic_thinking':
                return "Block 2-3 hour sessions for deep strategic work"
            elif category == 'team_leadership':
                return "Increase 1-on-1 frequency and team interaction"
            else:
                return "Prioritize this category in schedule"
        else:
            if category == 'operational_oversight':
                return "Delegate more operational decisions"
            else:
                return "Reduce time in this category"

    def _analyze_meeting_efficiency(self, calendar_data: List[TimeBlock]) -> Dict:
        """Analyze meeting efficiency metrics"""
        meetings = [b for b in calendar_data if 'meeting' in b.subcategory.lower()]

        if not meetings:
            return {'status': 'No meetings found'}

        total_meeting_time = sum((m.end_time - m.start_time).total_seconds() / 3600 for m in meetings)
        avg_outcome_quality = sum(m.outcome_quality for m in meetings) / len(meetings)

        return {
            'total_meeting_hours': total_meeting_time,
            'meeting_count': len(meetings),
            'average_duration': total_meeting_time / len(meetings),
            'average_outcome_quality': avg_outcome_quality,
            'meeting_load': 'Heavy' if total_meeting_time > 20 else 'Moderate',
            'meeting_reduction_potential': self._calculate_reduction_potential(meetings)
        }

    def _calculate_reduction_potential(self, meetings: List[TimeBlock]) -> Dict:
        """Calculate meeting reduction potential"""
        reduction = {
            'elimination_potential': 0,
            'delegation_potential': 0,
            'total_hours_saveable': 0
        }

        for meeting in meetings:
            duration = (meeting.end_time - meeting.start_time).total_seconds() / 3600

            if meeting.outcome_quality < 50:
                reduction['elimination_potential'] += duration

            if len(meeting.attendees) > 5:
                reduction['delegation_potential'] += duration * 0.5

        reduction['total_hours_saveable'] = (
            reduction['elimination_potential'] +
            reduction['delegation_potential']
        )

        return reduction

    def _analyze_focus_time(self, calendar_data: List[TimeBlock]) -> Dict:
        """Analyze deep work and focus time"""
        focus_blocks = []

        for block in calendar_data:
            duration = (block.end_time - block.start_time).total_seconds() / 3600

            if block.category in ['strategic_thinking', 'personal_development'] and duration >= 1:
                focus_blocks.append({
                    'time': block.start_time,
                    'duration': duration,
                    'quality': block.outcome_quality
                })

        total_focus_time = sum(b['duration'] for b in focus_blocks)

        return {
            'total_focus_hours': total_focus_time,
            'focus_block_count': len(focus_blocks),
            'average_block_duration': total_focus_time / len(focus_blocks) if focus_blocks else 0,
            'focus_time_percentage': (total_focus_time / 40) * 100,
            'recommendation': self._get_focus_recommendation(total_focus_time)
        }

    def _get_focus_recommendation(self, total_focus_hours: float) -> str:
        """Get focus time recommendation"""
        if total_focus_hours < 5:
            return "CRITICAL: Need minimum 2-hour daily focus blocks"
        elif total_focus_hours < 10:
            return "Increase focus time to 2-3 hours daily"
        else:
            return "Excellent focus time allocation"

    def _identify_optimization_opportunities(self, calendar_data: List[TimeBlock]) -> List[Dict]:
        """Identify specific optimization opportunities"""
        opportunities = []

        # Meeting batching
        meetings_per_day = {}
        for block in calendar_data:
            if 'meeting' in block.subcategory.lower():
                day = block.start_time.date()
                if day not in meetings_per_day:
                    meetings_per_day[day] = 0
                meetings_per_day[day] += 1

        scattered_days = sum(1 for count in meetings_per_day.values() if 1 < count < 4)
        if scattered_days > 2:
            opportunities.append({
                'type': 'Meeting Batching',
                'impact': 'High',
                'time_saved': '3-4 hours/week',
                'recommendation': 'Batch meetings into 2-3 days per week'
            })

        # Email batching
        email_blocks = [b for b in calendar_data if 'email' in b.subcategory.lower()]
        if len(email_blocks) > 5:
            opportunities.append({
                'type': 'Email Batching',
                'impact': 'Medium',
                'time_saved': '1-2 hours/week',
                'recommendation': 'Process email in 2-3 dedicated blocks daily'
            })

        return opportunities


def optimize_ceo_time_energy() -> str:
    """Main function to optimize CEO time and energy"""

    # Generate sample data
    now = datetime.now()
    calendar_data = [
        TimeBlock(
            start_time=now.replace(hour=8, minute=0),
            end_time=now.replace(hour=9, minute=30),
            category='strategic_thinking',
            subcategory='strategy_session',
            energy_cost=85,
            value_created=90,
            attendees=['CEO', 'CSO'],
            outcome_quality=88,
            notes='Quarterly strategy review'
        ),
        TimeBlock(
            start_time=now.replace(hour=11, minute=0),
            end_time=now.replace(hour=12, minute=0),
            category='operational_oversight',
            subcategory='routine_meeting',
            energy_cost=50,
            value_created=30,
            attendees=['CEO', 'Ops Team'],
            outcome_quality=45,
            notes='Weekly ops review'
        )
    ]

    optimizer = CEOOptimizer()
    time_analysis = optimizer.analyze_time_allocation(calendar_data)

    # Format output
    output = [
        "=" * 50,
        "CEO TIME & ENERGY OPTIMIZATION REPORT",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "=" * 50,
        "",
        "TIME ALLOCATION ANALYSIS:",
        ""
    ]

    for category, data in time_analysis['current_allocation'].items():
        output.append(f"  {category}: {data['percentage']:.1f}% ({data['status']})")

    if time_analysis['allocation_gaps']:
        output.append("\nCRITICAL GAPS:")
        for gap in time_analysis['allocation_gaps'][:3]:
            output.append(f"  {gap['category']}: {gap['gap']:+.1f}% gap")
            output.append(f"    → {gap['recommendation']}")

    meeting_data = time_analysis['meeting_efficiency']
    if isinstance(meeting_data, dict) and 'total_meeting_hours' in meeting_data:
        output.extend([
            "",
            "MEETING EFFICIENCY:",
            f"  Total Hours: {meeting_data.get('total_meeting_hours', 0):.1f}",
            f"  Meeting Load: {meeting_data.get('meeting_load', 'Unknown')}"
        ])

    focus = time_analysis['focus_time_analysis']
    output.extend([
        "",
        "FOCUS TIME:",
        f"  Total: {focus['total_focus_hours']:.1f} hours",
        f"  {focus['recommendation']}"
    ])

    return '\n'.join(output)


if __name__ == "__main__":
    print(optimize_ceo_time_energy())
