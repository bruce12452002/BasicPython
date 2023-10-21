import matplotlib.pyplot as plt
from matplotlib import font_manager

# 官網連結
# https://matplotlib.org/stable/gallery/index.html

# 折線圖連結
# https://matplotlib.org/stable/gallery/text_labels_and_annotations/titles_demo.html#sphx-glr-gallery-text-labels-and-annotations-titles-demo-py

# for font in font_manager.fontManager.ttflist:
#     # 所有字體名稱和字體的路徑，字體路徑有中文的就有支援中文
#     print(font.name, "=", font.fname)

plt.rc("font", family="DFBiaoKaiShu-B5")

'''
一筆資料
(1,3)(2,6)(3,9)(4,12)(5,15)
'''
# plt.plot([1, 2, 3, 4, 5], [3, 6, 9, 12, 15])

'''
兩筆資料
(1,3)(2,6)(3,9)(4,12)(5,15)
(1,2)(2,4)(3,6)(4,8)(5,10)
'''
plt.plot([1, 2, 3, 4, 5], [[3, 2], [6, 4], [9, 6], [12, 8], [15, 10]], label=["第一筆", "第二筆"])
plt.legend()  # 顯示哪個顏色代表哪一個
plt.xlabel("左右的標籤")
plt.ylabel("上下的標籤")
plt.title('我是標題')
plt.show()
