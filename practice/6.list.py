# 1.給一個整數，用迴圈將平方放入 list。
# 如果給 5，表示 list 裡有 5 個元素，分別是 1 4 9 16 25，也就是 1 的平方 ~ 5 的平方
#
n = 5
my_list = []

for i in range(1, n + 1):
    my_list.append(i * i)
print(my_list)

# 2.將 list2 加到 list1 裡並在最後增加 7，最後在索引 1 的位置增加 2，
# 結果 list1 裡的元素是 1~7 才是正確的
list1 = [1, 3, 4]
list2 = [5, 6]
#
list1.extend(list2)
list1.append(7)
list1.insert(1, 2)
print(list1)

# 3.使用迴圈印出上一題 list1 的元素
#
for i in list1:
    print(i, end=" ")
print()

# 4.清空上一題 list1 的所有元素
#
list1.clear()
print(list1)

# 5.刪除 ls 裡的元素 c
ls = ['a', 7, False, 'c', 5.6]
#
# del ls[3]
ls.remove("c")
print(ls)
