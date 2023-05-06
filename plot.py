import numpy as np
import matplotlib.pyplot as plt
from functions import *

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)



def plot_regression(f, points, label):
    bound = find_point_bounds(points)
    bound_diff = bound[1]-bound[0]
    t = np.arange(bound[0]-0.2*bound_diff, bound[1]+0.2*bound_diff, 0.02)
    plt.plot(t, f(t), label=label)
    plt.scatter(*zip(*points))
    plt.show()
