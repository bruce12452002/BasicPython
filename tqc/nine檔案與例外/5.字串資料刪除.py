"""
請撰寫一程式，要求使用者輸入檔案名稱data.txt和一字串s，顯示該檔案的內容。
接著刪除檔案中的字串s，顯示刪除後的檔案內容並存檔

範例輸入1
data.txt
Tomato
範例輸出1
=== Before the deletion
Apple Kiwi Banana
Tomato Pear Durian
=== After the deletion
Apple Kiwi Banana
 Pear Durian
 
範例輸入2
data.txt
Kiwi
範例輸出2
=== Before the deletion
Apple Kiwi Banana
Tomato Pear Durian
=== After the deletion
Apple  Banana
Tomato Pear Durian
data.txt檔案內容

Apple Kiwi Banana 
Tomato Pear Durian
"""
with open("data905.txt", mode="r+") as f:
    s = input("輸入想刪除的字串: ")
    print("=== Before the deletion")
    data = f.read()
    print(data)
    data = data.replace(s, "")
    print("=== After the deletion")
    print(data)
    f.truncate(0)
    f.seek(0)
    f.write(data)
