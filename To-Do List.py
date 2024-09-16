import os
import json

TASKS_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from the file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, task_description):
    """Add a new task to the list."""
    tasks.append({"description": task_description, "completed": False})
    save_tasks(tasks)

def list_tasks(tasks):
    """List all tasks."""
    for i, task in enumerate(tasks):
        status = "✓" if task["completed"] else "✗"
        print(f"{i + 1}. {task['description']} [{status}]")

def complete_task(tasks, task_index):
    """Mark a task as completed."""
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        save_tasks(tasks)
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            description = input("Enter the task description: ")
            add_task(tasks, description)
            print("Task added.")
        
        elif choice == '2':
            list_tasks(tasks)
        
        elif choice == '3':
            list_tasks(tasks)
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            complete_task(tasks, task_index)
            print("Task marked as completed.")
        
        elif choice == '4':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
