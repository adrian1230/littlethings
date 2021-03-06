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

alpha1 = "abcdefghijklmnopqrstuvwxyz"

alpha2 = alpha1.upper()

beta = "0123456789"

theta = ".!"

def prob(j):
    return np.random.randint(j) / j

while len(pass_) != a:
    rand = prob(1000)
    if rand <= 0.25:
        pass_ += alpha1[np.random.randint(len(alpha1))]
    elif rand > 0.25 and rand <= 0.5:
        pass_ += alpha2[np.random.randint(len(alpha2))]
    elif rand > 0.5 and rand <= 0.75:
        pass_ += beta[np.random.randint(len(beta))]
    elif rand > 0.75:
        pass_ += theta[np.random.randint(len(theta))]
    else:
        pass

print(pass_,len(pass_))

print("\nChecking...\n\nResult:")

check = 0
 
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
        while e != len(pass_):
            if e > (len(pass_) - 3):
                pass
            else:
                if pass_[e] == pass_[e+1] == pass_[e+2]:
                    e = -1
                    break
            e += 1
        if e != -1:
            print("0, already strong - no change needed")
        else:
            check = 1
    else:
        check = 1
else:
    check = 1

if check == 1:
    theta_, beta_, alpha_1, alpha_2 = 0, 0, 0, 0
    for i in range(len(pass_)):
        if pass_[i] in theta:
            theta_ += 1
        elif pass_[i] in beta:
            beta_ += 1
        elif pass_[i] in alpha1:
            alpha_1 += 1
        elif pass_[i] in alpha2:
            alpha_2 += 1
        else:
            raise ValueError("not allowed to be in pass")
    counter = 0
    while len(pass_) > 20:
        buffer = 0
        while buffer == 0:
            location = np.random.randint(len(pass_))
            target = pass_[location]
            if target in theta:
                if theta_ == 1:
                    buffer = 0
                else:
                    pass_ = pass_.replace(target,'',1)
                    theta_ -= 1
                    counter += 1
                    buffer += 1
            elif target in beta:
                if beta_ == 1:
                    buffer = 0
                else:
                    pass_ = pass_.replace(target,'',1)
                    beta_ -= 1
                    counter += 1
                    buffer += 1
            elif target in alpha1:
                if alpha_1 == 1:
                    buffer = 0
                else:
                    pass_ = pass_.replace(target,'',1)
                    alpha_1 -= 1
                    counter += 1
                    buffer += 1
            elif target in alpha2:
                if alpha_2 == 1:
                    buffer = 0
                else:
                    pass_ = pass_.replace(target,'',1)
                    alpha_2 -= 1
                    counter += 1
                    buffer += 1
            else:
                pass
    while len(pass_) < 6:
        rand = prob(1000)
        if rand <= 0.25:
            pass_ += alpha1[np.random.randint(len(alpha1))]
            alpha_1 += 1
            counter += 1
        elif rand > 0.25 and rand <= 0.5:
            pass_ += alpha2[np.random.randint(len(alpha2))]
            alpha_2 += 1
            counter += 1
        elif rand > 0.5 and rand <= 0.75:
            pass_ += beta[np.random.randint(len(beta))]
            beta_ += 1
            counter += 1
        elif rand > 0.75:
            pass_ += theta[np.random.randint(len(theta))]
            theta_ += 1
            counter += 1
        else:
            pass
    comb = [theta_,beta_,alpha_1,alpha_2]
    ination = [theta,beta,alpha1,alpha2]
    if theta_ == 0:
        max_index = comb.index(max(comb))
        position = [
            i for i in range(len(pass_)) 
            if pass_[i] in ination[max_index]
            ]
        pass_ = pass_.replace(
            pass_[position[np.random.randint(len(position))]],
            theta[np.random.randint(len(theta))],
            1)
        theta_ += 1
        counter += 1
        if ination[max_index] == beta:
            beta_ -= 1
        elif ination[max_index] == alpha1:
            alpha_1 -= 1
        else:
            alpha_2 -= 1
    if beta_ == 0:
        max_index = comb.index(max(comb))
        position = [
            i for i in range(len(pass_)) 
            if pass_[i] in ination[max_index]
            ]
        pass_ = pass_.replace(
            pass_[position[np.random.randint(len(position))]],
            beta[np.random.randint(len(beta))],
            1)
        beta_ += 1
        counter += 1
        if ination[max_index] == theta:
            theta_ -= 1
        elif ination[max_index] == alpha1:
            alpha_1 -= 1
        else:
            alpha_2 -= 1
    if alpha_1 == 0:
        max_index = comb.index(max(comb))
        position = [
            i for i in range(len(pass_)) 
            if pass_[i] in ination[max_index]
            ]
        pass_ = pass_.replace(
            pass_[position[np.random.randint(len(position))]],
            alpha1[np.random.randint(len(alpha1))],
            1)
        alpha_1 += 1
        counter += 1
        if ination[max_index] == beta:
            beta_ -= 1
        elif ination[max_index] == theta:
            theta_ -= 1
        else:
            alpha_2 -= 1
    if alpha_2 == 0:
        max_index = comb.index(max(comb))
        position = [
            i for i in range(len(pass_)) 
            if pass_[i] in ination[max_index]
            ]
        pass_ = pass_.replace(
            pass_[position[np.random.randint(len(position))]],
            alpha2[np.random.randint(len(alpha2))],
            1)
        alpha_2 += 1
        counter += 1
        if ination[max_index] == beta:
            beta_ -= 1
        elif ination[max_index] == theta:
            theta_ -= 1
        else:
            alpha_1 -= 1
    print(pass_,len(pass_))
    print("# theta: {}, # beta: {}, # alpha 1: {}, # alpha 2: {}".format(
        theta_,beta_,alpha_1,alpha_2))
    print("# steps to become Strong: {}".format(counter))
