import sqlite3

# 데이터 조회 : fetchone(), fetchmany(), fetchall()

conn = sqlite3.connect("../db/test.db", isolation_level=None)

cursor = conn.cursor()

# sql =
# cursor.execute("select * from users where id=?", (3,))
# cursor.execute("select * from users where id = %d" % 3)
# print(cursor.fetchone())


# cursor.execute("select * from users where id in (%d, %d)" % (2, 4))
cursor.execute("select * from users where id = :id1 or id=:id2", {"id1":1, "id2":3})
print(cursor.fetchall())

conn.close()