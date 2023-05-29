import requests as req
from bs4 import BeautifulSoup

print("============ requests ============")
res = req.get("https://www.taiwanlottery.com.tw")
# print(res.status_code)
# print(res.text)

print("============ BeautifulSoup ============")
bs = BeautifulSoup(res.text, "lxml")

power = bs.find('div', class_='contents_box02')
print('power==>', power)
title = power.find('span', class_='font_black15').text
print('title==>', title)

datas = power.find_all('div', class_='ball_tx ball_green')
print('datas==>', datas)

for i in range(0, 6):
    print(datas[i].text, end=' ')
for i in range(6, 12):
    print(datas[i].text, end=' ')
print('==========')
# machine_order_list = []  # 開出順序
# asc_order_list = []  # 小到大順序
# for i in datas:
#     # print(i.text, end=" ")
#     if len(machine_order_list) < 6:
#         machine_order_list.append(int(i.text))
#     else:
#         asc_order_list.append(int(i.text))
# print(machine_order_list)
# print(asc_order_list)

print('第二區:', power.find('div', class_='ball_red').text)
