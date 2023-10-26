"""
請撰寫一程式，要求使用者輸入五個人的名字並加入到data.txt的尾端
之後再顯示此檔案的內容

範例輸入
Daisy
Kelvin
Tom
Joyce
Sarah

範例輸出
Append completed!
Content of "data.txt":
Ben
Cathy
Tony
Daisy
Kelvin
Tom
Joyce
Sarah
"""
file_name = 'data903.txt'
with open(file_name, "a+") as f:
    for i in range(5):
        f.write(input("請輸入名字: ") + '\n')

    print("Append completed!")
    print(f'Content of "{file_name}":')

    f.seek(0)
    print(f.read())
