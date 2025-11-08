# from numpy import random

# x = random.logistic(loc=1, scale=2, size=(2,3))

# print(x)


# from numpy import random
# x = random.logistic(loc=2, scale=4, size=(3, 5))

# print(x)



# from numpy import random
# x = random.logistic(loc=4,scale=2, size=(2,4))
# print(x)



#visualization of logistic distribution


# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.displot(random.logistic(size=1000), kind="kde")

# plt.show()


# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.displot(random.logistic(size=200), kind="kde")

# plt.show()



#difference between logistic and normal distribution


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "normal": random.normal(scale=2, size=1000),
    "logistic": random.logistic(size=1000)
}

sns.displot(data, kind="kde")

plt.show()


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "normal": random.normal(scale=3, size=250),
    "logistic": random.logistic(size=250)
}

sns.displot(data, kind="kde")

plt.show()