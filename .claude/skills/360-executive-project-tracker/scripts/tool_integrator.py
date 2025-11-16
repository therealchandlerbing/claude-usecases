"""
Tool Integration Module for 360 Project Status Tracker
Connects to Claude tools for Gmail, Calendar, and Drive data collection
"""

import json
import re
from datetime import datetime, timedelta
from typing import List, Dict, Any

class ToolIntegrator:
    """Integrates with Claude tools to collect task data"""

    def __init__(self):
        self.collected_tasks = []
        self.collection_log = []

    def collect_from_gmail(self, days_back=7, project_keywords=None):
        """
        Collect task information from Gmail.
        Uses search_gmail_messages and read_gmail_thread tools.

        Args:
            days_back: Days to look back
            project_keywords: Optional list of project names to focus on

        Returns:
            List of task dictionaries
        """
        tasks = []

        # Calculate date for search query
        cutoff_date = datetime.now() - timedelta(days=days_back)
        date_str = cutoff_date.strftime('%Y/%m/%d')

        # Define search queries
        search_queries = [
            f'after:{date_str} (status update OR weekly update)',
            f'after:{date_str} (blocker OR blocked OR blocked on)',
            f'after:{date_str} (working on OR currently working)',
            f'after:{date_str} (completed OR finished OR shipped)',
            f'after:{date_str} subject:(status OR update OR progress)',
        ]

        # Add project-specific searches if provided
        if project_keywords:
            for keyword in project_keywords:
                search_queries.append(f'after:{date_str} "{keyword}"')

        # Return the search plan structure
        # Actual tool calls would happen here in live mode
        gmail_plan = {
            'tool': 'search_gmail_messages',
            'queries': search_queries,
            'extraction_method': 'parse_email_for_tasks',
            'expected_patterns': {
                'task': r'(?:working on|task:|TODO:)\s*(.+?)(?:\n|$)',
                'status': r'(?:status:|is)\s*(not started|in progress|blocked|done)',
                'blocker': r'(?:blocked? (?:by|on)|blocker:)\s*(.+?)(?:\n|$)',
                'owner': r'(?:owner:|assigned to:)\s*(.+?)(?:\n|$)',
                'priority': r'(?:priority:)\s*(low|medium|high|critical)',
            }
        }

        self.collection_log.append({
            'source': 'gmail',
            'queries_planned': len(search_queries),
            'method': 'search_gmail_messages'
        })

        return tasks, gmail_plan

    def collect_from_calendar(self, days_back=7):
        """
        Collect task information from Google Calendar.
        Uses list_gcal_events tool.

        Args:
            days_back: Days to look back

        Returns:
            List of task dictionaries
        """
        tasks = []

        # Calculate time range
        time_min = (datetime.now() - timedelta(days=days_back)).isoformat() + 'Z'
        time_max = datetime.now().isoformat() + 'Z'

        # Return the calendar search plan
        calendar_plan = {
            'tool': 'list_gcal_events',
            'parameters': {
                'calendar_id': 'primary',
                'time_min': time_min,
                'time_max': time_max,
                'max_results': 50
            },
            'extraction_method': 'parse_event_for_tasks',
            'extract_from': ['description', 'summary', 'attendees'],
            'action_patterns': [
                r'action item:\s*(.+?)(?:\n|$)',
                r'TODO:\s*(.+?)(?:\n|$)',
                r'follow up:\s*(.+?)(?:\n|$)',
                r'next steps?:\s*(.+?)(?:\n|$)',
                r'\[\s?\]\s*(.+?)(?:\n|$)',  # Unchecked checkbox
                r'\[x\]\s*(.+?)(?:\n|$)',    # Checked checkbox
            ]
        }

        self.collection_log.append({
            'source': 'calendar',
            'time_range': f'{time_min} to {time_max}',
            'method': 'list_gcal_events'
        })

        return tasks, calendar_plan

    def collect_from_drive(self, days_back=7, folders=None):
        """
        Collect task information from Google Drive.
        Uses google_drive_search tool.

        Args:
            days_back: Days to look back
            folders: List of folder configs or single folder name string
                    Format: [{'name': 'Folder Name', 'folder_id': 'optional_id'}, ...]
                    Or: 'Folder Name' (single string for backwards compatibility)

        Returns:
            List of task dictionaries and list of drive plans
        """
        tasks = []

        # Handle backwards compatibility: convert string to list format
        if folders is None:
            folders = [{'name': 'A - Processed Meeting Deliverables'}]
        elif isinstance(folders, str):
            folders = [{'name': folders}]

        # Calculate date for Drive query
        modified_after = (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%d')

        # Build search plans for each folder
        all_drive_plans = []

        for folder_config in folders:
            folder_name = folder_config.get('name', '')
            folder_id = folder_config.get('folder_id')

            # Build query based on whether we have folder_id
            if folder_id:
                # Use folder_id directly in parent search
                api_query = f"'{folder_id}' in parents and modifiedTime > '{modified_after}T00:00:00' and mimeType = 'application/vnd.google-apps.document'"
                drive_plan = {
                    'tool': 'google_drive_search',
                    'search_steps': [
                        {
                            'step': 1,
                            'purpose': f'Search documents in folder: {folder_name}',
                            'query': {
                                'api_query': api_query,
                                'semantic_query': 'meeting notes action items tasks deliverables'
                            }
                        }
                    ],
                    'folder_reference': f'{folder_name} (ID: {folder_id})'
                }
            else:
                # Search by folder name (original behavior)
                drive_plan = {
                    'tool': 'google_drive_search',
                    'search_steps': [
                        {
                            'step': 1,
                            'purpose': 'Find target folder',
                            'query': {
                                'api_query': f"name contains '{folder_name}' and mimeType = 'application/vnd.google-apps.folder'",
                                'semantic_query': folder_name
                            }
                        },
                        {
                            'step': 2,
                            'purpose': 'Search documents in folder',
                            'query': {
                                'api_query': f"modifiedTime > '{modified_after}T00:00:00' and mimeType = 'application/vnd.google-apps.document'",
                                'semantic_query': 'meeting notes action items tasks deliverables'
                            }
                        }
                    ],
                    'folder_reference': folder_name
                }

            drive_plan['extraction_method'] = 'parse_doc_for_tasks'
            drive_plan['task_indicators'] = [
                'Action Items',
                'Tasks',
                'Next Steps',
                'TODO',
                'Follow-up',
                'Deliverables'
            ]
            drive_plan['patterns'] = {
                'section_header': r'##?\s*(Action Items?|Tasks?|Next Steps?|TODO)',
                'bullet_task': r'[-*•]\s*(.+?)(?:\n|$)',
                'numbered_task': r'\d+\.\s*(.+?)(?:\n|$)',
                'checkbox': r'\[\s?\]\s*(.+?)(?:\n|$)',
                'owner': r'@(\w+)|Owner:\s*([^,\n]+)|\(([^)]+)\)'
            }

            all_drive_plans.append(drive_plan)

            self.collection_log.append({
                'source': 'drive',
                'folder': folder_name,
                'folder_id': folder_id,
                'modified_after': modified_after,
                'method': 'google_drive_search'
            })

        return tasks, all_drive_plans

    def parse_email_for_tasks(self, email_content, email_metadata):
        """
        Parse email content to extract task information.

        Args:
            email_content: Full email text
            email_metadata: Email metadata (sender, date, subject, etc.)

        Returns:
            List of task dictionaries
        """
        tasks = []

        # Extract task descriptions
        task_patterns = [
            r'(?:working on|task:|TODO:)\s*(.+?)(?:\n|\.|$)',
            r'(?:^|\n)[-*]\s*(.+?)(?:\n|$)',
        ]

        for pattern in task_patterns:
            matches = re.finditer(pattern, email_content, re.IGNORECASE | re.MULTILINE)
            for match in matches:
                task_text = match.group(1).strip()

                # Create task entry
                task = {
                    'description': task_text,
                    'owner': self.extract_owner(email_content, email_metadata.get('from')),
                    'status': self.infer_status(task_text),
                    'priority': self.infer_priority(email_content),
                    'blocker_details': self.extract_blocker(task_text),
                    'source_context': f"Gmail: {email_metadata.get('subject')} ({email_metadata.get('date')})",
                    'next_steps': self.extract_next_steps(email_content),
                    'date': email_metadata.get('date')
                }

                tasks.append(task)

        return tasks

    def parse_event_for_tasks(self, event_data):
        """
        Parse calendar event to extract task information.

        Args:
            event_data: Calendar event dictionary

        Returns:
            List of task dictionaries
        """
        tasks = []

        # Extract text from event
        text = ''
        if event_data.get('description'):
            text += event_data['description'] + '\n'
        if event_data.get('summary'):
            text += event_data['summary'] + '\n'

        # Look for action items
        action_patterns = [
            r'action item:\s*(.+?)(?:\n|$)',
            r'TODO:\s*(.+?)(?:\n|$)',
            r'\[\s?\]\s*(.+?)(?:\n|$)',
        ]

        for pattern in action_patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE | re.MULTILINE)
            for match in matches:
                task_text = match.group(1).strip()

                # Get attendees as potential owners
                attendees = event_data.get('attendees', [])
                owner = self.extract_owner(task_text, attendees)

                task = {
                    'description': task_text,
                    'owner': owner,
                    'status': self.infer_status(task_text),
                    'priority': self.infer_priority(text),
                    'source_context': f"Calendar: {event_data.get('summary')} ({event_data.get('start', {}).get('dateTime', 'N/A')})",
                    'next_steps': '',
                    'date': event_data.get('start', {}).get('dateTime', '')
                }

                tasks.append(task)

        return tasks

    def parse_doc_for_tasks(self, doc_content, doc_metadata):
        """
        Parse Google Doc content to extract task information.

        Args:
            doc_content: Full document text
            doc_metadata: Document metadata (title, modified date, etc.)

        Returns:
            List of task dictionaries
        """
        tasks = []

        # Look for task sections
        section_pattern = r'##?\s*(Action Items?|Tasks?|Next Steps?|TODO)(.+?)(?=##|\Z)'
        sections = re.finditer(section_pattern, doc_content, re.IGNORECASE | re.DOTALL)

        for section_match in sections:
            section_text = section_match.group(2)

            # Extract individual tasks
            task_patterns = [
                r'[-*•]\s*(.+?)(?:\n|$)',
                r'\d+\.\s*(.+?)(?:\n|$)',
                r'\[\s?\]\s*(.+?)(?:\n|$)',
            ]

            for pattern in task_patterns:
                matches = re.finditer(pattern, section_text, re.MULTILINE)
                for match in matches:
                    task_text = match.group(1).strip()

                    task = {
                        'description': task_text,
                        'owner': self.extract_owner(task_text, doc_metadata.get('owner')),
                        'status': self.infer_status(task_text),
                        'priority': self.infer_priority(task_text),
                        'source_context': f"Drive: {doc_metadata.get('title')} (modified {doc_metadata.get('modifiedTime')})",
                        'next_steps': '',
                        'date': doc_metadata.get('modifiedTime')
                    }

                    tasks.append(task)

        return tasks

    def extract_owner(self, text, default='Unassigned'):
        """Extract owner/assignee from text"""
        patterns = [
            r'@(\w+)',
            r'owner:\s*([^,\n]+)',
            r'assigned to:\s*([^,\n]+)',
            r'\(([^)]+)\)',
        ]

        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip()

        return default

    def infer_status(self, text):
        """Infer task status from text"""
        text_lower = text.lower()

        if any(word in text_lower for word in ['blocked', 'blocker', 'waiting', 'stuck']):
            return 'Blocked'
        elif any(word in text_lower for word in ['done', 'completed', 'finished', 'shipped', '[x]']):
            return 'Done'
        elif any(word in text_lower for word in ['working', 'in progress', 'ongoing', 'current']):
            return 'In Progress'
        else:
            return 'Not Started'

    def infer_priority(self, text):
        """Infer priority from text"""
        text_lower = text.lower()

        if any(word in text_lower for word in ['critical', 'urgent', 'asap', 'emergency', 'p0']):
            return 'Critical'
        elif any(word in text_lower for word in ['high', 'important', 'p1']):
            return 'High'
        elif any(word in text_lower for word in ['low', 'nice to have', 'p3']):
            return 'Low'
        else:
            return 'Medium'

    def extract_blocker(self, text):
        """Extract blocker information from text"""
        blocker_patterns = [
            r'blocked? (?:by|on)\s*(.+?)(?:\.|$)',
            r'blocker:\s*(.+?)(?:\.|$)',
            r'waiting (?:on|for)\s*(.+?)(?:\.|$)',
        ]

        for pattern in blocker_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip()

        return ''

    def extract_next_steps(self, text):
        """Extract next steps from text"""
        next_steps_patterns = [
            r'next steps?:\s*(.+?)(?:\n\n|$)',
            r'follow up:\s*(.+?)(?:\n\n|$)',
            r'action:\s*(.+?)(?:\n\n|$)',
        ]

        for pattern in next_steps_patterns:
            match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).strip()[:200]  # Limit length

        return ''

    def get_collection_summary(self):
        """Return summary of data collection activities"""
        return {
            'total_sources': len(self.collection_log),
            'sources': self.collection_log,
            'tasks_collected': len(self.collected_tasks),
            'timestamp': datetime.now().isoformat()
        }
