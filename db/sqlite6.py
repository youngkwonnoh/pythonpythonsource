import sqlite3
from datetime import date, datetime

# 데이터 삽입

conn = sqlite3.connect("../db/test.db", isolation_level=None)

# 커서획득
cursor = conn.cursor()

sql = "insert into users values(?, ?, ?, ?, ?, ?)"

# 오늘 날짜 구하기
now = datetime.now()
nowDateTime = now.strftime("%Y-%m-%d %H:%M:%S")

users = (
    (3, 'choi', 'choi@naver.com', '010-3451-3451', 'choi.com', nowDateTime),
    (4, 'lee', 'lee@naver.com', '010-3456-3456', 'lee.com', nowDateTime),
    (5, 'yoo', 'yoo@naver.com', '010-5678-5678', 'yoo.com', nowDateTime)

)

cursor.executemany(sql, users)
conn.commit()
conn.close()