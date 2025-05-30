import csv
import os

CSV_FILE = 'tasks.csv'
HEADERS = ['task_content', 'priority', 'due_date', 'memo']

# こちらに内容を記入

if __name__ == '__main__':
    delete_task()
    # from view import view_tasks (循環参照に注意、テスト時のみ)
    # print("\n削除後のリスト:")
    # view_tasks()