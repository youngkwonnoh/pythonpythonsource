import sqlite3

# isolation_level=None(autocommit 여부)

# 데이터베이스 생성
conn = sqlite3.connect("../db/test.db", isolation_level=None)

# Cursor : 인 메모리 방식에서는 Cursor를 통해서 sql 구문 실행
cursor = conn.cursor()
print("cursor : {}".format(type(cursor)))

sql = """
    CREATE TABLE IF NOT EXISTS users(id integer primary key, 
    username text, email text, phone text, website text, regdate text)
"""
cursor.execute(sql)
conn.commit()
conn.close()
