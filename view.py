import csv
import os

CSV_FILE = 'tasks.csv'

df = pd.read_csv(CSV_FILE)

for index, row in df.iterrows():
    print(f'【{index+1}行目】')
    for column in df.columns:
        print(f'{column}: {row[column]}')
    print('----------------------')

if __name__ == '__main__':
    view_tasks()