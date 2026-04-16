import random

def main():
    probability = random.random()
    favourite = "dogs" if probability <= 0.8 else ("cats" if probability < 0.9 else "bats")
        
    print("I love " + favourite)



main()