countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
male_fishers = [1822, 2575, 3400, 11291, 1731]
female_fishers = [69, 77, 400, 320, 26]

def guess(winner_gender):
    fishers = female_fishers if winner_gender == 'female' else male_fishers
    total = sum(fishers)

    probs = [f / total * 100 for f in fishers]

    max_index = probs.index(max(probs))

    return countries[max_index], probs[max_index]

def main():
    country, fraction = guess("male")
    print("if the winner is male, my guess is he's from %s; probability %.2f%%" % (country, fraction))
    country, fraction = guess("female")
    print("if the winner is female, my guess is she's from %s; probability %.2f%%" % (country, fraction))

main()