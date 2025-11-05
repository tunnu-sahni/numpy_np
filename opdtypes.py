# import numpy as np
# arr = np.array([1,2,3])
# for x in np.nditer(arr,flags=['buffered'], op_dtypes=['5']):
#     print(x)




import numpy as np
arr = np.array([[1,2,3,4],[5,6,7,8]])
for x in np.nditer(arr[:,::2]):
    print(x)




import numpy as np
arr = np.array([[1,2,3,4],[5,6,7,8]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)



import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)



import numpy as np
arr = np.array([[[1,2],[3,4],[5,6],[7,8]]])
for matrix in arr:
    for row in matrix:
        for x in row:
            print(x)