from numpy import random

x = random.zipf(a=2, size=(2, 3))

print(x)


from numpy import random

x = random.zipf(a=4, size=(3, 4))

print(x)


from numpy import random

x = random.zipf(a=4, size=(4, 5))

print(x)



from numpy import random

x = random.zipf(a=5, size=(8,9))

print(x)



from numpy import random 

x = random.zipf(a=9, size=(8,3))

print(x)



from numpy import random

x = random.zipf(a=3, size=(4,6))

print(x)



# visualization of zipf distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=1000)
sns.displot(x[x<10])

plt.show()



from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=3, size=2000)
sns.displot(x[x<20])

plt.show()



from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x= random.zipf(a=3, size=3000)
sns.displot(x[x<30])

plt.show()



from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=4, size=6000)
sns.displot(x[x<5])

plt.show()



from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=5, size=2000)
sns.displot(x[x>10])

plt.show()