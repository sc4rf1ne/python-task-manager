# -*- coding: utf-8 -*-
"""Модульные тесты для консольного менеджера задач."""
import unittest
from src.main import add_task, complete_task, get_all_tasks


class TestTaskManager(unittest.TestCase):
    def test_add_task(self):
        tasks = []
        task = add_task(tasks, "Проверить создание ветки", "Высокий")
        self.assertEqual(len(tasks), 1)
        self.assertEqual(task["title"], "Проверить создание ветки")
        self.assertFalse(task["completed"])

    def test_complete_task(self):
        tasks = []
        add_task(tasks, "Выполнить коммит")
        res = complete_task(tasks, 1)
        self.assertTrue(res)
        self.assertTrue(tasks[0]["completed"])

    def test_get_all_tasks(self):
        tasks = []
        add_task(tasks, "Задача 1", "Низкий")
        lines = get_all_tasks(tasks)
        self.assertEqual(len(lines), 1)
        self.assertIn("Задача 1", lines[0])


if __name__ == "__main__":
    unittest.main()
