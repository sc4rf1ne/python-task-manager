# Python Task Manager

Консольный менеджер задач на языке Python для планирования, отслеживания статуса и управления списком задач.

## Структура проекта

```text
python-task-manager/
├── src/
│   └── main.py
├── tests/
│   └── test_main.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Основные функции
- `add_task(tasks, title, priority)` — добавление новой задачи с приоритетом;
- `complete_task(tasks, task_id)` — отметка задачи как выполненной;
- `get_all_tasks(tasks)` — получение форматированного списка всех задач.
