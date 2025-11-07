# from numpy import random
# x = random.poisson(lam=2, size=10)

# print(x)


# from numpy import random
# x = random.poisson(lam=3, size=14)

# print(x)



# from numpy import random
# x = random.poisson(lam=5, size=20)

# print(x)


# visualization of poisson distribution


# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.displot(random.poisson(lam=2, size=1000))

# plt.show()



# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.displot(random.poisson(lam=5, size=1000))

# plt.show()



# difference between normal and  poisson distribution


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "normal": random.normal(loc=50, scale=7, size=1000),
    "poisson":random.poisson(lam=50, size=1000)
}

sns.displot(data, kind="kde")

plt.show()


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "normal": random.normal(loc=30, scale=5, size=200),
    "poisson": random.poisson(lam=2, size=200)
}

sns.displot(data, kind='kde')

plt.show()



# difference between binomial and poisson distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "binomial": random.binomial(n=1000, p=0.5, size=1000),
    "poisson": random.poisson(lam=10, size=1000)
}

sns.displot(data, kind="kde")

plt.show()