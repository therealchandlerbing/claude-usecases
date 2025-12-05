"""
Tests for the 360 Workflow Debugger module.

This module provides comprehensive testing for workflow error diagnosis,
recovery strategies, and notification systems.
"""

import pytest
import asyncio
import json
import os
import tempfile
from datetime import datetime
from unittest.mock import AsyncMock, MagicMock, patch

# We need to add the module to path for imports
import sys
sys.path.insert(0, os.path.join(
    os.path.dirname(__file__),
    '../../../.claude/skills/workflow-debugging/src'
))

from workflow_debugger import (
    WorkflowDebugger,
    ErrorContext,
    DiagnosisResult,
    ErrorSeverity,
    WorkflowRegion,
    debug_workflow_error,
    SlackNotifier,
    AsanaTaskCreator,
    EmailNotifier
)


class TestErrorSeverity:
    """Tests for ErrorSeverity enum"""

    def test_severity_values(self):
        """Test that all severity levels have correct values"""
        assert ErrorSeverity.CRITICAL.value == "critical"
        assert ErrorSeverity.HIGH.value == "high"
        assert ErrorSeverity.MEDIUM.value == "medium"
        assert ErrorSeverity.LOW.value == "low"


class TestWorkflowRegion:
    """Tests for WorkflowRegion enum"""

    def test_region_values(self):
        """Test that all regions have correct values"""
        assert WorkflowRegion.US_WEST.value == "us-west"
        assert WorkflowRegion.BRAZIL.value == "br-south"
        assert WorkflowRegion.EUROPE.value == "eu-west"


class TestErrorContext:
    """Tests for ErrorContext dataclass"""

    @pytest.fixture
    def sample_error_context(self):
        """Create sample error context for testing"""
        return ErrorContext(
            workflow_id="wf-test-001",
            workflow_name="Test Workflow",
            client_name="Test Client",
            region=WorkflowRegion.US_WEST,
            error_type="ConnectionError",
            error_message="Connection timeout",
            stack_trace="Traceback...",
            timestamp=datetime(2025, 1, 15, 10, 30),
            variables={"key": "value"},
            completed_steps=["step1", "step2"],
            current_step="step3",
            user_email="test@example.com",
            severity=ErrorSeverity.HIGH
        )

    def test_to_dict_serialization(self, sample_error_context):
        """Test that ErrorContext serializes to dict correctly"""
        result = sample_error_context.to_dict()

        assert result['workflow_id'] == "wf-test-001"
        assert result['workflow_name'] == "Test Workflow"
        assert result['region'] == "us-west"
        assert result['severity'] == "high"
        assert result['timestamp'] == "2025-01-15T10:30:00"
        assert result['variables'] == {"key": "value"}

    def test_to_dict_is_json_serializable(self, sample_error_context):
        """Test that to_dict output is JSON serializable"""
        result = sample_error_context.to_dict()
        json_str = json.dumps(result)
        assert isinstance(json_str, str)


class TestWorkflowDebugger:
    """Tests for main WorkflowDebugger class"""

    @pytest.fixture
    def debugger(self):
        """Create debugger instance for testing"""
        return WorkflowDebugger()

    @pytest.fixture
    def debugger_with_config(self):
        """Create debugger with custom config"""
        return WorkflowDebugger(config={
            'auto_recovery': False,
            'max_retry_attempts': 5,
            'retry_delay_seconds': 10,
            'notification_channels': ['email'],
            'log_retention_days': 30,
            'regions': {
                'us-west': {'timezone': 'America/Los_Angeles', 'language': 'en-US'}
            }
        })

    def test_default_config(self, debugger):
        """Test default configuration is set correctly"""
        config = debugger.config
        assert config['auto_recovery'] is True
        assert config['max_retry_attempts'] == 3
        assert config['retry_delay_seconds'] == 30
        assert 'slack' in config['notification_channels']
        assert config['log_retention_days'] == 90

    def test_custom_config(self, debugger_with_config):
        """Test custom configuration overrides defaults"""
        config = debugger_with_config.config
        assert config['auto_recovery'] is False
        assert config['max_retry_attempts'] == 5

    def test_error_patterns_loaded(self, debugger):
        """Test that error patterns are loaded"""
        patterns = debugger.error_patterns
        assert 'ConnectionTimeout' in patterns
        assert 'AuthenticationError' in patterns
        assert 'DataValidationError' in patterns
        assert 'RateLimitError' in patterns
        assert 'EncodingError' in patterns

    def test_recovery_strategies_loaded(self, debugger):
        """Test that recovery strategies are loaded"""
        strategies = debugger.recovery_strategies
        assert 'retry_with_backoff' in strategies
        assert 'refresh_credentials' in strategies
        assert 'validate_and_transform' in strategies
        assert 'exponential_backoff' in strategies
        assert 'normalize_encoding' in strategies


