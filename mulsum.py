import numpy as np
import sys

# python mulsum.py 4 9 2 3 5 7 8 1 6 0

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d = int(sys.argv[4])
e = int(sys.argv[5])
f = int(sys.argv[6])
g = int(sys.argv[7])
h = int(sys.argv[8])
i = int(sys.argv[9])

j = int(sys.argv[10])

arr = np.array(
	[
		[a,b,c],
		[d,e,f],
		[g,h,i]
	]
)

def mulsum(arr): 
    a = arr[0][0] * arr[0][1] * arr[0][2] 
    while len(str(a)) != 1: 
        aa = 0 
        for i in str(a): 
            aa += int(i) 
        a = aa 
    print('F+(abc) = ' + str(a)) 
    b = arr[1][0] * arr[1][1] * arr[1][2] 
    while len(str(b)) != 1: 
        bb = 0 
        for i in str(b): 
            bb += int(i) 
        b = bb 
    print('F+(def) = ' + str(b)) 
    c = arr[2][0] * arr[2][1] * arr[2][2] 
    while len(str(c)) != 1: 
        cc = 0 
        for i in str(c): 
            cc += int(i) 
        c = cc 
    print('F+(ghi) = ' + str(c)) 
    d = arr[0][0] * arr[1][0] * arr[2][0] 
    while len(str(d)) != 1: 
        dd = 0 
        for i in str(d): 
            dd += int(i) 
        d = dd
    print('F+(adg) = ' + str(d)) 
    e = arr[0][1] * arr[1][1] * arr[2][1] 
    while len(str(e)) != 1: 
        ee = 0 
        for i in str(e): 
            ee += int(i) 
        e = ee 
    print('F+(beh) = ' + str(e)) 
    f = arr[0][2] * arr[1][2] * arr[2][2] 
    while len(str(f)) != 1: 
        ff = 0 
        for i in str(f): 
            ff += int(i) 
        f = ff 
    print('F+(cfi) = ' + str(f)) 
    g = arr[0][0] * arr[1][1] * arr[2][2] 
    while len(str(g)) != 1: 
        gg = 0 
        for i in str(g): 
            gg += int(i) 
        g = gg 
    print('F+(aei) = ' + str(g)) 
    h = arr[0][2] * arr[1][1] * arr[2][0]
    while len(str(h)) != 1:
        hh = 0
        for i in str(h):
            hh += int(i)
        h = hh
    print('F+(ceg) = ' + str(h))

mulsum(arr+j)

