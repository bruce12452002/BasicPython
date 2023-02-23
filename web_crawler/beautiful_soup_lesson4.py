from bs4 import BeautifulSoup

html_str = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>我是標題</title>
</head>
<body>
  <p class="p1">
    <a href="http://www.google.com" class="a1">click me1</a>
    <span>
        <a href="http://tw.yahoo.com" class="a2">click me2</a>
    </span>
    <a href="http://www.ruten.com.tw" class="a3">click me3</a>
  </p>
  <p>
    <ul class="p2">
        <li> aaa
        <li> bbb
        <li> ccc
    </ul>
  </p>
</body>
</html>
""".replace("\n", "")

data = BeautifulSoup(markup=html_str, features="lxml")
a2 = data.select(".a2")  # css selector
print(type(a2), a2)

