x = [1,2,3,4]
y = [4,5,6,7]
z = []

for i, j in zip(x, y):
    z.append(i + j)

print(z)


x = [4,5,6]
y = [7,8,9]
z = []

for i, j in zip(x, y):
    z.append(i + j)

print(z)
print(y)
print(x)




x = [10,20,30,49]
y = [30,49,50,69]
z = []

for i, j in zip(x, y):
    z.append(i - j)

print(z)



x = [19,29,39,49,59]
y = [39,459,956,96,80]
z = []

for i, j in zip(x, y):
    z.append(i +j)

print(z)



# add ufunf 


import numpy as np

x = [1,2,3,4]
y = [4,5,6,7]
z = np.add(x, y)

print(z)



import numpy as np

x = [22,33,44,55]
y = [33,4,55,66]
z = np.add(x, y)

print(z)



import numpy as np
x = [323,55,66,77,88]
y = [455,77,55,44,77]
z = np.add(x, y)

print(z)