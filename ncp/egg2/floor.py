import numpy as np

unknown = np.random.randint(1,101) # 18
# break x => 19
# save x <= 18
# 0 <= x <= 100 

c = 0

egg = 2

same = 0

s_f = np.random.randint(1,101)

while egg != 0:
    print("current selected floor: {}".format(s_f))
    if s_f < unknown: # 6 < 18
        s_f = np.random.randint(s_f+1,101)
        pass
    elif s_f == unknown: # 18 == 18
        s_f = np.random.randint(s_f+1,101)
        same += 1
        pass
    else: # 20 > 18
        s_f = np.random.randint(1,s_f)
        egg -= 1
    if same == 1:
        if s_f == (unknown + 1):
            print("get it")
    c += 1
    print("c: {}".format(c))
    print("egg: {}".format(egg))
    print("---------------")

print("final: ")
print("c: {}".format(c))
print("the limit: {}".format(unknown))

# limit = 18;
# f = 13;     f = 20;
# egg = 2;    egg = 1; 
# f = 18;     f = 16;
# egg = 2;    egg = 1;
# f = 25;     f = 18;
# egg = 1;    egg = 1;
# f = 23;     f = 19;
# egg = 0;    egg = 0;
