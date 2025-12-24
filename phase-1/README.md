<<<<<<< HEAD
# TodoPhase1 - In-Memory CLI Todo Application

A Python 3.13 command-line Todo application that stores tasks in memory, built with spec-driven development using Spec-Kit Plus.

## Project Constitution

This project follows the principles outlined in our constitution:

### Core Principles

1. **Spec-Driven Development**: All features must be specified before implementation using Spec-Kit Plus; Specifications must include acceptance criteria, error paths, and constraints

2. **CLI Interface**: The application exposes functionality via command-line interface; Follows standard input/output protocols with human-readable and JSON formats

3. **Test-First (NON-NEGOTIABLE)**: TDD mandatory: Tests written before implementation; Red-Green-Refactor cycle strictly enforced; All features must have corresponding tests

4. **Clean Code & PEP8 Compliance**: All code must follow PEP8 standards and clean code principles; Proper project structure with modular design; Code reviews required before merging

5. **In-Memory Storage**: Tasks stored in memory only, no persistent storage; Simple implementation focused on core functionality; Data loss on exit is acceptable

6. **Python 3.13 Standard Library**: Use only Python 3.13 standard library modules; No external dependencies; Leverage built-in data structures and modules

## Features

- Add new todo items
- View all todo items
- Update existing todo items
- Delete todo items
- Mark todo items as complete

## Getting Started

1. Clone the repository
2. Ensure you have Python 3.13 installed
3. Run the CLI application directly from the source

```bash
python src/main.py --help
```

## Usage Examples

```bash
# Add a new task
python src/main.py add "Buy groceries" "Milk, bread, eggs"

# View all tasks
python src/main.py list

# Update a task
python src/main.py update 1 "New title" "New description"

# Mark a task as complete
python src/main.py complete 1

# Mark a task as incomplete
python src/main.py incomplete 1

# Delete a task
python src/main.py delete 1
```

## Project Structure

```
TodoPhase1/
├── src/                 # Source code
│   ├── __init__.py
│   ├── main.py          # Main CLI entry point
│   ├── models/          # Data models
│   │   └── task.py      # Task entity definition
│   ├── services/        # Business logic
│   │   └── todo_service.py # Todo operations implementation
│   ├── cli/             # Command-line interface
│   │   └── cli_interface.py # CLI command parsing and handling
│   └── lib/             # Utilities
│       └── utils.py     # Utility functions
├── tests/               # Test files
│   ├── unit/            # Unit tests
│   │   ├── test_task.py
│   │   └── test_todo_service.py
│   ├── integration/     # Integration tests
│   │   └── test_cli_integration.py
│   └── contract/        # Contract tests
│       └── test_todo_contract.py
├── specs/               # Feature specifications
└── .specify/            # Spec-Kit Plus configuration
    ├── memory/          # Project constitution
    ├── templates/       # Template files
    └── scripts/         # Utility scripts
```

## Development

This project uses a spec-driven development approach:

1. Create feature specifications in `/specs/`
2. Generate implementation plans with `/sp.plan`
3. Break features into tasks with `/sp.tasks`
4. Implement following the generated tasks

## Contributing

All contributions must comply with the project constitution and follow the established development workflow.
=======
# Hackathon-II
>>>>>>> 63d223f91774d538fd13e48e0c6446e9c2731a53
<<<<<<< HEAD
Your local changes here
=======
Remote changes here
>>>>>>> origin/main
