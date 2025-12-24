"""
Task model definition for the CLI Todo Application.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Task:
    """
    Represents a single todo task.
    
    Attributes:
        id: Unique identifier for the task
        title: Task title (required, non-empty)
        description: Task description (optional)
        status: Completion status (True for complete, False for incomplete)
        created_at: Timestamp when the task was created
    """
    id: int
    title: str
    description: Optional[str] = ""
    status: bool = False  # False = incomplete, True = complete
    created_at: datetime = None

    def __post_init__(self):
        """Initialize the created_at field if not provided."""
        if self.created_at is None:
            self.created_at = datetime.now()

    def __str__(self) -> str:
        """String representation of the task."""
        status_str = "✓" if self.status else "○"
        # Use ASCII representation to avoid encoding issues
        status_ascii = "X" if self.status else "O"
        return f"[{status_ascii}] {self.id}: {self.title} - {self.description}"

    def validate(self) -> bool:
        """
        Validate the task data.
        
        Returns:
            True if the task is valid, False otherwise
        """
        if not self.title or not self.title.strip():
            return False
        return True