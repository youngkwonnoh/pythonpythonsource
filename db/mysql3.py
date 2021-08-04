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
    sql = """insert into users(username, email, phone, website) 
    values(%s, %s, %s, %s)
    """

    cursor.execute(sql, ('park', 'park@gmail.com', '010-2345-2345', 'park.com'))

    conn.commit()
    conn.close()

except Exception as e:
    print("연결실패", e)