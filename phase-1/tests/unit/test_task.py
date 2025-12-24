"""
Unit tests for the Task model.
"""
import pytest
from datetime import datetime
from src.models.task import Task


class TestTask:
    """Test cases for the Task model."""
    
    def test_task_creation(self):
        """Test creating a task with valid data."""
        task = Task(id=1, title="Test Task", description="Test Description", status=False)
        
        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.status is False
        assert isinstance(task.created_at, datetime)
    
    def test_task_creation_defaults(self):
        """Test creating a task with default values."""
        task = Task(id=1, title="Test Task")
        
        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == ""
        assert task.status is False
        assert isinstance(task.created_at, datetime)
    
    def test_task_validation_valid(self):
        """Test that a valid task passes validation."""
        task = Task(id=1, title="Valid Task")
        assert task.validate() is True
    
    def test_task_validation_invalid_empty_title(self):
        """Test that a task with empty title fails validation."""
        task = Task(id=1, title="", description="Test Description")
        assert task.validate() is False
        
        task = Task(id=1, title="   ", description="Test Description")
        assert task.validate() is False
    
    def test_task_string_representation(self):
        """Test the string representation of a task."""
        task = Task(id=1, title="Test Task", description="Test Description", status=False)
        expected = "[○] 1: Test Task - Test Description"
        assert str(task) == expected
        
        task.status = True
        expected = "[✓] 1: Test Task - Test Description"
        assert str(task) == expected