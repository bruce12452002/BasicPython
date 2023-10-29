print("============ while ============")
i = 0
while i < 10:
    print(i, end=' ')
    i += 1
print()

# while True:
#     pass  # 什麼都不做，但還是有在執行，所以是無限迴圈

print("============ for ============")
# for 不會有無限迴圈
letter = "abc"
for i in letter:
    print(i, end=' ')
print()

print("============ for-range 一 ============")
# range 預設是 0:x:1
for i in range(5):
    print(i, end=' ')
print()

print("============ for-range 二 ============")
for i in range(5, 10):
    print(i, end=' ')
print()

print("============ for-range 三 ============")
for i in range(1, 10, 2):
    print(i, end=' ')
print()

for i in range(0, -10, -2):
    print(i, end=' ')
print()

print("============ break continue ============")
for i in range(5, 10):
    if i == 6:
        continue
    if i == 8:
        break
    print(i, end=' ')
print()

print("============ for-else ============")
for i in range(5, 10):
    if i == 9:
        continue
    # if i == 8:
    #     break
    print(i, end=' ')
else:
    print("finish")  # 如果被 break 或拋出例外，就沒執行了
print()

print("============ while-else ============")
i = 0
while i < 10:
    if i == 8:
        break
    i += 1
    if i == 10:
        continue
    print(i, end=' ')
else:
    print("finish")  # 如果被 break 或拋出例外，就沒執行了
print()

print("============ 模擬 do-while ============")
# 有些程式語言有 do while 的迴圈，功能是至少會執行一次迴圈
# 只要將判斷寫在 while 內部，然後將判斷條件改相反就可以完成這個功能

# 如下，一次都不會執行
i = 0
while i > 0:
    print("我執行了")
    i -= 1

# 多個 if 之後，將條件改相反即可
i = 0
while True:
    print("我執行了")
    if i <= 0:
        break
    i -= 1
