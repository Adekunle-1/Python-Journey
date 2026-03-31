from fastapi import FastAPI, HTTPException
from task_manager import TaskManager
from schemas import TaskCreate
from db import init_db

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()
    
manager = TaskManager()


@app.get("/tasks")
def get_tasks():
    return manager.get_all_tasks()

@app.post("/tasks")
def create_tasks(task: TaskCreate):
    
    if task.priority not in ["low", "medium", "high"]:
        task.priority = "low"

    manager.add_task(task.title,task.priority)
    return {"message": "Task created successfully"}

@app.patch("/tasks/{task_id}")
def complete_task(task_id:int):

    success = manager.mark_complete(task_id)

    if not success:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task updated"}


@app.delete("/tasks/{task_id}")
def delete_task(task_id:int):

    success = manager.delete_task(task_id)

    if not success:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted"}


#run with uvicorn api:app --reload