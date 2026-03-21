from datetime import datetime

class Task:

    def __init__(self, id, title, priority, status="pending", created_at=None, due_date=None):
        self.id = id
        self.title = title
        self.priority = priority
        self.status = status
        self.created_at = created_at or datetime.now().isoformat()
        self.due_date = due_date

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "priority": self.priority,
            "created_at": self.created_at,
            "due_date": self.due_date
        }
    
    def __str__(self):
        return f"[{self.id}] {self.title} - {self.status} ({self.priority})"