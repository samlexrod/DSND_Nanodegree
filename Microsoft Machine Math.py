import numpy as np


v = np.array([3, 5])
print(v)
v_sq = v**2
print(v_sq)
v_sq_sum = v_sq.sum()
print(v_sq_sum)
magnitude = np.sqrt(v_sq_sum)
print('{:2.3f}'.format(magnitude))


print((np.array([2, 5]) * np.array([4, 3])).sum())


print(np.cross(np.array([4, 1, 6]), np.array([2, 3, 5])))