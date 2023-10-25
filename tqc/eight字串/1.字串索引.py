"""
請撰寫一程式，要求使用者輸入一字串，顯示該字串每個字元的索引。

範例輸入
Sandwich
範例輸出
Index of 'S': 0
Index of 'a': 1
Index of 'n': 2
Index of 'd': 3
Index of 'w': 4
Index of 'i': 5
Index of 'c': 6
Index of 'h': 7
"""
st = "Sandwich"

print("方法一")
for i, s in enumerate(st):
    print(f"Index of '{s}': {i}")

print("方法二")
index = 0
for s in st:
    print(f"Index of '{s}': {index}")
    index += 1
