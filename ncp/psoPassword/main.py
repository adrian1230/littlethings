# time limit: 2 secs
# memory limit: 256 mb

import sys

a = sys.argv[1]

if len(a) > 1000000:
    raise ValueError("Exceed la guy")

if len(a) == 1 or len(a) == 2:
    print("Just a legend")

else:
    if len(a) % 3 == 0:
        alt = len(a) / 3
    else:
        alt = round(len(a)/3)
    b = a[:int(alt)]
    c = a[int(alt):-int(alt)]
    d = a[-int(alt):]
    e, counter = 0, 0
    box = []
    print(b,c,d)
    while e != len(b):
        chosen = b[:e+1]
        if chosen in d and chosen in c:
            if chosen == d[
                    -len(chosen):
            ]:
                if chosen == c[
                        c.index(chosen):
                        c.index(chosen)+len(chosen)
                ]:
                    box.append(chosen)
                    print("yes: {}".format(chosen))
                    counter += 1
        e += 1
    print(' ')
    f = 0
    while f != (len(a)-1):
        selected = a[:f+1]
        left = a[-(f+1):]
        if selected == left:
            print("yes: {}".format(selected))
        f += 1
