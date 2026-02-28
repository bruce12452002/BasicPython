print("============ 淺複製 ============")
# 淺複製：新的變數修改值時(非一般的等號賦值)，會影響舊的變數值
# 一般的等號賦值是將記憶體指向到新的空間，所以位址和原來是不同的
# 但二維陣列(含)以上的 = 只要父項在，位址就不會改變，所以淺複製會影響原來的
# 如 x[0][1]，x[0] 是父項，修改 x[0][number]時，淺複製會影響原來的
data = [[False, 1, 2.3, "4", [5, 6], (7, 8), {9, 10}, {"k": 11}]]
copy_list = data.copy()  # 等同 copy_list = my_list，當然等號右邊改成 my_list[:] 也是一樣

print("============ 淺複製測 bool ============")
print(copy_list[0][0] is data[0][0])
copy_list[0][0] = True
print(f"{data[0][0]}, {copy_list[0][0]}")
print(copy_list[0][0] is data[0][0], copy_list is data)

print("============ 淺複製測 int ============")
print(copy_list[0][1] is data[0][1])
copy_list[0][1] = 2
print(f"{data[0][1]}, {copy_list[0][1]}")
print(copy_list[0][1] is data[0][1], copy_list is data)

print("============ 淺複製測 float ============")
print(copy_list[0][2] is data[0][2])
copy_list[0][2] = 77.5
print(f"{data[0][2]}, {copy_list[0][2]}")
print(copy_list[0][2] is data[0][2], copy_list is data)

print("============ 淺複製測 str ============")
print(copy_list[0][3] is data[0][3])
copy_list[0][3] = "8"
print(f"{data[0][3]}, {copy_list[0][3]}")
print(copy_list[0][3] is data[0][3], copy_list is data)

print("============ 淺複製測 list ============")
print(copy_list[0][4] is data[0][4])
copy_list[0][4][0] = 3
print(f"{data[0][4]}, {copy_list[0][4]}")
print(copy_list[0][4] is data[0][4], copy_list is data)

print("============ 淺複製測 tuple ============")
# tuple 原本就不能修改

print("============ 淺複製測 set ============")
print(copy_list[0][6] is data[0][6])
copy_list[0][6].add(99)
print(f"{data[0][6]}, {copy_list[0][6]}")
print(copy_list[0][6] is data[0][6], copy_list is data)

print("============ 淺複製測 dict ============")
print(copy_list[0][7] is data[0][7])
copy_list[0][7] = {"k1": 999}
print(f"{data[0][7]}, {copy_list[0][7]}")
print(copy_list[0][7] is data[0][7], copy_list is data)

print("============ 深複製 ============")
# 深複製：完全複製一個新的
import copy

# 記憶體位址再複製時就不一樣了
deep_clone = copy.deepcopy(data)

print("============ 深複製測 bool ============")
print(deep_clone[0][0] is data[0][0])
print(f"原本兩個是 {data[0][0]}, {deep_clone[0][0]}")
deep_clone[0][0] = False
print(f"修改後是 {data[0][0]}, {deep_clone[0][0]}")
print(deep_clone[0][0] is data[0][0], deep_clone is data)

print("============ 深複製測 int ============")
print(deep_clone[0][1] is data[0][1])
print(f"原本兩個是 {data[0][1]}, {deep_clone[0][1]}")
deep_clone[0][1] = 20
print(f"修改後是 {data[0][1]}, {deep_clone[0][1]}")
print(deep_clone[0][1] is data[0][1], deep_clone is data)

print("============ 深複製測 float ============")
print(deep_clone[0][2] is data[0][2])
print(f"原本兩個是 {data[0][2]}, {deep_clone[0][2]}")
deep_clone[0][2] = 90.5
print(f"修改後是 {data[0][2]}, {deep_clone[0][2]}")
print(deep_clone[0][2] is data[0][2], deep_clone is data)

print("============ 深複製測 str ============")
print(deep_clone[0][3] is data[0][3])
print(f"原本兩個是 {data[0][3]}, {deep_clone[0][3]}")
deep_clone[0][3] = "88"
print(f"修改後是 {data[0][3]}, {deep_clone[0][3]}")
print(deep_clone[0][3] is data[0][3], deep_clone is data)

print("============ 深複製測 list ============")
print(deep_clone[0][4] is data[0][4])
print(f"原本兩個是 {data[0][4]}, {deep_clone[0][4]}")
deep_clone[0][4][0] = 51
print(f"修改後是 {data[0][4]}, {deep_clone[0][4]}")
print(deep_clone[0][4] is data[0][4], deep_clone is data)

print("============ 深複製測 tuple ============")
# tuple 原本就不能修改

print("============ 深複製測 set ============")
print(deep_clone[0][6] is data[0][6])
print(f"原本兩個是 {data[0][6]}, {deep_clone[0][6]}")
deep_clone[0][6].add(88)
print(f"修改後是 {data[0][6]}, {deep_clone[0][6]}")
print(deep_clone[0][6] is data[0][6], deep_clone is data)

print("============ 深複製測 dict ============")
print(deep_clone[0][7] is data[0][7])
print(f"原本兩個是 {data[0][7]}, {deep_clone[0][7]}")
deep_clone[0][7] = {"k2": 777}
print(f"修改後是 {data[0][7]}, {deep_clone[0][7]}")
print(deep_clone[0][7] is data[0][7], deep_clone is data)

print("============ dict ============")
# dict 的 value，仍然是淺複製
my_dict = {"xxx": [1, 2, 3]}
clone_dict = my_dict.copy()
clone_dict.setdefault("a")
print(my_dict, clone_dict)
my_dict.get("xxx").append(4)
print(my_dict, clone_dict)
