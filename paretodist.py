from numpy import random

x = random.pareto(a=2, size=(2, 3))

print(x)



from numpy import random

x = random.pareto(a=4, size=(4, 6))

print(x)


from numpy import random

x = random.pareto(a=1, size=(4, 5))

print(x)



from numpy import random

x = random.pareto(a=6, size=(3, 9))

print(x)


from numpy import random

x = random.pareto(a=4, size=(5, 4))

print(x)



from numpy import random

x = random.pareto(a=3, size=(8, 5))

print(x)


from numpy import random

x = random.pareto(a=8, size=(8, 6))

print(x)




# visualization of pareto distribution


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.pareto(a=2, size=1000))

plt.show()



from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.pareto(a=3, size=200))

plt.show()



from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.pareto(a=4, size=300))

plt.show()




from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.pareto(a=4, size=4000))

plt.show()



from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.pareto(a=5, size=5000))

plt.show()



from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.pareto(a=8, size=9000))

plt.show()



from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.pareto(a=9, size=2000))

plt.show()