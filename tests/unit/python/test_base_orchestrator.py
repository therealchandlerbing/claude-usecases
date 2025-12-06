"""
Tests for the shared base_orchestrator module.

Tests cover:
- Configuration loading (dict, file, defaults)
- Result management
- Error and warning tracking
- Lifecycle methods (run, reset)
- Utility methods
"""

import pytest
from pathlib import Path
from typing import Dict, Any

from shared.base_orchestrator import BaseOrchestrator, OrchestratorError
from shared.config_loader import ConfigurationError


# ==============================================================================
# Test Fixtures - Concrete Implementations
# ==============================================================================


class SimpleOrchestrator(BaseOrchestrator):
    """Minimal orchestrator for basic tests."""

    def _get_default_config(self) -> Dict[str, Any]:
        return {"setting": "default_value", "timeout": 30}

    def _initialize(self) -> None:
        self.initialized = True
        self.components = []

    def execute(self, **kwargs) -> Dict[str, Any]:
        return {"executed": True, "kwargs": kwargs}


class CountingOrchestrator(BaseOrchestrator):
    """Orchestrator that counts operations for testing."""

    def _get_default_config(self) -> Dict[str, Any]:
        return {"multiplier": 2}

    def _initialize(self) -> None:
        self.call_count = 0

    def execute(self, value: int = 1, **kwargs) -> Dict[str, Any]:
        self.call_count += 1
        multiplier = self.config.get("multiplier", 1)
        result = value * multiplier
        self.set_result("computed", result)
        return {"value": result, "call_count": self.call_count}


class FailingOrchestrator(BaseOrchestrator):
    """Orchestrator that fails for error handling tests."""

    def _get_default_config(self) -> Dict[str, Any]:
        return {}

    def _initialize(self) -> None:
        pass

    def execute(self, should_fail: bool = True, **kwargs) -> Dict[str, Any]:
        if should_fail:
            raise ValueError("Intentional failure for testing")
        return {"success": True}


class NestedConfigOrchestrator(BaseOrchestrator):
    """Orchestrator with nested configuration for utility tests."""

    def _get_default_config(self) -> Dict[str, Any]:
        return {
            "database": {
                "host": "localhost",
                "port": 5432,
                "credentials": {
                    "user": "admin"
                }
            },
            "features": ["auth", "logging"]
        }

    def _initialize(self) -> None:
        pass

    def execute(self, **kwargs) -> Dict[str, Any]:
        return {}


# ==============================================================================
# Test Classes
# ==============================================================================


class TestOrchestratorInitialization:
    """Tests for orchestrator initialization."""

    def test_init_with_default_config(self):
        """Test initialization with default configuration."""
        orch = SimpleOrchestrator()

        assert orch.config == {"setting": "default_value", "timeout": 30}
        assert orch.initialized is True

    def test_init_with_provided_config(self):
        """Test initialization with provided configuration."""
        custom_config = {"setting": "custom_value", "extra": "data"}
        orch = SimpleOrchestrator(config=custom_config)

        assert orch.config == custom_config
        assert orch.config["setting"] == "custom_value"

    def test_init_with_config_file(self, tmp_path: Path):
        """Test initialization with configuration file."""
        config_file = tmp_path / "config.yaml"
        config_file.write_text("setting: from_file\ntimeout: 60\n")

        orch = SimpleOrchestrator(config_path=config_file)

        assert orch.config["setting"] == "from_file"
        assert orch.config["timeout"] == 60

    def test_init_with_empty_config_file_uses_defaults(self, tmp_path: Path):
        """Test that empty config file falls back to defaults."""
        config_file = tmp_path / "empty.yaml"
        config_file.write_text("")

        orch = SimpleOrchestrator(config_path=config_file)

        assert orch.config == {"setting": "default_value", "timeout": 30}

    def test_init_with_string_config_path(self, tmp_path: Path):
        """Test initialization with string config path."""
        config_file = tmp_path / "config.yaml"
        config_file.write_text("setting: string_path\n")

        orch = SimpleOrchestrator(config_path=str(config_file))

        assert orch.config["setting"] == "string_path"

    def test_init_priority_config_over_path(self, tmp_path: Path):
        """Test that direct config takes priority over config_path."""
        config_file = tmp_path / "config.yaml"
        config_file.write_text("setting: from_file\n")

        orch = SimpleOrchestrator(
            config={"setting": "direct"},
            config_path=config_file
        )

        assert orch.config["setting"] == "direct"

    def test_init_verbose_mode(self):
        """Test verbose mode is stored correctly."""
        orch = SimpleOrchestrator(verbose=True)
        assert orch.verbose is True

        orch2 = SimpleOrchestrator(verbose=False)
        assert orch2.verbose is False

    def test_init_creates_empty_tracking_lists(self):
        """Test that result tracking is initialized empty."""
        orch = SimpleOrchestrator()

        assert orch._results == {}
        assert orch._errors == []
        assert orch._warnings == []
        assert orch._info == []


