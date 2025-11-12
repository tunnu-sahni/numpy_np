import numpy as np

x = np.sin(np.pi/2)

print(x)


import numpy as np

x = np.sin(np.pi/3)

print(x)


import numpy as np

x = np.sin(np.pi/4)

print(x)


import numpy as np

x = np.sin(np.pi/6)

print(x)



import numpy as np

x = np.sin(np.pi/8)

print(x)


import numpy as np

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.sin(arr)

print(x)



import numpy as np

arr = np.array([np.pi/4, np.pi/8])

x = np.sin(arr)

print(x)



import numpy as np

arr = np.array([np.pi/5])

x = np.sin(arr)

print(x)



import numpy as np

arr = np.array([np.pi/4, np.pi/7])

x = np.sin(arr)

print(x)



import numpy as np

arr = np.array([np.pi/8, np.pi/7])

x = np.sin(arr)

print(x)



# convert degree into radians


import numpy as np

arr = np.array([90, 180, 270, 360])

x = np.deg2rad(arr)

print(x)


import numpy as np

arr = np.array([10, 30, 45, 90])

x = np.deg2rad(arr)

print(x)



import numpy as np

arr = np.array([20, 15,3,80, 75])

x = np.deg2rad(arr)

print(x)



import numpy as np

arr = np.array([90, 110, 290])

x = np.deg2rad(arr)

print(x)



# radians to degree


import numpy as np

arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])

x = np.rad2deg(arr)

print(x)


import numpy as np

arr = np.array([np.pi/3, np.pi, 3.4*np.pi, 4*np.pi])

x = np.rad2deg(arr)

print(x)



import numpy as np

arr = np.array([np.pi/6, np.pi, 7*np.pi, 6.4*np.pi])

x = np.rad2deg(arr)

print(x)



# findind angles


import numpy as np

x = np.arcsin(1.0)

print(x)


import numpy as np

x = np.arcsin(1.6)

print(x)


import numpy as np

x = np.arcsin(3.4)

print(x)


import numpy as np

x = np.arcsin(1.5)

print(x)




# angles of each value in array


import numpy as np

arr = np.array([1, -1, 0.1])

x = np.arcsin(arr)

print(x)



import numpy as np

arr = np.array([4, 9, 43,90])

x = np.arcsin(arr)

print(x)



# hypotenues


import numpy as np

base = 3
perp = 4

x = np.hypot(base, perp)

print(x)


import numpy as np

base = 40
perp = 50

x = np.hypot(base, perp)

print(x)


import numpy as np

perp = 50
base = 70

x = np.hypot(base, perp)

print(x)


import numpy as np

base = 8
perp = 6

x = np.hypot(base, perp)

print(x)