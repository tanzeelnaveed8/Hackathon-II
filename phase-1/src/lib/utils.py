"""
Utility functions for the CLI Todo Application.
"""
import logging
from datetime import datetime


def setup_logging():
    """
    Set up logging configuration for the application.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )


def format_task_output(task, output_format='table'):
    """
    Format a task for output based on the specified format.
    
    Args:
        task: The task object to format
        output_format: The format to use ('table' or 'json')
        
    Returns:
        Formatted string representation of the task
    """
    if output_format == 'json':
        import json
        task_data = {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'status': 'complete' if task.status else 'incomplete',
            'created_at': task.created_at.isoformat()
        }
        return json.dumps(task_data, indent=2)
    else:  # table format
        status = "✓" if task.status else "○"
        title = task.title[:17] + "..." if len(task.title) > 17 else task.title
        description = task.description[:27] + "..." if len(task.description) > 27 else task.description
        return f"{task.id:<4} {status:<8} {title:<20} {description:<30}"


def validate_task_id(task_id):
    """
    Validate that the task ID is a positive integer.
    
    Args:
        task_id: The task ID to validate
        
    Returns:
        True if valid, False otherwise
    """
    return isinstance(task_id, int) and task_id > 0