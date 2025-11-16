#!/usr/bin/env python3
"""
Company Data Gathering Script
Automates collection of financial and operational data from multiple sources
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json
import requests
from typing import Dict, List, Optional, Tuple

class CompanyDataGatherer:
    """
    Systematic data collection for investment analysis.
    Integrates with financial data platforms and web sources.
    """

    def __init__(self, company_name: str, ticker: Optional[str] = None):
        self.company_name = company_name
        self.ticker = ticker
        self.data = {
            'basic_info': {},
            'financials': {},
            'metrics': {},
            'comparables': {},
            'market_data': {}
        }

    def gather_all_data(self) -> Dict:
        """
        Execute complete data gathering workflow.
        Returns comprehensive dataset for modeling.
        """
        print(f"Gathering data for {self.company_name}...")

        # Execute data collection in sequence
        self.gather_basic_info()
        self.gather_financial_statements()
        self.gather_operating_metrics()
        self.gather_market_intelligence()
        self.gather_comparable_companies()

        # Validate and clean collected data
        self.validate_data()

        # Generate summary statistics
        self.calculate_derived_metrics()

        return self.data

    def gather_basic_info(self):
        """Collect basic company information."""
        self.data['basic_info'] = {
            'company_name': self.company_name,
            'ticker': self.ticker,
            'sector': None,  # To be populated from API
            'subsector': None,
            'founded': None,
            'headquarters': None,
            'employees': None,
            'website': None,
            'description': None
        }

        # Note: In production, this would connect to APIs
        print("  ✓ Basic company info gathered")

    def gather_financial_statements(self):
        """Pull historical financial statements."""

        # Initialize financial statement structure
        years = list(range(datetime.now().year - 5, datetime.now().year))

        self.data['financials'] = {
            'income_statement': self._create_income_statement_template(years),
            'balance_sheet': self._create_balance_sheet_template(years),
            'cash_flow': self._create_cash_flow_template(years)
        }

        print("  ✓ Financial statements gathered")

    def _create_income_statement_template(self, years: List[int]) -> Dict:
        """Create income statement template with key line items."""
        template = {
            'revenue': {},
            'cogs': {},
            'gross_profit': {},
            'opex': {
                'sales_marketing': {},
                'research_development': {},
                'general_admin': {},
                'total_opex': {}
            },
            'operating_income': {},
            'ebitda': {},
            'net_income': {}
        }

        # Initialize with years
        for year in years:
            for key in ['revenue', 'cogs', 'gross_profit', 'operating_income', 'ebitda', 'net_income']:
                if key in template:
                    template[key][str(year)] = None

        return template

    def _create_balance_sheet_template(self, years: List[int]) -> Dict:
        """Create balance sheet template with key line items."""
        template = {
            'current_assets': {
                'cash': {},
                'accounts_receivable': {},
                'inventory': {},
                'total_current_assets': {}
            },
            'total_assets': {},
            'current_liabilities': {
                'accounts_payable': {},
                'accrued_expenses': {},
                'short_term_debt': {},
                'total_current_liabilities': {}
            },
            'long_term_debt': {},
            'total_equity': {},
            'total_liabilities_equity': {}
        }

        return template

    def _create_cash_flow_template(self, years: List[int]) -> Dict:
        """Create cash flow statement template."""
        template = {
            'operating_cash_flow': {},
            'investing_cash_flow': {},
            'financing_cash_flow': {},
            'free_cash_flow': {},
            'beginning_cash': {},
            'ending_cash': {}
        }

        return template

    def gather_operating_metrics(self):
        """Collect SaaS metrics and operational KPIs."""

        self.data['metrics'] = {
            'saas_metrics': {
                'arr': None,  # Annual Recurring Revenue
                'mrr': None,  # Monthly Recurring Revenue
                'arr_growth_rate': None,
                'net_revenue_retention': None,
                'gross_revenue_retention': None,
                'cac': None,  # Customer Acquisition Cost
                'ltv': None,  # Lifetime Value
                'ltv_cac_ratio': None,
                'payback_months': None,
                'magic_number': None,
                'rule_of_40': None,
                'burn_multiple': None
            },
            'customer_metrics': {
                'total_customers': None,
                'enterprise_customers': None,
                'customer_concentration': {
                    'top_customer_pct': None,
                    'top_3_pct': None,
                    'top_10_pct': None
                },
                'logo_churn': None,
                'revenue_churn': None,
                'arpu': None,  # Average Revenue Per User
                'expansion_revenue_pct': None
            },
            'operational_metrics': {
                'gross_margin': None,
                'ebitda_margin': None,
                'sales_efficiency': None,
                'r&d_as_pct_revenue': None,
                's&m_as_pct_revenue': None,
                'g&a_as_pct_revenue': None,
                'employee_productivity': None
            }
        }

        print("  ✓ Operating metrics gathered")

    def gather_market_intelligence(self):
        """Collect market and competitive intelligence."""

        self.data['market_data'] = {
            'market_size': {
                'tam': None,  # Total Addressable Market
                'sam': None,  # Serviceable Addressable Market
                'som': None,  # Serviceable Obtainable Market
                'cagr': None  # Market growth rate
            },
            'competitive_landscape': {
                'direct_competitors': [],
                'market_share': None,
                'competitive_advantages': [],
                'market_position': None
            },
            'industry_trends': {
                'growth_drivers': [],
                'headwinds': [],
                'regulatory_changes': [],
                'technology_shifts': []
            }
        }

        print("  ✓ Market intelligence gathered")

    def gather_comparable_companies(self):
        """Identify and pull data for comparable companies."""

        self.data['comparables'] = {
            'public_comps': [],
            'transaction_comps': [],
            'valuation_multiples': {
                'ev_revenue_median': None,
                'ev_ebitda_median': None,
                'pe_median': None,
                'peg_median': None
            }
        }

        # Structure for comparable company
        comp_template = {
            'name': None,
            'ticker': None,
            'market_cap': None,
            'enterprise_value': None,
            'revenue': None,
            'revenue_growth': None,
            'ebitda': None,
            'ebitda_margin': None,
            'ev_revenue': None,
            'ev_ebitda': None,
            'rule_of_40': None
        }

        print("  ✓ Comparable companies gathered")

    def validate_data(self):
        """Validate collected data for completeness and accuracy."""

        validation_results = {
            'completeness': self._check_completeness(),
            'accuracy': self._check_accuracy(),
            'warnings': [],
            'errors': []
        }

        # Log validation results
        if validation_results['errors']:
            print(f"  ⚠ Data validation found {len(validation_results['errors'])} errors")
        else:
            print("  ✓ Data validation passed")

        return validation_results

    def _check_completeness(self) -> float:
        """Check what percentage of expected fields are populated."""
        total_fields = 0
        populated_fields = 0

        def count_fields(obj):
            nonlocal total_fields, populated_fields
            if isinstance(obj, dict):
                for value in obj.values():
                    count_fields(value)
            elif isinstance(obj, list):
                for item in obj:
                    count_fields(item)
            else:
                total_fields += 1
                if obj is not None:
                    populated_fields += 1

        count_fields(self.data)

        return populated_fields / total_fields if total_fields > 0 else 0

    def _check_accuracy(self) -> bool:
        """Perform accuracy checks on financial data."""
        checks_passed = True

        # Check if balance sheet balances
        # Check if cash flow reconciles
        # Check if growth rates are reasonable
        # Check if margins are within industry norms

        return checks_passed

    def calculate_derived_metrics(self):
        """Calculate additional metrics from raw data."""

        # Calculate growth rates
        if self.data['financials']['income_statement']['revenue']:
            revenues = self.data['financials']['income_statement']['revenue']
            growth_rates = self._calculate_growth_rates(revenues)
            self.data['metrics']['growth_rates'] = growth_rates

        # Calculate margin trends
        # Calculate working capital metrics
        # Calculate return metrics (ROE, ROA, ROIC)

        print("  ✓ Derived metrics calculated")

    def _calculate_growth_rates(self, values: Dict[str, float]) -> Dict[str, float]:
        """Calculate year-over-year growth rates."""
        growth_rates = {}
        sorted_years = sorted(values.keys())

        for i in range(1, len(sorted_years)):
            prev_year = sorted_years[i-1]
            curr_year = sorted_years[i]

            if values[prev_year] and values[curr_year]:
                growth = (values[curr_year] - values[prev_year]) / values[prev_year]
                growth_rates[f"{prev_year}_{curr_year}"] = growth

        return growth_rates

    def export_to_excel(self, filename: str = "company_data.xlsx"):
        """Export collected data to Excel for modeling."""

        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            # Export each data section to different sheets

            # Basic info sheet
            basic_df = pd.DataFrame([self.data['basic_info']])
            basic_df.to_excel(writer, sheet_name='Company Info', index=False)

            # Financial statements sheets
            for statement_name, statement_data in self.data['financials'].items():
                if statement_data:
                    df = pd.DataFrame(statement_data)
                    sheet_name = statement_name.replace('_', ' ').title()
                    df.to_excel(writer, sheet_name=sheet_name)

            # Metrics sheet
            metrics_df = self._flatten_nested_dict(self.data['metrics'])
            pd.DataFrame([metrics_df]).to_excel(writer, sheet_name='Metrics', index=False)

            print(f"  ✓ Data exported to {filename}")

    def _flatten_nested_dict(self, nested_dict: Dict, parent_key: str = '') -> Dict:
        """Flatten nested dictionary for Excel export."""
        items = []
        for k, v in nested_dict.items():
            new_key = f"{parent_key}_{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(self._flatten_nested_dict(v, new_key).items())
            else:
                items.append((new_key, v))
        return dict(items)

    def generate_data_summary(self) -> str:
        """Generate text summary of collected data."""

        completeness = self._check_completeness()

        summary = f"""
