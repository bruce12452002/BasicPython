print("============ 宣告 lambda(匿名方法) ============")
# 語法 lambda 參數(沒參數可不寫):方法體(只能寫一行)，
my_lambda = lambda x, y: x * y

print(my_lambda(5, 6))
print((lambda x, y: x * y)(5, 6))  # lambda 不加圓括號會是記憶體位址


def my_lambda(x, y):
    return (lambda x1, y1: x1 * y1)(x, y)


print(my_lambda(5, 6))

print("============ lambda 也可用特殊參數 ============")
lam = lambda p, /, s="str", *, k="123": print(p + 1)
lam(10)

print("============ 傳 lambda ============")


def fun_param(h):
    print(h())


fun_param(lambda: "I'm lambda")  # 傳一般方法也是可以的


def fun_param2(h):
    print(type(h))
    result = h(x=0, y=0)  # x、y 名稱必須和傳進來的 lambda 參數名稱一樣
    print(result)


fun_param2(lambda x, y: 3 + 4)


def fun_param2_plam(x, y):
    return 7 + 9


fun_param2(fun_param2_plam)


def fun_param3(h):
    result = h(3, 4)  # 相當於 fun_param2 寫 result = h(x=3, y=4)
    print(result)


fun_param3(lambda x, y: x + y)
fun_param3(lambda x, y: 7 + 8)  # 將預設值改掉


def fun_param3_plam(x, y):
    return x + y


fun_param3(fun_param3_plam)

print("============ 回傳 lambda ============")
""" 
    累加 lambda 
"""


def fun_param4(h):  # 回傳一個匿名方法
    return lambda x: x + h


fun = fun_param4(100)
print(fun(20))  # 120
print(fun(500))  # 600

fun_param5 = lambda h: lambda x: x + h  # fun_param4 方法再精簡
fx = fun_param5(5)
print(fx(6))
print(fx(7))
print(fun_param5(5)(8))

print("============ lambda 應用 ============")
odd_or_even = lambda x: "odd" if x % 2 == 0 else "even"
print(odd_or_even(20))
print(odd_or_even(-11))

my_list = [56, 8, 11, 4, 99, 20]

print(list(filter(lambda n: n > 20, my_list)))  # 過濾
print(list(map(lambda n: n // 2, my_list)))  # 映射

from functools import reduce

print(reduce(lambda i, j: i + j, my_list))  # 合併成一個
print(sorted(my_list, key=lambda i: i, reverse=True))  # 排序
