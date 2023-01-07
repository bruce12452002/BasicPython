# 沒有 break，只會執行其中一個條件
# 只可以完全匹配，不能有 > <

print("============ match-case 一 ============")
key = "oo"
match key:
    case "x" | "xx":  # case 裡不可用 or
        print("xxx")
    case "o":
        print("ooo")
    case _:  # _ 就是預設值，可選
        print("default")
    #  ValueError("Not a x or o")  # 可以拋出例外

print("============ match-case 二 ============")
# 資料結構可判斷 list tuple dict，但 set 不支援
z = (7, 8)  # list tuple 可混合判斷，元素要完全匹配才可以
# z = {"k": 1}
match z:
    case (1, 2):
        print("one")
    case (7, 8):
        print("two")
    case {"k": 1}:
        print("three")

print("============ match-case 三 ============")


class Animal:
    num: int = 99
    name: str = "monkey"
    age: int = 2


a = Animal()
b = "xx"
c = "xx"
match a:
    case Animal(num=78, name="dog"):
        print("dog")
    case Animal(name="monkey", num=98):
        print("monkey")
    case Animal(name="monkey", num=99) if b == c:  # 兩個條件都得達成
        print("same")
    case _:
        print("default")

print("============ match-case 四 ============")
from enum import Enum


class Car(Enum):
    TOYOTA = "Japan",
    HONDA = "Japan",
    TESLA = "America"


car = Car.TOYOTA
match car:
    case Car.TESLA:
        print("a")
    case Car.HONDA:
        print("b")
    case Car.TESLA:
        print("c")
