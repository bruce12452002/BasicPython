"""
請使用迴圈敘述撰寫一程式，要求使用者輸入一個數字，此數字代表後面測試資料的數量
每一筆測試資料是一個正整數（由使用者輸入），將此正整數的每位數全部加總起來

輸入與輸出會交雜如下，輸出的部份以粗體字表示 1
1 -> 輸入
98765 -> 輸入
Sum of all digits of 98765 is 35 -> 輸出

輸入與輸出會交雜如下，輸出的部份以粗體字表示 2
3 -> 輸入
32412 -> 輸入
Sum of all digits of 32412 is 12 -> 輸出
0 -> 輸入
Sum of all digits of 0 is 0 -> 輸出
769 -> 輸入
Sum of all digits of 769 is 22 -> 輸出
"""

n = int(input("請輸入測試次數:"))
for i in range(n):
    data = input("請輸入測試資料(正整數):")

    count = 0
    for j in range(len(data)):
        count += int(data[j])
    print("Sum of all digits of {} is {}".format(data, count))
