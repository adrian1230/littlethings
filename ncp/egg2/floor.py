import numpy as np

unknown = np.random.randint(1,101)
# if limit = 18
# break 19 <= x <= 100
# save 1 <= x <= 18
# 1 <= x <= 100 

c = 0

egg = 2

same = 0

s_f = np.random.randint(1,101)

minus = False

greater = 0

while egg != 0:
    minus = False
    print("current selected floor: {}".format(s_f))
    if s_f < unknown: # 6 < 18
        s_f = np.random.randint(s_f+1,101)
    elif s_f == unknown: # 18 == 18
        same += 1
        if greater == 1:
            break
        s_f = np.random.randint(s_f+1,101)
    else: # 25 > 18
        egg -= 1
        if s_f == (unknown + 1):
            greater += 1
        if same == 1:
            minus = True
        if minus == True:
            if s_f == (unknown + 1):
                print("get it")
                break
        s_f = np.random.randint(1,s_f)
    c += 1
    print("c: {}".format(c))
    print("egg: {}".format(egg))
    print("---------------")

print("the limit: {}".format(unknown))

