# r+ 可寫，在最後一行開始增加； r r+ 沒有檔案都「會」報錯
# a+ 可讀； a a+ 沒有檔案也「不會」報錯，但讀是從最後開始讀，可用 seek(0) 到最前面
# w+ 可讀； a a+ 沒有檔案也「不會」報錯
# w+ 無法讀舊的資料，只能讀自己寫過的
# 使用 w w+，就算什麼都不做，檔案也會被清空，因為很危險，所以可以改用下面的 x

# x 和 w 基本一樣，但如果檔案已存在就報錯
# x+ 和 w+ 基本一樣，但如果檔案已存在就報錯

# rwax 只能使用其中一種，預設是 r

# t 為 text，表示使用文字，b 為 binary，表示使用二進制，預設為 t
# b 可寫文字外，也可寫圖片、音樂等，速度也較文字快，但如果要處理文字，用 t 有較多方法可用
# 使用 b 時，不可用 encoding
# t b 只能使用其中一種，預設是 t
# 順序可換，如 +w 等同 w+ 也等同 tw+

# with open("test.txt", "ta+", encoding="UTF-8") as f:
#     # 有 + 可以讀，但不加這行，會從檔案最後開始讀，所以什麼都讀不到，可用 seek 到最前面讀
#     f.seek(0)  # 讀取第 2 個字元就是 seek(1)
#     print(f.read())
#     f.write('yeah')

print('====================')

# with open("test.txt", "w+", encoding="UTF-8") as f:
#     f.seek(0)
#     print('1', f.read())  # 讀不到，因為無法讀舊的資料
#     f.write('yeah')
#     print('2', f.read())  # 讀不到，因為指針已在檔案最後面
#     f.seek(0)
#     print('3', f.read())  # 這行才讀的到

with open("download\\2.png", "br") as r:
    with open("download\\2a.png", "bw") as w:
        w.write(r.read())
        w.flush()
