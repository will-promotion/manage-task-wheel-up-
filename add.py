import csv
import os

CSV_FILE = 'tasks.csv'
HEADERS = ['task_content', 'priority', 'due_date', 'memo']

def add_task():
    """
    ユーザーからの入力を受け取り、新しいタスクをCSVファイルに追加する。
    CSVファイルが存在しない場合はヘッダーと共に新規作成する。
    """
    print("\n--- タスク追加 ---")
    task_content = input("ToDoの内容を入力してください: ")
    priority = input("優先度を入力してください (例: 高, 中, 低): ")
    due_date = input("期限を入力してください (例: YYYY-MM-DD): ")
    memo = input("メモを入力してください (任意): ")
# こちらに内容を記入

    new_task = [task_content, priority, due_date, memo]

    file_exists = os.path.isfile(CSV_FILE)

    try:
        with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if not file_exists or os.path.getsize(CSV_FILE) == 0:
                writer.writerow(HEADERS) # ファイルが空ならヘッダーを書き込む
            writer.writerow(new_task)
        print("タスクが追加されました。")
    except IOError:
        print(f"エラー: {CSV_FILE} への書き込みに失敗しました。")
    except Exception as e:
        print(f"予期せぬエラーが発生しました: {e}")

if __name__ == '__main__':
    # add.py を直接実行した場合のテスト用
    add_task()
    # 確認のためにview.pyの関数を一時的に呼び出すなどしても良い
    # from view import view_tasks (循環参照に注意、テスト時のみ)
    # view_tasks()