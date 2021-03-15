import scipy.stats

def doAThing(values, skews, locs, scales):
    return scipy.stats.pearson3.cdf(values, skews, locs, scales)
