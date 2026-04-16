portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
 
def permutations(route, ports):
    if len(ports) > 0:
        # Write your recursive code here
        for i, port in enumerate(ports):
            route = route + [port]
            permutations(route, ports[:i] + ports[i+1:])
            route.pop()
        
    if len(ports) < 1:
        print(' '.join([portnames[i] for i in route]))

# This will start the recursion with 0 ("PAN") as the first stop
permutations([0], list(range(1, len(portnames))))