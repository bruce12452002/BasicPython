"""
請撰寫一程式，輸入數個整數並儲存至串列中，以輸入-9999為結束點（串列中不包含-9999），
再將此串列轉換成數組，最後顯示該數組以及其長度（Length）、
最大值（Max）、最小值（Min）、總和（Sum）

範例輸入
-4
0
37
19
26
-43
9
-9999
範例輸出
(-4, 0, 37, 19, 26, -43, 9)
Length: 7
Max: 37
Min: -43
Sum: 44
"""
my_list = []
while True:
    n = int(input("請輸入整數:"))
    if n == -9999:
        break
    my_list.append(n)

print(tuple(my_list))
print(f"Length: {len(my_list)}")
print(f"Max: {max(my_list)}")
print(f"Min: {min(my_list)}")
print(f"Sum: {sum(my_list)}")
