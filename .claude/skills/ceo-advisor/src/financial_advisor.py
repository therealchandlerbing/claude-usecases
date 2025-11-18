"""
Financial Advisor Module - Chief Financial Officer

Part of the CEO Advisor Team of Experts.
Provides financial health monitoring, resource allocation, and cash flow forecasting.

Author: Claude Usecases Repository
Version: 2.0.0
"""

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import List, Dict, Optional
import json


class FinancialHealth(Enum):
    """Overall financial health status"""
    EXCELLENT = "excellent"    # All metrics green
    HEALTHY = "healthy"        # Most metrics good
    CAUTIONARY = "cautionary"  # Some concerns
    WARNING = "warning"        # Multiple concerns
    CRITICAL = "critical"      # Immediate action needed


class TrendDirection(Enum):
    """Trend direction for metrics"""
    IMPROVING = "improving"
    STABLE = "stable"
    DECLINING = "declining"
    VOLATILE = "volatile"


class InvestmentPriority(Enum):
    """Investment priority levels"""
    ESSENTIAL = "essential"    # Must fund
    STRATEGIC = "strategic"    # Important for growth
    OPPORTUNISTIC = "opportunistic"  # Good if resources allow
    DEFER = "defer"           # Can wait


@dataclass
class FinancialMetric:
    """Represents a financial metric with context"""
    name: str
    current_value: float
    previous_value: float
    target_value: float
    unit: str  # currency, percentage, ratio, months
    trend: TrendDirection
    health: str  # green, yellow, red
    context: str


@dataclass
class CashFlowForecast:
    """Cash flow forecast for a period"""
    period: str
    beginning_cash: float
    operating_inflows: float
    operating_outflows: float
    investment_outflows: float
    financing_flows: float
    ending_cash: float
    runway_months: float
    notes: List[str]


@dataclass
class InvestmentOpportunity:
    """Investment opportunity for evaluation"""
    name: str
    category: str  # growth, efficiency, maintenance, strategic
    amount: float
    timing: str
    expected_return: float
    payback_months: int
    risk_level: str
    priority: InvestmentPriority
    dependencies: List[str]
    notes: str


@dataclass
class BudgetVariance:
    """Budget variance tracking"""
    category: str
    budgeted: float
    actual: float
    variance: float
    variance_pct: float
    explanation: str
    action_required: bool


