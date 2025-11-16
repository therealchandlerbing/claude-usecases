"""
XLSX to HTML Dashboard Exporter
Reads 360_project_tracker.xlsx and injects data into HTML dashboard
"""

import openpyxl
import json
import re
from datetime import datetime, date

def format_date_for_html(date_value):
    """
    Convert Excel date to YYYY-MM-DD format for HTML
    """
    if isinstance(date_value, (datetime, date)):
        return date_value.strftime('%Y-%m-%d')
    elif isinstance(date_value, str):
        return date_value
    else:
        return ''

def extract_tasks_from_xlsx(xlsx_path):
    """
    Extract all tasks from XLSX Project Status sheet
    Returns list of task dictionaries compatible with HTML dashboard
    """
    wb = openpyxl.load_workbook(xlsx_path)
    ws = wb['Project Status']

    tasks = []

    # Iterate through data rows (skip header)
    for row in ws.iter_rows(min_row=2, values_only=True):
        # Skip empty rows
        if not row[0]:  # No Task ID
            continue

        task = {
            'id': row[0] or '',
            'owner': row[1] or '',
            'description': row[2] or '',
            'status': row[3] or 'Not Started',
            'priority': row[4] or 'Medium',
            'progress': int(row[5]) if row[5] is not None else 0,
            'blocker': row[6] or '',
            'daysBlocked': int(row[7]) if row[7] else 0,
            'lastUpdate': format_date_for_html(row[8]),
            'source': row[9] or '',
            'nextSteps': row[10] or '',
            'firstDetected': format_date_for_html(row[11]),
        }

        # Add enhanced fields (columns O and P)
        if len(row) >= 15:
            task['category'] = row[14] or 'Uncategorized'
        else:
            task['category'] = 'Uncategorized'

        if len(row) >= 16:
            task['sourceDetails'] = row[15] or row[9] or ''  # Fallback to source if no details
        else:
            task['sourceDetails'] = row[9] or ''

        tasks.append(task)

    return tasks

def inject_tasks_into_html(html_path, tasks, output_path):
    """
    Replace tasks array in HTML file with data from XLSX
    """
    # Read HTML template
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Convert tasks to formatted JavaScript
    tasks_js = json.dumps(tasks, indent=12)

    # Find and replace the tasks array
    # Pattern: const tasks = [ ... ];
    pattern = r'const tasks = \[.*?\];'

    replacement = f'const tasks = {tasks_js};'

    # Replace in HTML
    new_html = re.sub(
        pattern,
        replacement,
        html_content,
        flags=re.DOTALL
    )

    # Add generation timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    new_html = new_html.replace(
        '<!-- Auto-generated timestamp -->',
        f'<!-- Auto-generated from XLSX on {timestamp} -->'
    )

    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(new_html)

    return output_path

def export_xlsx_to_html(xlsx_path, html_template_path, output_path=None):
    """
    Complete export: XLSX -> HTML Dashboard

    Args:
        xlsx_path: Path to 360_project_tracker.xlsx
        html_template_path: Path to HTML template file
        output_path: Where to save generated HTML (defaults to template path)

    Returns:
        Path to generated HTML file
    """
    if output_path is None:
        output_path = html_template_path.replace('_template', '').replace('.html', '_live.html')

    print(f"Loading tasks from: {xlsx_path}")
    tasks = extract_tasks_from_xlsx(xlsx_path)
    print(f"  ✓ Loaded {len(tasks)} tasks")

    print(f"Injecting into HTML template: {html_template_path}")
    result_path = inject_tasks_into_html(html_template_path, tasks, output_path)
    print(f"  ✓ Generated dashboard: {result_path}")

    # Print summary
    print("\nTask Summary:")
    print(f"  Total tasks: {len(tasks)}")

    statuses = {}
    for task in tasks:
        status = task['status']
        statuses[status] = statuses.get(status, 0) + 1

    for status, count in sorted(statuses.items()):
        print(f"  {status}: {count}")

    return result_path

def generate_task_summary(xlsx_path):
    """
    Generate text summary of tasks for quick review
    """
    tasks = extract_tasks_from_xlsx(xlsx_path)

    summary = []
    summary.append("=" * 80)
    summary.append("360 PROJECT TRACKER - TASK SUMMARY")
    summary.append("=" * 80)
    summary.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    summary.append(f"Total Tasks: {len(tasks)}\n")

    # Group by status
    by_status = {}
    for task in tasks:
        status = task['status']
        if status not in by_status:
            by_status[status] = []
        by_status[status].append(task)

    # Print each status group
    for status in ['Blocked', 'In Progress', 'Not Started', 'Done']:
        if status in by_status:
            summary.append(f"\n{status.upper()} ({len(by_status[status])} tasks)")
            summary.append("-" * 80)

            for task in by_status[status]:
                summary.append(f"  [{task['id']}] {task['description']}")
                summary.append(f"       Owner: {task['owner']} | Priority: {task['priority']} | Progress: {task['progress']}%")

                if task['blocker']:
                    summary.append(f"       🚫 BLOCKER: {task['blocker']}")
                    if task['daysBlocked'] > 0:
                        summary.append(f"          Blocked for {task['daysBlocked']} days")

                if task['nextSteps']:
                    summary.append(f"       → Next: {task['nextSteps']}")

                summary.append("")

    summary.append("=" * 80)

    return "\n".join(summary)

if __name__ == "__main__":
    import sys

    # Default paths
    xlsx_path = '/home/claude/360_project_tracker.xlsx'
    html_template = '/mnt/user-data/uploads/360_project_tracker_final__1_.html'
    output_path = '/mnt/user-data/outputs/360_project_tracker_dashboard.html'

    # Allow command line override
    if len(sys.argv) > 1:
        xlsx_path = sys.argv[1]
    if len(sys.argv) > 2:
        html_template = sys.argv[2]
    if len(sys.argv) > 3:
        output_path = sys.argv[3]

    # Generate summary
    print("\nGenerating task summary...")
    summary = generate_task_summary(xlsx_path)
    print(summary)

    # Export to HTML
    print("\n\nExporting to HTML dashboard...")
    try:
        result = export_xlsx_to_html(xlsx_path, html_template, output_path)
        print(f"\n✓ SUCCESS! Dashboard ready at: {result}")
    except FileNotFoundError as e:
        print(f"\n✗ ERROR: {e}")
        print("\nTo export, you need:")
        print(f"  1. XLSX file at: {xlsx_path}")
        print(f"  2. HTML template at: {html_template}")
