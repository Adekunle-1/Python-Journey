from fastapi import FastAPI, HTTPException
from task_manager import TaskManager

app = FastAPI()

manager = TaskManager()

@app.get("/tasks")
def get_tasks():
    return [task.todict() for task in manager.tasks]

@app.post("/tasks")
def create_tasks(title:str, priority:str):

    if not title:
        raise HTTPException(status_code=400, detail="Title cannot be empty")
    
    if priority not in ["low", "medium", "high"]:
        priority = "low"

    manager.add_task(title,priority)
    return {"message": "Task created successfully"}

app.patch("/tasks/{task_id}")
def complete_task(task_id:int):

    manager.mark_complete(task_id)
    return {"message": "Task updated"}


app.delete("/tasks/{task_id}")
def delete_task(task_id:int):

    manager.delete_task(task_id)
    return {"message": "Task deleted"}