class FinancialAdvisor:
    """
    Chief Financial Officer AI Expert

    Provides financial health monitoring, resource allocation optimization,
    cash flow forecasting, and investment evaluation for CEO decision-making.
    """

    def __init__(self, config: Optional[Dict] = None):
        self.config = config or self._default_config()

        # Financial thresholds
        self.thresholds = {
            'runway_warning_months': 9,
            'runway_critical_months': 6,
            'burn_variance_warning': 0.10,
            'burn_variance_critical': 0.20,
            'gross_margin_warning': 0.60,
            'gross_margin_critical': 0.50,
            'ltv_cac_warning': 2.0,
            'ltv_cac_critical': 1.5
        }

    def _default_config(self) -> Dict:
        return {
            'currency': 'USD',
            'fiscal_year_start': 1,  # January
            'forecast_months': 12,
            'scenario_count': 3
        }

    def run_financial_analysis(self, financial_data: Optional[Dict] = None) -> Dict:
        """
        Run comprehensive financial analysis.

        Returns analysis including health check, cash flow forecast,
        resource allocation, and recommendations.
        """
        financial_data = financial_data or self._get_sample_financial_data()

        analysis = {
            'timestamp': datetime.now().isoformat(),
            'overall_health': self._assess_overall_health(financial_data),
            'key_metrics': self._analyze_key_metrics(financial_data),
            'cash_flow_forecast': self._forecast_cash_flow(financial_data),
            'budget_performance': self._analyze_budget_performance(financial_data),
            'resource_allocation': self._optimize_resource_allocation(financial_data),
            'investment_evaluation': self._evaluate_investments(financial_data),
            'risk_assessment': self._assess_financial_risks(financial_data),
            'recommendations': self._generate_recommendations(financial_data)
        }

        return analysis

    def _assess_overall_health(self, data: Dict) -> Dict:
        """Assess overall financial health"""
        issues = []
        warnings = []

        # Check runway
        runway = data.get('runway_months', 12)
        if runway < self.thresholds['runway_critical_months']:
            issues.append(f"Critical: Runway at {runway} months")
        elif runway < self.thresholds['runway_warning_months']:
            warnings.append(f"Runway at {runway} months")

        # Check burn rate
        burn_variance = abs(data.get('burn_variance', 0))
        if burn_variance > self.thresholds['burn_variance_critical']:
            issues.append(f"Burn rate variance at {burn_variance:.0%}")
        elif burn_variance > self.thresholds['burn_variance_warning']:
            warnings.append(f"Burn rate variance at {burn_variance:.0%}")

        # Check gross margin
        gross_margin = data.get('gross_margin', 0.70)
        if gross_margin < self.thresholds['gross_margin_critical']:
            issues.append(f"Gross margin at {gross_margin:.0%}")
        elif gross_margin < self.thresholds['gross_margin_warning']:
            warnings.append(f"Gross margin at {gross_margin:.0%}")

        # Determine overall status
        if issues:
            status = FinancialHealth.CRITICAL if len(issues) > 1 else FinancialHealth.WARNING
        elif warnings:
            status = FinancialHealth.CAUTIONARY if len(warnings) > 1 else FinancialHealth.HEALTHY
        else:
            status = FinancialHealth.EXCELLENT

        return {
            'status': status.value,
            'issues': issues,
            'warnings': warnings,
            'summary': self._generate_health_summary(status, issues, warnings)
        }

    def _analyze_key_metrics(self, data: Dict) -> List[Dict]:
        """Analyze key financial metrics"""
        metrics = [
            FinancialMetric(
                name='Monthly Recurring Revenue',
                current_value=data.get('mrr', 850000),
                previous_value=data.get('mrr_previous', 820000),
                target_value=data.get('mrr_target', 900000),
                unit='currency',
                trend=self._calculate_trend(850000, 820000),
                health='green' if data.get('mrr', 0) >= data.get('mrr_target', 0) * 0.9 else 'yellow',
                context='3.7% MoM growth, on track for quarterly target'
            ),
            FinancialMetric(
                name='Cash Position',
                current_value=data.get('cash', 5900000),
                previous_value=data.get('cash_previous', 6300000),
                target_value=data.get('cash_target', 5000000),
                unit='currency',
                trend=TrendDirection.DECLINING,
                health='green',
                context=f"{data.get('runway_months', 14)} months runway'
            ),
            FinancialMetric(
                name='Gross Margin',
                current_value=data.get('gross_margin', 0.72),
                previous_value=data.get('gross_margin_previous', 0.71),
                target_value=data.get('gross_margin_target', 0.75),
                unit='percentage',
                trend=TrendDirection.IMPROVING,
                health='green',
                context='Improved 1pp from infrastructure optimization'
            ),
            FinancialMetric(
                name='Burn Rate',
                current_value=data.get('burn_rate', 420000),
                previous_value=data.get('burn_rate_previous', 400000),
                target_value=data.get('burn_rate_target', 400000),
                unit='currency',
                trend=TrendDirection.STABLE,
                health='yellow' if data.get('burn_rate', 0) > data.get('burn_rate_target', 0) else 'green',
                context='5% above target due to accelerated hiring'
            ),
            FinancialMetric(
                name='LTV/CAC Ratio',
                current_value=data.get('ltv_cac', 3.2),
                previous_value=data.get('ltv_cac_previous', 3.0),
                target_value=data.get('ltv_cac_target', 3.5),
                unit='ratio',
                trend=TrendDirection.IMPROVING,
                health='green',
                context='Healthy unit economics, improved from sales efficiency'
            ),
            FinancialMetric(
                name='Net Revenue Retention',
                current_value=data.get('nrr', 1.15),
                previous_value=data.get('nrr_previous', 1.12),
                target_value=data.get('nrr_target', 1.20),
                unit='percentage',
                trend=TrendDirection.IMPROVING,
                health='green',
                context='Strong expansion, low churn'
            )
        ]

        return [m.__dict__ for m in metrics]

    def _forecast_cash_flow(self, data: Dict) -> Dict:
        """Generate cash flow forecast"""
        current_cash = data.get('cash', 5900000)
        monthly_burn = data.get('burn_rate', 420000)
        revenue = data.get('mrr', 850000)
        revenue_growth = 0.03  # 3% monthly

        forecasts = []
        cash = current_cash

        for i in range(1, 7):  # 6 month forecast
            period_revenue = revenue * (1 + revenue_growth) ** i
            operating_in = period_revenue * 0.95  # 95% collection
            operating_out = monthly_burn * (1 + 0.02 * i)  # 2% monthly increase
            investment = 50000 if i % 3 == 0 else 0

            ending = cash + operating_in - operating_out - investment

            forecast = CashFlowForecast(
                period=f"Month {i}",
                beginning_cash=cash,
                operating_inflows=operating_in,
                operating_outflows=operating_out,
                investment_outflows=investment,
                financing_flows=0,
                ending_cash=ending,
                runway_months=ending / operating_out,
                notes=[]
            )

            if forecast.runway_months < 6:
                forecast.notes.append("⚠️ Runway below 6 months")

            forecasts.append(forecast.__dict__)
            cash = ending

        return {
            'forecasts': forecasts,
            'summary': {
                'starting_cash': current_cash,
                'ending_cash': cash,
                'net_change': cash - current_cash,
                'average_burn': monthly_burn,
                'final_runway_months': cash / monthly_burn
            },
            'scenarios': self._generate_cash_scenarios(data)
        }

    def _generate_cash_scenarios(self, data: Dict) -> List[Dict]:
        """Generate cash flow scenarios"""
        return [
            {
                'scenario': 'Base Case',
                'probability': 50,
                'assumptions': [
                    'Revenue grows 3% monthly',
                    'Burn increases 2% monthly',
                    'No fundraising'
                ],
                'runway_months': 14,
                'ending_cash': 4800000
            },
            {
                'scenario': 'Accelerated Growth',
                'probability': 25,
                'assumptions': [
                    'Revenue grows 5% monthly',
                    'Burn increases 3% monthly',
                    'Land major enterprise deal'
                ],
                'runway_months': 16,
                'ending_cash': 5500000
            },
            {
                'scenario': 'Conservative',
                'probability': 25,
                'assumptions': [
                    'Revenue grows 2% monthly',
                    'Burn flat',
                    'No major deals'
                ],
                'runway_months': 13,
                'ending_cash': 4200000
            }
        ]

    def _analyze_budget_performance(self, data: Dict) -> Dict:
        """Analyze budget vs actual performance"""
        variances = [
            BudgetVariance(
                category='Sales & Marketing',
                budgeted=250000,
                actual=265000,
                variance=-15000,
                variance_pct=-0.06,
                explanation='Accelerated ad spend for product launch',
                action_required=False
            ),
            BudgetVariance(
                category='Engineering',
                budgeted=180000,
                actual=175000,
                variance=5000,
                variance_pct=0.03,
                explanation='Delayed hire start date',
                action_required=False
            ),
            BudgetVariance(
                category='General & Admin',
                budgeted=60000,
                actual=58000,
                variance=2000,
                variance_pct=0.03,
                explanation='Lower than expected travel',
                action_required=False
            ),
            BudgetVariance(
                category='Customer Success',
                budgeted=80000,
                actual=82000,
                variance=-2000,
                variance_pct=-0.025,
                explanation='Additional tooling investment',
                action_required=False
            )
        ]

        total_budget = sum(v.budgeted for v in variances)
        total_actual = sum(v.actual for v in variances)

        return {
            'variances': [v.__dict__ for v in variances],
            'summary': {
                'total_budgeted': total_budget,
                'total_actual': total_actual,
                'net_variance': total_budget - total_actual,
                'variance_pct': (total_budget - total_actual) / total_budget
            },
            'actions_needed': [v.category for v in variances if v.action_required]
        }

    def _optimize_resource_allocation(self, data: Dict) -> Dict:
        """Optimize resource allocation"""
        return {
            'current_allocation': {
                'sales_marketing': {'amount': 250000, 'pct': 0.45},
                'engineering': {'amount': 180000, 'pct': 0.32},
                'customer_success': {'amount': 80000, 'pct': 0.14},
                'general_admin': {'amount': 50000, 'pct': 0.09}
            },
            'recommended_allocation': {
                'sales_marketing': {'amount': 240000, 'pct': 0.43, 'change': -0.02},
                'engineering': {'amount': 190000, 'pct': 0.34, 'change': 0.02},
                'customer_success': {'amount': 85000, 'pct': 0.15, 'change': 0.01},
                'general_admin': {'amount': 45000, 'pct': 0.08, 'change': -0.01}
            },
            'rationale': [
                'Increase engineering to accelerate AI roadmap',
                'Increase customer success to improve retention',
                'Optimize S&M spend efficiency',
                'Reduce G&A through automation'
            ],
            'expected_impact': {
                'revenue_growth': '+5% incremental',
                'retention': '+3% NRR',
                'efficiency': '10% cost reduction in G&A'
            }
        }

    def _evaluate_investments(self, data: Dict) -> List[Dict]:
        """Evaluate investment opportunities"""
        investments = [
            InvestmentOpportunity(
                name='AI Platform Development',
                category='strategic',
                amount=500000,
                timing='Q1-Q2 2025',
                expected_return=2.5,
                payback_months=18,
                risk_level='medium',
                priority=InvestmentPriority.STRATEGIC,
                dependencies=['AI talent hired', 'Data pipeline complete'],
                notes='Critical for competitive positioning'
            ),
            InvestmentOpportunity(
                name='Sales Automation',
                category='efficiency',
                amount=150000,
                timing='Q1 2025',
                expected_return=3.0,
                payback_months=12,
                risk_level='low',
                priority=InvestmentPriority.ESSENTIAL,
                dependencies=['CRM migration complete'],
                notes='Quick win with clear ROI'
            ),
            InvestmentOpportunity(
                name='European Expansion',
                category='growth',
                amount=750000,
                timing='Q2-Q3 2025',
                expected_return=2.0,
                payback_months=24,
                risk_level='high',
                priority=InvestmentPriority.OPPORTUNISTIC,
                dependencies=['US growth targets met', 'Localization complete'],
                notes='Significant opportunity but requires proven US execution'
            ),
            InvestmentOpportunity(
                name='Office Expansion',
                category='maintenance',
                amount=200000,
                timing='Q3 2025',
                expected_return=1.0,
                payback_months=36,
                risk_level='low',
                priority=InvestmentPriority.DEFER,
                dependencies=['Team growth on track'],
                notes='Can defer with continued remote-first approach'
            )
        ]

        # Sort by priority
        priority_order = {
            InvestmentPriority.ESSENTIAL: 0,
            InvestmentPriority.STRATEGIC: 1,
            InvestmentPriority.OPPORTUNISTIC: 2,
            InvestmentPriority.DEFER: 3
        }

        investments.sort(key=lambda x: priority_order[x.priority])

        return [{
            **i.__dict__,
            'priority': i.priority.value
        } for i in investments]

    def _assess_financial_risks(self, data: Dict) -> Dict:
        """Assess financial risks"""
        return {
            'top_risks': [
                {
                    'risk': 'Customer concentration',
                    'description': 'Top 3 customers = 35% of revenue',
                    'probability': 'medium',
                    'impact': 'high',
                    'mitigation': 'Diversify customer base, multi-thread relationships'
                },
                {
                    'risk': 'Delayed fundraise',
                    'description': 'Market conditions may extend timeline',
                    'probability': 'medium',
                    'impact': 'high',
                    'mitigation': 'Maintain optionality with bridge terms, extend runway'
                },
                {
                    'risk': 'Hiring cost inflation',
                    'description': 'AI talent premium may exceed budget',
                    'probability': 'high',
                    'impact': 'medium',
                    'mitigation': 'Build training program, consider remote talent'
                }
            ],
            'sensitivity_analysis': {
                'revenue_decrease_10pct': {
                    'runway_impact': '-2 months',
                    'action': 'Reduce discretionary spend'
                },
                'burn_increase_20pct': {
                    'runway_impact': '-3 months',
                    'action': 'Hiring freeze, vendor renegotiation'
                },
                'customer_churn_5pct': {
                    'runway_impact': '-1 month',
                    'action': 'Customer success intervention'
                }
            }
        }

    def _generate_recommendations(self, data: Dict) -> Dict:
        """Generate financial recommendations"""
        return {
            'immediate_actions': [
                {
                    'action': 'Approve sales automation investment',
                    'rationale': 'Quick payback, clear ROI, low risk',
                    'amount': 150000,
                    'timeline': 'This week'
                },
                {
                    'action': 'Review customer concentration risk',
                    'rationale': 'Top 3 customers represent 35% of revenue',
                    'timeline': 'This month'
                }
            ],
            'short_term': [
                {
                    'action': 'Finalize AI investment decision',
                    'rationale': 'Critical for competitive positioning',
                    'amount': 500000,
                    'timeline': 'Q1 2025'
                },
                {
                    'action': 'Begin fundraise preparation',
                    'rationale': 'Lead time for process even if not needed',
                    'timeline': 'Q1 2025'
                }
            ],
            'monitoring': [
                'Burn rate vs target (weekly)',
                'Cash collection days (weekly)',
                'Pipeline coverage ratio (weekly)',
                'Customer health scores (monthly)'
            ]
        }

    def _generate_health_summary(self, status: FinancialHealth, issues: List, warnings: List) -> str:
        """Generate health summary text"""
        if status == FinancialHealth.EXCELLENT:
            return "All financial metrics healthy. Continue monitoring key indicators."
        elif status == FinancialHealth.HEALTHY:
            return f"Overall healthy with {len(warnings)} item(s) to monitor."
        elif status == FinancialHealth.CAUTIONARY:
            return f"Caution advised: {len(warnings)} warning(s) require attention."
        elif status == FinancialHealth.WARNING:
            return f"Warning: {len(issues)} issue(s) need immediate review."
        else:
            return f"Critical: {len(issues)} urgent issue(s) require immediate action."

    def _calculate_trend(self, current: float, previous: float) -> TrendDirection:
        """Calculate trend direction"""
        if previous == 0:
            return TrendDirection.STABLE

        change = (current - previous) / previous

        if change > 0.05:
            return TrendDirection.IMPROVING
        elif change < -0.05:
            return TrendDirection.DECLINING
        else:
            return TrendDirection.STABLE

    def _get_sample_financial_data(self) -> Dict:
        """Get sample financial data for demonstration"""
        return {
            'mrr': 850000,
            'mrr_previous': 820000,
            'mrr_target': 900000,
            'cash': 5900000,
            'cash_previous': 6300000,
            'cash_target': 5000000,
            'burn_rate': 420000,
            'burn_rate_previous': 400000,
            'burn_rate_target': 400000,
            'burn_variance': 0.05,
            'gross_margin': 0.72,
            'gross_margin_previous': 0.71,
            'gross_margin_target': 0.75,
            'ltv_cac': 3.2,
            'ltv_cac_previous': 3.0,
            'ltv_cac_target': 3.5,
            'nrr': 1.15,
            'nrr_previous': 1.12,
            'nrr_target': 1.20,
            'runway_months': 14
        }


