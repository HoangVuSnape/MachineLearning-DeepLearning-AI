import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a)
# check number of dimension
print(a.ndim)

#index
print(a[1][0] + a[0][1]) # 4+ 6

print('2nd element on 1st row: ', a[0, 1])

b = np.array([22, 26, 28, 10, 1, 2, 3])
print("\n")
print(b[:])
print(b[:2]) # 22 26 - bỏ số address cuối đi

print(b[-3:-1]) # 3 : -1 , 2: -2, 1 : -3

print(b[1:6:2]) 
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2])

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

#subtract 
newarr = np.subtract(arr1, arr2) #minus
#product
newarr = np.multiply(arr1, arr2) #product

#sort
arr = np.array([3, 2, 0, 1])

print(np.sort(arr))

#search = value equal 4
arr = np.array([1, 2, 4, 5,66, 44])
x = np.where(arr == 4)
print(x)

#find index if x mod 2 == 1 
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 1)
print(x)
