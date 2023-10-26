"""
請撰寫一程式，要求使用者讀入read.dat（以UTF-8編碼格式讀取），第一列為欄位名稱，第二列之後是個人記錄
請輸出檔案內容並顯示男生人數和女生人數（根據”性別”欄位，0為女性、1為男性）

範例輸出
學號 姓名 性別 科系

101 陳小華 0 餐旅管理

202 李小安 1 廣告

303 張小威 1 英文

404 羅小美 0 法文

505 陳小凱 1 日文
Number of males: 3
Number of females: 2

read.dat檔案內容(請先存成.dat檔案)
學號 姓名 性別 科系
101 陳小華 0 餐旅管理
202 李小安 1 廣告
303 張小威 1 英文
404 羅小美 0 法文
505 陳小凱 1 日文
"""
male = 0
female = 0
with open("read.dat", encoding="UTF-8") as f:
    title = True
    for data in f.readlines():
        print(data)
        if title:
            title = False
            continue

        if int(data.split(" ")[2]) == 1:
            male += 1
        else:
            female += 1

print(f"Number of males: {male}")
print(f"Number of females: {female}")
