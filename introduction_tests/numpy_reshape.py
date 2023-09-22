import numpy as np

a_1d = np.random.rand(1000)
print(a_1d)

a_2d = np.reshape(a_1d, (100, 10))
print(a_2d)

a_3d = np.reshape(a_1d, (10, 10, 10))
print(a_3d)

"""???"""
