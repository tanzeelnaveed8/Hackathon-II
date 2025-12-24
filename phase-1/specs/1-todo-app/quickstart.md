# Quickstart Guide: CLI Todo Application

## Prerequisites
- Python 3.13 installed on your system
- Basic command line familiarity

## Installation
1. Clone the repository
2. Navigate to the project directory
3. Ensure you're using Python 3.13

## Running the Application
```bash
python src/main.py --help
```

## Basic Commands

### Add a new task
```bash
python src/main.py add "Task Title" "Optional task description"
```

### View all tasks
```bash
python src/main.py list
```

### Update a task
```bash
python src/main.py update 1 "New Title" "New Description"
```

### Delete a task
```bash
python src/main.py delete 1
```

### Mark a task as complete
```bash
python src/main.py complete 1
```

### Mark a task as incomplete
```bash
python src/main.py incomplete 1
```

## Example Workflow
1. Add a task: `python src/main.py add "Buy groceries" "Milk, bread, eggs"`
2. View tasks: `python src/main.py list`
3. Mark as complete: `python src/main.py complete 1`
4. View updated list: `python src/main.py list`

## Error Handling
- Invalid task IDs will result in clear error messages
- Empty titles will be rejected with appropriate feedback
- Use `--help` flag with any command for usage information