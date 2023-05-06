import math
from functions import *
from plot import plot_regression

epochs = 100000
lr = 0.0001

points = [(1, 3), (-4, 7), (5, -7)]

a = 1
b = 1
c = 1

for i in range(epochs):
    a, b, c = update_values_quadratic(a, b, c, points, lr)

regression_function, label = create_quadratic(a, b, c)

plot_regression(regression_function, points, label)