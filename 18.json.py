import json

print("============ loads、dumps  ============")
# dumps：物件轉 str； loads：str 轉 list
data = [{"name": "孫悟空", "attack": 90}, {"name": "牛魔王", "attack": 85}, {"name": "如來佛", "attack": 1000}]
my_json = json.dumps(data)
print(f"{my_json}, {type(my_json)}")
my_json = json.dumps(data, ensure_ascii=False)
print(f"{my_json}, {type(my_json)}")

my_list = json.loads(my_json)
print(f"{my_list}, {type(my_list)}")
for x in my_list:
    print(f"{x}, {type(x)}")  # 已是 dict

# i = 0
# while i < len(my_list):
#     print(my_list[i])
#     i += 1

# x = '{"name": "孫悟空", "attack": 90}'  # 裡面雙引號，外面單引號才能轉成功
# my_dict = json.loads(x)
# print(f"{my_dict}, {type(my_dict)}\n")


print("============ load、dump ============")
# 使用在讀寫檔時

with open("read_json.txt", "r", encoding="UTF-8") as read_file:
    print(json.load(read_file))

with open("write_json.txt", "w", encoding="UTF-8") as write_file:  # 檔案不用先存在
    print(json.dump(["apple", "banana", "strawberry"], write_file))
