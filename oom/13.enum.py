import enum
from enum import Enum
from functools import total_ordering


class Zodiac(Enum):
    RAT = 1
    OX = 2
    TIGER = 3
    RABBIT = 4
    DRAGON = 5
    SNAKE = 6
    HORSE = 7
    SHEEP = 8
    MONKEY = 9
    CHICKEN = 10
    DOG = 11
    PIG = 12


print(Zodiac.DRAGON)
print(Zodiac.DRAGON.name)
print(Zodiac.DRAGON.value)


# Zodiac.DRAGON = 999  # 編譯錯誤

def get_zodiac(z: Zodiac):
    if z == Zodiac.DRAGON:
        print(Zodiac.DRAGON.value)
    else:
        print(z.name)


get_zodiac(Zodiac.RAT)
# Zodiac.name  # 錯誤，不曉得要取得哪一個
print(Zodiac["OX"], Zodiac["OX"].name, Zodiac["OX"].value)
print(Zodiac(10), Zodiac(10).name, Zodiac(10).value)
# Zodiac["aaa"]  # 值對映不到就報錯了

print("============ 遍例 ============")
for zo in Zodiac:
    print(zo)

print("============ 重複的 value ============")
"""
相同的 value 時，整個鍵值對是一組，由上而下，第一個為主要的，其他都算別名
"""


# @enum.unique  # 注意 unique 是小寫的，如果不想讓 value 有重覆可加這個裝飾器
class KeyValue(Enum):
    A = "aa"
    B = "bb"
    C = "aa"
    D = "bb"


for kv in KeyValue:
    print(kv)  # 只會印出主要的

print(KeyValue("bb"))  # 得到主要的
print(KeyValue.__members__)  # 全部都會取得到
for k, v in KeyValue.__members__.items():
    print(k, v, sep="=")

print("============ 特殊方法 ============")


@total_ordering  # 如果 value 想支援排序可用這個裝飾器 + __lt__ 方法
class Computer(Enum):
    NAME = 111
    COLOR = 222
    WEIGHT = 333

    def __str__(self):
        return f"{self.name} {self.value}"  # 印出來時會調用

    def __eq__(self, other):  # == 時會調用
        if isinstance(other, int):
            return self.value == other

        if isinstance(other, str):
            return self.name == other.upper()

        """
        原本 Computer.COLOR == Computer.COLOR 會是 True，但寫了這個方法變 False，所以必需加這個判斷
        """
        if isinstance(other, Computer):
            return self is other

        return False

    def __lt__(self, other):  # < 時會調用
        if isinstance(other, int):
            return self.value < other

        if isinstance(other, Computer):
            return self.value < other.value


print(Computer.COLOR)
print(Computer.COLOR == 222)
print(Computer.COLOR == "color")
print(Computer.COLOR == Computer.COLOR)

print(Computer.COLOR < 333)
print(Computer.COLOR < Computer.WEIGHT)
