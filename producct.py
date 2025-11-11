import numpy as np

arr = np.array([1, 2, 3, 4])

x = np.prod(arr)

print(x)



import numpy as np

arr = np.array([2, 3, 5, 6, 7])

x = np.prod(arr)

print(x)



import numpy as np

arr = np.array([4, 5, 6, 7, 9])

x = np.prod(arr)

print(x)



import numpy as np

arr = np.array([3,44,5,6])

x = np.prod(arr)

print(x)


# find the product of the element of two array


import numpy as np

arr1 = np.array([2,3,4])
arr2 = np.array([4,5,6])

x = np.prod([arr1, arr2])

print(x)



import numpy as np

arr1 = np.array([4,5,6])
arr2 = np.array([4,5,6])

x = np.prod([arr1, arr2])

print(x)



import numpy as np

arr1 = np.array([43,5,6])
arr2 = np.array([4,6,7])

x = np.prod([arr1, arr2])

print(x)



# product over an axis


import numpy as np

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

newarr = np.prod([arr1, arr2], axis=1)

print(newarr)



import numpy as np

arr1 = np.array([4,5,6])
arr2 = np.array([5,6,7])

newarr = np.prod([arr1, arr2], axis=1)

print(newarr)



import numpy as np

arr2 = np.array([4,56,6])
arr3 = np.array([665,77,8])

newarr = np.prod([arr2, arr3], axis=1)

print(newarr)



# cummulative product

import numpy as np

arr = np.array([5,6,7,8])

newarr = np.cumprod(arr)

print(newarr)



import numpy as np

arr = np.array([55,6,7,8])

newarr = np.cumprod(arr)

print(newarr)


import numpy as np

arr = np.array([4,6,8,7])

newarr = np.cumprod(arr)

print(newarr)



import numpy as np

arr = np.array([22,4,6,7])

newarr = np.cumprod(arr)

print(newarr)