import sqlite3

# 데이터 조회 : fetchone(), fetchmany(), fetchall()

conn = sqlite3.connect("../db/test.db", isolation_level=None)

cursor = conn.cursor()

sql = "select * from users"
cursor.execute(sql)

print("first : {}".format(cursor.fetchone()))

print("three : {}".format(cursor.fetchmany(size=3)))

print("all : {}".format(cursor.fetchall()))

conn.close()