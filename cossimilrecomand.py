import numpy as np

A = np.random.rand(5, 4)
sim = (A@A.T) / (np.linalg.norm(A,axis=1)[:, None]*np.linalg.norm(A,axis=1))

print(sim)



# cosine similarity recommender


import numpy as np

A = np.random.rand(10, 6)

sim = (A@A.T) / (np.linalg.norm(A,axis=1)[:, None]*np.linalg.norm(A,axis=1))

print(sim)




import numpy as np

A = np.random.rand(9, 3)

sim = (A@A.T) / (np.linalg.norm(A, axis=1)[:, None]*np.linalg.norm(A,axis=1))

print(sim)



import numpy as np

A = np.random.rand(5, 6)

sim = (A@A.T) / (np.linalg.norm(A, axis=1)[:, None]*np.linalg.norm(A,axis=1))

print(sim)