"""
Integration Tests for Multi-Skill Workflows

Tests realistic scenarios where multiple skills work together:
1. Executive Intelligence → Dashboard Update
2. Research → Persona Builder → Portfolio
3. Financial Data → 990-EZ → Board Prep

These tests use the test data factories and shared utilities.
"""

import pytest
from typing import Dict, Any
from pathlib import Path

# Import test factories
from tests.factories import (
    FinancialDataFactory,
    PersonaDataFactory,
    OrganizationDataFactory,
    ProjectDataFactory,
)

# Import shared utilities
from shared.config_loader import ConfigLoader, ConfigurationError
from shared.base_orchestrator import BaseOrchestrator


# =============================================================================
# Test Fixtures
# =============================================================================


@pytest.fixture
def financial_factory():
    """Seeded financial data factory for reproducible tests."""
    return FinancialDataFactory(seed=42)


@pytest.fixture
def persona_factory():
    """Seeded persona data factory for reproducible tests."""
    return PersonaDataFactory(seed=42)


@pytest.fixture
def org_factory():
    """Seeded organization data factory for reproducible tests."""
    return OrganizationDataFactory(seed=42)


@pytest.fixture
def project_factory():
    """Seeded project data factory for reproducible tests."""
    return ProjectDataFactory(seed=42)


# =============================================================================
# Mock Orchestrators for Testing
# =============================================================================


