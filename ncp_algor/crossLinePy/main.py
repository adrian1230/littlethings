import sys

a = int(sys.argv[1])

if a < 2:
    raise ValueError("err")

def generate_array(i):
    array = []
    while len(array) != i:
        list = []
        print("--------")
        while len(list) != 2:
            list.append(int(input("pos int: ")))
        array.append(list)
    return array

#[[1,3],[2,2],[8,19],[1,18],[5,13]]
#[1,3]: 1
#[1,18]: 3

#[[1,9],[1,2],[4,9]]
#[[1,2],[4,9]]

def calculate(v):
    c = 0
    d = 0
    while d != len(v):
        left = v.copy()
        del left[d]
        for j in range(len(left)):
            if left[j][0] > v[d][0]:
                if left[j][1] < v[d][1]:
                    c += 1
                elif left[j][1] == v[d][1]:
                    c += 1
                else:
                    pass
            elif left[j][0] == v[d][0]:
                if left[j][1] < v[d][1]:
                    c += 1
                elif left[j][1] == v[d][1]:
                    c += 1
                else:
                    pass
            else:
                pass
        d += 1
    if c == 0:
        print(-1)
    else:
        print(c)

calculate(generate_array(a))
        
