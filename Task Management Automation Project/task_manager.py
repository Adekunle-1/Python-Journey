from db import get_connection
from datetime import datetime

class TaskManager:

    def get_all_tasks(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()

        conn.close()

        return [dict(row) for row in rows]
    
    def list_tasks(self):
        tasks = self.get_all_tasks()

        print("\nCurrent Tasks:")
        if not tasks:
            print("No tasks available.")
            return

        for task in tasks:
            print(task)

    def add_task(self, title, priority):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(""" 
                       INSERT INTO tasks (title, priority, created_at) 
                       VALUES (?,?,?)
                       """, (title, priority, datetime.now().isoformat()))
        
        conn.commit()
        conn.close()  
        print ("Task Successfully Added)")   

    def mark_complete(self, task_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("UPDATE tasks SET status = 'completed' WHERE id = ?", (task_id,))

        conn.commit()
        updated = cursor.rowcount
        conn.close()

        return updated > 0

    def delete_task(self, task_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

        conn.commit()
        deleted = cursor.rowcount
        conn.close()

        return deleted > 0
    
    """def show_report(self):
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
            print(f"{level.capitalize()}: {count}")"""