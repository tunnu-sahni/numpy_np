import numpy as np

def kmeans(x,k=2, iter=10):
    cent=x[np.random.choice(len(x),k,False)]
    for _ in range(iter):
        labels = np.argmin(((x[:,None]-cent[None,:])**2).sum(2),axis=1)
        cent = np.array([x[labels==i].mean(0) for i in range(k)])
        return labels, cent
    x = np.random.randn(100, 2)
    print(kmeans(x,3)[1])




import numpy as np

def kmeans(x,k=3, iter=20):
    cent=x[np.random.choice(len(x),k,False)]

    for _ in range(iter):

        labels = np.argmin(((x[:,None]-cent[None,:])**3).sum(3),axis=3)
        return labels, cent
    x = np.random.randn(200,3)

    print(kmeans(x,4)[2])