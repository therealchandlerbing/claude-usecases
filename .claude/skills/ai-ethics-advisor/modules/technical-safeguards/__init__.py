"""
AI Ethics Advisor - Technical Safeguards

Technical implementation modules for responsible AI development including
bias monitoring, explainability, and privacy-preserving techniques.

Main Components:
    - BiasMonitor: Real-time bias detection and monitoring
    - FairnessMetrics: Fairness metric calculation
    - ExplainabilityEngine: Model explainability tools
    - DifferentialPrivacyEngine: Differential privacy implementation
    - FederatedLearningCoordinator: Federated learning coordination
    - DataMinimizer: Data minimization utilities

Example:
    >>> from technical_safeguards import BiasMonitor
    >>> monitor = BiasMonitor()
    >>> report = monitor.analyze_model_outputs(predictions, demographics)
"""

from .bias_monitoring import BiasMonitor, FairnessMetrics
from .explainability import ExplainabilityEngine
from .privacy_preserving import (
    DifferentialPrivacyEngine,
    FederatedLearningCoordinator,
    DataMinimizer,
)

__all__ = [
    "BiasMonitor",
    "FairnessMetrics",
    "ExplainabilityEngine",
    "DifferentialPrivacyEngine",
    "FederatedLearningCoordinator",
    "DataMinimizer",
]

__version__ = "1.0.0"
