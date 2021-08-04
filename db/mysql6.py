import pymysql

conn = pymysql.connect(
            host='localhost',
            user='root',
            password='12345',
            database='bigdata',
            port=3306,
            charset='utf8')

cursor = conn.cursor()

# %s : 모든 데이터 타입 처리 가능
sql = "select * from users where id = %s"
cursor.execute(sql, 3)

print(cursor.fetchone())

conn.close()