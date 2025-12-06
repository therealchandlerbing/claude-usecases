"""
Test Data Factories

Provides Faker-based factories for generating realistic test data
across different skill domains.

Usage:
    from tests.factories import FinancialDataFactory, PersonaDataFactory

    # Generate 990-eligible organization
    factory = FinancialDataFactory()
    org_data = factory.create_990_eligible()

    # Generate stakeholder data
    persona_factory = PersonaDataFactory()
    stakeholder = persona_factory.create_stakeholder()
"""

from tests.factories.financial import FinancialDataFactory
from tests.factories.persona import PersonaDataFactory
from tests.factories.organization import OrganizationDataFactory
from tests.factories.project import ProjectDataFactory

__all__ = [
    "FinancialDataFactory",
    "PersonaDataFactory",
    "OrganizationDataFactory",
    "ProjectDataFactory",
]