class TestResultManagement:
    """Tests for result storage and retrieval."""

    def test_set_and_get_result(self):
        """Test setting and getting results."""
        orch = SimpleOrchestrator()

        orch.set_result("key1", "value1")
        orch.set_result("key2", 42)

        assert orch.get_result("key1") == "value1"
        assert orch.get_result("key2") == 42

    def test_get_result_default(self):
        """Test getting nonexistent result with default."""
        orch = SimpleOrchestrator()

        assert orch.get_result("missing") is None
        assert orch.get_result("missing", "default") == "default"

    def test_get_results_returns_copy(self):
        """Test that get_results returns a copy."""
        orch = SimpleOrchestrator()
        orch.set_result("key", "value")

        results = orch.get_results()
        results["key"] = "modified"

        assert orch.get_result("key") == "value"

    def test_execute_can_set_results(self):
        """Test that execute can set results via set_result."""
        orch = CountingOrchestrator()
        orch.execute(value=5)

        assert orch.get_result("computed") == 10  # 5 * 2 (default multiplier)


class TestErrorAndWarningManagement:
    """Tests for error, warning, and info tracking."""

    def test_add_error(self):
        """Test adding errors."""
        orch = SimpleOrchestrator()

        orch.add_error("Something went wrong", code="ERR001", phase="validation")

        errors = orch.get_errors()
        assert len(errors) == 1
        assert errors[0]["message"] == "Something went wrong"
        assert errors[0]["code"] == "ERR001"
        assert errors[0]["phase"] == "validation"
        assert "timestamp" in errors[0]

    def test_add_warning(self):
        """Test adding warnings."""
        orch = SimpleOrchestrator()

        orch.add_warning("This might be a problem", code="WARN001")

        warnings = orch.get_warnings()
        assert len(warnings) == 1
        assert warnings[0]["message"] == "This might be a problem"
        assert warnings[0]["code"] == "WARN001"

    def test_add_info(self):
        """Test adding info messages."""
        orch = SimpleOrchestrator()

        orch.add_info("Processing started", phase="init")

        assert len(orch._info) == 1
        assert orch._info[0]["message"] == "Processing started"

    def test_has_errors(self):
        """Test has_errors check."""
        orch = SimpleOrchestrator()

        assert orch.has_errors() is False
        orch.add_error("Error")
        assert orch.has_errors() is True

    def test_has_warnings(self):
        """Test has_warnings check."""
        orch = SimpleOrchestrator()

        assert orch.has_warnings() is False
        orch.add_warning("Warning")
        assert orch.has_warnings() is True

    def test_get_errors_returns_copy(self):
        """Test that get_errors returns a copy."""
        orch = SimpleOrchestrator()
        orch.add_error("Error")

        errors = orch.get_errors()
        errors.append({"message": "fake"})

        assert len(orch.get_errors()) == 1


class TestExecute:
    """Tests for the execute method."""

    def test_basic_execute(self):
        """Test basic execute call."""
        orch = SimpleOrchestrator()

        result = orch.execute()

        assert result == {"executed": True, "kwargs": {}}

    def test_execute_with_kwargs(self):
        """Test execute with keyword arguments."""
        orch = SimpleOrchestrator()

        result = orch.execute(param1="value1", param2=42)

        assert result["kwargs"] == {"param1": "value1", "param2": 42}

    def test_execute_modifies_state(self):
        """Test that execute can modify orchestrator state."""
        orch = CountingOrchestrator()

        assert orch.call_count == 0
        orch.execute()
        assert orch.call_count == 1
        orch.execute()
        assert orch.call_count == 2


