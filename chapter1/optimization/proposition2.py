portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# https://sea-distances.org/
# nautical miles converted to km

D = [
        [0,8943,8019,3652,10545],
        [8943,0,2619,6317,2078],
        [8019,2619,0,5836,4939],
        [3652,6317,5836,0,7825],
        [10545,2078,4939,7825,0]
    ]

# https://timeforchange.org/co2-emissions-shipping-goods
# assume 20g per km per metric ton (of pineapples)

co2 = 0.020

smallest = 1000000
bestroute = [0, 0, 0, 0, 0]

def permutations(route, ports):
    global smallest, bestroute, co2

    if len(ports) < 1:
        distance = sum([ D[route[index]][route[index + 1]] for index, r in enumerate(route[:-1])])

        if distance < smallest:
            smallest = distance
            bestroute = route
            # print(' '.join([portnames[i] for i in route]))
    else:
        for i, port in enumerate(ports):
            permutations(route + [port], ports[:i] + ports[i+1:])

def main():
    permutations([0], list(range(1, len(portnames))))
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % (smallest * co2))

main()