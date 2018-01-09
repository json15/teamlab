import numpy as np

a= np.random.normal(3,5,10000000)
split = 0

for i in a:
    split += i

b = split/10000000
print(b)