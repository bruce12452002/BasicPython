import numpy as np

# https://numpy.org
print(np.__version__)

print("============ 零一維陣列 ============")
arr0 = np.array("aa")  # 一個元素的陣列，多個元素要用 list tuple set
print(arr0, type(arr0))

arr1 = np.array({1, 2, 3, 4, 5})
print(arr1, type(arr1))

arr2 = np.array([1, 2, 3, 4, 5])
print(arr2, type(arr2))

arr3 = np.array((1, 2, 3, 4, 5))
print(arr3, type(arr3))

# 檢查幾維陣列，一個元素和 set 算 0 維，set 只能用在 0 維
print(arr0.ndim, arr1.ndim, arr2.ndim, arr3.ndim)

# 顯示陣列是幾乘幾的
print(arr0.shape, arr1.shape, arr2.shape, arr3.shape)

# 檢查陣列裡有幾個元素
print(arr0.size, arr1.size, arr2.size, arr3.size)

# 元素的型態是什
print(arr0.dtype, arr1.dtype, arr2.dtype, arr3.dtype)

print("============ 零一維陣列取值 ============")
# 零維不可用方括號，會報錯
# 方括號支援負的
print(arr0)
print(arr1)
print(arr2, arr2[0], arr2[2], arr2[-1])
print(arr3, arr3[0], arr3[1], arr3[-2])

print("============ 多維陣列 ============")
# 長寬高必需一樣才行
arr_two = np.array([[1, 2], [3, 4]])
print(arr_two, type(arr_two))
arr_three = np.array([
    [
        [1, 2, 3], [4, 5, 6]
    ],
    [
        [7, 8, 9], ["a", True, 1]
     ]
])
print(arr_three, type(arr_three))
print(arr_two.ndim, arr_two.shape, arr_two.size, arr_two.dtype)
print(arr_three.ndim, arr_three.shape, arr_three.size, arr_three.dtype)

print("============ 多維陣列取值 ============")
# [0][1] 和 [0, 1] 是一樣的
print(arr_two, arr_two[1], arr_two[0][1], arr_two[0, 1], sep="--")
print()
print(arr_three, arr_three[0], arr_three[0][1], arr_three[0][1][1], sep="--")
print()
print(arr_three, arr_three[0], arr_three[0, 1], arr_three[0, 1, 1], sep="--")
print()

print("============ slice ============")
# 基本上和 slice 一樣，看 13 章，這裡寫 slice 沒有的功能
# slice 時的長度，以後面的為主，前面的會自動延伸
two = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(two[1, 1:3])  # 第一個元素的 1 和 2 元素
print(two[0:2, 1:3])  # 第零和一元素的 1 和 2 元素
print(two[..., 1], two[..., 1:])  # 元素的 1 元素； 元素的 1之後的元素
print(two[1, ...], two[1:, ...])  # 第一個元素的所有元素； 第一個元素的之後的元素的所有元素
print(two[1, 1:4])
print(two[1:, 4:])
print(two[0:, 4:])  # ... 等同 0:

print("============ 設定多維陣列 ============")
# # 1 維以下，包括負的，都算1維
print(np.array([1, 2], ndmin=1))
print(np.array([1, 2], ndmin=2))
print(np.array([1, 2], ndmin=3))

xxx = np.array([1, 2], ndmin=3)
print(xxx[0], xxx[0][0], xxx[0][0][0])

print("============ arange ============")
a = np.arange(5)  # 0~4
print(a, type(a))
print(np.sqrt(a))

# arrange 用法和 range 一樣
print(np.arange(1, 5))  # 1~4
print(np.arange(1, 5, 2))  # 1 3
