def add(a, b):
    return a + b


# __name__ 這個檔案執行時，會是 __name__，如果是其他檔案 import 這個檔案會是「資料夾名.檔案名」，也就是 my_dir.my_module
if __name__ == "__main__":  # 有其人檔案 import 這個檔案後，會自動調用 add 方法，所以加上這個判斷，這樣別的檔案就不會執行這方法了
    print(add(9, 10))


def multiply(a, b):
    return a * b


# 其他檔案 from 資料夾(沒有.檔案名稱) import * 這個檔案時，會看有沒有 __all__，沒有就全部方法都不可以用；有的話就看裡面定義什麼方法，就只能用什麼方法
# 但 import 時，指明哪個方法還是可以用的
# __all__ = ["add"]
