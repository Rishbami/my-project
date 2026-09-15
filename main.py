# tiny command line app

MAX_TASKS = 10


def add_task(tasks, description):
    """
    Adds a task with a description.
    Return false if list is already full.
    """
    if len(tasks) >= MAX_TASKS:
        return False
    tasks.append({"description": description, "done": False})
    return True
