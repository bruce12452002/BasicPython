"""
請使用選擇敘述撰寫一程式，讓使用者輸入兩個整數a、b，
然後再輸入一算術運算子 (+、-、*、/、//、%） ，輸出經過運算後的結果

範例輸入
30
20
*
範例輸出1
600
"""
a = int(input("請輸入一個整數:"))
b = int(input("請再輸入一個整數:"))
sign = input("請輸入 +、-、*、/、//、% 其中之一:").strip()

if sign == '+':
    print(a + b)
elif sign == '-':
    print(a - b)
elif sign == '*':
    print(a * b)
elif sign == '/':
    print(a / b)
elif sign == '//':
    print(a // b)
elif sign == '%':
    print(a % b)
