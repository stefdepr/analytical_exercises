import numpy as np

arr_1 = np.random.normal(loc=0, scale=1, size=(2, 4))
arr_2 = np.random.normal(loc=3, scale=10, size=(4, 5))

matrix_multiplication = np.dot(arr_1, arr_2)
print(np.sum(matrix_multiplication, axis=1))