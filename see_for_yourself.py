import numpy as np
from dostuff.code import doAThing

values, skew, loc, scale = \
    (np.loadtxt(f"tests/fixture/{n}") for n in \
    ('values', 'skew', 'loc', 'scale'))

result = doAThing(values, skew, loc, scale)
print(np.count_nonzero(result == 0))
