"""
請撰寫一程式，將使用者輸入的五筆資料寫入到write.txt（若不存在，則讓程式建立它），
每一筆資料為一行，包含學生名字和期末總分，以空白隔開。檔案寫入完成後要關閉
將輸入的五筆資料寫入檔案中，不另外輸出於頁面。

範例輸入

Leon 87
Ben 90
Sam 77
Karen 92
Kelena 92
"""
with open("write.txt", mode="at") as f:
    for i in range(5):
        f.write(input("請輸入資料: ") + '\n')
