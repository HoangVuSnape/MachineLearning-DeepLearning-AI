#slicing, view, copy, shape, reshape
import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# arr = np.array([1,2,3])

# difference between copy and view - 
# copy when you change copy it not affect original array
# view thì khác.

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr) # 
print(x)

print(arr[1:5])
## copy

arr1 = np.array([1, 2, 3, 4, 5])
x = arr1.copy()
arr1[0] = 42

print(arr1)
print(x)

# shape.
# cot nay dong.


a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(a.shape)

print(len(a)) # number of row
print(len(a[1])) # of column

# reshape
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newshape = arr.reshape(4, 3)

print(newshape)