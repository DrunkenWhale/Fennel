import sqlite3
from os import getcwd, sep

conn = sqlite3.connect(getcwd() + sep + "data.db")
cursor = conn.cursor()

def create_table():
    try:
        cursor.execute(
            """
            CREATE TABLE NOTE(
                ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                NAME CHAR(128) NOT NULL,
                FINISH INTEGER DEFAULT 0,
                DESCRIBE CHAR(255),
                TIME DATETIME);
            """
        )
        print("正在初始化数据库")
    except:
        pass
