# input 1 - 1000000 long string.
# find password met the qualify of prefix, suffix, and obelix.
# else: "Just a legend" without quote in return.

# time limit: 2 secs
# memory limit: 256 mb
# input & output: standard

import sys

# asdakdbasdjbasjhdas len 19

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
    print(b,c,d)
    e, counter = 0, 0
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
                    print(chosen)
                    counter += 1
        e += 1