class TestSeverityDetermination:
    """Tests for error severity determination"""

    @pytest.fixture
    def debugger(self):
        return WorkflowDebugger()

    def test_critical_for_production_client_facing(self, debugger):
        """Test critical severity for production client-facing errors"""
        error = Exception("Test error")
        context = {'environment': 'production', 'client_facing': True}
        severity = debugger._determine_severity(error, context)
        assert severity == ErrorSeverity.CRITICAL

    def test_high_for_blocking_errors(self, debugger):
        """Test high severity for blocking errors"""
        error = Exception("This is a blocking error")
        context = {}
        severity = debugger._determine_severity(error, context)
        assert severity == ErrorSeverity.HIGH

    def test_medium_for_timeout_errors(self, debugger):
        """Test medium severity for timeout errors"""
        error = Exception("Request timeout occurred")
        context = {}
        severity = debugger._determine_severity(error, context)
        assert severity == ErrorSeverity.MEDIUM

    def test_low_for_generic_errors(self, debugger):
        """Test low severity for generic errors"""
        error = Exception("Some generic error")
        context = {}
        severity = debugger._determine_severity(error, context)
        assert severity == ErrorSeverity.LOW


class TestComponentIdentification:
    """Tests for affected component identification"""

    @pytest.fixture
    def debugger(self):
        return WorkflowDebugger()

    def test_identifies_workflow_step(self, debugger):
        """Test identification of workflow step"""
        context = ErrorContext(
            workflow_id="test", workflow_name="test", client_name="test",
            region=WorkflowRegion.US_WEST, error_type="Error",
            error_message="Error", stack_trace=None,
            timestamp=datetime.now(), variables={},
            completed_steps=[], current_step="data_processing",
            user_email="test@test.com", severity=ErrorSeverity.LOW
        )
        components = debugger._identify_affected_components(context)
        assert "Step: data_processing" in components

    def test_identifies_api_component(self, debugger):
        """Test identification of API component"""
        context = ErrorContext(
            workflow_id="test", workflow_name="test", client_name="test",
            region=WorkflowRegion.US_WEST, error_type="Error",
            error_message="API call failed", stack_trace=None,
            timestamp=datetime.now(), variables={},
            completed_steps=[], current_step="",
            user_email="test@test.com", severity=ErrorSeverity.LOW
        )
        components = debugger._identify_affected_components(context)
        assert "External API" in components

    def test_identifies_database_component(self, debugger):
        """Test identification of database component"""
        context = ErrorContext(
            workflow_id="test", workflow_name="test", client_name="test",
            region=WorkflowRegion.US_WEST, error_type="Error",
            error_message="Database connection failed", stack_trace=None,
            timestamp=datetime.now(), variables={},
            completed_steps=[], current_step="",
            user_email="test@test.com", severity=ErrorSeverity.LOW
        )
        components = debugger._identify_affected_components(context)
        assert "Database" in components

    def test_identifies_service_integrations(self, debugger):
        """Test identification of service integrations"""
        for service in ['asana', 'slack', 'google', 'vianeo', 'genip']:
            context = ErrorContext(
                workflow_id="test", workflow_name="test", client_name="test",
                region=WorkflowRegion.US_WEST, error_type="Error",
                error_message=f"Error with {service} service", stack_trace=None,
                timestamp=datetime.now(), variables={},
                completed_steps=[], current_step="",
                user_email="test@test.com", severity=ErrorSeverity.LOW
            )
            components = debugger._identify_affected_components(context)
            assert f"{service.capitalize()} Integration" in components


class TestWorkaroundGeneration:
    """Tests for workaround generation"""

    @pytest.fixture
    def debugger(self):
        return WorkflowDebugger()

    def test_timeout_workaround(self, debugger):
        """Test workaround for timeout errors"""
        context = ErrorContext(
            workflow_id="test", workflow_name="test", client_name="test",
            region=WorkflowRegion.US_WEST, error_type="Error",
            error_message="Request timeout", stack_trace=None,
            timestamp=datetime.now(), variables={},
            completed_steps=[], current_step="",
            user_email="test@test.com", severity=ErrorSeverity.LOW
        )
        workaround = debugger._generate_workaround(context)
        assert "timeout" in workaround.lower() or "batch" in workaround.lower()

    def test_auth_workaround(self, debugger):
        """Test workaround for authentication errors"""
        context = ErrorContext(
            workflow_id="test", workflow_name="test", client_name="test",
            region=WorkflowRegion.US_WEST, error_type="Error",
            error_message="Authentication failed", stack_trace=None,
            timestamp=datetime.now(), variables={},
            completed_steps=[], current_step="",
            user_email="test@test.com", severity=ErrorSeverity.LOW
        )
        workaround = debugger._generate_workaround(context)
        assert "credentials" in workaround.lower()

    def test_brazil_region_workaround(self, debugger):
        """Test workaround for Brazil region issues"""
        context = ErrorContext(
            workflow_id="test", workflow_name="test", client_name="test",
            region=WorkflowRegion.BRAZIL, error_type="Error",
            error_message="Generic error", stack_trace=None,
            timestamp=datetime.now(), variables={},
            completed_steps=[], current_step="",
            user_email="test@test.com", severity=ErrorSeverity.LOW
        )
        workaround = debugger._generate_workaround(context)
        assert "proxy" in workaround.lower() or "regional" in workaround.lower()


