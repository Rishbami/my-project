import runpy

import main


def test_add_task_adds_new_task():
    tasks = []

    assert main.add_task(tasks, "write tests") is True

    assert tasks == [{"description": "write tests", "done": False}]


def test_add_task_returns_false_when_full():
    tasks = [{"description": f"task {i}", "done": False} for i in range(main.MAX_TASKS)]

    assert main.add_task(tasks, "one too many") is False
    assert len(tasks) == main.MAX_TASKS


def test_complete_task_marks_task_done():
    tasks = [{"description": "write tests", "done": False}]

    assert main.complete_task(tasks, 0) is True

    assert tasks[0]["done"] is True


def test_complete_task_rejects_invalid_indexes():
    tasks = [{"description": "write tests", "done": False}]

    assert main.complete_task(tasks, -1) is False
    assert main.complete_task(tasks, 1) is False
    assert tasks[0]["done"] is False


def test_remove_task_removes_existing_task():
    tasks = [
        {"description": "keep", "done": False},
        {"description": "remove", "done": False},
    ]

    assert main.remove_task(tasks, 1) is True

    assert tasks == [{"description": "keep", "done": False}]


def test_remove_task_rejects_invalid_indexes():
    tasks = [{"description": "keep", "done": False}]

    assert main.remove_task(tasks, -1) is False
    assert main.remove_task(tasks, 1) is False
    assert tasks == [{"description": "keep", "done": False}]


def test_list_tasks_prints_statuses(capsys):
    tasks = [
        {"description": "unfinished", "done": False},
        {"description": "finished", "done": True},
    ]

    main.list_tasks(tasks)

    assert capsys.readouterr().out == "[✗] 1. unfinished\n[✓] 2. finished\n"


def test_command_line_happy_path(monkeypatch, capsys):
    inputs = iter(
        [
            "1",
            "learn pytest",
            "4",
            "2",
            "1",
            "3",
            "1",
            "5",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    runpy.run_module("main", run_name="__main__")

    output = capsys.readouterr().out
    assert "Task added." in output
    assert "[✗] 1. learn pytest" in output
    assert "Task completed." in output
    assert "Task removed." in output


def test_command_line_error_paths(monkeypatch, capsys):
    inputs = iter(["2", "1", "3", "1", "x", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    runpy.run_module("main", run_name="__main__")

    output = capsys.readouterr().out
    assert output.count("Invalid task number.") == 2
    assert "Invalid option. Please try again." in output


def test_command_line_reports_full_task_list(monkeypatch, capsys):
    inputs = []
    for i in range(main.MAX_TASKS + 1):
        inputs.extend(["1", f"task {i}"])
    inputs.append("5")
    input_values = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(input_values))

    runpy.run_module("main", run_name="__main__")

    assert "Task list is full." in capsys.readouterr().out
