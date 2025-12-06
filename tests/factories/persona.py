"""
Persona Data Factory

Generates realistic persona and stakeholder data for testing
strategic persona builder, CEO advisor, and sales automation skills.
"""

import random
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional

try:
    from faker import Faker
    HAS_FAKER = True
except ImportError:
    HAS_FAKER = False


class PersonaDataFactory:
    """Factory for generating persona and stakeholder test data."""

    INDUSTRIES = [
        "Technology", "Healthcare", "Education", "Finance",
        "Manufacturing", "Retail", "Energy", "Government"
    ]

    PAIN_POINTS = [
        "Difficulty scaling operations",
        "High customer acquisition costs",
        "Talent retention challenges",
        "Legacy system integration",
        "Regulatory compliance burden",
        "Data silos across departments"
    ]

    GOALS = [
        "Increase market share by 20%",
        "Reduce operational costs",
        "Improve customer satisfaction",
        "Accelerate digital transformation",
        "Expand into new markets",
        "Build strategic partnerships"
    ]

    def __init__(self, seed: Optional[int] = None):
        """Initialize the factory with optional seed."""
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
        if self.fake:
            return self.fake.name()
        return self._rng.choice(["Alex Chen", "Sarah Johnson", "Michael Brown", "Emily Davis"])

    def _random_email(self, name: str) -> str:
        if self.fake:
            return self.fake.email()
        clean_name = name.lower().replace(" ", ".")
        return f"{clean_name}@example.com"

    def _random_company(self) -> str:
        if self.fake:
            return self.fake.company()
        return self._rng.choice(["Acme Corp", "TechStart Inc", "Global Partners", "Innovation Labs"])

    def create_stakeholder(
        self,
        stakeholder_type: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Create a stakeholder persona.

        Args:
            stakeholder_type: Type of stakeholder (partner, funder, client, etc.)
        """
        name = self._random_name()
        company = self._random_company()

        return {
            "id": f"stk_{self._rng.randint(1000, 9999)}",
            "name": name,
            "email": self._random_email(name),
            "company": company,
            "title": self._rng.choice([
                "CEO", "VP of Operations", "Director of Strategy",
                "Chief Innovation Officer", "Head of Partnerships"
            ]),
            "type": stakeholder_type or self._rng.choice([
                "partner", "funder", "client", "advisor", "vendor"
            ]),
            "relationship_strength": self._rng.randint(1, 10),
            "engagement_score": round(self._rng.uniform(0, 1), 2),
            "last_contact": (datetime.now() - timedelta(days=self._rng.randint(1, 90))).isoformat(),
            "preferred_channels": self._rng.sample(
                ["email", "phone", "video", "in-person", "slack"],
                k=self._rng.randint(1, 3)
            ),
            "notes": f"Key contact at {company}",
            "tags": self._rng.sample(
                ["strategic", "high-value", "new", "at-risk", "champion"],
                k=self._rng.randint(1, 3)
            )
        }

    def create_vianeo_persona(self) -> Dict[str, Any]:
        """Create a Vianeo-framework persona."""
        name = self._random_name()

        return {
            "persona_id": f"vp_{self._rng.randint(1000, 9999)}",
            "name": name,
            "archetype": self._rng.choice([
                "The Innovator", "The Pragmatist", "The Visionary",
                "The Operator", "The Change Agent"
            ]),
            "demographic": {
                "age_range": self._rng.choice(["25-34", "35-44", "45-54", "55-64"]),
                "role_level": self._rng.choice(["C-Suite", "VP", "Director", "Manager"]),
                "industry": self._rng.choice(self.INDUSTRIES),
                "company_size": self._rng.choice(["1-50", "51-200", "201-1000", "1000+"])
            },
            "jobs_to_be_done": {
                "functional": self._rng.sample(self.GOALS, k=2),
                "emotional": [
                    "Feel confident in strategic decisions",
                    "Reduce stress from uncertainty"
                ],
                "social": [
                    "Be seen as an innovative leader",
                    "Build trust with stakeholders"
                ]
            },
            "pain_points": self._rng.sample(self.PAIN_POINTS, k=3),
            "gains": self._rng.sample(self.GOALS, k=2),
            "decision_criteria": {
                "price_sensitivity": self._rng.choice(["low", "medium", "high"]),
                "risk_tolerance": self._rng.choice(["conservative", "moderate", "aggressive"]),
                "decision_speed": self._rng.choice(["fast", "moderate", "slow"])
            },
            "information_sources": self._rng.sample(
                ["industry reports", "peer recommendations", "conferences",
                 "linkedin", "podcasts", "newsletters"],
                k=3
            ),
            "quote": f"As a leader in {self._rng.choice(self.INDUSTRIES)}, I need solutions that scale."
        }

    def create_empathy_map(self) -> Dict[str, Any]:
        """Create an empathy map for persona development."""
        return {
            "says": [
                "We need to move faster",
                "Budget is always a concern",
                "I need to see proven results"
            ],
            "thinks": [
                "Is this worth the investment?",
                "How will this affect my team?",
                "What are the risks?"
            ],
            "does": [
                "Researches competitors",
                "Consults with peers",
                "Requests case studies"
            ],
            "feels": [
                "Pressure to deliver results",
                "Excitement about new opportunities",
                "Concern about implementation"
            ],
            "pain_points": self._rng.sample(self.PAIN_POINTS, k=2),
            "gains": self._rng.sample(self.GOALS, k=2)
        }

    def create_relationship_history(
        self,
        stakeholder_id: str,
        num_interactions: int = 5
    ) -> List[Dict[str, Any]]:
        """Create relationship history for a stakeholder."""
        interactions = []
        base_date = datetime.now() - timedelta(days=180)

        interaction_types = [
            ("email", "Sent proposal follow-up"),
            ("meeting", "Quarterly business review"),
            ("call", "Strategy discussion"),
            ("event", "Met at industry conference"),
            ("email", "Shared case study")
        ]

        for i in range(num_interactions):
            int_type, description = self._rng.choice(interaction_types)
            date = base_date + timedelta(days=self._rng.randint(0, 180))

            interactions.append({
                "id": f"int_{self._rng.randint(10000, 99999)}",
                "stakeholder_id": stakeholder_id,
                "date": date.isoformat(),
                "type": int_type,
                "description": description,
                "sentiment": self._rng.choice(["positive", "neutral", "negative"]),
                "outcome": self._rng.choice([
                    "follow-up scheduled",
                    "proposal sent",
                    "deal progressed",
                    "information shared",
                    "relationship maintained"
                ])
            })

        return sorted(interactions, key=lambda x: x["date"])

    def create_customer_profile(self) -> Dict[str, Any]:
        """Create a customer profile for sales automation."""
        company = self._random_company()

        return {
            "company_name": company,
            "industry": self._rng.choice(self.INDUSTRIES),
            "size": self._rng.choice(["SMB", "Mid-Market", "Enterprise"]),
            "annual_revenue": f"${self._rng.randint(1, 100)}M",
            "employee_count": self._rng.randint(50, 5000),
            "location": self._rng.choice([
                "San Francisco, CA", "New York, NY", "Austin, TX",
                "Seattle, WA", "Boston, MA", "Chicago, IL"
            ]),
            "decision_makers": [
                self.create_stakeholder("client") for _ in range(self._rng.randint(1, 3))
            ],
            "current_solutions": self._rng.sample(
                ["Salesforce", "HubSpot", "Custom CRM", "Spreadsheets", "None"],
                k=self._rng.randint(1, 2)
            ),
            "pain_points": self._rng.sample(self.PAIN_POINTS, k=2),
            "budget_range": self._rng.choice([
                "$10K-$50K", "$50K-$100K", "$100K-$500K", "$500K+"
            ]),
            "timeline": self._rng.choice([
                "Immediate", "1-3 months", "3-6 months", "6-12 months"
            ]),
            "lead_score": self._rng.randint(1, 100)
        }
