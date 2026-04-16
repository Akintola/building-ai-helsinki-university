countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
populations = [5615000, 5439000, 324000, 5080000, 9609000]
male_fishers = [1822, 2575, 3400, 11291, 1731]
female_fishers = [69, 77, 400, 320, 26] 

def guess(winner_gender):
    fishers = female_fishers if winner_gender == 'female' else male_fishers
    
    probs = []
    for i in range(len(countries)):
        probs.append(fishers[i] / sum(fishers) * 100)

    max_index = probs.index(max(probs))

    guess = countries[max_index]
    biggest = probs[max_index]

    return (guess, biggest)  

def main():
    country, fraction = guess("male")
    print("if the winner is male, my guess is he's from %s; probability %.2f%%" % (country, fraction))
    country, fraction = guess("female")
    print("if the winner is female, my guess is she's from %s; probability %.2f%%" % (country, fraction))

main()