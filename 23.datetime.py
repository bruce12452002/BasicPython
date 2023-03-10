# https://docs.python.org/zh-tw/3/library/datetime.html#strftime-and-strptime-format-codes
import datetime
import time

print("============ 取得現在時間 ============")
# now 可以給 timezone；today 不行

now = datetime.datetime.now()
today = datetime.datetime.today()
print(f"now={now}, today={today}")
print(now.year, now.month, now.day)
print(now.hour, now.minute, now.minute, now.microsecond)
print(today.strftime("%Y/%m/%d %H:%M:%S.%f"))

# now 給時區
tzone = datetime.timezone(datetime.timedelta(hours=-5))
print(datetime.datetime.now(tz=tzone))

print("============ 設定時間 ============")
print(datetime.date(2000, 10, 1))
print(datetime.time(14, 20, 55, 666666))
print(datetime.datetime(2010, 1, 10, 17, 20, 5, 222))

print("============ 時間和時間戳轉換 ============")
# 日期字串轉成時間
time1 = time.strptime("2020/10/01 15:26:37.123456", "%Y/%m/%d %H:%M:%S.%f")  # strptime -> str parse time

# 時間轉日期字串
print(time.strftime("%Y-%m-%d %H:%M:%S", time1))  # strftime -> str from time

# 時間轉時間戳
timestamp = int(time.mktime(time1))
print(timestamp)

# 時間戳轉日期字串
time2 = time.localtime(timestamp)
print(time.strftime("%Y-%m-%d %H:%M:%S", time2))
