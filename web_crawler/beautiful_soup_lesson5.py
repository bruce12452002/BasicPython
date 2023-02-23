from bs4 import BeautifulSoup
import re

html_str = "<p><ul class='u1'><li>a</li></ul><a id='a1'>a1<p>p</p></a><a id='a2'>a2</a><a>a3</a><ul><li>a</li></ul></p>"

data = BeautifulSoup(markup=html_str, features="lxml")
print(data.find(name="a"))  # 只會查第一個
print(data.find_all(name="a"))
print(data.find_all(name=["a", "ul"]))
print(data.find_all(name="a", attrs={'id': 'a1'}))
print(data.find_all(name="a", id='a1'))
print(data.find_all(class_='u1'))  # class 是關鍵字，用 class_ 才能找 class
print(data.find_all(name="ul", attrs={'class': 'u1'}))  # 寫在 attrs 時，因為是字串，沒有關鍵字的問題，加底線反而查不到
print(data.find_all(name=re.compile('^ul')))
print(data.find_all('li', string='a'))  # tag 包起來的字串

print("============ 全抓 ============")
print(data.find_all(name=True, limit=5))  # 全抓，可用 limit 限制抓回來的數量
print(data.find_all(name=True, recursive=False))  # 不遞迴，相當於 limit=1

print("============ 其他方法 ============")
# data.findXxx，大同小異，差在取值範圍不同而已
