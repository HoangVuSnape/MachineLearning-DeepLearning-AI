import numpy as np 

A = np.array([
[12, 15, 10, 16, 12],
[5, 9, 14, 7, 10],
[8, 12, 10 , 9, 15]
])

A1 = A.T

price = np.array([
[2], [1], [3]
])

print("result = ", np.matmul(A1, price))