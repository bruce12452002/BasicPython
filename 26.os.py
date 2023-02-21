import os
from os import path

print("============ 列出目錄結構 ============")
print(os.getcwd())  # 回傳當前目錄
print(os.listdir())  # 回傳當前「目錄」下的檔案和目錄


p = "/Users/bruce"
# print(os.listdir(p))  # 給路徑，回傳「這一層」的目錄和檔案，路徑不存在「會」報錯
#
# for p, d, f in os.walk(p):  # 給路徑，回傳「多」層的目錄和檔案，路徑不存在「不會」報錯
#     print(f"path={p}, directory={d}, file={f}")

print("============ 增加/刪除空目錄 ============")
p2 = "/a"
if path.exists(p + p2):
    print("exist")
else:
    print("not exist")
    os.mkdir(p + p2)
    print(path.exists(p + p2))
    print(path.join(p, p2))
    os.rmdir(path.join(p, "a"))  # 刪除空目錄，裡面有檔案或目錄會報錯
    print(path.exists(p + p2))

# os.makedirs()  # 新增多層目錄

print("============ path.join 注意事項 ============")
print(path.join("aa", "bb", "cc"))  # aa/bb/cc
print(path.join("/aa", "/bb", "/cc"))  # /cc
print(path.join("/aa", "bb", "cc"))  # /aa/bb/cc
print(path.join("aa", "/bb", "cc"))  # /bb/cc
print(path.join("aa", "/bb", "cc", ""))  # /bb/cc/
# 1. 如果所有參數都不是絕對路徑，會自動增加中間的「/」
# 2. 如果其中一個參數有絕對路徑，會以最後一個絕對路徑開始，前面會忽略
# 3. 如果最後一個參數是空，會自動增加「/」
print(path.sep)  # 回傳系統的分隔符號

print("============ path.split ============")
print(path.split(os.getcwd()))  # 回傳兩個參數，最後一個是「/」後的字串；第一個是前面的路徑，可以是不存在的路徑
print(path.split(os.getcwd() + "/abcdef"))
print(path.dirname(os.getcwd()))  # 取得 split 回傳結果的第一個元素
print(path.basename(os.getcwd()))  # 取得 split 回傳結果的第二個元素
print(path.abspath(".."))  # 給相對路徑或絕對路徑，回傳絕對路徑

print("============ 檔案或目錄 ============")
for d in os.listdir():
    if path.isdir(d):
        print(f"dir={d}, {path.getsize(d)}")  # getsize，單位為 bit
    elif path.isfile(d):
        print(f"file={d}, {path.getsize(d)}")

