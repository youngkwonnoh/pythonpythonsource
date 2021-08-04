import sqlite3

conn = sqlite3.connect("../db/test.db", isolation_level=None)

cursor = conn.cursor()

# cursor.execute("delete from users where id=?", (2, ))
# cursor.execute("delete from users where id=%d" % 3)
cursor.execute("delete from users where id=:id", {'id' : 5})

for row in cursor.execute("select * from users").fetchall():
    print(row)


conn.commit()
conn.close()