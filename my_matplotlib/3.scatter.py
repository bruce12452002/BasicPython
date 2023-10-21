import matplotlib.pyplot as plt

# 官網連結
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html

plt.rc("font", family="DFBiaoKaiShu-B5")

'''
一筆資料
(1,3)(2,6)(3,9)(6,2)(3,1)
'''
# plt.scatter([1, 2, 3, 6, 3], [3, 6, 9, 2, 1], c="red", s=50)
# plt.show()

'''
兩筆資料
(1,3)(2,6)(3,9)(6,2)(3,1)
(5,2)(4,4)(3,6)(2,8)(4,4)
'''
plt.scatter([1, 2, 3, 6, 3], [3, 6, 9, 2, 1], c="red", s=50, label="xxx")
plt.scatter([5, 4, 3, 2, 4], [2, 4, 6, 8, 7], c="blue", s=10, label="ooo")
plt.legend()  # 顯示哪個顏色代表哪一個
plt.xlabel("左右的標籤")
plt.ylabel("上下的標籤")
plt.title('我是標題')
plt.show()
