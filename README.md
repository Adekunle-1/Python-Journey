# Python Journey

A documented progression through Python — from first scripts to real software architecture. Each project builds on the last, intentionally. This isn't a collection of tutorials; it's a working codebase that grows as my understanding does.

---

## Projects

### 1. Guessing Game
The starting point. A number guessing game covering variables, input/output, conditionals, and loops.

**Concepts:** `input()`, `if/else`, `while`, `random`

---

### 2. Hangman
A fully playable CLI hangman game. First time working with string manipulation, lists, and game state across a loop.

**Concepts:** lists, string methods, loops, game loop logic

---

### 3. Personal Workflow Automation System (PWAS) — 🚧 In Progress
A CLI task manager built to simulate real backend architecture — not just to solve a problem, but to learn the right way to structure one.

The architecture deliberately separates concerns the way a production system would: storage knows nothing about tasks, the task model knows nothing about the CLI, and the manager orchestrates between them.

```
automation_app/
├── main.py          # CLI interface and menu loop
├── task.py          # Task data model (OOP)
├── task_manager.py  # Business logic layer
├── storage.py       # JSON persistence (tasks + logs)
├── logger.py        # Action logging system
└── data/
    ├── tasks.json
    └── logs.json
```

**Features (Phase 1 — complete):**
- Add, list, complete, and delete tasks
- Priority levels (low / medium / high)
- Auto-incrementing IDs
- ISO timestamp on creation
- JSON persistence across sessions
- Action logging to `logs.json`
- Task report (totals, completion rate, priority breakdown)

**Concepts:** OOP, modular design, JSON I/O, `datetime`, separation of concerns, CLI design

**Roadmap:**

| Phase | Focus | Status |
|---|---|---|
| 1 | Procedural → OOP CLI engine | ✅ Done |
| 2 | OOP refactor | 🚧 In progress |
| 3 | FastAPI backend | ⏳ Planned |
| 4 | Database integration | ⏳ Planned |

---

## What This Repo Is

Every project here was written to understand something specific, not just to make it work. The commit history reflects that — incremental builds, rewrites when a better pattern clicked, and notes on why decisions were made.

The end goal is a FastAPI backend with a real database, built from a foundation I actually understand rather than one I copied.

---

## Stack

- **Language:** Python 3.x
- **Phase 1–2:** Standard library only (`json`, `os`, `datetime`)
- **Phase 3+:** FastAPI, Pydantic, PostgreSQL

---

## Related

This repo is part of a broader set of projects being built in parallel:

- **[mysquad-server](https://github.com/Adekunle-1/mysquad-server)** — Production FastAPI backend (where this is headed)
- **[n8n-workflows](https://github.com/Adekunle-1/n8n-workflows)** — Automation layer built on top of it