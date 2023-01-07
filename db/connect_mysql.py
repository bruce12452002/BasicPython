# 須先下載 PyMySQL 才可以 import
from pymysql import Connection

conn = Connection(
    host="localhost",
    user="root",
    password="123456",
    database="my_db",
    port=3306,
    # autocommit=True
)

print(conn.get_server_info())
# conn.select_db("my_db")
cursor = conn.cursor()
cursor.execute("select * from zodiac")
# cursor.fetchone()  # 取一筆
# cursor.fetchmany(5)  # 取多少筆
print(cursor.description)  # 取欄位名稱細項
result_set = cursor.fetchall()
for r in result_set:
    print(f"{r}, {type(r)}")
cursor.close()
conn.close()

print("========== 提交/回滾 ==========")
conn = Connection(
    host="localhost",
    user="root",
    password="123456",
    database="my_db",
    port=3306,
    # autocommit=True
)
# 如果 sql 是增刪改，也沒有自動提交，就要 commit 才會生效
try:
    cursor = conn.cursor()
    cursor.execute("insert into zodiac values(10, '雞', 'chicken', '啄', 30)")
    # i = 1 / 0
except Exception as ex:
    print(ex)
    conn.rollback()
else:
    conn.commit()
    print("success")
finally:
    cursor.close()
    conn.close()
