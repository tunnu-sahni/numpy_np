import numpy as np

x = np.linspace(0, 1, 6)
y = np.array([0,1,4,9,16,25])
coeffs = np.polyfit(x, y, 2)
print(np.poly1d(coeffs))



import numpy as np

x = np.linspace(3, 5, 6)
y = np.array([3, 5,6,7,8,9])
coeffs = np.polyfit(x, y, 3)
print(np.poly1d(coeffs))