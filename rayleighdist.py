from numpy import random

x = random.rayleigh(scale=2, size=(2, 3))

print(x)


from numpy import random

x = random.rayleigh(scale=3, size=(1, 4))

print(x)



from numpy import random

x = random.rayleigh(scale=4, size=(4, 5))

print(x)



from numpy import random

x = random.rayleigh(scale=5, size=(5, 6))

print(x)



# visualization of rayleigh distribution


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.rayleigh(size=1000), kind="kde")

plt.show()



from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.rayleigh(size=400), kind="kde")

plt.show()