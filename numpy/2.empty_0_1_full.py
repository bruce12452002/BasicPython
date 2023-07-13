import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2], [3, 4]])

print("============ empty、empty_like，產生陣列的隨機值 ============")
print(np.empty(5))  # 一維陣列裡有 5 個值，值是隨機的
print(np.empty((2, 3), dtype=float))  # 兩橫三直，每一橫條有 3 個值，值是隨機的

print(np.empty_like(arr1))  # 將 x 維陣列的內容變成隨機值
print(np.empty_like(arr2))  # 將 x 維陣列的內容變成隨機值

print("============ zeros、zeros_like，陣列裡的元素都是 0 ============")
print(np.zeros(5))  # 一維陣列裡有 5 個 0
print(np.zeros((2, 3), dtype=float))  # 兩橫三直，每一橫條有 3 個 0

print(np.zeros_like(arr1))  # 將 x 維陣列的內容變成 0
print(np.zeros_like(arr2))  # 將 x 維陣列的內容變成 0

print("============ ones、ones_like，陣列裡的元素都是 1 ============")
print(np.ones(5))  # 一維陣列裡有 5 個 1
print(np.ones((2, 3), dtype=float))  # 兩橫三直，每一橫條有 3 個 1

print(np.ones_like(arr1))  # 將 x 維陣列的內容變成 1
print(np.ones_like(arr2))  # 將 x 維陣列的內容變成 1

print("============ full、full_like，陣列裡的元素都是指定的值 ============")
print(np.full(5, -1))  # 一維陣列裡有 5 個 -1
print(np.full((2, 3), -1, dtype=int))  # 兩橫三直，每一橫條有 3 個 -1

print(np.full_like(arr1, -1))  # 將 x 維陣列的內容變成 -1
print(np.full_like(arr2, -1))  # 將 x 維陣列的內容變成 -1
