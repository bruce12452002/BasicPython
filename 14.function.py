# 方法為了可以重覆調用、縮短程式碼
# 預設無法取得方法外變數，除非用 global、nonlocal
print("============ 內鍵方法 ============")
print(len("abc"))

print("============ 宣告方法 ============")


def function_name(param1, param2):
    """
    將兩個參數相加並回傳結果
    :param param1: 數字
    :param param2: 數字
    :return: 兩參數相加的結果
    """
    print("into function_name")
    return param1 + param2


# 調用方法
print(function_name(9, 1))
print(type(function_name(9, 1)))

# 同名方法，後者蓋前者

print("============ 宣告方法，有無回傳值 ============")


def function_name2():
    return None  # 等同 pass


def function_name3():
    print("into function_name3")  # 回傳也是 None


print(function_name2())
print(type(function_name2()))
print(function_name3())
print(type(function_name3()))


def function_name3():
    print("into function_name333")


function_name3()  # 宣告了兩個名稱一樣的方法，呼叫時會往上找到最近的

print("============ 多個返回值 ============")


def multi_return():
    return 1, "a", True  # 回傳三個返回值


# 接收返回值時，有幾個回傳值就用就個變數接，否則執行期報錯；但用一個變數是例外，可以自動幫我們轉成 tuple
a = multi_return()
print(f"{a}, {type(a)}")
b, c, d = multi_return()
print(b, c, d)

print("============ 參數預設值 ============")


def display(num, name, price=5000):  # price 如呼叫時不給值，預設是 5000；但預設值都得放在最後面，也可以連續，但就是中間不能斷，否則編譯錯誤
    print(f"{num}, {name}, {price}")


display(1, "tiger", 8000)  # 按順序傳參
display(name="dragon", num=2)  # 按名稱傳參，此時順序可不依方法的順序

print("============ 預設值為可變的注意事項 ============")


def f(i, li=[]):  # 預設值為可變的，如 list、dict，會累加
    li.append(i)
    return li


print(f(10))
print(f(20))


# 不想累加可如下方式修改
def f(i, li=None):
    if li is None:
        li = []
    li.append(i)
    return li


print(f(10))
print(f(20))

print("============ 不定長參數 ============")


# 一個 * 等同 tuple；兩個 * 等同 dict
# 兩個可以一起使用，但 * 要在 ** 前面
# 兩種都表示 0~多個參數


def arbitrary_param(*num):
    print(type(num))
    count = 0
    for i in num:
        count += i
    return count


print(arbitrary_param(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(arbitrary_param(1, 2, 3))


def arbitrary_param(**num):
    print(type(num))
    print(num.keys(), type(num.keys))
    print(num.values(), type(num.values()))


arbitrary_param(k1=1, k2=2, k3=3)
print()
arbitrary_param(**{"k4": 4, "k5": 5})

print("============ 傳**關鍵字參數 ============")


def unpacking_argument(p1, p2=2, p3="ccc"):
    print(p1, p2, p3, end=" ")
    print()


d1 = {"p1": 1.23, "p2": 9}
d2 = {"p3": "ddd", "p2": 99}
unpacking_argument(**d1)
unpacking_argument("s", **d2)  # 不可傳 **d1，因為會有兩個 p1

print("============ 方法當參數傳遞 ============")


def fun_param(h):
    print(type(h))
    print(h())


def hi():
    return "hi"


def say_hi():
    return "say_hi"


fun_param(hi)
fun_param(say_hi)

print("============ 特殊參數 ============")


# /前：按位置傳參，可寫多個參數後再 /
# *後：按關鍵字傳參，*後可寫多個關鍵字
# 中間：按位置、關鍵字傳參都可以，/後*前可寫多個
# 使用位置傳參較好，若使用者使用關鍵字傳參，而在未來改變名稱時，使用者還的改；按位置傳參就沒這個問題

def standard_arg(arg):
    print(arg)


standard_arg(1)
standard_arg(arg=1)


def pos_only_arg(arg, /):
    print(arg)


# pos_only_arg(arg=1)  # 會報錯，因為 pos_only_arg 的 / 前面必須是按位置傳參
pos_only_arg(1)


def kwd_only_arg(*, arg):
    print(arg)


# kwd_only_arg(1)  # 會報錯，因為 kwd_only_arg 的 * 後面必須是按關鍵字傳參
kwd_only_arg(arg=1)


def combined(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


# combined(1, 2, 3)  # 前兩個參數沒問題，但第三個要傳 kwd_only 關鍵字
combined(1, 2, kwd_only=3)
combined(1, standard=2, kwd_only=3)
# combined(pos_only=1, standard=2, kwd_only=3)  # 第一個參數是按位置傳的

print("============ 特殊參數衝突 ============")


def conflict(name, **kwds):
    return 'name' in kwds


# print(conflict(1, **{'name': 2}))  # 有兩個 name

def conflicting(name, /, **kwds):  # 使用 / 解決衝突問題
    return 'name' in kwds


print(conflicting(1, **{'name': 2}))

print("============ recursive ============")


# 方法調用自己為 recursive (遞迴)


def my_recursive(i: int, count: int) -> int:
    if i <= 0:
        return count
    count += i
    i -= 1
    return my_recursive(i, count)  # 不寫 return 為 None


print(my_recursive(100, 0))

print("============ signature ============")
import inspect


def my_function(i: int, s: str) -> str:
    return str(i) + s


def xxx():
    pass


signature = inspect.signature(conflicting)  # 取得參數長什麼樣子
print(str(signature))  # (name, /, **kwds)
print(str(inspect.signature(my_function)))  # (i: int, s: str) -> str
print(str(inspect.signature(xxx)))  # ()
