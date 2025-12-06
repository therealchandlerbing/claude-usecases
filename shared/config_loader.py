"""
Centralized Configuration Loader

Provides consistent configuration loading with standardized error handling
across all skills and scripts in the claude-usecases repository.

Usage:
    from shared.config_loader import ConfigLoader, ConfigurationError

    # Load required config (raises ConfigurationError if not found)
    config = ConfigLoader.load_yaml(Path("config/settings.yaml"))

    # Load optional config (returns None if not found)
    config = ConfigLoader.load_yaml(Path("config/optional.yaml"), required=False)

    # Load with default values
    config = ConfigLoader.load_yaml_with_defaults(
        Path("config/settings.yaml"),
        defaults={"timeout": 30, "retries": 3}
    )
"""

from pathlib import Path
from typing import Any, Dict, Optional, Union

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore


class ConfigurationError(Exception):
    """Exception raised for configuration loading errors."""

    def __init__(self, message: str, path: Optional[Path] = None):
        self.path = path
        super().__init__(message)


class ConfigLoader:
    """Centralized configuration loading with consistent error handling."""

    @staticmethod
    def _ensure_yaml_available() -> None:
        """Ensure PyYAML is available, raise helpful error if not."""
        if yaml is None:
            raise ConfigurationError(
                "PyYAML is required for configuration loading. "
                "Install with: pip install pyyaml"
            )

    @staticmethod
    def load_yaml(
        path: Union[Path, str],
        required: bool = True,
        encoding: str = "utf-8"
    ) -> Optional[Dict[str, Any]]:
        """
        Load YAML configuration from file with standardized error handling.

        Args:
            path: Path to the YAML configuration file
            required: If True, raises ConfigurationError when file not found
            encoding: File encoding (default: utf-8)

        Returns:
            Parsed configuration dictionary, or None if file not found and not required

        Raises:
            ConfigurationError: If required file is not found or YAML is invalid
        """
        ConfigLoader._ensure_yaml_available()

        path = Path(path) if isinstance(path, str) else path

        try:
            with open(path, "r", encoding=encoding) as f:
                config = yaml.safe_load(f)
            # Handle empty files
            return config if config is not None else {}
        except FileNotFoundError:
            if required:
                raise ConfigurationError(
                    f"Required configuration file not found: {path}",
                    path=path
                )
            return None
        except yaml.YAMLError as e:
            raise ConfigurationError(
                f"Invalid YAML syntax in {path}: {e}",
                path=path
            )
        except PermissionError:
            raise ConfigurationError(
                f"Permission denied when reading: {path}",
                path=path
            )

    @staticmethod
    def load_yaml_with_defaults(
        path: Union[Path, str],
        defaults: Dict[str, Any],
        required: bool = False,
        encoding: str = "utf-8"
    ) -> Dict[str, Any]:
        """
        Load YAML configuration with default values.

        If the file doesn't exist and is not required, returns only defaults.
        If the file exists, values from file override defaults.

        Args:
            path: Path to the YAML configuration file
            defaults: Default values to use
            required: If True, raises ConfigurationError when file not found
            encoding: File encoding (default: utf-8)

        Returns:
            Merged configuration dictionary with defaults and file values

        Raises:
            ConfigurationError: If required file is not found or YAML is invalid
        """
        config = ConfigLoader.load_yaml(path, required=required, encoding=encoding)

        if config is None:
            return defaults.copy()

        # Merge: file values override defaults
        result = defaults.copy()
        result.update(config)
        return result

    @staticmethod
    def load_frontmatter(
        path: Union[Path, str],
        encoding: str = "utf-8"
    ) -> Optional[Dict[str, Any]]:
        """
        Extract and parse YAML frontmatter from a markdown file.

        Frontmatter must be delimited by --- at the start and end.

        Args:
            path: Path to the markdown file
            encoding: File encoding (default: utf-8)

        Returns:
            Parsed frontmatter as dictionary, or None if no frontmatter found

        Raises:
            ConfigurationError: If YAML parsing fails
        """
        ConfigLoader._ensure_yaml_available()

        path = Path(path) if isinstance(path, str) else path

        try:
            with open(path, "r", encoding=encoding) as f:
                content = f.read()
        except FileNotFoundError:
            return None
        except PermissionError:
            raise ConfigurationError(
                f"Permission denied when reading: {path}",
                path=path
            )

        # Check for frontmatter
        if not content.startswith("---"):
            return None

        # Find closing delimiter
        end_match = content.find("\n---", 3)
        if end_match == -1:
            return None

        frontmatter_text = content[3:end_match].strip()

        try:
            return yaml.safe_load(frontmatter_text)
        except yaml.YAMLError as e:
            raise ConfigurationError(
                f"Invalid YAML frontmatter in {path}: {e}",
                path=path
            )

    @staticmethod
    def validate_required_fields(
        config: Dict[str, Any],
        required_fields: list,
        context: str = "configuration"
    ) -> None:
        """
        Validate that required fields are present in configuration.

        Args:
            config: Configuration dictionary to validate
            required_fields: List of required field names
            context: Context string for error messages

        Raises:
            ConfigurationError: If any required fields are missing
        """
        missing = [field for field in required_fields if field not in config]
        if missing:
            raise ConfigurationError(
                f"Missing required fields in {context}: {', '.join(missing)}"
            )
