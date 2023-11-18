def add(a, b):
    return a + b


# __name__ 這個檔案執行時，會是 __main__，如果是其他檔案 import 這個檔案會是「資料夾名.檔案名」，也就是 my_dir.my_module
if __name__ == "__main__":  # 有其人檔案 import 這個檔案後，會自動調用 add 方法，所以加上這個判斷，這樣別的檔案就不會執行這方法了
    print(add(9, 10))


def multiply(a, b):
    return a * b
