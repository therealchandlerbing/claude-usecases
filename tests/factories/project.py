"""
Project Data Factory

Generates realistic project and workflow data for testing
project tracking, workflow debugging, and intelligence extraction skills.
"""

import random
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional

try:
    from faker import Faker
    HAS_FAKER = True
except ImportError:
    HAS_FAKER = False


class ProjectDataFactory:
    """Factory for generating project and workflow test data."""

    PROJECT_TYPES = [
        "Product Launch", "System Integration", "Process Improvement",
        "Research Initiative", "Marketing Campaign", "Infrastructure Upgrade"
    ]

    STATUSES = ["not_started", "in_progress", "on_hold", "completed", "cancelled"]

    PRIORITIES = ["critical", "high", "medium", "low"]

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
        return self._rng.choice(["Alex Chen", "Sam Wilson", "Jordan Lee"])

    def create_project(self) -> Dict[str, Any]:
        """Create a project with tasks and milestones."""
        start_date = datetime.now() - timedelta(days=self._rng.randint(30, 180))
        end_date = start_date + timedelta(days=self._rng.randint(60, 365))

        return {
            "id": f"proj_{self._rng.randint(1000, 9999)}",
            "name": f"{self._rng.choice(self.PROJECT_TYPES)} - Q{self._rng.randint(1, 4)}",
            "type": self._rng.choice(self.PROJECT_TYPES),
            "status": self._rng.choice(self.STATUSES[:3]),  # Active statuses
            "priority": self._rng.choice(self.PRIORITIES),
            "owner": self._random_name(),
            "team_size": self._rng.randint(3, 12),
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
            "budget": self._rng.randint(50000, 500000),
            "progress": self._rng.randint(10, 90),
            "milestones": [
                self.create_milestone(start_date, end_date)
                for _ in range(self._rng.randint(3, 6))
            ],
            "tasks": [
                self.create_task() for _ in range(self._rng.randint(5, 15))
            ],
            "risks": [
                self.create_risk() for _ in range(self._rng.randint(1, 4))
            ],
            "stakeholders": [
                {"name": self._random_name(), "role": role}
                for role in self._rng.sample(
                    ["Sponsor", "Lead", "Contributor", "Reviewer", "Advisor"],
                    k=self._rng.randint(2, 4)
                )
            ]
        }

    def create_milestone(
        self,
        project_start: datetime,
        project_end: datetime
    ) -> Dict[str, Any]:
        """Create a project milestone."""
        milestone_date = project_start + timedelta(
            days=self._rng.randint(
                0,
                (project_end - project_start).days
            )
        )

        return {
            "id": f"ms_{self._rng.randint(100, 999)}",
            "name": self._rng.choice([
                "Requirements Complete",
                "Design Approved",
                "Development Complete",
                "Testing Complete",
                "Launch Ready",
                "Post-Launch Review"
            ]),
            "due_date": milestone_date.isoformat(),
            "status": self._rng.choice(["pending", "completed", "at_risk"]),
            "deliverables": self._rng.randint(1, 5)
        }

    def create_task(self) -> Dict[str, Any]:
        """Create a project task."""
        return {
            "id": f"task_{self._rng.randint(10000, 99999)}",
            "title": self._rng.choice([
                "Review requirements",
                "Design system architecture",
                "Implement core features",
                "Write unit tests",
                "Conduct code review",
                "Deploy to staging",
                "User acceptance testing",
                "Documentation update"
            ]),
            "status": self._rng.choice(self.STATUSES),
            "priority": self._rng.choice(self.PRIORITIES),
            "assignee": self._random_name(),
            "estimated_hours": self._rng.randint(2, 40),
            "actual_hours": self._rng.randint(0, 50),
            "due_date": (datetime.now() + timedelta(days=self._rng.randint(-10, 30))).isoformat(),
            "tags": self._rng.sample(
                ["backend", "frontend", "infrastructure", "testing", "documentation"],
                k=self._rng.randint(1, 3)
            )
        }

    def create_risk(self) -> Dict[str, Any]:
        """Create a project risk."""
        return {
            "id": f"risk_{self._rng.randint(100, 999)}",
            "description": self._rng.choice([
                "Resource availability constraints",
                "Technical complexity higher than estimated",
                "Dependency on external team delivery",
                "Scope creep potential",
                "Integration challenges with legacy systems"
            ]),
            "probability": self._rng.choice(["low", "medium", "high"]),
            "impact": self._rng.choice(["low", "medium", "high"]),
            "status": self._rng.choice(["open", "mitigating", "resolved"]),
            "mitigation": "Implementing contingency plan",
            "owner": self._random_name()
        }

    def create_workflow(self) -> Dict[str, Any]:
        """Create a workflow definition."""
        return {
            "id": f"wf_{self._rng.randint(1000, 9999)}",
            "name": self._rng.choice([
                "Client Onboarding",
                "Content Approval",
                "Expense Reimbursement",
                "Lead Qualification",
                "Support Ticket Resolution"
            ]),
            "version": f"{self._rng.randint(1, 3)}.{self._rng.randint(0, 9)}",
            "status": self._rng.choice(["draft", "active", "deprecated"]),
            "steps": [
                {
                    "step_id": i + 1,
                    "name": step,
                    "type": self._rng.choice(["task", "approval", "notification", "condition"]),
                    "assignee_type": self._rng.choice(["user", "role", "team"]),
                    "timeout_hours": self._rng.randint(4, 48)
                }
                for i, step in enumerate([
                    "Initial Request",
                    "Review & Validate",
                    "Process",
                    "Approve",
                    "Complete"
                ])
            ],
            "triggers": [
                {"type": "manual", "description": "User initiated"},
                {"type": "scheduled", "description": "Daily at 9 AM"}
            ],
            "metrics": {
                "avg_completion_time_hours": round(self._rng.uniform(4, 72), 1),
                "completion_rate": round(self._rng.uniform(0.85, 0.99), 2),
                "instances_this_month": self._rng.randint(10, 200)
            }
        }

    def create_workflow_instance(self, workflow_id: str) -> Dict[str, Any]:
        """Create a workflow execution instance."""
        start_time = datetime.now() - timedelta(hours=self._rng.randint(1, 168))

        steps_completed = self._rng.randint(1, 5)
        step_history = []

        for i in range(steps_completed):
            step_time = start_time + timedelta(hours=i * self._rng.randint(1, 8))
            step_history.append({
                "step_id": i + 1,
                "status": "completed",
                "completed_at": step_time.isoformat(),
                "completed_by": self._random_name(),
                "duration_minutes": self._rng.randint(5, 120)
            })

        return {
            "instance_id": f"wfi_{self._rng.randint(10000, 99999)}",
            "workflow_id": workflow_id,
            "status": self._rng.choice(["running", "completed", "failed", "cancelled"]),
            "started_at": start_time.isoformat(),
            "current_step": steps_completed + 1,
            "step_history": step_history,
            "variables": {
                "requestor": self._random_name(),
                "request_type": self._rng.choice(["standard", "urgent", "bulk"]),
                "amount": self._rng.randint(100, 10000)
            },
            "errors": [] if self._rng.random() > 0.2 else [
                {
                    "step_id": steps_completed,
                    "error_type": "timeout",
                    "message": "Step exceeded time limit",
                    "timestamp": datetime.now().isoformat()
                }
            ]
        }

    def create_asana_task(self) -> Dict[str, Any]:
        """Create mock Asana API task response."""
        return {
            "gid": str(self._rng.randint(1000000000000, 9999999999999)),
            "name": self._rng.choice([
                "Review Q4 budget proposal",
                "Prepare board presentation",
                "Follow up with partner organization",
                "Update stakeholder database",
                "Schedule team retrospective"
            ]),
            "completed": self._rng.choice([True, False]),
            "due_on": (datetime.now() + timedelta(days=self._rng.randint(-5, 30))).strftime("%Y-%m-%d"),
            "assignee": {
                "gid": str(self._rng.randint(1000000000, 9999999999)),
                "name": self._random_name()
            },
            "projects": [
                {
                    "gid": str(self._rng.randint(1000000000, 9999999999)),
                    "name": f"Project {self._rng.choice(['Alpha', 'Beta', 'Gamma'])}"
                }
            ],
            "tags": [
                {"gid": str(self._rng.randint(100000, 999999)), "name": tag}
                for tag in self._rng.sample(["urgent", "client", "internal", "follow-up"], k=2)
            ],
            "notes": "Task details and context would go here.",
            "created_at": (datetime.now() - timedelta(days=self._rng.randint(1, 30))).isoformat() + "Z",
            "modified_at": datetime.now().isoformat() + "Z"
        }

    def create_intelligence_signal(self) -> Dict[str, Any]:
        """Create an intelligence signal for CEO advisor."""
        return {
            "id": f"sig_{self._rng.randint(10000, 99999)}",
            "type": self._rng.choice([
                "market_trend", "competitor_action", "regulatory_change",
                "partnership_opportunity", "risk_indicator"
            ]),
            "source": self._rng.choice([
                "news_feed", "social_media", "industry_report",
                "partner_communication", "internal_data"
            ]),
            "title": self._rng.choice([
                "New competitor enters market",
                "Regulatory change announced",
                "Partnership opportunity identified",
                "Market trend shift detected",
                "Customer sentiment change"
            ]),
            "summary": "Brief summary of the intelligence signal",
            "impact_score": round(self._rng.uniform(0.3, 1.0), 2),
            "confidence": round(self._rng.uniform(0.6, 0.95), 2),
            "urgency": self._rng.choice(["immediate", "short-term", "medium-term"]),
            "recommended_actions": [
                "Review and assess impact",
                "Schedule strategy discussion",
                "Update stakeholders"
            ],
            "detected_at": datetime.now().isoformat(),
            "expires_at": (datetime.now() + timedelta(days=self._rng.randint(7, 30))).isoformat()
        }
