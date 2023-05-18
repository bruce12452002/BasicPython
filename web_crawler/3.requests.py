import requests as r

res = r.get("http://books.gotop.com.tw/default.aspx")
# res = r.get("https://baidu.com")
print(res.content)
# print(res.url)
# print(res.status_code)
# print(res.headers)
# res.encoding = 'UTF-8'
# print(res.text)
