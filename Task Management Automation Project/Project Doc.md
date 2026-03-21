# Personal Workflow Automation System (PWAS)

## 1. Project Overview

The Personal Workflow Automation System (PWAS) is a CLI-based automation engine that allows users to:

- Create and manage tasks
- Track task status
- Log system actions
- Generate productivity reports
- Persist data using JSON storage
- Later evolve into a FastAPI backend

This project is designed to simulate real-world backend architecture principles using core Python.

---

## 2. Objectives

By completing this project, you will:

- Understand modular project structure
- Separate business logic from storage logic
- Design your own data models
- Implement JSON persistence
- Implement logging systems
- Practice refactoring into OOP
- Prepare codebase for FastAPI integration
- Improve ability to read structured/LLM-generated code

---

## 3. Technology Stack (Phase 1)

- **Language:** Python 3.x
- **Built-in modules:** `json`, `os`, `datetime`
- **Optional (Phase 5):** `pandas`
- **Future Phase:** FastAPI

---

## 4. Project Architecture

### Folder Structure

```
automation_app/
│
├── main.py
├── storage.py
├── logger.py        (Day 4)
├── report.py        (Day 5)
│
└── data/
    ├── tasks.json
    └── logs.json
```

> Phase 1 starts minimal. Files are added progressively.

---

## 5. Data Models

### Task Model

```json
{
  "id": "int",
  "title": "str",
  "status": "pending | completed",
  "priority": "low | medium | high",
  "created_at": "str (ISO format)",
  "due_date": "str or None"
}
```

### Log Model

```json
{
  "timestamp": "str (ISO format)",
  "action": "str",
  "metadata": "dict"
}
```

---

## 6. Functional Requirements

### Task Management
- Add task
- List tasks
- Mark complete
- Delete task

### Logging System
- Log all actions automatically
- Store logs in `logs.json`
- Include timestamp + metadata

### Reporting System
- Completion rate
- Tasks by priority
- Tasks per day
- Most productive day

---

## 7. Constraints

- No global state
- No file writes outside storage module
- `tasks.json` must always contain a list
- `logs.json` must always contain a list
- IDs must auto-increment
- `created_at` must be ISO format

---

## 8. Non-Functional Goals

- Code readability
- Clean separation of concerns
- Refactor-ready for OOP
- API-ready structure

---

## 9. Phase Roadmap

| Phase   | Focus                        |
|---------|------------------------------|
| Phase 1 | Procedural CLI engine        |
| Phase 2 | OOP refactor                 |
| Phase 3 | FastAPI backend              |
| Phase 4 | Possible database integration |