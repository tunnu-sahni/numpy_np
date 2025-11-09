# create your own ufunc for addition

import numpy as np

def myadd(x, y):
    return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1,2,3,4],[5,6,7,8]))



# check if a function is a ufunc


import numpy as np

print(type(np.add))


import numpy as np

print(type(np.add))




# check the of another function concatenate()

import numpy as np
print(type(np.concatenate))



import numpy as np

print(type(np.concatenate))



# check the type of something that does not exist


import numpy as np

print(type(np.blahblah))



import numpy as np

if type(np.add) == np.ufunc:
    print("add is ufunc")

else:
    print('add is not ufunc')




import numpy as np

if type(np.add) == np.ufunc:
    print('add is ufunc')

else:
    print('add is not ufunc')