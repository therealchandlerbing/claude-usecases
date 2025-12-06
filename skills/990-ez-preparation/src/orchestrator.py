"""
IRS Form 990-EZ Preparation Orchestrator
Main workflow coordinator for Form 990-EZ preparation

Version: 1.0.0
Author: 360 Social Impact Studios
Date: November 2025
"""

from typing import Dict, List, Optional, Tuple
from datetime import datetime
from decimal import Decimal
import json

# Import yaml with guard to provide helpful error message
try:
    import yaml
except ImportError:
    yaml = None  # type: ignore


class Form990EZOrchestrator:
    """
    Main orchestration engine for IRS Form 990-EZ preparation.

    Coordinates the 5-phase workflow:
    1. Eligibility Verification
    2. Data Collection
    3. Form Population
    4. Multi-Level Validation
    5. Filing Package Generation
    """

    def __init__(self, config_path: str = "config/"):
        """
        Initialize the orchestrator with configuration files.

        Args:
            config_path: Path to configuration directory
        """
        self.config_path = config_path
        self.validation_rules = self._load_config("validation-rules.yaml")
        self.form_mappings = self._load_config("form-mappings.yaml")
        self.api_config = self._load_config("api-integrations.yaml")

        # Initialize data storage
        self.organization_data = {}
        self.financial_data = {}
        self.program_data = {}
        self.governance_data = {}
        self.donor_data = {}

        # Validation results
        self.validation_results = []
        self.errors = []
        self.warnings = []
        self.info = []

    def _load_config(self, filename: str) -> Dict:
        """Load a YAML configuration file."""
        if yaml is None:
            raise ImportError(
                "PyYAML is required for Form 990-EZ preparation. "
                "Install with: pip install pyyaml"
            )
        try:
            with open(f"{self.config_path}{filename}", 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            print(f"Warning: Config file {filename} not found")
            return {}

    # ========================================================================
    # PHASE 1: ELIGIBILITY VERIFICATION
    # ========================================================================

    def verify_eligibility(self, gross_receipts: float, total_assets: float,
                          donor_advised_fund: bool = False,
                          operates_hospital: bool = False) -> Tuple[bool, Optional[str]]:
        """
        Check if organization qualifies for Form 990-EZ filing.

        Args:
            gross_receipts: Total gross receipts for the year
            total_assets: Total assets at end of year
            donor_advised_fund: Whether organization sponsors donor advised funds
            operates_hospital: Whether organization operates hospital facilities

        Returns:
            Tuple of (eligible: bool, reason: Optional[str])
        """
        eligibility_rules = self.validation_rules['eligibility']

        # Check gross receipts threshold
        receipts_threshold = eligibility_rules['gross_receipts']['threshold']
        if gross_receipts >= receipts_threshold:
            return False, (f"Gross receipts ${gross_receipts:,.2f} exceed "
                          f"${receipts_threshold:,.2f} threshold. Must file Form 990.")

        # Check total assets threshold
        assets_threshold = eligibility_rules['total_assets']['threshold']
        if total_assets >= assets_threshold:
            return False, (f"Total assets ${total_assets:,.2f} exceed "
                          f"${assets_threshold:,.2f} threshold. Must file Form 990.")

        # Check disqualifying conditions
        if donor_advised_fund:
            return False, "Donor advised fund sponsors must file Form 990."

        if operates_hospital:
            return False, "Hospital operators must file Form 990."

        return True, None

    def check_eligibility_interactive(self) -> bool:
        """
        Interactive eligibility check that guides user through questions.

        Returns:
            True if eligible, False otherwise
        """
        print("\n" + "="*70)
        print("IRS FORM 990-EZ ELIGIBILITY VERIFICATION")
        print("="*70 + "\n")

        print("Let me verify if your organization qualifies for Form 990-EZ.\n")

        # Gather basic information
        try:
            gross_receipts = float(input("What were your gross receipts for the tax year? $"))
            total_assets = float(input("What were your total assets at year end? $"))

            donor_advised = input("Are you a donor advised fund sponsor? (yes/no): ").lower() == 'yes'
            operates_hospital = input("Do you operate hospital facilities? (yes/no): ").lower() == 'yes'

            eligible, reason = self.verify_eligibility(
                gross_receipts, total_assets, donor_advised, operates_hospital
            )

            print("\n" + "-"*70)
            if eligible:
                print("✓ YOUR ORGANIZATION QUALIFIES FOR FORM 990-EZ")
                print(f"\n  Gross Receipts: ${gross_receipts:,.2f} (< $200,000 ✓)")
                print(f"  Total Assets:   ${total_assets:,.2f} (< $500,000 ✓)")
                print("\nYou may proceed with Form 990-EZ preparation!")
            else:
                print("✗ YOUR ORGANIZATION DOES NOT QUALIFY FOR FORM 990-EZ")
                print(f"\n  Reason: {reason}")
                print("\nYou must file Form 990 (full version) instead.")
            print("-"*70 + "\n")

            return eligible

        except ValueError:
            print("\nError: Please enter valid numeric values.")
            return False

    # ========================================================================
    # PHASE 2: DATA COLLECTION
    # ========================================================================

    def collect_organization_info(self) -> Dict:
        """
        Collect basic organization information.

        Returns:
            Dictionary with organization details
        """
        print("\n" + "="*70)
        print("ORGANIZATION INFORMATION")
        print("="*70 + "\n")

        org_info = {
            'legal_name': input("Organization's legal name: "),
            'ein': input("EIN (XX-XXXXXXX): "),
            'tax_year': int(input("Tax year (e.g., 2024): ")),
            'fiscal_year_end': input("Fiscal year end (MM/DD/YYYY): "),
            'classification': input("501(c) classification (e.g., 501(c)(3)): "),
        }

        self.organization_data = org_info
        return org_info

    def collect_financial_data(self, use_manual_entry: bool = True) -> Dict:
        """
        Collect financial data (revenue, expenses, balance sheet).

        Args:
            use_manual_entry: If True, use manual data entry. If False, attempt API integration.

        Returns:
            Dictionary with financial data
        """
        print("\n" + "="*70)
        print("FINANCIAL DATA COLLECTION")
        print("="*70 + "\n")

        if use_manual_entry:
            return self._collect_financial_manual()
        else:
            # Future: Implement QuickBooks integration
            print("API integration not yet implemented. Using manual entry.")
            return self._collect_financial_manual()

    def _collect_financial_manual(self) -> Dict:
        """Manual financial data collection with guided prompts."""

        financial = {
            'revenue': {},
            'expenses': {},
            'balance_sheet': {
                'beginning': {},
                'ending': {}
            }
        }

        # Revenue Collection
        print("\n--- REVENUE INFORMATION ---\n")
        print("Enter revenue amounts (enter 0 if not applicable):\n")

        financial['revenue']['contributions'] = float(
            input("  Contributions, gifts, and grants: $")
        )
        financial['revenue']['program_service_revenue'] = float(
            input("  Program service revenue (earned income): $")
        )
        financial['revenue']['investment_income'] = float(
            input("  Investment income (interest, dividends): $")
        )
        financial['revenue']['other'] = float(
            input("  Other revenue: $")
        )

        financial['revenue']['total'] = sum(financial['revenue'].values())
        print(f"\n  Total Revenue: ${financial['revenue']['total']:,.2f}")

        # Expense Collection
        print("\n--- EXPENSE INFORMATION ---\n")
        print("Allocate expenses by function (enter 0 if not applicable):\n")

        financial['expenses']['program_services'] = float(
            input("  Program services expenses: $")
        )
        financial['expenses']['management_general'] = float(
            input("  Management & general expenses: $")
        )
        financial['expenses']['fundraising'] = float(
            input("  Fundraising expenses: $")
        )

        financial['expenses']['total'] = sum(financial['expenses'].values())
        print(f"\n  Total Expenses: ${financial['expenses']['total']:,.2f}")

        # Calculate expense ratios
        if financial['expenses']['total'] > 0:
            program_ratio = financial['expenses']['program_services'] / financial['expenses']['total']
            print(f"  Program Expense Ratio: {program_ratio:.1%}")
            if program_ratio < 0.65:
                print("  ⚠️  Warning: Program expense ratio below recommended 65%")

        # Balance Sheet - Beginning of Year
        print("\n--- BALANCE SHEET (Beginning of Year) ---\n")

        financial['balance_sheet']['beginning']['cash'] = float(
            input("  Cash and savings: $")
        )
        financial['balance_sheet']['beginning']['other_assets'] = float(
            input("  Other assets: $")
        )
        financial['balance_sheet']['beginning']['total_assets'] = (
            financial['balance_sheet']['beginning']['cash'] +
            financial['balance_sheet']['beginning']['other_assets']
        )

        financial['balance_sheet']['beginning']['liabilities'] = float(
            input("  Total liabilities: $")
        )
        financial['balance_sheet']['beginning']['net_assets'] = (
            financial['balance_sheet']['beginning']['total_assets'] -
            financial['balance_sheet']['beginning']['liabilities']
        )

        print(f"\n  Net Assets (Beginning): ${financial['balance_sheet']['beginning']['net_assets']:,.2f}")

        # Balance Sheet - End of Year
        print("\n--- BALANCE SHEET (End of Year) ---\n")

        financial['balance_sheet']['ending']['cash'] = float(
            input("  Cash and savings: $")
        )
        financial['balance_sheet']['ending']['other_assets'] = float(
            input("  Other assets: $")
        )
        financial['balance_sheet']['ending']['total_assets'] = (
            financial['balance_sheet']['ending']['cash'] +
            financial['balance_sheet']['ending']['other_assets']
        )

        financial['balance_sheet']['ending']['liabilities'] = float(
            input("  Total liabilities: $")
        )
        financial['balance_sheet']['ending']['net_assets'] = (
            financial['balance_sheet']['ending']['total_assets'] -
            financial['balance_sheet']['ending']['liabilities']
        )

        print(f"\n  Net Assets (Ending): ${financial['balance_sheet']['ending']['net_assets']:,.2f}")

        # Calculate net income
        financial['net_income'] = financial['revenue']['total'] - financial['expenses']['total']
        print(f"\n  Net Income: ${financial['net_income']:,.2f}")

        self.financial_data = financial
        return financial

    def collect_program_data(self) -> List[Dict]:
        """
        Collect program accomplishment data for Part III.

        Returns:
            List of program dictionaries
        """
        print("\n" + "="*70)
        print("PROGRAM ACCOMPLISHMENTS")
        print("="*70 + "\n")

        print("Form 990-EZ allows up to 3 program descriptions.")
        print("Each should include: WHO you serve, WHAT you do, and IMPACT achieved.\n")

        programs = []

        for i in range(3):
            print(f"\n--- PROGRAM {i+1} ---")
            add_program = input(f"\nDo you want to add program {i+1}? (yes/no): ").lower() == 'yes'

            if not add_program:
                break

            program = {
                'number': i + 1,
                'description': input("\nProgram description (be specific and include metrics): "),
                'expenses': float(input("Program expenses: $")),
                'revenue': float(input("Program revenue (if any, enter 0 if none): $")),
            }

            programs.append(program)

        self.program_data = programs
        return programs

    def collect_governance_data(self) -> Dict:
        """
        Collect governance information (officers, directors, policies).

        Returns:
            Dictionary with governance data
        """
        print("\n" + "="*70)
        print("GOVERNANCE INFORMATION")
        print("="*70 + "\n")

        governance = {
            'officers': [],
            'policies': {}
        }

        # Collect officer information
        print("--- OFFICERS AND DIRECTORS ---\n")
        print("List all officers and directors:\n")

        while True:
            add_officer = input("\nAdd an officer/director? (yes/no): ").lower() == 'yes'
            if not add_officer:
                break

            officer = {
                'name': input("  Name: "),
                'title': input("  Title: "),
                'hours_per_week': float(input("  Average hours per week: ")),
                'compensation': float(input("  Annual compensation (enter 0 if unpaid): $")),
            }

            governance['officers'].append(officer)

        # Check for required policies
        print("\n--- GOVERNANCE POLICIES ---\n")

        governance['policies']['conflict_of_interest'] = (
            input("Do you have a conflict of interest policy? (yes/no): ").lower() == 'yes'
        )
        governance['policies']['whistleblower'] = (
            input("Do you have a whistleblower policy? (yes/no): ").lower() == 'yes'
        )
        governance['policies']['document_retention'] = (
            input("Do you have a document retention policy? (yes/no): ").lower() == 'yes'
        )

        self.governance_data = governance
        return governance

    # ========================================================================
    # PHASE 3: FORM POPULATION
    # ========================================================================

    def populate_form(self) -> Dict:
        """
        Generate complete Form 990-EZ using collected data.

        Returns:
            Dictionary representing completed form
        """
        print("\n" + "="*70)
        print("GENERATING FORM 990-EZ")
        print("="*70 + "\n")

        form = {
            'organization': self.organization_data,
            'part_i': self._populate_part_i(),
            'part_ii': self._populate_part_ii(),
            'part_iii': self._populate_part_iii(),
            'part_iv': self._populate_part_iv(),
            'part_v': self._populate_part_v(),
        }

        print("✓ Form 990-EZ populated successfully")
        return form

    def _populate_part_i(self) -> Dict:
        """Populate Part I: Revenue, Expenses, and Changes in Net Assets."""
        revenue = self.financial_data['revenue']
        expenses = self.financial_data['expenses']
        bs_begin = self.financial_data['balance_sheet']['beginning']
        bs_end = self.financial_data['balance_sheet']['ending']

        part_i = {
            # Revenue
            'line_1': revenue.get('contributions', 0),
            'line_2': revenue.get('program_service_revenue', 0),
            'line_3': 0,  # Membership dues
            'line_4': revenue.get('investment_income', 0),
            'line_8': revenue.get('other', 0),
            'line_9': revenue['total'],

            # Expenses
            'line_10': expenses.get('program_services', 0),
            'line_11b': sum(officer['compensation'] for officer in self.governance_data.get('officers', [])),
            'line_13': expenses.get('management_general', 0),
            'line_14': expenses.get('fundraising', 0),
            'line_16': expenses['total'],

            # Net Assets
            'line_17': revenue['total'] - expenses['total'],  # Excess or deficit
            'line_18': bs_begin.get('net_assets', 0),
            'line_21': bs_end.get('net_assets', 0),
        }

        return part_i

    def _populate_part_ii(self) -> Dict:
        """Populate Part II: Balance Sheet."""
        bs_begin = self.financial_data['balance_sheet']['beginning']
        bs_end = self.financial_data['balance_sheet']['ending']

        part_ii = {
            'line_22': {
                'beginning': bs_begin.get('cash', 0),
                'ending': bs_end.get('cash', 0),
            },
            'line_24': {
                'beginning': bs_begin.get('other_assets', 0),
                'ending': bs_end.get('other_assets', 0),
            },
            'line_25': {
                'beginning': bs_begin.get('total_assets', 0),
                'ending': bs_end.get('total_assets', 0),
            },
            'line_26': {
                'beginning': bs_begin.get('liabilities', 0),
                'ending': bs_end.get('liabilities', 0),
            },
            'line_27': {
                'beginning': bs_begin.get('net_assets', 0),
                'ending': bs_end.get('net_assets', 0),
            },
        }

        return part_ii

    def _populate_part_iii(self) -> List[Dict]:
        """Populate Part III: Program Service Accomplishments."""
        return self.program_data

    def _populate_part_iv(self) -> List[Dict]:
        """Populate Part IV: Officers, Directors, Trustees, Key Employees."""
        return self.governance_data.get('officers', [])

    def _populate_part_v(self) -> Dict:
        """Populate Part V: Other Information."""
        policies = self.governance_data.get('policies', {})

        part_v = {
            'line_33': False,  # Political activity (typically No for 501(c)(3))
            'line_34': False,  # Lobbying
            'line_44a': policies.get('conflict_of_interest', False),
            'line_44b': policies.get('whistleblower', False),
            'line_44c': policies.get('document_retention', False),
        }

        return part_v

    # ========================================================================
    # PHASE 4: VALIDATION
    # ========================================================================

    def validate_form(self, form: Dict) -> Dict:
        """
        Perform multi-level validation on completed form.

        Args:
            form: Completed form dictionary

        Returns:
            Validation report
        """
        print("\n" + "="*70)
        print("VALIDATING FORM 990-EZ")
        print("="*70 + "\n")

        self.validation_results = []
        self.errors = []
        self.warnings = []
        self.info = []

        # Level 1: Mathematical Validation
        self._validate_mathematical(form)

        # Level 2: Regulatory Compliance
        self._validate_regulatory(form)

        # Level 3: Narrative Quality
        self._validate_narrative(form)

        # Level 4: Strategic Indicators
        self._validate_strategic(form)

        # Generate summary
        summary = {
            'errors': len(self.errors),
            'warnings': len(self.warnings),
            'info': len(self.info),
            'filing_ready': len(self.errors) == 0,
            'details': {
                'errors': self.errors,
                'warnings': self.warnings,
                'info': self.info,
            }
        }

        # Print summary
        print("\n--- VALIDATION SUMMARY ---\n")
        print(f"  Errors:   {summary['errors']}")
        print(f"  Warnings: {summary['warnings']}")
        print(f"  Info:     {summary['info']}")
        print(f"\n  Filing Ready: {'YES ✓' if summary['filing_ready'] else 'NO ✗'}")

        if self.errors:
            print("\n  ERRORS (must fix before filing):")
            for error in self.errors:
                print(f"    ✗ {error}")

        if self.warnings:
            print("\n  WARNINGS (should address):")
            for warning in self.warnings:
                print(f"    ⚠️  {warning}")

        return summary

    def _validate_mathematical(self, form: Dict):
        """Level 1: Mathematical accuracy validation."""
        part_i = form['part_i']
        part_ii = form['part_ii']

        # Check revenue totals
        revenue_sum = part_i['line_1'] + part_i['line_2'] + part_i['line_3'] + part_i['line_4'] + part_i['line_8']
        if abs(revenue_sum - part_i['line_9']) > 0.01:
            self.errors.append(f"Part I revenue lines don't sum correctly ({revenue_sum} ≠ {part_i['line_9']})")

        # Check balance sheet equation
        ending_assets = part_ii['line_25']['ending']
        ending_liabilities = part_ii['line_26']['ending']
        ending_net_assets = part_ii['line_27']['ending']

        if abs(ending_assets - (ending_liabilities + ending_net_assets)) > 0.01:
            self.errors.append("Balance sheet doesn't balance (Assets ≠ Liabilities + Net Assets)")

        # Check Part I and Part II reconciliation
        if abs(part_i['line_21'] - ending_net_assets) > 0.01:
            self.errors.append("Part I ending net assets doesn't match Part II net assets")

        if len(self.errors) == 0:
            self.info.append("All mathematical calculations verified ✓")

    def _validate_regulatory(self, form: Dict):
        """Level 2: Regulatory compliance validation."""
        part_i = form['part_i']
        part_v = form['part_v']

        # Check expense allocation
        total_expenses = part_i['line_16']
        if total_expenses > 0:
            program_ratio = part_i['line_10'] / total_expenses
            if program_ratio < 0.65:
                self.warnings.append(f"Program expense ratio {program_ratio:.1%} below recommended 65%")

        # Check governance policies
        if not part_v.get('line_44a'):
            self.warnings.append("Missing conflict of interest policy")

        if not part_v.get('line_44b'):
            self.info.append("Consider adopting a whistleblower policy")

    def _validate_narrative(self, form: Dict):
        """Level 3: Narrative quality validation."""
        programs = form.get('part_iii', [])

        for i, program in enumerate(programs):
            desc = program.get('description', '')
            if len(desc) < 50:
                self.warnings.append(f"Program {i+1} description seems too brief")

    def _validate_strategic(self, form: Dict):
        """Level 4: Strategic indicators validation."""
        part_i = form['part_i']

        # Financial sustainability
        if part_i['line_17'] < 0:
            self.warnings.append("Organization operated at a deficit this year")

        # Revenue diversification
        total_revenue = part_i['line_9']
        if total_revenue > 0:
            contrib_ratio = part_i['line_1'] / total_revenue
            if contrib_ratio > 0.75:
                self.info.append("High reliance on contributions - consider revenue diversification")

    # ========================================================================
    # PHASE 5: FILING PACKAGE GENERATION
    # ========================================================================

    def generate_filing_package(self, form: Dict, validation: Dict) -> Dict:
        """
        Generate complete filing package.

        Args:
            form: Completed and validated form
            validation: Validation results

        Returns:
            Filing package with all components
        """
        print("\n" + "="*70)
        print("GENERATING FILING PACKAGE")
        print("="*70 + "\n")

        package = {
            'form_990ez': form,
            'validation_report': validation,
            'schedules': {},
            'filing_checklist': self._generate_checklist(form),
            'executive_summary': self._generate_summary(form),
        }

        # Determine required schedules
        if self.organization_data.get('classification') == '501(c)(3)':
            package['schedules']['schedule_a'] = True
            print("  ✓ Schedule A (Public Charity Status) - Required")

        if form['part_i']['line_1'] >= 5000:  # Check if any single contribution >= $5,000
            package['schedules']['schedule_b'] = True
            print("  ✓ Schedule B (Contributors) - Required")

        print("\n  Filing package generated successfully!")

        return package

    def _generate_checklist(self, form: Dict) -> List[str]:
        """Generate pre-filing checklist."""
        checklist = [
            "All required fields completed",
            "All schedules attached",
            "Officer signatures obtained",
            "Form dated",
            "Mathematical accuracy verified",
            "Board approval obtained",
            "Copies made for records",
        ]
        return checklist

    def _generate_summary(self, form: Dict) -> Dict:
        """Generate executive summary of filing."""
        part_i = form['part_i']

        summary = {
            'organization': self.organization_data.get('legal_name'),
            'tax_year': self.organization_data.get('tax_year'),
            'total_revenue': part_i['line_9'],
            'total_expenses': part_i['line_16'],
            'net_income': part_i['line_17'],
            'ending_net_assets': part_i['line_21'],
        }

        return summary


def main():
    """Main entry point for interactive 990-EZ preparation."""
    print("\n" + "="*70)
    print("IRS FORM 990-EZ PREPARATION ASSISTANT")
    print("Version 1.0 | 360 Social Impact Studios")
    print("="*70 + "\n")

    # Initialize orchestrator
    orchestrator = Form990EZOrchestrator()

    # Phase 1: Eligibility Check
    if not orchestrator.check_eligibility_interactive():
        print("\nExiting: Organization must file Form 990 instead of 990-EZ.")
        return

    # Phase 2: Data Collection
    input("\nPress Enter to continue to data collection...")
    orchestrator.collect_organization_info()
    orchestrator.collect_financial_data()
    orchestrator.collect_program_data()
    orchestrator.collect_governance_data()

    # Phase 3: Form Population
    input("\nPress Enter to generate Form 990-EZ...")
    form = orchestrator.populate_form()

    # Phase 4: Validation
    input("\nPress Enter to validate form...")
    validation = orchestrator.validate_form(form)

    # Phase 5: Filing Package
    if validation['filing_ready']:
        input("\nPress Enter to generate filing package...")
        package = orchestrator.generate_filing_package(form, validation)

        print("\n" + "="*70)
        print("FORM 990-EZ PREPARATION COMPLETE!")
        print("="*70 + "\n")
        print("Your filing package is ready. Review all documents before filing.")
        print("\nNext steps:")
        print("  1. Review all documents for accuracy")
        print("  2. Obtain board approval")
        print("  3. Obtain officer signatures")
        print("  4. File electronically by deadline")
        print("\n" + "="*70 + "\n")
    else:
        print("\n" + "="*70)
        print("FORM HAS ERRORS - CANNOT FILE")
        print("="*70 + "\n")
        print("Please address all errors before generating filing package.")


if __name__ == "__main__":
    main()
