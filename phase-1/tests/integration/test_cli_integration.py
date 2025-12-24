"""
Integration tests for the CLI functionality.
"""
import pytest
import sys
from io import StringIO
from unittest.mock import patch
from src.cli.cli_interface import TodoCLI


class TestCLIIntegration:
    """Integration tests for the CLI functionality."""
    
    def setup_method(self):
        """Set up a fresh TodoCLI instance for each test."""
        self.cli = TodoCLI()
        # Clear any existing tasks for consistent testing
        self.cli.service.tasks = []
        self.cli.service._next_id = 1
    
    def test_add_task_command(self):
        """Test the add command."""
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            self.cli.run(['add', 'Test Task', 'Test Description'])
            output = captured_output.getvalue()
            
            # Check that the task was added successfully
            assert 'Task added successfully!' in output
            assert 'Test Task' in output
            assert 'Test Description' in output
            
            # Verify the task exists in the service
            tasks = self.cli.service.get_all_tasks()
            assert len(tasks) == 1
            assert tasks[0].title == 'Test Task'
            assert tasks[0].description == 'Test Description'
        finally:
            # Restore stdout
            sys.stdout = sys.__stdout__
    
    def test_list_tasks_command_empty(self):
        """Test the list command when there are no tasks."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            self.cli.run(['list'])
            output = captured_output.getvalue()
            
            assert 'No tasks found.' in output
        finally:
            sys.stdout = sys.__stdout__
    
    def test_list_tasks_command_with_tasks(self):
        """Test the list command when there are tasks."""
        # Add some tasks first
        self.cli.service.add_task('Task 1', 'Description 1')
        self.cli.service.add_task('Task 2', 'Description 2')
        
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            self.cli.run(['list'])
            output = captured_output.getvalue()
            
            # Check that tasks are listed
            assert 'Task 1' in output
            assert 'Task 2' in output
            assert 'Description 1' in output
            assert 'Description 2' in output
        finally:
            sys.stdout = sys.__stdout__
    
    def test_update_task_command(self):
        """Test the update command."""
        # Add a task first
        task = self.cli.service.add_task('Original Title', 'Original Description')
        
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            self.cli.run(['update', str(task.id), 'New Title', 'New Description'])
            output = captured_output.getvalue()
            
            # Check that the task was updated successfully
            assert f'Task {task.id} updated successfully!' in output
            assert 'New Title' in output
            assert 'New Description' in output
            
            # Verify the task was updated in the service
            updated_task = self.cli.service.get_task_by_id(task.id)
            assert updated_task.title == 'New Title'
            assert updated_task.description == 'New Description'
        finally:
            sys.stdout = sys.__stdout__
    
    def test_delete_task_command(self):
        """Test the delete command."""
        # Add a task first
        task = self.cli.service.add_task('Task to Delete', 'Description')
        
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            self.cli.run(['delete', str(task.id)])
            output = captured_output.getvalue()
            
            # Check that the task was deleted successfully
            assert f'Task {task.id} deleted successfully!' in output
            
            # Verify the task no longer exists in the service
            tasks = self.cli.service.get_all_tasks()
            assert len(tasks) == 0
        finally:
            sys.stdout = sys.__stdout__
    
    def test_complete_task_command(self):
        """Test the complete command."""
        # Add a task first
        task = self.cli.service.add_task('Task to Complete', 'Description')
        assert task.status is False  # Should initially be incomplete
        
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            self.cli.run(['complete', str(task.id)])
            output = captured_output.getvalue()
            
            # Check that the task was marked as complete
            assert f'Task {task.id} marked as complete!' in output
            
            # Verify the task status was updated in the service
            completed_task = self.cli.service.get_task_by_id(task.id)
            assert completed_task.status is True
        finally:
            sys.stdout = sys.__stdout__
    
    def test_incomplete_task_command(self):
        """Test the incomplete command."""
        # Add and complete a task first
        task = self.cli.service.add_task('Task to Mark Incomplete', 'Description')
        completed_task = self.cli.service.mark_complete(task.id)
        assert completed_task.status is True  # Should be complete
        
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            self.cli.run(['incomplete', str(task.id)])
            output = captured_output.getvalue()
            
            # Check that the task was marked as incomplete
            assert f'Task {task.id} marked as incomplete!' in output
            
            # Verify the task status was updated in the service
            incompleted_task = self.cli.service.get_task_by_id(task.id)
            assert incompleted_task.status is False
        finally:
            sys.stdout = sys.__stdout__
    
    def test_error_handling_invalid_task_id(self):
        """Test error handling for invalid task IDs."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            self.cli.run(['complete', '999'])
            output = captured_output.getvalue()
            
            # Check that an appropriate error message is displayed
            assert 'Error:' in output
            assert 'not found' in output
        finally:
            sys.stdout = sys.__stdout__