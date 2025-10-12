import numpy as np
arr = np.array([10,25,30,45,60])
print(arr[arr>30])




import numpy as np
arr = np.array([13,34,55,66,78,99])
print(arr[arr>13])
print(arr[arr<66])



import numpy as np
arr = np.array([10,12,33,44,45,56,57,67,68])
print(arr[arr%2 ==0])
print(arr[arr%2 <=0])
print(arr[arr %3 ==0])




import numpy as np
arr = np.array([2,3,4,5,12,33,55,64,43,65,76,56,43])
print(arr[arr>2])
print(arr<3)
print(arr<2)



import numpy as np
arr = np.array([10,12,23,23,34,35,333,45,5,767,87,97])
print(arr<10)
print(arr>5)
print(arr[arr>5])



import numpy as np
arr = np.array([[10,12,13,14,15],[34,34,55,56,567]])
print(arr[arr>12])
print(arr%2 == 0)
print(arr[arr%2 ==0])