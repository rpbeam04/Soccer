import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import poisson

trials = 100
rate = 0.8
x = []
for i in range(trials):
    x.append(sum([1 for x in np.random.random(90) if x < rate/90]))
y = poisson.pmf(range(0,max(x)+1), rate)

goals, counts = np.unique(x, return_counts=True)
counts = np.divide(counts,trials)
plt.bar(goals, counts, align='center')
plt.plot(range(max(x)+1), y, color = "orange")
plt.show()