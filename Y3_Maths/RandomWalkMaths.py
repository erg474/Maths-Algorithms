# Not to be confused with the Financial Model for Random Walk, which I have used in the FinanncialTimeSeries repo.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

#need a 2d visualisation

# Random walk W_n (n>=0) = W_0 + X_1 + ... + X_n, X_1, X_2, ..., X_n are iid RVs



def RandomWalk(origin_x, origin_y, steps, stride, dimension): #assume dimension is 2 for now
    w_x, w_y = origin_x, origin_y
    coord_list = []
    count=0
    for i in range(0, steps):
        dx, dy = np.random.randint(-stride, stride), np.random.randint(-stride, stride)
        w_x += dx
        w_y += dy
        print(w_x, w_y)
        coord_list.append((w_x, w_y))
        count+=1
    return coord_list

RW = RandomWalk(0, 0, 25, 1, 2)

print(zip(*RW))
x,y = zip(*RW)
plt.scatter(x, y, c=range(0, 25), cmap="hsv")
plt.plot(x, y)
plt.axvline(x=0, label="x=0")
plt.axhline(y=0, label="y=0")
plt.legend()

plt.show()


#plt.scatter(x_vals, y_vals, c=counter, cmap="Greens_r")
#plt.show()

# Calculating properties of a Random Walk
# Number of Distinct Sites , S(t)
# Information Rate


# Gaussian Random Walk (this is used as model for a real-world time series such as financial markets)
# The Black-Scholes formula for modelling option prices uses a Gaussian random walk as an underlying assumption