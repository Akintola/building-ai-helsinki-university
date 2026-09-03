import numpy as np
import random, math

N = 100     # size of the problem is N x N                                      
steps = 3000    # total number of iterations                                        
tracks = 50

# generate a landscape with multiple local optima                                          
def generator(x, y, x0=0.0, y0=0.0):
    return np.sin((x/N-x0)*np.pi)+np.sin((y/N-y0)*np.pi)+\
        .07*np.cos(12*(x/N-x0)*np.pi)+.07*np.cos(12*(y/N-y0)*np.pi)

x0 = np.random.random() - 0.5
y0 = np.random.random() - 0.5
h = np.fromfunction(np.vectorize(generator), (N, N), x0=x0, y0=y0, dtype=int)
peak_x, peak_y = np.unravel_index(np.argmax(h), h.shape)

# starting points                                                               
x = np.random.randint(0, N, tracks)
y = np.random.randint(0, N, tracks)

def treshold(S_old, S_new, T):
    return 1.0 if (S_new > S_old) else math.exp(-(S_old-S_new)/T)

def main():
    x = np.random.randint(0, N, tracks)
    y = np.random.randint(0, N, tracks)

    best_x, best_y = x.copy(), y.copy()
    best_scores = h[x, y].copy()

    T0 = 1.0
    alpha = 0.995

    for step in range(steps):
        T = T0 * (alpha ** step)

        step_size = int(max(1, T * N / 10))

        dx = np.random.randint(-step_size, step_size + 1, size=tracks)
        dy = np.random.randint(-step_size, step_size + 1, size=tracks)

        x_new = np.clip(x + dx, 0, N-1)
        y_new = np.clip(y + dy, 0, N-1)

        S_old = h[x, y]
        S_new = h[x_new, y_new]

        probs = np.exp((S_new - S_old) / T)
        accept = (S_new > S_old) | (np.random.rand(tracks) < probs)

        x[accept] = x_new[accept]
        y[accept] = y_new[accept]

        improved = S_new > best_scores
        best_x[improved] = x_new[improved]
        best_y[improved] = y_new[improved]
        best_scores[improved] = S_new[improved]

    print(sum((best_x == peak_x) & (best_y == peak_y)))