# 1.倒序輸出 my_tuple 的內容
my_tuple = (7, 8, 9, 10)

# 方法一
# rtn = list(my_tuple)
# rtn.reverse()
# print(rtn)

# 方法二
for i in range(len(my_tuple), 0, -1):
    print(my_tuple[i - 1], end=" ")
print()

# 2.以下的 abcde_tuple 少了元素 b，請將 b 插入正確位置
abcde_tuple = ('a', "c", 'd', 'e')
#
rtn = list(abcde_tuple)
rtn.insert(1, "b")
print(rtn)

# 3.承上題，取得 abcde_tuple 元素裡， d 的索引值

# 4.輸出 tup 裡的元素 c 有幾個
tup = ('c', "a", "b", 'c', False, 'c', 56)
#
