import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)


import numpy as np
arr = np.array([3,4,5,6,7])
x = arr.copy()
arr[0] = 53
print(arr)
print(x)




import numpy as np
arr1 = np.array([10,20,30,40])
arr2 = arr1.copy()
arr1[0] = 99
print("original array:", arr1)
print("copied array:", arr2)




import numpy as np
arr1 = np.array([10,20,30,40])
arr2 = arr1.copy()
arr1[1] = 90
print("original array:", arr1)
print("copied array:", arr2)





import numpy as np
arr1 = np.array([20,30,40,40,50,60])
arr2 = arr1.copy()
arr1[3] = 100

print("original array:", arr1)
print("copied array:", arr2)


print(arr1 is arr2)
print(arr1.base is None)





import numpy as np
arr1 = np.array([10,20,30,40,50,60,70,80,90])
arr2 = arr1.copy()
arr1[5] = 100

print("original array:", arr1)
print("copied array:", arr2)



import numpy as np
arr1 = np.array([2,3,4,5,6])
arr2 = arr1.copy()
print("original array:", arr1)
print("copied array:", arr2)


print(arr1 is arr2)
print(arr1.base is None)