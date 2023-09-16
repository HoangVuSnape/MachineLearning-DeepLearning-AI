# for, concatentate # random, arange

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)
    
#concatetate
x = np.array([[1,2],[3,4]])  
y = np.array([[12,30]])  
z = np.concatenate((x,y))  
print(z)

# 
a=np.random.rand(5,2)  
print(a)

a=np.random.randint(44, size=10)  
print(a)

#arange
print(np.arange(1,6))
f_n_c = lambda n: n ** 3
x_n_c = list( map(f_n_c, np.arange(1, 6)) )
print(x_n_c)
