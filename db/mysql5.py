import pymysql

conn = pymysql.connect(
            host='localhost',
            user='root',
            password='12345',
            database='bigdata',
            port=3306,
            charset='utf8')

cursor = conn.cursor()

sql = "select * from users"
cursor.execute(sql)

print(cursor.fetchone())
print(cursor.fetchmany(size=3))
print(cursor.fetchall())


conn.close()