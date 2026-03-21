from storage import load_logs,save_logs
from datetime import datetime

def log_action (action, metadata=None):
    logs = load_logs()

    entry = {
        "timestamp":datetime.now().isoformat(),
        "action": action,
        "metadata": metadata or {}
    }

    logs.append(entry)
    save_logs(logs)

