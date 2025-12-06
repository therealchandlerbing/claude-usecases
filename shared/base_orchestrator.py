"""
Base Orchestrator Class

Provides a standardized foundation for all skill orchestrators in the claude-usecases
repository. Reduces boilerplate code by ~100 lines per skill while ensuring consistent
patterns for configuration, result management, and lifecycle hooks.

Usage:
    from shared.base_orchestrator import BaseOrchestrator

    class MySkillOrchestrator(BaseOrchestrator):
        def _get_default_config(self) -> Dict[str, Any]:
            return {"setting": "value"}

        def _initialize(self) -> None:
            self.my_component = SomeComponent()

        def execute(self, **kwargs) -> Dict[str, Any]:
            # Main skill logic
            return {"result": "success"}
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

from shared.config_loader import ConfigLoader, ConfigurationError


class OrchestratorError(Exception):
    """Base exception for orchestrator errors."""

    def __init__(self, message: str, phase: Optional[str] = None, details: Optional[Dict] = None):
        self.phase = phase
        self.details = details or {}
        super().__init__(message)


class BaseOrchestrator(ABC):
    """
    Abstract base class for all skill orchestrators.

    Provides:
    - Flexible configuration loading (dict, path, or defaults)
    - Standardized result and error tracking
    - Lifecycle hooks for initialization and cleanup
    - Common utility methods

    Subclasses must implement:
    - _get_default_config(): Return default configuration dict
    - _initialize(): Set up skill-specific components
    - execute(): Main skill workflow logic
    """

    def __init__(
        self,
        config: Optional[Dict[str, Any]] = None,
        config_path: Optional[Union[Path, str]] = None,
        verbose: bool = False
    ):
        """
        Initialize the orchestrator with configuration.

        Args:
            config: Direct configuration dictionary
            config_path: Path to YAML configuration file
            verbose: Enable verbose logging

        Priority: config > config_path > defaults
        """
        self.verbose = verbose
        self._started_at: Optional[datetime] = None
        self._completed_at: Optional[datetime] = None

        # Load configuration with priority: provided > file > defaults
        if config is not None:
            self.config = config
        elif config_path is not None:
            path = Path(config_path) if isinstance(config_path, str) else config_path
            # Fallback to defaults if config file is empty
            self.config = ConfigLoader.load_yaml(path) or self._get_default_config()
        else:
            self.config = self._get_default_config()

        # Initialize result tracking
        self._results: Dict[str, Any] = {}
        self._errors: List[Dict[str, Any]] = []
        self._warnings: List[Dict[str, Any]] = []
        self._info: List[Dict[str, Any]] = []

        # Call subclass initialization
        self._initialize()

    @abstractmethod
    def _get_default_config(self) -> Dict[str, Any]:
        """
        Return default configuration for the skill.

        Override in subclass to provide skill-specific defaults.

        Returns:
            Dictionary of default configuration values
        """
        pass

    @abstractmethod
    def _initialize(self) -> None:
        """
        Initialize skill-specific components.

        Called after configuration is loaded. Override in subclass to:
        - Set up internal data structures
        - Initialize sub-components
        - Validate configuration
        """
        pass

    @abstractmethod
    def execute(self, **kwargs) -> Dict[str, Any]:
        """
        Execute the main skill workflow.

        Override in subclass to implement the core skill logic.

        Args:
            **kwargs: Skill-specific execution parameters

        Returns:
            Dictionary containing execution results
        """
        pass

    # =========================================================================
    # Result Management
    # =========================================================================

    def get_results(self) -> Dict[str, Any]:
        """Return a copy of accumulated results."""
        return self._results.copy()

    def set_result(self, key: str, value: Any) -> None:
        """Store a result value."""
        self._results[key] = value

    def get_result(self, key: str, default: Any = None) -> Any:
        """Retrieve a result value."""
        return self._results.get(key, default)

    # =========================================================================
    # Error and Warning Management
    # =========================================================================

    def add_error(
        self,
        message: str,
        code: Optional[str] = None,
        phase: Optional[str] = None,
        details: Optional[Dict] = None
    ) -> None:
        """Record an error."""
        self._errors.append({
            "message": message,
            "code": code,
            "phase": phase,
            "details": details or {},
            "timestamp": datetime.now().isoformat()
        })

    def add_warning(
        self,
        message: str,
        code: Optional[str] = None,
        phase: Optional[str] = None
    ) -> None:
        """Record a warning."""
        self._warnings.append({
            "message": message,
            "code": code,
            "phase": phase,
            "timestamp": datetime.now().isoformat()
        })

    def add_info(self, message: str, phase: Optional[str] = None) -> None:
        """Record an informational message."""
        self._info.append({
            "message": message,
            "phase": phase,
            "timestamp": datetime.now().isoformat()
        })

    def get_errors(self) -> List[Dict[str, Any]]:
        """Return all recorded errors."""
        return self._errors.copy()

    def get_warnings(self) -> List[Dict[str, Any]]:
        """Return all recorded warnings."""
        return self._warnings.copy()

    def has_errors(self) -> bool:
        """Check if any errors have been recorded."""
        return len(self._errors) > 0

    def has_warnings(self) -> bool:
        """Check if any warnings have been recorded."""
        return len(self._warnings) > 0

    # =========================================================================
    # Lifecycle Methods
    # =========================================================================

    def run(self, **kwargs) -> Dict[str, Any]:
        """
        Run the orchestrator with lifecycle tracking.

        This is a convenience wrapper around execute() that adds:
        - Timing information
        - Error handling
        - Summary generation

        Args:
            **kwargs: Passed to execute()

        Returns:
            Dictionary with results, timing, and status information
        """
        self._started_at = datetime.now()

        try:
            result = self.execute(**kwargs)
            status = "success" if not self.has_errors() else "completed_with_errors"
        except Exception as e:
            self.add_error(str(e), code="EXECUTION_ERROR")
            result = {}
            status = "failed"

        self._completed_at = datetime.now()

        return {
            "status": status,
            "result": result,
            "errors": self._errors,
            "warnings": self._warnings,
            "timing": {
                "started_at": self._started_at.isoformat(),
                "completed_at": self._completed_at.isoformat(),
                "duration_seconds": (self._completed_at - self._started_at).total_seconds()
            }
        }

    def reset(self) -> None:
        """Reset the orchestrator state for reuse."""
        self._results = {}
        self._errors = []
        self._warnings = []
        self._info = []
        self._started_at = None
        self._completed_at = None

    # =========================================================================
    # Utility Methods
    # =========================================================================

    def log(self, message: str, level: str = "info") -> None:
        """Log a message if verbose mode is enabled."""
        if self.verbose:
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"[{timestamp}] [{level.upper()}] {message}")

    def get_config_value(self, key: str, default: Any = None) -> Any:
        """
        Get a configuration value with dot notation support.

        Args:
            key: Configuration key (supports dots, e.g., "database.host")
            default: Default value if key not found

        Returns:
            Configuration value or default
        """
        keys = key.split(".")
        value = self.config

        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default

        return value

    def validate_config(self, required_keys: List[str]) -> None:
        """
        Validate that required configuration keys are present.

        Args:
            required_keys: List of required configuration keys

        Raises:
            ConfigurationError: If required keys are missing
        """
        ConfigLoader.validate_required_fields(
            self.config,
            required_keys,
            context=f"{self.__class__.__name__} configuration"
        )

    def get_summary(self) -> Dict[str, Any]:
        """Generate a summary of the orchestrator state."""
        return {
            "class": self.__class__.__name__,
            "config_keys": list(self.config.keys()),
            "result_count": len(self._results),
            "error_count": len(self._errors),
            "warning_count": len(self._warnings),
            "has_run": self._completed_at is not None,
            "duration": (
                (self._completed_at - self._started_at).total_seconds()
                if self._completed_at and self._started_at
                else None
            )
        }
