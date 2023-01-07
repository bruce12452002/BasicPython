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
from typing import Union, Tuple

my_tuple2: tuple[int, str, str, int] = (1, "xx", "oo", 89)
my_tuple3: Union = (1, "xx", "oo", 89)
my_tuple4: Union[tuple] = (1, "xx", "oo", 89)
my_tuple5: Union[tuple[int, str, str, int]] = (1, "xx", "oo", 89)
my_tuple6: Union[tuple[int | str]] = (1, "xx", "oo", 89)

print(my_tuple2)


def ooo(x: list[Union[str, int]]) -> Union[tuple[str, int]]:
    print(ooo.__annotations__)
    return "xxx", 1


ooo([])
