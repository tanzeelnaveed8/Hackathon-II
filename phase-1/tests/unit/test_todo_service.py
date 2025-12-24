"""
Unit tests for the TodoService.
"""
import pytest
from src.services.todo_service import TodoService, TaskNotFoundError, InvalidTaskDataError
from src.models.task import Task


class TestTodoService:
    """Test cases for the TodoService."""
    
    def setup_method(self):
        """Set up a fresh TodoService instance for each test."""
        self.service = TodoService()
    
    def test_add_task_success(self):
        """Test adding a task successfully."""
        task = self.service.add_task("Test Title", "Test Description")
        
        assert task.id == 1
        assert task.title == "Test Title"
        assert task.description == "Test Description"
        assert task.status is False
        
        # Verify the task was added to the service
        tasks = self.service.get_all_tasks()
        assert len(tasks) == 1
        assert tasks[0].id == 1
    
    def test_add_task_without_description(self):
        """Test adding a task without a description."""
        task = self.service.add_task("Test Title")
        
        assert task.id == 1
        assert task.title == "Test Title"
        assert task.description == ""
        assert task.status is False
    
    def test_add_task_empty_title_error(self):
        """Test that adding a task with an empty title raises an error."""
        with pytest.raises(InvalidTaskDataError):
            self.service.add_task("")
        
        with pytest.raises(InvalidTaskDataError):
            self.service.add_task("   ")
    
    def test_get_all_tasks_empty(self):
        """Test getting all tasks when the list is empty."""
        tasks = self.service.get_all_tasks()
        
        assert len(tasks) == 0
    
    def test_get_all_tasks_with_tasks(self):
        """Test getting all tasks when there are tasks in the list."""
        self.service.add_task("Task 1", "Description 1")
        self.service.add_task("Task 2", "Description 2")
        
        tasks = self.service.get_all_tasks()
        
        assert len(tasks) == 2
        assert tasks[0].title == "Task 1"
        assert tasks[1].title == "Task 2"
    
    def test_get_task_by_id_success(self):
        """Test getting a task by its ID."""
        added_task = self.service.add_task("Test Task", "Test Description")
        
        retrieved_task = self.service.get_task_by_id(added_task.id)
        
        assert retrieved_task.id == added_task.id
        assert retrieved_task.title == added_task.title
        assert retrieved_task.description == added_task.description
        assert retrieved_task.status == added_task.status
    
    def test_get_task_by_id_not_found(self):
        """Test that getting a task by non-existent ID raises an error."""
        with pytest.raises(TaskNotFoundError):
            self.service.get_task_by_id(999)
    
    def test_update_task_success(self):
        """Test updating a task successfully."""
        task = self.service.add_task("Original Title", "Original Description")
        
        updated_task = self.service.update_task(task.id, "New Title", "New Description")
        
        assert updated_task.id == task.id
        assert updated_task.title == "New Title"
        assert updated_task.description == "New Description"
        assert updated_task.status == task.status  # Status should remain unchanged
    
    def test_update_task_partial(self):
        """Test updating only the title or description of a task."""
        task = self.service.add_task("Original Title", "Original Description")
        
        # Update only the title
        updated_task = self.service.update_task(task.id, title="New Title")
        
        assert updated_task.title == "New Title"
        assert updated_task.description == "Original Description"  # Should remain unchanged
        
        # Update only the description
        updated_task = self.service.update_task(task.id, description="New Description")
        
        assert updated_task.title == "New Title"  # Should remain unchanged
        assert updated_task.description == "New Description"
    
    def test_update_task_not_found(self):
        """Test that updating a non-existent task raises an error."""
        with pytest.raises(TaskNotFoundError):
            self.service.update_task(999, "New Title")
    
    def test_update_task_empty_title_error(self):
        """Test that updating a task with an empty title raises an error."""
        task = self.service.add_task("Original Title", "Original Description")
        
        with pytest.raises(InvalidTaskDataError):
            self.service.update_task(task.id, "")
    
    def test_delete_task_success(self):
        """Test deleting a task successfully."""
        task = self.service.add_task("Test Title", "Test Description")
        
        result = self.service.delete_task(task.id)
        
        assert result is True
        assert len(self.service.get_all_tasks()) == 0
    
    def test_delete_task_not_found(self):
        """Test that deleting a non-existent task returns False."""
        result = self.service.delete_task(999)
        
        assert result is False
    
    def test_mark_complete_success(self):
        """Test marking a task as complete."""
        task = self.service.add_task("Test Title", "Test Description")
        
        assert task.status is False  # Should initially be incomplete
        
        completed_task = self.service.mark_complete(task.id)
        
        assert completed_task.status is True
    
    def test_mark_complete_not_found(self):
        """Test that marking a non-existent task as complete raises an error."""
        with pytest.raises(TaskNotFoundError):
            self.service.mark_complete(999)
    
    def test_mark_incomplete_success(self):
        """Test marking a task as incomplete."""
        task = self.service.add_task("Test Title", "Test Description")
        completed_task = self.service.mark_complete(task.id)
        
        assert completed_task.status is True  # Should be complete
        
        incompleted_task = self.service.mark_incomplete(task.id)
        
        assert incompleted_task.status is False
    
    def test_mark_incomplete_not_found(self):
        """Test that marking a non-existent task as incomplete raises an error."""
        with pytest.raises(TaskNotFoundError):
            self.service.mark_incomplete(999)