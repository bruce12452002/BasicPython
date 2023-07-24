import pandas as pd

# pandas 是使用陣列的功能

print("============ read csv ============")
c = pd.read_csv("./csv_file.csv")
print(c.head())
print(c.shape)  # (4, 3)，四橫三直(三個標題)
print(c.columns)  # Index(['姓名', '電話', '血型'], dtype='object')
print(c.index)  # RangeIndex(start=0, stop=4, step=1)，0~3 四筆
print(c.dtypes)  # 每一欄的資料類型

print("============ read txt ============")
# header=None 表示將標題變成內容；names 表示自訂標籤名稱，沒指定是左到右的索引
# 有 names 時，header 會自動 None
t = pd.read_csv("./txt_file.txt", sep="--", header=None, names=['xxx', 'ooo', 'qoo'])
print(t.head())

print("============ read other ============")
# pd.read_excel("")

import pymysql as mysql

conn = mysql.connect(host='127.0.0.1', user='root', password='123456', database='my_db', charset='utf-8')
pd.read_sql("select * from table", con=conn)
