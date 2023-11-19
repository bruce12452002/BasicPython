def outer():
    a = 2

    def do_global():
        global a
        a = 5

    do_global()


a = 1
outer()
print("最外層a =", a)
