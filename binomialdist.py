# from numpy import random
# x = random.binomial(n=10, p=0.5, size=10)

# print(x)



# from numpy import random
# x = random.binomial(n=5, p=.10, size=20)

# print(x)


# from numpy import random
# x = random.binomial(n=12, p=.10, size=13)

# print(x)



# visualization of binomial distribution


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.binomial(n=10, p=0.5, size=1000))

plt.show()



from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.binomial(n=20, p=0.20, size=(200)))

plt.show()