import matplotlib.pyplot as plt

# 圓餅圖連結
# https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html#sphx-glr-gallery-pie-and-polar-charts-pie-features-py

plt.rc("font", family="DFBiaoKaiShu-B5")

# labeldistance 控製 label 顯示在哪，越小越接近圓心，0 就是圓心了
plt.pie([10, 25, 45], labels=['十五', '廿五', '四五'], labeldistance=0.2)
plt.legend()  # 顯示哪個顏色代表哪一個
plt.title('我是標題')
plt.show()
