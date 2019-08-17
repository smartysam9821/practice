import numpy as np
import matplotlib.pyplot as plt

a = np.random.randint(10,100,50)
#1. crate boxplot for numpy array
plt.boxplot(a)
plt.show()


# 3. create histogram for numpy array
plt.hist(a)
plt.show()

print("histogram plotted")

