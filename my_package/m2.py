def module2():
    print("module2")


def module4():
    print("module4")


# __all__，只有在使用 from my_package import * 才會有影響
__all__ = ['module2']  # 只可使用哪個模組或方法
