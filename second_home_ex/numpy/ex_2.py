import numpy as np
import random


arr_1 = np.reshape(np.arange(4000), (20, 200))
arr_2 = np.zeros(shape=(4, 5))

print(arr_1)
print(arr_2)

random_matrix = arr_1[np.random.randint(arr_1.shape[0], size=(2, 5))]
print(random_matrix)

final_arr = np.concatenate([arr_2, random_matrix], axis=0)

print(final_arr)