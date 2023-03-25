from oom.test_encapsulate import MyEnc


class MyEnc2(MyEnc):
    pass

m = MyEnc2()
print(m.a)
print(m._a)
print(m.__a)
