import sqlite3
from pathlib import Path
import sys

db_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("students_day18.db")

connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# TODO 1:
# 使用 cursor.execute() 執行 CREATE TABLE IF NOT EXISTS
# 欄位結構必須與目前 students 資料表相同

cursor.execute(
    "CREATE TABLE IF NOT EXISTS students(" \
    "id INTEGER PRIMARY KEY," \
    "name TEXT," \
    "score INTEGER);"
)


# TODO 2:
# 將資料庫變更正式儲存

connection.commit()


# TODO 3:
# 關閉資料庫連線

connection.close()


print("Database initialized successfully.")