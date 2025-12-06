"""
Organization Data Factory

Generates realistic organization data for testing executive intelligence,
board meeting prep, and other organizational skills.
"""

import random
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional

try:
    from faker import Faker
    HAS_FAKER = True
except ImportError:
    HAS_FAKER = False


class OrganizationDataFactory:
    """Factory for generating organization test data."""

    ORG_TYPES = [
        "501(c)(3) Public Charity",
        "501(c)(3) Private Foundation",
        "501(c)(4) Social Welfare",
        "501(c)(6) Trade Association",
        "B Corporation"
    ]

    MISSION_AREAS = [
        "Education", "Healthcare", "Environment", "Arts & Culture",
        "Social Services", "Economic Development", "Human Rights",
        "Animal Welfare", "Community Development"
    ]

    def __init__(self, seed: Optional[int] = None):
        """Initialize with optional seed."""
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
        return self._rng.choice(["John Smith", "Jane Doe", "Bob Johnson"])

    def create_nonprofit(self) -> Dict[str, Any]:
        """Create a nonprofit organization profile."""
        mission_area = self._rng.choice(self.MISSION_AREAS)
        budget = self._rng.randint(100000, 5000000)

        return {
            "name": f"{mission_area} Impact Foundation",
            "ein": f"{self._rng.randint(10, 99)}-{self._rng.randint(1000000, 9999999)}",
            "type": self._rng.choice(self.ORG_TYPES[:3]),
            "mission_area": mission_area,
            "founded_year": self._rng.randint(1990, 2020),
            "annual_budget": budget,
            "staff_count": self._rng.randint(5, 50),
            "volunteer_count": self._rng.randint(10, 200),
            "beneficiaries_served": self._rng.randint(1000, 50000),
            "geographic_scope": self._rng.choice([
                "Local", "Regional", "State", "National", "International"
            ]),
            "programs": [
                self.create_program() for _ in range(self._rng.randint(2, 5))
            ],
            "funding_sources": self.create_funding_mix(budget),
            "metrics": {
                "program_efficiency_ratio": round(self._rng.uniform(0.7, 0.9), 2),
                "fundraising_efficiency": round(self._rng.uniform(0.8, 0.95), 2),
                "overhead_ratio": round(self._rng.uniform(0.1, 0.25), 2)
            }
        }

    def create_program(self) -> Dict[str, Any]:
        """Create a program within an organization."""
        return {
            "name": self._rng.choice([
                "Youth Development Initiative",
                "Community Health Program",
                "Educational Excellence",
                "Environmental Stewardship",
                "Economic Empowerment"
            ]),
            "budget": self._rng.randint(50000, 500000),
            "staff_fte": round(self._rng.uniform(1, 10), 1),
            "start_date": (datetime.now() - timedelta(days=self._rng.randint(365, 1825))).isoformat(),
            "outcomes": [
                {"metric": "People served", "value": self._rng.randint(100, 5000)},
                {"metric": "Satisfaction rate", "value": f"{self._rng.randint(80, 98)}%"}
            ],
            "status": self._rng.choice(["active", "expanding", "evaluating"])
        }

    def create_funding_mix(self, total_budget: int) -> Dict[str, Any]:
        """Create realistic funding source breakdown."""
        individual_pct = self._rng.uniform(0.2, 0.5)
        foundation_pct = self._rng.uniform(0.2, 0.4)
        corporate_pct = self._rng.uniform(0.05, 0.2)
        government_pct = self._rng.uniform(0.1, 0.3)
        earned_pct = 1 - individual_pct - foundation_pct - corporate_pct - government_pct

        return {
            "individual_donations": round(total_budget * individual_pct),
            "foundation_grants": round(total_budget * foundation_pct),
            "corporate_giving": round(total_budget * corporate_pct),
            "government_grants": round(total_budget * max(0, government_pct)),
            "earned_revenue": round(total_budget * max(0, earned_pct))
        }

    def create_board_member(self) -> Dict[str, Any]:
        """Create a board member profile."""
        name = self._random_name()
        return {
            "name": name,
            "title": self._rng.choice([
                "Chair", "Vice Chair", "Secretary", "Treasurer", "Director"
            ]),
            "term_start": (datetime.now() - timedelta(days=self._rng.randint(90, 1095))).isoformat(),
            "term_end": (datetime.now() + timedelta(days=self._rng.randint(90, 730))).isoformat(),
            "committees": self._rng.sample(
                ["Executive", "Finance", "Governance", "Development", "Programs"],
                k=self._rng.randint(1, 3)
            ),
            "expertise": self._rng.sample(
                ["Finance", "Legal", "Marketing", "Operations", "Fundraising", "Program"],
                k=self._rng.randint(1, 3)
            ),
            "attendance_rate": round(self._rng.uniform(0.7, 1.0), 2),
            "donation_level": self._rng.choice(["Major Donor", "Donor", "Non-donor"])
        }

    def create_board(self, size: int = 9) -> List[Dict[str, Any]]:
        """Create a complete board of directors."""
        board = []
        titles = ["Chair", "Vice Chair", "Secretary", "Treasurer"] + ["Director"] * (size - 4)

        for i, title in enumerate(titles[:size]):
            member = self.create_board_member()
            member["title"] = title
            board.append(member)

        return board

    def create_strategic_plan(self) -> Dict[str, Any]:
        """Create a strategic plan summary."""
        return {
            "vision": "To create lasting positive change in our community",
            "mission": "Empowering individuals through innovative programs",
            "values": ["Integrity", "Innovation", "Impact", "Inclusion"],
            "time_horizon": self._rng.choice(["3 years", "5 years"]),
            "strategic_priorities": [
                {
                    "priority": "Expand Program Reach",
                    "objectives": [
                        "Increase beneficiaries by 25%",
                        "Launch 2 new program sites"
                    ],
                    "progress": self._rng.randint(20, 80)
                },
                {
                    "priority": "Strengthen Financial Sustainability",
                    "objectives": [
                        "Grow operating reserve to 6 months",
                        "Diversify revenue streams"
                    ],
                    "progress": self._rng.randint(20, 80)
                },
                {
                    "priority": "Build Organizational Capacity",
                    "objectives": [
                        "Invest in staff development",
                        "Upgrade technology systems"
                    ],
                    "progress": self._rng.randint(20, 80)
                }
            ],
            "kpis": [
                {"name": "Program Impact Score", "target": 85, "actual": self._rng.randint(70, 95)},
                {"name": "Donor Retention Rate", "target": 75, "actual": self._rng.randint(60, 85)},
                {"name": "Staff Satisfaction", "target": 80, "actual": self._rng.randint(70, 90)}
            ]
        }

    def create_meeting_agenda(self, meeting_type: str = "board") -> Dict[str, Any]:
        """Create a board or committee meeting agenda."""
        return {
            "meeting_type": meeting_type,
            "date": (datetime.now() + timedelta(days=self._rng.randint(7, 30))).isoformat(),
            "duration_minutes": self._rng.choice([60, 90, 120]),
            "location": self._rng.choice(["Virtual", "Headquarters", "Hybrid"]),
            "items": [
                {"item": "Call to Order", "duration": 5, "presenter": "Chair"},
                {"item": "Approval of Minutes", "duration": 5, "presenter": "Secretary"},
                {"item": "Financial Report", "duration": 15, "presenter": "Treasurer"},
                {"item": "Executive Director Report", "duration": 20, "presenter": "ED"},
                {"item": "Committee Reports", "duration": 15, "presenter": "Various"},
                {"item": "New Business", "duration": 20, "presenter": "Chair"},
                {"item": "Adjournment", "duration": 5, "presenter": "Chair"}
            ],
            "materials": [
                "Board Packet",
                "Financial Statements",
                "Program Reports",
                "Strategic Plan Update"
            ]
        }
