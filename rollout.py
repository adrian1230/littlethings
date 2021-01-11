import sys

def rollOut(
    start:'start value',
    length:'length of array',
    first:'only s: singular or p: plural'):
    array = [start]
    # if True:
    if first.lower() == 's':
        value = start
        c = 0
        # start and value = 1
        # c = position
        # 1 4 10
        #  3 6
        while len(array) != length:
            long = len(array)
            last = array[-1]
            # if len(array) == long:
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
                            pass
                else:
                    if value % 2 == 0:
                        if value > last:
                            array.append(last+value)
                        else:
                            pass
                    else:
                        pass
            print(c,last,long,array)
    # elif first.lower() == "p":
    #     val = start
    #     d = 0
    #     while len(array) != length:
    #         final = array[-1]
    #         d += 1
    #         val += 1
    #         if d % 2 != 0:
    #             if val % 2 == 0:
    #                 if value > final:
    #                     array.append(final+val)
    #             else:
    #                 pass
    #         else:
    #             if val % 2 == 0:
    #                 pass
    #             else:
    #                 if value > final:
    #                     array.append(final+val)
    print(array)

rollOut(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3])
