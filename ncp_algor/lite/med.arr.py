# arr1 len = m; arr2 len = n
# 0 <= m & n <= 1000
# 1 <= m + n <= 1000
# -10^6 <= arr1[x], arr2[x] <= 10^6 

import numpy as np

arr1, arr2 = [], []

a1 = np.random.randint(0,1001)

a2 = a1

while a1 == a2:
    a2 = np.random.randint(0,1001)

while len(arr1) != a1:
    val = np.random.randint(-1000000,1000001)
    if val not in arr1:
        arr1.append(val)

while len(arr2) != a2:
    val = np.random.randint(-1000000,1000001)
    if val not in arr2:
        arr2.append(val)

arr1 = sorted(arr1)
arr2 = sorted(arr2)

