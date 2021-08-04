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

cursor.execute(sql, (2, 'park', 'park@naver.com', '010-2345-2345', 'park.com', nowDateTime))
conn.commit()
conn.close()