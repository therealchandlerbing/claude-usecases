"""
Data Collection Module for 360 Project Tracker
Pulls task information from Gmail, Google Calendar, and Google Drive
"""

import re
from datetime import datetime, timedelta
from typing import List, Dict, Any
import json

class DataCollector:
    """Collects task data from various sources"""

    def __init__(self, gmail_tool, calendar_tool, drive_tool):
        self.gmail = gmail_tool
        self.calendar = calendar_tool
        self.drive = drive_tool
        self.tasks = []

    def collect_all_sources(self, days_back=7, specific_projects=None):
        """
        Collect from all sources and consolidate into task list.

        Args:
            days_back: How many days to look back
            specific_projects: List of project names to focus on (optional)

        Returns:
            List of task dictionaries
        """
        print(f"Collecting data from last {days_back} days...")

        # Collect from each source
        gmail_tasks = self.collect_from_gmail(days_back, specific_projects)
        calendar_tasks = self.collect_from_calendar(days_back)
        drive_tasks = self.collect_from_drive(days_back)

        # Consolidate and deduplicate
        all_tasks = gmail_tasks + calendar_tasks + drive_tasks
        consolidated = self.consolidate_tasks(all_tasks)

        return consolidated

    def collect_from_gmail(self, days_back=7, specific_projects=None):
        """
        Search Gmail for status updates, blockers, and task mentions.

        Returns list of task dictionaries extracted from emails.
        """
        tasks = []

        # Calculate date for Gmail query
        cutoff_date = datetime.now() - timedelta(days=days_back)
        date_filter = cutoff_date.strftime('%Y/%m/%d')

        # Search queries for different types of updates
        search_queries = [
            f'after:{date_filter} (status update OR update on)',
            f'after:{date_filter} (blocker OR blocked OR blocked on)',
            f'after:{date_filter} (working on OR currently working)',
            f'after:{date_filter} (completed OR finished OR done with)',
            f'after:{date_filter} subject:(weekly update OR status report)',
        ]

        # If specific projects mentioned, add those
        if specific_projects:
            for project in specific_projects:
                search_queries.append(f'after:{date_filter} "{project}"')

        # This is the structure we'll return for Gmail tasks
        # Actual tool calls will be added in next phase
        gmail_structure = {
            'search_queries': search_queries,
            'extract_patterns': {
                'task_description': [
                    r'working on (.+?)(?:\.|$)',
                    r'task: (.+?)(?:\.|$)',
                    r'currently (.+?)(?:\.|$)',
                ],
                'blocker': [
                    r'blocked (?:by|on) (.+?)(?:\.|$)',
                    r'blocker: (.+?)(?:\.|$)',
                    r'waiting (?:on|for) (.+?)(?:\.|$)',
                ],
                'status': [
                    r'status: (\w+)',
                    r'(?:is |currently )?(not started|in progress|blocked|done)',
                ],
                'owner': [
                    r'owner: (.+?)(?:\.|$)',
                    r'assigned to: (.+?)(?:\.|$)',
                ],
            },
            'source_type': 'gmail'
        }

        return tasks

    def collect_from_calendar(self, days_back=7):
        """
        Pull recent calendar meetings and extract action items from notes/descriptions.

        Returns list of task dictionaries from calendar events.
        """
        tasks = []

        # Calculate time range
        time_min = (datetime.now() - timedelta(days=days_back)).isoformat() + 'Z'
        time_max = datetime.now().isoformat() + 'Z'

        calendar_structure = {
            'time_range': {
                'time_min': time_min,
                'time_max': time_max,
            },
            'extract_from': [
                'event_title',
                'description',
                'notes',
                'attendees'
            ],
            'action_item_patterns': [
                r'action item: (.+?)(?:\n|$)',
                r'TODO: (.+?)(?:\n|$)',
                r'follow up: (.+?)(?:\n|$)',
                r'next steps?: (.+?)(?:\n|$)',
                r'\[ \] (.+?)(?:\n|$)',  # Checkbox items
            ],
            'assignment_patterns': [
                r'@(\w+)',  # @mentions
                r'assigned to: (.+?)(?:\n|$)',
                r'owner: (.+?)(?:\n|$)',
            ],
            'source_type': 'calendar'
        }

        return tasks

    def collect_from_drive(self, days_back=7):
        """
        Search Google Drive folder for meeting deliverables and extract tasks.

        Returns list of task dictionaries from Drive documents.
        """
        tasks = []

        # Calculate date for Drive query
        modified_after = (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%d')

        drive_structure = {
            'folder_name': 'A - Processed Meeting Deliverables',
            'search_query': f"modifiedTime > '{modified_after}' and mimeType = 'application/vnd.google-apps.document'",
            'extract_patterns': {
                'task_sections': [
                    r'## Tasks?(?:\n|$)',
                    r'## Action Items?(?:\n|$)',
                    r'## Next Steps?(?:\n|$)',
                ],
                'task_items': [
                    r'[-*] (.+?)(?:\n|$)',
                    r'\d+\. (.+?)(?:\n|$)',
                    r'TASK: (.+?)(?:\n|$)',
                ],
                'owner_markers': [
                    r'\(([^)]+)\)',  # (Name) after task
                    r'@(\w+)',  # @mention
                    r'Owner: (.+?)(?:\n|$)',
                ],
                'status_markers': [
                    r'\[x\]',  # Checked checkbox = done
                    r'\[ \]',  # Empty checkbox = not started
                    r'BLOCKED:',
                    r'IN PROGRESS:',
                ],
            },
            'source_type': 'drive'
        }

        return tasks

    def consolidate_tasks(self, task_list: List[Dict]) -> List[Dict]:
        """
        Consolidate tasks from multiple sources, merge duplicates, and structure data.

        Args:
            task_list: Raw list of tasks from all sources

        Returns:
            Consolidated list with merged duplicates
        """
        consolidated = {}

        for task in task_list:
            # Create a key for deduplication (based on task description similarity)
            key = self.generate_task_key(task)

            if key in consolidated:
                # Merge with existing task
                consolidated[key] = self.merge_tasks(consolidated[key], task)
            else:
                # Add new task
                consolidated[key] = task

        return list(consolidated.values())

    def generate_task_key(self, task: Dict) -> str:
        """Generate a unique key for task deduplication"""
        # Normalize task description for matching
        desc = task.get('description', '').lower().strip()
        owner = task.get('owner', '').lower().strip()

        # Simple key: first 50 chars of description + owner
        return f"{desc[:50]}_{owner}"

    def merge_tasks(self, existing: Dict, new: Dict) -> Dict:
        """
        Merge two task entries, prioritizing more recent and more complete information.
        """
        merged = existing.copy()

        # Update with non-empty values from new task
        for key, value in new.items():
            if value and (not existing.get(key) or new.get('date', '') > existing.get('date', '')):
                merged[key] = value

        # Merge source contexts
        if 'source_context' in existing and 'source_context' in new:
            merged['source_context'] = f"{existing['source_context']}; {new['source_context']}"

        return merged

    def parse_status_from_text(self, text: str) -> str:
        """
        Infer task status from text content.

        Returns: 'Not Started', 'In Progress', 'Blocked', or 'Done'
        """
        text_lower = text.lower()

        if any(word in text_lower for word in ['blocked', 'blocker', 'waiting on', 'stuck']):
            return 'Blocked'
        elif any(word in text_lower for word in ['done', 'completed', 'finished', 'shipped']):
            return 'Done'
        elif any(word in text_lower for word in ['working on', 'in progress', 'currently', 'ongoing']):
            return 'In Progress'
        else:
            return 'Not Started'

    def parse_priority_from_text(self, text: str) -> str:
        """
        Infer priority from text content.

        Returns: 'Low', 'Medium', 'High', or 'Critical'
        """
        text_lower = text.lower()

        if any(word in text_lower for word in ['critical', 'urgent', 'asap', 'emergency']):
            return 'Critical'
        elif any(word in text_lower for word in ['high priority', 'important', 'high']):
            return 'High'
        elif any(word in text_lower for word in ['low priority', 'low', 'nice to have']):
            return 'Low'
        else:
            return 'Medium'

    def extract_blockers(self, text: str) -> str:
        """Extract blocker information from text"""
        blocker_patterns = [
            r'blocked (?:by|on) (.+?)(?:\.|$)',
            r'blocker: (.+?)(?:\.|$)',
            r'waiting (?:on|for) (.+?)(?:\.|$)',
            r'dependency: (.+?)(?:\.|$)',
        ]

        for pattern in blocker_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip()

        return ''

    def format_task_for_tracker(self, raw_task: Dict) -> Dict:
        """
        Format raw task data into tracker structure.

        Returns task dictionary matching tracker columns.
        """
        return {
            'task_id': raw_task.get('id', ''),
            'owner': raw_task.get('owner', 'Unassigned'),
            'description': raw_task.get('description', ''),
            'status': raw_task.get('status', 'Not Started'),
            'priority': raw_task.get('priority', 'Medium'),
            'progress': raw_task.get('progress', 0),
            'blocker_details': raw_task.get('blocker', ''),
            'days_blocked': '',  # Will be calculated by formula
            'last_update': raw_task.get('date', datetime.now().strftime('%Y-%m-%d')),
            'source_context': raw_task.get('source', ''),
            'next_steps': raw_task.get('next_steps', ''),
            'first_detected': raw_task.get('date', datetime.now().strftime('%Y-%m-%d')),
            'last_auto_update': datetime.now().strftime('%Y-%m-%d'),
            'manual_override': 'No'
        }


class TaskExtractor:
    """Helper class for extracting structured task information from text"""

    @staticmethod
    def extract_owner(text: str, default: str = 'Unassigned') -> str:
        """Extract task owner from text"""
        patterns = [
            r'@(\w+)',
            r'owner: ([^,\n]+)',
            r'assigned to: ([^,\n]+)',
            r'\(([^)]+)\)',  # Name in parentheses
        ]

        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip()

        return default

    @staticmethod
    def extract_date(text: str) -> str:
        """Extract date mentions from text"""
        date_patterns = [
            r'(\d{4}-\d{2}-\d{2})',
            r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2})',
            r'(by [A-Z][a-z]+ \d{1,2})',
        ]

        for pattern in date_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip()

        return ''

    @staticmethod
    def clean_text(text: str) -> str:
        """Clean and normalize text"""
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        # Remove special characters but keep basics
        text = re.sub(r'[^\w\s.,!?@()-]', '', text)
        return text.strip()


def main():
    """Test the data collector structure"""
    print("Data Collector Module")
    print("=" * 50)

    # This will be initialized with actual tool instances later
    collector = DataCollector(None, None, None)

    print("\nGmail Collection Structure:")
    gmail_tasks = collector.collect_from_gmail(7)
    print(f"  • Search queries configured")
    print(f"  • Extraction patterns ready")

    print("\nCalendar Collection Structure:")
    calendar_tasks = collector.collect_from_calendar(7)
    print(f"  • Time range calculations ready")
    print(f"  • Action item patterns configured")

    print("\nDrive Collection Structure:")
    drive_tasks = collector.collect_from_drive(7)
    print(f"  • Folder search configured")
    print(f"  • Task extraction patterns ready")

    print("\n" + "=" * 50)
    print("Data collection module ready for integration")

if __name__ == "__main__":
    main()
