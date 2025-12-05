"""
Workflow Debugging - Systematic Debugging Toolkit

A comprehensive debugging toolkit for complex workflow orchestration systems,
enabling rapid identification, isolation, and resolution of execution failures.

Main Components:
    - WorkflowDebugger: Main debugging coordinator
    - ErrorContext: Structured error information
    - DiagnosisResult: Debugging diagnosis results
    - SlackNotifier: Slack integration for error notifications
    - AsanaTaskCreator: Asana task creation for follow-up
    - EmailNotifier: Email notification support

Example:
    >>> from workflow_debugging import WorkflowDebugger, ErrorContext
    >>> debugger = WorkflowDebugger()
    >>> context = ErrorContext(
    ...     error_message="API timeout",
    ...     source_file="data_collector.py",
    ...     line_number=42
    ... )
    >>> result = debugger.analyze_error(context)
"""

from .workflow_debugger import (
    WorkflowDebugger,
    ErrorSeverity,
    WorkflowRegion,
    ErrorContext,
    DiagnosisResult,
    SlackNotifier,
    AsanaTaskCreator,
    EmailNotifier,
)

__all__ = [
    "WorkflowDebugger",
    "ErrorSeverity",
    "WorkflowRegion",
    "ErrorContext",
    "DiagnosisResult",
    "SlackNotifier",
    "AsanaTaskCreator",
    "EmailNotifier",
]

__version__ = "1.0.0"
