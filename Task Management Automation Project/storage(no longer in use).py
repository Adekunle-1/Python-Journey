import json
import os

BASE_DIR = os.path.dirname(__file__)
TASKS_FILE = os.path.join(BASE_DIR, "data", "tasks.json")
LOGS_FILE = os.path.join(BASE_DIR, "data", "logs.json" )

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w") as f:
            json.dump([], f)
        return []
    try:
        with open (TASKS_FILE, "r") as f:
            data = json.load(f)
            if isinstance(data,list):
                return data
            else:
                return []
    except json.JSONDecodeError:
        return[]
    
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def load_logs():
    if not os.path.exists(LOGS_FILE):
        with open(LOGS_FILE, "w") as f:
            json.dump([], f)
            return []
    try:
        with open (LOGS_FILE, "r") as f:
            data =json.load(f)
            if isinstance(data,list):
                return data
            else:
                return []
    except json.JSONDecodeError:
        return []
    
def save_logs(logs):
    with open(LOGS_FILE, "w") as f:
        json.dump(logs, f, indent=4)
