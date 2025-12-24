"""
Contract tests for the Todo Application CLI commands.
"""
import pytest
import sys
from io import StringIO
from src.cli.cli_interface import TodoCLI


class TestTodoContract:
    """Contract tests for the CLI commands."""
    
    def setup_method(self):
        """Set up a fresh TodoCLI instance for each test."""
        self.cli = TodoCLI()
        # Clear any existing tasks for consistent testing
        self.cli.service.tasks = []
        self.cli.service._next_id = 1
    
    def test_add_command_contract(self):
        """Contract test for add command."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            # Test with both title and description
            self.cli.run(['add', 'Test Title', 'Test Description'])
            output = captured_output.getvalue()
            
            # Verify the output contains expected elements
            assert 'Task added successfully!' in output
            assert 'Test Title' in output
            assert 'Test Description' in output
            assert 'ID:' in output
            assert 'Status:' in output
            
            # Verify the task was actually added
            tasks = self.cli.service.get_all_tasks()
            assert len(tasks) == 1
            assert tasks[0].title == 'Test Title'
            assert tasks[0].description == 'Test Description'
            assert tasks[0].status is False  # Should be incomplete by default
        finally:
            sys.stdout = sys.__stdout__
    
    def test_list_command_contract(self):
        """Contract test for list command."""
        # Add some tasks first
        self.cli.service.add_task('Task 1', 'Description 1')
        self.cli.service.add_task('Task 2', 'Description 2')
        
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            self.cli.run(['list'])
            output = captured_output.getvalue()
            
            # Verify the output contains expected elements
            assert 'ID' in output
            assert 'Status' in output
            assert 'Title' in output
            assert 'Description' in output
            assert 'Task 1' in output
            assert 'Task 2' in output
            assert 'Description 1' in output
            assert 'Description 2' in output
        finally:
            sys.stdout = sys.__stdout__
    
    def test_update_command_contract(self):
        """Contract test for update command."""
        # Add a task first
        task = self.cli.service.add_task('Original Title', 'Original Description')
        
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            self.cli.run(['update', str(task.id), 'New Title', 'New Description'])
            output = captured_output.getvalue()
            
            # Verify the output contains expected elements
            assert f'Task {task.id} updated successfully!' in output
            assert 'New Title' in output
            assert 'New Description' in output
            
            # Verify the task was actually updated
            updated_task = self.cli.service.get_task_by_id(task.id)
            assert updated_task.title == 'New Title'
            assert updated_task.description == 'New Description'
        finally:
            sys.stdout = sys.__stdout__
    
    def test_delete_command_contract(self):
        """Contract test for delete command."""
        # Add a task first
        task = self.cli.service.add_task('Task to Delete', 'Description')
        
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            self.cli.run(['delete', str(task.id)])
            output = captured_output.getvalue()
            
            # Verify the output contains expected elements
            assert f'Task {task.id} deleted successfully!' in output
            
            # Verify the task was actually deleted
            tasks = self.cli.service.get_all_tasks()
            assert len(tasks) == 0
        finally:
            sys.stdout = sys.__stdout__
    
    def test_complete_command_contract(self):
        """Contract test for complete command."""
        # Add a task first
        task = self.cli.service.add_task('Task to Complete', 'Description')
        assert task.status is False  # Should initially be incomplete
        
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            self.cli.run(['complete', str(task.id)])
            output = captured_output.getvalue()
            
            # Verify the output contains expected elements
            assert f'Task {task.id} marked as complete!' in output
            
            # Verify the task status was actually updated
            completed_task = self.cli.service.get_task_by_id(task.id)
            assert completed_task.status is True
        finally:
            sys.stdout = sys.__stdout__
    
    def test_incomplete_command_contract(self):
        """Contract test for incomplete command."""
        # Add and complete a task first
        task = self.cli.service.add_task('Task to Mark Incomplete', 'Description')
        completed_task = self.cli.service.mark_complete(task.id)
        assert completed_task.status is True  # Should be complete
        
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            self.cli.run(['incomplete', str(task.id)])
            output = captured_output.getvalue()
            
            # Verify the output contains expected elements
            assert f'Task {task.id} marked as incomplete!' in output
            
            # Verify the task status was actually updated
            incompleted_task = self.cli.service.get_task_by_id(task.id)
            assert incompleted_task.status is False
        finally:
            sys.stdout = sys.__stdout__
    
    def test_error_handling_contract(self):
        """Contract test for error handling."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            # Try to complete a non-existent task
            self.cli.run(['complete', '999'])
            output = captured_output.getvalue()
            
            # Verify an appropriate error message is provided
            assert 'Error:' in output
            assert 'not found' in output or 'does not exist' in output
        finally:
            sys.stdout = sys.__stdout__