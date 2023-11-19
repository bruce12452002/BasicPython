def outer():
    a = 2

    def do_nonlocal():
        # a = 6 # nonlocal 宣告的變數不能在之前宣告
        nonlocal a  # nonlocal 之前的層級就必須宣告變數，但不包括 global
        print("do_nonlocal1", a)
        a = 4
        print("do_nonlocal2", a)

        def sub_do_nonlocal():
            nonlocal a  # 不會找自己的變數，往外一直找，但不會找 global
            print("sub_do_nonlocal", a)

        sub_do_nonlocal()

    do_nonlocal()


a = 1
outer()
print("最外層a =", a)
