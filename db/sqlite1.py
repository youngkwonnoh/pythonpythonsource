import sqlite3
from datetime import date, datetime

print("sqlite3.version {}".format(sqlite3.version))
print("sqlite3.sqlite_version {}".format(sqlite3.sqlite_version))

now = datetime.now()
print("now : {}".format(now))

nowDateTime = now.strftime("%Y-%m-%d %H:%M:%S")
print("nowDateTime : {}".format(nowDateTime))