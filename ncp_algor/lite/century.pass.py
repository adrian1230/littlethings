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

print(pass_,len(pass_))

while True:
    if len(pass_) >= 6 and len(pass_) <= 20:
        b = 0
        while b != len(pass_):
            if pass_.islower() == True:
                b = len(pass_)
            else:
                b += 1
            print(b)
        c = 0
        print(" ")
        while c != len(pass_):
            if pass_.isupper() == True:
                c = len(pass_)
            else:
                c += 1
            print(c)
