# CLI Command Contracts: Todo Application

## Command Structure
```
python todo_app.py <command> [arguments] [options]
```

## Commands

### Add Task
- **Command**: `add`
- **Arguments**: 
  - title (required): string, task title
  - description (optional): string, task description
- **Options**: None
- **Example**: `python todo_app.py add "Buy groceries" "Milk, bread, eggs"`
- **Output**: Task object with ID, title, description, status
- **Errors**: 
  - Empty title: "Error: Task title cannot be empty"

### List Tasks
- **Command**: `list`
- **Arguments**: None
- **Options**: 
  - `--format`: Output format (table, json)
- **Example**: `python todo_app.py list`
- **Output**: List of all tasks with ID, title, description, status
- **Errors**: None

### Update Task
- **Command**: `update`
- **Arguments**: 
  - id (required): integer, task ID
  - title (optional): string, new title
  - description (optional): string, new description
- **Options**: None
- **Example**: `python todo_app.py update 1 "New title" "New description"`
- **Output**: Updated task object
- **Errors**: 
  - Invalid ID: "Error: Task with ID X not found"

### Delete Task
- **Command**: `delete`
- **Arguments**: 
  - id (required): integer, task ID
- **Options**: None
- **Example**: `python todo_app.py delete 1`
- **Output**: Confirmation message
- **Errors**: 
  - Invalid ID: "Error: Task with ID X not found"

### Complete Task
- **Command**: `complete`
- **Arguments**: 
  - id (required): integer, task ID
- **Options**: None
- **Example**: `python todo_app.py complete 1`
- **Output**: Updated task object with status=True
- **Errors**: 
  - Invalid ID: "Error: Task with ID X not found"

### Incomplete Task
- **Command**: `incomplete`
- **Arguments**: 
  - id (required): integer, task ID
- **Options**: None
- **Example**: `python todo_app.py incomplete 1`
- **Output**: Updated task object with status=False
- **Errors**: 
  - Invalid ID: "Error: Task with ID X not found"