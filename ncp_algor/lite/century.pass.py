# 1 <= input <= 50
# '.' & '!' are allowed
# check to be strong
# 6 <= x <= 20
# lower() in x => 1
# upper() in x => 1
# isdigit() in x => 1
# non-3-recurring letters
# 2-recurring if former requirements are met
# return 0 if password is strong
# return mini-step for turning the password into a strong one
# in 1 step
# you can insert a character
# you can delete a character
# you can replace a character with another

import numpy as np

a = np.random.randint(1,51)

pass_ = ""

alpha = "abcdefghijklmnopqrstuvwxyz"

beta = "0123456789"

theta = ".!"

def prob(j):
    return np.random.randint(j) / j

while len(pass_) != a:
    rand = prob(1000)
    if rand < 33.33333333333333:
        pass_ += alpha[np.random.randint(len(alpha))]
    elif rand >= 33.33333333333333 and rand < 66.66666666666666:
        pass_ += beta[np.random.randint(len(beta))]
    elif rand >= 66.66666666666666:
        pass_ += theta[np.random.randint(len(theta))]
    else:
        pass

# print(pass_,len(pass_))

pass_ = "aghjH2!asdsss"
 
if len(pass_) >= 6 and len(pass_) <= 20:
    b = 0
    while b != len(pass_):
        if pass_[b].islower() == True:
            b = -1
            break
        else:
            b += 1
    c = 0
    while c != len(pass_):
        if pass_[c].isupper() == True:
            c = -1
            break
        else:
            c += 1
    d = 0
    while d != (len(pass_)-1):
        if pass_[d].isdigit() == True:
            d = -1
            break
        else:
            d += 1
    if b == -1 and c == -1 and d == -1:
        e = 0
        # aghjH2!asdsss
        # aghjH2!assdss
        while e != len(pass_):
            if e > (len(pass_) - 3):
                pass
            else:
                if pass_[e] == pass_[e+1] == pass_[e+2]:
                    pass
                else:
                    e = -1
                    break
            e += 1
    if e == -1:
        print(0)
else:
    pass
