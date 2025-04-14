import json
import os

TODO_FILE = "todo.json"

def load_tasks():
    """Load tasks from the JSON file or return an empty list if the file doesn't exist."""
    return json.load(open(TODO_FILE)) if os.path.exists(TODO_FILE) else []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    """Add a new task to the to-do list."""
    task = input("Enter your task: ")
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"✅ Task added: {task}")

def list_tasks():
    """List all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    
    for index, task in enumerate(tasks, 1):
        status = "✅" if task['done'] else "❌"
        print(f"{index}. {task['task']} [{status}]")

def complete_task():
    """Mark a task as completed."""
    list_tasks()
    try:
        task_number = int(input("Enter task number to mark as completed: "))
        tasks = load_tasks()
        if 0 < task_number <= len(tasks):
            tasks[task_number - 1]["done"] = True
            save_tasks(tasks)
            print(f"✅ Task {task_number} marked as completed.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def remove_task():
    """Remove a task from the list."""
    list_tasks()
    try:
        task_number = int(input("Enter task number to remove: "))
        tasks = load_tasks()
        if 0 < task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"🗑️ Removed task: {removed_task['task']}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    """Interactive CLI Menu."""
    while True:
        print("\n📌 To-Do List Menu:")
        print("1️⃣ Add a Task")
        print("2️⃣ List Tasks")
        print("3️⃣ Complete a Task")
        print("4️⃣ Remove a Task")
        print("5️⃣ Exit")
        
        choice = input("Select an option (1-5): ")
        actions = {"1": add_task, "2": list_tasks, "3": complete_task, "4": remove_task}
        
        if choice in actions:
            actions[choice]()
        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()