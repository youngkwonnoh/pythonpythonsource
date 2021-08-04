import pymysql

try:
    conn = pymysql.connect(
            host='localhost',
            user='root',
            password='12345',
            database='bigdata',
            port=3306,
            charset='utf8'
    )
    print("연결성공")
except Exception as e:
    print("연결실패")