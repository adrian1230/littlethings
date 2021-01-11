import sys

# give a start value and final length of the array
# determine either the first add value is singular or plural
# render the final list

def rollOut(
    start:'start value',
    length:'length of array',
    first:'only s: singular or p: plural'):
    array = [start]
    if first.lower() == 's':
        value = start
        c = 0
        while len(array) != length:
            long = len(array)
            last = array[-1]
            c += 1
            while len(array) == long:
                value += 1
                if c % 2 != 0:
                    if value % 2 == 0:
                        pass
                    else:
                        if value > last:
                            array.append(last+value)
                else:
                    if value % 2 == 0:
                        if value > last:
                            array.append(last+value)
    elif first.lower() == "p":
        value = start
        c = 0
        while len(array) != length:
            long = len(array)
            last = array[-1]
            c += 1
            while len(array) == long:
                value += 1
                if c % 2 != 0:
                    if value % 2 == 0:
                        if value > last:
                            array.append(last+value)
                else:
                    if value % 2 == 0:
                        pass
                    else:
                        if value > last:
                            array.append(last+value)
    print(array)

rollOut(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3])
