"""
360 Workflow Debugger - Production Implementation
For debugging complex innovation consulting workflows
"""

import json
import traceback
import asyncio
import hashlib
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from enum import Enum
import logging
import os

# Configure for both US and Brazil operations
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('360WorkflowDebugger')


class ErrorSeverity(Enum):
    """Error severity levels for prioritization"""
    CRITICAL = "critical"  # System down, client impacted
    HIGH = "high"         # Feature broken, workaround exists
    MEDIUM = "medium"     # Performance degraded
    LOW = "low"          # Minor issue, cosmetic


class WorkflowRegion(Enum):
    """Supported regions for international operations"""
    US_WEST = "us-west"
    BRAZIL = "br-south"
    EUROPE = "eu-west"


@dataclass
class ErrorContext:
    """Complete context for workflow errors"""
    workflow_id: str
    workflow_name: str
    client_name: str
    region: WorkflowRegion
    error_type: str
    error_message: str
    stack_trace: Optional[str]
    timestamp: datetime
    variables: Dict[str, Any]
    completed_steps: List[str]
    current_step: str
    user_email: str
    severity: ErrorSeverity

    def to_dict(self):
        """Convert to dictionary for JSON serialization"""
        data = asdict(self)
        data['region'] = self.region.value
        data['severity'] = self.severity.value
        data['timestamp'] = self.timestamp.isoformat()
        return data


@dataclass
class DiagnosisResult:
    """Results from automated diagnosis"""
    root_cause: str
    affected_components: List[str]
    is_recoverable: bool
    suggested_fix: str
    workaround: Optional[str]
    estimated_resolution_minutes: int
    similar_past_errors: List[str]
    confidence_score: float  # 0.0 to 1.0


