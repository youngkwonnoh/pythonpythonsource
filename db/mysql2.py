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

    cursor = conn.cursor()

    # id(auto_increment, regdate(timestamp)
    sql = "insert into users(username, email, phone, website) values('hong', 'hong@naver.com', '010-1234-1234', 'hong.com')"

    cursor.execute(sql)

    conn.commit()
    conn.close()

except Exception as e:
    print("연결실패", e)