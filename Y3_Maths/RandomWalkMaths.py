# Not to be confused with the Financial Model for Random Walk, which I have used in the FinanncialTimeSeries repo.

import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

#need a 2d visualisation

# Random walk W_n (n>=0) = W_0 + X_1 + ... + X_n, X_1, X_2, ..., X_n are iid RVs


w_x, w_y = 0, 0       # First Point W_0
n = 15 #length of walk

for i in range(1, n):
    dx, dy = np.random.randint(-5,5), np.random.randint(-5,5)
    w_x += dx
    w_y += dy
    print(w_x, w_y)

def RandomWalk(origin, steps, stride, dimension): #assume dimension is 2 for now
    for i in range(0, n):
        dx, dy = np.rand(-stride, stride), np.rand(-stride, stride)
        w_x += dx
        w_y += dy
        print(w_x, w_y)

# Calculating properties of a Random Walk
# Number of Distinct Sites , S(t)
# Information Rate


# Gaussian Random Walk (this is used as model for a real-world time series such as financial markets)
# The Black-Scholes formula for modelling option prices uses a Gaussian random walk as an underlying assumption