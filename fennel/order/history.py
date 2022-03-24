# 查看历史记录
import click
import time
from fennel.extension import cursor


@click.command()
@click.option("-t")
def show(t):
    try:
        if t is not None:
            # 查询特定记录
            li = t.split("-")
            time_ = time.strptime(li[0] + " " + li[1] + " " + li[2], "%Y %m %d")
            year = time_.tm_year
            month = time_.tm_mon
            day = time_.tm_mday
            if month < 10:
                month = "0" + str(month)
            time_string = str(year) + "-" + str(month) + "-" + str(day)
            res = cursor.execute("SELECT * FROM NOTE WHERE TIME='%s'" % time_string)
            print("%-10s %-10s %-10s %-30s %-s" % ("id", "name", "finish", "time", "descibe"))

            for i, name, finish, desc, ti in res:
                print("%-10s %-10s " % (str(i), name), end="")

                if finish:
                    print("%-10s " % "√", end="")
                else:
                    print("%-10s " % "X", end="")

                print("%-30s " % ti, end="")

                if desc is not None:
                    print(desc, end="")

                print("")

        else:
            res = cursor.execute("SELECT * FROM NOTE")
            print("%-10s %-10s %-10s %-30s %-s" % ("id", "name", "finish", "time", "descibe"))

            for i, name, finish, desc, ti in res:
                print("%-10s %-10s " % (str(i), name), end="")

                if finish:
                    print("%-10s " % "√", end="")
                else:
                    print("%-10s " % "X", end="")

                print("%-30s " % ti, end="")

                if desc is not None:
                    print(desc, end="")

                print("")

    except:
        print("illegal argument: time")
