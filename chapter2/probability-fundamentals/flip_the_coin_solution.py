import numpy as np

N = 10000

def generate(p1, n=N):
    return np.random.choice([0, 1], size=n, p=[1 - p1, p1])

def count(seq):
    # sliding window for 5 consecutive 1s
    return np.sum(
        (seq[:-4] == 1) &
        (seq[1:-3] == 1) &
        (seq[2:-2] == 1) &
        (seq[3:-1] == 1) &
        (seq[4:] == 1)
    )

def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))