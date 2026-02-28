print("============ 查看內鍵方法 ============")
# 兩種方法一樣
print(dir(False))
print(False.__dir__())

print("============ iterable ============")
iterable = '__iter__'
print(iterable in dir(False))  # False
print(iterable in dir(1))  # False
print(iterable in dir(2.3))  # False
print(iterable in dir(""))  # True
print(iterable in dir([]))  # True
print(iterable in dir(()))  # True
print(iterable in dir({}))  # True
print(iterable in dir(set()))  # True
