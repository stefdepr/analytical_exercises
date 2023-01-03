import numpy as np

arr = np.array([3, -4, 5, 8, 2])

arr_exp = np.exp(arr)

sum_arr_exp = sum(arr_exp)

final_arr = arr_exp / sum_arr_exp

print(final_arr)