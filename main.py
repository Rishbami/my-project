# tiny command line app

MAX_TASKS = 10


# Adding a task
def add_task(tasks, description):
    """
    Adds a task with a description.
    Return false if list is already full.
    """
    if len(tasks) >= MAX_TASKS:
        return False
    tasks.append({"description": description, "done": False})
    return True


# Completing a task
def complete_task(tasks, index):
    """Mark a task as done."""
    if index < 0 or index >= len(tasks):
        return False
    tasks[index]["done"] = True
    return True


# Remove a task
def remove_task(tasks, index):
    """Remove a task."""
    if index < 0 or index >= len(tasks):
        return False
    tasks.pop(index)
    return True


# List all tasks:
def list_tasks(tasks):
    """List all tasks."""
    for i, task in enumerate(tasks):
        status = "✓" if task["done"] else "✗"
        print(f"[{status}] {i + 1}. {task['description']}")


def main():
    tasks: list[dict[str, bool]] = []
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Remove Task")
        print("4. List Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter task description: ")
            if add_task(tasks, description):
                print("Task added.")
            else:
                print("Task list is full.")
        elif choice == "2":
            index = int(input("Enter task number to complete: ")) - 1
            if complete_task(tasks, index):
                print("Task completed.")
            else:
                print("Invalid task number.")
        elif choice == "3":
            index = int(input("Enter task number to remove: ")) - 1
            if remove_task(tasks, index):
                print("Task removed.")
            else:
                print("Invalid task number.")
        elif choice == "4":
            list_tasks(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
