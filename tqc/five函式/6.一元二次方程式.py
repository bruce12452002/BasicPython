"""
請撰寫一程式，將使用者輸入的三個整數
（代表一元二次方程式 ax^2+bx+c=0 的三個係數a、b、c）
作為參數傳遞給一個名為compute()的函式，該函式回傳方程式的解，
如無解則輸出【Your equation has no root.】
輸出有順序性

範例輸入1
2
-3
1
範例輸出1
1.0, 0.5

範例輸入2
9
9
8
範例輸出2
Your equation has no root.
"""

'''
判斷 formula = b ** 2 - 4 * a * c 是否有解  
formula > 0  有兩組解          
    ans1 = (-b + formula ** 0.5) / (2 * a)          
    ans2 = (-b - formula ** 0.5) / (2 * a)    
formula == 0 只有一組解        
    output = -b / 2 * a   
formula < 0 無解
'''


def compute(a, b, c):
    formula = b ** 2 - 4 * a * c
    if formula > 0:
        ans1 = (-b + formula ** 0.5) // (2 * a)
        ans2 = (-b - formula ** 0.5) // (2 * a)
        print(f"{ans1}, {ans2}")
    elif formula == 0:
        print(-b / 2 * a)
    else:
        print("Your equation has no root.")


compute(int(input("請輸入第一個整數:")),
        int(input("請輸入第二個整數:")),
        int(input("請輸入第三個整數:")))
