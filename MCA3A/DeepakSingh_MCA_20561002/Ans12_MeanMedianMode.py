import numpy as np
from scipy import stats

dataset = [58, 2, 8, 6, 12, 4]
mean = np.mean(dataset)
print(mean)

median = np.median(dataset)
print(median)

mode = stats.mode(dataset)
print(mode)
