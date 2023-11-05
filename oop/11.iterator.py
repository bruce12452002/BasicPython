# for-in 的設計
# 1.實作 __iter__ 表示自己是 iterable
# 2.實作 __next__ 每次迴圈都會執行，結束時給一個 StopIteration

class Display:
    """設計 iterator"""

    def __init__(self, data: str) -> None:
        self.data = data
        self.i = 0

    def __iter__(self) -> 'Display':
        print("進入 __iter__")
        return self

    def __next__(self) -> str:
        print("進入 __next__")
        if self.i == len(self.data):
            raise StopIteration

        rtn = self.data[self.i]
        self.i += 1
        return rtn


d = Display("abc")
print(iter(d))

for s in d:
    print(s)

print("============ for-range 沒有用到 Display 類別 ============")
d2 = "abc"
for i in range(len(d2)):
    print(d2[i])
