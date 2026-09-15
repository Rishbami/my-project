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
    # Check if index is valid
    # if valid, remove
    if index < 0 or index >= len(tasks):
        return False
    tasks.pop(index)
    return True
