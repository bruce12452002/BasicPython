print("============ 一個例外 ============")
try:
    file = open("xxx.txt")
    raise TypeError
# except:  # 所有例外都捕獲
except Exception as e:
    print("哇！")

try:
    1 / 0
except ZeroDivisionError as ex:  # 沒捕獲到會發生錯誤
    print(ex)

print("============ 多個例外 ============")

try:
    add + 1
    1 / 0
except ZeroDivisionError as ex:
    print(1, ex)
except NameError as ex:
    print(2, ex)

print("============ 多個例外合併成一個 ============")
try:
    add + 1
    # 1 / 0
except (ZeroDivisionError, NameError) as ex:
    print(ex)

print("============ 正常結束 else ============")
try:
    # print("xx")
    1 / 0
except ZeroDivisionError as ex:
    print(ex)
else:
    print("finish")  # 沒例外才會執行

print("============ 都會執行的 finally ============")
try:
    print("xx")
    # 1 / 0
except ZeroDivisionError as ex:
    print(ex)
else:
    print("finish")  # 沒例外才會執行
finally:
    print("不管怎樣都會執行")

print("============ return 和 finally ============")


# 有了 return，else 將不起作用
# 如果沒例外：finally 執行完，然後 return
# 如果有例外：except -> finally，然後 return None

def test() -> int:
    try:
        print("xx")
        1 / 0
        return 888
    except ZeroDivisionError as ex:
        print(ex)
    else:
        print("finish")  # 沒例外才會執行
    finally:
        print("不管怎樣都會執行")


print(test())

print("============ 捕獲多個異常 ============")
'''
    except*，*一加，所有的 except 都得加
    只要其中一個例外沒捕獲到就會報錯
'''


def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('there were problems', excs)

    # raise ExceptionGroup("group1",
    #                      [OSError(1),
    #                       SystemError(2),
    #                       ExceptionGroup("group2",
    #                                      [OSError(3), RecursionError(4)])])


try:
    f()
except* OSError as e:
    print("OSErrors OSErrors")
except* SystemError as e:
    print("SystemErrors SystemErrors")
# except* Exception as e:
#     print(e)