class MockIntelligenceExtractor(BaseOrchestrator):
    """Mock intelligence extractor for testing workflows."""

    def _get_default_config(self) -> Dict[str, Any]:
        return {"extraction_mode": "standard"}

    def _initialize(self) -> None:
        self.extracted_items = []

    def execute(self, source_data: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """Extract intelligence from source data."""
        # Simulate extraction
        self.extracted_items = [
            {
                "type": "partnership",
                "entity": source_data.get("name", "Unknown"),
                "confidence": 0.85,
                "signals": ["positive sentiment", "growth potential"]
            }
        ]
        self.set_result("extracted_count", len(self.extracted_items))
        return {"items": self.extracted_items, "source": "mock"}


class MockDashboardUpdater(BaseOrchestrator):
    """Mock dashboard updater for testing workflows."""

    def _get_default_config(self) -> Dict[str, Any]:
        return {"update_mode": "incremental"}

    def _initialize(self) -> None:
        self.updates_applied = []

    def execute(self, intelligence_data: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """Update dashboard with intelligence data."""
        items = intelligence_data.get("items", [])
        for item in items:
            self.updates_applied.append({
                "action": "upsert",
                "entity": item.get("entity"),
                "timestamp": "2024-01-01T00:00:00"
            })
        self.set_result("updates_count", len(self.updates_applied))
        return {"updates": self.updates_applied, "status": "success"}


class MockPersonaBuilder(BaseOrchestrator):
    """Mock persona builder for testing workflows."""

    def _get_default_config(self) -> Dict[str, Any]:
        return {"framework": "vianeo"}

    def _initialize(self) -> None:
        self.personas = []

    def execute(self, stakeholder_data: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """Build persona from stakeholder data."""
        persona = {
            "name": stakeholder_data.get("name", "Unknown Persona"),
            "archetype": "The Pragmatist",
            "jobs_to_be_done": ["Achieve goals", "Reduce friction"],
            "pain_points": stakeholder_data.get("pain_points", [])
        }
        self.personas.append(persona)
        self.set_result("persona_count", len(self.personas))
        return {"persona": persona}


class MockFinancialValidator(BaseOrchestrator):
    """Mock financial validator for testing workflows."""

    def _get_default_config(self) -> Dict[str, Any]:
        return {"validation_level": "comprehensive"}

    def _initialize(self) -> None:
        self.validation_results = []

    def execute(self, financial_data: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """Validate financial data."""
        # Check 990-EZ eligibility
        gross_receipts = financial_data.get("financial", {}).get("gross_receipts", 0)
        total_assets = financial_data.get("financial", {}).get("total_assets", 0)

        is_eligible = gross_receipts < 200000 and total_assets < 500000

        result = {
            "eligible_990ez": is_eligible,
            "gross_receipts": gross_receipts,
            "total_assets": total_assets,
            "validation_passed": True
        }

        if not is_eligible:
            self.add_warning(
                "Organization exceeds 990-EZ thresholds",
                code="990EZ_THRESHOLD"
            )

        self.set_result("eligibility", is_eligible)
        return result


# =============================================================================
# Integration Test Classes
# =============================================================================


@pytest.mark.integration
class TestIntelligenceToDashboardWorkflow:
    """
    Test workflow: Intelligence Extraction → Dashboard Update

    Scenario: Extract intelligence from meeting notes, then update
    the partnership dashboard with the findings.
    """

    def test_complete_workflow(self, persona_factory):
        """Test complete intelligence to dashboard workflow."""
        # Step 1: Create source data
        stakeholder = persona_factory.create_stakeholder(stakeholder_type="partner")

        # Step 2: Extract intelligence
        extractor = MockIntelligenceExtractor()
        intelligence = extractor.execute(stakeholder)

        assert intelligence["items"]
        assert extractor.get_result("extracted_count") == 1

        # Step 3: Update dashboard
        updater = MockDashboardUpdater()
        result = updater.execute(intelligence)

        assert result["status"] == "success"
        assert updater.get_result("updates_count") == 1
        assert not updater.has_errors()

    def test_workflow_with_empty_source(self):
        """Test workflow handles empty source data gracefully."""
        extractor = MockIntelligenceExtractor()
        intelligence = extractor.execute({})

        # Should still produce output
        assert "items" in intelligence

        updater = MockDashboardUpdater()
        result = updater.execute(intelligence)

        assert result["status"] == "success"

    def test_workflow_preserves_data_integrity(self, persona_factory):
        """Test that data flows correctly through the workflow."""
        stakeholder = persona_factory.create_stakeholder()
        original_name = stakeholder["name"]

        extractor = MockIntelligenceExtractor()
        intelligence = extractor.execute(stakeholder)

        # Verify name is preserved
        assert intelligence["items"][0]["entity"] == original_name

        updater = MockDashboardUpdater()
        result = updater.execute(intelligence)

        # Verify name flows to dashboard
        assert result["updates"][0]["entity"] == original_name


@pytest.mark.integration
class TestResearchToPortfolioWorkflow:
    """
    Test workflow: Research → Persona Builder → Portfolio

    Scenario: Research stakeholders, build personas, then generate
    portfolio page content.
    """

    def test_stakeholder_to_persona(self, persona_factory):
        """Test converting stakeholder data to persona."""
        stakeholder = persona_factory.create_stakeholder()
        stakeholder["pain_points"] = ["Scaling challenges", "Budget constraints"]

        builder = MockPersonaBuilder()
        result = builder.execute(stakeholder)

        assert result["persona"]["name"] == stakeholder["name"]
        assert result["persona"]["pain_points"] == stakeholder["pain_points"]
        assert builder.get_result("persona_count") == 1

    def test_multiple_personas_workflow(self, persona_factory):
        """Test building multiple personas in sequence."""
        builder = MockPersonaBuilder()

        # Build 3 personas
        for _ in range(3):
            stakeholder = persona_factory.create_stakeholder()
            builder.execute(stakeholder)

        assert builder.get_result("persona_count") == 3
        assert len(builder.personas) == 3

    def test_vianeo_persona_integration(self, persona_factory):
        """Test that Vianeo personas have required fields."""
        vianeo_persona = persona_factory.create_vianeo_persona()

        # Verify Vianeo framework fields
        assert "jobs_to_be_done" in vianeo_persona
        assert "functional" in vianeo_persona["jobs_to_be_done"]
        assert "emotional" in vianeo_persona["jobs_to_be_done"]
        assert "pain_points" in vianeo_persona
        assert "decision_criteria" in vianeo_persona


@pytest.mark.integration
class TestFinancialComplianceWorkflow:
    """
    Test workflow: Financial Data → 990-EZ Validation → Board Prep

    Scenario: Validate financial data for 990-EZ eligibility and
    prepare board meeting materials.
    """

    def test_990_eligible_organization(self, financial_factory):
        """Test workflow with 990-EZ eligible organization."""
        org_data = financial_factory.create_990_eligible()

        validator = MockFinancialValidator()
        result = validator.execute(org_data)

        assert result["eligible_990ez"] is True
        assert result["validation_passed"] is True
        assert not validator.has_warnings()

    def test_990_ineligible_high_receipts(self, financial_factory):
        """Test workflow with organization exceeding receipt threshold."""
        org_data = financial_factory.create_990_ineligible_high_receipts()

        validator = MockFinancialValidator()
        result = validator.execute(org_data)

        assert result["eligible_990ez"] is False
        assert validator.has_warnings()

    def test_990_ineligible_high_assets(self, financial_factory):
        """Test workflow with organization exceeding asset threshold."""
        org_data = financial_factory.create_990_ineligible_high_assets()

        validator = MockFinancialValidator()
        result = validator.execute(org_data)

        assert result["eligible_990ez"] is False
        assert validator.has_warnings()

    def test_financial_data_completeness(self, financial_factory):
        """Test that generated financial data has all required fields."""
        org_data = financial_factory.create_990_eligible()

        # Verify organization fields
        assert "ein" in org_data["organization"]
        assert "name" in org_data["organization"]

        # Verify financial fields
        financial = org_data["financial"]
        assert "gross_receipts" in financial
        assert "total_assets" in financial
        assert "program_expenses" in financial
        assert "total_expenses" in financial

        # Verify governance fields
        governance = org_data["governance"]
        assert "board_members" in governance
        assert "has_conflict_of_interest_policy" in governance


@pytest.mark.integration
class TestProjectWorkflowIntegration:
    """
    Test workflow: Project Creation → Task Management → Workflow Execution

    Scenario: Create project with tasks, simulate workflow execution,
    and verify state transitions.
    """

    def test_project_with_tasks(self, project_factory):
        """Test project creation with tasks."""
        project = project_factory.create_project()

        assert project["tasks"]
        assert project["milestones"]
        assert project["risks"]
        assert project["progress"] >= 0
        assert project["progress"] <= 100

    def test_workflow_execution(self, project_factory):
        """Test workflow instance execution."""
        workflow = project_factory.create_workflow()
        instance = project_factory.create_workflow_instance(workflow["id"])

        assert instance["workflow_id"] == workflow["id"]
        assert instance["step_history"]
        assert instance["current_step"] > 0

    def test_asana_task_format(self, project_factory):
        """Test that mock Asana tasks match API format."""
        task = project_factory.create_asana_task()

        # Verify Asana API format
        assert "gid" in task
        assert "name" in task
        assert "assignee" in task
        assert "projects" in task
        assert "due_on" in task

    def test_intelligence_signal_format(self, project_factory):
        """Test intelligence signal generation."""
        signal = project_factory.create_intelligence_signal()

        assert signal["impact_score"] >= 0
        assert signal["impact_score"] <= 1
        assert signal["confidence"] >= 0
        assert signal["confidence"] <= 1
        assert signal["recommended_actions"]


@pytest.mark.integration
class TestOrganizationWorkflowIntegration:
    """
    Test workflow: Organization → Board → Strategic Plan

    Scenario: Create organization with board and strategic plan,
    then validate for board meeting preparation.
    """

    def test_nonprofit_complete_data(self, org_factory):
        """Test nonprofit creation with all components."""
        org = org_factory.create_nonprofit()

        assert org["programs"]
        assert org["funding_sources"]
        assert org["metrics"]
        assert org["mission_area"]

    def test_board_composition(self, org_factory):
        """Test board creation with proper composition."""
        board = org_factory.create_board(size=9)

        assert len(board) == 9
        titles = [m["title"] for m in board]
        assert "Chair" in titles
        assert "Treasurer" in titles

    def test_strategic_plan_structure(self, org_factory):
        """Test strategic plan has required elements."""
        plan = org_factory.create_strategic_plan()

        assert plan["vision"]
        assert plan["mission"]
        assert plan["strategic_priorities"]
        assert plan["kpis"]

        # Verify KPIs have targets and actuals
        for kpi in plan["kpis"]:
            assert "target" in kpi
            assert "actual" in kpi

    def test_meeting_agenda_workflow(self, org_factory):
        """Test board meeting agenda generation."""
        agenda = org_factory.create_meeting_agenda("board")

        assert agenda["items"]
        assert agenda["materials"]

        total_duration = sum(item["duration"] for item in agenda["items"])
        assert total_duration > 0


# =============================================================================
# Cross-Factory Integration Tests
# =============================================================================


@pytest.mark.integration
class TestCrossFactoryIntegration:
    """Test interactions between different data factories."""

    def test_financial_and_org_consistency(
        self,
        financial_factory,
        org_factory
    ):
        """Test that financial and org data can be combined."""
        financial_data = financial_factory.create_990_eligible()
        org_data = org_factory.create_nonprofit()

        # Combine data
        combined = {
            **org_data,
            "financials": financial_data["financial"],
            "ein": financial_data["organization"]["ein"]
        }

        assert combined["ein"]
        assert combined["programs"]
        assert combined["financials"]

    def test_persona_and_project_integration(
        self,
        persona_factory,
        project_factory
    ):
        """Test combining personas with projects."""
        stakeholders = [
            persona_factory.create_stakeholder() for _ in range(3)
        ]
        project = project_factory.create_project()

        # Assign stakeholders to project
        project["external_stakeholders"] = stakeholders

        assert len(project["external_stakeholders"]) == 3
        assert all("email" in s for s in project["external_stakeholders"])

    def test_reproducibility_with_seed(self):
        """Test that seeded factories produce reproducible data."""
        factory1 = FinancialDataFactory(seed=12345)
        factory2 = FinancialDataFactory(seed=12345)

        data1 = factory1.create_990_eligible()
        data2 = factory2.create_990_eligible()

        # Should produce identical data with same seed
        assert data1["financial"]["gross_receipts"] == data2["financial"]["gross_receipts"]
