"""
請撰寫一程式，讀取read.txt的內容（內容為數字，以空白分隔）並將這些數字加總後輸出
檔案讀取完成後要關閉

範例輸出
660
read.txt內容

11 22 33 22 33 44 33 44 55 44 55 66 55 66 77
"""
with open("read.txt", "rt") as r:
    count = 0
    for i in r.readline().split(" "):
        count += int(i)
    print(count)
