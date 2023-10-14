"""
請撰寫一程式，將使用者輸入的三個參數，
變數名稱分別為a（代表字元character）、x（代表個數）、y（代表列數），
作為參數傳遞給一個名為compute()的函式，該函式功能為：一列印出x個a字元，
總共印出y列
輸出的每一個字元後方有一空格

範例輸入

e
5
4
範例輸出

e e e e e 
e e e e e 
e e e e e 
e e e e e 
"""


def compute(character, row, column):
    for i in range(column):
        for j in range(row):
            print(f"{character:<2}", end="")
        print()

    print("利用字串的 *")
    for i in range(column):
        print(f"{character:<2}" * row)


a = input("請輸入一個字元:")
x = int(input("請輸入 row 數:"))
y = int(input("請輸入 column 數:"))

compute(character=a, row=x, column=y)
