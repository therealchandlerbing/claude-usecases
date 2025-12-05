"""
360 Executive Project Tracker - Scripts

A comprehensive project tracking system that consolidates information from
Gmail, Google Calendar, Google Drive, and Asana into Excel dashboards
and interactive HTML visualizations.

Main Components:
    - TrackerOrchestrator: Main workflow coordinator
    - DataCollector: Multi-source data collection
    - TaskExtractor: Task extraction from various sources
    - ProjectTrackerBuilder: Excel tracker builder
    - ToolIntegrator: External tool integration
    - xlsx_enhancer: Excel schema enhancement utilities
    - xlsx_to_html_export: HTML export utilities

Example:
    >>> from tracker_scripts import TrackerOrchestrator
    >>> orchestrator = TrackerOrchestrator(config)
    >>> result = orchestrator.build_tracker()
"""

from .tracker_orchestrator import TrackerOrchestrator
from .data_collector import DataCollector, TaskExtractor
from .project_tracker_builder import ProjectTrackerBuilder
from .tool_integrator import ToolIntegrator
from .xlsx_enhancer import enhance_xlsx_schema, verify_schema
from .xlsx_to_html_export import (
    format_date_for_html,
    extract_tasks_from_xlsx,
    inject_tasks_into_html,
    export_xlsx_to_html,
    generate_task_summary,
)

__all__ = [
    "TrackerOrchestrator",
    "DataCollector",
    "TaskExtractor",
    "ProjectTrackerBuilder",
    "ToolIntegrator",
    "enhance_xlsx_schema",
    "verify_schema",
    "format_date_for_html",
    "extract_tasks_from_xlsx",
    "inject_tasks_into_html",
    "export_xlsx_to_html",
    "generate_task_summary",
]

__version__ = "1.0.0"