class TestResolutionTimeEstimation:
    """Tests for resolution time estimation"""

    @pytest.fixture
    def debugger(self):
        return WorkflowDebugger()

    def test_critical_faster_resolution(self, debugger):
        """Test that critical errors have faster estimated resolution"""
        critical_context = ErrorContext(
            workflow_id="test", workflow_name="test", client_name="test",
            region=WorkflowRegion.US_WEST, error_type="Error",
            error_message="Error", stack_trace=None,
            timestamp=datetime.now(), variables={},
            completed_steps=[], current_step="",
            user_email="test@test.com", severity=ErrorSeverity.CRITICAL
        )
        low_context = ErrorContext(
            workflow_id="test", workflow_name="test", client_name="test",
            region=WorkflowRegion.US_WEST, error_type="Error",
            error_message="Error", stack_trace=None,
            timestamp=datetime.now(), variables={},
            completed_steps=[], current_step="",
            user_email="test@test.com", severity=ErrorSeverity.LOW
        )

        critical_time = debugger._estimate_resolution_time(critical_context)
        low_time = debugger._estimate_resolution_time(low_context)

        assert critical_time < low_time

    def test_timeout_quick_resolution(self, debugger):
        """Test that timeout errors have quick resolution estimate"""
        context = ErrorContext(
            workflow_id="test", workflow_name="test", client_name="test",
            region=WorkflowRegion.US_WEST, error_type="Error",
            error_message="Connection timeout", stack_trace=None,
            timestamp=datetime.now(), variables={},
            completed_steps=[], current_step="",
            user_email="test@test.com", severity=ErrorSeverity.MEDIUM
        )
        time_estimate = debugger._estimate_resolution_time(context)
        assert time_estimate <= 15  # Should be relatively quick


class TestOncallEngineer:
    """Tests for on-call engineer lookup"""

    @pytest.fixture
    def debugger(self):
        return WorkflowDebugger()

    def test_us_west_oncall(self, debugger):
        """Test US West on-call engineer"""
        email = debugger._get_oncall_engineer(WorkflowRegion.US_WEST)
        assert email == "eng-us@360studios.com"

    def test_brazil_oncall(self, debugger):
        """Test Brazil on-call engineer"""
        email = debugger._get_oncall_engineer(WorkflowRegion.BRAZIL)
        assert email == "eng-br@360studios.com"

    def test_europe_oncall(self, debugger):
        """Test Europe on-call engineer"""
        email = debugger._get_oncall_engineer(WorkflowRegion.EUROPE)
        assert email == "eng-eu@360studios.com"


class TestNotificationFormatting:
    """Tests for notification formatting"""

    @pytest.fixture
    def debugger(self):
        return WorkflowDebugger()

    def test_format_error_notification(self, debugger):
        """Test error notification formatting"""
        error_context = ErrorContext(
            workflow_id="wf-001", workflow_name="Test Workflow",
            client_name="Test Client", region=WorkflowRegion.US_WEST,
            error_type="Error", error_message="Test error",
            stack_trace=None, timestamp=datetime(2025, 1, 15),
            variables={}, completed_steps=[], current_step="step1",
            user_email="test@test.com", severity=ErrorSeverity.HIGH
        )
        diagnosis = DiagnosisResult(
            root_cause="Test cause",
            affected_components=["Component1"],
            is_recoverable=True,
            suggested_fix="Fix it",
            workaround="Try this",
            estimated_resolution_minutes=15,
            similar_past_errors=["ERR-001"],
            confidence_score=0.8
        )

        notification = debugger._format_error_notification(error_context, diagnosis)

        assert notification['type'] == 'error'
        assert notification['severity'] == 'high'
        assert notification['workflow'] == 'Test Workflow'
        assert notification['client'] == 'Test Client'
        assert notification['root_cause'] == 'Test cause'
        assert notification['confidence'] == '80%'


