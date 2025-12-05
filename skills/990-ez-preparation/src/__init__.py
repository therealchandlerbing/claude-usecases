"""
990-EZ Preparation - IRS Form 990-EZ Automation

Comprehensive automation for IRS Form 990-EZ preparation including
eligibility verification, multi-level validation, and complete filing
package generation.

Main Components:
    - Form990EZOrchestrator: Main workflow coordinator for 990-EZ preparation

Example:
    >>> from form_990ez import Form990EZOrchestrator
    >>> orchestrator = Form990EZOrchestrator(org_data)
    >>> package = orchestrator.prepare_filing()
"""

from .orchestrator import Form990EZOrchestrator, main

__all__ = [
    "Form990EZOrchestrator",
    "main",
]

__version__ = "1.0.0"