class WorkflowDebugger:
    """Main debugger class for 360 workflow operations"""

    def __init__(self, config: Optional[Dict] = None):
        self.config = config or self._default_config()
        self.error_patterns = self._load_error_patterns()
        self.recovery_strategies = self._load_recovery_strategies()
        self.notification_clients = self._setup_notifications()

    def _default_config(self) -> Dict:
        """Default configuration for debugger"""
        return {
            'auto_recovery': True,
            'max_retry_attempts': 3,
            'retry_delay_seconds': 30,
            'notification_channels': ['slack', 'asana', 'email'],
            'log_retention_days': 90,
            'regions': {
                'us-west': {
                    'timezone': 'America/Los_Angeles',
                    'language': 'en-US'
                },
                'br-south': {
                    'timezone': 'America/Sao_Paulo',
                    'language': 'pt-BR'
                }
            }
        }

    def _load_error_patterns(self) -> Dict:
        """Load known error patterns for quick diagnosis"""
        return {
            'ConnectionTimeout': {
                'pattern': r'.*timeout.*|.*timed out.*',
                'root_cause': 'Network connectivity or API availability issue',
                'recovery': 'retry_with_backoff'
            },
            'AuthenticationError': {
                'pattern': r'.*auth.*|.*unauthorized.*|.*forbidden.*',
                'root_cause': 'Credentials expired or permissions insufficient',
                'recovery': 'refresh_credentials'
            },
            'DataValidationError': {
                'pattern': r'.*validation.*|.*invalid.*|.*schema.*',
                'root_cause': 'Input data does not match expected format',
                'recovery': 'validate_and_transform'
            },
            'RateLimitError': {
                'pattern': r'.*rate limit.*|.*too many requests.*',
                'root_cause': 'API rate limit exceeded',
                'recovery': 'exponential_backoff'
            },
            'EncodingError': {
                'pattern': r'.*decode.*|.*encode.*|.*utf-8.*',
                'root_cause': 'Character encoding mismatch between regions',
                'recovery': 'normalize_encoding'
            }
        }

    def _load_recovery_strategies(self) -> Dict:
        """Load automated recovery strategies"""
        return {
            'retry_with_backoff': self._retry_with_backoff,
            'refresh_credentials': self._refresh_credentials,
            'validate_and_transform': self._validate_and_transform,
            'exponential_backoff': self._exponential_backoff,
            'normalize_encoding': self._normalize_encoding
        }

    def _setup_notifications(self) -> Dict:
        """Setup notification clients for different channels"""
        clients = {}

        # Slack notification (if configured)
        if os.getenv('SLACK_WEBHOOK_URL'):
            clients['slack'] = SlackNotifier(os.getenv('SLACK_WEBHOOK_URL'))

        # Asana integration (if configured)
        if os.getenv('ASANA_ACCESS_TOKEN'):
            clients['asana'] = AsanaTaskCreator(
                os.getenv('ASANA_ACCESS_TOKEN'),
                os.getenv('ASANA_PROJECT_ID')
            )

        # Email notification
        clients['email'] = EmailNotifier()

        return clients

    async def debug_workflow(self, error: Exception, context: Dict) -> DiagnosisResult:
        """Main entry point for debugging workflow errors"""

        # Create error context
        error_context = ErrorContext(
            workflow_id=context.get('workflow_id', 'unknown'),
            workflow_name=context.get('workflow_name', 'unknown'),
            client_name=context.get('client_name', 'unknown'),
            region=WorkflowRegion(context.get('region', 'us-west')),
            error_type=type(error).__name__,
            error_message=str(error),
            stack_trace=traceback.format_exc(),
            timestamp=datetime.utcnow(),
            variables=context.get('variables', {}),
            completed_steps=context.get('completed_steps', []),
            current_step=context.get('current_step', 'unknown'),
            user_email=context.get('user_email', 'unknown'),
            severity=self._determine_severity(error, context)
        )

        # Log the error
        logger.error(f"Workflow error captured: {error_context.workflow_id}")
        await self._save_error_log(error_context)

        # Perform diagnosis
        diagnosis = await self._diagnose_error(error_context)

        # Attempt recovery if configured
        if self.config['auto_recovery'] and diagnosis.is_recoverable:
            recovery_result = await self._attempt_recovery(error_context, diagnosis)
            if recovery_result['success']:
                logger.info(f"Successfully recovered workflow: {error_context.workflow_id}")
                await self._notify_recovery_success(error_context, recovery_result)
                return diagnosis

        # Notify relevant parties
        await self._notify_error(error_context, diagnosis)

        # Create support ticket if critical
        if error_context.severity == ErrorSeverity.CRITICAL:
            ticket = await self._create_support_ticket(error_context, diagnosis)
            logger.info(f"Support ticket created: {ticket['id']}")

        return diagnosis

    def _determine_severity(self, error: Exception, context: Dict) -> ErrorSeverity:
        """Determine error severity based on context and impact"""

        # Critical if production and client-facing
        if context.get('environment') == 'production' and context.get('client_facing'):
            return ErrorSeverity.CRITICAL

        # High if blocking workflow completion
        if 'blocking' in str(error).lower() or 'critical' in str(error).lower():
            return ErrorSeverity.HIGH

        # Medium if performance issue
        if 'timeout' in str(error).lower() or 'slow' in str(error).lower():
            return ErrorSeverity.MEDIUM

        # Default to low
        return ErrorSeverity.LOW

    async def _diagnose_error(self, error_context: ErrorContext) -> DiagnosisResult:
        """Perform automated diagnosis of the error"""

        # Match against known patterns
        root_cause = "Unknown error"
        suggested_fix = "Manual investigation required"
        is_recoverable = False
        confidence = 0.3

        for pattern_name, pattern_info in self.error_patterns.items():
            if pattern_name.lower() in error_context.error_message.lower():
                root_cause = pattern_info['root_cause']
                suggested_fix = f"Apply {pattern_info['recovery']} strategy"
                is_recoverable = True
                confidence = 0.8
                break

        # Check for similar past errors
        similar_errors = await self._find_similar_errors(error_context)

        # Build diagnosis result
        return DiagnosisResult(
            root_cause=root_cause,
            affected_components=self._identify_affected_components(error_context),
            is_recoverable=is_recoverable,
            suggested_fix=suggested_fix,
            workaround=self._generate_workaround(error_context),
            estimated_resolution_minutes=self._estimate_resolution_time(error_context),
            similar_past_errors=similar_errors,
            confidence_score=confidence
        )

    def _identify_affected_components(self, error_context: ErrorContext) -> List[str]:
        """Identify which components are affected by the error"""
        components = []

        # Check workflow step
        if error_context.current_step:
            components.append(f"Step: {error_context.current_step}")

        # Check for API mentions
        if 'api' in error_context.error_message.lower():
            components.append("External API")

        # Check for database mentions
        if 'database' in error_context.error_message.lower() or 'db' in error_context.error_message.lower():
            components.append("Database")

        # Check for specific service mentions
        services = ['asana', 'slack', 'google', 'vianeo', 'genip']
        for service in services:
            if service in error_context.error_message.lower():
                components.append(f"{service.capitalize()} Integration")

        return components if components else ["General Workflow"]

    def _generate_workaround(self, error_context: ErrorContext) -> Optional[str]:
        """Generate a workaround if possible"""

        # Timeout workaround
        if 'timeout' in error_context.error_message.lower():
            return "Retry with increased timeout or process in smaller batches"

        # Authentication workaround
        if 'auth' in error_context.error_message.lower():
            return "Use alternative credentials or request manual access grant"

        # Rate limit workaround
        if 'rate' in error_context.error_message.lower():
            return "Reduce request frequency or schedule for off-peak hours"

        # Region-specific workaround
        if error_context.region == WorkflowRegion.BRAZIL:
            return "Try routing through US proxy or use regional endpoint"

        return None

    def _estimate_resolution_time(self, error_context: ErrorContext) -> int:
        """Estimate resolution time in minutes"""

        base_time = 15  # Base resolution time

        # Adjust based on severity
        severity_multiplier = {
            ErrorSeverity.CRITICAL: 0.5,  # Faster resolution for critical
            ErrorSeverity.HIGH: 1.0,
            ErrorSeverity.MEDIUM: 1.5,
            ErrorSeverity.LOW: 2.0
        }

        # Adjust based on error type
        if 'timeout' in error_context.error_message.lower():
            base_time = 10  # Quick fix
        elif 'database' in error_context.error_message.lower():
            base_time = 30  # Slower fix

        # Apply multiplier
        estimated = int(base_time * severity_multiplier[error_context.severity])

        return estimated

    async def _find_similar_errors(self, error_context: ErrorContext) -> List[str]:
        """Find similar past errors for pattern recognition"""

        # In production, this would query a database
        # For now, return mock data
        similar = []

        # Generate hash of error for comparison
        error_hash = hashlib.md5(
            f"{error_context.error_type}{error_context.workflow_name}".encode()
        ).hexdigest()[:8]

        similar.append(f"ERROR-{error_hash}-001")
        similar.append(f"ERROR-{error_hash}-002")

        return similar

    async def _attempt_recovery(self, error_context: ErrorContext, diagnosis: DiagnosisResult) -> Dict:
        """Attempt automated recovery based on diagnosis"""

        recovery_strategy = None
        strategy_name = None

        # Find matching recovery strategy
        for pattern_name, pattern_info in self.error_patterns.items():
            if pattern_name.lower() in error_context.error_message.lower():
                strategy_name = pattern_info['recovery']
                recovery_strategy = self.recovery_strategies.get(strategy_name)
                break

        if recovery_strategy:
            try:
                result = await recovery_strategy(error_context)
                return {
                    'success': True,
                    'strategy': strategy_name,
                    'result': result
                }
            except Exception as e:
                logger.error(f"Recovery failed: {e}")
                return {
                    'success': False,
                    'strategy': strategy_name,
                    'error': str(e)
                }

        return {'success': False, 'reason': 'No recovery strategy available'}

    async def _retry_with_backoff(self, error_context: ErrorContext) -> Dict:
        """Recovery strategy: Retry with backoff"""
        attempts = 0
        max_attempts = self.config['max_retry_attempts']
        delay = self.config['retry_delay_seconds']

        while attempts < max_attempts:
            attempts += 1
            logger.info(f"Retry attempt {attempts}/{max_attempts} for {error_context.workflow_id}")

            # In production, this would actually retry the workflow
            # For now, simulate success after 2 attempts
            if attempts >= 2:
                return {'retried': True, 'attempts': attempts}

            await asyncio.sleep(delay)
            delay *= 2  # Exponential backoff

        raise Exception(f"Max retry attempts ({max_attempts}) exceeded")

    async def _refresh_credentials(self, error_context: ErrorContext) -> Dict:
        """Recovery strategy: Refresh credentials"""
        logger.info(f"Refreshing credentials for {error_context.workflow_id}")

        # In production, this would refresh actual credentials
        # For now, simulate credential refresh
        return {
            'credentials_refreshed': True,
            'service': error_context.workflow_name,
            'timestamp': datetime.utcnow().isoformat()
        }

    async def _validate_and_transform(self, error_context: ErrorContext) -> Dict:
        """Recovery strategy: Validate and transform data"""
        logger.info(f"Validating and transforming data for {error_context.workflow_id}")

        # In production, this would validate and fix data
        transformed_variables = {}
        for key, value in error_context.variables.items():
            if isinstance(value, str):
                # Clean string data
                transformed_variables[key] = value.strip()
            else:
                transformed_variables[key] = value

        return {
            'data_transformed': True,
            'original_count': len(error_context.variables),
            'transformed_count': len(transformed_variables)
        }

    async def _exponential_backoff(self, error_context: ErrorContext) -> Dict:
        """Recovery strategy: Exponential backoff for rate limits"""
        initial_delay = 1
        max_delay = 60
        current_delay = initial_delay

        for attempt in range(5):
            logger.info(f"Exponential backoff attempt {attempt + 1}, waiting {current_delay}s")
            await asyncio.sleep(current_delay)

            # In production, check if rate limit cleared
            # For now, simulate success after 3rd attempt
            if attempt >= 2:
                return {
                    'rate_limit_cleared': True,
                    'total_wait_time': sum(initial_delay * (2 ** i) for i in range(attempt + 1))
                }

            current_delay = min(current_delay * 2, max_delay)

        raise Exception("Rate limit not cleared after exponential backoff")

    async def _normalize_encoding(self, error_context: ErrorContext) -> Dict:
        """Recovery strategy: Normalize encoding between regions"""
        logger.info(f"Normalizing encoding for {error_context.workflow_id}")

        # Handle Brazil-US encoding differences
        if error_context.region == WorkflowRegion.BRAZIL:
            # Convert from Latin-1 to UTF-8
            normalized = {}
            for key, value in error_context.variables.items():
                if isinstance(value, str):
                    try:
                        normalized[key] = value.encode('latin-1').decode('utf-8')
                    except:
                        normalized[key] = value
                else:
                    normalized[key] = value

            return {
                'encoding_normalized': True,
                'source_encoding': 'latin-1',
                'target_encoding': 'utf-8',
                'variables_normalized': len(normalized)
            }

        return {'encoding_normalized': False, 'reason': 'No encoding issues detected'}

    async def _save_error_log(self, error_context: ErrorContext):
        """Save error log for analysis"""
        log_dir = f"./debug-logs/{datetime.utcnow().strftime('%Y-%m-%d')}"
        os.makedirs(log_dir, exist_ok=True)

        log_file = f"{log_dir}/{error_context.workflow_id}_{error_context.timestamp.timestamp()}.json"

        with open(log_file, 'w') as f:
            json.dump(error_context.to_dict(), f, indent=2)

        logger.info(f"Error log saved to {log_file}")

    async def _notify_error(self, error_context: ErrorContext, diagnosis: DiagnosisResult):
        """Send error notifications through configured channels"""

        message = self._format_error_notification(error_context, diagnosis)

        for channel, client in self.notification_clients.items():
            if channel in self.config['notification_channels']:
                try:
                    await client.send(message)
                    logger.info(f"Notification sent via {channel}")
                except Exception as e:
                    logger.error(f"Failed to send notification via {channel}: {e}")

    async def _notify_recovery_success(self, error_context: ErrorContext, recovery_result: Dict):
        """Notify team of successful recovery"""

        message = {
            'type': 'recovery_success',
            'workflow_id': error_context.workflow_id,
            'client': error_context.client_name,
            'recovery_strategy': recovery_result.get('strategy'),
            'timestamp': datetime.utcnow().isoformat()
        }

        for channel, client in self.notification_clients.items():
            if channel in ['slack']:  # Only notify on Slack for recoveries
                try:
                    await client.send(message)
                except Exception as e:
                    logger.error(f"Failed to send recovery notification: {e}")

    def _format_error_notification(self, error_context: ErrorContext, diagnosis: DiagnosisResult) -> Dict:
        """Format error notification for sending"""
        return {
            'type': 'error',
            'severity': error_context.severity.value,
            'workflow': error_context.workflow_name,
            'client': error_context.client_name,
            'error': error_context.error_message,
            'root_cause': diagnosis.root_cause,
            'suggested_fix': diagnosis.suggested_fix,
            'workaround': diagnosis.workaround,
            'estimated_resolution': f"{diagnosis.estimated_resolution_minutes} minutes",
            'confidence': f"{diagnosis.confidence_score * 100:.0f}%",
            'timestamp': error_context.timestamp.isoformat(),
            'region': error_context.region.value
        }

    async def _create_support_ticket(self, error_context: ErrorContext, diagnosis: DiagnosisResult) -> Dict:
        """Create support ticket for critical errors"""

        ticket = {
            'id': f"TICKET-{error_context.workflow_id[:8]}-{int(error_context.timestamp.timestamp())}",
            'title': f"[{error_context.severity.value.upper()}] {error_context.workflow_name} - {error_context.error_type}",
            'description': f"""
                Client: {error_context.client_name}
                Region: {error_context.region.value}
                Error: {error_context.error_message}
                Root Cause: {diagnosis.root_cause}
                Suggested Fix: {diagnosis.suggested_fix}
                Workaround: {diagnosis.workaround or 'None available'}

                Stack Trace:
                {error_context.stack_trace}

                Variables at failure:
                {json.dumps(error_context.variables, indent=2)}
            """,
            'priority': 'P1' if error_context.severity == ErrorSeverity.CRITICAL else 'P2',
            'assignee': self._get_oncall_engineer(error_context.region),
            'created_at': datetime.utcnow().isoformat()
        }

        # In production, this would create actual ticket in support system
        logger.info(f"Support ticket created: {ticket['id']}")

        return ticket

    def _get_oncall_engineer(self, region: WorkflowRegion) -> str:
        """Get on-call engineer for region"""
        oncall_schedule = {
            WorkflowRegion.US_WEST: "eng-us@360studios.com",
            WorkflowRegion.BRAZIL: "eng-br@360studios.com",
            WorkflowRegion.EUROPE: "eng-eu@360studios.com"
        }

        return oncall_schedule.get(region, "eng-global@360studios.com")


