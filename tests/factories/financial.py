"""
Financial Data Factory

Generates realistic financial data for testing 990-EZ preparation,
financial modeling, and compliance skills.
"""

import random
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional

try:
    from faker import Faker
    HAS_FAKER = True
except ImportError:
    HAS_FAKER = False


class FinancialDataFactory:
    """Factory for generating financial test data."""

    def __init__(self, seed: Optional[int] = None):
        """
        Initialize the factory.

        Args:
            seed: Random seed for reproducible data generation
        """
        self._seed = seed
        # Create isolated random generator for this instance
        self._rng = random.Random(seed)

        if HAS_FAKER:
            self.fake = Faker()
            if seed is not None:
                self.fake.seed_instance(seed)
        else:
            self.fake = None

    def _random_name(self) -> str:
        """Generate a random name."""
        if self.fake:
            return self.fake.name()
        names = ["John Smith", "Jane Doe", "Bob Johnson", "Alice Williams"]
        return self._rng.choice(names)

    def _random_company(self) -> str:
        """Generate a random company name."""
        if self.fake:
            return self.fake.company()
        companies = ["Acme Corp", "Global Inc", "Tech Solutions", "Impact Partners"]
        return self._rng.choice(companies)

    def _random_ein(self) -> str:
        """Generate a random EIN."""
        return f"{self._rng.randint(10, 99)}-{self._rng.randint(1000000, 9999999)}"

    def create_990_eligible(self) -> Dict[str, Any]:
        """
        Create financial data for a 990-EZ eligible organization.

        Returns organization with:
        - Gross receipts < $200,000
        - Total assets < $500,000
        """
        gross_receipts = self._rng.uniform(50000, 199999)
        total_assets = self._rng.uniform(100000, 499999)

        # Ensure reasonable expense ratios
        program_expenses = gross_receipts * self._rng.uniform(0.65, 0.85)
        admin_expenses = gross_receipts * self._rng.uniform(0.08, 0.15)
        fundraising_expenses = gross_receipts * self._rng.uniform(0.02, 0.10)

        return {
            "organization": {
                "name": f"{self._random_company()} Foundation",
                "ein": self._random_ein(),
                "address": {
                    "street": "123 Main St",
                    "city": "San Francisco",
                    "state": "CA",
                    "zip": "94102"
                },
                "fiscal_year_end": "12/31",
                "website": "https://example.org"
            },
            "financial": {
                "gross_receipts": round(gross_receipts, 2),
                "total_assets": round(total_assets, 2),
                "contributions": round(gross_receipts * 0.7, 2),
                "program_service_revenue": round(gross_receipts * 0.2, 2),
                "investment_income": round(gross_receipts * 0.05, 2),
                "other_revenue": round(gross_receipts * 0.05, 2),
                "program_expenses": round(program_expenses, 2),
                "administrative_expenses": round(admin_expenses, 2),
                "fundraising_expenses": round(fundraising_expenses, 2),
                "total_expenses": round(program_expenses + admin_expenses + fundraising_expenses, 2),
                "net_assets_beginning": round(total_assets * 0.8, 2),
                "net_assets_end": round(total_assets, 2)
            },
            "governance": {
                "board_members": self._rng.randint(5, 15),
                "voting_members": self._rng.randint(4, 12),
                "independent_members": self._rng.randint(3, 10),
                "has_conflict_of_interest_policy": True,
                "has_whistleblower_policy": self._rng.choice([True, False]),
                "has_document_retention_policy": self._rng.choice([True, False])
            }
        }

    def create_990_ineligible_high_receipts(self) -> Dict[str, Any]:
        """Create data for organization ineligible due to high receipts."""
        data = self.create_990_eligible()
        data["financial"]["gross_receipts"] = round(self._rng.uniform(250000, 500000), 2)
        return data

    def create_990_ineligible_high_assets(self) -> Dict[str, Any]:
        """Create data for organization ineligible due to high assets."""
        data = self.create_990_eligible()
        data["financial"]["total_assets"] = round(self._rng.uniform(600000, 1000000), 2)
        return data

    def create_revenue_breakdown(self, total: float) -> Dict[str, float]:
        """Create realistic revenue breakdown summing to total."""
        contributions_pct = self._rng.uniform(0.5, 0.8)
        program_pct = self._rng.uniform(0.1, 0.3)
        investment_pct = self._rng.uniform(0.02, 0.1)
        other_pct = 1 - contributions_pct - program_pct - investment_pct

        return {
            "contributions": round(total * contributions_pct, 2),
            "program_service_revenue": round(total * program_pct, 2),
            "investment_income": round(total * investment_pct, 2),
            "other_revenue": round(total * max(0, other_pct), 2)
        }

    def create_expense_breakdown(self, total: float) -> Dict[str, float]:
        """Create realistic expense breakdown summing to total."""
        program_pct = self._rng.uniform(0.65, 0.85)
        admin_pct = self._rng.uniform(0.08, 0.20)
        fundraising_pct = 1 - program_pct - admin_pct

        return {
            "program_expenses": round(total * program_pct, 2),
            "administrative_expenses": round(total * admin_pct, 2),
            "fundraising_expenses": round(total * max(0, fundraising_pct), 2)
        }

    def create_officer(self, is_compensated: bool = False) -> Dict[str, Any]:
        """Create officer/director data."""
        return {
            "name": self._random_name(),
            "title": self._rng.choice(["President", "Vice President", "Secretary", "Treasurer", "Director"]),
            "hours_per_week": self._rng.randint(1, 40) if is_compensated else self._rng.randint(1, 10),
            "compensation": round(self._rng.uniform(50000, 150000), 2) if is_compensated else 0,
            "is_officer": self._rng.choice([True, False]),
            "is_director": True
        }

    def create_program(self) -> Dict[str, Any]:
        """Create program accomplishment data."""
        expenses = round(self._rng.uniform(10000, 100000), 2)
        return {
            "name": self._rng.choice([
                "Youth Education Program",
                "Community Health Initiative",
                "Environmental Conservation",
                "Arts & Culture Program",
                "Food Security Initiative"
            ]),
            "description": "Program providing services to the community",
            "expenses": expenses,
            "grants": round(expenses * self._rng.uniform(0, 0.3), 2),
            "revenue": round(expenses * self._rng.uniform(0, 0.2), 2),
            "beneficiaries": self._rng.randint(100, 5000)
        }

    def create_donor(self, amount_range: tuple = (100, 10000)) -> Dict[str, Any]:
        """Create donor contribution data."""
        return {
            "name": self._random_name(),
            "amount": round(self._rng.uniform(*amount_range), 2),
            "date": (datetime.now() - timedelta(days=self._rng.randint(1, 365))).isoformat(),
            "type": self._rng.choice(["individual", "foundation", "corporate"]),
            "restricted": self._rng.choice([True, False]),
            "recurring": self._rng.choice([True, False])
        }
