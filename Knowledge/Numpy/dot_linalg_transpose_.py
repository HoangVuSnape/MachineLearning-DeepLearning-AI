#vs dot - linalg - transpose 
# product of 2 number, 
# - dinh thuc
import numpy as np  
a = np.dot(6,12)  
print(a)

#vi du 1 - tich cua 2-D voi 2-D
import numpy as np 
a = np.array([[1, 0],
              [0, 1]])
b = np.array([[4, 1],
              [2, 2]])

print(np.matmul(a, b))

#vi du 1 - tinh dinh thuc 2-D
import numpy as np 
arr1 = np.array([[1, 2], [3, 4]])
 
print(np.linalg.det(arr1))
#transpose
v1 = [1, 2, 3, 4]
v2 = [-1, 0, 1, 3]
v3 = [0, -5, 6, 8]
w = [3, -6, 17, 11]

A = np.transpose( [v1, v2, v3] ) # reverse row to column

# 
A = np.array([
[1, 2, 1],
[2, -1, 1],
[2, 1, 0]
])
b = np.transpose([0, 0, 0])
X = np.linalg.solve(A, b)
print("vd1: X = ", X)

