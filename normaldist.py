# from numpy import random
# x = random.normal(size=(2, 3))

# print(x) 



# from numpy import random
# x = random.normal(size=(3, 5))

# print(x)


# from numpy import random
# x = random.normal(loc=1, scale=2, size=(2, 3))
# print(x)



# from numpy import random
# x = random.normal(loc=2, scale=4, size=(3, 4))

# print(x)



# visualization of normal distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.normal(size=1000), kind= "kde")

plt.show()



from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.normal(size=(10, 30)))

plt.show()