# 1.倒序輸出 my_tuple 的內容
my_tuple = ("a", "b", "c", "d")

# 方法一
my_list = list(my_tuple)
my_list.reverse()
print(my_list)

# 方法二
for i in range(len(my_tuple) - 1, -1, -1):
    print(my_tuple[i], i, end=" ")

# 2.以下的 tuple 少了 b，請將 b 插入正確位置


# 3.承上題，取得 abcde_tuple 元素裡， d 的索引值


# 4.輸出 tup 裡的元素 c 有幾個
tup = ('c', "a", "b", 'c', False, 'c', 56)
