from bs4 import BeautifulSoup

data = BeautifulSoup(open("sample.html"), "lxml")
print(data.a, type(data.a))
print(data.a.name, type(data.a.name))  # 取得 tag 名稱
print(data.a.string)  # 取得前後 tag 包住的字串
print(data.a.attrs, type(data.a.attrs))
for k, v in data.a.attrs.items():
    print(k, end=" ")
    if isinstance(v, list):
        for vs in v:
            print(vs, end=", ")
    else:
        print(v, end="")
    print()
