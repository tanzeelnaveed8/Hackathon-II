---

description: "Task list template for feature implementation"
---

# Tasks: CLI Todo Application

**Input**: Design documents from `/specs/1-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **CLI App**: `src/`, `tests/` at repository root with `src/cli/` for command-line interface
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

<!--
  ============================================================================
  IMPORTANT: The tasks below are SAMPLE TASKS for illustration purposes only.

  The /sp.tasks command MUST replace these with actual tasks based on:
  - User stories from spec.md (with their priorities P1, P2, P3...)
  - Feature requirements from plan.md
  - Entities from data-model.md
  - Endpoints from contracts/

  Tasks MUST be organized by user story so each story can be:
  - Implemented independently
  - Tested independently
  - Delivered as an MVP increment

  DO NOT keep these sample tasks in the generated tasks.md file.
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan
- [x] T002 Initialize Python 3.13 project with basic directory structure
- [x] T003 [P] Configure linting and formatting tools (flake8, black)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [x] T004 Setup in-memory data structures and storage framework in src/services/todo_service.py
- [x] T005 [P] Implement CLI argument parsing and command routing in src/cli/cli_interface.py
- [x] T006 [P] Setup application configuration and settings
- [x] T007 Create base models/entities that all stories depend on in src/models/task.py
- [x] T008 Configure error handling and logging infrastructure with custom exceptions
- [x] T009 Setup testing framework and initial test structure

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Task (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks to their todo list with a title and description

**Independent Test**: Can be fully tested by adding a task with a title and description and verifying it appears in the task list with a unique ID and "incomplete" status

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T010 [P] [US1] Contract test for add command in tests/contract/test_todo_contract.py
- [x] T011 [P] [US1] Integration test for add task user journey in tests/integration/test_cli_integration.py

### Implementation for User Story 1

- [x] T012 [P] [US1] Create Task model in src/models/task.py
- [x] T013 [P] [US1] Create TodoService with add_task functionality in src/services/todo_service.py
- [x] T014 [US1] Implement add command in src/cli/cli_interface.py (depends on T012, T013)
- [x] T015 [US1] Implement main CLI entry point for add command in src/main.py
- [x] T016 [US1] Add validation and error handling for empty titles
- [x] T017 [US1] Add logging for add task operations

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P2)

**Goal**: Enable users to view all tasks in their todo list

**Independent Test**: Can be fully tested by adding several tasks and then viewing the complete list to verify all tasks are displayed with their ID, title, description, and status in order of creation

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [x] T018 [P] [US2] Contract test for list command in tests/contract/test_todo_contract.py
- [x] T019 [P] [US2] Integration test for view tasks user journey in tests/integration/test_cli_integration.py

### Implementation for User Story 2

- [x] T020 [P] [US2] Enhance TodoService with get_all_tasks functionality in src/services/todo_service.py
- [x] T021 [US2] Implement list command in src/cli/cli_interface.py
- [x] T022 [US2] Implement main CLI entry point for list command in src/main.py
- [x] T023 [US2] Format output to display ID, title, description, and status
- [x] T024 [US2] Ensure tasks are displayed in order of creation

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Task Complete/Incomplete (Priority: P3)

**Goal**: Enable users to mark tasks as complete or incomplete to track progress

**Independent Test**: Can be fully tested by adding a task, marking it as complete, then viewing it to verify the status has changed

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [x] T025 [P] [US3] Contract test for complete/incomplete commands in tests/contract/test_todo_contract.py
- [x] T026 [P] [US3] Integration test for mark task user journey in tests/integration/test_cli_integration.py

### Implementation for User Story 3

- [x] T027 [P] [US3] Enhance TodoService with mark_complete and mark_incomplete functionality in src/services/todo_service.py
- [x] T028 [US3] Implement complete command in src/cli/cli_interface.py
- [x] T029 [US3] Implement incomplete command in src/cli/cli_interface.py
- [x] T030 [US3] Implement main CLI entry points for complete/incomplete commands in src/main.py
- [x] T031 [US3] Add validation for valid task IDs

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Task Details (Priority: P4)

**Goal**: Enable users to update the title and description of existing tasks

**Independent Test**: Can be fully tested by adding a task, updating its details, then viewing it to verify the changes were applied

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [x] T032 [P] [US4] Contract test for update command in tests/contract/test_todo_contract.py
- [x] T033 [P] [US4] Integration test for update task user journey in tests/integration/test_cli_integration.py

### Implementation for User Story 4

- [x] T034 [P] [US4] Enhance TodoService with update_task functionality in src/services/todo_service.py
- [x] T035 [US4] Implement update command in src/cli/cli_interface.py
- [x] T036 [US4] Implement main CLI entry point for update command in src/main.py
- [x] T037 [US4] Add validation for valid task IDs and non-empty updates
- [x] T038 [US4] Add logging for update operations

**Checkpoint**: At this point, User Stories 1, 2, 3, AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Task (Priority: P5)

**Goal**: Enable users to delete tasks from their todo list

**Independent Test**: Can be fully tested by adding a task, deleting it, then viewing the task list to verify it's no longer present

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [x] T039 [P] [US5] Contract test for delete command in tests/contract/test_todo_contract.py
- [x] T040 [P] [US5] Integration test for delete task user journey in tests/integration/test_cli_integration.py

### Implementation for User Story 5

- [x] T041 [P] [US5] Enhance TodoService with delete_task functionality in src/services/todo_service.py
- [x] T042 [US5] Implement delete command in src/cli/cli_interface.py
- [x] T043 [US5] Implement main CLI entry point for delete command in src/main.py
- [x] T044 [US5] Add validation for valid task IDs
- [x] T045 [US5] Add confirmation or success message for deletion

**Checkpoint**: All user stories should now be independently functional

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T046 [P] Documentation updates in docs/
- [x] T047 Code cleanup and refactoring
- [x] T048 Performance optimization across all stories
- [x] T049 [P] Additional unit tests (if requested) in tests/unit/
- [x] T050 Security hardening
- [x] T051 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for add command in tests/contract/test_todo_contract.py"
Task: "Integration test for add task user journey in tests/integration/test_cli_integration.py"

# Launch all models for User Story 1 together:
Task: "Create Task model in src/models/task.py"
Task: "Create TodoService with add_task functionality in src/services/todo_service.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Add User Story 1 → Test independently → Deploy/Demo (MVP!)
   - Add User Story 2 → Test independently → Deploy/Demo
   - Add User Story 3 → Test independently → Deploy/Demo
   - Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence