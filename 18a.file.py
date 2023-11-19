import os

print("============ os ============")
p = '.'
print(os.path.exists(p))
print(os.path.isfile(p))
print(os.path.isdir(p))
# os.mkdir(p + "/xxx")  # 有會報錯
# os.rmdir(p + "/xxx")  # 沒有會報錯


# open 打開檔案
# encoding 預設是 None
# mode： r(read) w(write) a(append) x(execute) t(text) b(binary) +(read and write) 預設為rt
# 常用的為 r w a r+ w+ a+
# r 可讀不可寫； w 可寫不可讀，寫的時候會覆蓋之前的； a 可寫不可讀，寫的時候從最後增加
# open("test.txt", encoding="UTF-8")，mode 不設定預設是 rt，也就是讀取文字檔
# 沒有什麼 rw，如果讀寫都要，可用 +，19b會說明

print("============ 讀檔一 ============")
read_file = open("test.txt", "r", encoding="UTF-8")
print(type(read_file))
# print(read_file.read(5))  # 讀 5 個 Byte
# print(read_file.read())  # 全部讀(從上次讀的地方繼續讀)

print(f"{read_file.readline()}")  # 一次讀一行(從上次讀的地方繼續讀)，讀完了再調這個方法也不會報錯，什麼都沒做而已
# print(f"{read_file.readlines()}")  # 全部讀(從上次讀的地方繼續讀)
for f in read_file:
    print(f, end="")
# time.sleep(3)  # 睡 3 秒
read_file.close()  # 解除佔用的檔案，關閉完才可以對檔案做寫的動作

print("============ 讀檔二 ============")
with open("test.txt", "r", encoding="UTF-8") as rf:  # with-open 結束時會自動 close，就算遇到 exception 也可以
    print(rf.readlines())

print("============ 讀 csv 檔 ============")
import csv

file = open("salary.csv", encoding='UTF-8')
reader = csv.reader(file)
# i = 0
# while i < 4:
#     print(next(reader))
#     i += 1

# next 完了之後，reader 就不會往下跑了
for r in reader:
    print(r)

file.close()

print("============ 寫檔一 ============")
write_file = open("test2.txt", "w", encoding="UTF-8")  # 檔案不在會自動新增，但再次執行會覆蓋原本的內容，可改用 a
write_file.write("hello file\n")
write_file.write("end")
write_file.flush()
write_file.close()

print("============ 寫檔二 ============")
with open("test2.txt", "w", encoding="UTF-8") as wf:
    wf.write("hello file\n")
    wf.write("end")
    wf.flush()

print("============ 讀寫檔 ============")
# with open("test.txt", "a+", encoding="utf-8") as ra:
#     ra.seek(0)  # 注意非 ASCII 編碼的 Byte 大小
#     print(ra.readline(), end=" ")
#
#     ra.seek(13)
#     print(ra.readline(), end=" ")
#
#     ra.write("haha")

print("============ 讀 git 的 hash 檔 ============")
import zlib

with open("b97155ddcb78999738c8380449abf2fe03c8f3", "rb") as h:
    # b'blob 5\x00xxx \n'，也就是 b'型態 長度\x00內容 \n'
    print(zlib.decompress(h.read()))
