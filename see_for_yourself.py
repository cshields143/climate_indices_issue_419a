import numpy as np
import scipy.stats

values = np.loadtxt('values')
skew = np.loadtxt('skew')
loc = np.loadtxt('loc')
scale = np.loadtxt('scale')
out = np.loadtxt('out')

result = scipy.stats.pearson3.cdf(values, skew, loc, scale)
calculated = np.count_nonzero(result == 0)
actual = np.count_nonzero(out == 0)

assert calculated == actual
