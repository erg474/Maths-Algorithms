# Note , pooling probably has more efficient and shorter functions as part of packages
# Types of pooling : Max Pooling (highest value is kept), Average Pooling

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps

def get_pools(img: np.array, pool_size: int, stride: int):
    pools = []
    for i in np.arange(img.shape[0], step=stride):
        for j in np.arange(img.shape[0], step=stride):

            # Extract the current pool
            mat = img[i:i + pool_size, j:j + pool_size]

            # Make sure it's rectangular - has the shape identical to the pool size
            if mat.shape == (pool_size, pool_size):
                # Append to the list of pools
                pools.append(mat)

            # Return all pools as a Numpy array
        return np.array(pools)

def max_pooling(pools: np.array):
    num_pools = pools.shape[0]
    # Shape of matrix after pooling = square root of the number of pools
    tgt_shape = (int(np.sqrt(num_pools)), int(np.sqrt(num_pools)))

    pooled = []  # to store max values
    for pool in pools:
        pool.append(np.max(pool))  # max pooling

    # Reshape to target shape
    return np.array(pooled).reshape(tgt_shape)


def plot_image(img: np.array):
    plt.figure(figsize=(6, 6))
    plt.imshow(img, cmap='gray');


def plot_two_images(img1: np.array, img2: np.array):
    _, ax = plt.subplots(1, 2, figsize=(12, 6))
    ax[0].imshow(img1, cmap='gray')
    ax[1].imshow(img2, cmap='gray');


conv_output = np.array([
    [10, 12,  8,  7],
    [ 4, 11,  5,  9],
    [18, 13,  7,  7],
    [ 3, 15,  2,  2]
])
print(conv_output)
print()

pool_size = 2
stride = 2

test_pools = get_pools(img = conv_output, pool_size=2, stride=2)
print(test_pools)
max_pooling(pools=test_pools)

# Image Pooling
img = Image.open("londonsquare.jpg")
img = ImageOps.grayscale(img)
img = img.resize(size=(224,224))
plot_image(img=img)