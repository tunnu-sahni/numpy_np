import numpy as np

arr = np.arange(1, 10)

print(np.log2(arr))


import numpy as np

arr = np.arange(1, 10)

print(np.log2(arr))



# log at base 10


import numpy as np

arr = np.arange(1, 10)

print(np.log10(arr))



# natural log or log at base e


import numpy as np

arr = np.arange(1, 10)

print(np.log(arr))


# log at any base

from math import log 
import numpy as np

nplog = np.frompyfunc(log, 2, 1)

print(nplog(100,15))

