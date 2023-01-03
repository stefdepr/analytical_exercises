import numpy as np
import random

x = np.arange(100)

error = np.random.normal(loc=0, scale=30, size=(100,))

intercept = 10

coef = 3

y = intercept + coef * x + error

print(y)