def run_financial_analysis() -> Dict:
    """
    Run financial analysis.

    Returns comprehensive financial analysis.
    """
    advisor = FinancialAdvisor()
    return advisor.run_financial_analysis()


if __name__ == "__main__":
    print("=" * 60)
    print("CHIEF FINANCIAL OFFICER - FINANCIAL ANALYSIS")
    print("=" * 60)

    analysis = run_financial_analysis()

    print("\n💰 OVERALL FINANCIAL HEALTH")
    print("-" * 40)
    health = analysis['overall_health']
    status_emoji = {
        'excellent': '🟢',
        'healthy': '🔵',
        'cautionary': '🟡',
        'warning': '🟠',
        'critical': '🔴'
    }
    print(f"\nStatus: {status_emoji.get(health['status'], '⚪')} {health['status'].upper()}")
    print(f"Summary: {health['summary']}")

    if health['issues']:
        print("\nIssues:")
        for issue in health['issues']:
            print(f"  🚨 {issue}")

    if health['warnings']:
        print("\nWarnings:")
        for warning in health['warnings']:
            print(f"  ⚠️ {warning}")

    print("\n\n📊 KEY METRICS")
    print("-" * 40)
    for metric in analysis['key_metrics'][:4]:
        health_emoji = {'green': '🟢', 'yellow': '🟡', 'red': '🔴'}
        trend_emoji = {
            'improving': '↗️',
            'stable': '→',
            'declining': '↘️',
            'volatile': '↔️'
        }
        print(f"\n{metric['name']}")
        if metric['unit'] == 'currency':
            print(f"  ${metric['current_value']:,.0f} {health_emoji.get(metric['health'], '⚪')}")
        elif metric['unit'] == 'percentage':
            print(f"  {metric['current_value']:.0%} {health_emoji.get(metric['health'], '⚪')}")
        else:
            print(f"  {metric['current_value']:.1f}x {health_emoji.get(metric['health'], '⚪')}")
        print(f"  {trend_emoji.get(metric['trend'], '→')} {metric['context']}")

    print("\n\n💵 CASH FLOW FORECAST")
    print("-" * 40)
    cf = analysis['cash_flow_forecast']['summary']
    print(f"\nStarting Cash: ${cf['starting_cash']:,.0f}")
    print(f"Ending Cash (6 mo): ${cf['ending_cash']:,.0f}")
    print(f"Runway: {cf['final_runway_months']:.1f} months")

    print("\n\n🎯 INVESTMENT PRIORITIES")
    print("-" * 40)
    for inv in analysis['investment_evaluation'][:3]:
        priority_emoji = {
            'essential': '🔴',
            'strategic': '🟠',
            'opportunistic': '🟡',
            'defer': '⚪'
        }
        print(f"\n{inv['name']}")
        print(f"  {priority_emoji.get(inv['priority'], '⚪')} {inv['priority'].upper()}")
        print(f"  Amount: ${inv['amount']:,.0f}")
        print(f"  ROI: {inv['expected_return']}x in {inv['payback_months']} months")

    print("\n\n✅ RECOMMENDATIONS")
    print("-" * 40)
    for action in analysis['recommendations']['immediate_actions']:
        print(f"\n• {action['action']}")
        print(f"  {action['rationale']}")
        if 'amount' in action:
            print(f"  Amount: ${action['amount']:,.0f}")

    print("\n" + "=" * 60)
    print("Financial analysis complete")
    print("=" * 60)
