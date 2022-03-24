# 查看历史记录
import click
import time
from fennel.extension import cursor,conn


@click.command()
@click.argument("-n")
@click.option("-d")
@click.option("-t")
def add(_n, d, t):
    if d is None and t is None:
        cursor.execute("INSERT INTO NOTE(NAME,TIME) VALUES ('%s',(SELECT DATE('now'))) " % _n)
    elif d is None and t is not None:
        cursor.execute("INSERT INTO NOTE(NAME,TIME) VALUES ('%s','%s') " % (_n, t))
    elif d is not None and t is None:
        cursor.execute("INSERT INTO NOTE(NAME,DESCRIBE,TIME) VALUES ('%s','%s',(SELECT DATE('now'))) " % (_n, d))
    else:
        cursor.execute("INSERT INTO NOTE(NAME,DESCRIBE,TIME) VALUES ('%s','%s','%s') " % (_n, d, t))
    conn.commit()