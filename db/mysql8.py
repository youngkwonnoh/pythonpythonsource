import pymysql

conn = pymysql.connect(
            host='localhost',
            user='root',
            password='12345',
            database='bigdata',
            port=3306,
            charset='utf8')

# 출력결과를 딕셔너리 형태로 보고 싶은 경우
cursor = conn.cursor(pymysql.cursors.DictCursor)

# %s : 모든 데이터 타입 처리 가능
cursor.execute("update users set username = %s where id = %d", ('web', 5))

cursor.execute("select * from users where id = %d", 5)

print(cursor.fetchone())

conn.commit()
conn.close()