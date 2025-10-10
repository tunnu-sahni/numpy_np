import numpy as np
arr = np.array([1,2,3,4],ndmin=5)
print(arr)
print("dimension:",arr.ndim)



import numpy as np
arr = np.array([1,2,3],ndmin=4)
print(arr)
print(len(arr))
print("dimension:",arr.ndim)





import numpy as np
arr = np.array([2,3,44,55,66,7,77],ndmin=9)
print(arr)
print("dimension:",arr.ndim)
print(len(arr))





import numpy as np
arr = np.array([[2,3,4,5],[4,55,6,7]],ndmin=6)
print(arr)
print("dimension:",arr.ndim)




import numpy as np
arr = np.array([[[2,3,4],[4,5,6],[6,7,8]]],ndmin=6)
print(arr)
print("diemnsion:",arr.ndim)



import numpy as np
arr = np.array([[1,2,3,4],[5,6,7,8]],ndmin=1)
print(arr)
print("dimension:",arr.ndim)



import numpy as np
arr = np.array([[[1,2,3],[4,5,6],[7,8,9]]],ndmin=12)
print(arr)
print("dimension:",arr.ndim)



import numpy as np
arr = np.array([[3,4,5,6],[7,8,9,0]],ndmin=20)
print(arr)
print("dimension:",arr.ndim)




# check number of dimension

import numpy as np
arr = np.array(5)
print(arr)
print("number of dimension:",arr.ndim)