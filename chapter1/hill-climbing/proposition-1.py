import math
import random             	# just for generating random mountains                                 	 

# generate random mountains                                                                               	 

w = [.05, random.random()/3, random.random()/3]
h = [1.+math.sin(1+x/.6)*w[0]+math.sin(-.3+x/9.)*w[1]+math.sin(-.2+x/30.)*w[2] for x in range(100)]

def climb(x, h):
    # keep climbing until we've found a summit
    summit = False
    steps  = 5

    # edit here
    while not summit:
        summit = True # stop unless there's a way up
        for i in range(2 * steps):
            step = i - steps + 1
            if h[x + step] > h[x]:
                x = x + step      # right is higher, go there
                summit = False    # and keep going
                break
    return x

def main(h):
    # start at a random place                                                                                  	 
    x0 = random.randint(1, 98)
    x = climb(x0, h)

    return x0, x

main(h)