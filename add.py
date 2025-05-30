import csv
import os

CSV_FILE = 'tasks.csv'
HEADERS = ['task_content', 'priority', 'due_date', 'memo']

# こちらに内容を記入


if __name__ == '__main__':
    # add.py を直接実行した場合のテスト用
    add_task()
    # 確認のためにview.pyの関数を一時的に呼び出すなどしても良い
    # from view import view_tasks (循環参照に注意、テスト時のみ)
    # view_tasks()