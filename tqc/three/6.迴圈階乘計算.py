"""
請使用迴圈敘述撰寫一程式，讓使用者輸入一個正整數n，利用迴圈計算並輸出n!的值

範例輸入
15
範例輸出
1307674368000
"""
n = 15

# for
count = 1
for i in range(1, n + 1):
    count *= i
print(count)

# while
count = 1
i = 1
while i <= n:
    count *= i
    i += 1
print(count)
