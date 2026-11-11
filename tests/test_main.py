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



    def test_export_tasks_to_json(self):
        import os, json
        from src.main import export_tasks_to_json
        test_file = "test_export.json"
        try:
            tasks = [{"id": 1, "title": "Тестовая задача", "priority": "Высокий", "completed": False}]
            export_tasks_to_json(tasks, test_file)
            self.assertTrue(os.path.exists(test_file))
            with open(test_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["title"], "Тестовая задача")
        finally:
            if os.path.exists(test_file):
                os.remove(test_file)

if __name__ == "__main__":
    unittest.main()
