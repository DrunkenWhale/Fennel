import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()


def boot():
    pass


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