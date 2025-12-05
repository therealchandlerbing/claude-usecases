"""
CEO Advisor - Executive Intelligence Platform

A comprehensive AI-powered advisory board system that transforms CEO decision-making
from reactive management to predictive excellence.

Main Components:
    - CEOAdvisorOrchestrator: Main integration hub coordinating all advisors
    - ExecutiveIntelligenceSystem: Real-time intelligence aggregation and signal detection
    - StakeholderAnalytics: Relationship tracking and sentiment analysis
    - CEOOptimizer: Time and energy optimization
    - StrategyAdvisor: Strategic planning and analysis
    - FinancialAdvisor: Financial scenario modeling and oversight

Example:
    >>> from ceo_advisor import CEOAdvisorOrchestrator
    >>> orchestrator = CEOAdvisorOrchestrator()
    >>> brief = orchestrator.generate_daily_brief()
"""

from .ceo_advisor_orchestrator import CEOAdvisorOrchestrator, main
from .executive_intelligence_system import (
    ExecutiveIntelligenceSystem,
    SignalPriority,
    Signal,
    generate_intelligence_report,
)
from .stakeholder_analytics import (
    StakeholderAnalytics,
    Stakeholder,
    RelationshipStatus,
    CommunicationStyle,
    analyze_stakeholder_portfolio,
)
from .ceo_optimizer import (
    CEOOptimizer,
    TimeBlock,
    EnergyLevel,
    optimize_ceo_time_energy,
)
from .strategy_advisor import (
    StrategyAdvisor,
    StrategicPriority,
    RiskLevel,
    TimeHorizon,
    StrategicOption,
    Scenario,
    CompetitiveIntelligence,
    run_strategic_analysis,
)
from .financial_advisor import (
    FinancialAdvisor,
    FinancialHealth,
    TrendDirection,
    InvestmentPriority,
    FinancialMetric,
    CashFlowForecast,
    InvestmentOpportunity,
    BudgetVariance,
    run_financial_analysis,
)

__all__ = [
    # Main orchestrator
    "CEOAdvisorOrchestrator",
    "main",
    # Executive Intelligence
    "ExecutiveIntelligenceSystem",
    "SignalPriority",
    "Signal",
    "generate_intelligence_report",
    # Stakeholder Analytics
    "StakeholderAnalytics",
    "Stakeholder",
    "RelationshipStatus",
    "CommunicationStyle",
    "analyze_stakeholder_portfolio",
    # CEO Optimizer
    "CEOOptimizer",
    "TimeBlock",
    "EnergyLevel",
    "optimize_ceo_time_energy",
    # Strategy Advisor
    "StrategyAdvisor",
    "StrategicPriority",
    "RiskLevel",
    "TimeHorizon",
    "StrategicOption",
    "Scenario",
    "CompetitiveIntelligence",
    "run_strategic_analysis",
    # Financial Advisor
    "FinancialAdvisor",
    "FinancialHealth",
    "TrendDirection",
    "InvestmentPriority",
    "FinancialMetric",
    "CashFlowForecast",
    "InvestmentOpportunity",
    "BudgetVariance",
    "run_financial_analysis",
]

__version__ = "2.0.0"
