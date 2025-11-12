import numpy as np

arr = np.array([1,1,1,2,3,4,5,5,6,7])

x = np.unique(arr)

print(x)



import numpy as np

arr = np.array([2,3,4,5])

x = np.unique(arr)

print(x)



# finding union


import numpy as np

arr1 = np.array([1,2,3,4])
arr2 = np.array([3,4,5,6])

newarr = np.union1d(arr1, arr2)

print(newarr)


import numpy as np

arr1 = np.array([3,4,5])
arr2 = np.array([4,5,6])

newarr = np.union1d(arr1, arr2)

print(newarr)




# finding intersrction


import numpy as np

arr2 = np.array([1,2,3,4])
arr3 = np.array([3,4,5,6])

newarr = np.intersect1d(arr2, arr3, assume_unique=True)

print(newarr)



import numpy as np

arr1 = np.array([2,3,4,5])
arr2 = np.array([4,5,6,7])

newarr = np.intersect1d(arr1, arr2, assume_unique=True)

print(newarr)



# finding difference


import numpy as np

set1 = np.array([1,2,3,4])
set2 = np.array([3,4,5,6])

newarr = np.setdiff1d(set1, set2, assume_unique=True )

print(newarr)



import numpy as np

set1 = np.array([1,2,3,4])
set2 = np.array([4,5,6,7])

newarr = np.setdiff1d(set1, set2, assume_unique=True)

print(newarr)



import numpy as np

set1 = np.array([2,3,4,5])
set2 = np.array([5,6,7,8])

newarr = np.setdiff1d(set1, set2, assume_unique=True)

print(newarr)



# finding symmetric difference


import numpy as np

set1 = np.array([1,2,3,4])
set2 = np.array([3,4,5,6])

newarr = np.setxor1d(set1, set2, assume_unique=True)

print(newarr)



import numpy as np

set1 = np.array([3,4,5])
set2 = np.array([4,5,6])

newarr = np.setxor1d(set1, set2, assume_unique=True)

print(newarr)