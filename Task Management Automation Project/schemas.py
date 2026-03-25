from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    priority: str

class TaskResponse(BaseModel):
    id: int
    title: str
    status: str
    priority: str
    created_at: str
    due_date: str | None