class TestRunLifecycle:
    """Tests for the run lifecycle method."""

    def test_run_success(self):
        """Test successful run with timing."""
        orch = SimpleOrchestrator()

        result = orch.run()

        assert result["status"] == "success"
        assert result["result"] == {"executed": True, "kwargs": {}}
        assert result["errors"] == []
        assert "timing" in result
        assert "started_at" in result["timing"]
        assert "completed_at" in result["timing"]
        assert "duration_seconds" in result["timing"]

    def test_run_with_errors_recorded(self):
        """Test run when errors are recorded (but not raised)."""
        orch = SimpleOrchestrator()

        # Manually add an error before run
        orch.add_error("Pre-existing error")
        result = orch.run()

        assert result["status"] == "completed_with_errors"
        assert len(result["errors"]) == 1

    def test_run_catches_exceptions(self):
        """Test that run catches and records exceptions."""
        orch = FailingOrchestrator()

        result = orch.run(should_fail=True)

        assert result["status"] == "failed"
        assert len(result["errors"]) == 1
        assert "Intentional failure" in result["errors"][0]["message"]

    def test_run_passes_kwargs(self):
        """Test that run passes kwargs to execute."""
        orch = CountingOrchestrator()

        result = orch.run(value=10)

        assert result["result"]["value"] == 20  # 10 * 2

    def test_run_timing_is_positive(self):
        """Test that timing duration is positive."""
        orch = SimpleOrchestrator()

        result = orch.run()

        assert result["timing"]["duration_seconds"] >= 0


class TestReset:
    """Tests for the reset method."""

    def test_reset_clears_results(self):
        """Test that reset clears results."""
        orch = SimpleOrchestrator()
        orch.set_result("key", "value")
        orch.add_error("Error")
        orch.add_warning("Warning")
        orch.run()

        orch.reset()

        assert orch._results == {}
        assert orch._errors == []
        assert orch._warnings == []
        assert orch._info == []
        assert orch._started_at is None
        assert orch._completed_at is None


class TestUtilityMethods:
    """Tests for utility methods."""

    def test_get_config_value_simple(self):
        """Test getting simple config values."""
        orch = NestedConfigOrchestrator()

        assert orch.get_config_value("features") == ["auth", "logging"]

    def test_get_config_value_nested(self):
        """Test getting nested config values with dot notation."""
        orch = NestedConfigOrchestrator()

        assert orch.get_config_value("database.host") == "localhost"
        assert orch.get_config_value("database.port") == 5432
        assert orch.get_config_value("database.credentials.user") == "admin"

    def test_get_config_value_missing_with_default(self):
        """Test getting missing config value with default."""
        orch = NestedConfigOrchestrator()

        assert orch.get_config_value("missing") is None
        assert orch.get_config_value("missing", "default") == "default"
        assert orch.get_config_value("database.missing", 0) == 0

    def test_validate_config_passes(self):
        """Test config validation with all required keys present."""
        orch = NestedConfigOrchestrator()

        # Should not raise
        orch.validate_config(["database", "features"])

    def test_validate_config_fails(self):
        """Test config validation with missing required keys."""
        orch = SimpleOrchestrator()

        with pytest.raises(ConfigurationError) as exc_info:
            orch.validate_config(["missing_key"])

        assert "missing_key" in str(exc_info.value)

    def test_get_summary(self):
        """Test summary generation."""
        orch = CountingOrchestrator()
        orch.set_result("data", "value")
        orch.add_warning("Warning")
        orch.run(value=5)

        summary = orch.get_summary()

        assert summary["class"] == "CountingOrchestrator"
        assert "multiplier" in summary["config_keys"]
        assert summary["result_count"] >= 1
        assert summary["warning_count"] == 1
        assert summary["has_run"] is True
        assert summary["duration"] is not None

    def test_log_verbose_mode(self, capsys):
        """Test logging in verbose mode."""
        orch = SimpleOrchestrator(verbose=True)

        orch.log("Test message", level="info")

        captured = capsys.readouterr()
        assert "Test message" in captured.out
        assert "INFO" in captured.out

    def test_log_silent_mode(self, capsys):
        """Test logging in silent mode."""
        orch = SimpleOrchestrator(verbose=False)

        orch.log("Test message")

        captured = capsys.readouterr()
        assert captured.out == ""


class TestOrchestratorError:
    """Tests for OrchestratorError exception."""

    def test_error_with_message_only(self):
        """Test error with just a message."""
        error = OrchestratorError("Something failed")

        assert str(error) == "Something failed"
        assert error.phase is None
        assert error.details == {}

    def test_error_with_phase_and_details(self):
        """Test error with phase and details."""
        error = OrchestratorError(
            "Validation failed",
            phase="validation",
            details={"field": "email", "reason": "invalid format"}
        )

        assert "Validation failed" in str(error)
        assert error.phase == "validation"
        assert error.details["field"] == "email"
