# 每個檔案都可以有 __all__，這樣要一個一個檔案打開看很麻煩
# 這個檔案可以有個統一管理的作用

from my_package.m1 import *

# __all__，只有在使用 from my_package import * 才會有影響
# 表示只能使用哪個模組或方法
# 如果不寫 __all__，不會有限制
__all__ = ['module1']
