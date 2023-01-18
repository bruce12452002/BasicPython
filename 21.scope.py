# 變數範圍以找最近的變數為主，沒有就往上找，不會往下找
# global：在最外層設定或取得變數
# nonlocal：從本層到最外層，將變數傳播在中間層，也就是沒有本層和最外層
#

def outer():
    a = 2

    def inner():
        # a = 3
        print("inner", a)  # 最接近自己的先找，一直找到 global，但不能改值

    def do_nonlocal():
        # nonlocal a
        # print("do_nonlocal", a)
        a = 4

        def sub_do_nonlocal():
            nonlocal a  # 不會找自己的變數，往外一直找，但不會找 global
            print("sub_do_nonlocal", a)

        sub_do_nonlocal()

    def do_global():
        global a
        a = 5

    inner()
    do_nonlocal()
    print("outer", a)


a = 1
outer()
print("最外層a=", a)
