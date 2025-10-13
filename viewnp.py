import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)



import numpy as np
arr = np.array([10,20,30,40,50,60,70])
x = arr.view()
arr[3] = 44
print(arr)
print(x)



import numpy as np
arr1 = np.array([10,20,30,40,50])
arr2 = arr1.view()
arr1[0] = 455
print("original array:", arr1)
print("view array:", arr2)




import numpy as np
arr1 = np.array([1,2,3,4,5,6,7])
arr2 = arr1.view()
arr1[4] = 60

print("original array:", arr1)
print("view array:", arr2)


# check 

print(arr1 is arr2)
print(arr2.base is arr1)



import numpy as np
arr1 = np.array([10,20,30,40,50,60,70,80])
arr2 = arr1.view()
arr1[6] = 100

print("original array:", arr1)
print("view array:", arr2)