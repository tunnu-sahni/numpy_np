# from numpy import random

# x = random.uniform(size=(2, 3))

# print(x)


# from numpy import random
# x = random.uniform(size=(4, 5))

# print(x)



# from numpy import random
# x = random.uniform(size=(1,3))

# print(x)



# visualization of uniform distribution


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.uniform(size=1000), kind="kde")

plt.show()


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.uniform(size=100), kind="kde")

plt.show()


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.uniform(size=200), kind="kde")

plt.show()




from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.uniform(size=300), kind="kde")

plt.show()