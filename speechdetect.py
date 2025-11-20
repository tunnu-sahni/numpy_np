# speech activity detection


import numpy as np
def frame_energy(x, N=256, hope=128):
    return np.array([np.sum(x[i:i+N]**2) for i in range(0,len(x)-N, hope)])

x = np.concatenate([np.zeros(500),np.sin(2*np.pi*200*np.linspace(0,1,1000)),np.zeros(500)])

E = frame_energy(x)
# thresold or fit logistic 

th = (E.mean()+E.std())
vad = (E>th).astype(int)

print(E[:10], vad[:10])