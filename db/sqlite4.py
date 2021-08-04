import sqlite3

# 데이터 삽입

conn = sqlite3.connect("../db/test.db", isolation_level=None)

# 커서획득
cursor = conn.cursor()

sql = "insert into users values(1, 'kim', 'kim@naver.com', '010-1234-1234', 'kim.com', ?)"

# 오늘 날짜 구하기
now = datetime.now()
nowDateTime = now.strftime("%Y-%m-%d %H:%M:%S")

cursor.execute(sql, (nowDateTime,))
conn.commit()
conn.close()