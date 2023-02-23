# https://beautiful-soup-4.readthedocs.io/en/latest
# Xpath 和 Beautiful Soup 都可提取資料，但 Xpath 不能修改文件的資料
# Beautiful Soup 前3版已停止開發
# Beautiful Soup 解析器
# lxml 支持 解析 html xml
# html5lib 速度慢，但容錯率最好

# 1. BeautifulSoup("")  放 html 字串
# 2. BeautifulSoup(open(xxx.html))  使用 open 將 html 檔案放入參數
# 3. BeautifulSoup("", "lxml")  使用 lxml 解析器解析 html

from bs4 import BeautifulSoup

print("============ 解析 ============")
print(BeautifulSoup("<a></a>", "html.parser"))  # <a></a>，python 內鍵解析
print(BeautifulSoup("<a></a>", "lxml"))  # <html><body><a></a></body></html>
print(BeautifulSoup("<a></a>", "html5lib"))  # <html><head></head><body><a></a></body></html>

html_str = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>我是標題</title>
</head>
<body>
  <h1>超大字1</h1>
  <h1>超大字2</h1>
</body>
</html>
"""

print("============ 取得 tag ============")
data = BeautifulSoup(markup=html_str, features="lxml")
print(data.title, type(data.title))
print(data.h1, data.h1.string)  # 只會取得第一次
print(data.body.h1)
print(data.a)
print(data.getText())
