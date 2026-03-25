from storage import load_tasks, save_tasks
from task import Task

class TaskManager:

    def _load(self):
        data = load_tasks()

        if not isinstance(data, list):
            data = []

        return [Task(**task) for task in data]

    def _save(self, tasks):
        save_tasks([t.to_dict() for t in tasks])

    def list_tasks(self):
        tasks = self._load()

        print("\nCurrent Tasks:")

        if not tasks:
            print("No tasks available.")
            return

        for task in tasks:
            print(task)

    def add_task(self, title, priority):
        tasks = self._load()

        if tasks:
            new_id = max(task.id for task in tasks) + 1
        else:
            new_id = 1

        task = Task(new_id, title, priority)
        tasks.append(task)

        self._save(tasks)

        print("Task added successfully.")        

    def mark_complete(self, task_id):
        tasks = self._load()

        for task in tasks:
            if task.id == task_id:
                task.status = "completed"
                self._save(tasks)
                return True

        return False

    def delete_task(self, task_id):
        tasks = self._load()

        new_tasks = [task for task in tasks if task.id != task_id]

        if len(new_tasks) == len(tasks):
            return False

        self._save(new_tasks)
        return True
    
    def get_all_tasks(self):
        tasks = self._load()
        return [task.to_dict() for task in tasks]
    
    def show_report(self):
        tasks = self._load()

        if not tasks:
            print("No tasks available.")
            return

        total = len(tasks)
        completed = sum(1 for t in tasks if t.status == "completed")
        pending = total - completed

        print("\n--- Task Report ---")
        print(f"Total: {total}")
        print(f"Completed: {completed}")
        print(f"Pending: {pending}")

        priorities = {"low": 0, "medium": 0, "high": 0}

        for task in tasks:
            priorities[task.priority] += 1

        print("\nPriority Breakdown:")
        for level, count in priorities.items():
            print(f"{level.capitalize()}: {count}")