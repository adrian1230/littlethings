# arr1 len = m; arr2 len = n
# 0 <= m & n <= 1000
# 1 <= m + n <= 1000
# -10^6 <= arr1[x], arr2[x] <= 10^6 

import numpy as np

arr1, arr2 = [], []

a1 = np.random.randint(0,1001)

a2 = a1

c = 0

while c == 0:
    while a1 == a2:
        a2 = np.random.randint(0,1001)
    c += 1
    if (a1+a2) > 1000:
        c = 0
        a2 = a1

while len(arr1) != a1:
    val = np.random.randint(-1000000,1000001)
    arr1.append(val)

while len(arr2) != a2:
    val = np.random.randint(-1000000,1000001)
    arr2.append(val)

arr = arr1 + arr2
arr = sorted(arr)

if (a1+a2) % 2 == 0:
    m = (a1+a2) / 2
    m = int(m)
    print((arr[m-1]+arr[m])/2)

else:
    m = (a1+a2) / 2 - 0.5
    m = int(m)
    print(arr[m])
