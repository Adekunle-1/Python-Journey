from task_manager import TaskManager
from db import init_db

def id_input():
    while True:
        user_input = input('Enter task ID or press q to cancel: ')

        if user_input.lower() == 'q':
            return None

        try:
            return int(user_input)
        except ValueError:
            print ('Invalid ID. Please enter a number or q to cancel.')

def main():
    init_db()
    manager = TaskManager() 
    

    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":         
            title = input('Enter task title: ').strip() #set title
            if not title:
                print ('Title cannot be empty.')
                continue
            
            priority = input("Enter priority (low, medium, high): ").lower() #set priority
            if priority not in ['low','medium','high']:
                print ('invalid priority. Defaulting to Low')
                priority = 'low'
            manager.add_task(title, priority)
        
        elif choice == "2":
            manager.list_tasks()
        
        elif choice == "3":
            task_id = id_input()
            if task_id is None:
                continue

            success = manager.mark_complete(task_id)
            print("Done" if success else "Task not found")
        
        elif choice == "4":
            task_id = id_input()
            if task_id is None:
                continue
            
            success = manager.delete_task(task_id)
            print("Deleted" if success else "Task not found")

        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()