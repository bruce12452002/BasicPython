# [from 模組名稱] import [模組 | 類別 | 變數 | 方法 | *] [as 別名]
# import time  # 使用 time 模組，裡面的方法都可以使用
# time.sleep(3)
# time.localtime()

# from time import sleep  # 使用 time 模組裡面的 sleep 方法，只有 sleep 可以使用
# sleep(3)
# # localtime()  # 編譯錯誤

# from time import sleep as s
# s(3)

# from time import *
#
# import my_dir.my_module
#
# sleep(3)  # 如果用第 2 行的 import time，必須寫 time.，用這個不用

print("============ 自定義模組 ============")
# import my_dir.my_module
#
# print(my_dir.my_module.add(2, 3))

# from my_dir.my_module import add as a
#
# print(a(2, 3))

# 不同模組的同名功能，也就是 from 不同，import 相同，會後者蓋前者


from my_dir.my_module import *

# from my_dir.my_module import add, multiply
print(add(2, 3))
print(multiply(2, 3))

# import my_package.m1
# import my_package.m2
#
# my_package.m1.module1()
# my_package.m2.module2()


# from my_package import *
# module1()
# module2()

# from my_package.m1 import *
# from my_package.m2 import *
# module1()
# module2()  # from 指到檔案是可以的
