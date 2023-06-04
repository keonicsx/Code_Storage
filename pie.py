
import pandas as pd
import matplotlib.pyplot as plt

age=[20,25,28,21]
income=[100,125,150,250]


plt.scatter(income,age,c='red',marker='^')
plt.xlabel("Income")
plt.ylabel("Age")
plt.show()