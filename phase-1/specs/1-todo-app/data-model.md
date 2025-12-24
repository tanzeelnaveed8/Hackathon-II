# Data Model: CLI Todo Application

## Task Entity

### Attributes
- **id**: integer, unique identifier, automatically assigned, required
- **title**: string, task title, required, must not be empty
- **description**: string, task description, optional, can be empty
- **status**: boolean, completion status, required, default: false (incomplete)
- **created_at**: datetime, timestamp of creation, required, automatically set

### Validation Rules
- title must be a non-empty string
- id must be unique within the application
- status must be a boolean value (True for complete, False for incomplete)

### State Transitions
- Initial state: status = False (incomplete)
- Transition 1: status = False → status = True (marked complete)
- Transition 2: status = True → status = False (marked incomplete)

## In-Memory Storage Structure
- **tasks**: List<Task>, stores all Task objects in order of creation
- Operations: Add, retrieve by ID, update, delete by ID