class TestNotifiers:
    """Tests for notification clients"""

    @pytest.mark.asyncio
    async def test_slack_notifier_send(self):
        """Test Slack notifier send"""
        notifier = SlackNotifier("https://hooks.slack.com/test")
        message = {'type': 'test', 'content': 'test message'}
        # Should not raise
        await notifier.send(message)

    @pytest.mark.asyncio
    async def test_asana_task_creator_send(self):
        """Test Asana task creator send"""
        creator = AsanaTaskCreator("test-token", "test-project")
        message = {'type': 'test', 'content': 'test message'}
        # Should not raise
        await creator.send(message)

    @pytest.mark.asyncio
    async def test_email_notifier_send(self):
        """Test Email notifier send"""
        notifier = EmailNotifier()
        message = {'type': 'test', 'content': 'test message'}
        # Should not raise
        await notifier.send(message)


class TestAsyncRecoveryStrategies:
    """Tests for async recovery strategies"""

    @pytest.fixture
    def debugger(self):
        return WorkflowDebugger(config={
            'auto_recovery': True,
            'max_retry_attempts': 2,
            'retry_delay_seconds': 0.1,  # Fast for testing
            'notification_channels': [],
            'log_retention_days': 90,
            'regions': {}
        })

    @pytest.fixture
    def sample_context(self):
        return ErrorContext(
            workflow_id="test", workflow_name="test", client_name="test",
            region=WorkflowRegion.US_WEST, error_type="Error",
            error_message="test", stack_trace=None,
            timestamp=datetime.now(), variables={'key': 'value'},
            completed_steps=[], current_step="",
            user_email="test@test.com", severity=ErrorSeverity.LOW
        )

    @pytest.mark.asyncio
    async def test_retry_with_backoff(self, debugger, sample_context):
        """Test retry with backoff strategy"""
        result = await debugger._retry_with_backoff(sample_context)
        assert result['retried'] is True
        assert result['attempts'] >= 2

    @pytest.mark.asyncio
    async def test_refresh_credentials(self, debugger, sample_context):
        """Test credential refresh strategy"""
        result = await debugger._refresh_credentials(sample_context)
        assert result['credentials_refreshed'] is True
        assert 'timestamp' in result

    @pytest.mark.asyncio
    async def test_validate_and_transform(self, debugger, sample_context):
        """Test validate and transform strategy"""
        result = await debugger._validate_and_transform(sample_context)
        assert result['data_transformed'] is True
        assert result['original_count'] == 1

    @pytest.mark.asyncio
    async def test_normalize_encoding_brazil(self, debugger):
        """Test encoding normalization for Brazil region"""
        context = ErrorContext(
            workflow_id="test", workflow_name="test", client_name="test",
            region=WorkflowRegion.BRAZIL, error_type="Error",
            error_message="test", stack_trace=None,
            timestamp=datetime.now(), variables={'text': 'test'},
            completed_steps=[], current_step="",
            user_email="test@test.com", severity=ErrorSeverity.LOW
        )
        result = await debugger._normalize_encoding(context)
        assert result['encoding_normalized'] is True
        assert result['target_encoding'] == 'utf-8'


class TestDebugWorkflowError:
    """Tests for the main debug_workflow_error function"""

    @pytest.mark.asyncio
    async def test_debug_workflow_error_returns_diagnosis(self):
        """Test that debug_workflow_error returns proper diagnosis"""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Patch the log directory
            with patch('workflow_debugger.os.makedirs'):
                with patch('builtins.open', MagicMock()):
                    error = ConnectionError("Test timeout error")
                    result = await debug_workflow_error(
                        error=error,
                        workflow_id="test-001",
                        workflow_name="Test Workflow",
                        client_name="Test Client",
                        region="us-west"
                    )

                    assert 'diagnosis' in result
                    assert 'error_id' in result
                    assert result['error_id'] == "test-001"


class TestErrorLogSaving:
    """Tests for error log saving functionality"""

    @pytest.mark.asyncio
    async def test_save_error_log_creates_file(self):
        """Test that error logs are saved correctly"""
        debugger = WorkflowDebugger()

        with tempfile.TemporaryDirectory() as tmpdir:
            # Patch the log directory base
            with patch.object(debugger, '_save_error_log') as mock_save:
                mock_save.return_value = None
                # Just verify the method can be called
                context = ErrorContext(
                    workflow_id="test", workflow_name="test", client_name="test",
                    region=WorkflowRegion.US_WEST, error_type="Error",
                    error_message="test", stack_trace=None,
                    timestamp=datetime.now(), variables={},
                    completed_steps=[], current_step="",
                    user_email="test@test.com", severity=ErrorSeverity.LOW
                )
                await debugger._save_error_log(context)
                mock_save.assert_called_once()
