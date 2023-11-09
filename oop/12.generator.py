a = [i ** 2 for i in range(10)]
b = (i ** 2 for i in range(10))
print(type(a), type(b))
for i in b:
    print(i, end=' ')  # 0 1 4 9 16 25 36 49 64 81
for i in b:
    print(i, end=' ')  # 只能跑一次，所以這個迴圈沒跑

print("============ next 取值 ============")
b = (i ** 2 for i in range(10))
# 每次跑一個值，如果想全跑，可用迴圈
print(next(b))  # 0
print(next(b))  # 1
print(next(b))  # 4

print("============ yield 寫在方法裡 ============")


def f():
    yield 1  # 使用 yield
    yield 2
    yield 3


g = f()  # 賦值給變數 g
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3
# print(next(g))  # 報錯

print(next(f()))  # 1
print(next(f()))  # 1
print(next(f()))  # 1
