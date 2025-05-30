import csv
import os

CSV_FILE = 'tasks.csv'

def view_tasks():
    """
    CSVファイルからタスクを読み込み、一覧表示する。
    タスクがない場合はその旨を表示する。
    """
    print("\n--- ToDoリスト ---")
    if not os.path.isfile(CSV_FILE) or os.path.getsize(CSV_FILE) == 0:
        print("タスクはありません。")
        return

    try:
        with open(CSV_FILE, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader, None) # ヘッダー行を読み飛ばすか確認

            if not headers:
                print("タスクファイルは空か、ヘッダーがありません。")
                return

            tasks = list(reader)
            if not tasks:
                print("タスクはありません。")
                return

            print(f"{'No.':<5} {'内容':<30} {'優先度':<10} {'期限':<15} {'メモ':<30}")
            print("-" * 90)
            for i, task in enumerate(tasks):
                # taskが十分な要素数を持っているか確認
                if len(task) == len(headers):
                    print(f"{i+1:<5} {task[0]:<30} {task[1]:<10} {task[2]:<15} {task[3]:<30}")
                else:
                    # 要素数が足りない場合の表示（エラーハンドリングの一環）
                    print(f"{i+1:<5} --- データ形式不正 ---")

    except FileNotFoundError:
        print("タスクファイルが見つかりません。")
    except StopIteration: # ヘッダーしかない空ファイルの場合
        print("タスクはありません。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == '__main__':
    view_tasks()