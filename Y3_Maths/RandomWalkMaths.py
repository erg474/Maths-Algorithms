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
        dx, dy = np.random.randint(-stride, stride+1), np.random.randint(-stride, stride+1)
        w_x += dx
        w_y += dy
        #print(w_x, w_y)
        coord_list.append((w_x, w_y))
        count+=1
    return coord_list

def RandomWalk2(n):
    """Return coordinates after 'n' block random walk."""
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = (np.random.randint(-1, 2), np.random.randint(-1, 2))
        x += dx
        y += dy
    return(x, y)


testwalk='''
RW = RandomWalk(0, 0, 25, 1, 2)
print(zip(*RW))
x,y = zip(*RW)
plt.scatter(x, y, c=range(0, 25), cmap="hsv")
plt.plot(x, y)
plt.axvline(x=0, label="x=0")
plt.axhline(y=0, label="y=0")
plt.legend()

plt.show()'''

walk_length = 100

for i in range(100):
    RW = RandomWalk(0, 0, walk_length, 1, 2)
    # print(RW, "Distance from origin = ")
    # print(zip(*RW))
    x, y = zip(*RW)
    plt.scatter(x, y, c=range(0, walk_length), cmap="hsv")
    plt.plot(x, y)
    plt.axvline(x=0, label="x=0")
    plt.axhline(y=0, label="y=0")
#plt.show()

number_of_walks = 20000

# monte carlo method to find...
for walk_length in range(1, 31):
    no_travel = 0 # Number of walks 4 or fewer blocks from home
    for i in range(number_of_walks):
        (x,y) = RandomWalk2(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_travel+=1
        no_travel_percentage = float(no_travel / number_of_walks)
        if i == number_of_walks-1:
            print("Walk Size", walk_length,
                  " / % of no travel =  ", 100*no_travel_percentage)




#plt.scatter(x_vals, y_vals, c=counter, cmap="Greens_r")
#plt.show()

# Calculating properties of a Random Walk
# Number of Distinct Sites , S(t)
# Information Rate


# Gaussian Random Walk (this is used as model for a real-world time series such as financial markets)
# The Black-Scholes formula for modelling option prices uses a Gaussian random walk as an underlying assumption

print(np.random.randint(-1 , 1))