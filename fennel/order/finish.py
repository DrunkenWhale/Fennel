# 查看历史记录
import click
from fennel.extension import cursor, conn


@click.command()
@click.argument("id")
def finish(id):
    cursor.execute("UPDATE NOTE SET FINISH = 1 WHERE ID = %s" % id)
    conn.commit()
