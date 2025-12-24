"""
TodoService implementation for the CLI Todo Application.
Handles all business logic for todo operations.
"""
import os
import sys
from typing import List, Optional

# Add the src directory to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from models.task import Task


class TaskNotFoundError(Exception):
    """Exception raised when a task with a specified ID is not found."""
    pass


class InvalidTaskDataError(Exception):
    """Exception raised when task data is invalid."""
    pass


class TodoService:
    """
    Service class that handles all todo operations.
    Uses in-memory storage to store tasks.
    """
    
    def __init__(self):
        """Initialize the TodoService with an empty task list."""
        self.tasks: List[Task] = []
        self._next_id = 1
    
    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task to the list.
        
        Args:
            title: The task title (required)
            description: The task description (optional)
            
        Returns:
            The newly created Task object
            
        Raises:
            InvalidTaskDataError: If the title is empty
        """
        if not title or not title.strip():
            raise InvalidTaskDataError("Task title cannot be empty")
        
        task = Task(
            id=self._next_id,
            title=title.strip(),
            description=description.strip() if description else "",
            status=False  # New tasks are incomplete by default
        )
        
        if not task.validate():
            raise InvalidTaskDataError("Invalid task data")
        
        self.tasks.append(task)
        self._next_id += 1
        
        return task
    
    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the order they were created.
        
        Returns:
            A list of all Task objects
        """
        return self.tasks.copy()  # Return a copy to prevent external modification
    
    def get_task_by_id(self, task_id: int) -> Task:
        """
        Get a specific task by its ID.
        
        Args:
            task_id: The ID of the task to retrieve
            
        Returns:
            The Task object with the specified ID
            
        Raises:
            TaskNotFoundError: If no task with the given ID exists
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        
        raise TaskNotFoundError(f"Task with ID {task_id} not found")
    
    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Task:
        """
        Update an existing task.
        
        Args:
            task_id: The ID of the task to update
            title: New title (optional)
            description: New description (optional)
            
        Returns:
            The updated Task object
            
        Raises:
            TaskNotFoundError: If no task with the given ID exists
            InvalidTaskDataError: If the new title is empty
        """
        task = self.get_task_by_id(task_id)
        
        # Update title if provided
        if title is not None:
            title = title.strip()
            if not title:
                raise InvalidTaskDataError("Task title cannot be empty")
            task.title = title
        
        # Update description if provided
        if description is not None:
            task.description = description.strip() if description else ""
        
        # Validate the updated task
        if not task.validate():
            raise InvalidTaskDataError("Invalid task data after update")
        
        return task
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.
        
        Args:
            task_id: The ID of the task to delete
            
        Returns:
            True if the task was deleted, False if it didn't exist
        """
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                return True
        return False
    
    def mark_complete(self, task_id: int) -> Task:
        """
        Mark a task as complete.
        
        Args:
            task_id: The ID of the task to mark as complete
            
        Returns:
            The updated Task object
            
        Raises:
            TaskNotFoundError: If no task with the given ID exists
        """
        task = self.get_task_by_id(task_id)
        task.status = True
        return task
    
    def mark_incomplete(self, task_id: int) -> Task:
        """
        Mark a task as incomplete.
        
        Args:
            task_id: The ID of the task to mark as incomplete
            
        Returns:
            The updated Task object
            
        Raises:
            TaskNotFoundError: If no task with the given ID exists
        """
        task = self.get_task_by_id(task_id)
        task.status = False
        return task