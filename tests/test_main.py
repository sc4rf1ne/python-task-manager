# -*- coding: utf-8 -*-
"""Модульные тесты для консольного менеджера задач (валидация и поиск)."""
import unittest
from src.main import (
    add_task, complete_task, delete_task, get_all_tasks,
    search_tasks_by_keyword, filter_tasks_by_priority
)


class TestTaskManager(unittest.TestCase):
    def test_add_and_complete_task(self):
        tasks = []
        task = add_task(tasks, "Проверить создание ветки", "Высокий")
        self.assertEqual(len(tasks), 1)
        self.assertTrue(complete_task(tasks, task["id"]))
        self.assertTrue(tasks[0]["completed"])

    def test_search_and_filter(self):
        tasks = []
        add_task(tasks, "Настроить GitLab CI", "Высокий")
        add_task(tasks, "Изучить Git Rebase", "Средний")
        found = search_tasks_by_keyword(tasks, "rebase")
        self.assertEqual(len(found), 1)
        high_prio = filter_tasks_by_priority(tasks, "Высокий")
        self.assertEqual(len(high_prio), 1)


if __name__ == "__main__":
    unittest.main()
