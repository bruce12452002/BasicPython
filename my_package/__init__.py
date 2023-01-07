# 每個檔案都可以有 __all__，這樣要一個一個檔案打開看很麻煩，這個檔案是做統一管理的作用
from my_package.m1 import *

__all__ = ['module1']
