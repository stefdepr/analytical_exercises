import numpy as np

#create array of random normal numbers mean 0 stdev 5
initial_array = np.array([[[3, 3],
                           [3, 3],
                           [3, 3]],

                          [[3, 3],
                           [3, 3],
                           [3, 3]]])

shape = initial_array.shape

arr = np.random.normal(loc=0, scale=1, size=shape)

arr_final = arr + initial_array

print(arr_final)