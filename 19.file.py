import os

print("============ os ============")
p = '.'
print(os.path.exists(p))
print(os.path.isfile(p))
print(os.path.isdir(p))
# os.mkdir(p + "/xxx")  # 有會報錯
# os.rmdir(p + "/xxx")  # 沒有會報錯

import time
# open 打開檔案；mode： r(read)w(write)a(append)預設為r  encoding 預設是 None

print("============ 讀檔一 ============")
read_file = open("test.txt", "r", encoding="UTF-8")
print(type(read_file))
# print(file.read(5))  # 讀 5 個 Byte
# print(file.read())  # 全部讀(從上次讀的地方繼續讀)

print(f"{read_file.readline()}")  # 一次讀一行(從上次讀的地方繼續讀)，讀完了再調這個方法也不會報錯，什麼都沒做而已
# print(f"{file.readlines()}")  # 全部讀(從上次讀的地方繼續讀)
for f in read_file:
    print(f, end="")
# time.sleep(3)  # 睡 3 秒
read_file.close()  # 解除佔用的檔案，關閉完才可以對檔案做寫的動作

print("============ 讀檔二 ============")
with open("test.txt", "r", encoding="UTF-8") as rf:  # with-open 結束時會自動 close，就算遇到 exception 也可以
    print(rf.readlines())

print("============ 寫檔一 ============")
write_file = open("test2.txt", "w", encoding="UTF-8")  # 檔案不在會自動新增，但再次執行會覆蓋原本的內容，可改用 a
write_file.write("hello file\n")
write_file.write("end")
write_file.flush()
write_file.close()

print("============ 寫檔二 ============")
# with open("test2.txt", "w", encoding="UTF-8") as wf:
#     wf.write("hello file\n")
#     wf.write("end")
#     wf.flush()
