"""
CLI interface for the Todo Application.
Handles command-line argument parsing and command routing.
"""
import argparse
import os
import sys
from typing import List, Optional

# Add the src directory to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from services.todo_service import TodoService, TaskNotFoundError, InvalidTaskDataError


class TodoCLI:
    """
    Command-line interface for the Todo Application.
    """
    
    def __init__(self):
        """Initialize the CLI with a TodoService instance."""
        self.service = TodoService()
    
    def run(self, args: Optional[List[str]] = None):
        """
        Run the CLI application.
        
        Args:
            args: Command-line arguments (for testing purposes)
        """
        parser = argparse.ArgumentParser(
            description="CLI Todo Application",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  %(prog)s add "Buy groceries" "Milk, bread, eggs"
  %(prog)s list
  %(prog)s update 1 "New title" "New description"
  %(prog)s complete 1
  %(prog)s delete 1
            """.rstrip()
        )
        
        # Create subparsers for different commands
        subparsers = parser.add_subparsers(dest='command', help='Available commands')
        
        # Add command
        add_parser = subparsers.add_parser('add', help='Add a new task')
        add_parser.add_argument('title', help='Task title')
        add_parser.add_argument('description', nargs='?', default='', help='Task description')
        
        # List command
        list_parser = subparsers.add_parser('list', help='List all tasks')
        list_parser.add_argument('--format', choices=['table', 'json'], default='table', 
                                help='Output format (default: table)')
        
        # Update command
        update_parser = subparsers.add_parser('update', help='Update a task')
        update_parser.add_argument('id', type=int, help='Task ID')
        update_parser.add_argument('title', nargs='?', help='New task title')
        update_parser.add_argument('description', nargs='?', help='New task description')
        
        # Delete command
        delete_parser = subparsers.add_parser('delete', help='Delete a task')
        delete_parser.add_argument('id', type=int, help='Task ID')
        
        # Complete command
        complete_parser = subparsers.add_parser('complete', help='Mark a task as complete')
        complete_parser.add_argument('id', type=int, help='Task ID')
        
        # Incomplete command
        incomplete_parser = subparsers.add_parser('incomplete', help='Mark a task as incomplete')
        incomplete_parser.add_argument('id', type=int, help='Task ID')
        
        # Parse arguments
        parsed_args = parser.parse_args(args)
        
        # Route to appropriate command handler
        if parsed_args.command == 'add':
            self._handle_add(parsed_args.title, parsed_args.description)
        elif parsed_args.command == 'list':
            self._handle_list(parsed_args.format)
        elif parsed_args.command == 'update':
            self._handle_update(parsed_args.id, parsed_args.title, parsed_args.description)
        elif parsed_args.command == 'delete':
            self._handle_delete(parsed_args.id)
        elif parsed_args.command == 'complete':
            self._handle_complete(parsed_args.id)
        elif parsed_args.command == 'incomplete':
            self._handle_incomplete(parsed_args.id)
        elif parsed_args.command is None:
            parser.print_help()
        else:
            parser.print_help()
    
    def _handle_add(self, title: str, description: str):
        """Handle the 'add' command."""
        try:
            task = self.service.add_task(title, description)
            print(f"Task added successfully!")
            print(f"ID: {task.id}")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Status: {'Complete' if task.status else 'Incomplete'}")
        except InvalidTaskDataError as e:
            print(f"Error: {e}")
    
    def _handle_list(self, output_format: str):
        """Handle the 'list' command."""
        tasks = self.service.get_all_tasks()
        
        if not tasks:
            print("No tasks found.")
            return
        
        if output_format == 'json':
            import json
            tasks_data = [
                {
                    'id': task.id,
                    'title': task.title,
                    'description': task.description,
                    'status': 'complete' if task.status else 'incomplete',
                    'created_at': task.created_at.isoformat()
                }
                for task in tasks
            ]
            print(json.dumps(tasks_data, indent=2))
        else:  # table format
            print(f"{'ID':<4} {'Status':<8} {'Title':<20} {'Description':<30}")
            print("-" * 70)
            for task in tasks:
                status = "Done" if task.status else "Todo"
                title = task.title[:17] + "..." if len(task.title) > 17 else task.title
                description = task.description[:27] + "..." if len(task.description) > 27 else task.description
                print(f"{task.id:<4} {status:<8} {title:<20} {description:<30}")
    
    def _handle_update(self, task_id: int, title: Optional[str], description: Optional[str]):
        """Handle the 'update' command."""
        try:
            task = self.service.update_task(task_id, title, description)
            print(f"Task {task_id} updated successfully!")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
        except TaskNotFoundError as e:
            print(f"Error: {e}")
        except InvalidTaskDataError as e:
            print(f"Error: {e}")
    
    def _handle_delete(self, task_id: int):
        """Handle the 'delete' command."""
        deleted = self.service.delete_task(task_id)
        if deleted:
            print(f"Task {task_id} deleted successfully!")
        else:
            print(f"Error: Task with ID {task_id} not found")
    
    def _handle_complete(self, task_id: int):
        """Handle the 'complete' command."""
        try:
            task = self.service.mark_complete(task_id)
            print(f"Task {task_id} marked as complete!")
        except TaskNotFoundError as e:
            print(f"Error: {e}")
    
    def _handle_incomplete(self, task_id: int):
        """Handle the 'incomplete' command."""
        try:
            task = self.service.mark_incomplete(task_id)
            print(f"Task {task_id} marked as incomplete!")
        except TaskNotFoundError as e:
            print(f"Error: {e}")