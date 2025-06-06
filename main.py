# 各機能モジュールをインポート
import add
import view
import delete
# import os # CSVファイル初期化などで必要に応じて

# CSV_FILE_PATH = 'tasks.csv'
# CSV_HEADERS = ['task_content', 'priority', 'due_date', 'memo']

def main():
    # initialize_csv() # 必要であれば呼び出す

    while True:
        print("\nToDoリスト アプリ")
        print("1: タスクを表示")
        print("2: タスクを追加")
        print("3: タスクを削除")
        print("4: 終了")

        choice = input("操作を選んでください (1-4): ")

        if choice == '1':
            view.view_tasks()
        elif choice == '2':
            add.add_task()
        elif choice == '3':
            delete.delete_task()
        elif choice == '4':
            print("アプリを終了します。")
            break
        else:
            print("無効な選択です。1から4の数字を入力してください。")

if __name__ == '__main__':
    main()