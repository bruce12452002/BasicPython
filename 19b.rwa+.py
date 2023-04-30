# r+ 可寫，在最後一行開始增加； r r+ 沒有檔案都「會」報錯
# a+ 可讀； a a+ 沒有檔案都「不會」報錯
# w+ 可讀； a a+ 沒有檔案都「不會」報錯
# w+ 無法讀舊的資料，只能讀自己寫過的
# 使用 w w+，就算什麼都不做，檔案也會被清空

# x 和 w 基本一樣，但如果檔案已存在就報錯
# x+ 和 w+ 基本一樣，但如果檔案已存在就報錯

with open("test.txt", "a+", encoding="UTF-8") as f:
    # 有 + 可以讀，但不加這行，會從檔案最後開始讀，所以什麼都讀不到，可用 seek 到最前面讀
    f.seek(0)  # 讀取第 2 個字元就是 seek(1)
    print(f.read())
    f.write('yeah')

print('====================')

# with open("test.txt", "w+", encoding="UTF-8") as f:
#     f.seek(0)
#     print('1', f.read())  # 讀不到，因為無法讀舊的資料
#     f.write('yeah')
#     print('2', f.read())  # 讀不到，因為指針已在檔案最後面
#     f.seek(0)
#     print('3', f.read())  # 這行才讀的到