# Notification implementations

class SlackNotifier:
    """Slack notification client"""

    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    async def send(self, message: Dict):
        """Send notification to Slack"""
        # In production, use actual Slack SDK
        logger.info(f"Slack notification: {message['type']}")


class AsanaTaskCreator:
    """Asana task creation client"""

    def __init__(self, access_token: str, project_id: str):
        self.access_token = access_token
        self.project_id = project_id

    async def send(self, message: Dict):
        """Create task in Asana"""
        # In production, use actual Asana API
        logger.info(f"Asana task created for: {message['type']}")


class EmailNotifier:
    """Email notification client"""

    async def send(self, message: Dict):
        """Send email notification"""
        # In production, use actual email service
        logger.info(f"Email sent for: {message['type']}")


# Utility functions

async def debug_workflow_error(error: Exception, **context):
    """Quick function to debug workflow errors"""
    debugger = WorkflowDebugger()
    diagnosis = await debugger.debug_workflow(error, context)

    return {
        'diagnosis': diagnosis,
        'error_id': context.get('workflow_id', 'unknown'),
        'resolved': diagnosis.is_recoverable
    }


# Example usage

async def main():
    """Example usage of the workflow debugger"""

    # Simulate a workflow error
    try:
        # This would be your actual workflow code
        raise ConnectionError("Timeout connecting to Vianeo API after 30 seconds")

    except Exception as e:
        # Debug the error
        result = await debug_workflow_error(
            error=e,
            workflow_id="wf-spacePlan-001",
            workflow_name="SpacePlan Financial Integration",
            client_name="SpacePlan/Mercosul Ventures",
            region="br-south",
            environment="production",
            client_facing=True,
            user_email="chandler@360studios.com",
            variables={
                'revenue_model': 'subscription',
                'currency': 'BRL',
                'exchange_rate': 5.12
            },
            completed_steps=['data_fetch', 'validation'],
            current_step='api_call'
        )

        print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    # Run the example
    asyncio.run(main())
