import sys

def rollOut(
    start:'start value',
    length:'length of array',
    first:'only s or p'):
    array = [start]
    if first.lower() == 's':
        value = start
        c = 0
        while len(array) != length:
            last = array[-1]
            c += 1
            value += 1
            if c % 2 != 0:
                if value % 2 == 0:
                    pass
                else:
                    if value > last:
                        array.append(last+value)
                    else:
                        pass
            else:
                if value % 2 == 0:
                    if value > last:
                        array.append(last+value)
                    else:
                        pass
                else:
                    pass
    elif first.lower() == "p":
        val = start
        d = 0
        while len(array) != length:
            final = array[-1]
            d += 1
            val += 1
            if d % 2 != 0:
                if val % 2 == 0:
                    if value > final:
                        array.append(final+val)
                else:
                    pass
            else:
                if val % 2 == 0:
                    pass
                else:
                    if value > final:
                        array.append(final+val)
            print(array)
        print(array)
    else:
        pass
    print(array)

rollOut(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3])
