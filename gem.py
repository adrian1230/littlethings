import numpy as np
from decimal import Decimal

data = []

def get(num,length,per,cent):
    letters = 'abcdefghijklmnopqrstuvwxyz'

    while len(data) < num:
        target = np.random.randint(len(letters))
        data.append(letters[target])

    for i in range(len(data)):
        while len(data[i]) < length:
            p = np.random.randint(per)/per
            d = np.random.randint(cent)/cent
            ip = 0
            if p <= 0.500000000000000000000000000000:
                left = []
                position = 0
                digit = str(Decimal(p)*100).split('.')
                if len(digit) < 2:
                    ip = int(digit[0])
                    while len(str(ip)) != 1:
                        pi = 1
                        for g in str(ip):
                            pi *= int(g)
                        ip = pi
                if len(digit) == 2:
                    pat1 = digit[0]
                    pat2 = digit[1]
                    while len(str(pat1)) != 1:
                        p1 = 1
                        for j in str(pat1):
                            p1 *= int(j)
                        pat1 = p1
                    p2 = 0
                    for m in pat2:
                        p2 += int(m)
                    pat2 = p2
                    ip = pat1 * pat2
                    pi = 0 
                    for n in str(ip):
                        pi += int(n)
                    ip = pi
                for p in range(len(letters)):
                    if letters[p] in data[i]:
                        pass
                    else:
                        left.append(letters[p])
                        position = np.random.randint(len(left))
                if d <= 0.330000000000000000000000000000:
                    data[i] = str(ip) + left[position] + data[i]
                elif d > 0.330000000000000000000000000000 and d <= 0.660000000000000000000000000000:
                    data[i] = left[position] + str(ip) + data[i]
                elif d > 0.660000000000000000000000000000:
                    data[i] = left[position] + data[i] + str(ip)
                else:
                    pass       
            elif p > 0.500000000000000000000000000000:
                left = []
                position = 0
                digit = str(Decimal(p)*100).split('.')
                if len(digit) < 2:
                    ip = int(digit[0])
                    while len(str(ip)) != 1:
                        pi = 1
                        for g in str(ip):
                            pi *= int(g)
                        ip = pi
                if len(digit) == 2:
                    pat1 = digit[0]
                    pat2 = digit[1]
                    while len(str(pat1)) != 1:
                        p1 = 1
                        for j in str(pat1):
                            p1 *= int(j)
                        pat1 = p1
                    p2 = 0
                    for m in pat2:
                        p2 += int(m)
                    pat2 = p2
                    ip = pat1 * pat2
                    pi = 0 
                    for n in str(ip):
                        pi += int(n)
                    ip = pi
                for p in range(len(letters)):
                    if letters[p] in data[i]:
                        pass
                    else:
                        left.append(letters[p])
                        position = np.random.randint(len(left))
                if d <= 0.330000000000000000000000000000:
                    data[i] = str(ip) + data[i] + left[position] 
                elif d > 0.330000000000000000000000000000 and d <= 0.660000000000000000000000000000:
                    data[i] = data[i] + str(ip) + left[position]
                elif d > 0.660000000000000000000000000000:
                    data[i] = data[i] + left[position] + str(ip)
                else:
                    pass
                
get(100,43,10000,1000)

print(data[np.random.randint(len(data))])
                
