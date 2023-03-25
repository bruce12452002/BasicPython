class MyEnc:
    a = 0
    _a = 1
    __a = 2

m = MyEnc()
print(m.a)
print(m._a)
print(m.__a)