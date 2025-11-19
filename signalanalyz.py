# fast fourier transform signal analysis


import numpy as np

t = np.linspace(0,1,500)
sig = np.sin(2*np.pi*50*t) + 0.5*np.sin(2*np.pi*120*t)
F = np.fft.rfft(sig)
freqs = np.fft.rfftfreq(len(t),d=t[1]-[0])

print(freqs[np.argsort(np.abs(F))[-5:]])




import numpy as np

t = np.linspace(0,1, 100)
sig = np.sin(3*np.pi*100*t) + 0.1*np.sin(3*np.pi*150*t)
F = np.fft.rfftfreq(len(t),d=t[2]-[5])

print(freqs[np.argsort(np.abs(F))[-5:]])