# -*- coding: utf-8 -*-
"""Консольный менеджер задач (Python Task Manager) — с валидацией ввода."""

APP_VERSION = "1.2.0"
ALLOWED_PRIORITIES = ("Низкий", "Средний", "Высокий")


def validate_task_input(title: str, priority: str) -> None:
    """Проверяет корректность названия и приоритета задачи."""
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Название задачи не может быть пустым.")
    if priority not in ALLOWED_PRIORITIES:
        raise ValueError(f"Недопустимый приоритет '{priority}'.")


def add_task(tasks: list, title: str, priority: str = "Средний") -> dict:
    """Добавляет новую задачу в список задач после валидации."""
    validate_task_input(title, priority)
    new_task = {
        "id": len(tasks) + 1,
        "title": title.strip(),
        "priority": priority,
        "completed": False
    }
    tasks.append(new_task)
    return new_task


def complete_task(tasks: list, task_id: int) -> bool:
    """Отмечает задачу с указанным ID как выполненную."""
    if not isinstance(task_id, int) or task_id <= 0:
        raise ValueError("ID задачи должен быть положительным числом.")
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return True
    return False


def delete_task(tasks: list, task_id: int) -> bool:
    """Удаляет задачу по её идентификатору ID."""
    for idx, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(idx)
            return True
    return False


def get_task_statistics(tasks: list) -> dict:
    """Подсчитывает статистику: всего, выполнено и осталось задач."""
    total = len(tasks)
    completed = sum(1 for t in tasks if t["completed"])
    return {"total": total, "completed": completed, "pending": total - completed}


def get_all_tasks(tasks: list) -> list:
    """Возвращает форматированный список всех задач."""
    result = []
    for task in tasks:
        status = "[x]" if task["completed"] else "[ ]"
        result.append(f"{task['id']}. {status} {task['title']} (Приоритет: {task['priority']})")
    return result


def main():
    tasks = []
    add_task(tasks, "Настроить Git-репозиторий проекта", "Высокий")
    add_task(tasks, "Реализовать базовые функции менеджера задач", "Высокий")
    add_task(tasks, "Написать модульные тесты в каталоге tests", "Средний")
    complete_task(tasks, 1)

    print("=== МОЙ СПИСОК ЗАДАЧ (ВЕРСИЯ 2.0) ===")
    for line in get_all_tasks(tasks):
        print(line)
    stats = get_task_statistics(tasks)
    print(f"Статистика: всего={stats['total']}, выполнено={stats['completed']}, в работе={stats['pending']}")


if __name__ == "__main__":
    main()
