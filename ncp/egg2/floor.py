import numpy as np

unknown = np.random.randint(1,101) # 18
# break x => 19
# save x <= 18
# 0 <= x <= 100 

c = 0

egg = 2

same = 0

s_f = np.random.randint(1,101)

# 9:2 18:2 20:1
# 9:2 20:1 18:1

while egg != 0:
    bucket = egg 
    if same == 1:
        if bucket == egg:
            pass
        elif bucket == (egg - 1):
            if s_f == (unknown + 1):
                print("get it")
                break
        else:
            pass
    print("current selected floor: {}".format(s_f))
    if s_f < unknown: # 6 < 18
        s_f = np.random.randint(s_f+1,101)
    elif s_f == unknown: # 18 == 18
        s_f = np.random.randint(s_f+1,101)
        same += 1
    else: # 25 > 18
        s_f = np.random.randint(1,s_f)
        egg -= 1
    c += 1
    print("c: {}".format(c))
    print("egg: {}".format(egg))
    print("---------------")

print("the limit: {}".format(unknown))

# limit = 18;
# f = 13;     f = 20;      f = 20;
# egg = 2;    egg = 1;     egg = 1;
# f = 18;     f = 16;      f = 18;
# egg = 2;    egg = 1;     egg = 1;
# f = 25;     f = 18;      break; as 18 worked not 20; so 19 must be limit + 1
# egg = 1;    egg = 1;
# f = 23;     f = 19;
# egg = 0;    egg = 0;
