import requests as req
from bs4 import BeautifulSoup

print("============ requests ============")
res = req.get("https://www.taiwanlottery.com.tw")
# print(res.status_code)
# print(res.text)

print("============ BeautifulSoup ============")
bs = BeautifulSoup(res.text, "lxml")

game_index = 3  # 0:威力彩  1:38樂合彩  2:大樂透  3:49樂合彩
power = bs.find_all('div', class_='contents_box02')
print('power==>', power)
title = power[game_index].find('span', class_='font_black15').text
print('title==>', title)

match game_index:
    case 0 | 1:
        color = 'ball_green'
    case 2 | 3:
        color = 'ball_yellow'
    case _:
        color = ''

datas = power[game_index].find_all('div', class_='ball_tx ' + color)
print('datas==>', datas)

for i in range(0, 6):
    print(datas[i].text, end=' ')
print()
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

if game_index == 0:
    print('第二區:', power[game_index].find('div', class_='ball_red').text)
elif game_index == 2:
    print('特別號:', power[game_index].find('div', class_='ball_red').text)
