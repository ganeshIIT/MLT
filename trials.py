import numpy as np

y = np.array([2,3,2,5,6])

encoded= np.zeros((y.size, y.max()+1))

print(encoded)

encoded[np.arange(y.size), y] = 1.0

print(encoded)