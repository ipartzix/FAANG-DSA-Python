# #Create an array and print all elements
# from array import array
# import numpy as np
# data_list: list[int] = [2, 4, 5, 67, 889, 9, 9, "hello ", True, 3.4, -12]
# data_array: array = array('i', [1, 2, 3, 4, 5])
# data_np: np.ndarray = np.array([1, 2, 3, 4, 5], dtype=np.int32)
# print(data_array)
# print(data_np)
# print(data_list)
# Create an array and print all elements

from array import array

arr = array('i', [2, 4, 5, 67, 889, 9])  # 'i' → integer array

for element in arr:
    print(element)