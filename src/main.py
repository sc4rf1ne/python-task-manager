# -*- coding: utf-8 -*-
"""Консольный менеджер задач (Python Task Manager) — базовая версия."""


def add_task(tasks: list, title: str, priority: str = "Средний") -> dict:
    """Добавляет новую задачу в список задач."""
    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "completed": False
    }
    tasks.append(new_task)
    return new_task


def complete_task(tasks: list, task_id: int) -> bool:
    """Отмечает задачу с указанным ID как выполненную."""
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return True
    return False


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

    print("=== Список задач ===")
    for line in get_all_tasks(tasks):
        print(line)


if __name__ == "__main__":
    main()
