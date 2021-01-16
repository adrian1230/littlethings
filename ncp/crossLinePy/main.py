import sys
import numpy as np

a = int(sys.argv[1])

if a < 2:
    raise ValueError("err")

def generate_array(i):
    array = []
    while len(array) != i:
        list = []
        while len(list) != 2:
            list.append(int(input("pos int: ")))
        array.append(list)
    return array

"[[1,3],[2,2],[8,19]]"

"""
[1,3]: [2,2],[8,19]
[2,2]: [1,3],[8,19]
[8,19]: [1,3],[2,2]
"""

def calculate(v):
    c = 0
    for k in range(len(v)):
        left = v.pop(k)
        #ran = np.arange(v[k][0],v[k][1]+1)
        for j in range(len(left)):
            if left[j][0] > v[k][0]:
                if left[j][1] < v[k][1]:
                    c += 1
                else:
                    pass
            else:
                pass
                
