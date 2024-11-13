# File name: sphere.py

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm
from matplotlib.ticker import LinearLocator

def sphere(radius, center, color):
    # Plots a sphere with the given radius and center

    # Defining data
    phi = np.linspace(0, np.pi, 100)
    theta = np.linspace(0, 2 * np.pi, 100)
    phi, theta = np.meshgrid(phi, theta)
    x = center[0] + radius * np.sin(phi) * np.cos(theta)
    y = center[1] + radius * np.sin(phi) * np.sin(theta)
    z = center[2] + radius * np.cos(phi)

    # Plotting
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize = (10,10))
    plt.gca().set_aspect('equal')
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    ax.set_zlim(0, 100)
    ax.plot_surface(x, y, z, color=color)

    # Labelling
    plt.title("Sphere")
    ax.set_ylabel("Y values")
    ax.set_xlabel("X values")
    ax.set_zlabel("Z values")