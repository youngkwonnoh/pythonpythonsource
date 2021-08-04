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
    users = (
        ('choi', 'choi@naver.com', '010-3451-3451', 'choi.com'),
        ('lee', 'lee@naver.com', '010-3456-3456', 'lee.com'),
        ('yoo', 'yoo@naver.com', '010-5678-5678', 'yoo.com')

    )

    sql = """insert into users(username, email, phone, website) 
    values(%s, %s, %s, %s)
    """

    cursor.executemany(sql, users)

    conn.commit()
    conn.close()

except Exception as e:
    print("연결실패", e)