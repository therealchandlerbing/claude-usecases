"""
Unit tests for IRS Form 990-EZ Preparation Orchestrator.

Tests cover all 5 phases of the 990-EZ preparation workflow:
1. Eligibility Verification
2. Data Collection
3. Form Population
4. Multi-Level Validation
5. Filing Package Generation

Priority: CRITICAL (Financial/Compliance)
"""

import pytest
import tempfile
from pathlib import Path

# Import yaml with guard to prevent CI failures
try:
    import yaml
except ImportError:
    yaml = None  # type: ignore

# Skip all tests in this module if yaml is not available
pytestmark = pytest.mark.skipif(
    yaml is None,
    reason="PyYAML not installed - skipping yaml-dependent tests"
)

from unittest.mock import patch, MagicMock
import sys
import os

# Add skills directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "skills" / "990-ez-preparation" / "src"))

# Guard the import to prevent issues during test collection if yaml is missing
if yaml is not None:
    from orchestrator import Form990EZOrchestrator
else:
    Form990EZOrchestrator = None  # type: ignore


# ============================================================================
# FIXTURES
# ============================================================================

@pytest.fixture
def temp_config_dir():
    """Create temporary configuration directory with test config files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir)

        # Create validation-rules.yaml
        validation_rules = {
            'eligibility': {
                'gross_receipts': {'threshold': 200000},
                'total_assets': {'threshold': 500000},
            },
            'regulatory_compliance': {
                'expense_allocation': {
                    'program_services': {
                        'minimum_recommended': 0.65
                    }
                }
            }
        }

        with open(config_path / 'validation-rules.yaml', 'w') as f:
            yaml.dump(validation_rules, f)

        # Create form-mappings.yaml (empty for tests)
        with open(config_path / 'form-mappings.yaml', 'w') as f:
            yaml.dump({}, f)

        # Create api-integrations.yaml (empty for tests)
        with open(config_path / 'api-integrations.yaml', 'w') as f:
            yaml.dump({}, f)

        yield str(config_path) + "/"


@pytest.fixture
def orchestrator(temp_config_dir):
    """Create Form990EZOrchestrator instance with test configuration."""
    return Form990EZOrchestrator(config_path=temp_config_dir)


@pytest.fixture
def sample_organization_data():
    """Sample organization data for testing."""
    return {
        'legal_name': 'Test Nonprofit Organization',
        'ein': '12-3456789',
        'tax_year': 2024,
        'fiscal_year_end': '12/31/2024',
        'classification': '501(c)(3)',
    }


@pytest.fixture
def sample_financial_data():
    """Sample financial data for testing."""
    return {
        'revenue': {
            'contributions': 100000.00,
            'program_service_revenue': 40000.00,
            'investment_income': 5000.00,
            'other': 5000.00,
            'total': 150000.00,
        },
        'expenses': {
            'program_services': 90000.00,
            'management_general': 25000.00,
            'fundraising': 10000.00,
            'total': 125000.00,
        },
        'balance_sheet': {
            'beginning': {
                'cash': 50000.00,
                'other_assets': 150000.00,
                'total_assets': 200000.00,
                'liabilities': 50000.00,
                'net_assets': 150000.00,
            },
            'ending': {
                'cash': 60000.00,
                'other_assets': 165000.00,
                'total_assets': 225000.00,
                'liabilities': 50000.00,
                'net_assets': 175000.00,
            }
        },
        'net_income': 25000.00,
    }


@pytest.fixture
def sample_governance_data():
    """Sample governance data for testing."""
    return {
        'officers': [
            {
                'name': 'Jane Doe',
                'title': 'Executive Director',
                'hours_per_week': 40.0,
                'compensation': 75000.00,
            },
            {
                'name': 'John Smith',
                'title': 'Board Chair',
                'hours_per_week': 5.0,
                'compensation': 0.00,
            },
        ],
        'policies': {
            'conflict_of_interest': True,
            'whistleblower': True,
            'document_retention': True,
        }
    }


@pytest.fixture
def sample_program_data():
    """Sample program data for testing."""
    return [
        {
            'number': 1,
            'description': 'Provided educational workshops to 500 underserved youth, resulting in 85% improvement in literacy scores and 95% high school graduation rate among participants.',
            'expenses': 60000.00,
            'revenue': 10000.00,
        },
        {
            'number': 2,
            'description': 'Operated food bank serving 200 families monthly, distributing 50,000 pounds of food and providing nutritional education to 150 participants.',
            'expenses': 30000.00,
            'revenue': 5000.00,
        },
    ]


# ============================================================================
# PHASE 1: ELIGIBILITY VERIFICATION TESTS
# ============================================================================

@pytest.mark.unit
@pytest.mark.financial
@pytest.mark.compliance
class TestEligibilityVerification:
    """Tests for Phase 1: Eligibility Verification."""

    def test_eligible_organization_basic(self, orchestrator):
        """Test basic eligibility check with qualifying organization."""
        eligible, reason = orchestrator.verify_eligibility(
            gross_receipts=150000.00,
            total_assets=400000.00
        )

        assert eligible is True
        assert reason is None

    def test_eligible_at_threshold_minus_one(self, orchestrator):
        """Test eligibility at just below thresholds."""
        eligible, reason = orchestrator.verify_eligibility(
            gross_receipts=199999.99,
            total_assets=499999.99
        )

        assert eligible is True
        assert reason is None

    def test_ineligible_gross_receipts_exceeds_threshold(self, orchestrator):
        """Test ineligibility due to gross receipts exceeding $200,000 threshold."""
        eligible, reason = orchestrator.verify_eligibility(
            gross_receipts=200000.00,
            total_assets=100000.00
        )

        assert eligible is False
        assert "Gross receipts" in reason
        assert "200,000" in reason
        assert "Must file Form 990" in reason

    def test_ineligible_total_assets_exceeds_threshold(self, orchestrator):
        """Test ineligibility due to total assets exceeding $500,000 threshold."""
        eligible, reason = orchestrator.verify_eligibility(
            gross_receipts=100000.00,
            total_assets=500000.00
        )

        assert eligible is False
        assert "Total assets" in reason
        assert "500,000" in reason
        assert "Must file Form 990" in reason

    def test_ineligible_both_thresholds_exceeded(self, orchestrator):
        """Test ineligibility when both thresholds are exceeded."""
        eligible, reason = orchestrator.verify_eligibility(
            gross_receipts=250000.00,
            total_assets=600000.00
        )

        assert eligible is False
        # Should fail on gross receipts first
        assert "Gross receipts" in reason

    def test_ineligible_donor_advised_fund(self, orchestrator):
        """Test ineligibility for donor advised fund sponsors."""
        eligible, reason = orchestrator.verify_eligibility(
            gross_receipts=100000.00,
            total_assets=200000.00,
            donor_advised_fund=True
        )

        assert eligible is False
        assert "donor advised fund" in reason.lower()
        assert "must file form 990" in reason.lower()

    def test_ineligible_hospital_operator(self, orchestrator):
        """Test ineligibility for hospital operators."""
        eligible, reason = orchestrator.verify_eligibility(
            gross_receipts=100000.00,
            total_assets=200000.00,
            operates_hospital=True
        )

        assert eligible is False
        assert "hospital" in reason.lower()
        assert "must file form 990" in reason.lower()

    def test_edge_case_zero_amounts(self, orchestrator):
        """Test eligibility with zero gross receipts and assets."""
        eligible, reason = orchestrator.verify_eligibility(
            gross_receipts=0.00,
            total_assets=0.00
        )

        assert eligible is True
        assert reason is None

    def test_edge_case_negative_amounts_should_be_eligible(self, orchestrator):
        """Test behavior with negative amounts (should be eligible by threshold logic)."""
        # Note: Negative amounts shouldn't occur in practice but testing threshold logic
        eligible, reason = orchestrator.verify_eligibility(
            gross_receipts=-100.00,
            total_assets=-100.00
        )

        assert eligible is True


# ============================================================================
# PHASE 2: DATA COLLECTION TESTS
# ============================================================================

@pytest.mark.unit
class TestDataCollection:
    """Tests for Phase 2: Data Collection."""

    def test_organization_data_storage(self, orchestrator, sample_organization_data):
        """Test that organization data is stored correctly."""
        orchestrator.organization_data = sample_organization_data

        assert orchestrator.organization_data['legal_name'] == 'Test Nonprofit Organization'
        assert orchestrator.organization_data['ein'] == '12-3456789'
        assert orchestrator.organization_data['tax_year'] == 2024
        assert orchestrator.organization_data['classification'] == '501(c)(3)'

    def test_financial_data_storage(self, orchestrator, sample_financial_data):
        """Test that financial data is stored correctly."""
        orchestrator.financial_data = sample_financial_data

        assert orchestrator.financial_data['revenue']['total'] == 150000.00
        assert orchestrator.financial_data['expenses']['total'] == 125000.00
        assert orchestrator.financial_data['net_income'] == 25000.00

    def test_governance_data_storage(self, orchestrator, sample_governance_data):
        """Test that governance data is stored correctly."""
        orchestrator.governance_data = sample_governance_data

        assert len(orchestrator.governance_data['officers']) == 2
        assert orchestrator.governance_data['policies']['conflict_of_interest'] is True

    def test_program_data_storage(self, orchestrator, sample_program_data):
        """Test that program data is stored correctly."""
        orchestrator.program_data = sample_program_data

        assert len(orchestrator.program_data) == 2
        assert orchestrator.program_data[0]['number'] == 1


# ============================================================================
# PHASE 3: FORM POPULATION TESTS
# ============================================================================

@pytest.mark.unit
@pytest.mark.financial
class TestFormPopulation:
    """Tests for Phase 3: Form Population."""

    def test_populate_part_i_revenue_lines(self, orchestrator, sample_financial_data, sample_governance_data):
        """Test Part I revenue line population."""
        orchestrator.financial_data = sample_financial_data
        orchestrator.governance_data = sample_governance_data

        part_i = orchestrator._populate_part_i()

        assert part_i['line_1'] == 100000.00  # Contributions
        assert part_i['line_2'] == 40000.00   # Program service revenue
        assert part_i['line_4'] == 5000.00    # Investment income
        assert part_i['line_8'] == 5000.00    # Other revenue
        assert part_i['line_9'] == 150000.00  # Total revenue

    def test_populate_part_i_expense_lines(self, orchestrator, sample_financial_data, sample_governance_data):
        """Test Part I expense line population."""
        orchestrator.financial_data = sample_financial_data
        orchestrator.governance_data = sample_governance_data

        part_i = orchestrator._populate_part_i()

        assert part_i['line_10'] == 90000.00   # Program services
        assert part_i['line_13'] == 25000.00   # Management & general
        assert part_i['line_14'] == 10000.00   # Fundraising
        assert part_i['line_16'] == 125000.00  # Total expenses

    def test_populate_part_i_officer_compensation(self, orchestrator, sample_financial_data, sample_governance_data):
        """Test Part I officer compensation calculation."""
        orchestrator.financial_data = sample_financial_data
        orchestrator.governance_data = sample_governance_data

        part_i = orchestrator._populate_part_i()

        # Total compensation: $75,000 + $0 = $75,000
        assert part_i['line_11b'] == 75000.00

    def test_populate_part_i_net_income_calculation(self, orchestrator, sample_financial_data, sample_governance_data):
        """Test Part I net income calculation."""
        orchestrator.financial_data = sample_financial_data
        orchestrator.governance_data = sample_governance_data

        part_i = orchestrator._populate_part_i()

        # Net income: $150,000 - $125,000 = $25,000
        assert part_i['line_17'] == 25000.00

    def test_populate_part_ii_balance_sheet(self, orchestrator, sample_financial_data):
        """Test Part II balance sheet population."""
        orchestrator.financial_data = sample_financial_data

        part_ii = orchestrator._populate_part_ii()

        # Check beginning balances
        assert part_ii['line_22']['beginning'] == 50000.00   # Cash
        assert part_ii['line_25']['beginning'] == 200000.00  # Total assets
        assert part_ii['line_26']['beginning'] == 50000.00   # Liabilities
        assert part_ii['line_27']['beginning'] == 150000.00  # Net assets

        # Check ending balances
        assert part_ii['line_22']['ending'] == 60000.00   # Cash
        assert part_ii['line_25']['ending'] == 225000.00  # Total assets
        assert part_ii['line_26']['ending'] == 50000.00   # Liabilities
        assert part_ii['line_27']['ending'] == 175000.00  # Net assets

    def test_populate_part_iii_programs(self, orchestrator, sample_program_data):
        """Test Part III program accomplishments population."""
        orchestrator.program_data = sample_program_data

        part_iii = orchestrator._populate_part_iii()

        assert len(part_iii) == 2
        assert part_iii[0]['number'] == 1
        assert 'educational workshops' in part_iii[0]['description'].lower()
        assert part_iii[0]['expenses'] == 60000.00

    def test_populate_part_iv_officers(self, orchestrator, sample_governance_data):
        """Test Part IV officers population."""
        orchestrator.governance_data = sample_governance_data

        part_iv = orchestrator._populate_part_iv()

        assert len(part_iv) == 2
        assert part_iv[0]['name'] == 'Jane Doe'
        assert part_iv[0]['title'] == 'Executive Director'
        assert part_iv[0]['compensation'] == 75000.00

    def test_populate_part_v_policies(self, orchestrator, sample_governance_data):
        """Test Part V policies population."""
        orchestrator.governance_data = sample_governance_data

        part_v = orchestrator._populate_part_v()

        assert part_v['line_44a'] is True  # Conflict of interest
        assert part_v['line_44b'] is True  # Whistleblower
        assert part_v['line_44c'] is True  # Document retention

    def test_populate_complete_form(self, orchestrator, sample_organization_data,
                                    sample_financial_data, sample_governance_data, sample_program_data):
        """Test complete form population."""
        orchestrator.organization_data = sample_organization_data
        orchestrator.financial_data = sample_financial_data
        orchestrator.governance_data = sample_governance_data
        orchestrator.program_data = sample_program_data

        form = orchestrator.populate_form()

        assert 'organization' in form
        assert 'part_i' in form
        assert 'part_ii' in form
        assert 'part_iii' in form
        assert 'part_iv' in form
        assert 'part_v' in form


# ============================================================================
# PHASE 4: VALIDATION TESTS
# ============================================================================

@pytest.mark.unit
@pytest.mark.financial
@pytest.mark.compliance
class TestValidation:
    """Tests for Phase 4: Multi-Level Validation."""

    def test_validate_mathematical_revenue_sum_correct(self, orchestrator, sample_organization_data,
                                                       sample_financial_data, sample_governance_data, sample_program_data):
        """Test mathematical validation passes with correct revenue sums."""
        orchestrator.organization_data = sample_organization_data
        orchestrator.financial_data = sample_financial_data
        orchestrator.governance_data = sample_governance_data
        orchestrator.program_data = sample_program_data

        form = orchestrator.populate_form()
        validation = orchestrator.validate_form(form)

        assert validation['filing_ready'] is True
        assert validation['errors'] == 0

    def test_validate_mathematical_balance_sheet_balances(self, orchestrator, sample_organization_data,
                                                          sample_financial_data, sample_governance_data, sample_program_data):
        """Test mathematical validation verifies balance sheet equation."""
        orchestrator.organization_data = sample_organization_data
        orchestrator.financial_data = sample_financial_data
        orchestrator.governance_data = sample_governance_data
        orchestrator.program_data = sample_program_data

        form = orchestrator.populate_form()

        # Verify balance sheet equation: Assets = Liabilities + Net Assets
        part_ii = form['part_ii']
        assets = part_ii['line_25']['ending']
        liabilities = part_ii['line_26']['ending']
        net_assets = part_ii['line_27']['ending']

        assert abs(assets - (liabilities + net_assets)) < 0.01

    def test_validate_mathematical_part_i_part_ii_reconciliation(self, orchestrator, sample_organization_data,
                                                                  sample_financial_data, sample_governance_data, sample_program_data):
        """Test that Part I and Part II net assets reconcile."""
        orchestrator.organization_data = sample_organization_data
        orchestrator.financial_data = sample_financial_data
        orchestrator.governance_data = sample_governance_data
        orchestrator.program_data = sample_program_data

        form = orchestrator.populate_form()

        # Part I ending net assets should match Part II net assets
        part_i_net_assets = form['part_i']['line_21']
        part_ii_net_assets = form['part_ii']['line_27']['ending']

        assert abs(part_i_net_assets - part_ii_net_assets) < 0.01

    def test_validate_regulatory_program_expense_ratio_adequate(self, orchestrator, sample_organization_data,
                                                                sample_financial_data, sample_governance_data, sample_program_data):
        """Test regulatory validation with adequate program expense ratio (72%)."""
        orchestrator.organization_data = sample_organization_data
        orchestrator.financial_data = sample_financial_data
        orchestrator.governance_data = sample_governance_data
        orchestrator.program_data = sample_program_data

        form = orchestrator.populate_form()
        validation = orchestrator.validate_form(form)

        # Program ratio: $90,000 / $125,000 = 0.72 (72%) - above 65% threshold
        assert validation['warnings'] == 0 or not any('Program expense ratio' in w for w in validation['details']['warnings'])

    def test_validate_regulatory_program_expense_ratio_low(self, orchestrator, sample_organization_data,
                                                           sample_governance_data, sample_program_data):
        """Test regulatory validation warns about low program expense ratio."""
        # Create financial data with low program ratio (60%)
        low_program_financial = {
            'revenue': {'contributions': 100000, 'program_service_revenue': 0,
                       'investment_income': 0, 'other': 0, 'total': 100000},
            'expenses': {'program_services': 60000, 'management_general': 25000,
                        'fundraising': 15000, 'total': 100000},
            'balance_sheet': {
                'beginning': {'cash': 50000, 'other_assets': 50000, 'total_assets': 100000,
                             'liabilities': 20000, 'net_assets': 80000},
                'ending': {'cash': 50000, 'other_assets': 50000, 'total_assets': 100000,
                          'liabilities': 20000, 'net_assets': 80000}
            },
            'net_income': 0,
        }

        orchestrator.organization_data = sample_organization_data
        orchestrator.financial_data = low_program_financial
        orchestrator.governance_data = sample_governance_data
        orchestrator.program_data = sample_program_data

        form = orchestrator.populate_form()
        validation = orchestrator.validate_form(form)

        # Should warn about program ratio below 65%
        assert any('Program expense ratio' in w and '60' in w for w in validation['details']['warnings'])

    def test_validate_regulatory_missing_conflict_of_interest_policy(self, orchestrator, sample_organization_data,
                                                                      sample_financial_data, sample_program_data):
        """Test regulatory validation warns about missing conflict of interest policy."""
        # Governance data without conflict of interest policy
        governance_no_coi = {
            'officers': [{'name': 'Test Officer', 'title': 'Director',
                         'hours_per_week': 10, 'compensation': 0}],
            'policies': {
                'conflict_of_interest': False,
                'whistleblower': False,
                'document_retention': False,
            }
        }

        orchestrator.organization_data = sample_organization_data
        orchestrator.financial_data = sample_financial_data
        orchestrator.governance_data = governance_no_coi
        orchestrator.program_data = sample_program_data

        form = orchestrator.populate_form()
        validation = orchestrator.validate_form(form)

        # Should warn about missing conflict of interest policy
        assert any('conflict of interest' in w.lower() for w in validation['details']['warnings'])

    def test_validate_narrative_adequate_description(self, orchestrator, sample_organization_data,
                                                     sample_financial_data, sample_governance_data, sample_program_data):
        """Test narrative validation passes with adequate program descriptions."""
        orchestrator.organization_data = sample_organization_data
        orchestrator.financial_data = sample_financial_data
        orchestrator.governance_data = sample_governance_data
        orchestrator.program_data = sample_program_data

        form = orchestrator.populate_form()
        validation = orchestrator.validate_form(form)

        # Both program descriptions are >50 characters, should not warn
        assert not any('description seems too brief' in w for w in validation['details']['warnings'])

    def test_validate_narrative_brief_description_warning(self, orchestrator, sample_organization_data,
                                                          sample_financial_data, sample_governance_data):
        """Test narrative validation warns about brief program descriptions."""
        # Program with brief description (<50 characters)
        brief_program = [{
            'number': 1,
            'description': 'Education program',  # Only 17 characters
            'expenses': 50000,
            'revenue': 0,
        }]

        orchestrator.organization_data = sample_organization_data
        orchestrator.financial_data = sample_financial_data
        orchestrator.governance_data = sample_governance_data
        orchestrator.program_data = brief_program

        form = orchestrator.populate_form()
        validation = orchestrator.validate_form(form)

        # Should warn about brief description
        assert any('description seems too brief' in w for w in validation['details']['warnings'])

    def test_validate_strategic_deficit_warning(self, orchestrator, sample_organization_data,
                                               sample_governance_data, sample_program_data):
        """Test strategic validation warns about deficit operations."""
        # Financial data with deficit (expenses > revenue)
        deficit_financial = {
            'revenue': {'contributions': 50000, 'program_service_revenue': 0,
                       'investment_income': 0, 'other': 0, 'total': 50000},
            'expenses': {'program_services': 40000, 'management_general': 15000,
                        'fundraising': 5000, 'total': 60000},
            'balance_sheet': {
                'beginning': {'cash': 50000, 'other_assets': 50000, 'total_assets': 100000,
                             'liabilities': 20000, 'net_assets': 80000},
                'ending': {'cash': 40000, 'other_assets': 50000, 'total_assets': 90000,
                          'liabilities': 20000, 'net_assets': 70000}
            },
            'net_income': -10000,
        }

        orchestrator.organization_data = sample_organization_data
        orchestrator.financial_data = deficit_financial
        orchestrator.governance_data = sample_governance_data
        orchestrator.program_data = sample_program_data

        form = orchestrator.populate_form()
        validation = orchestrator.validate_form(form)

        # Should warn about deficit
        assert any('deficit' in w.lower() for w in validation['details']['warnings'])

    def test_validate_strategic_high_contribution_dependence(self, orchestrator, sample_organization_data,
                                                             sample_governance_data, sample_program_data):
        """Test strategic validation notes high reliance on contributions."""
        # Financial data with 80% contribution dependence
        high_contrib_financial = {
            'revenue': {'contributions': 80000, 'program_service_revenue': 20000,
                       'investment_income': 0, 'other': 0, 'total': 100000},
            'expenses': {'program_services': 70000, 'management_general': 20000,
                        'fundraising': 10000, 'total': 100000},
            'balance_sheet': {
                'beginning': {'cash': 50000, 'other_assets': 50000, 'total_assets': 100000,
                             'liabilities': 20000, 'net_assets': 80000},
                'ending': {'cash': 50000, 'other_assets': 50000, 'total_assets': 100000,
                          'liabilities': 20000, 'net_assets': 80000}
            },
            'net_income': 0,
        }

        orchestrator.organization_data = sample_organization_data
        orchestrator.financial_data = high_contrib_financial
        orchestrator.governance_data = sample_governance_data
        orchestrator.program_data = sample_program_data

        form = orchestrator.populate_form()
        validation = orchestrator.validate_form(form)

        # Should provide info about contribution dependence
        assert any('reliance on contributions' in i.lower() or 'diversification' in i.lower()
                  for i in validation['details']['info'])


# ============================================================================
# PHASE 5: FILING PACKAGE GENERATION TESTS
# ============================================================================

@pytest.mark.unit
class TestFilingPackage:
    """Tests for Phase 5: Filing Package Generation."""

    def test_generate_filing_package_structure(self, orchestrator, sample_organization_data,
                                               sample_financial_data, sample_governance_data, sample_program_data):
        """Test filing package contains all required components."""
        orchestrator.organization_data = sample_organization_data
        orchestrator.financial_data = sample_financial_data
        orchestrator.governance_data = sample_governance_data
        orchestrator.program_data = sample_program_data

        form = orchestrator.populate_form()
        validation = orchestrator.validate_form(form)
        package = orchestrator.generate_filing_package(form, validation)

        assert 'form_990ez' in package
        assert 'validation_report' in package
        assert 'schedules' in package
        assert 'filing_checklist' in package
        assert 'executive_summary' in package

    def test_generate_filing_package_schedule_a_required_501c3(self, orchestrator, sample_organization_data,
                                                               sample_financial_data, sample_governance_data, sample_program_data):
        """Test that Schedule A is required for 501(c)(3) organizations."""
        orchestrator.organization_data = sample_organization_data  # 501(c)(3)
        orchestrator.financial_data = sample_financial_data
        orchestrator.governance_data = sample_governance_data
        orchestrator.program_data = sample_program_data

        form = orchestrator.populate_form()
        validation = orchestrator.validate_form(form)
        package = orchestrator.generate_filing_package(form, validation)

        assert package['schedules'].get('schedule_a') is True

    def test_generate_filing_package_executive_summary(self, orchestrator, sample_organization_data,
                                                      sample_financial_data, sample_governance_data, sample_program_data):
        """Test executive summary contains key financial information."""
        orchestrator.organization_data = sample_organization_data
        orchestrator.financial_data = sample_financial_data
        orchestrator.governance_data = sample_governance_data
        orchestrator.program_data = sample_program_data

        form = orchestrator.populate_form()
        validation = orchestrator.validate_form(form)
        package = orchestrator.generate_filing_package(form, validation)

        summary = package['executive_summary']
        assert summary['organization'] == 'Test Nonprofit Organization'
        assert summary['tax_year'] == 2024
        assert summary['total_revenue'] == 150000.00
        assert summary['total_expenses'] == 125000.00
        assert summary['net_income'] == 25000.00

    def test_generate_checklist_items(self, orchestrator, sample_organization_data,
                                     sample_financial_data, sample_governance_data, sample_program_data):
        """Test that filing checklist contains all required items."""
        orchestrator.organization_data = sample_organization_data
        orchestrator.financial_data = sample_financial_data
        orchestrator.governance_data = sample_governance_data
        orchestrator.program_data = sample_program_data

        form = orchestrator.populate_form()
        validation = orchestrator.validate_form(form)
        package = orchestrator.generate_filing_package(form, validation)

        checklist = package['filing_checklist']
        assert isinstance(checklist, list)
        assert len(checklist) > 0
        assert any('signatures' in item.lower() for item in checklist)
        assert any('accuracy' in item.lower() for item in checklist)


# ============================================================================
# INTEGRATION TESTS
# ============================================================================

@pytest.mark.integration
@pytest.mark.financial
@pytest.mark.compliance
class TestEndToEndWorkflow:
    """Integration tests for complete 990-EZ preparation workflow."""

    def test_complete_workflow_eligible_organization(self, orchestrator, sample_organization_data,
                                                     sample_financial_data, sample_governance_data, sample_program_data):
        """Test complete workflow from eligibility through filing package."""
        # Phase 1: Eligibility
        eligible, _ = orchestrator.verify_eligibility(
            gross_receipts=sample_financial_data['revenue']['total'],
            total_assets=sample_financial_data['balance_sheet']['ending']['total_assets']
        )
        assert eligible is True

        # Phase 2: Data Collection
        orchestrator.organization_data = sample_organization_data
        orchestrator.financial_data = sample_financial_data
        orchestrator.governance_data = sample_governance_data
        orchestrator.program_data = sample_program_data

        # Phase 3: Form Population
        form = orchestrator.populate_form()
        assert 'part_i' in form

        # Phase 4: Validation
        validation = orchestrator.validate_form(form)
        assert validation['filing_ready'] is True

        # Phase 5: Filing Package
        package = orchestrator.generate_filing_package(form, validation)
        assert package['form_990ez'] == form
        assert package['validation_report'] == validation

    def test_complete_workflow_ineligible_organization(self, orchestrator):
        """Test workflow stops for ineligible organization."""
        # Phase 1: Eligibility - should fail
        eligible, reason = orchestrator.verify_eligibility(
            gross_receipts=250000.00,  # Above threshold
            total_assets=100000.00
        )

        assert eligible is False
        assert reason is not None
        # Workflow should stop here - organization must file Form 990 instead


# ============================================================================
# EDGE CASES AND ERROR HANDLING
# ============================================================================

@pytest.mark.unit
class TestEdgeCases:
    """Tests for edge cases and error handling."""

    def test_config_file_not_found_returns_empty_dict(self, temp_config_dir):
        """Test graceful handling of missing config files."""
        # Remove one config file
        os.remove(temp_config_dir + "validation-rules.yaml")

        orchestrator = Form990EZOrchestrator(config_path=temp_config_dir)

        # Should create orchestrator with empty validation rules
        assert orchestrator.validation_rules == {}

    def test_zero_revenue_and_expenses(self, orchestrator, sample_organization_data, sample_governance_data):
        """Test handling of organization with zero revenue and expenses."""
        zero_financial = {
            'revenue': {'contributions': 0, 'program_service_revenue': 0,
                       'investment_income': 0, 'other': 0, 'total': 0},
            'expenses': {'program_services': 0, 'management_general': 0,
                        'fundraising': 0, 'total': 0},
            'balance_sheet': {
                'beginning': {'cash': 10000, 'other_assets': 0, 'total_assets': 10000,
                             'liabilities': 0, 'net_assets': 10000},
                'ending': {'cash': 10000, 'other_assets': 0, 'total_assets': 10000,
                          'liabilities': 0, 'net_assets': 10000}
            },
            'net_income': 0,
        }

        orchestrator.organization_data = sample_organization_data
        orchestrator.financial_data = zero_financial
        orchestrator.governance_data = sample_governance_data
        orchestrator.program_data = []

        form = orchestrator.populate_form()
        validation = orchestrator.validate_form(form)

        # Should not crash, should validate mathematically
        assert validation['errors'] == 0

    def test_no_officers(self, orchestrator, sample_organization_data, sample_financial_data, sample_program_data):
        """Test handling of organization with no officers listed."""
        governance_no_officers = {
            'officers': [],
            'policies': {'conflict_of_interest': True, 'whistleblower': False, 'document_retention': False}
        }

        orchestrator.organization_data = sample_organization_data
        orchestrator.financial_data = sample_financial_data
        orchestrator.governance_data = governance_no_officers
        orchestrator.program_data = sample_program_data

        form = orchestrator.populate_form()
        part_i = form['part_i']

        # Officer compensation should be 0
        assert part_i['line_11b'] == 0.00

    def test_no_programs(self, orchestrator, sample_organization_data, sample_financial_data, sample_governance_data):
        """Test handling of organization with no programs listed."""
        orchestrator.organization_data = sample_organization_data
        orchestrator.financial_data = sample_financial_data
        orchestrator.governance_data = sample_governance_data
        orchestrator.program_data = []

        form = orchestrator.populate_form()
        part_iii = form['part_iii']

        # Programs should be empty list
        assert part_iii == []


# ============================================================================
# PARAMETRIZED TESTS FOR THRESHOLD BOUNDARIES
# ============================================================================

@pytest.mark.unit
@pytest.mark.financial
@pytest.mark.parametrize("gross_receipts,total_assets,expected_eligible", [
    (0.00, 0.00, True),
    (100000.00, 100000.00, True),
    (199999.99, 499999.99, True),
    (200000.00, 100000.00, False),  # At threshold
    (100000.00, 500000.00, False),  # At threshold
    (200000.01, 100000.00, False),  # Just over
    (100000.00, 500000.01, False),  # Just over
    (250000.00, 600000.00, False),  # Both over
])
def test_eligibility_threshold_boundaries(orchestrator, gross_receipts, total_assets, expected_eligible):
    """Test eligibility verification at various threshold boundaries."""
    eligible, _ = orchestrator.verify_eligibility(gross_receipts, total_assets)
    assert eligible == expected_eligible


# ============================================================================
# INTERACTIVE METHOD TESTS
# ============================================================================

@pytest.mark.unit
class TestInteractiveMethods:
    """Tests for interactive data collection methods."""

    def test_check_eligibility_interactive_eligible(self, orchestrator):
        """Test interactive eligibility check with eligible organization."""
        with patch('builtins.input', side_effect=['150000', '400000', 'no', 'no']):
            with patch('builtins.print') as mock_print:
                result = orchestrator.check_eligibility_interactive()

                assert result is True
                # Verify success message was printed
                assert any('QUALIFIES FOR FORM 990-EZ' in str(call) for call in mock_print.call_args_list)

    def test_check_eligibility_interactive_ineligible_receipts(self, orchestrator):
        """Test interactive eligibility check with ineligible organization (high receipts)."""
        with patch('builtins.input', side_effect=['250000', '100000', 'no', 'no']):
            with patch('builtins.print') as mock_print:
                result = orchestrator.check_eligibility_interactive()

                assert result is False
                # Verify failure message was printed
                assert any('DOES NOT QUALIFY' in str(call) for call in mock_print.call_args_list)

    def test_check_eligibility_interactive_ineligible_assets(self, orchestrator):
        """Test interactive eligibility check with ineligible organization (high assets)."""
        with patch('builtins.input', side_effect=['100000', '600000', 'no', 'no']):
            with patch('builtins.print') as mock_print:
                result = orchestrator.check_eligibility_interactive()

                assert result is False
                assert any('DOES NOT QUALIFY' in str(call) for call in mock_print.call_args_list)

    def test_check_eligibility_interactive_donor_advised_fund(self, orchestrator):
        """Test interactive eligibility check with donor advised fund."""
        with patch('builtins.input', side_effect=['100000', '200000', 'yes', 'no']):
            with patch('builtins.print') as mock_print:
                result = orchestrator.check_eligibility_interactive()

                assert result is False
                assert any('donor advised fund' in str(call).lower() for call in mock_print.call_args_list)

    def test_check_eligibility_interactive_hospital(self, orchestrator):
        """Test interactive eligibility check with hospital operator."""
        with patch('builtins.input', side_effect=['100000', '200000', 'no', 'yes']):
            with patch('builtins.print') as mock_print:
                result = orchestrator.check_eligibility_interactive()

                assert result is False
                assert any('hospital' in str(call).lower() for call in mock_print.call_args_list)

    def test_check_eligibility_interactive_invalid_input(self, orchestrator):
        """Test interactive eligibility check with invalid input."""
        with patch('builtins.input', side_effect=['invalid', '100000', 'no', 'no']):
            with patch('builtins.print') as mock_print:
                result = orchestrator.check_eligibility_interactive()

                assert result is False
                # Should show error message
                assert any('Error' in str(call) or 'valid' in str(call) for call in mock_print.call_args_list)

    def test_collect_organization_info(self, orchestrator):
        """Test interactive organization information collection."""
        test_inputs = [
            'Test Nonprofit Org',
            '12-3456789',
            '2024',
            '12/31/2024',
            '501(c)(3)'
        ]

        with patch('builtins.input', side_effect=test_inputs):
            with patch('builtins.print'):
                result = orchestrator.collect_organization_info()

                assert result['legal_name'] == 'Test Nonprofit Org'
                assert result['ein'] == '12-3456789'
                assert result['tax_year'] == 2024
                assert result['fiscal_year_end'] == '12/31/2024'
                assert result['classification'] == '501(c)(3)'
                assert orchestrator.organization_data == result

    def test_collect_financial_data_manual_entry(self, orchestrator):
        """Test interactive financial data collection with manual entry."""
        test_inputs = [
            '100000',  # contributions
            '40000',   # program service revenue
            '5000',    # investment income
            '5000',    # other revenue
            '90000',   # program services expenses
            '25000',   # management & general
            '10000',   # fundraising
            '50000',   # beginning cash
            '150000',  # beginning other assets
            '50000',   # beginning liabilities
            '60000',   # ending cash
            '165000',  # ending other assets
            '50000',   # ending liabilities
        ]

        with patch('builtins.input', side_effect=test_inputs):
            with patch('builtins.print'):
                result = orchestrator.collect_financial_data(use_manual_entry=True)

                assert result['revenue']['contributions'] == 100000
                assert result['revenue']['total'] == 150000
                assert result['expenses']['total'] == 125000
                assert result['net_income'] == 25000
                assert orchestrator.financial_data == result

    def test_collect_financial_data_api_fallback(self, orchestrator):
        """Test financial data collection falls back to manual when API not available."""
        test_inputs = [
            '100000', '40000', '5000', '5000',
            '90000', '25000', '10000',
            '50000', '150000', '50000',
            '60000', '165000', '50000',
        ]

        with patch('builtins.input', side_effect=test_inputs):
            with patch('builtins.print') as mock_print:
                result = orchestrator.collect_financial_data(use_manual_entry=False)

                # Should print message about API not implemented
                assert any('not yet implemented' in str(call).lower() or 'manual' in str(call).lower()
                          for call in mock_print.call_args_list)
                assert result is not None

    def test_collect_financial_data_low_program_ratio_warning(self, orchestrator):
        """Test that low program ratio triggers warning during financial collection."""
        test_inputs = [
            '100000',  # contributions
            '0',       # program service revenue
            '0',       # investment income
            '0',       # other revenue
            '50000',   # program services expenses (50% - below 65%)
            '40000',   # management & general
            '10000',   # fundraising
            '50000',   # beginning cash
            '50000',   # beginning other assets
            '20000',   # beginning liabilities
            '50000',   # ending cash
            '50000',   # ending other assets
            '20000',   # ending liabilities
        ]

        with patch('builtins.input', side_effect=test_inputs):
            with patch('builtins.print') as mock_print:
                result = orchestrator.collect_financial_data(use_manual_entry=True)

                # Should warn about program ratio below 65%
                assert any('Warning' in str(call) or 'below' in str(call)
                          for call in mock_print.call_args_list)

    def test_collect_program_data_multiple_programs(self, orchestrator):
        """Test interactive program data collection with multiple programs."""
        test_inputs = [
            'yes',  # Add program 1
            'Educational workshops for 500 underserved youth with 85% improvement in literacy',
            '60000',
            '10000',
            'yes',  # Add program 2
            'Food bank serving 200 families monthly distributing 50000 pounds of food',
            '30000',
            '5000',
            'no',   # Don't add program 3
        ]

        with patch('builtins.input', side_effect=test_inputs):
            with patch('builtins.print'):
                result = orchestrator.collect_program_data()

                assert len(result) == 2
                assert result[0]['number'] == 1
                assert result[0]['expenses'] == 60000
                assert result[1]['number'] == 2
                assert result[1]['expenses'] == 30000
                assert orchestrator.program_data == result

    def test_collect_program_data_no_programs(self, orchestrator):
        """Test interactive program data collection with no programs."""
        test_inputs = ['no']  # Don't add any programs

        with patch('builtins.input', side_effect=test_inputs):
            with patch('builtins.print'):
                result = orchestrator.collect_program_data()

                assert len(result) == 0
                assert orchestrator.program_data == []

    def test_collect_program_data_one_program_then_stop(self, orchestrator):
        """Test program data collection that stops after one program."""
        test_inputs = [
            'yes',  # Add program 1
            'Community health screenings for 1000 residents with early detection of diabetes',
            '75000',
            '15000',
            'no',   # Don't add program 2
        ]

        with patch('builtins.input', side_effect=test_inputs):
            with patch('builtins.print'):
                result = orchestrator.collect_program_data()

                assert len(result) == 1
                assert result[0]['number'] == 1

    def test_collect_governance_data_with_officers(self, orchestrator):
        """Test interactive governance data collection with officers."""
        test_inputs = [
            'yes',   # Add officer 1
            'Jane Doe',
            'Executive Director',
            '40',
            '75000',
            'yes',   # Add officer 2
            'John Smith',
            'Board Chair',
            '5',
            '0',
            'no',    # No more officers
            'yes',   # Conflict of interest policy
            'yes',   # Whistleblower policy
            'no',    # No document retention policy
        ]

        with patch('builtins.input', side_effect=test_inputs):
            with patch('builtins.print'):
                result = orchestrator.collect_governance_data()

                assert len(result['officers']) == 2
                assert result['officers'][0]['name'] == 'Jane Doe'
                assert result['officers'][0]['compensation'] == 75000
                assert result['officers'][1]['name'] == 'John Smith'
                assert result['officers'][1]['compensation'] == 0
                assert result['policies']['conflict_of_interest'] is True
                assert result['policies']['whistleblower'] is True
                assert result['policies']['document_retention'] is False
                assert orchestrator.governance_data == result

    def test_collect_governance_data_no_officers(self, orchestrator):
        """Test governance data collection with no officers."""
        test_inputs = [
            'no',    # No officers
            'yes',   # Conflict of interest policy
            'no',    # No whistleblower policy
            'yes',   # Document retention policy
        ]

        with patch('builtins.input', side_effect=test_inputs):
            with patch('builtins.print'):
                result = orchestrator.collect_governance_data()

                assert len(result['officers']) == 0
                assert result['policies']['conflict_of_interest'] is True
                assert result['policies']['whistleblower'] is False
                assert result['policies']['document_retention'] is True

    def test_main_function_eligible_complete_workflow(self, temp_config_dir):
        """Test main() function with complete workflow for eligible organization."""
        test_inputs = [
            # Eligibility check (4 inputs)
            '150000', '400000', 'no', 'no',
            # Press Enter to continue to data collection (1 input)
            '',
            # Organization info (5 inputs)
            'Test Org', '12-3456789', '2024', '12/31/2024', '501(c)(3)',
            # Financial data (13 inputs)
            '100000', '40000', '5000', '5000',
            '90000', '25000', '10000',
            '50000', '150000', '50000',
            '60000', '165000', '50000',
            # Program data (5 inputs)
            'yes', 'Educational program for youth with measurable outcomes', '60000', '10000', 'no',
            # Governance data (9 inputs)
            'yes', 'Jane Doe', 'Executive Director', '40', '75000', 'no',
            'yes', 'yes', 'yes',
            # Press Enter to generate form (1 input)
            '',
            # Press Enter to validate (1 input)
            '',
            # Press Enter to generate filing package (1 input)
            '',
        ]

        with patch('builtins.input', side_effect=test_inputs):
            with patch('builtins.print') as mock_print:
                # Mock Form990EZOrchestrator to use test config
                with patch('orchestrator.Form990EZOrchestrator') as mock_orch_class:
                    mock_orch = Form990EZOrchestrator(config_path=temp_config_dir)
                    mock_orch_class.return_value = mock_orch

                    from orchestrator import main
                    main()

                    # Verify completion message
                    assert any('COMPLETE' in str(call) for call in mock_print.call_args_list)

    def test_main_function_ineligible_organization(self, temp_config_dir):
        """Test main() function with ineligible organization."""
        test_inputs = [
            '250000',  # High gross receipts
            '100000',
            'no',
            'no',
        ]

        with patch('builtins.input', side_effect=test_inputs):
            with patch('builtins.print') as mock_print:
                # Mock Form990EZOrchestrator to use test config
                with patch('orchestrator.Form990EZOrchestrator') as mock_orch_class:
                    mock_orch = Form990EZOrchestrator(config_path=temp_config_dir)
                    mock_orch_class.return_value = mock_orch

                    from orchestrator import main
                    main()

                    # Should exit early with message about Form 990
                    assert any('must file form 990' in str(call).lower() or 'exiting' in str(call).lower()
                              for call in mock_print.call_args_list)

    def test_main_function_complete_workflow_alternative(self, temp_config_dir):
        """Test main() function with complete workflow (alternative data)."""
        test_inputs = [
            # Eligibility check (4 inputs)
            '150000', '400000', 'no', 'no',
            # Press Enter to data collection (1 input)
            '',
            # Organization info (5 inputs)
            'Test Org', '12-3456789', '2024', '12/31/2024', '501(c)(3)',
            # Financial data (13 inputs)
            '100000', '0', '0', '0',
            '90000', '10000', '0',
            '50000', '50000', '10000',  # Beginning: Assets=100k, Liab=10k, Net=90k
            '60000', '60000', '10000',  # Ending: Assets=120k, Liab=10k, Net=110k
            # Program data (1 input - no programs)
            'no',
            # Governance data (4 inputs - no officers)
            'no', 'yes', 'yes', 'yes',
            # Press Enter to generate form (1 input)
            '',
            # Press Enter to validate (1 input)
            '',
            # Press Enter to generate filing package (1 input) - form is valid
            '',
        ]

        with patch('builtins.input', side_effect=test_inputs):
            with patch('builtins.print') as mock_print:
                # Mock Form990EZOrchestrator to use test config
                with patch('orchestrator.Form990EZOrchestrator') as mock_orch_class:
                    mock_orch = Form990EZOrchestrator(config_path=temp_config_dir)
                    mock_orch_class.return_value = mock_orch

                    from orchestrator import main
                    main()

                    # Verify completion message
                    assert any('COMPLETE' in str(call) for call in mock_print.call_args_list)

    def test_main_function_with_validation_errors(self, temp_config_dir):
        """Test main() function when form has validation errors."""
        test_inputs = [
            # Eligibility check (4 inputs)
            '150000', '400000', 'no', 'no',
            # Press Enter to data collection (1 input)
            '',
            # Organization info (5 inputs)
            'Test Org', '12-3456789', '2024', '12/31/2024', '501(c)(3)',
            # Financial data with INCORRECT totals that will cause validation errors (13 inputs)
            '100000', '40000', '5000', '5000',  # These sum to 150000
            '90000', '25000', '10000',          # These sum to 125000
            '50000', '150000', '50000',         # Beginning
            '60000', '165000', '50000',         # Ending
            # Program data (1 input)
            'no',
            # Governance data (4 inputs)
            'no', 'yes', 'yes', 'yes',
            # Press Enter to generate form (1 input)
            '',
            # Press Enter to validate (1 input)
            '',
            # No filing package prompt since form has errors
        ]

        with patch('builtins.input', side_effect=test_inputs):
            with patch('builtins.print') as mock_print:
                # Mock Form990EZOrchestrator to use test config
                with patch('orchestrator.Form990EZOrchestrator') as mock_orch_class:
                    mock_orch = Form990EZOrchestrator(config_path=temp_config_dir)
                    # Force validation to fail by making validate_form return errors
                    original_validate = mock_orch.validate_form

                    def failing_validate(form):
                        result = original_validate(form)
                        # Force an error
                        result['errors'] = 1
                        result['filing_ready'] = False
                        result['details']['errors'] = ['Test validation error']
                        return result

                    mock_orch.validate_form = failing_validate
                    mock_orch_class.return_value = mock_orch

                    from orchestrator import main
                    main()

                    # Verify error message was shown
                    assert any('FORM HAS ERRORS' in str(call) or 'CANNOT FILE' in str(call)
                              for call in mock_print.call_args_list)


# ============================================================================
# ADDITIONAL VALIDATION EDGE CASES
# ============================================================================

@pytest.mark.unit
@pytest.mark.financial
class TestValidationEdgeCases:
    """Additional tests for validation edge cases to improve coverage."""

    def test_validate_mathematical_revenue_sum_incorrect(self, orchestrator, sample_organization_data,
                                                         sample_governance_data, sample_program_data):
        """Test mathematical validation catches incorrect revenue sums."""
        # Create financial data with incorrect total
        bad_financial = {
            'revenue': {
                'contributions': 100000,
                'program_service_revenue': 40000,
                'investment_income': 5000,
                'other': 5000,
                'total': 140000,  # Wrong! Should be 150000
            },
            'expenses': {
                'program_services': 90000,
                'management_general': 25000,
                'fundraising': 10000,
                'total': 125000,
            },
            'balance_sheet': {
                'beginning': {'cash': 50000, 'other_assets': 150000, 'total_assets': 200000,
                             'liabilities': 50000, 'net_assets': 150000},
                'ending': {'cash': 60000, 'other_assets': 155000, 'total_assets': 215000,
                          'liabilities': 50000, 'net_assets': 165000}
            },
            'net_income': 15000,
        }

        orchestrator.organization_data = sample_organization_data
        orchestrator.financial_data = bad_financial
        orchestrator.governance_data = sample_governance_data
        orchestrator.program_data = sample_program_data

        form = orchestrator.populate_form()
        validation = orchestrator.validate_form(form)

        # Should have error about revenue not summing correctly
        assert validation['errors'] > 0
        assert any('revenue' in e.lower() for e in validation['details']['errors'])

    def test_validate_mathematical_balance_sheet_imbalanced(self, orchestrator, sample_organization_data,
                                                            sample_governance_data, sample_program_data):
        """Test mathematical validation catches imbalanced balance sheet."""
        # Create financial data with imbalanced balance sheet
        imbalanced_financial = {
            'revenue': {'contributions': 100000, 'program_service_revenue': 0,
                       'investment_income': 0, 'other': 0, 'total': 100000},
            'expenses': {'program_services': 90000, 'management_general': 10000,
                        'fundraising': 0, 'total': 100000},
            'balance_sheet': {
                'beginning': {'cash': 50000, 'other_assets': 50000, 'total_assets': 100000,
                             'liabilities': 20000, 'net_assets': 80000},
                'ending': {'cash': 60000, 'other_assets': 50000, 'total_assets': 110000,
                          'liabilities': 20000, 'net_assets': 100000}  # Imbalanced: 110 ≠ 20 + 100
            },
            'net_income': 0,
        }

        orchestrator.organization_data = sample_organization_data
        orchestrator.financial_data = imbalanced_financial
        orchestrator.governance_data = sample_governance_data
        orchestrator.program_data = sample_program_data

        form = orchestrator.populate_form()
        validation = orchestrator.validate_form(form)

        # Should have error about balance sheet not balancing
        assert validation['errors'] > 0
        assert any('balance sheet' in e.lower() for e in validation['details']['errors'])

    def test_validate_mathematical_part_i_part_ii_mismatch(self, orchestrator, sample_organization_data,
                                                           sample_governance_data, sample_program_data):
        """Test validation catches mismatch between Part I and Part II net assets."""
        # Create financial data where Part I and Part II won't reconcile
        mismatch_financial = {
            'revenue': {'contributions': 100000, 'program_service_revenue': 0,
                       'investment_income': 0, 'other': 0, 'total': 100000},
            'expenses': {'program_services': 90000, 'management_general': 10000,
                        'fundraising': 0, 'total': 100000},
            'balance_sheet': {
                'beginning': {'cash': 50000, 'other_assets': 50000, 'total_assets': 100000,
                             'liabilities': 20000, 'net_assets': 80000},
                'ending': {'cash': 50000, 'other_assets': 50000, 'total_assets': 100000,
                          'liabilities': 20000, 'net_assets': 80000}  # No change, but net income is 0
            },
            'net_income': 0,
        }

        orchestrator.organization_data = sample_organization_data
        orchestrator.financial_data = mismatch_financial
        orchestrator.governance_data = sample_governance_data
        orchestrator.program_data = sample_program_data

        form = orchestrator.populate_form()
        validation = orchestrator.validate_form(form)

        # Part I should show ending net assets = 80k (beginning) + 0 (net income) = 80k
        # This should match Part II, so no error expected
        # But if we force a mismatch by changing Part I line 21:
        form['part_i']['line_21'] = 90000  # Force mismatch

        validation = orchestrator.validate_form(form)

        # Should have error about Part I/II mismatch
        assert validation['errors'] > 0
        assert any('part i' in e.lower() and 'part ii' in e.lower() for e in validation['details']['errors'])

    def test_validate_with_missing_whistleblower_policy(self, orchestrator, sample_organization_data,
                                                        sample_financial_data, sample_program_data):
        """Test that missing whistleblower policy generates info message."""
        governance_no_whistleblower = {
            'officers': [{'name': 'Test', 'title': 'Director', 'hours_per_week': 10, 'compensation': 0}],
            'policies': {
                'conflict_of_interest': True,
                'whistleblower': False,
                'document_retention': True,
            }
        }

        orchestrator.organization_data = sample_organization_data
        orchestrator.financial_data = sample_financial_data
        orchestrator.governance_data = governance_no_whistleblower
        orchestrator.program_data = sample_program_data

        form = orchestrator.populate_form()
        validation = orchestrator.validate_form(form)

        # Should have info message about whistleblower policy
        assert any('whistleblower' in i.lower() for i in validation['details']['info'])
