import urllib.request

import ssl

# ssl._create_default_https_context = ssl._create_unverified_context # https

url = "https://baidu.com"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

req = urllib.request.Request(url=url, headers=header)

res = urllib.request.urlopen(req, context=ssl._create_unverified_context())

print(res.read().decode("UTF-8"))
