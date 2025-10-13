import numpy as np
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)



import numpy as np
arr = np.array([1.1, 2.1, 3.1, 4.1, 5.1])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)




import numpy as np
arr = np.array([1,0,3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)




import numpy as np
arr = np.array([1,2,0,3,0,4])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)




import numpy as np
arr = np.array([2,3,0,6,4,0])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)