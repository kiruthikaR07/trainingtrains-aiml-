import numpy as np

a = [9,3,3,5]

arr = np.array(a)

print(arr)
print(arr[0])
print(arr[1:3])
print(arr.sum())
print(arr.mean())
print(arr.max())
print(arr.min())
A = np.array([
    [1,2],
    [3,4]
])

print(A)
print(np.dot(A,A))
import numpy as np

b = np.random.normal(0,1,5)

print(b)
c = np.arange(10)

print(c*5)