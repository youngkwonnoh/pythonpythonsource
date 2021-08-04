import sqlite3

conn = sqlite3.connect("../db/test.db", isolation_level=None)

cursor = conn.cursor()

# cursor.execute("update users set username=? where id=?", ('hong', 2))
# cursor.execute("update users set username='%s' where id=%d" % ('son', 3))
cursor.execute("update users set username=:username where id=:id", {'username' : 'park', 'id' : 2})

for row in cursor.execute("select * from users").fetchall():
    print(row)


conn.commit()
conn.close()