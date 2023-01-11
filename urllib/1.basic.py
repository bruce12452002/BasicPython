import urllib.request
import ssl

# ssl._create_default_https_context = ssl._create_unverified_context # https

res = urllib.request.urlopen("http://baidu.com")
print(res.read().decode("UTF-8"))

# res.read()
# res.read(5)
# res.readline()
# res.readlines()
# res.getcode()
# res.geturl()
# res.getheaders()


# download 影片、圖片
urllib.request.urlretrieve(url="", filename="xxx.jpg")

