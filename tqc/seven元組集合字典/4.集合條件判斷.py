"""
請撰寫一程式，輸入數個整數並儲存至集合，以輸入-9999為結束點（集合中不包含-9999），
最後顯示該集合的長度（Length）、最大值（Max）、最小值（Min）、總和（Sum）

範例輸入
34
-23
29
7
0
-1
-9999
範例輸出
Length: 6
Max: 34
Min: -23
Sum: 46
"""
my_list = list()

while True:
    n = int(input("請輸入整數:"))
    if n == -9999:
        break
    my_list.append(n)

print(f"Length: {len(my_list)}")
print(f"Max: {max(my_list)}")
print(f"Min: {min(my_list)}")
print(f"Sum: {sum(my_list)}")
