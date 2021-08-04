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
cursor.execute("select * from users where id in (%d, %d)" % (3, 5))

print(cursor.fetchone())

conn.close()