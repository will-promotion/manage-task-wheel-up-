import csv
import os

CSV_FILE = 'tasks.csv'
HEADERS = ['task_content', 'priority', 'due_date', 'memo']


def delete_task():
    delete_content = input("削除するタスクの内容を入力してください: ")
    temp_file = 'temp_tasks.csv'
    task_found = False

    # 読み書きモードで一時ファイルを開く
    with open(CSV_FILE, 'r', newline='', encoding='utf-8') as infile, \
            open(temp_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=HEADERS)

        # ヘッダーを一時ファイルに書き込む
        writer.writeheader()

        # 各行を読み込み、削除対象でなければ一時ファイルに書き込む
        for row in reader:
            if row['task_content'] == delete_content:
                task_found = True
                print(f"タスク「{delete_content}」を削除しました。")
            else:
                writer.writerow(row)

    if task_found:
        # 元のファイルを削除し、一時ファイルをリネーム
        os.remove(CSV_FILE)
        os.rename(temp_file, CSV_FILE)
    else:
        print(f"タスク「{delete_content}」は見つかりませんでした。")
        # タスクが見つからなかった場合、一時ファイルは不要なので削除
        os.remove(temp_file)


if __name__ == '__main__':
    delete_task()
    
    # 削除後のリストを確認したい場合は、view_tasks関数（別途実装）を呼び出してください
    # from view import view_tasks
    # print("\n削除後のリスト:")
    # view_tasks()