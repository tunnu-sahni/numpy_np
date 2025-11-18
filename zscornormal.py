import numpy as np

x = np.array([[10, 200],[20, 300],[40, 400]] , dtype=float)
mu = x.mean(axis=0); sigma = x.std(axis=0)
x_norm = (x - mu) / sigma
print(x_norm)


import numpy as np

y = np.array([[20, 300],[40, 500]], dtype=float)
mu = x.mean(axis=0); sigma = x.std(axis=0)
x_norm = ( x - mu) / sigma 
print(x_norm)


import numpy as np

x = np.array([[2, 44],[5, 600],[3, 400]], dtype=float)
mu = x.mean(axis=0); sigma = x.std(axis=0)
x_norm = (x - mu) / sigma
print(x_norm)



import numpy as np
a = np.array([[2, 33],[4, 500],[6, 700]], dtype=float)
ab = a.mean(axis=0); sigma = a.std(axis=0)
ab_norm = (a - a) / sigma
ab_norm = (a - ab) / sigma
print(ab_norm)