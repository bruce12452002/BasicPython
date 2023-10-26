"""
請撰寫一程式，將使用者輸入的五個人的資料寫入data.dat檔，每一個人的資料為姓名和電話號碼，以空白分隔
再將檔案加以讀取並顯示檔案內容。

範例輸入
Karen 123456789
Bonnie 235689147
Simon 987612345
Louis 675489321
Andy 019238475

範例輸出
The content of "data.dat":
Karen 123456789

Bonnie 235689147

Simon 987612345

Louis 675489321

Andy 019238475
"""
file_name = "data.dat"
with open(file_name, mode="w") as f:
    for i in range(5):
        f.write(input("請輸入資料: ") + '\n')

with open(file_name) as f:
    print(f'The content of "{file_name}":')
    print(f.read())
