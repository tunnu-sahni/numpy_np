import numpy as np
arr = np.array([1,2,3])
for x in arr:
    print(x)




import numpy as np
arr = np.array([1,2,3,4,5,6,7])
for x in arr:
    print(x)



import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
for x in arr:
    print(x)




import numpy as np
arr = np.array([[10,11,12,13],[14,15,16,17]])
for x in arr:
    print(x)



import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
for x in arr:
    print(x)




# down to the scalar


import numpy as np
arr = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)
            print(y)
            print(x)





import numpy as np
arr = np.array([[[1,2],[3,4],[5,6]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)
            print(x)
            print(y)