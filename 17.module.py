print("============ 自定義模組 ============")
print("============ 1.import ============")
import my_dir.my_module

print(my_dir.my_module.add(2, 3))

print("============ 2.import-as ============")
import my_dir.my_module as mm

print(mm.add(2, 3))

print("============ 3.from-import ============")
from my_dir.my_module import add, multiply

# import 多個時，用逗號隔開
print(add(2, 3))
print(multiply(2, 3))

print("============ 4.from-import-as ============")
# 可以有些用 as，有些不用 as
from my_dir.my_module import add as a, multiply as m

print(a(2, 3))
print(m(2, 3))

print("============ 5.from-import-* ============")
from my_dir.my_module import *

print(add(2, 3))
print(multiply(2, 3))

print("============ 6.package 的 __init__ ============")
'''
import my_package

# import my_package.m2

my_package.m1.module1()
# my_package.m2.module2()

from my_package import *

module1()
# module2()
'''
print("============ 7-1.檔案 裡的 __all__ ============")
'''
from my_package.m2 import *

module2()
# module4()
'''

print("============ 7-2.__init__ 檔案 裡的 __all__ ============")
'''
from my_package import *

module1()
module2()
# module3()
# module4()
'''

print("============ 8.同名覆蓋 ============")
# from 不同，import 相同，會後者蓋前者
from my_package.m1 import module1
from my_package.m2 import module1

# 如果 import *，找到就會用
# from my_package.m2 import *
# from my_package.m1 import *

module1()

print("============ 內鍵模組 ============")
import time  # 使用 time 模組，裡面的方法都可以使用
time.sleep(3)
time.localtime()

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
