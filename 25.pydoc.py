print("============ help() ============")
# >>> help()

print("============ __doc__ ============")
i = 1
print(i.__doc__)
print("========================")
f = 1.1
print(f.__doc__)
print("========================")


class MyClass:
    """My class"""

    @staticmethod
    def __doc__():
        print("我的類別")


print(MyClass.__doc__)  # 沒實作會印出註解內容；有實作會印記憶體位址資訊
MyClass.__doc__()  # 沒實作會報錯

print("============ command line ============")
# python -m pydoc [module name | class name | function name]
# python -m pydoc math
# python -m pydoc
# -k 關鍵字
# -n 接 ip，然後隨機給我們一個沒在使用的 port 號
# -p 給一個 port 號
# -b 隨機給我們一個沒在使用的 port 號
# -w 產生文件
#
# python -m pydoc -k pygame
# 找到後，再針對其中一個搜尋
# python -m pydoc pygame.base
#
#
# python -m pydoc -n localhost -> b or q
# python -m pydoc -p 9999 -> b or q
# python -m pydoc -b -> b or q
# python -m pydoc -w tuple -> 在目前目錄下產生 tuple.html，然後用 open 或 start 打開
# python -m pydoc -w ./Pb.py -> Pb.py 是自己寫的
