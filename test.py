import numpy as np
import os
# def cutting_window_2D(a, n):
#     # a: 2D Input array
#     # n: Group/sliding window length
#     split_positions = list(range(n, a.shape[0], n))
#     split_result = np.array_split(a, split_positions)
#     np_result = []
#     if split_result[-1].shape[0] == split_result[-2].shape[0]:
#         for array in split_result[:-1]:
#             np_result.append(array)
#     else:
#         for array in split_result[:-1]:
#             np_result.append(array)
#     return np.stack(np_result)

# a = np.random.randint(low=1,high=100,size=(100,1))
# print(a)
# n=4
# print(cutting_window_2D(a,4))
for root, dirs, files in os.walk('./data/AIOPS'):
    print(root,files,dirs)