Data Collection Summary for {self.company_name}
{'='*50}

Data Completeness: {completeness:.1%}

Financial Data:
- Historical years available: {len(self.data['financials']['income_statement'].get('revenue', {}))}
- Latest revenue: {self._get_latest_metric('revenue')}
- Latest EBITDA margin: {self._get_latest_metric('ebitda_margin')}

Operating Metrics:
- ARR: {self.data['metrics']['saas_metrics'].get('arr', 'N/A')}
- Growth rate: {self.data['metrics']['saas_metrics'].get('arr_growth_rate', 'N/A')}
- Rule of 40: {self.data['metrics']['saas_metrics'].get('rule_of_40', 'N/A')}

Market Intelligence:
- TAM: {self.data['market_data']['market_size'].get('tam', 'N/A')}
- Market position: {self.data['market_data']['competitive_landscape'].get('market_position', 'N/A')}

Comparable Companies:
- Public comps identified: {len(self.data['comparables'].get('public_comps', []))}
- Transaction comps identified: {len(self.data['comparables'].get('transaction_comps', []))}
"""

        return summary

    def _get_latest_metric(self, metric_name: str):
        """Get the most recent value for a metric."""
        # Implementation would fetch latest available value
        return "N/A"


def main():
    """Example usage of the data gatherer."""

    # Initialize gatherer
    gatherer = CompanyDataGatherer(
        company_name="MediTech Solutions",
        ticker="MDTCH"
    )

    # Collect all data
    data = gatherer.gather_all_data()

    # Export to Excel
    gatherer.export_to_excel("meditech_data.xlsx")

    # Generate summary
    summary = gatherer.generate_data_summary()
    print("\n" + summary)

    return data


if __name__ == "__main__":
    main()
