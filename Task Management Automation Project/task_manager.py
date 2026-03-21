from storage import load_tasks, save_tasks
from task import Task

class TaskManager:

    def __init__(self):
        data = load_tasks()

        if not isinstance(data,list):
            data = []
        
        self.tasks = [Task(**task) for task in data]

    def list_tasks(self):
        print("\nCurrent Tasks:")

        if not self.tasks:
            print("No tasks available")

        for task in self.tasks:
            print(task)

    def add_task(self, title, priority):

        if self.tasks:
            new_id = max(task.id for task in self.tasks) + 1
        else:
            new_id = 1

        task = Task (new_id,title,priority)

        self.tasks.append(task)

        save_tasks([t.to_dict() for t in self.tasks])

        print("Task added successfully.")

    def mark_complete(self, task_id):

        for task in self.tasks:
            if task.id == task_id:
                task.status = "completed"
                save_tasks([t.to_dict() for t in self.tasks])
                print(f"Task {task_id} marked as completed.")
                return
        
        print('Task not found.')

    def delete_task(self, task_id):
        
        new_task = [task for task in self.tasks if task.id != task_id]

        if len(new_task) == len(self.tasks):
            print("Task not found.")
            return
        
        self.tasks = new_task
        save_tasks([t.to_dict() for t in self.tasks])

        print("Task deleted successfully.")

    def show_report(self):
        
        if not self.tasks:
            print("No tasks available.")
            return

        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task.status == "completed")
        pending = total - completed

        print("\n--- Task Report ---")
        print(f"Total tasks: {total}")
        print(f"Completed: {completed}")
        print(f"Pending: {pending}")

        priorities = {"low": 0, "medium": 0, "high": 0}

        for task in self.tasks:
            priorities[task.priority] += 1

        print("\nPriority Breakdown:")
        for level, count in priorities.items():
            print(f"{level.capitalize()}: {count}")