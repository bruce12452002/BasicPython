# 倒序輸出 my_tuple 的內容
my_tuple = ("a", "b", "c", "d")

# 方法一
my_list = list(my_tuple)
my_list.reverse()
print(my_list)

# 方法二
for i in range(len(my_tuple) - 1, -1, -1):
    print(my_tuple[i], i, end=" ")
