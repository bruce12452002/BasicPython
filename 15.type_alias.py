# 都只是別名而已，方便開發工具提示，值亂給是不會報錯的

a: int = 1
b: float = 2.2
c: str = "haha"
d: bool = False
my_list1: list = ["a", "b", "c"]
my_list2: list[str] = ["a", "b", "c"]
my_tuple: tuple[int, bool, str] = (1, True, "xx")
my_dict: dict[int, str] = {1: "a"}


def xxx(x: str, o: int) -> str:  # -> 為回傳值的alias
    print(xxx.__annotations__)  # 如果有別名會印出別名資訊
    return "xxx"


xxx("", 0)

print("============ 聯合別名 ============")
# 參數或回傳值，如果想定義多個型態，可用 Union
# 表示參數或回傳值可以是什麼型態或什麼型態
from typing import Union

my_tuple2: tuple[int, str, str, int] = (1, "xx", "oo", 89)
my_tuple3: Union = (1, "xx", "oo", 89)
my_tuple4: Union[tuple] = (1, "xx", "oo", 89)
my_tuple5: Union[tuple[int, str, str, int]] = (1, "xx", "oo", 89)

print(my_tuple2)


def yyy(x: int or str) -> str or int:
    return 1.5


# 回傳值的 Union 有警告
def zzz(x: Union[int, str]) -> Union[str, int]:
    return 1.5


# 調用方法時不會警告
yyy(False)
zzz(False)
