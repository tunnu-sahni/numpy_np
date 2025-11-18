import numpy as np
data = np.array([1, np.nan, 3, 4, np.nan])
mean = np.nanmean(data)
data[np.isnan(data)] = mean
print(data)


import numpy as np
data = np.array([1,np.nan, 2, 3,4, 5, np.nan, np.nan])
mean = np.nanmean(data)
data[np.isnan(data)] = mean
print(data)



import numpy as np
data = np.array([0, np.nan, 2, 3, np.nan, np.nan, np.nan])
mean = np.nanmean(data)
data[np.isnan(data)] = mean

print(data)



import numpy as np
data = np.array([2,3, np.nan, np.nan, 6, 7, 8])
mean = np.nanmean(data)
data[np.isnan(data)] = mean
print(data)



import numpy as np
value = np.array([1, 2, np.nan, 4, np.nan])
mean = np.nanmean(value)
value[np.isnan(value)] = mean
print(value)