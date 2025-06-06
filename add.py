import csv
import os
import pandas as pd

CSV_FILE = 'tasks.csv'
HEADERS = ['task_content', 'priority', 'due_date', 'memo']

# こちらに内容を記入

def add_task():
    task_content = input("追加するタスクの名前: ")
    task_priority = input("優先度: ")
    task_due_day = input("期限: ")
    task_memo = input("メモ: ")
    new_task = pd.DataFrame({
        'task_content': [task_content],
        'priority':[task_priority],
        'due_date':[task_due_day],
        'memo':[task_memo]
    })
    new_task.to_csv('tasks.csv', mode='a', header=False, index=False, encoding='utf-8-sig')
if __name__ == '__main__':
    # add.py を直接実行した場合のテスト用
    add_task()
    # 確認のためにview.pyの関数を一時的に呼び出すなどしても良い
    # from view import view_tasks (循環参照に注意、テスト時のみ)
    # view_tasks()
