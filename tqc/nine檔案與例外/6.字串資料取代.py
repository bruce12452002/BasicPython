"""
請撰寫一程式，要求使用者輸入檔名data.txt、字串s1和字串s2。程式將檔案中的字串s1以s2取代之

範例輸入
data.txt
pen
sneakers
範例輸出
=== Before the replacement
watch shoes skirt
pen trunks pants
=== After the replacement
watch shoes skirt
sneakers trunks pants

data.txt內容
watch shoes skirt
pen trunks pants
"""
with open("data906.txt", "r+") as f:
    data = f.read()
    print("=== Before the replacement")
    print(data)

    print("=== After the replacement")
    data = data.replace(input("請輸入字串一: "), input("請輸入字串二: "))
    print(data)

    f.truncate(0)
    f.seek(0)
    f.write(data)
