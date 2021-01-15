import sys

a = int(sys.argv[1])

if a < 2:
    raise ValueError("err")

def generate_array(i):
    array = []
    while len(array) != i:
        list = []
        print(len(array))
        while len(list) != 2:
            list.append(int(input("pos int: ")))
        array.append(list)
    return array

"[[1,3],[2,2],[8,19]]"

def calculate(v):
    for k in range(len(v)):
        val = v[k]
        
