import math
from functions import *

epochs = 1000000
lr = 0.00001

points = [(0, 2), (4, 10), (2,8)]

a = 1
b = 1
c = 1


for i in range(epochs):
     a, b = update_values_linear(a, b, points, lr)
     
     
print(a, b)