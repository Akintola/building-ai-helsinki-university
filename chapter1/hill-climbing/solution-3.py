import math, random

def accept_prob(S_old, S_new, T):
    if S_new > S_old:
        return 1.0
    else:
        return math.exp((S_new - S_old)/T) # Or analogously, math.exp(-(S_old - S_new)/T)

def accept(S_old, S_new, T):
    if math.random() < accept_prob(S_old, S_new, T):
        return True
    else:
        return False