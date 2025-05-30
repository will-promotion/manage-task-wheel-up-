import csv
import os

CSV_FILE = 'tasks.csv'
HEADERS = ['task_content', 'priority', 'due_date', 'memo']

def delete_task():
    """
    タスク一覧を表示し、ユーザーに削除したいタスクの番号を入力させ、
    該当タスクをCSVファイルから削除する。
    """
    print("\n--- タスク削除 ---")
    # まず現在のタスクを表示 (view.pyの機能を一部借用、またはview.pyをimport)
    # ここでは簡略化のため、view.pyの主要ロジックを再利用する形で記述
    if not os.path.isfile(CSV_FILE) or os.path.getsize(CSV_FILE) == 0:
        print("削除できるタスクがありません。")
        return

    tasks = []
    try:
        with open(CSV_FILE, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers_read = next(reader, None) # ヘッダー読み込み
            if not headers_read: # ヘッダーすらない空ファイル
                print("削除できるタスクがありません。")
                return
            tasks = list(reader)

        if not tasks:
            print("削除できるタスクがありません。")
            return

        print("現在のタスク:")
        print(f"{'No.':<5} {'内容':<30}")
        print("-" * 40)
        for i, task_row in enumerate(tasks):
            if task_row: # 空行などをスキップ
                print(f"{i+1:<5} {task_row[0]:<30}") # 内容のみ表示

        while True:
            try:
                task_num_str = input("削除したいタスクの番号を入力してください (キャンセルする場合はc): ")
                if task_num_str.lower() == 'c':
                    print("削除をキャンセルしました。")
                    return
                task_num = int(task_num_str)
                if 1 <= task_num <= len(tasks):
                    break
                else:
                    print(f"1から{len(tasks)}の間の番号を入力してください。")
            except ValueError:
                print("有効な番号を入力してください。")

        deleted_task = tasks.pop(task_num - 1) # 0-indexedに変換

        # ヘッダーを含めてファイルに書き戻す
        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(HEADERS) # グローバル変数または読み込んだヘッダーを使用
            writer.writerows(tasks)

        print(f"タスク「{deleted_task[0]}」を削除しました。")

    except FileNotFoundError:
        print("タスクファイルが見つかりません。")
    except StopIteration:
        print("削除できるタスクがありません。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")


if __name__ == '__main__':
    delete_task()
    # from view import view_tasks (循環参照に注意、テスト時のみ)
    # print("\n削除後のリスト:")
    # view_tasks()