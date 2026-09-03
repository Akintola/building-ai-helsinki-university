import numpy as np

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

def distance(line1, line2):
    if np.array_equal(np.asarray(line1), np.asarray(line2)):
        return np.inf
    else:
        return sum([abs(line1[i] - line2[i]) for i in range(len(line1))])

def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=float)

    for index, line1 in enumerate(data):
        dist[index] = [distance(line1, line2) for line2 in data]

    print(np.unravel_index(np.argmin(dist), dist.shape))

find_nearest_pair(data)