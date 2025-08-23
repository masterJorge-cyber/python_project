import numpy as np
import time

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 1000

start = time.time()

for i in range(len(a)):
    a[i] = a[i]*2
    # print(a[i])

print(f"\n Time taken for list {time.time() - start}")
